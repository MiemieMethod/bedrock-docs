# -*- coding: utf-8 -*-
import random
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseFriendScript.apiUtil as apiUtil
import weakref
import neteaseFriendScript.friendConsts as friendConsts
from neteaseFriendScript.ui.uiDef import UIDef

TalkShowTimeIntervalMax = 600
TalkShowTimeIntervalMin = 15
LengthLineOne = 16
LengthLineTwo = 32
TalkLengthMin = 50
TalkLengthMax = 100
FakeTalkMessages = (
	"hello, how are you?",
	"hello, how are you? fine, thank you?",
	"hello, how are you? fine, thank you, and you? I am fine too.",
	"我是一行字。o1o",
	"我希望自己是两行字，所以有点多。o1o",
	"我希望自己是三行字，所有要非常多非常多非常多非常多非常多。o1o",
)

class panelType:
	friend = 0
	black = 1
	temp =2

class FriendListScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIFriendList
		self.mRecentTalkList = []
		self.mTalkWarningCooldown = 0
		self.mTextInput = ""
		self.mClientSystem = None
		self.ori_uid_list = []
		self.ori_temp_uid_list = []

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIOpen(self.mUiKey)
			self.SetInputEnable(True)
		else:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIClose(self.mUiKey)
			self.SetInputEnable(False)
			self.mSelectFriendUid = None
			self.mSelectBlackUid = None
			self.mSelectTempUid = None
		self.SetVisible("", flag)
		
	def GetIsShow(self):
		return self.mBShow

	def InitScreen(self):
		self.ChangeScreenVisible(False)
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		
		
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'LocalUpdatePlayerData', self, self.OnLocalUpdatePlayerData)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'LocalChatRecordData', self, self.OnLocalChatRecordData)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'LocalFriendListChangeEvent', self, self.OnLocalFriendListChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'LocalTempListChangeEvent', self, self.OnLocalTempListChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'LocalRNFriendListChangeEvent', self, self.OnLocalFriendListChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalBlackListChangeEvent', self, self.OnLocalBlackListChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, 'ClientFriendStateChangeEvent', self, self.OnClientFriendChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, 'ClientTempChatTimeChangeEvent', self, self.OnClientTempChatTimeChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalIsAnyChatNewChange', self, self.OnLocalIsAnyChatNewChange)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalFriendUnReadChangeEvent', self, self.OnLocalFriendUnReadChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalLoadYourPlayerData', self, self.OnLocalLoadYourPlayerData)
		
	def OnLocalIsAnyChatNewChange(self, args):
		self.DrawPanelLeft()
		self.DrawFriendListSelect()
		
	def OnLocalFriendUnReadChangeEvent(self, args):
		self.ReDrawAll()
		
	def OnLocalFriendListChangeEvent(self, args):
		self.OnFriendListChange()
		
	def OnLocalTempListChangeEvent(self, args):
		self.OnTempListChange()
		
	def OnLocalBlackListChangeEvent(self, args):
		self.OnBlackListChange()
		
	def OnLocalUpdatePlayerData(self, args):
		print "OnLocalUpdatePlayerData", args
		uid = args.get("uid")
		if uid != self.mClientSystem.mMyPlayerUid:
			self.ReDrawOnePlayerData(uid)
			self.ReDrawAll(drawTalk=True)
		else:
			self.mLocalPlayerHead = self.GetLocalPlayerHeadImage()
			self.ReDrawAll(drawTalk=True)
			
	def OnLocalLoadYourPlayerData(self, args):
		self.mLocalPlayerHead = self.GetLocalPlayerHeadImage()
	
	def OnClientFriendChangeEvent(self, args):
		self.updateOnlineNum()
		if self.mShowIngListType == panelType.friend:
			self.DrawFriendList()
		
	def OnClientTempChatTimeChangeEvent(self, args):
		self.updateTempChatDes()
		if self.mShowIngListType == panelType.temp:
			self.DrawTempList()
		
	def ReDrawOnePlayerData(self, uid):
		if uid not in self.ori_uid_list:
			return
		idx = self.ori_uid_list.index(uid)
		singlePart = self.mSinglePlayerList[idx]
		print "ReDrawOnePlayerData", uid
		self.DrawSinglePlayerPart(singlePart, uid)

	def DrawSinglePlayerPart(self, singlePart, uid):
		playerData = self.GetPlayerDataByUid(uid)
		if not playerData:
			playerData = {
				"nickname": "正在获取中",
				"head_image": "textures/ui/netease_friend/img01@3x",
			}
		self.SetText("%s/lb_friend_name" % singlePart, playerData["nickname"])
		self.SetSprite("%s/img_friend_head" % singlePart, playerData["head_image"])
		if self.mShowIngListType == panelType.friend:
			self.SetVisible("%s/btn_friend_remove" % singlePart, False)
			self.SetVisible("%s/img_friend_tag1" % singlePart, True)
			if self.IsFriendOnline(uid):
				self.SetSprite("%s/img_friend_tag1" % singlePart, "textures/ui/netease_friend/tag02@3x")
			else:
				self.SetSprite("%s/img_friend_tag1" % singlePart, "textures/ui/netease_friend/tag02_02@3x")
			if self.IsPlatformFriend(uid):
				self.SetVisible("%s/img_friend_tag2" % singlePart, True)
			else:
				self.SetVisible("%s/img_friend_tag2" % singlePart, False)
			if self.IsFriendNewTalk(uid):
				self.SetVisible("%s/img_friend_tag3" % singlePart, True)
			else:
				self.SetVisible("%s/img_friend_tag3" % singlePart, False)
		elif self.mShowIngListType == panelType.black:
			self.SetVisible("%s/btn_friend_remove" % singlePart, True)
			self.SetVisible("%s/img_friend_tag1" % singlePart, False)
			self.SetVisible("%s/img_friend_tag2" % singlePart, False)
			self.SetVisible("%s/img_friend_tag3" % singlePart, False)
		else:
			self.SetVisible("%s/btn_friend_remove" % singlePart, False)
			self.SetVisible("%s/img_friend_tag1" % singlePart, False)
			self.SetVisible("%s/img_friend_tag2" % singlePart, False)
			self.SetVisible("%s/img_friend_tag3" % singlePart, False)
		
	def updateOnlineNum(self):
		self.ori_uid_list = self.GetFriendUidList()
		self.mFriendUidList = []
		self.onlineNum = 0
		for idx, uid in enumerate(self.ori_uid_list):
			data = {"uid": uid}
			state = self.mClientSystem.mFriendManager.mFriendState.get(uid, 1)
			data["state"] = state
			if state == 1:
				self.onlineNum += 1
			self.mFriendUidList.append(data)
		self.mFriendUidList.sort(self.cmp_friend)
		self.ori_uid_list = []
		for fData in self.mFriendUidList:
			self.ori_uid_list.append(fData["uid"])
		if self.mShowIngListType == panelType.friend:
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", True)
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", "在线:%d" % self.onlineNum)
		
	def updateTempChatDes(self):
		self.ori_temp_uid_list = self.GetTempList()
		self.mTempUidList = []
		for idx, uid in enumerate(self.ori_temp_uid_list):
			data = {"uid": uid}
			data["lastChatTime"] =  self.mClientSystem.mChatManager.mLastChatTime.get("uid", 0)
			self.mTempUidList.append(data)
		self.mTempUidList.sort(self.cmp_temp_friend)
		
	def OnLocalChatRecordData(self, args):
		print "OnLocalChatRecordData", args
		if self.mShowIngListType == panelType.friend:
			if self.mSelectFriendUid and self.mSelectFriendUid == args.get("friendUid"):
				self.ReDrawAllTalks(args.get("friendUid"), self.mClientSystem.mChatManager.TryGetRecord(args.get("friendUid")))
		elif self.mShowIngListType == panelType.temp:
			if self.mSelectTempUid and self.mSelectTempUid == args.get("friendUid"):
				self.ReDrawAllTalks(args.get("friendUid"), self.mClientSystem.mChatManager.TryGetRecord(args.get("friendUid")))
		
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if self.mTalkWarningCooldown > 0:
			self.mTalkWarningCooldown -= 1
			if self.mTalkWarningCooldown <= 0:
				self.ShowTalkWarning("")

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		# 关闭按钮
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_close", self.OnButtonClose)
		# 好友列表
		scrollInfo = {}
		scrollBase = "/main_pnl/pnl_invite/img_base_friends/scroll_friend_list"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			scrollInfo["parent"] = scrollBaseTouch
			scrollInfo["parent_size"] = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			scrollInfo["parent"] = scrollBaseMouse
			scrollInfo["parent_size"] = size
		scrollInfo["base"] = scrollInfo["parent"] + "/btn_friend_base"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["base_offset"] = 2
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mSinglePlayerList = []
		self.mPlayerListScrollInfo = scrollInfo
		self.PlayerListResize(0)
		# for key, value in self.mPlayerListScrollInfo.iteritems():
		#	print "key=%s value=%s" % (key, str(value))
		# 聊天语句
		scrollInfo = {}
		scrollBase = "/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe"
		scrollBaseTouch = scrollBase + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		size = self.GetSize(scrollBaseTouch)
		if size:
			scrollInfo["parent"] = scrollBaseTouch
			scrollInfo["parent_size"] = size
		else:
			scrollBaseMouse = scrollBase + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			size = self.GetSize(scrollBaseMouse)
			scrollInfo["parent"] = scrollBaseMouse
			scrollInfo["parent_size"] = size
		scrollInfo["base"] = scrollBase
		scrollInfo["base_dict"] = {}
		for style, name in {"time":"/lb_time_base", "other":"/pnl_talk_base_other", "me":"/pnl_talk_base_me"}.iteritems():
			part = {}
			part["base"] = scrollInfo["parent"] + name
			part["base_size"] = self.GetSize(part["base"])
			part["base_pos"] = self.GetPosition(part["base"])
			scrollInfo["base_dict"][style] = part
			self.SetVisible(part["base"], False)
		scrollInfo["base_offset"] = 2
		scrollInfo["max_pid"] = 1
		self.mTalkScrollInfo = scrollInfo
		self.mUsedTalkDict = {}
		self.mFreeTalkDict = {}
		for style in ("time", "other", "me"):
			self.mFreeTalkDict[style] = []
		self.ResetTalkDraw()
		# 左侧分页按钮
		self.SetTouchEnable("/main_pnl/tab_left_friends", False)
		self.mNewTagFriend = "/main_pnl/tab_left_friends/img_list_new"
		self.SetVisible(self.mNewTagFriend, False)
		self.SetTouchEnable("/main_pnl/tab_left_add", True)
		self.mNewTagInvite = "/main_pnl/tab_left_add/img_invite_new"
		self.SetVisible(self.mNewTagInvite, False)
		self.AddTouchEventHandler("/main_pnl/tab_left_add", self.OnButtonInvite)
		# 上方分页按钮、弹出菜单按钮
		self.mShowIngListType = panelType.friend
		self.mSelectFriendUid = None
		self.mSelectBlackUid = None
		self.mSelectTempUid = None
		self.mSelectFriendHead = ""
		self.mFriendUidList = []
		self.mBlackUidList = []
		self.mTempUidList = []
		self.mLocalPlayerHead = self.GetLocalPlayerHeadImage()
		#
		self.mUpperTabButtons = {
			panelType.friend: "/main_pnl/pnl_invite/img_base_friends/tab_upper_myFriends",
			panelType.black: "/main_pnl/pnl_invite/img_base_friends/tab_upper_blacklist",
			panelType.temp: "/main_pnl/pnl_invite/img_base_friends/tab_upper_temp",
		}
		self.SetTouchEnable(self.mUpperTabButtons[panelType.friend], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[panelType.friend], self.OnButtonShowFriend)
		self.SetTouchEnable(self.mUpperTabButtons[panelType.black], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[panelType.black], self.OnButtonShowBlack)
		self.SetTouchEnable(self.mUpperTabButtons[panelType.temp], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[panelType.temp], self.OnButtonShowTemp)
		#
		self.mIsShowFriendHint = True
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_settings", self.OnButtonTopHint)
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", self.OnButtonAddBlack)
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", self.OnButtonDelFriend)
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", self.OnButtonAddFriend)
		# 右方发送按钮
		self.mInputLabelName = '/main_pnl/pnl_invite/img_base_friends/text_edit_input'
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_send", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_friends/btn_send", self.OnButtonSendTalk)

	def PlayerListResize(self, size):
		"""
		左侧好友列表长度变化（由新增好友或者删除好友触发）
		"""
		# 假如resize的尺寸刚好和之前的尺寸相同，那么不需要做任何事，直接return
		# 某些全局刷新操作也会触发这个函数
		scrollInfo = self.mPlayerListScrollInfo
		if size == scrollInfo["size"]:
			return
		# 记录下最新的列表尺寸
		scrollInfo["size"] = size
		# 界面显示要求：如果好友列表为空，需要显示一句特别的提示文字
		if size == 0:
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_left_friendsList_empty", True)
			if self.mShowIngListType == panelType.friend:
				self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_left_friendsList_empty", "当前没有好友")
			elif self.mShowIngListType == panelType.temp:
				self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_left_friendsList_empty", "当前没有临时好友")
			else:
				self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_left_friendsList_empty", "")
		else:
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_left_friendsList_empty", False)
		# 计算一下需要新生成的单个好友控件数量
		lackNum = size - len(self.mSinglePlayerList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(self.mSinglePlayerList)
			for idx in xrange(lackNum):
				self.CloneSinglePlayer(beginIndex + idx, scrollInfo)
		# 控件多余了，那么隐藏多余不用的控件
		for idx, part in enumerate(self.mSinglePlayerList):
			if idx < size:
				self.SetVisible(part, True)
			else:
				self.SetVisible(part, False)
		# 重设滚动区域的大小
		height = scrollInfo["base_pos"][1] + size * (scrollInfo["base_size"][1] + scrollInfo["base_offset"])
		height = max(height, scrollInfo["parent_size"][1])
		self.SetSize(scrollInfo["parent"], (scrollInfo["parent_size"][0], height))

	def CloneSinglePlayer(self, idx, scrollInfo):
		name = "btn_friend_%d" % idx
		self.Clone(scrollInfo["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.mSinglePlayerList.append(fullName)
		height = scrollInfo["base_pos"][1] + idx * (scrollInfo["base_size"][1] + scrollInfo["base_offset"])
		self.SetPosition(fullName, (scrollInfo["base_pos"][0], height))
		#
		self.SetTouchEnable(fullName, True)
		self.AddTouchEventHandler(fullName, self.OnClickPlayerMain)
		self.SetTouchEnable("%s/btn_friend_remove" % fullName, True)
		self.AddTouchEventHandler("%s/btn_friend_remove" % fullName, self.OnClickPlayerDelBlack)
	# --------------------------------------------------------------------------------------
	def ResetTalkDraw(self):
		self.mTalkLinkedUid = None
		self.mTalkLastTime = 0
		self.mTalkLastShowTime = 0
		self.mRecentH = 5
		for pid in self.mUsedTalkDict.keys():
			self.FreeSingleTalk(pid)

	def FreeSingleTalk(self, pid):
		data = self.mUsedTalkDict.get(pid, None)
		if not data:
			return
		del self.mUsedTalkDict[pid]
		style, name = data["style"], data["name"]
		self.SetVisible(name, False)
		self.mFreeTalkDict[style].append(data)

	def TalkCheckShowTime(self, now, singleTalk):
		timestamp = singleTalk["chatTime"]
		if (self.mTalkLastTime <= 0) and (now - timestamp < TalkShowTimeIntervalMax):
			return None
		if timestamp - self.mTalkLastTime < TalkShowTimeIntervalMin:
			return None
		if timestamp - self.mTalkLastShowTime < TalkShowTimeIntervalMax:
			return None
		self.mTalkLastShowTime = timestamp
		return timestamp

	def ReDrawAllTalks(self, uid, talkList):
		self.ResetTalkDraw()
		if len(talkList) > TalkLengthMin:
			talkList = talkList[-TalkLengthMin:]
		self.mRecentTalkList = talkList
		self.mTalkLinkedUid = uid
		now = int(time.time())
		yearNow = time.localtime().tm_year
		todayS, yesterdayS, weekS = apiUtil.GetTodayStart(now), apiUtil.GetYesterdayStart(now), apiUtil.GetWeekStart(now)
		for singleTalk in talkList:
			tp = self.TalkCheckShowTime(now, singleTalk)
			if not tp is None:
				timestr = apiUtil.GetTalkTimeFormat(tp, todayS, yesterdayS, weekS, yearNow)
				self.AppendTalkTime(timestr, autoResize=False)
			self.AppendTalk(uid, singleTalk, autoResize=False)
			self.mTalkLastTime = singleTalk["chatTime"]
		self.DoTalkResize()
		#自动拉到最底
		self.SetScrollViewPercentValue(self.mTalkScrollInfo["base"], 100)

	def AddNewTalk(self, talkList):
		length = len(self.mRecentTalkList) + len(talkList)
		# 需要截取，彻底重绘
		if length > TalkLengthMax:
			newTalkList = self.mRecentTalkList[:]
			newTalkList.extend(talkList)
			self.ReDrawAllTalks(self.mTalkLinkedUid, newTalkList)
			return
		now = int(time.time())
		yearNow = time.localtime().tm_year
		todayS, yesterdayS, weekS = apiUtil.GetTodayStart(now), apiUtil.GetYesterdayStart(now), apiUtil.GetWeekStart(now)
		for singleTalk in talkList:
			tp = self.TalkCheckShowTime(now, singleTalk)
			if not tp is None:
				timestr = apiUtil.GetTalkTimeFormat(tp, todayS, yesterdayS, weekS, yearNow)
				self.AppendTalkTime(timestr, autoResize=False)
			self.AppendTalk(self.mTalkLinkedUid, singleTalk, autoResize=False)
			self.mTalkLastTime = singleTalk["chatTime"]
		self.DoTalkResize()

	def DoTalkResize(self):
		height = max(self.mRecentH, self.mTalkScrollInfo["parent_size"][1])
		self.SetSize(self.mTalkScrollInfo["parent"], (self.mTalkScrollInfo["parent_size"][0], height))

	def AppendTalkTime(self, timestr, autoResize=False):
		data = self.CloneTalkByStyle("time")
		self.SetVisible(data["name"], True)
		self.SetText(data["name"], timestr)
		self.SetPosition(data["name"], (data["x"], self.mRecentH))
		self.mRecentH += data["h"] + self.mTalkScrollInfo["base_offset"]
		if autoResize:
			self.DoTalkResize()
		return data["h"] + self.mTalkScrollInfo["base_offset"]

	def AppendTalk(self, uid, singleTalk, autoResize=False):
		if uid == singleTalk["fromUid"]:	# 好友的发言
			style = "other"
			image = self.mSelectFriendHead
		else:
			style = "me"
			image = self.mLocalPlayerHead
		data = self.CloneTalkByStyle(style)
		self.SetVisible(data["name"], True)
		lbName = "%s/img_bg_%s/lb_talk_%s" % (data["name"], style, style)
		self.SetText(lbName, singleTalk["message"], syncSize=True)
		self.SetSprite(data["name"], image)
		size = self.GetSize(lbName)
		bgSize = (93, size[1]+4)
		data["h"] = bgSize[1]
		self.SetSize("%s/img_bg_%s" % (data["name"], style), bgSize)
		self.SetPosition(data["name"], (data["x"], self.mRecentH))
		self.mRecentH += data["h"] + self.mTalkScrollInfo["base_offset"]
		if autoResize:
			self.DoTalkResize()
		return data["h"] + self.mTalkScrollInfo["base_offset"]

	def CloneTalkByStyle(self, style):
		freeList = self.mFreeTalkDict[style]
		if freeList:
			data = freeList.pop(0)
			self.mUsedTalkDict[data["pid"]] = data
			return data
		scrollInfo = self.mTalkScrollInfo
		pid = scrollInfo["max_pid"]
		scrollInfo["max_pid"] += 1
		name = "talk_pid_%d" % pid
		part = scrollInfo["base_dict"][style]
		self.Clone(part["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.SetVisible(fullName, True)
		data = {
			"name": fullName,
			"pid": pid,
			"style": style,
			"x": part["base_pos"][0],
			"h": part["base_size"][1],
		}
		if style == "me":
			data["x"] -= 4
		self.mUsedTalkDict[pid] = data
		return data
	# ---------------------------------------------------------------------------------
	def DrawPanelLeft(self):
		if self.IsAnyFriendNewTalk():
			self.SetVisible(self.mNewTagFriend, True)
		else:
			self.SetVisible(self.mNewTagFriend, False)
		if self.IsAnyFriendInvite():
			self.SetVisible(self.mNewTagInvite, True)
		else:
			self.SetVisible(self.mNewTagInvite, False)

	def DrawPanelTop(self):
		for stype in (panelType.friend, panelType.black, panelType.temp):
			if self.mShowIngListType == stype:
				apiUtil.DrawButtonImage(self, self.mUpperTabButtons[stype], "btn03_select@3x")
			else:
				apiUtil.DrawButtonImage(self, self.mUpperTabButtons[stype], "btn03@3x")
		if self.mShowIngListType == panelType.friend:
			self.DrawFriendList()
			self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings", True)
		elif self.mShowIngListType == panelType.black:
			self.ChangeFriendHintShow(False)
			self.DrawBlackList()
			self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings", False)
		else:
			self.ChangeFriendHintShow(False)
			self.DrawTempList()
			self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_settings", True)

	def DrawTempList(self):
		size = len(self.mTempUidList)
		self.PlayerListResize(size)
		friendMaxNum = self.mClientSystem.mFriendManager.TEMP_MAX_NUM
		text = "临时聊天数量 %d/%d" % (size, friendMaxNum)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", False)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_totalNumbers", True)
		self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_totalNumbers", text)
		#
		for idx, tData in enumerate(self.mTempUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.SetVisible("%s/btn_del_black" % singlePart, True)
			self.DrawSinglePlayerPart(singlePart, tData["uid"])
		self.DrawTempListSelect()

	def DrawTempListSelect(self):
		for idx, tData in enumerate(self.mTempUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.SetVisible("%s/img_friend_selected" % singlePart, False)
			if tData["uid"] == self.mSelectTempUid:
				apiUtil.DrawButtonImage(self, singlePart, "btn01_select")
			else:
				apiUtil.DrawButtonImage(self, singlePart, "btn01")
				
	def DrawFriendList(self):
		size = len(self.mFriendUidList)
		self.PlayerListResize(size)
		self.onlineNum = 0
		for idx, fData in enumerate(self.mFriendUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.DrawSinglePlayerPart(singlePart, fData["uid"])
			if self.IsFriendOnline(fData["uid"]):
				self.onlineNum += 1
		self.DrawFriendListSelect()
		friendMaxNum = self.mClientSystem.mFriendManager.FRIENDS_MAX_NUM
		text = "好友数量:%d/%d" % (size, friendMaxNum)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_totalNumbers", True)
		self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_totalNumbers", text)
		text = "在线:%d" % self.onlineNum
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", True)
		self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", text)

	def DrawFriendListSelect(self):
		for idx, fData in enumerate(self.mFriendUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.SetVisible("%s/img_friend_selected" % singlePart, False)
			if fData["uid"] == self.mSelectFriendUid:
				apiUtil.DrawButtonImage(self, singlePart, "btn01_select")
			else:
				apiUtil.DrawButtonImage(self, singlePart, "btn01")
			if self.IsFriendNewTalk(fData["uid"]):
				self.SetVisible("%s/img_friend_tag3" % singlePart, True)
			else:
				self.SetVisible("%s/img_friend_tag3" % singlePart, False)

	def DrawBlackList(self):
		self.mBlackUidList = self.GetBlackUidList()
		size = len(self.mBlackUidList)
		self.PlayerListResize(size)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_totalNumbers", False)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_onlineNumbers", False)
		for idx, uid in enumerate(self.mBlackUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.DrawSinglePlayerPart(singlePart, uid)
		self.DrawBlackListSelect()

	def DrawBlackListSelect(self):
		for idx, uid in enumerate(self.mBlackUidList):
			singlePart = self.mSinglePlayerList[idx]
			self.SetVisible("%s/img_friend_selected" % singlePart, False)
			if uid == self.mSelectBlackUid:
				apiUtil.DrawButtonImage(self, singlePart, "btn01_select")
			else:
				apiUtil.DrawButtonImage(self, singlePart, "btn01")

	def ChangeFriendHintShow(self, isShow=None):
		if isShow is None:
			self.mIsShowFriendHint = not self.mIsShowFriendHint
		else:
			self.mIsShowFriendHint = isShow
		if self.mIsShowFriendHint:
			if self.mShowIngListType == panelType.friend:
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", True)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", True)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", False)
			elif self.mShowIngListType == panelType.temp:
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", True)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", False)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", True)
			else:
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", False)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", False)
				self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", False)
		else:
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toBlacklist", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_delete", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_settings/btn_unfold_toFriend", False)

	def ShowTalkWarning(self, text, cooldown=90):
		if not text:
			self.SetVisible("/main_pnl/pnl_invite/pnl_input_hint", False)
			self.mTalkWarningCooldown = 0
			return
		self.SetVisible("/main_pnl/pnl_invite/pnl_input_hint", True)
		self.SetText("/main_pnl/pnl_invite/pnl_input_hint/lb_input_hint", text)
		self.mTalkWarningCooldown = cooldown

	def DrawTalkPanel(self):
		if self.mShowIngListType == panelType.friend:
			self.DrawFriendTalkPanel()
		elif self.mShowIngListType == panelType.black:
			self.DrawBlackTalkPanel()
		else:
			self.DrawTempTalkPanel()

	def DrawTempTalkPanel(self):
		if self.mSelectTempUid is None:
			self.SetVisible(self.mInputLabelName, False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", True)
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", "请选择一名玩家开始临时聊天")
			return
		friendData = self.GetPlayerDataByUid(self.mSelectTempUid)
		self.SetVisible(self.mInputLabelName, True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", True)
		if friendData:
			self.mSelectFriendHead = friendData["head_image"]
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "与%s对话中" % friendData["nickname"])
		else:
			self.mSelectFriendHead = "textures/ui/netease_friend/img01@3x"
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "")
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", True)
		talkList = self.GetTalkByUid(self.mSelectTempUid)
		self.ReDrawAllTalks(self.mSelectTempUid, talkList)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", False)
		self.mClientSystem.BroadcastEvent("LocalReadChatEvent", {"mSelectFriendUid": self.mSelectFriendUid})

	def DrawBlackTalkPanel(self):
		if self.mSelectBlackUid is None:
			self.SetVisible(self.mInputLabelName, False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", False)
			return
		friendData = self.GetPlayerDataByUid(self.mSelectBlackUid)
		self.SetVisible(self.mInputLabelName, True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", True)
		if friendData:
			self.mSelectFriendHead = friendData["head_image"]
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "与%s的聊天历史" % friendData["nickname"])
		else:
			self.mSelectFriendHead = "textures/ui/netease_friend/img01@3x"
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "")
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", True)
		talkList = self.GetTalkByUid(self.mSelectBlackUid)
		self.ReDrawAllTalks(self.mSelectBlackUid, talkList)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", False)

	def DrawFriendTalkPanel(self):
		if self.mSelectFriendUid is None:
			self.SetVisible(self.mInputLabelName, False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", True)
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", "请选择一名好友开始聊天")
			return
		friendData = self.GetPlayerDataByUid(self.mSelectFriendUid)
		self.SetVisible(self.mInputLabelName, True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/btn_send", True)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", True)
		if friendData:
			self.mSelectFriendHead = friendData["head_image"]
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "与%s对话中" % friendData["nickname"])
		else:
			self.mSelectFriendHead = "textures/ui/netease_friend/img01@3x"
			self.SetText("/main_pnl/pnl_invite/img_base_friends/lb_title_chat", "")
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/scroll_right_chatframe", True)
		talkList = self.GetTalkByUid(self.mSelectFriendUid)
		self.ReDrawAllTalks(self.mSelectFriendUid, talkList)
		self.SetVisible("/main_pnl/pnl_invite/img_base_friends/lb_right_chat_empty", False)
		self.mClientSystem.BroadcastEvent("LocalReadChatEvent", {"mSelectFriendUid":self.mSelectFriendUid})

	def ChangeSelectBlack(self, uid):
		if self.mSelectBlackUid == uid:
			return
		self.mSelectBlackUid = uid
		self.DrawBlackListSelect()
		self.DrawTalkPanel()
		
	def ChangeSelectTemp(self, uid):
		#print "ChangeSelectTemp be", self.mSelectTempUid, uid
		if self.mSelectTempUid == uid:
			return
		#print "ChangeSelectTemp af", self.mSelectTempUid, uid
		self.mSelectTempUid = uid
		self.DrawTempListSelect()
		self.DrawTalkPanel()

	def ChangeSelectFriend(self, uid):
		if self.mSelectFriendUid == uid:
			return
		self.mSelectFriendUid = uid
		self.DrawFriendListSelect()
		self.DrawTalkPanel()
		if self.mClientSystem.mChatManager.mIsAnyChatNew.get(self.mSelectFriendUid, False) == True:
			self.mClientSystem.BroadcastEvent("LocalReadChatEvent", {"mSelectFriendUid": self.mSelectFriendUid})
	
	def DrawSendButton(self, enable=None):
		text = self.GetEditText(self.mInputLabelName)
		if not text:
			text = ""
		self.mTextInput = text.strip()
		if enable is None:
			if self.mTextInput:
				enable = True
			else:
				enable = False
		# print "DrawSendButton text={} enable={}".format(text, enable)
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_friends/btn_send", enable)
		if enable:
			apiUtil.DrawButtonImage(self, "/main_pnl/pnl_invite/img_base_friends/btn_send", "btn01@3x")
		else:
			apiUtil.DrawButtonImage(self, "/main_pnl/pnl_invite/img_base_friends/btn_send", "btn01_select@3x")
	# ---------------------------------------------------------------------------------
	def Show(self):
		self.ChangeScreenVisible(True)
		self.ReDrawAll(drawTalk=True)
		self.ChangeFriendHintShow(False)
		self.ShowTalkWarning("")

	def ReDrawAll(self, drawTalk=False):
		self.DrawPanelLeft()
		self.DrawPanelTop()
		self.DrawSendButton()
		if drawTalk:
			self.DrawTalkPanel()

	def OnFriendListChange(self):
		#self.mFriendUidList = self.GetFriendUidList()
		self.ori_uid_list = self.GetFriendUidList()
		self.mFriendUidList = []
		for idx, uid in enumerate(self.ori_uid_list):
			data = {"uid":uid}
			data["state"] = self.mClientSystem.mFriendManager.mFriendState.get(uid, 1)
			self.mFriendUidList.append(data)
		self.mFriendUidList.sort(self.cmp_friend)
		self.ori_uid_list = []
		for fData in self.mFriendUidList:
			self.ori_uid_list.append(fData["uid"])
		# 删除了正在聊天的Friend，需要清理聊天列表
		if self.mSelectFriendUid and self.mSelectFriendUid not in self.ori_uid_list:
			self.mSelectFriendUid = None
			self.ReDrawAll(drawTalk=True)
		else:
			self.ReDrawAll(drawTalk=False)
			
	def cmp_friend(self, a, b):
		return cmp(a["state"], b["state"])
	
	def cmp_temp_friend(self, a, b):
		return cmp(a["lastChatTime"], b["lastChatTime"])

	def OnBlackListChange(self):
		newBlackList = self.GetBlackUidList()
		if self.mSelectBlackUid and self.mSelectBlackUid not in newBlackList:
			self.mSelectBlackUid = None
			self.ReDrawAll(drawTalk=True)
		else:
			self.ReDrawAll(drawTalk=False)
			
	def OnTempListChange(self):
		self.ori_temp_uid_list = self.GetTempList()
		self.mTempUidList = []
		for idx, uid in enumerate(self.ori_temp_uid_list):
			data = {"uid": uid}
			data["lastChatTime"] = self.mClientSystem.mChatManager.mLastChatTime.get("uid", 0)
			self.mTempUidList.append(data)
		self.mTempUidList.sort(self.cmp_temp_friend)
		if self.mSelectTempUid and self.mSelectTempUid not in self.ori_temp_uid_list:
			self.mSelectTempUid = None
			self.ReDrawAll(drawTalk=True)
		else:
			self.ReDrawAll(drawTalk=False)

	def OnFriendTalkArrive(self, uid, talkList):
		if uid != self.mSelectFriendUid:
			self.DrawPanelLeft()
			self.DrawFriendListSelect()
		else:
			self.AddNewTalk(talkList)

	def OnFriendInviteArrive(self):
		self.DrawPanelLeft()
	# ---------------------------------------------------------------------------------
	def GetFriendUidList(self):
		# if self.mFriendUidList:
		# 	return self.mFriendUidList
		# _list = []
		# for i in xrange(random.randint(3, 40)):
		# 	_list.append(1000*i + random.randint(1000, 1999))
		# return _list
		if self.mClientSystem.mFriendManager.mFriendData.GetFriends() is None:
			return []
		else:
			return self.mClientSystem.mFriendManager.mFriendData.GetFriends()

	def GetBlackUidList(self):
		#if self.mBlackUidList:
		# 	return self.mBlackUidList
		# _list = []
		# for i in xrange(random.randint(3, 40)):
		# 	_list.append(1000 * i + random.randint(1000, 1999))
		# return _list
		if self.mClientSystem.mFriendManager.mFriendData.GetBlackList() is None:
			return []
		else:
			return self.mClientSystem.mFriendManager.mFriendData.GetBlackList()
		
	def GetTempList(self):
		if self.mClientSystem.mFriendManager.mFriendData.GetTempFriends() is None:
			return []
		else:
			return self.mClientSystem.mFriendManager.mFriendData.GetTempFriends()

	def GetTalkByUid(self, uid):
		# _list = []
		# now = int(time.time())
		# for i in xrange(random.randint(20,60)):
		# 	data = {
		# 		"fromUid": random.choice([uid, 11]),
		# 		"chatTime": random.randint(now-86400*15, now-1),
		# 		"message": random.choice(FakeTalkMessages),
		# 	}
		# 	_list.append(data)
		# _list.sort(self.CmpChatTime)
		# return _list
		return self.mClientSystem.mChatManager.TryGetRecord(uid)

	def CmpChatTime(self, a, b):
		return cmp(a["chatTime"], b["chatTime"])

	def GetPlayerDataByUid(self, uid):
		# data = {
		# 	"uid": uid,
		# 	"nickname": "昵称:%d" % uid,
		# 	"head_image": "textures/ui/netease_friend/img01@3x",
		# }
		# return data
		if self.mClientSystem.mPlayerManager.getPlayerData(uid) is not None:
			data = self.mClientSystem.mPlayerManager.getPlayerData(uid).GetPlayerData()
		else:
			data = {
				"nickname" : "名字正在获取中",
				"head_image" : "textures/ui/netease_friend/img01@3x"
			}
		if data is None:
			return {
				"nickname" : "名字正在获取中",
				"head_image" : "textures/ui/netease_friend/img01@3x"
			}
		return data

	def IsFriendNewTalk(self, uid):
		return self.mClientSystem.mChatManager.mIsAnyChatNew.get(uid, False)

	def IsAnyFriendNewTalk(self):
		if True in self.mClientSystem.mChatManager.mIsAnyChatNew.values():
			return True
		else:
			return False

	def IsAnyFriendInvite(self):
		if self.mClientSystem.mFriendManager.mFriendData.GetFriendRequests() is None:
			return False
		elif len(self.mClientSystem.mFriendManager.mFriendData.GetFriendRequests().keys()) > 0:
			return True
		else:
			return False

	def IsFriendOnline(self, uid):
		#return random.choice([True, False])
		state = self.mClientSystem.mFriendManager.mFriendState.get(uid, 1)
		#print "IsFriendOnline", uid, " ", state
		if state == 0:
			return True
		else:
			return False

	def IsPlatformFriend(self, uid):
		#return random.choice([True, False])
		RNFriends = self.mClientSystem.mFriendManager.mFriendData.GetRNFriend()
		if RNFriends and uid in RNFriends:
			return True
		else:
			return False

	def GetLocalPlayerHeadImage(self):
		if self.mClientSystem is None or self.mClientSystem.mMyPlayerUid == 0:
			return "textures/ui/netease_friend/img01@3x"
		else:
			return self.GetPlayerDataByUid(self.mClientSystem.mMyPlayerUid)["head_image"]
	# ---------------------------------------------------------------------------------
	def OnButtonClose(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeScreenVisible(False)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonShowFriend(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ForceShowFriendList()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonShowBlack(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ForceShowBlackList()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
		
	def OnButtonShowTemp(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ForceShowTempList()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonTopHint(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.TryChangeTopHintShow()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonDelFriend(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ShowDelFriendConfirm()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonAddBlack(self, args):
		print "OnButtonAddBlack", args
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ShowAddBlackConfirm()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
		
	def OnButtonAddFriend(self, args):
		print "OnButtonAddFriend", args
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.AddFriendFromTemp()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonInvite(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeScreenVisible(False)
			apiUtil.GetClientModSystem().OpenFriendInvite()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClickPlayerMain(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoChangeSelectPlayer(idx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClickPlayerDelBlack(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-2]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			if self.mShowIngListType == panelType.black:
				self.DoDelPlayerFromBlack(idx)
			elif self.mShowIngListType == panelType.temp:
				self.DoDelPlayerFromTemp(idx)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	# ---------------------------------------------------------------------------------
	def OnButtonSendTalk(self, args):
		print "OnButtonSendTalk", args
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.TrySendTalk()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def TrySendTalk(self):
		self.mTextInput = (self.GetEditText(self.mInputLabelName) or '').strip()
		length = apiUtil.GetTextViewLength(self.mTextInput)
		print "content=%s length=%s" % (self.mTextInput, length)
		if self.mShowIngListType == panelType.black:
			self.ShowTalkWarning("无法和黑名单中的玩家聊天!")
			self.mTextInput = ""
			return
		if not self.mTextInput:
			return
		if not apiUtil.IsWordValidClient(self.mTextInput):
			self.ShowTalkWarning("输入中含有敏感词，无法发送!")
			self.mTextInput = ""
			return
		singleTalk = {
			"fromUid": self.mSelectFriendUid,
			"message": self.mTextInput,
			"chatTime": int(time.time()),
		}
		if self.mShowIngListType == panelType.friend:
			self.mClientSystem.mChatManager.clientChat(self.mSelectFriendUid, self.mTextInput)
			self.mTextInput = ""
			self.SetEditText(self.mInputLabelName, "")
			self.DrawSendButton()
			return
		elif self.mShowIngListType == panelType.temp:
			self.mClientSystem.mChatManager.clientChat(self.mSelectTempUid, self.mTextInput)
			self.mTextInput = ""
			self.SetEditText(self.mInputLabelName, "")
			self.DrawSendButton()
			return
		#self.OnFriendTalkArrive(self.mSelectFriendUid, [singleTalk,])
		self.mTextInput = ""
		self.SetEditText(self.mInputLabelName, "")
		self.DrawSendButton()

	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_box(self, args):
		#print "SearchTextBox  ", args
		#self.mTextInput = args["Text"]
		self.DrawSendButton()
		# self.SetInputEnable(True)
		# if args['Finish'] and args['Mode'] == 'Finished':
		# 	self.SetInputEnable(False)
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_InteractButtonClick)
	def ClearButtonClick(self, args):
		self.mTextInput = ""
		self.DrawSendButton()
		return ViewRequest.Refresh

	# @ViewBinder.binding(ViewBinder.BF_BindString)
	# def ReturnTextString(self):
	# 	return self.mTextInput
	#
	# @ViewBinder.binding(ViewBinder.BF_BindString)
	# def ReturnHolderContent(self):
	# 	return "请输入聊天内容"
	# ---------------------------------------------------------------------------------
	def DoChangeSelectPlayer(self, idx):
		print "DoChangeSelectPlayer", idx
		if self.mShowIngListType == panelType.friend:
			if idx >= len(self.mFriendUidList):
				return
			uid = self.mFriendUidList[idx]["uid"]
			self.ChangeSelectFriend(uid)
		elif self.mShowIngListType == panelType.black:
			if idx >= len(self.mBlackUidList):
				return
			uid = self.mBlackUidList[idx]
			self.ChangeSelectBlack(uid)
		else:
			if idx >= len(self.mTempUidList):
				return
			uid = self.mTempUidList[idx]["uid"]
			self.ChangeSelectTemp(uid)

	def DoDelPlayerFromBlack(self, idx):
		print "DoDelPlayerFromBlack", idx
		if idx >= len(self.mBlackUidList):
			return
		uid = self.mBlackUidList[idx]
		callback = lambda : self.RealDelPlayerFromBlack(uid)
		nickname = self.GetPlayerDataByUid(uid).get("nickname", "")
		text = "是否确定将【%s】移出黑名单？" % nickname
		apiUtil.GetClientModSystem().ShowConfirmPop("移出黑名单", text, callback)

	def RealDelPlayerFromBlack(self, uid):
		self.mClientSystem.mFriendManager.delBlack(uid)
		
	def DoDelPlayerFromTemp(self, idx):
		print "DoDelPlayerFromTemp", idx
		if idx >= len(self.mTempUidList):
			return
		uid = self.mTempUidList[idx]["uid"]
		callback = lambda: self.RealDelPlayerFromTemp(uid)
		nickname = self.GetPlayerDataByUid(uid).get("nickname", "")
		text = "是否确定将【%s】移出临时聊天？" % nickname
		apiUtil.GetClientModSystem().ShowConfirmPop("移出临时聊天", text, callback)
		
	def RealDelPlayerFromTemp(self, uid):
		self.mClientSystem.mFriendManager.delTemp(uid)

	def ForceShowFriendList(self):
		if self.mShowIngListType == panelType.friend:
			return
		self.mShowIngListType = panelType.friend
		self.DrawPanelTop()
		self.DrawTalkPanel()

	def ForceShowBlackList(self):
		if self.mShowIngListType == panelType.black:
			return
		self.mShowIngListType = panelType.black
		self.DrawPanelTop()
		self.DrawTalkPanel()
		
	def ForceShowTempList(self):
		if self.mShowIngListType == panelType.temp:
			return
		self.mShowIngListType = panelType.temp
		self.DrawPanelTop()
		self.DrawTalkPanel()

	def TryChangeTopHintShow(self):
		if self.mShowIngListType == panelType.friend and self.mSelectFriendUid is None:
			return
		if self.mShowIngListType == panelType.temp and self.mSelectTempUid is None:
			return
		self.ChangeFriendHintShow()

	def ShowDelFriendConfirm(self):
		if not self.mSelectFriendUid:
			return
		self.ChangeFriendHintShow(False)
		uid = self.mSelectFriendUid
		callback = lambda: self.RealDelFriend(uid)
		nickname = self.GetPlayerDataByUid(uid).get("nickname", "")
		text = "是否确定删除好友【%s】？" % nickname
		apiUtil.GetClientModSystem().ShowConfirmPop("删除好友", text, callback)
		

	def RealDelFriend(self, uid):
		self.mClientSystem.mFriendManager.deleteFriend(uid)
		print "RealDelFriend", uid

	def ShowAddBlackConfirm(self):
		# if not self.mSelectFriendUid:
		# 	return
		uid = None
		self.ChangeFriendHintShow(False)
		if self.mShowIngListType == panelType.friend:
			uid = self.mSelectFriendUid
		elif self.mShowIngListType == panelType.temp:
			uid = self.mSelectTempUid
		if uid is None:
			return
		callback = lambda: self.RealAddBlack(uid)
		nickname = self.GetPlayerDataByUid(uid).get("nickname", "")
		text = "是否将【%s】移入黑名单？" % nickname
		apiUtil.GetClientModSystem().ShowConfirmPop("加入黑名单", text, callback)

	def RealAddBlack(self, uid):
		self.mClientSystem.mFriendManager.addBlack(uid)
		print "RealAddBlack", uid
		
	def AddFriendFromTemp(self):
		uid = None
		self.ChangeFriendHintShow(False)
		if self.mShowIngListType == panelType.temp:
			uid = self.mSelectTempUid
		if uid is None:
			return
		apiUtil.GetClientModSystem().ShowInviteConfirm(uid)
	# ---------------------------------------------------------------------------------


