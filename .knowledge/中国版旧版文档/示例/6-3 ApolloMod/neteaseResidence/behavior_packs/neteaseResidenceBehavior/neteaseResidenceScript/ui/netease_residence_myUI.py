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
import neteaseResidenceScript.util as util
import itertools
import neteaseResidenceScript.effect.effectFunc as effectFunc

class ResidenceMyUIScreen(ScreenNode):
	"""
	领地管理界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.SHOW_RES_PRE_EFFECT = True
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		
		self.mMyPanel = "/panel0"
		self.mCloseBtn = self.mMyPanel + "/close_button"#关闭
		self.mApplyBtn = self.mMyPanel + "/apply_button"#申请页面按钮
		self.mTransferBtn = self.mMyPanel + "/transfer_button"#传送页面按钮
		self.mTransferNewImg = self.mTransferBtn + "/image116"  # 传送页面按钮
		self.mGiveBtn = self.mMyPanel + "/give_button"#赋予页面按钮
		self.mManageBtn = self.mMyPanel + "/manage_button"#管理页面按钮
		self.mManageNewImg = self.mManageBtn + "/image114"  # 管理页面按钮
		self.mMyBtn = self.mMyPanel + "/my_button"#管理页面按钮
		self.mMySecondPanel = self.mMyPanel + "/panel1"
		self.mMySecondPanelImg = self.mMySecondPanel + "/image7"
		self.mMySecondPanelImgPanel = self.mMySecondPanelImg + "/panel4"
		self.mMyResidenceScroll = self.mMySecondPanelImgPanel + "/scroll_view0"
		self.mMyNewResidenceBtn = self.mMySecondPanelImg + "/button9"
		
		#新建领地panel
		self.mMyNewResidencePanel = self.mMyPanel + "/panel5"
		self.mMyNewResidencePanelImg = self.mMyNewResidencePanel + "/image10"
		self.mMyRealNewResidenceBtn = self.mMyNewResidencePanelImg + "/button23"
		self.mMyRealNewResidenceBtnLabel = self.mMyRealNewResidenceBtn + "/label12"
		self.mMyRealNewResidenceCloseBtn = self.mMyNewResidencePanelImg + "/button10"
		self.mMyRealNewResidenceNameText = self.mMyNewResidencePanelImg + "/text_edit_box0/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMinXText = self.mMyNewResidencePanelImg + "/text_edit_box1/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMinYText = self.mMyNewResidencePanelImg + "/text_edit_box2/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMinZText = self.mMyNewResidencePanelImg + "/text_edit_box3/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMaxXText = self.mMyNewResidencePanelImg + "/text_edit_box4/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMaxYText = self.mMyNewResidencePanelImg + "/text_edit_box5/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealNewResidenceMaxZText = self.mMyNewResidencePanelImg + "/text_edit_box6/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mNewMinXAddBtn = self.mMyNewResidencePanelImg + "/button11"
		self.mNewMinXMinusBtn = self.mMyNewResidencePanelImg + "/button12"
		self.mNewMinYAddBtn = self.mMyNewResidencePanelImg + "/button13"
		self.mNewMinYMinusBtn = self.mMyNewResidencePanelImg + "/button14"
		self.mNewMinZAddBtn = self.mMyNewResidencePanelImg + "/button16"
		self.mNewMinZMinusBtn = self.mMyNewResidencePanelImg + "/button15"
		
		self.mNewMaxXAddBtn = self.mMyNewResidencePanelImg + "/button17"
		self.mNewMaxXMinusBtn = self.mMyNewResidencePanelImg + "/button18"
		self.mNewMaxYAddBtn = self.mMyNewResidencePanelImg + "/button19"
		self.mNewMaxYMinusBtn = self.mMyNewResidencePanelImg + "/button20"
		self.mNewMaxZAddBtn = self.mMyNewResidencePanelImg + "/button21"
		self.mNewMaxZMinusBtn = self.mMyNewResidencePanelImg + "/button22"
		
		self.mNewResidenceName = ""
		self.mNewResidenceMinX = ""
		self.mNewResidenceMinY = ""
		self.mNewResidenceMinZ = ""
		self.mNewResidenceMaxX = ""
		self.mNewResidenceMaxY = ""
		self.mNewResidenceMaxZ = ""
	
		# 改建领地panel
		self.mMyChangeResidencePanel = self.mMyPanel + "/panel6"
		self.mMyChangeResidencePanelImg = self.mMyChangeResidencePanel + "/image24"
		self.mMyRealChangeResidenceBtn = self.mMyChangeResidencePanelImg + "/button37"
		self.mMyRealChangeResidenceBtnLabel = self.mMyRealChangeResidenceBtn + "/label17"
		self.mMyRealChangeResidenceNameText = self.mMyChangeResidencePanelImg + "/label14"
		self.mMyRealChangeResidenceCloseBtn = self.mMyChangeResidencePanelImg + "/button25"
		self.mMyRealChangeResidenceMinXText = self.mMyChangeResidencePanelImg + "/text_edit_box8/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealChangeResidenceMinYText = self.mMyChangeResidencePanelImg + "/text_edit_box9/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealChangeResidenceMinZText = self.mMyChangeResidencePanelImg + "/text_edit_box10/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealChangeResidenceMaxXText = self.mMyChangeResidencePanelImg + "/text_edit_box11/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealChangeResidenceMaxYText = self.mMyChangeResidencePanelImg + "/text_edit_box12/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mMyRealChangeResidenceMaxZText = self.mMyChangeResidencePanelImg + "/text_edit_box13/centering_panel/clipper_panel/visibility_panel/place_holder_control"
		self.mChangeMinXAddBtn = self.mMyChangeResidencePanelImg + "/button26"
		self.mChangeMinXMinusBtn = self.mMyChangeResidencePanelImg + "/button27"
		self.mChangeMinYAddBtn = self.mMyChangeResidencePanelImg + "/button28"
		self.mChangeMinYMinusBtn = self.mMyChangeResidencePanelImg + "/button29"
		self.mChangeMinZAddBtn = self.mMyChangeResidencePanelImg + "/button31"
		self.mChangeMinZMinusBtn = self.mMyChangeResidencePanelImg + "/button30"
		
		self.mChangeMaxXAddBtn = self.mMyChangeResidencePanelImg + "/button32"
		self.mChangeMaxXMinusBtn = self.mMyChangeResidencePanelImg + "/button33"
		self.mChangeMaxYAddBtn = self.mMyChangeResidencePanelImg + "/button34"
		self.mChangeMaxYMinusBtn = self.mMyChangeResidencePanelImg + "/button35"
		self.mChangeMaxZAddBtn = self.mMyChangeResidencePanelImg + "/button24"
		self.mChangeMaxZMinusBtn = self.mMyChangeResidencePanelImg + "/button36"
		
		self.mChangeResidenceMinX = ""
		self.mChangeResidenceMinY = ""
		self.mChangeResidenceMinZ = ""
		self.mChangeResidenceMaxX = ""
		self.mChangeResidenceMaxY = ""
		self.mChangeResidenceMaxZ = ""
		
		#确定面板
		self.mSureButtonPanel = self.mMyPanel + "/button38"
		self.mSureButtonPanelImg = self.mSureButtonPanel + "/image38"
		self.mSureButtonPanelClose = self.mSureButtonPanelImg + "/button39"
		self.mSureButtonPanelCostLabel = self.mSureButtonPanelImg + "/image39/label20"
		self.mSureButtonPanelTipsLabel = self.mSureButtonPanelImg + "/label19"
		
		#提示语
		self.mTipsPanel = self.mMyPanel + "/image44"
		self.mTipsLabel = self.mTipsPanel + "/label24"
		self.gameComp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		
		self.mDrawingFrameList = []
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "SearchResidenceResultByIdFromServerEvent", self,
		                                  self.OnShowSearchResidenceResult)
		self.OnSearchMyResidence()
		self.AddTouchEventHandler(self.mApplyBtn, self.mClientSystem.OnApplyBtn)
		self.AddTouchEventHandler(self.mTransferBtn, self.mClientSystem.OnTransferBtn)
		self.AddTouchEventHandler(self.mGiveBtn, self.mClientSystem.OnGiveBtn)
		self.AddTouchEventHandler(self.mManageBtn, self.mClientSystem.OnManageBtn)
		self.SetTouchEnable(self.mMyBtn, False)
		self.AddTouchEventHandler(self.mMyBtn, self.mClientSystem.OnMyBtn)
	
	def Show(self):
		self.ChangeScreenVisible(True)
		#self.InitScreenManage()
		#self.SetVisible(self.mTransferNewImg, len(self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead) > 0)
		self.OnSearchMyResidence()
		
	def OnSearchMyResidence(self):
		#TODO 点击我的领地触发
		dict = {
			"playerId": self.mLocalPlayerId
		}
		self.mClientSystem.NotifyToServer("CheckPlayerResidenceByIdFromClient", dict)
	
	def OnShowSearchResidenceResult(self, args):
		#print "OnShowSearchResidenceResult my", args, self.mIsShow
		if self.mIsShow == False:
			return
		resList = args.get("resList")
		resNum = len(resList)
		if resNum <= 0:
			self.SetVisible(self.mMyResidenceScroll, False)
		else:
			self.SetVisible(self.mMyResidenceScroll, True)
		
		deltaNum = resNum - len(self.mResidenceMyPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceMyPanels) + 1, resNum + 1):
				residenceMyPanel = "myResidence%s" % i
				residenceMyPanelPath = "%s/%s" % (self.mMyResidencePanel, residenceMyPanel)
				residenceMyNamePath = "%s/%s" % (residenceMyPanelPath, "label6")
				residenceMyChangeBtnPath = "%s/%s" % (residenceMyPanelPath, "button7")
				residenceMyTransferBtnPath = "%s/%s" % (residenceMyPanelPath, "button0")
				self.Clone(self.mResidenceMyPanel1, self.mMyResidencePanel, residenceMyPanel)
				self.mResidenceMyPanels.append(residenceMyPanelPath)
				self.mResidenceMyNames.append(residenceMyNamePath)
				self.mResidenceMyChangeBtns.append(residenceMyChangeBtnPath)
				self.mResidenceMyTransderBtns.append(residenceMyTransferBtnPath)
		elif deltaNum < 0:
			for i in xrange(resNum + 1, len(self.mResidenceMyPanels) + 1):
				if i == 1:
					continue
				print 'removing CheckPanel ', i
				residenceMyPanel = "myResidence%s" % i
				residenceMyPanelPath = "%s/%s" % (self.mMyResidencePanel, residenceMyPanel)
				residenceMyNamePath = "%s/%s" % (residenceMyPanelPath, "label6")
				residenceMyChangeBtnPath = "%s/%s" % (residenceMyPanelPath, "button7")
				residenceMyTransferBtnPath = "%s/%s" % (residenceMyPanelPath, "button0")
				self.RemoveComponent(residenceMyPanelPath, self.mResidenceMyPanel)
				self.Clone(self.mResidenceMyPanel1, self.mMyResidencePanel, residenceMyPanel)
				self.mResidenceMyPanels.remove(residenceMyPanelPath)
				self.mResidenceMyNames.remove(residenceMyNamePath)
				self.mResidenceMyChangeBtns.remove(residenceMyChangeBtnPath)
				self.mResidenceMyTransderBtns.remove(residenceMyTransferBtnPath)
		# 其余情况，正常显示
		d = self.GetSize(self.mResidenceMyPanel1)[1]
		for i, residenceMyPanelPath in enumerate(self.mResidenceMyPanels):
			self.SetPosition(residenceMyPanelPath,
			                 (self.mMyResidencePanelPos[0], self.mMyResidencePanelPos[1] + d * i))
		i = 0
		self.mAllMyResidence = []
		for idx, resData in enumerate(resList):
			self.mAllMyResidence.append(resData)
			self.SetText(self.mResidenceMyNames[i], resData["resName"].encode('utf-8'))
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mMyResidenceSize[1])
		self.SetSize(self.mMyResidencePanel, (self.mMyResidenceSize[0], height))
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.mIsShow = flag
		if flag:
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)
			self.ShowOtherPanel(True)
		else:
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	def Create(self):
		# 使用者的scroll
		mMyResidenceScrollTouch = self.mMyResidenceScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		myresidence_size = self.GetSize(mMyResidenceScrollTouch)
		if myresidence_size:
			self.mMyResidencePanel = mMyResidenceScrollTouch
			self.mMyResidencePanelReal = self.mMyResidencePanel + "/panel3"
			self.mMyResidenceSize = myresidence_size
		else:
			mMyResidenceScrollTouch = self.mMyResidenceScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			myresidence_size = self.GetSize(mMyResidenceScrollTouch)
			self.mMyResidencePanel = mMyResidenceScrollTouch
			self.mMyResidencePanelReal = self.mMyResidencePanel + "/panel3"
			self.mMyResidenceSize = myresidence_size
		self.mResidenceMyPanel1 = self.mMyResidencePanelReal + "/myResidence1"
		self.mResidenceMyPanels = [
			self.mResidenceMyPanel1
		]
		self.mResidenceMyName1 = self.mResidenceMyPanel1 + "/label6"
		self.mResidenceMyNames = [
			self.mResidenceMyName1
		]
		self.mResidenceMyChangeBtn1 = self.mResidenceMyPanel1 + "/button7"
		self.mResidenceMyChangeBtns = [
			self.mResidenceMyChangeBtn1
		]
		
		self.mResidenceMyTransferBtn1 = self.mResidenceMyPanel1 + "/button0"
		self.mResidenceMyTransderBtns = [
			self.mResidenceMyTransferBtn1
		]
		
		self.mAllMyResidence = []
		self.mChosenResId = -1
		
		self.mMyResidencePanelPos = self.GetPosition(self.mResidenceMyPanel1)
		
		self.AddTouchEventHandler(self.mMyNewResidenceBtn, self.OnMyNewResidenceBtn)
		self.AddTouchEventHandler(self.mMyRealNewResidenceCloseBtn, self.OnMyRealNewResidenceCloseBtn)
		self.AddTouchEventHandler(self.mMyRealChangeResidenceCloseBtn, self.OnmMyRealChangeResidenceCloseBtn)
		self.AddTouchEventHandler(self.mMyRealNewResidenceBtn, self.OnMyRealNewResidenceBtn)
		self.AddTouchEventHandler(self.mMyRealChangeResidenceBtn, self.OnMyRealChangeResidenceBtn)
		for index, residenceMyChangeBtn in enumerate(self.mResidenceMyChangeBtns):
			self.AddTouchEventHandler(residenceMyChangeBtn, self.OnResidenceMyChangeBtn)
		
		for index, residenceMyTransferBtn in enumerate(self.mResidenceMyTransderBtns):
			self.AddTouchEventHandler(residenceMyTransferBtn, self.OnResidenceMyTransferBtn)
		
		self.AddTouchEventHandler(self.mChangeMinXAddBtn, self.OnChangeMinXAddBtn)
		self.AddTouchEventHandler(self.mChangeMinXMinusBtn, self.OnChangeMinXMinusBtn)
		self.AddTouchEventHandler(self.mChangeMinYAddBtn, self.OnChangeMinYAddBtn)
		self.AddTouchEventHandler(self.mChangeMinYMinusBtn, self.OnChangeMinYMinusBtn)
		self.AddTouchEventHandler(self.mChangeMinZAddBtn, self.OnChangeMinZAddBtn)
		self.AddTouchEventHandler(self.mChangeMinZMinusBtn, self.OnChangeMinZMinusBtn)
		self.AddTouchEventHandler(self.mChangeMaxXAddBtn, self.OnChangeMaxXAddBtn)
		self.AddTouchEventHandler(self.mChangeMaxXMinusBtn, self.OnChangeMaxXMinusBtn)
		self.AddTouchEventHandler(self.mChangeMaxYAddBtn, self.OnChangeMaxYAddBtn)
		self.AddTouchEventHandler(self.mChangeMaxYMinusBtn, self.OnChangeMaxYMinusBtn)
		self.AddTouchEventHandler(self.mChangeMaxZAddBtn, self.OnChangeMaxZAddBtn)
		self.AddTouchEventHandler(self.mChangeMaxZMinusBtn, self.OnChangeMaxZMinusBtn)
		
		self.AddTouchEventHandler(self.mNewMinXAddBtn, self.OnNewMinXAddBtn)
		self.AddTouchEventHandler(self.mNewMinXMinusBtn, self.OnNewMinXMinusBtn)
		self.AddTouchEventHandler(self.mNewMinYAddBtn, self.OnNewMinYAddBtn)
		self.AddTouchEventHandler(self.mNewMinYMinusBtn, self.OnNewMinYMinusBtn)
		self.AddTouchEventHandler(self.mNewMinZAddBtn, self.OnNewMinZAddBtn)
		self.AddTouchEventHandler(self.mNewMinZMinusBtn, self.OnNewMinZMinusBtn)
		self.AddTouchEventHandler(self.mNewMaxXAddBtn, self.OnNewMaxXAddBtn)
		self.AddTouchEventHandler(self.mNewMaxXMinusBtn, self.OnNewMaxXMinusBtn)
		self.AddTouchEventHandler(self.mNewMaxYAddBtn, self.OnNewMaxYAddBtn)
		self.AddTouchEventHandler(self.mNewMaxYMinusBtn, self.OnNewMaxYMinusBtn)
		self.AddTouchEventHandler(self.mNewMaxZAddBtn, self.OnNewMaxZAddBtn)
		self.AddTouchEventHandler(self.mNewMaxZMinusBtn, self.OnNewMaxZMinusBtn)
		
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
	def OnResidenceMyTransferBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			resIndex = self.GetTransferResIdIndex(args["ButtonPath"])
			resData = self.mAllMyResidence[resIndex]
			# data = {'playerId': self.mLocalPlayerId, "resId":resId}
			resId = resData["resId"]
			dict = {
				"resId":resId,
				"playerId":self.mLocalPlayerId
			}
			print "TransferToResidenceFromClient", dict
			self.mClientSystem.NotifyToServer("TransferToResidenceFromClient", dict)
	
	def OnNewMinXAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos0 = int(self.mNewResidenceMinX)
			minPos0 = minPos0 + 1
			self.SetText(self.mMyRealNewResidenceMinXText, str(minPos0))
			self.mNewResidenceMinX = str(minPos0)
			self.OnChangeShowingPos((int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)), (int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMinXMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos0 = int(self.mNewResidenceMinX)
			minPos0 = minPos0 - 1
			self.SetText(self.mMyRealNewResidenceMinXText, str(minPos0))
			self.mNewResidenceMinX = str(minPos0)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMinYAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos1 = int(self.mNewResidenceMinY)
			minPos1 = minPos1 + 1
			self.SetText(self.mMyRealNewResidenceMinYText, str(minPos1))
			self.mNewResidenceMinY = str(minPos1)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	def OnNewMinYMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos1 = int(self.mNewResidenceMinY)
			minPos1 = minPos1 - 1
			self.SetText(self.mMyRealNewResidenceMinYText, str(minPos1))
			self.mNewResidenceMinY = str(minPos1)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	def OnNewMinZAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos2 = int(self.mNewResidenceMinZ)
			minPos2 = minPos2 + 1
			self.SetText(self.mMyRealNewResidenceMinZText, str(minPos2))
			self.mNewResidenceMinZ = str(minPos2)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMinZMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos2 = int(self.mNewResidenceMinZ)
			minPos2 = minPos2 - 1
			self.SetText(self.mMyRealNewResidenceMinZText, str(minPos2))
			self.mNewResidenceMinZ = str(minPos2)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMaxXAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos0 = int(self.mNewResidenceMaxX)
			maxPos0 = maxPos0 + 1
			print "OnNewMaxXAddBtn", maxPos0
			self.SetText(self.mMyRealNewResidenceMaxXText, str(maxPos0))
			self.mNewResidenceMaxX = str(maxPos0)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMaxXMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos0 = int(self.mNewResidenceMaxX)
			maxPos0 = maxPos0 - 1
			self.SetText(self.mMyRealNewResidenceMaxXText, str(maxPos0))
			self.mNewResidenceMaxX = str(maxPos0)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMaxYAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos1 = int(self.mNewResidenceMaxY)
			maxPos1 = maxPos1 + 1
			self.SetText(self.mMyRealNewResidenceMaxYText, str(maxPos1))
			self.mNewResidenceMaxY = str(maxPos1)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMaxYMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos1 = int(self.mNewResidenceMaxY)
			maxPos1 = maxPos1 - 1
			self.SetText(self.mMyRealNewResidenceMaxYText, str(maxPos1))
			self.mNewResidenceMaxY = str(maxPos1)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnNewMaxZAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos2 = int(self.mNewResidenceMaxZ)
			maxPos2 = maxPos2 + 1
			self.SetText(self.mMyRealNewResidenceMaxZText, str(maxPos2))
			self.mNewResidenceMaxZ = str(maxPos2)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnChangeMinXAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos0 = int(self.mChangeResidenceMinX)
			minPos0 = minPos0 + 1
			self.SetText(self.mMyRealChangeResidenceMinXText, str(minPos0))
			self.mChangeResidenceMinX = str(minPos0)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	def OnNewMaxZMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos2 = int(self.mNewResidenceMaxZ)
			maxPos2 = maxPos2 - 1
			self.SetText(self.mMyRealNewResidenceMaxZText, str(maxPos2))
			self.mNewResidenceMaxZ = str(maxPos2)
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
		
	def OnChangeMinXMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos0 = int(self.mChangeResidenceMinX)
			minPos0 = minPos0 - 1
			self.SetText(self.mMyRealChangeResidenceMinXText, str(minPos0))
			self.mChangeResidenceMinX = str(minPos0)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMinYAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos1 = int(self.mChangeResidenceMinY)
			minPos1 = minPos1 + 1
			self.SetText(self.mMyRealChangeResidenceMinYText, str(minPos1))
			self.mChangeResidenceMinY = str(minPos1)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
			
	def OnChangeMinYMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos1 = int(self.mChangeResidenceMinY)
			minPos1 = minPos1 - 1
			self.SetText(self.mMyRealChangeResidenceMinYText, str(minPos1))
			self.mChangeResidenceMinY = str(minPos1)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMinZAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos2 = int(self.mChangeResidenceMinZ)
			minPos2 = minPos2 + 1
			self.SetText(self.mMyRealChangeResidenceMinZText, str(minPos2))
			self.mChangeResidenceMinZ = str(minPos2)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMinZMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			minPos2 = int(self.mChangeResidenceMinZ)
			minPos2 = minPos2 - 1
			self.SetText(self.mMyRealChangeResidenceMinZText, str(minPos2))
			self.mChangeResidenceMinZ = str(minPos2)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxXAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos0 = int(self.mChangeResidenceMaxX)
			maxPos0 = maxPos0 + 1
			self.SetText(self.mMyRealChangeResidenceMaxXText, str(maxPos0))
			self.mChangeResidenceMaxX = str(maxPos0)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxXMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos0 = int(self.mChangeResidenceMaxX)
			maxPos0 = maxPos0 - 1
			self.SetText(self.mMyRealChangeResidenceMaxXText, str(maxPos0))
			self.mChangeResidenceMaxX = str(maxPos0)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxYAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos1 = int(self.mChangeResidenceMaxY)
			maxPos1 = maxPos1 + 1
			self.SetText(self.mMyRealChangeResidenceMaxYText, str(maxPos1))
			self.mChangeResidenceMaxY = str(maxPos1)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxYMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos1 = int(self.mChangeResidenceMaxY)
			maxPos1 = maxPos1 - 1
			self.SetText(self.mMyRealChangeResidenceMaxYText, str(maxPos1))
			self.mChangeResidenceMaxY = str(maxPos1)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxZAddBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos2 = int(self.mChangeResidenceMaxZ)
			maxPos2 = maxPos2 + 1
			self.SetText(self.mMyRealChangeResidenceMaxZText, str(maxPos2))
			self.mChangeResidenceMaxZ = str(maxPos2)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def OnChangeMaxZMinusBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			maxPos2 = int(self.mChangeResidenceMaxZ)
			maxPos2 = maxPos2 - 1
			self.SetText(self.mMyRealChangeResidenceMaxZText, str(maxPos2))
			self.mChangeResidenceMaxZ = str(maxPos2)
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
				self.OnChangeShowingPos(
					None,
					None, False)
		else:
			self.ChangeScreenVisible(False)
			
	def OnResidenceMyChangeBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			resIndex = self.GetResIdIndex(args["ButtonPath"])
			resData = self.mAllMyResidence[resIndex]
			# data = {'playerId': self.mLocalPlayerId, "resId":resId}
			resId = resData["resId"]
			dict = {
				"resId": resId,
				"playerId": self.mLocalPlayerId
			}
			print "TransferToResidenceFromClient", dict
			self.mClientSystem.NotifyToServer("TransferToResidenceFromClient", dict)
			# data = {'playerId': self.mLocalPlayerId, "resId":resId}
			self.mChosenResId = resData["resId"]
			self.SetVisible(self.mMyChangeResidencePanel, True)
			self.ShowOtherPanel(False)
			minPos = resData["minPos"]
			maxPos = resData["maxPos"]
			self.SetText(self.mMyRealChangeResidenceNameText, "当前领地名字：" + resData["resName"].encode("UTF-8"))
			self.SetText(self.mMyRealChangeResidenceBtnLabel, str(util.GetModConfByField("goods_id_to_price")["RESIDENCE_CHANGE"]))
			self.SetText(self.mMyRealChangeResidenceMinXText, str(minPos[0]))
			self.SetText(self.mMyRealChangeResidenceMinYText, str(minPos[1]))
			self.SetText(self.mMyRealChangeResidenceMinZText, str(minPos[2]))
			self.SetText(self.mMyRealChangeResidenceMaxXText, str(maxPos[0]))
			self.SetText(self.mMyRealChangeResidenceMaxYText, str(maxPos[1]))
			self.SetText(self.mMyRealChangeResidenceMaxZText, str(maxPos[2]))
			
			self.mChangeResidenceMinX = str(minPos[0])
			self.mChangeResidenceMinY = str(minPos[1])
			self.mChangeResidenceMinZ = str(minPos[2])
			self.mChangeResidenceMaxX = str(maxPos[0])
			self.mChangeResidenceMaxY = str(maxPos[1])
			self.mChangeResidenceMaxZ = str(maxPos[2])
			self.OnChangeShowingPos(
				(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
				(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
			
	def GetResIdIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceMyChangeBtns):
			if btnPath == path:
				return index
		return -1
	
	def GetTransferResIdIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceMyTransderBtns):
			if btnPath == path:
				return index
		return -1
		
	def OnMyRealNewResidenceBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			#print util.is_number(self.mNewResidenceMinX)
			if len(self.mNewResidenceName) <= 0:
				self.ShowTips("领地名字不能为空!")
				return
			elif self.mNewResidenceName == "***":
				self.ShowTips("领地名字符号规范!")
				return
			elif False in itertools.imap(lambda a:util.is_number(a),
			                           (self.mNewResidenceMinX, self.mNewResidenceMinY, self.mNewResidenceMinZ,
			                            self.mNewResidenceMaxX, self.mNewResidenceMaxY, self.mNewResidenceMaxZ)):
				self.ShowTips("坐标请输入数字!")
				return
			minPos = (min(int(self.mNewResidenceMinX), int(self.mNewResidenceMaxX)), min(int(self.mNewResidenceMinY), int(self.mNewResidenceMaxY)), min(int(self.mNewResidenceMinZ),  int(self.mNewResidenceMaxZ)))
			maxPos = (max(int(self.mNewResidenceMinX), int(self.mNewResidenceMaxX)), max(int(self.mNewResidenceMinY), int(self.mNewResidenceMaxY)), max(int(self.mNewResidenceMinZ),  int(self.mNewResidenceMaxZ)))
			#print self.mNewResidenceName, self.mNewResidenceMinX, self.mNewResidenceMinY, self.mNewResidenceMinZ, self.mNewResidenceMaxX, self.mNewResidenceMaxY, self.mNewResidenceMaxZ
			self.mClientSystem.NotifyToServer("CreateParentResidenceFromClient",
			                                         {"minPos": minPos, "maxPos": maxPos,
			                                          "dimension": self.mClientSystem.GetPlayerGac().mDimensionId, "playerId": self.mLocalPlayerId, "name": self.mNewResidenceName})
	
	def OnMyRealChangeResidenceBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			print self.mChangeResidenceMinX, self.mChangeResidenceMinY, self.mChangeResidenceMinZ, self.mChangeResidenceMaxX, self.mChangeResidenceMaxY, self.mChangeResidenceMaxZ
			if False in itertools.imap(lambda a: util.is_number(a),
			                        (self.mChangeResidenceMinX, self.mChangeResidenceMinY, self.mChangeResidenceMinZ,
			                         self.mChangeResidenceMaxX, self.mChangeResidenceMaxY, self.mChangeResidenceMaxZ)):
				self.ShowTips("坐标请输入数字!")
				return
			minPos = (
			min(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMaxX)), min(int(self.mChangeResidenceMinY), int(self.mChangeResidenceMaxY)),
			min(int(self.mChangeResidenceMinZ), int(self.mChangeResidenceMaxZ)))
			maxPos = (
			max(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMaxX)), max(int(self.mChangeResidenceMinY), int(self.mChangeResidenceMaxY)),
			max(int(self.mChangeResidenceMinZ), int(self.mChangeResidenceMaxZ)))
			self.mClientSystem.NotifyToServer("ChangeResidencePosFromClient",  {"minPos": minPos, "maxPos": maxPos,"resId":self.mChosenResId,
			                                          "dimension": self.mClientSystem.GetPlayerGac().mDimensionId, "playerId": self.mLocalPlayerId, "name": self.mNewResidenceName})
			#self.ShowTips("该功能暂时未开放!")
		#TODO 改建没接口
	
	def OnMyNewResidenceBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			posComp = extraClientApi.CreateComponent(self.mLocalPlayerId, "Minecraft", "pos")
			# 获取位置：
			playerPos = posComp.GetPos()
			self.SetVisible(self.mMyNewResidencePanel, True)
			self.ShowOtherPanel(False)
			self.mNewResidenceMinX = str(int(playerPos[0] - util.GetModConfByField("size_limit")["lv0"]["x"][0]/2))
			self.mNewResidenceMinY = str(int(playerPos[1] - util.GetModConfByField("size_limit")["lv0"]["y"][0]/2)) if util.GetModConfByField("residence_support_y_axis") else str(util.GetModConfByField("residence_y_size")[0])
			self.mNewResidenceMinZ = str(int(playerPos[2] - util.GetModConfByField("size_limit")["lv0"]["z"][0]/2))
			self.mNewResidenceMaxX = str(int(playerPos[0] + util.GetModConfByField("size_limit")["lv0"]["x"][0]/2))
			self.mNewResidenceMaxY = str(int(playerPos[1] + util.GetModConfByField("size_limit")["lv0"]["y"][0]/2)) if util.GetModConfByField("residence_support_y_axis") else str(util.GetModConfByField("residence_y_size")[1])
			self.mNewResidenceMaxZ = str(int(playerPos[2] + util.GetModConfByField("size_limit")["lv0"]["z"][0]/2))
			self.SetText(self.mMyRealNewResidenceMinXText, str(int(playerPos[0] - util.GetModConfByField("size_limit")["lv0"]["x"][0]/2)))
			self.SetText(self.mMyRealNewResidenceMinYText, self.mNewResidenceMinY)
			self.SetText(self.mMyRealNewResidenceMinZText, str(int(playerPos[2] - util.GetModConfByField("size_limit")["lv0"]["z"][0]/2)))
			self.SetText(self.mMyRealNewResidenceMaxXText, str(int(playerPos[0] + util.GetModConfByField("size_limit")["lv0"]["x"][0]/2)))
			self.SetText(self.mMyRealNewResidenceMaxYText, self.mNewResidenceMaxY)
			self.SetText(self.mMyRealNewResidenceMaxZText, str(int(playerPos[2] + util.GetModConfByField("size_limit")["lv0"]["z"][0]/2)))
			self.SetText(self.mMyRealNewResidenceBtnLabel, str(util.GetModConfByField("goods_id_to_price")["RESIDENCE_OPEN"]))
			
			self.OnChangeShowingPos(
				(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
				(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
			
	def OnMyRealNewResidenceCloseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mMyNewResidencePanel, False)
			self.ChangeScreenVisible(False)
			self.OnChangeShowingPos(
				None,
				None, False)
			
	def OnmMyRealChangeResidenceCloseBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetVisible(self.mMyChangeResidencePanel, False)
			self.ChangeScreenVisible(False)
			self.OnChangeShowingPos(
				None,
				None, False)
	
	def ShowTips(self, message):
		self.mClientSystem.NotifyToServer("ShowTipsFromClientEvent",
		                                  {"playerId": self.mLocalPlayerId, "message": message})
			
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newresidencename_text_box_content(self):
		# print "SearchTextBox  ", args
		return self.mNewResidenceName
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newresidencename_text_box(self, args):
		print "newresidencename_text_box  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		if comp:
			if comp.CheckWordsValid(args["Text"]):
				self.mNewResidenceName = args["Text"]
			else:
				self.mNewResidenceName = "***"
		#self.mNewResidenceName = args["Text"]
		return ViewRequest.Refresh
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newminx_text_box_content(self):
		return self.mNewResidenceMinX
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newminx_text_box(self, args):
		print "newminx_text_box_content  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMinX = args["Text"]
		if util.is_number(self.mNewResidenceMinX):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newmaxx_text_box_content(self):
		return self.mNewResidenceMaxX
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newmaxx_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMaxX = args["Text"]
		if util.is_number(self.mNewResidenceMaxX):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newminy_text_box_content(self):
		return self.mNewResidenceMinY
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newminy_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMinY = args["Text"]
		if util.is_number(self.mNewResidenceMinY):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newmaxy_text_box_content(self):
		return self.mNewResidenceMaxY
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newmaxy_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMaxY = args["Text"]
		if util.is_number(self.mNewResidenceMaxY):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newminz_text_box_content(self):
		return self.mNewResidenceMinZ
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newminz_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMinZ = args["Text"]
		if util.is_number(self.mNewResidenceMinZ):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def newmaxz_text_box_content(self):
		return self.mNewResidenceMaxZ
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def newmaxz_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mNewResidenceMaxZ = args["Text"]
		if util.is_number(self.mNewResidenceMaxZ):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mNewResidenceMinX), int(self.mNewResidenceMinY), int(self.mNewResidenceMinZ)),
			(int(self.mNewResidenceMaxX), int(self.mNewResidenceMaxY), int(self.mNewResidenceMaxZ)))
	
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changeminx_text_box_content(self):
		return self.mChangeResidenceMinX
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changeminx_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMinX = args["Text"]
		if util.is_number(self.mChangeResidenceMinX):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changemaxx_text_box_content(self):
		return self.mChangeResidenceMaxX
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changemaxx_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMaxX = args["Text"]
		if util.is_number(self.mChangeResidenceMaxX):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changeminy_text_box_content(self):
		return self.mChangeResidenceMinY
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changeminy_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMinY = args["Text"]
		if util.is_number(self.mChangeResidenceMinY):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changemaxy_text_box_content(self):
		return self.mChangeResidenceMaxY
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changemaxy_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMaxY = args["Text"]
		if util.is_number(self.mChangeResidenceMaxY):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changeminz_text_box_content(self):
		return self.mChangeResidenceMinZ
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changeminz_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMinZ = args["Text"]
		if util.is_number(self.mChangeResidenceMinZ):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
	
	@ViewBinder.binding(ViewBinder.BF_BindString)
	def changemaxz_text_box_content(self):
		return self.mChangeResidenceMaxZ
	
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def changemaxz_text_box(self, args):
		# print "SearchTextBox  ", args
		self.SetInputEnable(True)
		if args['Finish'] and args['Mode'] == 'Finished':
			self.SetInputEnable(False)
		self.mChangeResidenceMaxZ = args["Text"]
		if util.is_number(self.mChangeResidenceMaxZ):
			self.ShowTips("坐标请输入数字!")
			return
		self.OnChangeShowingPos(
			(int(self.mChangeResidenceMinX), int(self.mChangeResidenceMinY), int(self.mChangeResidenceMinZ)),
			(int(self.mChangeResidenceMaxX), int(self.mChangeResidenceMaxY), int(self.mChangeResidenceMaxZ)))
		
	def ShowTransferMainNewImg(self, visible):
		self.SetVisible(self.mTransferNewImg, visible)
		
	def ShowManageMainNewImg(self, visible):
		self.SetVisible(self.mManageNewImg, visible)
		
	
	def OnChangeShowingPos(self, minPos = None, maxPos = None, isShow = True):
		effectFunc.StopResidenceBox(self.mDrawingFrameList)
		if isShow and self.SHOW_RES_PRE_EFFECT:
			self.mDrawingFrameList = effectFunc.DrawResidenceBox(minPos, maxPos, "effects/green_line.json")
			print "self.mDrawingFrameList", self.mDrawingFrameList
   
	def ShowOtherPanel(self, flag):
		self.SetVisible(self.mMySecondPanel, flag)
		self.SetVisible(self.mCloseBtn, flag)
		self.SetVisible(self.mGiveBtn, flag)
		self.SetVisible(self.mApplyBtn, flag)
		self.SetVisible(self.mTransferBtn, flag)
		self.SetVisible(self.mManageBtn, flag)
		self.SetVisible(self.mMyBtn, flag)
	