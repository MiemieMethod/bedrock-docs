# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from guildConsts import GuildAttrType
from guildConsts import PlayerAttrType
import guildConsts as guildConsts
from guildConsts import UIDef
from guildConsts import DutyType
from guildConsts import NotifyDef

onlineText = {
	True: "在线",
	False: "离线"
}

class MyGuildScreen(ScreenNode):
	"""
	公会详情界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init MyGuildPanel"
		
		self.mMyGuildPanel = "/MyGuildPanel"
		self.mMyPartyImg = self.mMyGuildPanel + "/myparty_img"
		
		#公会名字，人数，活跃度信息
		self.mMyPartyBg = self.mMyPartyImg + "/myparty_bg"
		self.mPartyName = self.mMyPartyBg + "/party_1_0"
		self.mPartyNumber = self.mMyPartyBg + "/partynumber_1_0"
		self.mPartyActive = self.mMyPartyBg + "/partyactive_1_0"
		
		#退出公会按钮，申请列表按钮，回到领地按钮，关闭面板按钮
		self.mBoWoutBtn = self.mMyPartyImg + "/bowout_btn"
		self.mApplyListBtn = self.mMyPartyImg + "/applylist_btn"
		self.mTipsNewImg = self.mApplyListBtn + "/tips_new_img"
		self.mReturnBtn = self.mMyPartyImg + "/return_btn"
		self.mCloseBtn = self.mMyPartyImg + "/close_btn"
		
		#会员操作按钮
		self.mMemberMorePanel = self.mMyPartyImg + "/more_pnl"
		self.mMemberPromoteBtn = self.mMemberMorePanel + "/more_btn_1"
		self.mMemberDemoteBtn = self.mMemberMorePanel + "/more_btn_2"
		self.mMemberKickBtn = self.mMemberMorePanel + "/more_btn_3"
		self.mMemberAppointPresidentBtn = self.mMemberMorePanel + "/more_btn_4"
		
		self.mPresidentUidList = []
		self.mElderUidList = []
		self.mCommonUidList = []
		self.mMorePlayerUid = -1
		self.mGuildName = ""
		
	def OnShowGuild(self, attrsCurrent):
		print "OnShowGuild", attrsCurrent
		self.SetVisible(self.mMemberMorePanel, False)
		guildName = attrsCurrent.get(GuildAttrType.Name)
		self.mGuildName = guildName
		guildActivity = attrsCurrent.get(GuildAttrType.Activity)
		guildMaxNum = attrsCurrent.get(GuildAttrType.MaxNum)
		presidentPlayerDict = attrsCurrent.get(GuildAttrType.PresidentPlayerDict)
		if presidentPlayerDict == None:
			presidentPlayerNum = 0
		else:
			presidentPlayerNum = len(presidentPlayerDict)
		elderPlayerDict = attrsCurrent.get(GuildAttrType.ElderPlayerDict)
		if elderPlayerDict == None:
			elderPlayerNum = 0
		else:
			elderPlayerNum = len(elderPlayerDict)
		commonPlayerDict = attrsCurrent.get(GuildAttrType.CommonPlayerDict)
		if commonPlayerDict == None:
			commonPlayerNum = 0
		else:
			commonPlayerNum = len(commonPlayerDict)
		#总人数
		allPlayerNum = presidentPlayerNum + elderPlayerNum + commonPlayerNum
		deltaNum = allPlayerNum - len(self.mMemberListImgs)
		if deltaNum > 0:#数量发生变化再做增删
			for i in xrange(len(self.mMemberListImgs) + 1, allPlayerNum + 1):
				memberListImg = "memberlist_img_%s" % i
				memberListImgPath = '%s/%s' % (self.mMemberListPanel, memberListImg)
				memberJobLabelPath = '%s/%s' % (memberListImgPath, self.mJobLabel)
				memberNameLabelPath = '%s/%s' % (memberListImgPath, self.mNameLabel)
				memberStatusLabelPath = '%s/%s' % (memberListImgPath, self.mStatusLabel)
				memberLevelLabelPath = '%s/%s' % (memberListImgPath, self.mLevelLabel)
				memberActivityLabelPath = '%s/%s' % (memberListImgPath, self.mActivityLabel)
				memberMoreBtnPath = '%s/%s' % (memberListImgPath, self.mMoreBtn)
				self.Clone(self.mMemberListImg, self.mMemberListPanel, memberListImg)
				self.mMemberListImgs.append(memberListImgPath)
				self.mMemberJobLabels.append(memberJobLabelPath)
				self.mMemberNameLabels.append(memberNameLabelPath)
				self.mMemberStatusLabels.append(memberStatusLabelPath)
				self.mMemberLevelLabels.append(memberLevelLabelPath)
				self.mMemberActivityLabels.append(memberActivityLabelPath)
				self.mMemberMoreBtns.append(memberMoreBtnPath)
		elif deltaNum < 0 and allPlayerNum > 0:#少了就删掉,至少保留一个
			for i in xrange(allPlayerNum + 1, len(self.mMemberListImgs) + 1):
				memberListImg = "memberlist_img_%s" % i
				memberListImgPath = '%s/%s' % (self.mMemberListPanel, memberListImg)
				memberJobLabelPath = '%s/%s' % (memberListImgPath, self.mJobLabel)
				memberNameLabelPath = '%s/%s' % (memberListImgPath, self.mNameLabel)
				memberStatusLabelPath = '%s/%s' % (memberListImgPath, self.mStatusLabel)
				memberLevelLabelPath = '%s/%s' % (memberListImgPath, self.mLevelLabel)
				memberActivityLabelPath = '%s/%s' % (memberListImgPath, self.mActivityLabel)
				memberMoreBtnPath = '%s/%s' % (memberListImgPath, self.mMoreBtn)
				self.RemoveComponent(memberListImgPath, self.mMemberListPanel)
				self.mMemberListImgs.remove(memberListImgPath)
				self.mMemberJobLabels.remove(memberJobLabelPath)
				self.mMemberNameLabels.remove(memberNameLabelPath)
				self.mMemberStatusLabels.remove(memberStatusLabelPath)
				self.mMemberLevelLabels.remove(memberLevelLabelPath)
				self.mMemberActivityLabels.remove(memberActivityLabelPath)
				self.mMemberMoreBtns.remove(memberMoreBtnPath)
		#设置一下位移
		d = self.GetSize(self.mMemberListImg)[1]
		for i, memberListImg in enumerate(self.mMemberListImgs):
			self.SetPosition(memberListImg, (self.mMemberListImgPos[0], self.mMemberListImgPos[1] + d * i))
		
		self.mPresidentUidList = []
		self.mElderUidList = []
		self.mCommonUidList = []
		#其余情况，正常显示
		i = 0
		for playerUid, playerAttrs in presidentPlayerDict.items():
			self.SetText(self.mMemberNameLabels[i], playerAttrs.get(PlayerAttrType.Name))
			self.SetText(self.mMemberJobLabels[i], "会长")
			self.SetText(self.mMemberStatusLabels[i], onlineText[playerAttrs.get(PlayerAttrType.Online)])
			self.SetText(self.mMemberLevelLabels[i], str(playerAttrs.get(PlayerAttrType.Level)))
			self.SetText(self.mMemberActivityLabels[i], str(playerAttrs.get(PlayerAttrType.Activity)))
			self.mPresidentUidList.append(playerUid)
			i = i + 1
		for playerUid, playerAttrs in elderPlayerDict.items():
			self.SetText(self.mMemberNameLabels[i], playerAttrs.get(PlayerAttrType.Name))
			self.SetText(self.mMemberJobLabels[i], "长老")
			self.SetText(self.mMemberStatusLabels[i], onlineText[playerAttrs.get(PlayerAttrType.Online)])
			self.SetText(self.mMemberLevelLabels[i], str(playerAttrs.get(PlayerAttrType.Level)))
			self.SetText(self.mMemberActivityLabels[i], str(playerAttrs.get(PlayerAttrType.Activity)))
			self.mElderUidList.append(playerUid)
			i = i + 1
		for playerUid, playerAttrs in commonPlayerDict.items():
			self.SetText(self.mMemberNameLabels[i], playerAttrs.get(PlayerAttrType.Name))
			self.SetText(self.mMemberJobLabels[i], "会员")
			self.SetText(self.mMemberStatusLabels[i], onlineText[playerAttrs.get(PlayerAttrType.Online)])
			self.SetText(self.mMemberLevelLabels[i], str(playerAttrs.get(PlayerAttrType.Level)))
			self.SetText(self.mMemberActivityLabels[i], str(playerAttrs.get(PlayerAttrType.Activity)))
			self.mCommonUidList.append(playerUid)
			i = i + 1
		height = 10 + i * (10 + d)
		height = max(height, self.mMemberListPanelSize[1])
		self.SetSize(self.mMemberListPanel, (self.mMemberListPanelSize[0], height))
		self.SetText(self.mPartyName, "公会：" + guildName)
		self.SetText(self.mPartyActive, "本月活跃度：" + str(guildActivity))
		self.SetText(self.mPartyNumber, "人数：" + str(allPlayerNum) + "/" + str(guildMaxNum))
		
	
	def ApplyListPanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			data = {"UIDef": UIDef.UI_APPLY}
			guildConsts.GetClientModSystem().BroadcastEvent(guildConsts.ShowUIFromClientEvent, data)
	
	def MemberMorePanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/hover', "textures/ui/netease_guild/btn02@3x.png")
			self.SetSprite(args["ButtonPath"] + '/pressed', "textures/ui/netease_guild/btn02@3x.png")
			myPlayerUid = guildConsts.GetClientModSystem().GetGuildMgrGac().CheckUidByPlayerId(clientApi.GetLocalPlayerId())
			if myPlayerUid not in self.mPresidentUidList:
				return
			self.SetVisible(self.mMemberMorePanel, True)
			playerIndex = self.GetPlayerIndex(args["ButtonPath"])
			memberList = self.mPresidentUidList + self.mElderUidList + self.mCommonUidList
			self.mMorePlayerUid = memberList[playerIndex]
			if self.mMorePlayerUid in self.mCommonUidList:
				self.SetVisible(self.mMemberPromoteBtn, True)
				self.SetVisible(self.mMemberDemoteBtn, False)
				self.SetVisible(self.mMemberKickBtn, True)
				self.SetVisible(self.mMemberAppointPresidentBtn, True)
			if self.mMorePlayerUid in self.mElderUidList:
				self.SetVisible(self.mMemberPromoteBtn, False)
				self.SetVisible(self.mMemberDemoteBtn, True)
				self.SetVisible(self.mMemberKickBtn, True)
				self.SetVisible(self.mMemberAppointPresidentBtn, True)
			if self.mMorePlayerUid in self.mPresidentUidList:
				self.SetVisible(self.mMemberPromoteBtn, False)
				self.SetVisible(self.mMemberDemoteBtn, False)
				self.SetVisible(self.mMemberKickBtn, False)
				self.SetVisible(self.mMemberAppointPresidentBtn, False)
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
	
	def ChangePlayerDuty(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		buttonPath = args["ButtonPath"]
		if touchEvent == touch_event_enum.TouchUp:
			if buttonPath == self.mMemberPromoteBtn:
				data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'beAppointUid': self.mMorePlayerUid, 'desDuty': DutyType.Elder}
				guildConsts.GetClientModSystem().NotifyToServer(guildConsts.AppointPlayerFromClientEvent, data)
			elif buttonPath == self.mMemberDemoteBtn:
				data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'beAppointUid': self.mMorePlayerUid, 'desDuty': DutyType.Common}
				guildConsts.GetClientModSystem().NotifyToServer(guildConsts.AppointPlayerFromClientEvent, data)
			elif buttonPath == self.mMemberAppointPresidentBtn:
				data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'beAppointUid': self.mMorePlayerUid, 'desDuty': DutyType.President}
				guildConsts.GetClientModSystem().NotifyToServer(guildConsts.AppointPlayerFromClientEvent, data)
			elif buttonPath == self.mMemberKickBtn:
				data = {'operatorPlayerId': clientApi.GetLocalPlayerId(), 'kickUid': self.mMorePlayerUid}
				guildConsts.GetClientModSystem().NotifyToServer(guildConsts.KickPlayerFromClientEvent, data)
			self.mMorePlayerUid = -1
			
	def GetPlayerIndex(self, path):
		for index, btnPath in enumerate(self.mMemberMoreBtns):
			if btnPath == path:
				return index
		return -1
	
	def ExitGuild(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			UIOne = guildConsts.GetClientModSystem().GetUIMgr().GetUI(UIDef.UI_QUIT)
			playerUid = guildConsts.GetClientModSystem().GetGuildMgrGac().CheckUidByPlayerId(clientApi.GetLocalPlayerId())
			if UIOne:
				if playerUid in self.mPresidentUidList:
					if (len(self.mPresidentUidList) + len(self.mElderUidList) + len(self.mCommonUidList)) >= 2:
						messageData = "会长无法退出公会，请转让会长后再退出公会。"
					else:
						messageData = "当前公会只有一名成员，退出公会将直接解散公会。"
				else:
					exitGuildNotifyDef = NotifyDef.EXIT_GUILD.copy()
					messageData = exitGuildNotifyDef["message"].replace("%s", self.mGuildName)
				UIOne.SetNotifyPanel(NotifyDef.EXIT_GUILD, self.SureExit, self.CancelExit, messageData)
	
	def SureExit(self):
		data = {'playerId': clientApi.GetLocalPlayerId()}
		guildConsts.GetClientModSystem().NotifyToServer(guildConsts.ExitGuildFromClientEvent, data)
	
	def ReturnGuildMap(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			data = {'playerId': clientApi.GetLocalPlayerId()}
			guildConsts.GetClientModSystem().NotifyToServer(guildConsts.ReturnGuildMapFromClientEvent, data)
	
	def CancelExit(self):
		pass
	
	def ShowTipsNewImg(self, isShow):
		self.SetVisible(self.mTipsNewImg, isShow)
	
	def InitScreen(self):
		pass
	
	def Create(self):
		# 成员列表Title
		scrollBase = self.mMyPartyImg + "/myguild_scroll_base"
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
		
		#self.mMemberListPanel = self.mMyPartyImg + "/myguild_scroll_base/memberlist_pnl"
		self.mMemberTitle = self.mMyPartyImg + "/member_title_lbl"
		self.mJobTitle = self.mMyPartyImg + "/job_title_lbl"
		self.mLevelTitle = self.mMyPartyImg + "/level_title_lbl"
		self.mStatusTitle = self.mMyPartyImg + "/status_title_lbl"
		self.mActiveTitle = self.mMyPartyImg + "/partyactive_title_lbl"
		
		# 成员列表信息
		self.mMemberListImg = self.mMemberListPanel + "/memberlist_img_1"
		# 这个是因为至少有一个成员，不然就解散了，所以至少有一个成员panel
		self.mMemberListImgs = [
			self.mMemberListImg
		]
		self.mJobLabel = "job_lbl"
		self.mNameLabel = "member_lbl"
		self.mStatusLabel = "status_lbl"
		self.mLevelLabel = "level_lbl"
		self.mActivityLabel = "partyactive_lbl"
		self.mMoreBtn = "more_btn"
		self.mMemberJobLabels = [
			self.mMemberListImg + "/" + self.mJobLabel
		]
		self.mMemberNameLabels = [
			self.mMemberListImg + "/" + self.mNameLabel
		]
		self.mMemberStatusLabels = [
			self.mMemberListImg + "/" + self.mStatusLabel
		]
		self.mMemberLevelLabels = [
			self.mMemberListImg + "/" + self.mLevelLabel
		]
		self.mMemberActivityLabels = [
			self.mMemberListImg + "/" + self.mActivityLabel
		]
		self.mMemberMoreBtns = [
			self.mMemberListImg + "/" + self.mMoreBtn
		]
		
		self.mMemberListImgPos = self.GetPosition(self.mMemberListImg)
		#self.ShowPanel(False)
		self.SetVisible(self.mMyGuildPanel, False)
		self.AddTouchEventHandler(self.mCloseBtn, self.ClosePanel)
		self.AddTouchEventHandler(self.mApplyListBtn, self.ApplyListPanel)
		self.AddTouchEventHandler(self.mBoWoutBtn, self.ExitGuild)
		self.AddTouchEventHandler(self.mMemberPromoteBtn, self.ChangePlayerDuty)
		self.AddTouchEventHandler(self.mMemberDemoteBtn, self.ChangePlayerDuty)
		self.AddTouchEventHandler(self.mMemberKickBtn, self.ChangePlayerDuty)
		self.AddTouchEventHandler(self.mMemberAppointPresidentBtn, self.ChangePlayerDuty)
		self.AddTouchEventHandler(self.mReturnBtn, self.ReturnGuildMap)
		
		for index, memberMorePath in enumerate(self.mMemberMoreBtns):
			self.AddTouchEventHandler(memberMorePath, self.MemberMorePanel)
		
		
	def ClosePanel(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			self.ShowPanel(False)
	
	def ShowPanel(self, isShow):
		if isShow:
			clientApi.SetInputMode(1)
		else:
			clientApi.SetInputMode(0)
		self.SetVisible(self.mMyGuildPanel, isShow)
		
	def SetUITouchEnable(self, isTouch):
		self.SetTouchEnable(self.mMyGuildPanel, isTouch)
		
	