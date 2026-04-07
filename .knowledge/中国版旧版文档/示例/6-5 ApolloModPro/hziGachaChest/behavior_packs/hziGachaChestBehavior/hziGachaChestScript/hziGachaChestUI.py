# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)
import logging
import random
from copy import deepcopy
import mod.client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()
class HziGachaChestUI(ScreenNode):
    def __init__(self, namespace, name, param):
        super(HziGachaChestUI, self).__init__(namespace, name, param)
        self.gridPath = '/gacha_panel/left_panel/inside_panel/bg/grid'
        self.closeBtnPath = '/gacha_panel/right_panel/close_bg/close_button'
        self.startBtnPath = '/gacha_panel/right_panel/start_button'
        self.rightTitlePath = '/gacha_panel/right_panel/title'
        self.leftTitlePath = '/gacha_panel/left_panel/title'
        self.startButtonMsgPath = '/gacha_panel/right_panel/start_button/msg'
        self.displayImgPath = '/gacha_panel/right_panel/display_frame/display_img'
        self.currencyIconPath = '/gacha_panel/right_panel/start_button/msg/icon'
        self.renderControls = {}
        self.prizeSlotList = [] # 定义跑马灯顺序
        self.resultSlot = None # 抽奖结果
        self.roundIndex = None # 跑马灯prizeSlotList的实时index
        self.roundTick = None
        self.roundSpeed = None
        self.waitingForRender = None
        self.cardPoolIdentifier = None
        self.greetingsMsg = None
        self.startMsg = None
        self.selectedAudioName = None
        self.winAudioName = None
        self.centerSlot = None
        self.speedStepSize = None
        self.maxRoundSpeed = None
        self.tryStopSpeed = None
        self.animationStopStayTime = None
        self.animationStopClose = None
        self.cacheData = None
        self.timer = None
        self.status = UIStatus.Hide
        self.audioComp = clientApi.GetEngineCompFactory().CreateCustomAudio(clientApi.GetLevelId())

    def Show(self, data):
        if self.status == UIStatus.Show:
            self.Hide(None)
        elif self.status == UIStatus.PlayingAnimation:
            return
        """
        第一次 Show 的时候 Gird 可能没有渲染完成, 若没有渲染完成写入缓存等 Update 触发 LoadRenderControl
        """
        if not self.renderControls:
            self.waitingForRender = data
        else:
            self.LoadRenderControl(data)
        self.SetScreenVisible(True)
        self.SetIsHud(0)
        self.status = UIStatus.Show

    def Hide(self, e):
        if self.status == UIStatus.PlayingAnimation:
            return
        self.SetScreenVisible(False)
        self.SetIsHud(1)
        self.status = UIStatus.Hide
        """
        释放上次奖池的缓存数据
        """
        for control in self.renderControls.values():
            control.SetSelected(False)
        if not self.timer is None:
            game = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            game.CancelTimer(self.timer)
            self.timer = None
        self.renderControls.clear()
        self.prizeSlotList = []
        self.waitingForRender = None
        self.cardPoolIdentifier = None
        self.greetingsMsg = None
        self.startMsg = None
        self.resultSlot = None
        self.roundIndex = None
        self.roundTick = None
        self.roundSpeed = None
        self.winAudioName = None
        self.selectedAudioName = None
        self.centerSlot = None
        self.speedStepSize = None
        self.maxRoundSpeed = None
        self.tryStopSpeed = None
        self.animationStopStayTime = None
        self.cacheData = None
        self.animationStopClose = None

    def LoadRenderControl(self, data):
        """
        将服务端传过来的奖池数据渲染到控件上
        """
        self.cardPoolIdentifier = data['identifier']
        self.greetingsMsg = data['greetingsMsg'].replace('&', '§')
        self.startMsg = data['startMsg'].replace('&', '§')
        self.winAudioName = data['winAudioName']
        self.selectedAudioName = data['selectedAudioName']
        self.centerSlot = data['centerSlot']
        self.speedStepSize = data['speedStepSize']
        self.maxRoundSpeed = data['maxRoundSpeed']
        self.tryStopSpeed = data['tryStopSpeed']
        self.animationStopStayTime = data['animationStopStayTime']
        self.animationStopClose = data['animationStopClose']
        self.cacheData = data
        self.SetStartButtonStatus(True)
        self.GetBaseUIControl(self.rightTitlePath).asLabel().SetText(data['rightTitle'].replace('&', '§'))
        self.GetBaseUIControl(self.leftTitlePath).asLabel().SetText(data['leftTitle'].replace('&', '§'))
        self.GetBaseUIControl(self.startButtonMsgPath).asLabel().SetText(data['startMsg'].replace('&', '§'))
        self.GetBaseUIControl(self.displayImgPath).asImage().SetSprite(data['displayFrame'])
        self.GetBaseUIControl(self.currencyIconPath).asImage().SetSprite(data['currencyIcon'])
        if 'gridDimension' in data and data['gridDimension']:
            dimension = tuple(map(int, str(data['gridDimension']).split('x')))
        else:
            dimension = (5, 5)
        self.GetBaseUIControl(self.gridPath).asGrid().SetGridDimension(dimension)
        if data['centerSlot'] in self.renderControls:
            if not data['centerSlot'] in self.renderControls:
                logging.error('[抽奖插件]请检查 mod.json, slot:{} 的槽位不存在或渲染失败!'.format(data['centerSlot']))
                return
            control = self.renderControls.get(data['centerSlot']) # type: ItemRenderControl
            control.SetType(ItemRenderType.Center)
            control.SetRenderItem(data['centerDefault'])
        equal2 = len(data['adornmentSlot']) == len(data['adornmentItem'])
        for index, slot in enumerate(data['adornmentSlot']):
            if not slot in self.renderControls:
                logging.error('[抽奖插件]请检查 mod.json, slot:{} 的槽位不存在或渲染失败!'.format(slot))
                return
            control = self.renderControls.get(slot)  # type: ItemRenderControl
            control.SetType(ItemRenderType.Adornment)
            """
            如果槽位和物品数量对等就按照顺序放置, 否则随机抽取
            """
            control.SetRenderItem(data['adornmentItem'][index] if equal2 else random.choice(data['adornmentItem']))
        for prize in data['prizeList']:
            if not prize['slot'] in self.renderControls:
                logging.error('[抽奖插件]请检查 mod.json, slot:{} 的槽位不存在或渲染失败!'.format(prize['slot']))
                return
            self.prizeSlotList.append(prize['slot'])
            control = self.renderControls.get(prize['slot'])  # type: ItemRenderControl
            control.SetType(ItemRenderType.Prize)
            control.SetRenderItem(prize)

    def SetStartButtonStatus(self, canTouch):
        """
        设置启动抽奖按钮状态
        """
        startBtn = self.GetBaseUIControl(self.startBtnPath).asButton()
        startBtn.GetChildByName('default').asImage().SetSprite('textures/ui/hzi_gachachest/btn_{}'.format('default' if canTouch else 'unuse'))
        startBtn.SetTouchEnable(canTouch)
        self.GetBaseUIControl(self.startButtonMsgPath).asLabel().SetText(self.startMsg if canTouch else self.greetingsMsg)
        self.GetBaseUIControl(self.currencyIconPath).SetVisible(canTouch)

    def Create(self):
        self.GetBaseUIControl('/gacha_panel').SetLayer(clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1, True, True)
        closeBtn = self.GetBaseUIControl(self.closeBtnPath).asButton()
        closeBtn.AddTouchEventParams({'isSwallow': True})
        closeBtn.SetButtonTouchUpCallback(self.Hide)
        startBtn = self.GetBaseUIControl(self.startBtnPath).asButton()
        startBtn.AddTouchEventParams({'isSwallow': True})
        startBtn.SetButtonTouchUpCallback(self.StartButtonTouchUp)
        self.Hide(None)

    def StartButtonTouchUp(self, e):
        """
        玩家点击抽奖按钮, 此时 client 向服务端请求抽卡
        """
        self.SetStartButtonStatus(False)
        system = clientApi.GetSystem('HziGachaChest', 'HziGachaChestBeh')
        system.SendRequest(self.cardPoolIdentifier)

    def PlayAnimation(self, slot):
        """
        服务端返回抽奖结果, 开始播放动画
        :param slot: 抽中物品所在槽位
        """
        self.resultSlot = slot
        self.status = UIStatus.PlayingAnimation
        self.roundIndex = 0
        self.roundTick = 0
        self.roundSpeed = 1

    def Update(self):
        if not self.renderControls:
            """
            初始化渲染器, 此处在第一次 Show 界面才会触发
            """
            pathList = self.GetAllChildrenPath(self.gridPath)
            if pathList:
                for path in pathList:
                    # 筛除按钮的下级节点
                    if not '/' in path.replace(self.gridPath + '/', ''):
                        slot = int(path.split('/')[-1].replace('item_btn', ''))
                        self.renderControls[slot] = ItemRenderControl(path, self)
                if self.waitingForRender:
                    self.LoadRenderControl(self.waitingForRender)
        else:
            for control in self.renderControls.values():
                control.Update()
            """
            跑马灯动画处理
            """
            if self.status == UIStatus.PlayingAnimation:
                if self.roundTick <= 0:
                    if self.roundSpeed < self.maxRoundSpeed:
                        self.roundSpeed += self.speedStepSize
                    self.roundTick = self.roundSpeed
                    if self.roundIndex == len(self.prizeSlotList) - 1:
                        self.roundIndex = 0
                    else:
                        self.roundIndex += 1
                    if self.roundSpeed >= self.tryStopSpeed and self.prizeSlotList[self.roundIndex] == self.resultSlot:
                        """
                        抽中物品, 动画结束
                        """
                        self.status = UIStatus.Show
                        self.audioComp.PlayCustomMusic(self.winAudioName, (0, 0, 0), 1, 1, False, clientApi.GetLocalPlayerId())
                        if self.animationStopStayTime <= 0:
                            self.AnimationStop()
                        else:
                            game = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
                            self.timer = game.AddTimer(self.animationStopStayTime, self.AnimationStop)
                    now = self.renderControls[self.prizeSlotList[self.roundIndex]]
                    center = self.renderControls[self.centerSlot]
                    item = deepcopy(now.GetRenderItem())
                    """
                    不管物品是否支援此 enchantData
                    只要有就会被渲染器判定为带附魔
                    当然发放物品的时候必须要使用正确的 enchantData 或强制的 userData
                    """
                    item['enchantData'] = [(1, 1)]
                    center.SetRenderItem(item, animation=True)
                    last = self.renderControls[self.prizeSlotList[self.roundIndex - 1]]
                    last.SetSelected(False)
                    now.SetSelected(True)
                else:
                    self.roundTick -= 1

    def AnimationStop(self):
        system = clientApi.GetSystem('HziGachaChest', 'HziGachaChestBeh')
        system.AnimationStop()
        if self.animationStopClose:
            self.Hide(None)
        else:
            """
            若此卡池抽完不关闭, 则重置状态并重新渲染
            """
            for control in self.renderControls.values():
                control.SetSelected(False)
            if not self.timer is None:
                game = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
                game.CancelTimer(self.timer)
                self.timer = None
            self.LoadRenderControl(self.cacheData)

class ItemRenderControl(object):

    def __init__(self, path, uiNode):
        self.uiNode = uiNode # type: HziGachaChestUI
        self.itemDict = None
        self.buttonPath = path
        self.buttonControl = self.uiNode.GetBaseUIControl(path).asButton()
        self.buttonControl.AddTouchEventParams({'isSwallow': True})
        self.buttonControl.SetButtonTouchUpCallback(self.TouchUp)
        self.borderVisible = False
        self.borderAlpha = 0.0
        self.borderStayTime = 0.63
        self.borderControl = self.buttonControl.GetChildByName('item_name_bg')
        self.borderControl.SetAlpha(self.borderAlpha)
        self.type = None
        self.timer = None

    def GetRenderItem(self):
        return self.itemDict

    def SetRenderItem(self, itemDict, animation=False):
        """
        物品渲染逻辑
        """
        self.itemDict = itemDict
        itemName = itemDict['newItemName'] if 'newItemName' in itemDict else itemDict['itemName']
        auxValue = itemDict['newAuxValue'] if 'newAuxValue' in itemDict else itemDict['auxValue']
        isEnchanted = 'enchantData' in itemDict and itemDict['enchantData']
        userData = itemDict['userData'] if 'userData' in itemDict else None
        if 'count' in itemDict and itemDict['count'] > 1:
            self.buttonControl.GetChildByPath('/item_render/item_num').asLabel().SetText(str(itemDict['count']))
            self.buttonControl.GetChildByPath('/item_render/item_num').SetVisible(True)
        else:
            self.buttonControl.GetChildByPath('/item_render/item_num').SetVisible(False)
        result = self.uiNode.SetUiItem(self.buttonPath + '/item_render', itemName, auxValue, isEnchanted, userData)
        if not result:
            print logging.error('[抽奖插件]槽位物品渲染失败:' + self.buttonPath)
        """
        自定义tips, 播放跑马灯动画时不处理以节省性能
        """
        if animation:
            return
        comp = clientApi.GetEngineCompFactory().CreateItem(clientApi.GetLevelId())
        info = comp.GetItemBasicInfo(itemName, auxValue, isEnchanted)
        customTips = str(itemDict['showTips']).replace('&', '§') if 'showTips' in itemDict else info['itemName']
        lines = str(customTips).replace('§', '').split('\n')
        lineCount = len(lines) - 1
        longestLine = max(len(line) for line in lines)
        self.borderControl.SetSize((6.3 + longestLine * 3, 19 + lineCount * 8))
        label = self.borderControl.GetChildByName('item_name').asLabel()
        label.SetPosition((5, 4))
        label.SetText(customTips)
        if 'borderStayTime' in itemDict:
            self.borderStayTime = itemDict['borderStayTime']

    def SetSelected(self, selected):
        if selected:
            self.uiNode.audioComp.PlayCustomMusic(self.uiNode.selectedAudioName, (0, 0, 0), 1, 1, False, clientApi.GetLocalPlayerId())
        control = self.buttonControl.GetChildByName('selected_img')
        if control:
            control.SetVisible(selected)

    def SetType(self, renderType):
        self.type = renderType

    def SetSize(self, size):
        self.buttonControl.SetSize(size, resizeChildren=True)

    def Update(self):
        if not self.borderVisible and self.borderAlpha > 0:
            self.borderAlpha -= 1 / 30.0
            self.borderControl.SetAlpha(self.borderAlpha)

    def TouchUp(self, e):
        if self.type == ItemRenderType.Prize and self.uiNode.status != UIStatus.PlayingAnimation:
            self.borderAlpha = 1.0
            self.borderControl.SetAlpha(self.borderAlpha)
            self.borderVisible = True
            game = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            if self.timer:
                game.CancelTimer(self.timer)
            self.timer = game.AddTimer(self.borderStayTime, self.HideBorder)

    def HideBorder(self):
        self.borderVisible = False
        self.timer = None


class UIStatus(object):
    Show = 0
    Hide = 1
    PlayingAnimation = 2

class ItemRenderType(object):
    Center = 0
    Adornment = 1
    Prize = 2