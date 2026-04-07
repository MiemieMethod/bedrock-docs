# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
import neteaseTransactionScript.apiUtil as apiUtil
import neteaseTransactionScript.transactionClientConsts as transactionConsts


ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class TransactionScreenUI(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUpdateTradeUICnt = 0
		self.mBagInfo = []
		self.mBagPathToSlot = {}
		self.mHelpPanelPath = "/helpPanel"
		self.mIKnowBtnPath = self.mHelpPanelPath + "/helpInfoPanel/iKnowBtn"
		self.mLeftPanelPath = "/transactionPanel/leftPanel"
		self.mRightPanelPath = "/transactionPanel/rightPanel"
		self.mCloseBtnPath = self.mRightPanelPath + "/closeBtn"
		self.mHelpBtnPath = self.mRightPanelPath + "/helpBtn"
		self.mBagGridPath = self.mLeftPanelPath + "/bagPanel/bagContent/scrollingPanel/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"

		self.mLastSelectedItemPath = None

		# 物品交易相关
		self.mMyNickName = ""
		self.mPartnerNickName = ""
		self.mRemainTimes = 0
		self.mMaxTradeNum = 0
		self.mCurrencyIcon = "textures/ui/netease_transaction/currency1"
		self.mCurTradeNum = 0
		self.mCurTradeItem = None
		self.mCurTradeItemSlot = 0
		self.mTradeContentPanelPath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/tradeContentPanel"
		self.mTradeItemImgPath = self.mTradeContentPanelPath + "/tradeItem/itemImg"
		self.mTradeOperationPanelPath = self.mTradeContentPanelPath + "/tradeOperatePanel"
		self.mAddBtnPath = self.mTradeOperationPanelPath + "/addBtn"
		self.mSubBtnPath = self.mTradeOperationPanelPath + "/subBtn"
		self.mMaxBtnPath = self.mTradeOperationPanelPath + "/maxBtn"
		self.mTradeNumLabelPath = self.mTradeOperationPanelPath + "/tradeNum/numLabel"
		self.mRemainTradeLabelPath = self.mRightPanelPath + "/transactionInfoPanel/transactionInfoHeader/todayLimit/label"
		self.mRemainTradeTimesPath = self.mRightPanelPath + "/transactionInfoPanel/transactionInfoHeader/todayLimit/limitNum"
		self.mCurrencyNumPath = self.mRightPanelPath + "/transactionInfoPanel/transactionInfoHeader/currencyPanel/currencyNum"

		# 锁定按钮与确认交易按钮相关
		self.mEnableLock = True
		self.mEnableTrade = False
		self.mLocked = False
		self.mPartnerLocked = False
		self.mConfirmed = False
		self.mLockBtnPath = self.mRightPanelPath + "/transactionInfoPanel/btnPanel/lockTransactionBtn"
		self.mConfirmBtnPath = self.mRightPanelPath + "/transactionInfoPanel/btnPanel/confirmTradeBtn"
		self.mCurrencyInputPanelPath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/currencyInputPanel"
		self.mMyConfirmTagPath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/confirmTag"
		self.mPartnerConfirmTagPath = self.mRightPanelPath + "/transactionInfoPanel/patnerTransactionInfo/confirmTag"

		# 货币数量相关
		self.mMaxCurrency = 5000
		self.mTradeCurrency = "0"
		self.mEditBoxTextPath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/currencyInputPanel/currencyInputEditBox/centering_panel/clipper_panel/display_text"

		# 锁定信息相关
		self.mMyLockedInfoPath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/lockedInfo"
		self.mMyNamePath = self.mRightPanelPath + "/transactionInfoPanel/myTransactionInfo/nameInfo/name"
		self.mPartnerLockedInfoPath = self.mRightPanelPath + "/transactionInfoPanel/patnerTransactionInfo/lockedInfo"
		self.mPartnerInfoHintPath = self.mRightPanelPath + "/transactionInfoPanel/patnerTransactionInfo/hintLabel"
		self.mPartnerNamePath = self.mRightPanelPath + "/transactionInfoPanel/patnerTransactionInfo/nameInfo/name"
		self.mBShow = False

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		self.SetVisible("", flag)
		if flag:
			clientApi.SetInputMode(1)
			clientApi.HideHudGUI(True)
		else:
			clientApi.SetInputMode(0)
			clientApi.HideHudGUI(False)

	def InitScreen(self):
		self.ChangeScreenVisible(True)
		self.mUpdateTradeUICnt = 1

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用，初始化所有按钮回调及背包信息
	def Create(self):
		self.RegisterButtonEvent()

	def RegisterButtonEvent(self):
		self.AddTouchEventHandler(self.mCloseBtnPath, self.OnCloseButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mHelpBtnPath, self.OnHelpButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mIKnowBtnPath, self.OnIKnowButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mLockBtnPath, self.OnLockButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mConfirmBtnPath, self.OnTradeButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mAddBtnPath, self.OnAddButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mSubBtnPath, self.OnSubButtonClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mMaxBtnPath, self.OnMaxButtonClick, {"isSwallow": True})

	def TryUpdateTradeUI(self):
		'''
		注意：self.GetChildrenName(self.mBagGridPath) 可能失败，可能需要重试一次
		'''
		bagGridList = self.GetChildrenName(self.mBagGridPath)
		if not bagGridList:
			# PC版touch模式和鼠标模式scroll的路径不一致
			self.mBagGridPath = self.mLeftPanelPath + "/bagPanel/bagContent/scrollingPanel/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			bagGridList = self.GetChildrenName(self.mBagGridPath)
			if not bagGridList:
				print("Get Bag Grid List Error!!!")
				self.mBagGridPath = self.mLeftPanelPath + "/bagPanel/bagContent/scrollingPanel/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
				return False
		i = 0
		for bagGridChild in bagGridList:
			bagGridChildPath = self.mBagGridPath + "/" + bagGridChild
			itemDict = self.mBagInfo[i]
			self.mBagPathToSlot[bagGridChildPath] = i
			i += 1
			self.SetSlotUI(bagGridChildPath, itemDict)
			self.AddTouchEventHandler(bagGridChildPath, self.OnItemClick, {"isSwallow": True})
		self.SetText(self.mRemainTradeTimesPath, str(self.mRemainTimes))
		if self.mRemainTimes < 0:
			self.SetText(self.mRemainTradeTimesPath, "")
			self.SetText(self.mRemainTradeLabelPath, "")
		if self.mMaxCurrency <= 99999:
			currencyStr = str(self.mMaxCurrency)
		elif self.mMaxCurrency <= 999999:
			currencyStr = str(self.mMaxCurrency / 1000) + "k"
		else:
			currencyStr = str(self.mMaxCurrency / 1000000) + "m"
		self.SetText(self.mCurrencyNumPath, currencyStr)
		self.SetText(self.mMyNamePath, self.mMyNickName)
		self.SetText(self.mPartnerNamePath, self.mPartnerNickName)
		return True

	def UpdateBagInfo(self, args):
		self.mBagInfo = args["bagInfo"]
		self.mMaxCurrency = args["currency"]
		self.mRemainTimes = args["remainTimes"]
		self.mMyNickName = args["playerName"]
		self.mPartnerNickName = args["partnerName"]
		self.mCurrencyIcon = args["currencyIcon"]

	def SetSlotUI(self, path, item):
		"""设置目标槽位item渲染"""
		if item and item.get("count"):
			# 设值附魔
			isEnchant =  item.get("enchantData", False)
			userData = item.get("userData")
			self.SetUiItem(path + "/itemImg", item["itemName"], item["auxValue"], isEnchant, userData)
			self.SetVisible(path + "/itemImg", True)
			if item["count"] > 1:
				self.SetText(path + "/itemImg/itemNum", str(item["count"]))
			else:
				self.SetText(path + "/itemImg/itemNum", "")
		else:
			self.SetVisible(path + "/itemImg", False)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		# UI创建成功后的一帧更新UI信息
		if self.mBShow and self.mUpdateTradeUICnt >= 0:
			if self.mUpdateTradeUICnt == 0:
				if not self.TryUpdateTradeUI():
					self.mUpdateTradeUICnt = 1 #等一帧，再重试一次
			self.mUpdateTradeUICnt -= 1

	def UpdateButtonView(self):
		# 点击按钮后需要更新按钮的贴图和文字
		if self.mLocked:
			self.SetButtonLabel(self.mLockBtnPath, "取消锁定")
			self.SetSprite(self.mLockBtnPath + "/img", "textures/ui/netease_transaction/unlocked")
		else:
			self.SetButtonLabel(self.mLockBtnPath, "锁定")
			self.SetSprite(self.mLockBtnPath + "/img", "textures/ui/netease_transaction/locked")

		if self.mConfirmed:
			self.SetButtonLabel(self.mConfirmBtnPath, "已确认")
		else:
			self.SetButtonLabel(self.mConfirmBtnPath, "确认交易")

	def SetButtonLabel(self, buttonPath, text):
		self.SetText(buttonPath + "/default/label", text)
		self.SetText(buttonPath + "/hover/label", text)
		self.SetText(buttonPath + "/pressed/label", text)
		self.SetText(buttonPath + "/locked/label", text)

	def UpdateMyLockedInfo(self, locked):
		self.SetVisible(self.mMyLockedInfoPath, locked)
		self.SetVisible(self.mTradeContentPanelPath, not locked)
		self.SetVisible(self.mCurrencyInputPanelPath, not locked)
		if self.mCurTradeNum > 0:
			self.SetVisible(self.mMyLockedInfoPath + "/itemInfo", True)
			self.SetText(self.mMyLockedInfoPath + "/itemInfo/tradeNumPanel/tradeNum", str(self.mCurTradeNum))
			self.SetUiItem(self.mMyLockedInfoPath + "/itemInfo/itemImg", self.mCurTradeItem["itemName"], self.mCurTradeItem["auxValue"])
		else:
			self.SetVisible(self.mMyLockedInfoPath + "/itemInfo", False)
		self.SetText(self.mMyLockedInfoPath + "/currencyInfo/tradeNumPanel/tradeNum", self.mTradeCurrency)

	def UpdatePartnerLockedInfo(self, args):
		locked = args.get("isLocked", False)
		self.mPartnerLocked = locked
		if not locked:
			self.ResetTradePanel()
		self.mEnableTrade = locked and self.mLocked
		self.UpdateButtonView()
		tradeInfo = args.get("tradeInfo", {})
		tradeItem = tradeInfo.get("item", {})
		tradeItemNum = tradeInfo.get("itemNum", 0)
		tradeCurrencyNum = tradeInfo.get("currencyNum", 3)
		self.SetVisible(self.mPartnerLockedInfoPath, locked)
		self.SetVisible(self.mPartnerInfoHintPath, not locked)
		if tradeItemNum > 0:
			self.SetVisible(self.mPartnerLockedInfoPath + "/itemInfo", True)
			self.SetText(self.mPartnerLockedInfoPath + "/itemInfo/tradeNumPanel/tradeNum", str(tradeItemNum))
			self.SetUiItem(self.mPartnerLockedInfoPath + "/itemInfo/itemImg", tradeItem.get("itemName"), tradeItem.get("auxValue"))
		else:
			self.SetVisible(self.mPartnerLockedInfoPath + "/itemInfo", False)
		self.SetText(self.mPartnerLockedInfoPath + "/currencyInfo/tradeNumPanel/tradeNum", str(tradeCurrencyNum))

	def UpdatePartnerConfirmedInfo(self):
		self.SetVisible(self.mPartnerConfirmTagPath, True)

	def Hide(self):
		self.ChangeScreenVisible(False)

	def ResetTradePanel(self):
		self.mLocked = False
		self.mConfirmed = False
		self.mPartnerLocked = False
		self.mEnableTrade = False
		self.SetVisible(self.mMyLockedInfoPath, False)
		self.SetVisible(self.mTradeContentPanelPath, True)
		self.SetVisible(self.mCurrencyInputPanelPath, True)
		self.SetVisible(self.mPartnerLockedInfoPath, False)
		self.SetVisible(self.mPartnerInfoHintPath, True)
		self.SetVisible(self.mPartnerConfirmTagPath, False)
		self.SetVisible(self.mMyConfirmTagPath, False)
		self.UpdateButtonView()

################################ Button call back ################################
	@apiUtil.touch_filter("up")
	def OnCloseButtonClick(self, args):
		apiUtil.GetTransactionClientSystem().NotifyToServer(transactionConsts.CloseTransactionEvent, { "playerId": clientApi.GetLocalPlayerId() })

	@apiUtil.touch_filter("up")
	def OnHelpButtonClick(self, args):
		self.SetVisible(self.mHelpPanelPath, True)

	@apiUtil.touch_filter("up")
	def OnIKnowButtonClick(self, args):
		self.SetVisible(self.mHelpPanelPath, False)

	@apiUtil.touch_filter("up")
	def OnItemClick(self, args):
		buttonPath = args["ButtonPath"]
		buttonPath = buttonPath[buttonPath.find("/") : ]
		if self.mLastSelectedItemPath is not None:
			self.SetVisible(self.mLastSelectedItemPath + "/selectedImg", False)
		self.SetVisible(buttonPath + "/selectedImg", True)
		self.mLastSelectedItemPath = buttonPath
		if not self.mLocked:
			self.mCurTradeItem = self.mBagInfo[self.mBagPathToSlot[buttonPath]]
			if self.mCurTradeItem:
				self.mCurTradeItemSlot = self.mBagPathToSlot[buttonPath]
				self.SetVisible(self.mTradeItemImgPath, True)
				self.SetUiItem(self.mTradeItemImgPath, self.mCurTradeItem.get("itemName"), self.mCurTradeItem.get("auxValue"))
				self.mMaxTradeNum = self.mCurTradeItem.get("count", 1)
				self.SetTouchEnable(self.mAddBtnPath, True)
				self.SetTouchEnable(self.mMaxBtnPath, True)
				self.SetSprite(self.mMaxBtnPath + "/btnImg", "textures/ui/netease_transaction/max_icon")
				self.mCurTradeNum = 0
				self.SetTouchEnable(self.mSubBtnPath, False)
				self.SetText(self.mTradeNumLabelPath, str(self.mCurTradeNum))
			else:
				self.mCurTradeNum = 0
				self.SetVisible(self.mTradeItemImgPath, False)
				self.SetTouchEnable(self.mAddBtnPath, False)
				self.SetTouchEnable(self.mMaxBtnPath, False)
				self.SetTouchEnable(self.mSubBtnPath, False)
				self.SetSprite(self.mMaxBtnPath + "/btnImg", "textures/ui/netease_transaction/max_icon_unuse")
				self.SetText(self.mTradeNumLabelPath, str(self.mCurTradeNum))

	@apiUtil.touch_filter("up")
	def OnLockButtonClick(self, args):
		self.mLocked = not self.mLocked
		if not self.mLocked:
			self.ResetTradePanel()
		else:
			self.mEnableTrade = self.mLocked and self.mPartnerLocked
			self.UpdateButtonView()
			self.UpdateMyLockedInfo(self.mLocked)
		data = {
			"playerId": clientApi.GetLocalPlayerId(),
			"tradeInfo": {
				"item": self.mCurTradeItem,
				"itemSlot": self.mCurTradeItemSlot,
				"itemNum": self.mCurTradeNum,
				"currencyNum": int(self.mTradeCurrency)
			},
			"isLocked": self.mLocked
		}
		apiUtil.GetTransactionClientSystem().NotifyToServer(transactionConsts.LockTransactionEvent, data)
		return ViewRequest.Refresh

	@apiUtil.touch_filter("up")
	def OnTradeButtonClick(self, args):
		self.mEnableTrade = False
		self.mConfirmed = True
		self.SetVisible(self.mMyConfirmTagPath, True)
		self.UpdateButtonView()
		data = {
			"playerId": clientApi.GetLocalPlayerId()
		}
		apiUtil.GetTransactionClientSystem().NotifyToServer(transactionConsts.ConfirmTransactionEvent, data)
		return ViewRequest.Refresh

	@apiUtil.touch_filter("up")
	def OnAddButtonClick(self, args):
		self.mCurTradeNum += 1
		if self.mCurTradeNum >= self.mMaxTradeNum:
			self.SetTouchEnable(self.mAddBtnPath, False)
			self.SetTouchEnable(self.mMaxBtnPath, False)
			self.SetSprite(self.mMaxBtnPath + "/btnImg", "textures/ui/netease_transaction/max_icon_unuse")
		if self.mCurTradeNum > 0:
			self.SetTouchEnable(self.mSubBtnPath, True)
		self.SetText(self.mTradeNumLabelPath, str(self.mCurTradeNum))
		return ViewRequest.Refresh

	@apiUtil.touch_filter("up")
	def OnSubButtonClick(self, args):
		self.mCurTradeNum -= 1
		if self.mCurTradeNum < self.mMaxTradeNum:
			self.SetTouchEnable(self.mAddBtnPath, True)
			self.SetTouchEnable(self.mMaxBtnPath, True)
			self.SetSprite(self.mMaxBtnPath + "/btnImg", "textures/ui/netease_transaction/max_icon")
		if self.mCurTradeNum <= 0:
			self.SetTouchEnable(self.mSubBtnPath, False)
		self.SetText(self.mTradeNumLabelPath, str(self.mCurTradeNum))
		return ViewRequest.Refresh

	@apiUtil.touch_filter("up")
	def OnMaxButtonClick(self, args):
		self.mCurTradeNum = self.mMaxTradeNum
		self.SetTouchEnable(self.mAddBtnPath, False)
		self.SetTouchEnable(self.mMaxBtnPath, False)
		self.SetSprite(self.mMaxBtnPath + "/btnImg", "textures/ui/netease_transaction/max_icon_unuse")
		self.SetTouchEnable(self.mSubBtnPath, True)
		self.SetText(self.mTradeNumLabelPath, str(self.mCurTradeNum))
		return ViewRequest.Refresh

################################ UI bindings ################################
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def BindCurrencyEditChanged(self, args):
		# 输入框文字修改时触发，需检测输入是否合法（我们只需要数字）
		inputText = args["Text"]
		if inputText.isdigit():
			self.mTradeCurrency = inputText
		elif inputText == "":
			self.mTradeCurrency = "0"
		if len(self.mTradeCurrency) > 1:
			i = 0
			for char in self.mTradeCurrency:
				if char != "0":
					break
				i += 1
			self.mTradeCurrency = self.mTradeCurrency[i:]
			if len(self.mTradeCurrency) == 0:
				self.mTradeCurrency = "0"
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def BindCurrencyEditText(self):
		# 当输入交易金额超过已有金额时数字标红
		if int(self.mTradeCurrency) > self.mMaxCurrency:
			self.SetTextColor(self.mEditBoxTextPath, (1, 0, 0, 1))
			self.mEnableLock = False
		else:
			self.SetTextColor(self.mEditBoxTextPath, (1, 1, 1, 1))
			self.mEnableLock = True
		return self.mTradeCurrency

	@ViewBinder.binding(ViewBinder.BF_BindBool, "#bindLockBtnEnable")
	def BindLockBtnEnable(self):
		return self.mEnableLock

	@ViewBinder.binding(ViewBinder.BF_BindBool, "#bindTradeBtnEnable")
	def BindTradeBtnEnable(self):
		return self.mEnableTrade

	@ViewBinder.binding(ViewBinder.BF_BindString, "#bindCurrencyIcon")
	def BindCurrencyIcon(self):
		return self.mCurrencyIcon
