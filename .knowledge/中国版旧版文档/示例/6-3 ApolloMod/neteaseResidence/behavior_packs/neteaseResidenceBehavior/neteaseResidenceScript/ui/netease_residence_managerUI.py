# -*- coding: utf-8 -*-
import random
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
from neteaseResidenceScript.ui.uiDef import UIDef
import weakref
import neteaseResidenceScript.residenceConsts as residenceConsts

CheckTimeIntervalMax = 1.5

class ResidenceManageUIScreen(ScreenNode):
	"""
	领地管理界面（我的领地界面）
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		
		self.mManagePanel = "/managePanel"
		self.mCloseBtn = self.mManagePanel + "/close_button"#关闭
		self.mApplyBtn = self.mManagePanel + "/apply_button"#申请页面按钮
		self.mTransferBtn = self.mManagePanel + "/transfer_button"#传送页面按钮
		self.mTransferNewImg = self.mTransferBtn + "/image16"  # 传送页面按钮
		self.mGiveBtn = self.mManagePanel + "/give_button"#赋予页面按钮
		self.mManageBtn = self.mManagePanel + "/manage_button"#管理页面按钮
		self.mManageNewImg = self.mManageBtn + "/image14"  # 管理页面按钮
		self.mMyBtn = self.mManagePanel + "/my_button"#管理页面按钮
		self.mManageSecondPanel = self.mManagePanel + "/panel10"
		self.mManagePanelImg = self.mManageSecondPanel + "/image27"
		self.mManageApplicatorTabelPanel = self.mManagePanelImg + "/panel18"
		self.mManageUserTabelPanel = self.mManagePanelImg + "/panel17"
		self.mResidenceUserBtn = self.mManagePanelImg + "/button12"  # 访客管理按钮
		self.mApplicatorBtn = self.mManagePanelImg + "/button13"  # 申请管理按钮
		self.mApplicatorBtnNewImg = self.mApplicatorBtn + "/image43/image44"  # 申请管理按钮
		self.mResidenceCheckBtn = self.mManagePanelImg + "/button14"  # 领地选择按钮
		self.mResidenceCheckBtnNewImg = self.mResidenceCheckBtn + "/image42"  # 领地选择按钮
		# self.mResidenceCheckBtn = self.mManagePanelImg + "/button10"  # 领地查询按钮
		# self.mResidenceCheckText = self.mResidenceCheckBtn + "/label22"  # 领地查询按钮文字
		self.mResidenceUserScroll = self.mManagePanelImg + "/scroll_view3"  # 访客管理页面
		self.mResidenceApplicatorScroll = self.mManagePanelImg + "/scroll_view4"  # 权限列表
		self.mResidenceMyScroll = self.mResidenceCheckBtn + "/scroll_view7"
		# self.mTipImg = self.mGiveSecondPanel + "/image25"
		# self.mTipLabel = self.mTipImg + "/label32"
		self.mManageTipsPanel = self.mManageSecondPanel + "/tipsimage"  # 提示语
		self.mManageTipsLabel = self.mManageTipsPanel + "/tipslabel"
		
		self.mSurePanel = self.mManagePanel + "/panel13"
		self.mSurePanelImg = self.mSurePanel + "/button25/image11"
		self.mSurePanelCloseBtn = self.mSurePanelImg + "/button26"
		self.mSurePanelLabel = self.mSurePanelImg + "/label26"
		self.mSurePanelSureBtn = self.mSurePanelImg + "/button28"
		self.mSurePanelCancelBtn = self.mSurePanelImg + "/button27"
		
		self.mCurrentPage = "applicate"
		
		self.gameComp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
		self.InitScreenManage()
		
	def InitScreenManage(self):
		self.SetVisible(self.mManageUserTabelPanel, False)
		self.SetVisible(self.mResidenceUserScroll, False)
		self.SetVisible(self.mResidenceMyScroll, False)
		
		self.SetVisible(self.mManageApplicatorTabelPanel, True)
		if self.mChosenResId == -1:
			self.SetVisible(self.mResidenceApplicatorScroll, False)
		else:
			self.SetVisible(self.mResidenceApplicatorScroll, True)
			self.RefreshApplicator()
			self.RefreshUser()
		
		self.SetVisible(self.mManageTipsPanel, False)
	
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "SearchResidenceResultByIdFromServerEvent", self,
		                                  self.OnShowSearchResidenceResult)
		self.AddTouchEventHandler(self.mApplyBtn, self.mClientSystem.OnApplyBtn)
		self.AddTouchEventHandler(self.mTransferBtn, self.mClientSystem.OnTransferBtn)
		self.AddTouchEventHandler(self.mGiveBtn, self.mClientSystem.OnGiveBtn)
		self.SetTouchEnable(self.mManageBtn, False)
		self.AddTouchEventHandler(self.mManageBtn, self.mClientSystem.OnManageBtn)
		self.AddTouchEventHandler(self.mMyBtn, self.mClientSystem.OnMyBtn)
	
	def OnShowSearchResidenceResult(self, args):
		#print "OnShowSearchResidenceResult", args
		resList = args.get("resList")
		resNum = len(resList)
		if self.mIsShow == False:
			return
		if resNum <= 0:
			self.SetVisible(self.mResidenceMyScroll, False)
		else:
			self.SetVisible(self.mResidenceMyScroll, True)
		
		deltaNum = resNum - len(self.mResidenceCheckPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceCheckPanels) + 1, resNum + 1):
				residenceCheckPanel = "ResidenceCheckPanel%s" % i
				residenceCheckPanelPath = "%s/%s" % (self.mResidenceMyPanel, residenceCheckPanel)
				residenceCheckTextPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceCheckText)
				residenceChooseBtnPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceChooseBtn)
				residenceChooseBtnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnChosenImg)
				residenceChooseBtnUnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnUnChosenImg)
				self.Clone(self.mResidenceCheckPanel1, self.mResidenceMyPanel, residenceCheckPanel)
				self.mResidenceCheckPanels.append(residenceCheckPanelPath)
				self.mResidenceCheckTexts.append(residenceCheckTextPath)
				self.mResidenceChooseBtns.append(residenceChooseBtnPath)
				self.mResidenceChooseBtnChosenImgs.append(residenceChooseBtnChosenImgPath)
				self.mResidenceChooseBtnUnChosenImgs.append(residenceChooseBtnUnChosenImgPath)
		elif deltaNum < 0:
			for i in xrange(resNum + 1, len(self.mResidenceCheckPanels) + 1):
				if i == 1:
					continue
				print 'removing CheckPanel ', i
				residenceCheckPanel = "ResidenceCheckPanel%s" % i
				residenceCheckPanelPath = "%s/%s" % (self.mResidenceMyPanel, residenceCheckPanel)
				residenceCheckTextPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceCheckText)
				residenceChooseBtnPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceChooseBtn)
				residenceChooseBtnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnChosenImg)
				residenceChooseBtnUnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnUnChosenImg)
				self.RemoveComponent(residenceCheckPanelPath, self.mResidenceMyPanel)
				self.mResidenceCheckPanels.remove(residenceCheckPanelPath)
				self.mResidenceCheckTexts.remove(residenceCheckTextPath)
				self.mResidenceChooseBtns.remove(residenceChooseBtnPath)
				self.mResidenceChooseBtnChosenImgs.remove(residenceChooseBtnChosenImgPath)
				self.mResidenceChooseBtnUnChosenImgs.remove(residenceChooseBtnUnChosenImgPath)
		# 其余情况，正常显示
		d = self.GetSize(self.mResidenceCheckPanel1)[1]
		for i, residenceCheckPanelPath in enumerate(self.mResidenceCheckPanels):
			self.SetPosition(residenceCheckPanelPath,
			                 (self.mResidenceCheckPanelPos[0], self.mResidenceCheckPanelPos[1] + d * i))
		i = 0
		self.mAllCheckResidence = []
		for idx, resData in enumerate(resList):
			self.mAllCheckResidence.append(resData)
			self.SetText(self.mResidenceCheckTexts[i], resData["resName"].encode('utf-8'))
			if resData["resId"] == self.mChosenResId:
				self.SetVisible(self.mResidenceChooseBtnChosenImgs[i], True)
			else:
				self.SetVisible(self.mResidenceChooseBtnChosenImgs[i], False)
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mResidenceMySize[1])
		self.SetSize(self.mResidenceMyPanel, (self.mResidenceMySize[0], height))
		
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.mIsShow = flag
		if flag:
			extraClientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	def Create(self):
		# 使用者的scroll
		mResidenceUserScrollTouch = self.mResidenceUserScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residenceuser_size = self.GetSize(mResidenceUserScrollTouch)
		if residenceuser_size:
			self.mResidenceUserParentPanel = mResidenceUserScrollTouch
			self.mResidenceUserSize = residenceuser_size
		else:
			mResidenceUserScrollTouch = self.mResidenceUserScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residenceuser_size = self.GetSize(mResidenceUserScrollTouch)
			self.mResidenceUserParentPanel = mResidenceUserScrollTouch
			self.mResidenceUserSize = residenceuser_size
		self.mResidenceUserPanel1 = self.mResidenceUserParentPanel + "/ResidenceUser1"
		self.mResidenceUserPanels = [
			self.mResidenceUserPanel1
		]
		self.mResidenceUserName1 = self.mResidenceUserPanel1 + "/label39"
		self.mResidenceUserNames = [
			self.mResidenceUserName1
		]
		self.mResidencePlaceBlockBtn1 = self.mResidenceUserPanel1 + "/button15"
		self.mResidencePlaceBlockBtns = [
			self.mResidencePlaceBlockBtn1
		]
		self.mResidencePlaceBlockBtnImg1 = self.mResidencePlaceBlockBtn1 + "/image31"
		self.mResidencePlaceBlockBtnImgs = [
			self.mResidencePlaceBlockBtnImg1
		]
		self.mResidenceUseDoorBtn1 = self.mResidenceUserPanel1 + "/button16"
		self.mResidenceUseDoorBtns = [
			self.mResidenceUseDoorBtn1
		]
		self.mResidenceUseDoorBtnImg1 = self.mResidenceUseDoorBtn1 + "/image33"
		self.mResidenceUseDoorBtnImgs = [
			self.mResidenceUseDoorBtnImg1
		]
		self.mResidenceEnterBtn1 = self.mResidenceUserPanel1 + "/button17"
		self.mResidenceEnterBtns = [
			self.mResidenceEnterBtn1
		]
		self.mResidenceEnterBtnImg1 = self.mResidenceEnterBtn1 + "/image131"
		self.mResidenceEnterBtnImgs = [
			self.mResidenceEnterBtnImg1
		]
		
		self.mResidenceUserPanelPos = self.GetPosition(self.mResidenceUserPanel1)
		# 申请者的scroll
		#print "GetAllChildrenPath", self.GetAllChildrenPath(self.mResidenceApplicatorScroll)
		mResidenceApplicatorScrollTouch = self.mResidenceApplicatorScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residenceapplicator_size = self.GetSize(mResidenceApplicatorScrollTouch)
		if residenceapplicator_size:
			self.mResidenceApplicatorParentPanel = mResidenceApplicatorScrollTouch
			self.mResidenceApplicatorSize = residenceapplicator_size
		else:
			mResidenceApplicatorScrollTouch = self.mResidenceApplicatorScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residenceapplicator_size = self.GetSize(mResidenceApplicatorScrollTouch)
			self.mResidenceApplicatorParentPanel = mResidenceApplicatorScrollTouch
			self.mResidenceApplicatorSize = residenceapplicator_size
		
		self.mResidenceApplicatorPanel1 = self.mResidenceApplicatorParentPanel + "/ResidenceApplicator1"
		self.mResidenceApplicatorPanels = [
			self.mResidenceApplicatorPanel1
		]
		self.mResidenceApplicatorName1 = self.mResidenceApplicatorPanel1 + "/label34"
		self.mResidenceApplicatorNames = [
			self.mResidenceApplicatorName1
		]
		self.mResidenceApplicatorNewImgs1 = self.mResidenceApplicatorPanel1 + "/image49"
		self.mResidenceApplicatorNewImgs = [
			self.mResidenceApplicatorNewImgs1
		]
		self.mResidenceApplicatorMessage1 = self.mResidenceApplicatorPanel1 + "/label35"
		self.mResidenceApplicatorMessages = [
			self.mResidenceApplicatorMessage1
		]
		self.mResidencePlaceBlockImg1 = self.mResidenceApplicatorPanel1 + "/image46"
		self.mResidencePlaceBlockImgs = [
			self.mResidencePlaceBlockImg1
		]
		self.mResidenceUseDoorImg1 = self.mResidenceApplicatorPanel1 + "/image52"
		self.mResidenceUseDoorImgs = [
			self.mResidenceUseDoorImg1
		]
		self.mResidenceEnterImg1 = self.mResidenceApplicatorPanel1 + "/image53"
		self.mResidenceEnterImgs = [
			self.mResidenceEnterImg1
		]
		self.mResidenceAcceptBtn1 = self.mResidenceApplicatorPanel1 + "/button22"
		self.mResidenceAcceptBtns = [
			self.mResidenceAcceptBtn1
		]
		self.mResidenceRefuseBtn1 = self.mResidenceApplicatorPanel1 + "/button21"
		self.mResidenceRefuseBtns = [
			self.mResidenceRefuseBtn1
		]
		
		
		self.mResidenceApplicatorPanelPos = self.GetPosition(self.mResidenceApplicatorPanel1)
		
		# 领地信息的scroll
		mResidenceMyScrollTouch = self.mResidenceMyScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residencemy_size = self.GetSize(mResidenceMyScrollTouch)
		if residencemy_size:
			self.mResidenceMyPanel = mResidenceMyScrollTouch
			self.mResidenceMySize = residencemy_size
		else:
			mResidenceMyScrollTouch = self.mResidenceMyScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residencemy_size = self.GetSize(mResidenceMyScrollTouch)
			self.mResidenceMyPanel = mResidenceMyScrollTouch
			self.mResidenceMySize = residencemy_size
		self.mResidenceCheckPanel1 = self.mResidenceMyPanel + "/ResidenceCheckPanel1"
		self.mResidenceCheckText = "label3"
		self.mResidenceChooseBtn = "button2"
		self.mResidenceChooseBtnChosenImg = "image7"
		self.mResidenceChooseBtnUnChosenImg = "image6"
		
		self.mResidenceCheckPanels = [
			self.mResidenceCheckPanel1
		]
		
		self.mResidenceCheckTexts = [
			self.mResidenceCheckPanel1 + "/"+ self.mResidenceCheckText
		]
		
		self.mResidenceChooseBtns = [
			self.mResidenceCheckPanel1 + "/"+ self.mResidenceChooseBtn
		]
		
		self.mResidenceChooseBtnChosenImgs = [
			self.mResidenceCheckPanel1 + "/"+ self.mResidenceChooseBtn + "/"+ self.mResidenceChooseBtnChosenImg
		]
		
		self.mResidenceChooseBtnUnChosenImgs = [
			self.mResidenceCheckPanel1 + "/"+ self.mResidenceChooseBtn + "/"+ self.mResidenceChooseBtnUnChosenImg
		]
		
		self.mResidenceCheckPanelPos = self.GetPosition(self.mResidenceCheckPanel1)
		
		self.AddTouchEventHandler(self.mResidenceCheckBtn, self.OnResidenceCheckBtn)
		
		self.AddTouchEventHandler(self.mApplicatorBtn, self.OnApplicatorBtn)
		self.AddTouchEventHandler(self.mResidenceUserBtn, self.OnResidenceUserBtn)
		self.AddTouchEventHandler(self.mSurePanelCloseBtn, self.OnSurePanelCloseBtn)
		self.AddTouchEventHandler(self.mSurePanelSureBtn, self.OnSurePanelSureBtn)
		self.AddTouchEventHandler(self.mSurePanelCancelBtn, self.OnSurePanelCancelBtn)
		
		for index, residenceChooseBtn in enumerate(self.mResidenceChooseBtns):
			self.AddTouchEventHandler(residenceChooseBtn, self.OnResidenceChooseBtn)
			
		for index, residencePlaceBtn in enumerate(self.mResidencePlaceBlockBtns):
			self.AddTouchEventHandler(residencePlaceBtn, self.OnResidencePlaceBtn)
			
		for index, residenceUseDoorBtn in enumerate(self.mResidenceUseDoorBtns):
			self.AddTouchEventHandler(residenceUseDoorBtn, self.OnResidenceUseDoorBtn)
			
		for index, residenceEnterBtn in enumerate(self.mResidenceEnterBtns):
			self.AddTouchEventHandler(residenceEnterBtn, self.OnResidenceEnterBtn)
			
		for index, residenceAcceptBtn in enumerate(self.mResidenceAcceptBtns):
			self.AddTouchEventHandler(residenceAcceptBtn, self.OnResidenceAcceptBtn)
			
		for index, residenceRefuseBtn in enumerate(self.mResidenceRefuseBtns):
			self.AddTouchEventHandler(residenceRefuseBtn, self.OnResidenceRefuseBtn)
		
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
			
		self.mAllCheckResidence = [] #所有查找到的领地id
		self.mAllUserUid = [] #所有拥有者玩家的uid
		self.mAllApplicatorUid = []#所有申请者玩家的uid
		self.mAllApplicatorNames = []#所有申请者玩家的名字
		self.mAllApplicatorAuthority = []
		self.mChosenResId = -1
		self.mLastCheckTime = 0
		
		self.mDeletingUid = -1
		self.mDeletingResId = -1
	
	def ClosePanel(self, args=None):
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
		else:
			self.ChangeScreenVisible(False)
		
	def OnSurePanelCloseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mSurePanel,False)
			self.mDeletingUid = -1
			self.mDeletingResId = -1
			
	def OnSurePanelSureBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mSurePanel,False)
			if self.mDeletingUid == -1 or self.mDeletingResId == -1:
				return
			self.mClientSystem.NotifyToServer("DeleteAuthFromClientEvent", {"clientId":self.mLocalPlayerId, "uid":self.mDeletingUid, "resId":self.mDeletingResId})
			
	def OnSurePanelCancelBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mSurePanel,False)
			self.mDeletingUid = -1
			self.mDeletingResId = -1
			
	def OnShowSurePanel(self, args):
		userName = args.get("userName")
		uid = args.get("uid")
		resId = args.get("resId")
		self.SetVisible(self.mSurePanel, True)
		self.SetText(self.mSurePanelLabel, "你已取消“%s”所有权限,将从访客列表中移除"%(userName.encode("UTF-8")))
		self.mDeletingUid = uid
		self.mDeletingResId = resId
		
		
	def OnResidenceAcceptBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			acceptIndex = self.GetResidenceAcceptBtnIndex(args["ButtonPath"])
			applicatorUid = self.mAllApplicatorUid[acceptIndex]
			authority = self.mAllApplicatorAuthority[acceptIndex]
			dict = {
				"applicatorUid": applicatorUid,
				"resId": self.mChosenResId,
				"playerId": self.mLocalPlayerId,
				"authority": authority
			}
			self.mClientSystem.NotifyToServer("applicatorAcceptFromClientEvent", dict)
	
	def OnResidenceRefuseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			refuseIndex = self.GetResidenceRefuseBtnIndex(args["ButtonPath"])
			applicatorUid = self.mAllApplicatorUid[refuseIndex]
			dict = {
				"applicatorUid": applicatorUid,
				"resId": self.mChosenResId,
				"playerId": self.mLocalPlayerId
			}
			self.mClientSystem.NotifyToServer("applicatorRefuseFromClientEvent", dict)
			
	def GetResidenceAcceptBtnIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceAcceptBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetResidenceRefuseBtnIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceRefuseBtns):
			if btnPath == path:
				return index
		return -1
	
		
	def OnResidencePlaceBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				self.ShowTips("不能点太快!")
				return
			else:
				placeBlockIndex = self.GetPlaceBlockBtnIndex(args["ButtonPath"])
				uid = self.mAllUserUid[placeBlockIndex]
				userName = self.mAllUserNames[placeBlockIndex]
				if self.mChosenResId == -1:
					return
				dict = {
					"resId" : self.mChosenResId,
					"uid":uid,
					"userName":userName,
					"changeAuth": "PlacedBlock",
					"playerId": self.mLocalPlayerId
				}
				self.mClientSystem.NotifyToServer("ChangeAuthFromClientEvent", dict)
	
	def OnResidenceUseDoorBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				self.ShowTips("不能点太快!")
				return
			else:
				useDoorIndex = self.GetPlaceUseDoorBtnIndex(args["ButtonPath"])
				uid = self.mAllUserUid[useDoorIndex]
				userName = self.mAllUserNames[useDoorIndex]
				if self.mChosenResId == -1:
					return
				dict = {
					"resId" : self.mChosenResId,
					"uid":uid,
					"userName":userName,
					"changeAuth": "UseDoor",
					"playerId": self.mLocalPlayerId
				}
				self.mClientSystem.NotifyToServer("ChangeAuthFromClientEvent", dict)
	
	def OnResidenceEnterBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				self.ShowTips("不能点太快!")
				return
			else:
				enterIndex = self.GetPlaceEnterBtnIndex(args["ButtonPath"])
				uid = self.mAllUserUid[enterIndex]
				userName = self.mAllUserNames[enterIndex]
				if self.mChosenResId == -1:
					return
				dict = {
					"resId" : self.mChosenResId,
					"uid":uid,
					"userName":userName,
					"changeAuth": "Enter",
					"playerId": self.mLocalPlayerId
				}
				self.mClientSystem.NotifyToServer("ChangeAuthFromClientEvent", dict)
			
	def OnResidenceChooseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			print "OnResidenceChooseBtn", self.mAllCheckResidence
			resIndex = self.GetResIdIndex(args["ButtonPath"])
			resData = self.mAllCheckResidence[resIndex]
			#data = {'playerId': self.mLocalPlayerId, "resId":resId}
			self.mChosenResId = resData["resId"]
			self.SetVisible(self.mResidenceMyScroll, False)
			self.SetText(self.mResidenceCheckBtn + '/button_label', resData["resName"].encode('utf-8'))
			
	def GetResIdIndex(self, path):
		#print "GetResIdIndex", self.mResidenceChooseBtns
		#print "path", path
		for index, btnPath in enumerate(self.mResidenceChooseBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetPlaceBlockBtnIndex(self, path):
		for index, btnPath in enumerate(self.mResidencePlaceBlockBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetPlaceUseDoorBtnIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceUseDoorBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetPlaceEnterBtnIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceEnterBtns):
			if btnPath == path:
				return index
		return -1
		
	def OnResidenceCheckBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				#TODO 提示不能点太快
				self.ShowTips("不能点太快!")
				return
			else:
				self.mLastCheckTime = now
				dict = {
					"playerId":self.mLocalPlayerId
				}
				self.mClientSystem.NotifyToServer("CheckPlayerResidenceByIdFromClient",dict)
	
	def ShowTips(self, message):
		self.mClientSystem.NotifyToServer("ShowTipsFromClientEvent",
		                                  {"playerId": self.mLocalPlayerId, "message": message})
	def Show(self):
		self.ChangeScreenVisible(True)
		self.mCurrentPage = "applicate"
		self.InitScreenManage()
		#self.SetVisible(self.mTransferNewImg, len(self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead) > 0)
		
	def OnApplicatorBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mManageApplicatorTabelPanel, True)
			self.SetVisible(self.mManageUserTabelPanel, False)
			self.SetVisible(self.mResidenceUserScroll, False)
			self.mCurrentPage = "applicate"
			self.RefreshApplicator()
			
	def RefreshApplicator(self):
		if self.mCurrentPage != "applicate":
			return
		if self.mChosenResId == -1:
			self.SetVisible(self.mResidenceApplicatorScroll, False)
			return
		else:
			self.SetVisible(self.mResidenceApplicatorScroll, True)
		resApplication = self.mClientSystem.GetResidenceMgr().mResApplication.get(self.mChosenResId)
		print "resApplication", resApplication
		if resApplication is None:
			self.SetVisible(self.mResidenceApplicatorScroll, False)
			return
		applicatorNum = len(resApplication)
		if applicatorNum > 0:
			self.SetVisible(self.mResidenceApplicatorScroll, True)
		else:
			self.SetVisible(self.mResidenceApplicatorScroll, False)
			return
		deltaNum = applicatorNum - len(self.mResidenceApplicatorPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceApplicatorPanels) + 1, applicatorNum + 1):
				residenceApplicatorPanel = "ResidenceApplicator%s" % i
				residenceApplicatorPanelPath = "%s/%s" % (self.mResidenceApplicatorParentPanel, residenceApplicatorPanel)
				residenceApplicatorNamePath = residenceApplicatorPanelPath + "/label34"
				residenceApplicatorMessagePath = residenceApplicatorPanelPath + "/label35"
				residencePlaceBlockImg = residenceApplicatorPanelPath + "/image46"
				residenceUseDoorImg = residenceApplicatorPanelPath + "/image52"
				residenceEnterImg = residenceApplicatorPanelPath + "/image53"
				residenceAcceptBtn = residenceApplicatorPanelPath + "/button22"
				residenceRefuseBtn = residenceApplicatorPanelPath + "/button21"
				residenceApplicatorNewImg = residenceApplicatorPanelPath + "/image49"
				self.Clone(self.mResidenceApplicatorPanel1, self.mResidenceApplicatorParentPanel, residenceApplicatorPanel)
				self.mResidenceApplicatorPanels.append(residenceApplicatorPanelPath)
				self.mResidenceApplicatorNames.append(residenceApplicatorNamePath)
				self.mResidenceApplicatorMessages.append(residenceApplicatorMessagePath)
				self.mResidencePlaceBlockImgs.append(residencePlaceBlockImg)
				self.mResidenceUseDoorImgs.append(residenceUseDoorImg)
				self.mResidenceEnterImgs.append(residenceEnterImg)
				self.mResidenceAcceptBtns.append(residenceAcceptBtn)
				self.mResidenceRefuseBtns.append(residenceRefuseBtn)
				self.mResidenceApplicatorNewImgs.append(residenceApplicatorNewImg)
		elif deltaNum < 0:
			for i in xrange(applicatorNum + 1, len(self.mResidenceApplicatorPanels) + 1):
				if i == 1:
					continue
				print 'removing CheckPanel ', i
				residenceApplicatorPanel = "ResidenceApplicator%s" % i
				residenceApplicatorPanelPath = "%s/%s" % (self.mResidenceApplicatorParentPanel, residenceApplicatorPanel)
				residenceApplicatorNamePath = residenceApplicatorPanelPath + "/label34"
				residenceApplicatorMessagePath = residenceApplicatorPanelPath + "/label35"
				residencePlaceBlockImg = residenceApplicatorPanelPath + "/image46"
				residenceUseDoorImg = residenceApplicatorPanelPath + "/image52"
				residenceEnterImg = residenceApplicatorPanelPath + "/image53"
				residenceAcceptBtn = residenceApplicatorPanelPath + "/button22"
				residenceRefuseBtn = residenceApplicatorPanelPath + "/button21"
				residenceApplicatorNewImg = residenceApplicatorPanelPath + "/image49"
				self.RemoveComponent(residenceApplicatorPanelPath, self.mResidenceApplicatorParentPanel)
				self.mResidenceApplicatorPanels.remove(residenceApplicatorPanelPath)
				self.mResidenceApplicatorNames.remove(residenceApplicatorNamePath)
				self.mResidenceApplicatorMessages.remove(residenceApplicatorMessagePath)
				self.mResidencePlaceBlockImgs.remove(residencePlaceBlockImg)
				self.mResidenceUseDoorImgs.remove(residenceUseDoorImg)
				self.mResidenceEnterImgs.remove(residenceEnterImg)
				self.mResidenceAcceptBtns.remove(residenceAcceptBtn)
				self.mResidenceRefuseBtns.remove(residenceRefuseBtn)
				self.mResidenceApplicatorNewImgs.remove(residenceApplicatorNewImg)
		# 其余情况，正常显示
		print "608", self.mResidenceApplicatorPanel1
		d = self.GetSize(self.mResidenceApplicatorPanel1)[1]
		for i, residenceApplicatorPanelPath in enumerate(self.mResidenceApplicatorPanels):
			self.SetPosition(residenceApplicatorPanelPath, (self.mResidenceApplicatorPanelPos[0], self.mResidenceApplicatorPanelPos[1] + d * i))
		i = 0
		self.mAllApplicatorUid = []
		self.mAllApplicatorNames = []
		self.mAllApplicatorAuthority = []
		for uid, oneResApplication in resApplication.iteritems():
			self.mAllApplicatorUid.append(uid)
			self.mAllApplicatorNames.append(oneResApplication["username"])
			self.mAllApplicatorAuthority.append(oneResApplication["authority"])
			self.SetText(self.mResidenceApplicatorNames[i], oneResApplication["username"].encode('utf-8'))
			self.SetText(self.mResidenceApplicatorMessages[i], oneResApplication["applicationMessage"].encode('utf-8'))
			self.SetSprite(self.mResidencePlaceBlockImgs[i], "textures/ui/netease_residence/tag03.png" if oneResApplication["authority"]["PlacedBlock"] == True else "textures/ui/netease_residence/tag02.png")
			self.SetSprite(self.mResidenceUseDoorImgs[i], "textures/ui/netease_residence/tag03.png" if oneResApplication["authority"]["UseDoor"] == True else "textures/ui/netease_residence/tag02.png")
			self.SetSprite(self.mResidenceEnterImgs[i], "textures/ui/netease_residence/tag03.png" if oneResApplication["authority"]["Enter"] == True else "textures/ui/netease_residence/tag02.png")
			self.SetVisible(self.mResidenceApplicatorNewImgs[i], self.ShowNews(uid, self.mChosenResId))
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mResidenceApplicatorSize[1])
		self.SetSize(self.mResidenceApplicatorParentPanel, (self.mResidenceApplicatorSize[0], height))
		self.mClientSystem.GetResidenceMgr().UpdateApplicatorListState(self.mChosenResId, True)
		self.mClientSystem.NotifyToServer("ApplicatorHasReadFromClientEvent", {"resId":self.mChosenResId, "playerId":self.mLocalPlayerId})
		
	def ShowNews(self, uid, resId):
		if self.mClientSystem.GetResidenceMgr().mApplicatorUidUnRead.has_key(resId) and uid in self.mClientSystem.GetResidenceMgr().mApplicatorUidUnRead[resId]:
			return True
		else:
			return False
			
			
	def ShowBtnImgs(self, uid, changeAuth, state):
		index = self.mAllUserUid.index(uid)
		print "ShowBtnImgs", index, uid, changeAuth, state
		if index < 0 or index > len(self.mResidenceUserPanels) :
			return
		if changeAuth == "PlacedBlock":
			self.SetVisible(self.mResidencePlaceBlockBtnImgs[index], state == True )
		elif changeAuth == "UseDoor":
			print "self.mResidenceUseDoorBtnImgs[index]", self.mResidenceUseDoorBtnImgs[index]
			self.SetVisible(self.mResidenceUseDoorBtnImgs[index], state == True)
		elif changeAuth == "Enter":
			print "self.mResidenceEnterBtnImgs[index]", self.mResidenceEnterBtnImgs[index]
			self.SetVisible(self.mResidenceEnterBtnImgs[index], state == True)
		else:
			return
	
	def OnResidenceUserBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mManageApplicatorTabelPanel, False)
			self.SetVisible(self.mManageUserTabelPanel, True)
			self.SetVisible(self.mResidenceApplicatorScroll, False)
			self.mCurrentPage = "user"
			self.RefreshUser()
			
	def RefreshUser(self):
		if self.mCurrentPage != "user":
			return
		if self.mChosenResId == -1:
			self.SetVisible(self.mResidenceUserScroll, False)
			return
		else:
			self.SetVisible(self.mResidenceUserScroll, True)
		#TODO 获取玩家的领地使用者列表
		resUser = self.mClientSystem.GetResidenceMgr().mResAuthority.get(self.mChosenResId)
		print "reUser", self.mChosenResId, resUser
		if resUser is None:
			self.SetVisible(self.mResidenceUserScroll, False)
			return
		userNum = len(resUser)
		if userNum > 0:
			self.SetVisible(self.mResidenceUserScroll, True)
		else:
			self.SetVisible(self.mResidenceUserScroll, False)
			return
		deltaNum = userNum - len(self.mResidenceUserPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceUserPanels) + 1, userNum + 1):
				residenceUserPanel = "ResidenceUser%s" % i
				residenceUserPanelPath = "%s/%s" % (self.mResidenceUserParentPanel, residenceUserPanel)
				residenceUserNamePath = residenceUserPanelPath + "/label39"
				residencePlaceBlockBtn = residenceUserPanelPath + "/button15"
				residencePlaceBlockImg = residencePlaceBlockBtn + "/image31"
				residenceUseDoorBtn = residenceUserPanelPath + "/button16"
				residenceUseDoorImg = residenceUseDoorBtn + "/image33"
				residenceEnterBtn = residenceUserPanelPath + "/button17"
				residenceEnterImg = residenceEnterBtn + "/image131"
				self.Clone(self.mResidenceUserPanel1, self.mResidenceUserParentPanel,residenceUserPanel)
				self.mResidenceUserPanels.append(residenceUserPanelPath)
				self.mResidenceUserNames.append(residenceUserNamePath)
				self.mResidencePlaceBlockBtnImgs.append(residencePlaceBlockImg)
				self.mResidenceUseDoorBtnImgs.append(residenceUseDoorImg)
				self.mResidenceEnterBtnImgs.append(residenceEnterImg)
		elif deltaNum < 0:
			for i in xrange(userNum + 1, len(self.mResidenceUserPanels) + 1):
				if i == 1:
					continue
				residenceUserPanel = "ResidenceUser%s" % i
				residenceUserPanelPath = "%s/%s" % (self.mResidenceUserParentPanel, residenceUserPanel)
				residenceUserNamePath = residenceUserPanelPath + "/label39"
				residencePlaceBlockBtn = residenceUserPanelPath + "/button15"
				residencePlaceBlockImg = residencePlaceBlockBtn + "/image31"
				residenceUseDoorBtn = residenceUserPanelPath + "/button16"
				residenceUseDoorImg = residenceUseDoorBtn + "/image33"
				residenceEnterBtn = residenceUserPanelPath + "/button17"
				residenceEnterImg = residenceEnterBtn + "/image131"
				self.Clone(self.mResidenceUserPanel1, self.mResidenceUserParentPanel, residenceUserPanel)
				self.mResidenceUserPanels.remove(residenceUserPanelPath)
				self.mResidenceUserNames.remove(residenceUserNamePath)
				self.mResidencePlaceBlockBtnImgs.remove(residencePlaceBlockImg)
				self.mResidenceUseDoorBtnImgs.remove(residenceUseDoorImg)
				self.mResidenceEnterBtnImgs.remove(residenceEnterImg)
				self.RemoveComponent(residenceUserPanelPath, self.mResidenceUserParentPanel)
		# 其余情况，正常显示
		d = self.GetSize(self.mResidenceUserPanel1)[1]
		for i, residenceUserPanelPath in enumerate(self.mResidenceUserPanels):
			self.SetPosition(residenceUserPanelPath, (self.mResidenceUserPanelPos[0], self.mResidenceUserPanelPos[1] + d * i))
		i = 0
		self.mAllUserUid = []
		self.mAllUserNames = []
		for uid, oneResAuthority in resUser.iteritems():
			self.mAllUserUid.append(uid)
			#TODO 设置使用者信息
			self.SetText(self.mResidenceUserNames[i], oneResAuthority["username"].encode('utf-8'))
			self.mAllUserNames.append(oneResAuthority["username"])
			self.SetVisible(self.mResidencePlaceBlockBtnImgs[i], True if oneResAuthority["authority"]["PlacedBlock"] == True else False)
			self.SetVisible(self.mResidenceUseDoorBtnImgs[i], True if oneResAuthority["authority"]["UseDoor"] == True else False)
			self.SetVisible(self.mResidenceEnterBtnImgs[i], True if oneResAuthority["authority"]["Enter"] == True else False)
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mResidenceUserSize[1])
		self.SetSize(self.mResidenceUserParentPanel, (self.mResidenceUserSize[0], height))
		
	def ShowTransferMainNewImg(self, visible):
		self.SetVisible(self.mTransferNewImg, visible)
		
	def ShowManageMainNewImg(self, visible):
		self.SetVisible(self.mManageNewImg, visible)
		self.SetVisible(self.mResidenceCheckBtnNewImg, visible)
		self.SetVisible(self.mApplicatorBtnNewImg, visible)
		