# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)
import logging
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class HziGachaChestBeh(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.uiNode = None
        self.ListenForEvent('HziGachaChest', 'HziGachaChestDev', 'ShowUI', self, self.ShowUI)
        self.ListenForEvent('HziGachaChest', 'HziGachaChestDev', 'RequestReturn', self, self.RequestReturn)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.OnUIInitFinished)
        self.menus = None

    def OnUIInitFinished(self, e):
        clientApi.RegisterUI('hziGachaChest', 'hziGachaChestMain', 'hziGachaChestScript.hziGachaChestUI.HziGachaChestUI', 'hzi_gachachest_main.main')
        uiNode = clientApi.CreateUI('hziGachaChest', 'hziGachaChestMain')
        if not uiNode:
            logging.error('[抽奖插件]创建UI失败')
        self.uiNode = uiNode
        menusSystem = clientApi.GetSystem('neteaseMenus', 'neteaseMenusBeh')
        if menusSystem:
            self.ListenForEvent('neteaseMenus', 'neteaseMenusBeh', 'MenusNavigateEvent', self, self.OnMenusNavigate)
            self.menus = menusSystem

    def ShowUI(self, data):
        if self.uiNode:
            self.uiNode.Show(data)

    def SendRequest(self, cardPoolIdentifier):
        """
        玩家点击抽奖按钮, 请求抽奖
        """
        data = self.CreateEventData()
        data['client'] = clientApi.GetLocalPlayerId()
        data['identifier'] = cardPoolIdentifier
        self.NotifyToServer('RequestGacha', data)

    def RequestReturn(self, e):
        """
        服务端抽奖请求返回
        :param e: e['slot'] 如果抽奖成功, 奖品卡槽
        :param e: e['notHide'] 不关闭面板并重置按钮状态
        :return:
        """
        if not self.uiNode:
            return
        if 'slot' in e:
            self.uiNode.PlayAnimation(e['slot'])
        else:
            if 'notHide' in e and e['notHide']:
                self.uiNode.SetStartButtonStatus(True)
            else:
                self.uiNode.Hide(None)
            logging.warning('[抽奖插件]请求抽奖失败: {}'.format(e['msg']))

    def AnimationStop(self):
        """
        跑马灯动画播放完成, 回到大厅
        服务端要收到这个事件才会发放奖品, 广播事件, 更新数据库
        """
        data = self.CreateEventData()
        data['client'] = clientApi.GetLocalPlayerId()
        self.NotifyToServer('AnimationStop', data)

    def OnMenusNavigate(self, e):
        """
        如果菜单插件被装载, 询问服务端点击的按钮名称是否触发抽奖界面
        """
        if self.menus.GetMenus() and 'menusConfig' in self.menus.GetMenus():
            data = self.CreateEventData()
            data['client'] = clientApi.GetLocalPlayerId()
            data['name'] = self.menus.GetMenus()['menusConfig'][e['order']]['name']
            self.NotifyToServer('OnMenusNavigate', data)