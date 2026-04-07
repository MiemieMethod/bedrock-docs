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

class ResidenceGiveUIScreen(ScreenNode):
	"""
	权限赋予界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		
		self.mGivePanel = "/givePanel"
		self.mCloseBtn = self.mGivePanel + "/close_button"#关闭
		self.mApplyBtn = self.mGivePanel + "/apply_button"#申请页面按钮
		self.mTransferBtn = self.mGivePanel + "/transfer_button"#传送页面按钮
		self.mTransferNewImg = self.mTransferBtn + "/image16"  # 传送页面按钮
		self.mGiveBtn = self.mGivePanel + "/give_button"#赋予页面按钮
		self.mManageBtn = self.mGivePanel + "/manage_button"#管理页面按钮
		self.mManageNewImg = self.mManageBtn + "/image14"  # 管理页面按钮
		self.mMyBtn = self.mGivePanel + "/my_button"#管理页面按钮
		self.mGiveSecondPanel = self.mGivePanel + "/panel7"
		self.mGivePanelImg = self.mGiveSecondPanel + "/image19"
		self.mGiveNameText = self.mGivePanel + "/text_edit_box0"  # 访客名字
		self.mGiveSendBtn = self.mGivePanelImg + "/button8"  # 发送申请
		#self.mResidenceCheckBtn = self.mGivePanelImg + "/button10"  # 领地查询按钮
		#self.mResidenceCheckText = self.mResidenceCheckBtn + "/label22"  # 领地查询按钮文字
		self.mResidenceCheckBtn = self.mGivePanelImg + "/button0"  # 查询到的领地按钮
		self.mChosenResNameText = self.mResidenceCheckBtn + "/label1"  # 选择的领地
		self.mResidenceCheckScroll = self.mResidenceCheckBtn + "/scroll_view2"  # 查询到的领地下拉框
		self.mGiveResidenceScroll = self.mGivePanelImg + "/scroll_view1"  # 权限列表
		self.mTipImg = self.mGiveSecondPanel + "/image25"
		self.mTipLabel = self.mTipImg + "/label32"
		
		self.mGiveTipsPanel = self.mGivePanelImg + "/image25"  # 提示语
		self.mGiveTipsLabel = self.mGiveTipsPanel + "/label32"
		
		self.mGiverName = ""
		self.gameComp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "SearchResidenceResultByIdFromServerEvent", self, self.OnShowSearchResidenceResult)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "GiveSendPlayerResultFromServerEvent", self, self.OnGiveSendPlayerNotExistsFromServerEvent)
		self.AddTouchEventHandler(self.mApplyBtn, self.mClientSystem.OnApplyBtn)
		self.AddTouchEventHandler(self.mTransferBtn, self.mClientSystem.OnTransferBtn)
		self.SetTouchEnable(self.mGiveBtn, False)
		self.AddTouchEventHandler(self.mGiveBtn, self.mClientSystem.OnGiveBtn)
		self.AddTouchEventHandler(self.mManageBtn, self.mClientSystem.OnManageBtn)
		self.AddTouchEventHandler(self.mMyBtn, self.mClientSystem.OnMyBtn)
		
	def Show(self):
		self.ChangeScreenVisible(True)
		#self.SetVisible(self.mTransferNewImg, len(self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead) > 0)
		self.InitScreenManage()
	
	def OnShowSearchResidenceResult(self, args):
		#print "OnShowSearchResidenceResult", args
		if self.mIsShow == False:
			return
		resList = args.get("resList")
		resNum = len(resList)
		if resNum <= 0:
			self.SetVisible(self.mResidenceCheckScroll, False)
		else:
			self.SetVisible(self.mResidenceCheckScroll, True)
		
		deltaNum = resNum - len(self.mResidenceCheckPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceCheckPanels) + 1, resNum + 1):
				residenceCheckPanel = "residenceMyPanel%s" % i
				residenceCheckPanelPath = "%s/%s" % (self.mResidenceCheckPanel, residenceCheckPanel)
				residenceCheckTextPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceCheckText)
				residenceChooseBtnPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceChooseBtn)
				residenceChooseBtnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnChosenImg)
				residenceChooseBtnUnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnUnChosenImg)
				self.Clone(self.mResidenceCheckPanel1, self.mResidenceCheckPanel, residenceCheckPanel)
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
				residenceCheckPanel = "residenceMyPanel%s" % i
				residenceCheckPanelPath = "%s/%s" % (self.mResidenceCheckPanel, residenceCheckPanel)
				residenceCheckTextPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceCheckText)
				residenceChooseBtnPath = "%s/%s" % (residenceCheckPanelPath, self.mResidenceChooseBtn)
				residenceChooseBtnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnChosenImg)
				residenceChooseBtnUnChosenImgPath = "%s/%s" % (residenceChooseBtnPath, self.mResidenceChooseBtnUnChosenImg)
				self.RemoveComponent(residenceCheckPanelPath, self.mResidenceCheckPanel)
				self.mResidenceCheckPanels.remove(residenceCheckPanelPath)
				self.mResidenceCheckTexts.remove(residenceCheckTextPath)
				self.mResidenceChooseBtns.remove(residenceChooseBtnPath)
				self.mResidenceChooseBtnChosenImgs.remove(residenceChooseBtnChosenImgPath)
				self.mResidenceChooseBtnUnChosenImgs.remove(residenceChooseBtnUnChosenImgPath)
		# 其余情况，正常显示
		print self.mResidenceCheckPanel1, self.GetSize(self.mResidenceCheckPanel1)
		d = self.GetSize(self.mResidenceCheckPanel1)[1]
		for i, residenceCheckPanelPath in enumerate(self.mResidenceCheckPanels):
			self.SetPosition(residenceCheckPanelPath,
			                 (self.mResidenceCheckPanelPos[0], self.mResidenceCheckPanelPos[1] + d * i))
		i = 0
		self.mAllCheckResidence = []
		#self.mAllCheckResidenceNames = []
		for idx, resData in enumerate(resList):
			self.mAllCheckResidence.append(resData)
			#self.mAllCheckResidenceNames.append(resData["resName"])
			self.SetText(self.mResidenceCheckTexts[i], resData["resName"].encode('utf-8'))
			if resData["resId"] == self.mChosenResId:
				self.SetVisible(self.mResidenceChooseBtnChosenImgs[i], True)
			else:
				self.SetVisible(self.mResidenceChooseBtnChosenImgs[i], False)
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mResidenceCheckSize[1])
		self.SetSize(self.mResidenceCheckPanel, (self.mResidenceCheckSize[0], height))
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
		self.InitScreenManage()
		
	def InitScreenManage(self):
		self.SetVisible(self.mResidenceCheckScroll, False)
		#self.SetVisible(self.mResidenceCheckScroll, False)
		self.SetVisible(self.mGiveTipsPanel, False)
		
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
		# 权限的scroll
		mGiveResidenceScrollTouch = self.mGiveResidenceScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		giveresidence_size = self.GetSize(mGiveResidenceScrollTouch)
		if giveresidence_size:
			self.mGiveResidencePanel = mGiveResidenceScrollTouch
			self.mGiveResidenceSize = giveresidence_size
		else:
			mGiveResidenceScrollTouch = self.mGiveResidenceScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			giveresidence_size = self.GetSize(mGiveResidenceScrollTouch)
			self.mGiveResidencePanel = mGiveResidenceScrollTouch
			self.mGiveResidenceSize = giveresidence_size
		self.mResidencePlaceBlockBtn = self.mGiveResidencePanel + "/panel9/image69/button1"
		self.mResidenceUseDoorBtn = self.mGiveResidencePanel + "/panel9/image69/button4"
		self.mResidenceEnterBtn = self.mGiveResidencePanel + "/panel9/image69/button9"
		# 领地信息的scroll
		mResidenceChooseScrollTouch = self.mResidenceCheckScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residencechoose_size = self.GetSize(mResidenceChooseScrollTouch)
		if residencechoose_size:
			self.mResidenceCheckPanel = mResidenceChooseScrollTouch
			self.mResidenceCheckSize = residencechoose_size
		else:
			mResidenceChooseScrollTouch = self.mResidenceCheckScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residencechoose_size = self.GetSize(mResidenceChooseScrollTouch)
			self.mResidenceCheckPanel = mResidenceChooseScrollTouch
			self.mResidenceCheckSize = residencechoose_size
		#self.mResidenceCheckBtnLabel = self.mResidenceCheckPanel + "/label2"
		self.mResidenceCheckPanel1 = self.mResidenceCheckPanel + "/residenceMyPanel1"
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
		
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
		self.AddTouchEventHandler(self.mResidencePlaceBlockBtn, self.OnResidencePlaceBlockBtn)
		
		self.AddTouchEventHandler(self.mResidenceUseDoorBtn, self.OnResidenceUseDoorBtn)
		
		self.AddTouchEventHandler(self.mResidenceEnterBtn, self.OnResidenceEnterBtn)
		
		self.AddTouchEventHandler(self.mGiveSendBtn, self.OnGiveSendBtn)
		
		self.AddTouchEventHandler(self.mResidenceCheckBtn, self.OnResidenceCheckBtn)
		
		for index, residenceChooseBtn in enumerate(self.mResidenceChooseBtns):
			self.AddTouchEventHandler(residenceChooseBtn, self.OnResidenceChooseBtn)
		
		self.mResidenceState = {
			"PlacedBlock":True,
			"UseDoor":True,
			"Enter":True
		}
		
		self.mAllCheckResidence = [] #所有查找到的领地
		#self.mAllCheckResidenceNames = []
		self.mChosenResId = -1
		
	def OnResidenceCheckBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.OnSearchMyResidence()
			
			
	def OnSearchMyResidence(self):
		# TODO 点击我的领地触发
		dict = {
			"playerId": self.mLocalPlayerId
		}
		self.mClientSystem.NotifyToServer("CheckPlayerResidenceByIdFromClient", dict)
	
	
	def OnResidenceEnterBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.mResidenceState["Enter"] = not self.mResidenceState["Enter"]
			if self.mResidenceState["Enter"] == False:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_off.png")
			else:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_on.png")
	
	def OnResidencePlaceBlockBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.mResidenceState["PlacedBlock"] = not self.mResidenceState["PlacedBlock"]
			if self.mResidenceState["PlacedBlock"] == False:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_off.png")
			else:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_on.png")
	
	def OnResidenceUseDoorBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.mResidenceState["UseDoor"] = not self.mResidenceState["UseDoor"]
			if self.mResidenceState["UseDoor"] == False:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_off.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_off.png")
			else:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_residence/switch_on.png")
				self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_residence/switch_on.png")
			
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
		else:
			self.ChangeScreenVisible(False)
		
	def OnGiveSendBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			if self.mChosenResId == -1:
				#没选择任何ID
				self.ShowTips("没选择任何领地！")
				return
			elif len(self.mGiverName) <= 0:
				# 没选择任何权限
				self.ShowTips("请输入一个玩家名称！")
				return
			elif True not in self.mResidenceState.values():
				#没选择任何权限
				self.ShowTips("没选择任何权限！")
				return
			else:
				dict = {
					"playerId": self.mLocalPlayerId,
					"giverName": self.mGiverName,
					"chosenResId": self.mChosenResId,
					"authorityState": self.mResidenceState,
				}
				self.mClientSystem.NotifyToServer("GiveSendFromClientEvent", dict)
				
	def OnGiveSendPlayerNotExistsFromServerEvent(self, args):
		self.ShowTips(args.get("message").encode("utf-8"))
	
	def ShowTips(self, message):
		self.mClientSystem.NotifyToServer("ShowTipsFromClientEvent",
		                                  {"playerId": self.mLocalPlayerId, "message": message})
				
	def OnResidenceChooseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			resIndex = self.GetResIdIndex(args["ButtonPath"])
			resData = self.mAllCheckResidence[resIndex]
			#data = {'playerId': self.mLocalPlayerId, "resId":resId}
			self.mChosenResId = resData["resId"]
			self.SetVisible(self.mResidenceCheckScroll, False)
			self.SetText(self.mChosenResNameText, resData["resName"].encode('utf-8'))
			
	def GetResIdIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceChooseBtns):
			if btnPath == path:
				return index
		return -1
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def message_text_box_content(self):
		return self.mGiverName
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_box(self, args):
		# print "SearchTextBox  ", args
		self.mGiverName = args["Text"]
		
	def ShowTransferMainNewImg(self, visible):
		self.SetVisible(self.mTransferNewImg, visible)
		
	def ShowManageMainNewImg(self, visible):
		self.SetVisible(self.mManageNewImg, visible)