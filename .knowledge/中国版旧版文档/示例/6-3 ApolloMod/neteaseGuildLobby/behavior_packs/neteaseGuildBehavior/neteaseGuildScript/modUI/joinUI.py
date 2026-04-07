# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import guildConsts as guildConsts
from guildConsts import GuildAttrType
from guildConsts import UIDef

class JoinScreen(ScreenNode):
	"""
	加入公会界面，显示可加入的公会列表
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init JoinScreen"
		
		self.guildIdList = []
		
		#主界面
		self.mJoinPanel = "/JoinPanel"
		self.mJoinImg = self.mJoinPanel + "/joinparty_img"
		#创建公会按钮，关闭面板按钮
		self.mCreateBtn = self.mJoinImg + "/create_btn"
		self.mCloseBtn = self.mJoinImg + "/close_btn"
		self.mTipLabel = self.mJoinImg + "/tip_lbl"
	
	def Create(self):
		#self.ShowPanel(False)
		# 公会名字，会长名字，人数，活跃度
		# 成员列表Title
		scrollBase = self.mJoinImg + "/join_scroll_base"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			self.mGuildListPanel = scrollBaseTouch
			self.mGuildListPanelSize = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			self.mGuildListPanel = scrollBaseMouse
			self.mGuildListPanelSize = size
		
		#self.mGuildListPanel = self.mJoinImg + "/join_scroll_base/partylist_pnl"
		self.mGuildTitleLabel = self.mJoinImg + "/party_title_lbl"
		self.mPresidentTitleLabel = self.mJoinImg + "/president_title_lbl"
		self.mPeopleNumTitleLabel = self.mJoinImg + "/partynumber_title_lbl"
		self.mGuildActiveTitleLabel = self.mJoinImg + "/partyactive_title_lbl"
		
		# 所有公会列表信息
		self.mGuildListImg = self.mGuildListPanel + "/partylist_img_1"
		# TODO 先放一个看看好不好实现
		self.mGuildListImgs = [
			self.mGuildListImg
		]
		self.mGuildNameLabel = "party"
		self.mPresidentNameLabel = "partypresident"
		self.mPeopleNumLabel = "partynumber"
		self.mActivityLabel = "partyactive"
		self.mJoinBtn = "joinparty_btn"
		self.mGuildNameLabels = [
			self.mGuildListImg + "/" + self.mGuildNameLabel
		]
		self.mPresidentNameLabels = [
			self.mGuildListImg + "/" + self.mPresidentNameLabel
		]
		self.mPeopleNumLabels = [
			self.mGuildListImg + "/" + self.mPeopleNumLabel
		]
		self.mActivityLabels = [
			self.mGuildListImg + "/" + self.mActivityLabel
		]
		self.mJoinBtns = [
			self.mGuildListImg + "/" + self.mJoinBtn
		]
		self.SetVisible(self.mJoinPanel, False)
		self.mGuildListImgPos = self.GetPosition(self.mGuildListImg)
		self.AddTouchEventHandler(self.mCreateBtn, self.CreateGuild)
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		
		for index, joinBtnPath in enumerate(self.mJoinBtns):
			self.AddTouchEventHandler(joinBtnPath, self.JoinGuild)
		
	
	def JoinGuild(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
			guildIndex = self.GetGuildIndex(args["ButtonPath"])
			guildId = self.guildIdList[guildIndex]
			data = {'playerId': clientApi.GetLocalPlayerId(), 'guildId': guildId}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.JoinGuildFromClientEvent, data)
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
	
	def GetGuildIndex(self, path):
		for index,btnPath in enumerate(self.mJoinBtns):
			if btnPath == path:
				return index
		return -1
		
	def CreateGuild(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			data = {"UIDef": UIDef.UI_CREATEGUILD}
			guildConsts.GetClientModSystem().BroadcastEvent(guildConsts.ShowUIFromClientEvent, data)
	
	def ClosePanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.ShowPanel(False)
	
	def OnShowGuildBrief(self, guildDict):
		'''
		显示界面
		'''
		#self.ShowPanel(True)
		guildNum = len(guildDict)
		if guildNum <=0 :
			self.SetVisible(self.mGuildListImg, False)
			self.SetVisible(self.mTipLabel, True)
			#self.SetVisible(self.mCreateBtn, True)
			self.SetVisible(self.mGuildTitleLabel, False)
			self.SetVisible(self.mPresidentTitleLabel, False)
			self.SetVisible(self.mPeopleNumTitleLabel, False)
			self.SetVisible(self.mGuildActiveTitleLabel, False)
		else:
			self.SetVisible(self.mGuildListImg, True)
			self.SetVisible(self.mTipLabel, False)
			#self.SetVisible(self.mCreateBtn, False)
			self.SetVisible(self.mGuildTitleLabel, True)
			self.SetVisible(self.mPresidentTitleLabel, True)
			self.SetVisible(self.mPeopleNumTitleLabel, True)
			self.SetVisible(self.mGuildActiveTitleLabel, True)
		
		deltaNum = guildNum - len(self.mGuildListImgs)
		if deltaNum > 0:#数量发生变化再做增删
			for i in xrange(len(self.mGuildListImgs) + 1, guildNum + 1):
				guildListImg = "partylist_img_%s" % i
				guildListImgPath = '%s/%s' % (self.mGuildListPanel, guildListImg)
				guildNameLabelPath = '%s/%s' % (guildListImgPath, self.mGuildNameLabel)
				presidentNameLabelPath = '%s/%s' % (guildListImgPath, self.mPresidentNameLabel)
				peopleNumLabelPath = '%s/%s' % (guildListImgPath, self.mPeopleNumLabel)
				activityLabelPath = '%s/%s' % (guildListImgPath, self.mActivityLabel)
				joinBtnPath = '%s/%s' % (guildListImgPath, self.mJoinBtn)
				self.Clone(self.mGuildListImg, self.mGuildListPanel, guildListImg)
				self.mGuildListImgs.append(guildListImgPath)
				self.mGuildNameLabels.append(guildNameLabelPath)
				self.mPresidentNameLabels.append(presidentNameLabelPath)
				self.mPeopleNumLabels.append(peopleNumLabelPath)
				self.mActivityLabels.append(activityLabelPath)
				self.mJoinBtns.append(joinBtnPath)
		elif deltaNum < 0 and guildNum > 0:  # 少了就删掉，至少保留一个
			for i in xrange(guildNum + 1, len(self.mGuildListImgs) + 1):
				print 'removing ', i
				guildListImg = "partylist_img_%s" % i
				guildListImgPath = '%s/%s' % (self.mGuildListPanel, guildListImg)
				guildNameLabelPath = '%s/%s' % (guildListImgPath, self.mGuildNameLabel)
				presidentNameLabelPath = '%s/%s' % (guildListImgPath, self.mPresidentNameLabel)
				peopleNumLabelPath = '%s/%s' % (guildListImgPath, self.mPeopleNumLabel)
				activityLabelPath = '%s/%s' % (guildListImgPath, self.mActivityLabel)
				joinBtnPath = '%s/%s' % (guildListImgPath, self.mJoinBtn)
				self.RemoveComponent(guildListImgPath, self.mGuildListPanel)
				self.mGuildListImgs.remove(guildListImgPath)
				self.mGuildNameLabels.remove(guildNameLabelPath)
				self.mPresidentNameLabels.remove(presidentNameLabelPath)
				self.mPeopleNumLabels.remove(peopleNumLabelPath)
				self.mActivityLabels.remove(activityLabelPath)
				self.mJoinBtns.remove(joinBtnPath)
				# 其余情况，正常显示
		d = self.GetSize(self.mGuildListImg)[1]
		for i, guildListImg in enumerate(self.mGuildListImgs):
			self.SetPosition(guildListImg, (self.mGuildListImgPos[0], self.mGuildListImgPos[1] + d * i))
		i = 0
		self.guildIdList = []
		for guildId, guildAttrs in guildDict.items():
			self.guildIdList.append(guildId)
			self.SetText(self.mGuildNameLabels[i], guildAttrs.get(GuildAttrType.Name))
			self.SetText(self.mPresidentNameLabels[i], guildAttrs.get('PresidentName'))
			self.SetText(self.mPeopleNumLabels[i], str(guildAttrs.get(GuildAttrType.CurrentNum)) + "/" + str(guildAttrs.get(GuildAttrType.MaxNum)))
			self.SetText(self.mActivityLabels[i], str(guildAttrs.get(GuildAttrType.Activity)))
			i = i + 1
		
		height = 10 + i * (10 + d)
		height = max(height, self.mGuildListPanelSize[1])
		self.SetSize(self.mGuildListPanel, (self.mGuildListPanelSize[0], height))
	
	def InitScreen(self):
		guildConsts.GetClientModSystem().ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                                                guildConsts.GetGuildBriefFromServerEvent, self, self.OnShowGuildBrief)
	
	def ShowPanel(self, isShow):
		if isShow:
			clientApi.SetInputMode(1)
		else:
			clientApi.SetInputMode(0)
		self.SetVisible(self.mJoinPanel, isShow)