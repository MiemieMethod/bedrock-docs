# -*- coding: utf-8 -*-

import time
from mod_log import logger
from CustomFurnaceScripts.modCommon import modConfig
from CustomFurnaceScripts.modClient.clientUtils import apiUtil

import mod.client.extraClientApi as clientApi

from mod.client.ui.screenNode import ScreenNode
from mod.client.ui.screenController import ViewBinder, ViewRequest
from CustomFurnaceScripts.modClient.clientUtils.containerInteractionStateMachine import ContainerInteractionStateMachine, NodeId, ButtonEventType
from CustomFurnaceScripts.modClient.ui.flyImage import FlyImage
from CustomFurnaceScripts.modCommon.modCommonUtils import itemUtils

compFactory = clientApi.GetEngineCompFactory()

class CustomContainerUIScreenBase(ScreenNode):

    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.mMainPanelPath = "/customContainerPanel"
        self.mDropAreaPath = self.mMainPanelPath + "/dropArea"
        self.mProgressiveBarPath = self.mMainPanelPath + "/progressiveBar"
        self.mItemDetailPanelPath = self.mMainPanelPath + "/itemDetail"
        self.mItemDetailTextPath = self.mItemDetailPanelPath + "/itemDetailBg/itemDetailText"
        self.mHeaderContentPath = self.mMainPanelPath + "/headerContentStackPanel"
        self.mContentPanelPath = self.mHeaderContentPath + "/contentPanel"
        self.mFlyImgTemplatePath = self.mContentPanelPath + "/flyImgTemplate"
        self.mLeftPanelPath = self.mContentPanelPath + "/leftPanel"
        self.mBagGridPath = self.mLeftPanelPath + "/bagContent/scrollingPanel/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
        self.mRightPanelPath = self.mContentPanelPath + "/rightPanel"
        self.mItemBtnPathPrefix = self.mBagGridPath + "/itemBtn"
        self.mCloseBtnPath = self.mHeaderContentPath + "/header/closeBtn"
        self.mIsHide = False
        self.mLastSelectedPath = None
        # 管理背包数据及各个槽位对应的路径
        self.mBagInfo = {}
        self.mSlotToPath = {}
        self.mBlockPos = None
        self.mDimension = None
        self.mBlockName = None
        # 管理飞行动画相关数据
        self.mFlyImgPool = []
        self.mFlyImgIndex = 0
        self.mFlyAnimationTime = 0
        # 用于渐变显示物品详细信息
        self.mDetailAlpha = 0.0
        self.mContainerStateMachine = ContainerInteractionStateMachine()
        self.mAlreadyRegisterEvent = False
        self.RegisterStateMachine()
        # 用于判断点击事件
        self.mClickInterval = 0
        self.mHeldTime = None
        self.mLastTouchButton = None
        self.mLastTouchPosition = None
        self.mIsDoubleClick = False
        self.mTakePercent = 1

    def RegisterButtonEvents(self):
        if self.mAlreadyRegisterEvent:
            return
        self.mAlreadyRegisterEvent = True
        for path in self.mBagInfo.keys():
            self.AddTouchEventHandler(path, self.OnButtonTouch, {"isSwallow": True})
        self.AddTouchEventHandler(self.mCloseBtnPath, self.OnCloseClick, {"isSwallow": True})
        self.AddTouchEventHandler(self.mDropAreaPath, self.OnDropClick, {"isSwallow": True})

    def UpdateBagUI(self, args):
        # 更新背包UI
        bagGridList = self.GetChildrenName(self.mBagGridPath)
        if not bagGridList:
            # PC版touch模式和鼠标模式scroll的路径不一致。。。
            self.mBagGridPath = self.mLeftPanelPath + "/bagContent/scrollingPanel/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
            self.mItemBtnPathPrefix = self.mBagGridPath + "/itemBtn"
            bagGridList = self.GetChildrenName(self.mBagGridPath)
            if not bagGridList:
                logger.error("Get Bag Grid List Error!!!")
                self.OnCloseClick(None)
                return
        i = 0
        for bagGridChild in bagGridList:
            bagGridChildPath = self.mBagGridPath + "/" + bagGridChild
            itemDict = args[i]
            self.mBagInfo[bagGridChildPath] = {"slot": i, "item": itemDict}
            self.mSlotToPath[i] = bagGridChildPath
            i += 1
            self.SetSlotUI(bagGridChildPath, itemDict)
        self.RegisterButtonEvents()

    @ViewBinder.binding(ViewBinder.BF_BindFloat, "#itemDetailAlpha")
    def OnDetailShow(self):
        if self.mDetailAlpha > 1:
            return 1.0
        return self.mDetailAlpha

    def ShowItemDetail(self, item):
        itemComp = compFactory.CreateItem(clientApi.GetLevelId())
        detailText = itemComp.GetItemFormattedHoverText(item["itemName"], item["auxValue"], True, item.get("userData"))
        self.SetText(self.mItemDetailTextPath, detailText)
        self.mDetailAlpha = 2.0

    def InitScreen(self):
        self.HideUI()

    def InitCustomContainerUI(self, args):
        """初始化自定义容器的UI，由子类覆写"""
        pass

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        # 更新长按分堆
        if self.mHeldTime is not None:
            self.mHeldTime += 1
            if self.mHeldTime == 10:
                self.mContainerStateMachine.ReceiveEvent(self.mLastTouchButton, ButtonEventType.Pressed)
            if self.mContainerStateMachine.GetCurrentNodeId() == NodeId.TouchProgressiveSelect:
                self.SetProgressiveBar()
        if self.mClickInterval > 0:
            self.mClickInterval -= 1
        # 更新物品详细信息透明度
        if self.mDetailAlpha > 0:
            self.mDetailAlpha -= 0.04
        # 更新飞行动画
        if self.mFlyAnimationTime > 0:
            self.mFlyAnimationTime -= 1
            for flyImg in self.mFlyImgPool:
                if flyImg.IsUsing():
                    self.SetPosition(flyImg.GetPath(), flyImg.UpdateCurPosition())
                    if self.mFlyAnimationTime == 0:
                        flyImg.Release()
                        self.SetVisible(flyImg.GetPath(), False)

    def OnButtonTouch(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]
        touchPos = args["TouchPosX"], args["TouchPosY"]
        #触控在按钮范围内弹起时
        if touchEvent == touchEventEnum.TouchUp:
            if self.mIsDoubleClick:
                self.mContainerStateMachine.ReceiveEvent(args["ButtonPath"], ButtonEventType.DoubleClick)
            elif self.mHeldTime and self.mHeldTime < 10:
                self.mContainerStateMachine.ReceiveEvent(args["ButtonPath"], ButtonEventType.Clicked)
            else:
                self.mContainerStateMachine.ReceiveEvent(args["ButtonPath"], ButtonEventType.Released)
            self.mHeldTime = None
            self.mClickInterval = modConfig.DOUBLE_CLICK_INTERVAL
        #按钮按下时
        elif touchEvent == touchEventEnum.TouchDown:
            item = self.GetItemByPath(args["ButtonPath"])
            if item:
                self.ShowItemDetail(item)
            if self.mClickInterval > 0 and self.mLastTouchButton == args["ButtonPath"]:
                self.mIsDoubleClick = True
                return
            self.mIsDoubleClick = False
            self.mHeldTime = 0
            self.mLastTouchButton = args["ButtonPath"]
            self.mLastTouchPosition = touchPos
        #触控在按钮范围外弹起时
        elif touchEvent == touchEventEnum.TouchCancel:
            self.mHeldTime = None
            self.OnTouchCancel()
        #按下后触控移动时
        elif touchEvent == touchEventEnum.TouchMove:
            self.OnTouchCancel()
        elif touchEvent == touchEventEnum.TouchMoveIn:
            pass
        elif touchEvent == touchEventEnum.TouchMoveOut:
            self.mHeldTime = None
            self.mContainerStateMachine.ReceiveEvent(self.mLastTouchButton, ButtonEventType.Released)

    def OnTouchCancel(self):
        self.mContainerStateMachine.ReceiveEvent(None, ButtonEventType.Released)

    def HandleIdle(self, buttonPath):
        self.mClickInterval = 0
        self.mHeldTime = None
        self.mLastTouchButton = None
        self.mIsDoubleClick = False
        self.mTakePercent = 1
        self.SetVisible(self.mProgressiveBarPath, False)
        if self.mLastSelectedPath:
            self.SetVisible(self.mLastSelectedPath + "/selectedImg", False)
            self.mLastSelectedPath = None

    def HandleSelected(self, buttonPath):
        self.mLastSelectedPath = buttonPath
        self.SetVisible(self.mLastSelectedPath + "/selectedImg", True)

    def HandleUnSelected(self, buttonPath):
        self.mContainerStateMachine.ResetToDefaut()

    def HandleSwap(self, buttonPath):
        if not self.mLastSelectedPath:
            logger.error("there is no last selected button, swap failed!!!")
            return
        swapData = apiUtil.GetModClientSystem().CreateEventData()
        swapData["blockName"] = self.mBlockName
        swapData["fromSlot"] = self.GetSlotByPath(self.mLastSelectedPath)
        swapData["toSlot"] = self.GetSlotByPath(buttonPath)
        swapData["playerId"] = apiUtil.GetModClientSystem().GetPlayerId()
        swapData["fromItem"] = self.GetItemByPath(self.mLastSelectedPath)
        swapData["toItem"] = self.GetItemByPath(buttonPath)
        swapData["blockPos"] = self.mBlockPos
        swapData["dimension"] = self.mDimension
        swapData["takePercent"] = self.mTakePercent
        apiUtil.GetModClientSystem().NotifyToServer(modConfig.OnItemSwapClientEvent, swapData)
        self.mContainerStateMachine.ResetToDefaut()

    def HandleDropAll(self, buttonPath):
        if not self.mLastSelectedPath:
            logger.error("there is no last selected button, drop failed!!!")
            return
        dropData = apiUtil.GetModClientSystem().CreateEventData()
        dropData["blockName"] = self.mBlockName
        dropData["playerId"] = apiUtil.GetModClientSystem().GetPlayerId()
        dropData["blockPos"] = self.mBlockPos
        dropData["dimension"] = self.mDimension
        dropData["slot"] = self.GetSlotByPath(self.mLastSelectedPath)
        dropData["item"] = self.GetItemByPath(self.mLastSelectedPath)
        apiUtil.GetModClientSystem().NotifyToServer(modConfig.OnItemDropClientEvent, dropData)
        self.mContainerStateMachine.ResetToDefaut()

    def HandleTouchProgressiveSelect(self, buttonPath):
        self.HandleSelected(buttonPath)
        self.SetPosition(self.mProgressiveBarPath, (self.mLastTouchPosition[0] - 8, self.mLastTouchPosition[1] - 4))
        self.SetVisible(self.mProgressiveBarPath, True)

    def HandleTouchProgressiveComplete(self, buttonPath):
        self.mHeldTime = None

    def HandleTouchProgressiveCancel(self, buttonPath):
        self.mContainerStateMachine.ResetToDefaut()

    def HandleCoalesce(self, buttonPath):
        if isinstance(self.GetSlotByPath(buttonPath), str):
            # 非背包栏位禁止合堆
            self.mContainerStateMachine.ResetToDefaut()
        itemDict = self.GetItemByPath(buttonPath)
        itemComp = compFactory.CreateItem(clientApi.GetLevelId())
        basicInfo = itemComp.GetItemBasicInfo(itemDict.get("itemName", ""), itemDict.get("auxValue", 0))
        if basicInfo:
            maxStackSize = basicInfo.get("maxStackSize")
            if maxStackSize > 1 and itemDict.get("count") != maxStackSize:
                for path, bagInfo in self.mBagInfo.items():
                    if buttonPath == path or isinstance(self.GetSlotByPath(path), str):
                        continue
                    item = self.GetItemByPath(path)
                    if itemUtils.IsSameItem(item, itemDict) and item.get("count") != maxStackSize:
                        self.mLastSelectedPath = path
                        self.HandleSwap(buttonPath)
        self.SetVisible(buttonPath + "/selectedImg", False)
        self.mContainerStateMachine.ResetToDefaut()

    def OnCloseClick(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]
        if touchEvent == touchEventEnum.TouchDown:
            eventData = apiUtil.GetModClientSystem().CreateEventData()
            eventData["playerId"] = apiUtil.GetModClientSystem().GetPlayerId()
            apiUtil.GetModClientSystem().NotifyToServer(modConfig.CloseCustomFurnaceEvent, eventData)
            gameComp = compFactory.CreateGame(clientApi.GetLevelId())
            # 延迟0.1秒帧执行，防止刚关闭又触发使用再次打开界面
            gameComp.AddTimer(0.1, self.CloseUI)

    def OnDropClick(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]
        if touchEvent == touchEventEnum.TouchDown:
            self.mContainerStateMachine.ReceiveEvent(args["ButtonPath"], ButtonEventType.Clicked)

    def CloseUI(self):
        self.HideUI()

    def GetBagItemPosition(self, itemPath):
        """计算背包控件相对于ContentPanel的位置，用于飞行动画"""
        pos1 = self.GetPosition(self.mLeftPanelPath)
        pos2 = self.GetPosition(self.mLeftPanelPath + "/bagContent")
        pos3 = self.GetPosition(itemPath)
        return (pos1[0] + pos2[0] + pos3[0] + 2, pos1[1] + pos2[1] + pos3[1] + 2)

    def GetRightPanelItemPosition(self, itemPath):
        """计算RightPanel控件相对于ContentPanel的位置，用于飞行动画"""
        pos1 = self.GetPosition(self.mRightPanelPath)
        pos2 = self.GetPosition(itemPath)
        return (pos1[0] + pos2[0] + 4, pos1[1] + pos2[1] + 4)

    def IsRightPanel(self, path):
        """判断是否为RightPanel子控件"""
        if path.startswith(self.mRightPanelPath):
            return True
        return False

    def GetItemPosition(self, itemPath):
        if self.IsRightPanel(itemPath):
            return self.GetRightPanelItemPosition(itemPath)
        return self.GetBagItemPosition(itemPath)

    def SetItemAtPath(self, itemPath, item):
        self.mBagInfo[itemPath]["item"] = item

    def GetItemByPath(self, itemPath):
        return self.mBagInfo[itemPath]["item"]

    def GetSlotByPath(self, path):
        return self.mBagInfo[path]["slot"]

    # 丢弃物品
    def DropItem(self, slot):
        dropPath = self.mSlotToPath[slot]
        self.SetSlotUI(dropPath, None)
        self.SetItemAtPath(dropPath, None)

    # 交换物品
    def SwapItem(self, args):
        fromSlot = args["fromSlot"]
        toSlot = args["toSlot"]
        fromPath = self.mSlotToPath[fromSlot]
        toPath = self.mSlotToPath[toSlot]
        fromItem = args["fromItem"]
        toItem = args["toItem"]

        # 更新飞行动画
        self.mFlyAnimationTime = modConfig.FLY_ANIMATION_DURATION
        fromPosition = self.GetItemPosition(fromPath)
        toPosition = self.GetItemPosition(toPath)

        flyImageFrom = self.GetFlyImg()
        flyImageFrom.InitPosition(fromPosition, toPosition)
        self.SetUiItem(flyImageFrom.GetPath(), fromItem["itemName"], fromItem["auxValue"], fromItem.get("enchantData", False), fromItem.get("userData"))
        self.SetPosition(flyImageFrom.GetPath(), fromPosition)
        self.SetVisible(flyImageFrom.GetPath(), True)

        if toItem and not itemUtils.IsSameItem(fromItem, toItem):
            flyImageTo = self.GetFlyImg()
            flyImageTo.InitPosition(toPosition, fromPosition)
            self.SetUiItem(flyImageTo.GetPath(), toItem["itemName"], toItem["auxValue"], toItem.get("enchantData", False), toItem.get("userData"))
            self.SetPosition(flyImageTo.GetPath(), toPosition)
            self.SetVisible(flyImageTo.GetPath(), True)

        self.SwapItemUI(fromPath, toPath, fromItem, toItem)
        self.SetItemAtPath(fromPath, toItem)
        self.SetItemAtPath(toPath, fromItem)

    def SwapItemUI(self, fromPath, toPath, fromItem, toItem):
        self.SetSlotUI(fromPath, toItem)
        self.SetSlotUI(toPath, fromItem)

    def SetSlotUI(self, path, item):
        """设置目标槽位item渲染"""
        if item and item.get("count"):
            # 设置耐久
            self.SetDurabilityBar(path, item)
            # 设值附魔
            isEnchant = False
            if item.get("enchantData"):
                isEnchant = True
            userData = item.get("userData")
            self.SetUiItem(path + "/itemImg", item["itemName"], item["auxValue"], isEnchant, userData)
            self.SetVisible(path + "/itemImg", True)
            if item["count"] > 1:
                self.SetText(path + "/itemImg/itemNum", str(item["count"]))
            else:
                self.SetText(path + "/itemImg/itemNum", "")
        else:
            self.SetVisible(path + "/itemImg", False)
            self.SetVisible(path + "/durabilityBar", False)

    def SetDurabilityBar(self, path, item):
        """设置目标槽位耐久度UI"""
        durabilityRatio = self.CaculateDurabilityRatio(item)
        if durabilityRatio != 1:
            barPath = path + "/durabilityBar/barMask"
            self.SetSpriteColor(barPath, (1 - durabilityRatio, durabilityRatio, 0))
            self.SetSpriteClipRatio(barPath, 1 - durabilityRatio)
            self.SetVisible(path + "/durabilityBar", True)
        else:
            self.SetVisible(path + "/durabilityBar", False)

    def CaculateDurabilityRatio(self, itemDict):
        """计算耐久度比例，用于显示耐久度槽"""
        itemComp = compFactory.CreateItem(clientApi.GetLevelId())
        basicInfo = itemComp.GetItemBasicInfo(itemDict.get("itemName", ""), itemDict.get("auxValue", 0))
        if basicInfo:
            currentDurability = itemDict.get("durability")
            if currentDurability is None:
                return 1
            maxDurability = basicInfo.get("maxDurability", 0)
            if maxDurability != 0:
                return currentDurability * 1.0 / maxDurability
        return 1

    def SetProgressiveBar(self):
        """设置长按分堆进度条"""
        if not self.mLastTouchButton:
            logger.error("SetProgressiveBar Error!!! No Last Touch Button!!!")
            return
        item = self.GetItemByPath(self.mLastTouchButton)
        if not item:
            logger.error("SetProgressiveBar Error!!! Try progressive none item!!!")
            return
        self.CaculateProgressiveRatio(item)
        barPath = self.mProgressiveBarPath + "/barMask"
        self.SetSpriteClipRatio(barPath, 1 - self.mTakePercent)

    def CaculateProgressiveRatio(self, itemDict):
        if self.mHeldTime is None:
            logger.error("Enter Progressive State But The Held Time is None!!!")
            return
        heldTime = self.mHeldTime - 10
        if heldTime > 20:
            self.mTakePercent = 1
            return
        totalNum = itemDict.get("count")
        takeNum = heldTime * totalNum / 20
        if takeNum == 0:
            takeNum = 1
            self.mHeldTime = takeNum * 20 / totalNum + 10
        self.mTakePercent = takeNum * 1.0 / totalNum

    def ShowUI(self, args):
        if not self.mIsHide:
            return
        clientApi.HideHudGUI(True)
        clientApi.SetInputMode(1)
        clientApi.SetResponse(False)
        if self.mLastSelectedPath:
            self.SetVisible(self.mLastSelectedPath + "/selectedImg", False)
            self.mLastSelectedPath = None
        self.InitCustomContainerUI(args)
        self.mBlockPos = args["blockPos"]
        self.mDimension = args["dimension"]
        self.mBlockName = args["blockName"]
        self.mContainerStateMachine.ResetToDefaut()
        self.SetVisible(self.mMainPanelPath, True)
        self.mIsHide = False

    def HideUI(self):
        if self.mIsHide:
            return
        clientApi.HideHudGUI(False)
        clientApi.SetInputMode(0)
        clientApi.SetResponse(True)
        self.SetVisible(self.mMainPanelPath, False)
        self.mIsHide = True

    def UpdateCustomContainerUI(self, args):
        """更新自定义容器中内容"""
        pass

    def GetFlyImg(self):
        """获取飞行图片控件，优先从控件池里获取"""
        for flyImg in self.mFlyImgPool:
            if not flyImg.IsUsing():
                return flyImg
        newImgName = "flyImg{0}".format(self.mFlyImgIndex)
        self.mFlyImgIndex += 1
        self.Clone(self.mFlyImgTemplatePath, self.mContentPanelPath, newImgName)
        newFlyImg = FlyImage("{0}/{1}".format(self.mContentPanelPath, newImgName))
        self.mFlyImgPool.append(newFlyImg)
        return newFlyImg

    def CanSelected(self, buttonPath, buttonEvent):
        if buttonPath == self.mDropAreaPath or not buttonPath:
            return False
        item = self.GetItemByPath(buttonPath)
        if item and buttonEvent == ButtonEventType.Clicked:
            return True
        return False

    def CanUnSelected(self, buttonPath, buttonEvent):
        return buttonPath == self.mLastSelectedPath and buttonEvent == ButtonEventType.Clicked

    def CanSwap(self, buttonPath, buttonEvent):
        return buttonPath and buttonPath != self.mLastSelectedPath and buttonPath != self.mDropAreaPath and buttonEvent == ButtonEventType.Clicked

    def CanDrop(self, buttonPath, buttonEvent):
        return buttonPath == self.mDropAreaPath and self.mLastSelectedPath and buttonEvent == ButtonEventType.Clicked

    def CanProgressiveSelect(self, buttonPath, buttonEvent):
        if buttonPath == self.mDropAreaPath or not buttonPath:
            return False
        itemDict = self.GetItemByPath(buttonPath)
        if not itemDict or buttonEvent != ButtonEventType.Pressed:
            return False
        itemComp = compFactory.CreateItem(clientApi.GetLevelId())
        basicInfo = itemComp.GetItemBasicInfo(itemDict.get("itemName", ""), itemDict.get("auxValue", 0))
        if basicInfo:
            maxStackSize = basicInfo.get("maxStackSize")
            if maxStackSize > 1:
                return True
        return False

    def CanProgressiveCancel(self, buttonPath, buttonEvent):
        return not buttonPath and buttonEvent == ButtonEventType.Released

    def CanProgressiveComplete(self, buttonPath, buttonEvent):
        return buttonPath and buttonEvent == ButtonEventType.Released

    def CanCoalesce(self, buttonPath, buttonEvent):
        return buttonEvent == ButtonEventType.DoubleClick

    def RegisterStateMachine(self):
        # 注册状态节点
        self.mContainerStateMachine.AddNode(NodeId.Idle, self.HandleIdle, None, True)
        self.mContainerStateMachine.AddNode(NodeId.SelectSlot, self.HandleSelected)
        self.mContainerStateMachine.AddNode(NodeId.UnSelectSlot, self.HandleUnSelected)
        self.mContainerStateMachine.AddNode(NodeId.Swap, self.HandleSwap)
        self.mContainerStateMachine.AddNode(NodeId.DropAll, self.HandleDropAll)
        self.mContainerStateMachine.AddNode(NodeId.TouchProgressiveSelect, self.HandleTouchProgressiveSelect)
        self.mContainerStateMachine.AddNode(NodeId.TouchProgressiveSelectComplete, self.HandleTouchProgressiveComplete)
        self.mContainerStateMachine.AddNode(NodeId.TouchProgressiveSelectCancel, self.HandleTouchProgressiveCancel)
        self.mContainerStateMachine.AddNode(NodeId.Coalesce, self.HandleCoalesce)
        # 注册状态转移条件
        self.mContainerStateMachine.AddEdge(NodeId.Idle, NodeId.SelectSlot, self.CanSelected)
        self.mContainerStateMachine.AddEdge(NodeId.SelectSlot, NodeId.UnSelectSlot, self.CanUnSelected)
        self.mContainerStateMachine.AddEdge(NodeId.SelectSlot, NodeId.Swap, self.CanSwap)
        self.mContainerStateMachine.AddEdge(NodeId.SelectSlot, NodeId.DropAll, self.CanDrop)
        self.mContainerStateMachine.AddEdge(NodeId.SelectSlot, NodeId.Coalesce, self.CanCoalesce)
        self.mContainerStateMachine.AddEdge(NodeId.Idle, NodeId.TouchProgressiveSelect, self.CanProgressiveSelect)
        self.mContainerStateMachine.AddEdge(NodeId.TouchProgressiveSelect, NodeId.TouchProgressiveSelectComplete, self.CanProgressiveComplete)
        self.mContainerStateMachine.AddEdge(NodeId.TouchProgressiveSelect, NodeId.TouchProgressiveSelectCancel, self.CanProgressiveCancel)
        self.mContainerStateMachine.AddEdge(NodeId.TouchProgressiveSelectComplete, NodeId.Swap, self.CanSwap)
        self.mContainerStateMachine.AddEdge(NodeId.TouchProgressiveSelectComplete, NodeId.TouchProgressiveSelectCancel, self.CanUnSelected)