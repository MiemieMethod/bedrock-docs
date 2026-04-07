# -*- coding: utf-8 -*-
import random
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
from neteaseResidenceScript.ui.uiDef import UIDef
import neteaseResidenceScript.residenceConsts as residenceConsts
import weakref

CheckTimeIntervalMax = 1.5

class ResidenceApplyUIScreen(ScreenNode):
	"""
	申请权限界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		
		self.mApplyPanel = "/ApplyPanel"
		self.mCloseBtn = self.mApplyPanel + "/close_button"#关闭
		self.mApplyBtn = self.mApplyPanel + "/apply_button"#申请页面按钮
		self.mTransferBtn = self.mApplyPanel + "/transfer_button"#传送页面按钮
		self.mTransferNewImg = self.mTransferBtn + "/image16"#传送页面按钮
		self.mGiveBtn = self.mApplyPanel + "/give_button"#赋予页面按钮
		self.mManageBtn = self.mApplyPanel + "/manage_button"#管理页面按钮
		self.mManageNewImg = self.mManageBtn + "/image14"#管理页面按钮
		self.mMyBtn = self.mApplyPanel + "/my_button"#管理页面按钮
		self.mApplySecondPanel = self.mApplyPanel + "/panel3"
		
		self.mApplyTipsPanel = self.mApplySecondPanel + "/tipsimage"#提示语
		self.mApplyTipsLabel = self.mApplyTipsPanel + "/tipslabel"
		
		self.mApplyPanelImg = self.mApplySecondPanel + "/image0"
		self.mApplicatorNameText = self.mApplyPanelImg + "/text_edit_box2"#访客名字
		self.mApplicatorMessage = self.mApplyPanelImg + "/text_edit_box3"#留言
		self.mApplySendBtn = self.mApplyPanelImg + "/button1"#发送申请
		self.mResidenceCheckBtn = self.mApplyPanelImg + "/button10"#领地查询按钮
		self.mResidenceShowCheckText = self.mResidenceCheckBtn + "/label22"#领地查询按钮文字
		self.mResidenceCheckScroll = self.mResidenceCheckBtn + "/scroll_view7"#查询到的领地下拉框
		self.mApplyResidenceScroll = self.mApplyPanelImg + "/scroll_view5"#权限列表
		
		self.mApplicatorName = ""
		self.mApplicationMessage = ""
		
		self.gameComp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "SearchResidenceResultFromServerEvent", self, self.OnShowSearchResidenceResult)
		self.SetTouchEnable(self.mApplyBtn, False)
		self.AddTouchEventHandler(self.mApplyBtn, self.mClientSystem.OnApplyBtn)
		self.AddTouchEventHandler(self.mTransferBtn, self.mClientSystem.OnTransferBtn)
		self.AddTouchEventHandler(self.mGiveBtn, self.mClientSystem.OnGiveBtn)
		self.AddTouchEventHandler(self.mManageBtn, self.mClientSystem.OnManageBtn)
		self.AddTouchEventHandler(self.mMyBtn, self.mClientSystem.OnMyBtn)
		
	def InitScreen(self):
		self.ChangeScreenVisible(False)
		self.SetVisible(self.mResidenceCheckScroll, False)
		self.SetVisible(self.mApplyTipsPanel, False)
		#self.SetVisible(self.mTransferNewImg, False)
		
		
	def Create(self):
		#权限的scroll
		mApplyResidenceScrollTouch = self.mApplyResidenceScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		applyresidence_size = self.GetSize(mApplyResidenceScrollTouch)
		if applyresidence_size:
			self.mApplyResidencePanel = mApplyResidenceScrollTouch
			self.mApplyResidenceSize = applyresidence_size
		else:
			mApplyResidenceScrollTouch = self.mApplyResidenceScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			applyresidence_size = self.GetSize(mApplyResidenceScrollTouch)
			self.mApplyResidencePanel = mApplyResidenceScrollTouch
			self.mApplyResidenceSize = applyresidence_size
		self.mResidencePlaceBlockBtn = self.mApplyResidencePanel + "/panel9/image69/button4"
		self.mResidenceUseDoorBtn = self.mApplyResidencePanel + "/panel9/image69/button8"
		self.mResidenceEnterBtn = self.mApplyResidencePanel + "/panel9/image69/button9"
		#领地信息的scroll
		mResidenceCheckScrollTouch = self.mResidenceCheckScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residencecheck_size = self.GetSize(mResidenceCheckScrollTouch)
		if residencecheck_size:
			self.mResidenceCheckPanel = mResidenceCheckScrollTouch
			self.mResidenceCheckSize = residencecheck_size
		else:
			mResidenceCheckScrollTouch = self.mResidenceCheckScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residencecheck_size = self.GetSize(mResidenceCheckScrollTouch)
			self.mResidenceCheckPanel = mResidenceCheckScrollTouch
			self.mResidenceCheckSize = residencecheck_size
		self.mResidenceCheckPanel1 = self.mResidenceCheckPanel + "/ResidenceCheckPanel1"
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
		
		self.AddTouchEventHandler(self.mResidenceCheckBtn, self.OnResidenceCheckBtn)
		
		self.AddTouchEventHandler(self.mApplySendBtn, self.OnApplySendBtn)
		
		for index, residenceChooseBtn in enumerate(self.mResidenceChooseBtns):
			self.AddTouchEventHandler(residenceChooseBtn, self.OnResidenceChooseBtn)
			
		self.mResidenceState = {
			"PlacedBlock":True,
			"UseDoor":True,
			"Enter":True
		}
		self.mAllCheckResidence = [] #所有查找到的领地id
		self.mChosenResId = -1
		self.mLastCheckTime = 0
	
	def OnResidenceCheckBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			print "OnResidenceCheckBtn", self.mApplicatorName
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				#TODO 提示不能点太快
				self.ShowTips("不能点太快!")
				return
			if self.mApplicatorName == "":
				self.ShowTips("你输入的玩家名字为空!")
				return
			else:
				self.mLastCheckTime = now
				dict = {
					"playerId":self.mLocalPlayerId,
					"applicatorName":self.mApplicatorName
				}
				self.mClientSystem.NotifyToServer("CheckPlayerResidenceFromClient",dict)
	
	def OnResidenceChooseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			print "OnResidenceChooseBtn", self.mAllCheckResidence
			resIndex = self.GetResIdIndex(args["ButtonPath"])
			resData = self.mAllCheckResidence[resIndex]
			#data = {'playerId': self.mLocalPlayerId, "resId":resId}
			self.mChosenResId = resData["resId"]
			self.SetVisible(self.mResidenceCheckScroll, False)
			self.SetText(self.mResidenceShowCheckText, resData["resName"].encode('utf-8'))
			#self.SetText(self.mResidenceShowCheckText, resData["resName"].encode('utf-8'))
			
	
	def GetResIdIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceChooseBtns):
			if btnPath == path:
				return index
		return -1
	
	def OnResidenceShow(self, args):
		pass
	
	def OnApplySendBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			now = time.time()
			if (now - self.mLastCheckTime) < CheckTimeIntervalMax:
				# TODO 提示不能点太快
				self.ShowTips("不能点太快!")
				return
			if self.mChosenResId == -1:
				#没选择任何ID
				self.ShowTips("没选择任何领地！")
				return
			elif True not in self.mResidenceState.values():
				#没选择任何权限
				self.ShowTips("没选择任何权限！")
				return
			elif self.mApplicationMessage == "":
				self.ShowTips("留言不能为空！")
				return
			elif self.mApplicationMessage == "***":
				self.ShowTips("输入语违法！")
				return
			else:
				dict = {
					"playerId": self.mLocalPlayerId,
					"chosenResId": self.mChosenResId,
					"authorityState": self.mResidenceState,
					"applicationMessage":self.mApplicationMessage
				}
				self.mClientSystem.NotifyToServer("ApplicationResidenceFromClient", dict)
				
	def ShowTips(self, message):
		self.mClientSystem.NotifyToServer("ShowTipsFromClientEvent", {"playerId": self.mLocalPlayerId, "message":message})
	
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
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def name_text_box_content(self):
		#print "name_text_box_content", self.mApplicatorName
		return self.mApplicatorName
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def name_text_box(self, args):
		print "name_text_box", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mApplicatorName = args["Text"]
		return ViewRequest.Refresh
	
	
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def message_text_box_content(self):
		return self.mApplicationMessage
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_box(self, args):
		#print "message_text_box", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		# print 'set_input_string', args
		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		if comp:
			if comp.CheckWordsValid(args["Text"]):
				self.mApplicationMessage = args["Text"]
			else:
				self.mApplicationMessage = "***"
		return ViewRequest.Refresh
	
		
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
		else:
			self.ChangeScreenVisible(False)
		
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.mIsShow = flag
		if flag:
			extraClientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	def Show(self):
		self.ChangeScreenVisible(True)
		self.SetVisible(self.mResidenceCheckScroll, False)
		self.SetVisible(self.mApplyTipsPanel, False)
		#self.SetVisible(self.mTransferNewImg, len(self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead) > 0)
		
	def OnShowSearchResidenceResult(self, args):
		# print "OnShowSearchResidenceResult", args
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
				residenceCheckPanel = "ResidenceCheckPanel%s" % i
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
				residenceCheckPanel = "ResidenceCheckPanel%s" % i
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
			self.SetPosition(residenceCheckPanelPath, (self.mResidenceCheckPanelPos[0], self.mResidenceCheckPanelPos[1] + d * i))
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
		height = max(height, self.mResidenceCheckSize[1])
		self.SetSize(self.mResidenceCheckPanel, (self.mResidenceCheckSize[0], height))
		
	def ShowTransferMainNewImg(self, visible):
		self.SetVisible(self.mTransferNewImg, visible)
		
	def ShowManageMainNewImg(self, visible):
		self.SetVisible(self.mManageNewImg, visible)