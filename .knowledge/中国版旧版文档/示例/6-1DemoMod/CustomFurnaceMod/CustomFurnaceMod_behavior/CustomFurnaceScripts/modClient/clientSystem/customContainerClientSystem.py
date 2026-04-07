# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
from CustomFurnaceScripts.modCommon import modConfig
from mod_log import logger
from CustomFurnaceScripts.modClient.clientManager.containerUIMgr import UIMgr


class CustomContainerClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomContainerClientSystem, self).__init__(namespace, name)
        clientApi.SetUseEventTuple()
        self.mCustomFurnaceUINode = None
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mUIManager = UIMgr()
        self.ListenEvent()

    # 监听引擎和服务端脚本事件
    def ListenEvent(self):
        # 定义客户端自定义事件
        self.DefineEvent(modConfig.CloseCustomFurnaceEvent)
        self.DefineEvent(modConfig.OnItemSwapClientEvent)
        self.DefineEvent(modConfig.OnItemDropClientEvent)
        # 监听客户端引擎事件
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self.mUIManager, self.mUIManager.initAllUI)
        # 监听服务端自定义事件
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnCustomContainerChangedEvent, self, self.OnCustomContainerChanged)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnUIShouldCloseServerEvent, self, self.OnCustomContainerUIClose)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnBagChangedEvent, self, self.OnBagChanged)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OpenCustomContainerEvent, self, self.OpenCustomContainer)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnItemSwapServerEvent, self, self.OnItemSwap)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnItemDropServerEvent, self, self.OnItemDrop)

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        self.UnDefineEvent(modConfig.CloseCustomFurnaceEvent)
        self.UnDefineEvent(modConfig.OnItemSwapClientEvent)
        self.UnDefineEvent(modConfig.OnItemDropClientEvent)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self.mUIManager, self.mUIManager.initAllUI)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnCustomContainerChangedEvent, self, self.OnCustomContainerChanged)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnUIShouldCloseServerEvent, self, self.OnCustomContainerUIClose)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnBagChangedEvent, self, self.OnBagChanged)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OpenCustomContainerEvent, self, self.OpenCustomContainer)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnItemSwapServerEvent, self, self.OnItemSwap)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.OnItemDropServerEvent, self, self.OnItemDrop)

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        pass

    # 打开自定义熔炉UI并初始化
    def OpenCustomContainer(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.ShowUI(args)

    # 物品交换事件
    def OnItemSwap(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.SwapItem(args)

    # 物品丢弃事件
    def OnItemDrop(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.DropItem(args["slot"])

    # 背包发生变化的事件，需要更新背包UI
    def OnBagChanged(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.UpdateBagUI(args[modConfig.INVENTORY_BAG])

    # 自定义容器发生变化的事件，需要更新自定义容器的UI
    def OnCustomContainerChanged(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.UpdateCustomContainerUI(args)

    # 自定义容器对应的方块被摧毁或玩家死亡时，需要关闭UI
    def OnCustomContainerUIClose(self, args):
        blockName = args["blockName"]
        uiData = modConfig.UI_DEFS.get(blockName)
        if not uiData:
            logger.error("%s Has No UIData!!!" % blockName)
        uiNode = self.mUIManager.getUINode(uiData)
        uiNode.CloseUI()

    def GetPlayerId(self):
        return self.mPlayerId

    # 在清除该system的时候调用取消监听事件
    def Destroy(self):
        self.UnListenEvent()
