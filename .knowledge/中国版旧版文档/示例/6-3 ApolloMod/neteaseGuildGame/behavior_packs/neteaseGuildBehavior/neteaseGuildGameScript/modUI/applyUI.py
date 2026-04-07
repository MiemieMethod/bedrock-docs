# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import time
import guildConsts as guildConsts
from guildConsts import UIDef

class ApplyScreen(ScreenNode):
	"""
	申请加入公会的玩家列表界面
	"""
	def __init__(self,namespace,name,param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init ApplyScreen"
		
		self.mPlayerIdList = []
		
		self.mApplyPanel = "/ApplyPanel"
		self.mApplyImg = self.mApplyPanel + "/apply_img"
		self.mCloseBtn = self.mApplyImg + "/close_btn"
		
	def OnShowApplication(self, playerDict):
		'''
		显示申请玩家的信息
		'''
		print "OnShowApplication", playerDict
		if playerDict == None:
			playerNum = 0
		else:
			playerNum = len(playerDict)
		if playerNum <= 0:
			self.SetVisible(self.mPlayerListImg, False)
		else:
			self.SetVisible(self.mPlayerListImg, True)
		deltaNum = playerNum - len(self.mPlayerListImgs)
		
		if deltaNum > 0:#数量发生变化再做增删
			for i in xrange(len(self.mPlayerListImgs) + 1, playerNum + 1):
				mPlayerListImg = "apply_img_%s" % i
				playerListImgPath = '%s/%s' % (self.mMemberListPanel, mPlayerListImg)
				alreadyLblPath = '%s/%s' % (playerListImgPath, self.mAlreadyLbl)
				playerNameLblPath = '%s/%s' % (playerListImgPath, self.mPlayerNameLbl)
				levelLblPath = '%s/%s' % (playerListImgPath, self.mLevelLbl)
				applicationTimeLblPath = '%s/%s' % (playerListImgPath, self.mApplicationTimeLbl)
				acceptBtnPath = '%s/%s' % (playerListImgPath, self.mAcceptBtn)
				refuseBtnPath = '%s/%s' % (playerListImgPath, self.mRefuseBtn)
				self.Clone(self.mPlayerListImg, self.mMemberListPanel, mPlayerListImg)
				self.mPlayerListImgs.append(playerListImgPath)
				self.mAlreadyLbls.append(alreadyLblPath)
				self.mPlayerNameLbls.append(playerNameLblPath)
				self.mLevelLbls.append(levelLblPath)
				self.mApplicationTimeLbls.append(applicationTimeLblPath)
				self.mAcceptBtns.append(acceptBtnPath)
				self.mRefuseBtns.append(refuseBtnPath)
		elif deltaNum < 0 and playerNum > 0:  # 少了就删掉,至少保留一个
			for i in xrange(playerNum + 1, len(self.mPlayerListImgs) + 1):
				mPlayerListImg = "apply_img_%s" % i
				playerListImgPath = '%s/%s' % (self.mMemberListPanel, mPlayerListImg)
				alreadyLblPath = '%s/%s' % (playerListImgPath, self.mAlreadyLbl)
				playerNameLblPath = '%s/%s' % (playerListImgPath, self.mPlayerNameLbl)
				levelLblPath = '%s/%s' % (playerListImgPath, self.mLevelLbl)
				applicationTimeLblPath = '%s/%s' % (playerListImgPath, self.mApplicationTimeLbl)
				acceptBtnPath = '%s/%s' % (playerListImgPath, self.mAcceptBtn)
				refuseBtnPath = '%s/%s' % (playerListImgPath, self.mRefuseBtn)
				self.RemoveComponent(playerListImgPath, self.mMemberListPanel)
				self.mPlayerListImgs.remove(playerListImgPath)
				self.mAlreadyLbls.remove(alreadyLblPath)
				self.mPlayerNameLbls.remove(playerNameLblPath)
				self.mLevelLbls.remove(levelLblPath)
				self.mApplicationTimeLbls.remove(applicationTimeLblPath)
				self.mAcceptBtns.remove(acceptBtnPath)
				self.mRefuseBtns.remove(refuseBtnPath)
		# 其余情况，正常显示
		#d = self.GetSize(self.mPlayerListImg)[1]
		for i, playerListImg in enumerate(self.mPlayerListImgs):
			self.SetPosition(playerListImg, (self.mPlayerListImgPos[0], self.mPlayerListImgPos[1] + self.mPlayerListImgHeight * i))
		
		self.mPlayerIdList = []
		i = 0
		if playerNum > 0:
			for playerUid, playerAttrs in playerDict.items():
				self.SetText(self.mPlayerNameLbls[i], playerAttrs.get('name'))
				self.SetText(self.mLevelLbls[i], str(playerAttrs.get('level')))
				self.SetText(self.mApplicationTimeLbls[i], str(time.strftime("%Y-%m-%d", time.localtime(playerAttrs.get('applicationTime'))).replace('-', '.')))
				i = i + 1
				self.mPlayerIdList.append(playerUid)
		height = 10 + i * (10 + self.mPlayerListImgHeight)
		height = max(height, self.mMemberListPanelSize[1])
		self.SetSize(self.mMemberListPanel, (self.mMemberListPanelSize[0], height))
		
	def GetPlayerIndex(self, path):
		for index, btnPath in enumerate(self.mAcceptBtns):
			if btnPath == path:
				return index
		return -1

	def GetRefusePlayerIndex(self, path):
		for index, btnPath in enumerate(self.mRefuseBtns):
			if btnPath == path:
				return index
		return -1
		
	def Create(self):
		#self.ShowPanel(False)
		scrollBase = self.mApplyImg + "/applyui_scroll_base"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			self.mMemberListPanel = scrollBaseTouch
			self.mMemberListPanelSize = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			self.mMemberListPanel = scrollBaseMouse
			self.mMemberListPanelSize = size
		# self.mMemberListPanel = self.mApplyImg + "/applyui_scroll_base/memberlist_pnl"
		self.mPlayerListImg = self.mMemberListPanel + "/apply_img_1"
		self.mPlayerListImgHeight = self.GetSize(self.mPlayerListImg)[1]
		# TODO 先放一个看看好不好实现
		self.mPlayerListImgs = [
			self.mPlayerListImg
		]
		self.mAlreadyLbl = "already_lbl_1"
		self.mPlayerNameLbl = "gamer_lbl_1"
		self.mLevelLbl = "level_lbl_1"
		self.mApplicationTimeLbl = "applytime_lbl_1"
		self.mAcceptBtn = "accept_btn_1"
		self.mRefuseBtn = "refuse_btn_1"
		
		self.mAlreadyLbls = [
			self.mPlayerListImg + "/" + self.mAlreadyLbl
		]
		self.mPlayerNameLbls = [
			self.mPlayerListImg + "/" + self.mPlayerNameLbl
		]
		self.mLevelLbls = [
			self.mPlayerListImg + "/" + self.mLevelLbl
		]
		self.mApplicationTimeLbls = [
			self.mPlayerListImg + "/" + self.mApplicationTimeLbl
		]
		self.mAcceptBtns = [
			self.mPlayerListImg + "/" + self.mAcceptBtn
		]
		self.mRefuseBtns = [
			self.mPlayerListImg + "/" + self.mRefuseBtn
		]
		self.SetVisible(self.mApplyPanel, False)
		self.mPlayerListImgPos = self.GetPosition(self.mPlayerListImg)
	
	def InitScreen(self):
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
		for index, acceptBtnPath in enumerate(self.mAcceptBtns):
			self.AddTouchEventHandler(acceptBtnPath, self.AcceptPlayer)
			
		for index, refuseBtnPath in enumerate(self.mRefuseBtns):
			self.AddTouchEventHandler(refuseBtnPath, self.RefusePlayer)
			
	def AcceptPlayer(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
			playerIndex = self.GetPlayerIndex(args["ButtonPath"])
			playerUId = self.mPlayerIdList[playerIndex]
			data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'applicantUid': playerUId, 'isAdd': True}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.AgreePlayerFromClientEvent, data)
		elif touchEvent == touch_event_enum.TouchDown:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn01_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn01_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn01_click@3x.png")
		elif touchEvent == touch_event_enum.TouchCancel:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		elif touchEvent == touch_event_enum.TouchMove:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		else:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		
	def RefusePlayer(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
			playerIndex = self.GetRefusePlayerIndex(args["ButtonPath"])
			playerUId = self.mPlayerIdList[playerIndex]
			data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'applicantUid': playerUId, 'isAdd': False}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.AgreePlayerFromClientEvent, data)
		elif touchEvent == touch_event_enum.TouchDown:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn01_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn01_click@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn01_click@3x.png")
		elif touchEvent == touch_event_enum.TouchCancel:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		elif touchEvent == touch_event_enum.TouchMove:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		else:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
		
	def ClosePanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.ShowPanel(False)
	
	def ShowPanel(self, isShow):
		# if isShow:
		# 	clientApi.SetInputMode(1)
		# else:
		# 	clientApi.SetInputMode(0)
		self.SetVisible(self.mApplyPanel, isShow)
		UIOne = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_MYGUILD)
		UIOne.SetUITouchEnable(not isShow)