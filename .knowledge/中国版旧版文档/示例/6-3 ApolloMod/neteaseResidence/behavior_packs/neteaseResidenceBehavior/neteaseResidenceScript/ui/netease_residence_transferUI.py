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

class ResidenceTransferUIScreen(ScreenNode):
	"""
	我的领地界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		
		self.mTransferPanel = "/transferPanel"
		self.mCloseBtn = self.mTransferPanel + "/close_button"#关闭
		self.mApplyBtn = self.mTransferPanel + "/apply_button"#申请页面按钮
		self.mTransferBtn = self.mTransferPanel + "/transfer_button"#传送页面按钮
		self.mTransferNewImg = self.mTransferBtn + "/image16"  # 传送页面按钮
		self.mGiveBtn = self.mTransferPanel + "/give_button"#赋予页面按钮
		self.mManageBtn = self.mTransferPanel + "/manage_button"#管理页面按钮
		self.mManageNewImg = self.mManageBtn + "/image14"  # 管理页面按钮
		self.mMyBtn = self.mTransferPanel + "/my_button"#管理页面按钮
		self.mTransferSecondPanel = self.mTransferPanel + "/panel4"
		self.mTransferPanelImg = self.mTransferSecondPanel + "/image9"
		self.mTransferTipLabel = self.mTransferPanelImg + "/label9"
		self.mResidenceTransferScroll = self.mTransferPanelImg + "/scroll_view0"
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def Show(self):
		self.ChangeScreenVisible(True)
		#self.SetVisible(self.mTransferNewImg, len(self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead) > 0)
		#self.InitScreenManage()
		self.OnSearchMyResidence()
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.mIsShow = flag
		if flag:
			extraClientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, "SearchCanEnterPlayerResidenceByIdFromServerEvent", self,
		                                  self.OnShowSearchResidenceResult)
		self.AddTouchEventHandler(self.mApplyBtn, self.mClientSystem.OnApplyBtn)
		self.SetTouchEnable(self.mTransferBtn, False)
		self.AddTouchEventHandler(self.mTransferBtn, self.mClientSystem.OnTransferBtn)
		self.AddTouchEventHandler(self.mGiveBtn, self.mClientSystem.OnGiveBtn)
		self.AddTouchEventHandler(self.mManageBtn, self.mClientSystem.OnManageBtn)
		self.AddTouchEventHandler(self.mMyBtn, self.mClientSystem.OnMyBtn)
	
	def Create(self):
		# 传送的scroll
		mResidenceTransferScrollTouch = self.mResidenceTransferScroll + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		residencetransfer_size = self.GetSize(mResidenceTransferScrollTouch)
		if residencetransfer_size:
			self.mTransferResidencePanel = mResidenceTransferScrollTouch
			self.mTransferResidenceSize = residencetransfer_size
		else:
			mResidenceTransferScrollTouch = self.mResidenceTransferScroll + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			residencetransfer_size = self.GetSize(mResidenceTransferScrollTouch)
			self.mTransferResidencePanel = mResidenceTransferScrollTouch
			self.mTransferResidenceSize = residencetransfer_size
		self.mResidenceTransferPlayerPanel1 = self.mTransferResidencePanel + "/TransferPlayer1"
		self.mResidenceTransferPlayerNewImg1 = self.mResidenceTransferPlayerPanel1 + "/image10"
		self.mResidenceTransferPlayerNameLabel1 = self.mResidenceTransferPlayerPanel1 + "/label4"
		self.mResidenceTransferResidenceNameLabel1 = self.mResidenceTransferPlayerPanel1 + "/label5"
		self.mResidenceTransferResidenceTransferButton1 = self.mResidenceTransferPlayerPanel1 + "/button4"
		
		self.mResidenceTransferPlayerPanels = [
			self.mResidenceTransferPlayerPanel1
		]
		
		self.mResidenceTransferPlayerNewImgs = [
			self.mResidenceTransferPlayerNewImg1
		]
		
		self.mResidenceTransferPlayerNameLabels = [
			self.mResidenceTransferPlayerNameLabel1
		]
		
		self.mResidenceTransferResidenceNameLabels = [
			self.mResidenceTransferResidenceNameLabel1
		]
		
		self.mResidenceTransferResidenceTransferButtons = [
			self.mResidenceTransferResidenceTransferButton1
		]
		
		self.mTransferResidencePanelPos = self.GetPosition(self.mResidenceTransferPlayerPanel1)
		
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
		for index, residenceTransferBtn in enumerate(self.mResidenceTransferResidenceTransferButtons):
			self.AddTouchEventHandler(residenceTransferBtn, self.OnResidenceTransferBtn)
			
	def ClosePanel(self, args=None):
		print "======%s========" % "ClosePanel"
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
		else:
			self.ChangeScreenVisible(False)
	
	def OnShowSearchResidenceResult(self, args):
		print "OnShowSearchResidenceResultCanEnter", args
		resList = args.get("resList")
		if self.mIsShow == False:
			#self.system.BroadcastEvent("Sho")
			#self.mClientSystem.GetResidenceMgr().UpdateTransferResIdListState(resList, False)
			return
		playerName = args.get("playerName")
		resNum = len(resList)
		if resNum <= 0:
			self.SetVisible(self.mResidenceTransferScroll, False)
			self.SetVisible(self.mTransferTipLabel, True)
		else:
			self.SetVisible(self.mResidenceTransferScroll, True)
			self.SetVisible(self.mTransferTipLabel, False)
		
		deltaNum = resNum - len(self.mResidenceTransferPlayerPanels)
		if deltaNum > 0:
			for i in xrange(len(self.mResidenceTransferPlayerPanels) + 1, resNum + 1):
				residenceTransferPlayerPanel = "TransferPlayer%s" % i
				residenceTransferPlayerPanelPath = "%s/%s" % (self.mTransferResidencePanel, residenceTransferPlayerPanel)
				residenceTransferPlayerNewImgPath = "%s/%s" % (residenceTransferPlayerPanelPath, "image10")
				residenceTransferPlayerNameLabelPath = "%s/%s" % (residenceTransferPlayerPanelPath, "label4")
				residenceTransferResidenceNameLabelPath = "%s/%s" % (residenceTransferPlayerPanelPath, "label5")
				residenceTransferPlayerBtnPath = "%s/%s" % (residenceTransferPlayerPanelPath, "button4")
				self.Clone(self.mResidenceTransferPlayerPanel1, self.mTransferResidencePanel, residenceTransferPlayerPanel)
				self.mResidenceTransferPlayerPanels.append(residenceTransferPlayerPanelPath)
				self.mResidenceTransferPlayerNewImgs.append(residenceTransferPlayerNewImgPath)
				self.mResidenceTransferPlayerNameLabels.append(residenceTransferPlayerNameLabelPath)
				self.mResidenceTransferResidenceNameLabels.append(residenceTransferResidenceNameLabelPath)
				self.mResidenceTransferResidenceTransferButtons.append(residenceTransferPlayerBtnPath)
		elif deltaNum < 0:
			for i in xrange(resNum + 1, len(self.mResidenceTransferPlayerPanels) + 1):
				if i == 1:
					continue
				print 'removing CheckPanel ', i
				residenceTransferPlayerPanel = "TransferPlayer%s" % i
				residenceTransferPlayerPanelPath = "%s/%s" % (self.mTransferResidencePanel, residenceTransferPlayerPanel)
				residenceTransferPlayerNewImgPath = "%s/%s" % (residenceTransferPlayerPanelPath, "image10")
				residenceTransferPlayerNameLabelPath = "%s/%s" % (residenceTransferPlayerPanelPath, "label4")
				residenceTransferResidenceNameLabelPath = "%s/%s" % (residenceTransferPlayerPanelPath, "label5")
				residenceTransferPlayerBtnPath = "%s/%s" % (residenceTransferPlayerPanelPath, "button4")
				self.RemoveComponent(residenceTransferPlayerPanelPath, self.mTransferResidencePanel)
				self.mResidenceTransferPlayerPanels.remove(residenceTransferPlayerPanelPath)
				self.mResidenceTransferPlayerNewImgs.remove(residenceTransferPlayerNewImgPath)
				self.mResidenceTransferPlayerNameLabels.remove(residenceTransferPlayerNameLabelPath)
				self.mResidenceTransferResidenceNameLabels.remove(residenceTransferResidenceNameLabelPath)
				self.mResidenceTransferResidenceTransferButtons.remove(residenceTransferPlayerBtnPath)
		# 其余情况，正常显示
		d = self.GetSize(self.mResidenceTransferPlayerPanel1)[1]
		for i, residenceTransferPlayerPanelPath in enumerate(self.mResidenceTransferPlayerPanels):
			self.SetPosition(residenceTransferPlayerPanelPath,
			                 (self.mTransferResidencePanelPos[0], self.mTransferResidencePanelPos[1] + d * i))
		i = 0
		self.mAllCheckResidence = []
		for idx, resData in enumerate(resList):
			# print "idx", idx
			# print "i", i
			self.mAllCheckResidence.append(resData)
			self.SetText(self.mResidenceTransferPlayerNameLabels[i], resData["resUserName"].encode('utf-8'))
			self.SetText(self.mResidenceTransferResidenceNameLabels[i], resData["resName"].encode('utf-8'))
			#TODO 设置一下新
			self.SetVisible(self.mResidenceTransferPlayerNewImgs[i], resData["resId"] in self.mClientSystem.GetResidenceMgr().mTransferResIdUnRead)
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mTransferResidenceSize[1])
		self.SetSize(self.mTransferResidencePanel, (self.mTransferResidenceSize[0], height))
		
		self.mClientSystem.GetResidenceMgr().UpdateTransferResIdListState(resList, True)
		self.SetVisible(self.mTransferNewImg, False)
		self.mClientSystem.NotifyToServer("TransferHasReadFromClientEvent", {"playerId": self.mLocalPlayerId})
		
			
	def OnSearchMyResidence(self):
		#TODO 点击我的领地触发
		dict = {
			"playerId": self.mLocalPlayerId
		}
		self.mClientSystem.NotifyToServer("CheckCanEnterPlayerResidenceByIdFromClient", dict)
		
	def OnResidenceTransferBtn(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			resIndex = self.GetResIdIndex(args["ButtonPath"])
			resData = self.mAllCheckResidence[resIndex]
			# data = {'playerId': self.mLocalPlayerId, "resId":resId}
			resId = resData["resId"]
			dict = {
				"resId":resId,
				"playerId":self.mLocalPlayerId
			}
			print "TransferToResidenceFromClient", dict
			self.mClientSystem.NotifyToServer("TransferToResidenceFromClient", dict)
	
	def GetResIdIndex(self, path):
		for index, btnPath in enumerate(self.mResidenceTransferResidenceTransferButtons):
			if btnPath == path:
				return index
		return -1
	
	def ShowTransferMainNewImg(self, visible):
		self.SetVisible(self.mTransferNewImg, visible)
		
	def ShowManageMainNewImg(self, visible):
		self.SetVisible(self.mManageNewImg, visible)