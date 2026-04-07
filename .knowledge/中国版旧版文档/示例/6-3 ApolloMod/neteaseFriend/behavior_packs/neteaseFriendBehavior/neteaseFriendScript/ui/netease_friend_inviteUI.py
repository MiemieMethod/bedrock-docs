# -*- coding: utf-8 -*-
import random
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseFriendScript.apiUtil as apiUtil
import neteaseFriendScript.friendConsts as friendConsts
from neteaseFriendScript.ui.uiDef import UIDef
import weakref

PageNearList = "PageNearList"
PageFindList = "PageFindList"
PageInviteList = "PageInviteList"

ScrollPartLong = "ScrollPartLong"
ScrollPartSmall = "ScrollPartSmall"

class FriendInviteScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIFriendInvite
		self.mTextInput = ""
		self.mRecentPage = PageInviteList
		self.mRecentPlayerList = []
		self.mUidInProcess = {}
		self.mNearUidList = []
		self.mFindUidList = []
		self.mInviteUidList = []

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIClose(self.mUiKey)
			self.SetInputEnable(False)
		self.SetVisible("", flag)

	def InitScreen(self):
		self.ChangeScreenVisible(False)
		
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalUpdatePlayerData', self, self.OnLocalUpdatePlayerData)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalSearchFriendChangeEvent', self, self.OnLocalSearchFriendChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalSearchAroundChangeEvent', self, self.OnLocalSearchAroundChangeEvent)
		self.mClientSystem.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                                  'LocalFriendRequestChangeEvent', self, self.OnLocalFriendRequestChangeEvent)
		
	def OnLocalUpdatePlayerData(self, args):
		print "OnLocalUpdatePlayerData"
		#self.ReDrawAll()
		uid = args.get("uid")
		self.ReDrawOnePlayerData(uid)
	
	def OnLocalFriendRequestChangeEvent(self, args):
		print "OnLocalFriendRequestChangeEvent"
		self.ReDrawAll()
		
	def OnLocalSearchFriendChangeEvent(self, args):
		if len(args.get("mSearchFriendUid"))>0:
			self.ReDrawAll()
	
	def OnLocalSearchAroundChangeEvent(self, args):
		if len(args.get("mAroundFriendUid")) > 0:
			self.ReDrawAll()
		
	def ReDrawOnePlayerData(self, uid):
		if uid not in self.mRecentPlayerList:
			return
		idx = self.mRecentPlayerList.index(uid)
		now = int(time.time())
		
		if self.mRecentPage in (PageNearList, PageInviteList):
			sType = ScrollPartLong
		else:
			sType = ScrollPartSmall
		singlePart = self.mScrollPartMap[sType][idx]
		friendData = self.GetPlayerDataByUid(uid)
		if sType == ScrollPartLong:
			self.SetText("%s/lb_apply_name" % singlePart, friendData["nickname"])
			self.SetSprite("%s/img_apply_head" % singlePart, friendData["head_image"])
		else:
			self.SetText("%s/lb_search_name" % singlePart, friendData["nickname"])
			self.SetSprite("%s/img_search_head" % singlePart, friendData["head_image"])
		self.DrawSinglePlayerState(uid, singlePart, now)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		# 关闭按钮
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_invite/btn_close", self.OnButtonClose)
		# 玩家列表
		self.mScrollInfoMap = {}
		self.mScrollPartMap = {}
		# 玩家列表（长）
		scrollInfo = {}
		scrollBase = "/main_pnl/pnl_invite/img_base_invite/scroll_nearby"
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
		scrollInfo["base"] = scrollInfo["parent"] + "/pnl_apply_base"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["base_offset"] = 2
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mScrollPartMap[ScrollPartLong] = []
		self.mScrollInfoMap[ScrollPartLong] = scrollInfo
		self.PlayerListResize(ScrollPartLong, 0)
		# 玩家列表（短）
		scrollInfo = {}
		scrollBase = "/main_pnl/pnl_invite/img_base_invite/scroll_nearby_small"
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
		scrollInfo["base"] = scrollInfo["parent"] + "/pnl_search_base"
		scrollInfo["base_size"] = self.GetSize(scrollInfo["base"])
		scrollInfo["base_pos"] = self.GetPosition(scrollInfo["base"])
		scrollInfo["base_offset"] = 2
		scrollInfo["size"] = 0
		self.SetVisible(scrollInfo["base"], False)
		self.mScrollPartMap[ScrollPartSmall] = []
		self.mScrollInfoMap[ScrollPartSmall] = scrollInfo
		self.PlayerListResize(ScrollPartSmall, 0)
		# 左侧分页按钮
		self.SetTouchEnable("/main_pnl/tab_left_list", True)
		self.mNewTagFriend = "/main_pnl/tab_left_list/img_tag_list"
		self.SetVisible(self.mNewTagFriend, False)
		self.AddTouchEventHandler("/main_pnl/tab_left_list", self.OnButtonFriendList)
		self.SetTouchEnable("/main_pnl/tab_left_invite", False)
		self.mNewTagInvite = "/main_pnl/tab_left_invite/img_tag_invite"
		self.SetVisible(self.mNewTagInvite, False)
		# 上方分页按钮、弹出菜单按钮
		self.mUpperTabButtons = {
			PageNearList: "/main_pnl/pnl_invite/img_base_invite/btn_upper_nearby",
			PageFindList: "/main_pnl/pnl_invite/img_base_invite/btn_upper_search",
			PageInviteList: "/main_pnl/pnl_invite/img_base_invite/btn_upper_apply",
		}
		self.SetTouchEnable(self.mUpperTabButtons[PageNearList], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[PageNearList], self.OnButtonShowNear)
		self.SetTouchEnable(self.mUpperTabButtons[PageFindList], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[PageFindList], self.OnButtonShowFind)
		self.SetTouchEnable(self.mUpperTabButtons[PageInviteList], True)
		self.AddTouchEventHandler(self.mUpperTabButtons[PageInviteList], self.OnButtonShowInvite)
		#
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_invite/btn_search", True)
		self.AddTouchEventHandler("/main_pnl/pnl_invite/img_base_invite/btn_search", self.OnButtonSendFind)

	def PlayerListResize(self, stype, size):
		scrollInfo = self.mScrollInfoMap[stype]
		if size == scrollInfo["size"]:
			return
		scrollPartList = self.mScrollPartMap[stype]
		scrollInfo["size"] = size
		lackNum = size - len(scrollPartList)
		# 控件不够用，创建一些
		if lackNum > 0:
			beginIndex = len(scrollPartList)
			for idx in xrange(lackNum):
				self.CloneSinglePlayer(stype, beginIndex + idx, scrollInfo)
		# 隐藏多余不用的控件
		for idx, part in enumerate(scrollPartList):
			if idx < size:
				self.SetVisible(part, True)
			else:
				self.SetVisible(part, False)
		# 重设滚动区域的大小
		height = scrollInfo["base_pos"][1] + size * (scrollInfo["base_size"][1] + scrollInfo["base_offset"])
		height = max(height, scrollInfo["parent_size"][1])
		self.SetSize(scrollInfo["parent"], (scrollInfo["parent_size"][0], height))

	def CloneSinglePlayer(self, stype, idx, scrollInfo):
		name = "single_player_%d" % idx
		self.Clone(scrollInfo["base"], scrollInfo["parent"], name)
		fullName = "%s/%s" % (scrollInfo["parent"], name)
		self.mScrollPartMap[stype].append(fullName)
		height = scrollInfo["base_pos"][1] + idx * (scrollInfo["base_size"][1] + scrollInfo["base_offset"])
		self.SetPosition(fullName, (scrollInfo["base_pos"][0], height))
		#
		if stype == ScrollPartLong:
			self.SetTouchEnable("%s/btn_apply_add" % fullName, True)
			self.AddTouchEventHandler("%s/btn_apply_add" % fullName, self.OnClickInvitePlayer)
			self.SetTouchEnable("%s/btn_apply_refuse" % fullName, True)
			self.AddTouchEventHandler("%s/btn_apply_refuse" % fullName, self.OnClickRefuseInvite)
			self.SetTouchEnable("%s/btn_apply_accept" % fullName, True)
			self.AddTouchEventHandler("%s/btn_apply_accept" % fullName, self.OnClickAcceptInvite)
		else:
			self.SetTouchEnable("%s/btn_search_add" % fullName, True)
			self.AddTouchEventHandler("%s/btn_search_add" % fullName, self.OnClickInvitePlayer)
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
		for pType in (PageNearList, PageFindList, PageInviteList):
			if self.mRecentPage == pType:
				apiUtil.DrawButtonImage(self, self.mUpperTabButtons[pType], "btn04_select@3x")
			else:
				apiUtil.DrawButtonImage(self, self.mUpperTabButtons[pType], "btn04@3x")
		if self.mRecentPage == PageNearList:
			self.mRecentPlayerList = self.GetNearUidList()
			self.DrawInput(False)
			sType = ScrollPartLong
		elif self.mRecentPage == PageFindList:
			self.mRecentPlayerList = self.GetFindUidList()
			self.DrawInput(True)
			sType = ScrollPartSmall
		else:
			self.mRecentPlayerList = self.GetInviteUidList()
			self.DrawInviteHint(False)
			self.DrawInput(False)
			sType = ScrollPartLong
		if sType == ScrollPartLong:
			self.SetVisible("/main_pnl/pnl_invite/img_base_invite/scroll_nearby", True)
			self.SetVisible("/main_pnl/pnl_invite/img_base_invite/scroll_nearby_small", False)
		else:
			self.SetVisible("/main_pnl/pnl_invite/img_base_invite/scroll_nearby", False)
			self.SetVisible("/main_pnl/pnl_invite/img_base_invite/scroll_nearby_small", True)
		self.DrawPlayerList(sType)
		if self.IsAnyFriendInvite():
			self.SetVisible(self.mNewTagInvite, True)
		else:
			self.SetVisible(self.mNewTagInvite, False)

	def DrawPlayerList(self, sType):
		size = len(self.mRecentPlayerList)
		self.PlayerListResize(sType, size)
		now = int(time.time())
		for idx, uid in enumerate(self.mRecentPlayerList):
			singlePart = self.mScrollPartMap[sType][idx]
			friendData = self.GetPlayerDataByUid(uid)
			if sType == ScrollPartLong:
				self.SetText("%s/lb_apply_name" % singlePart, friendData["nickname"])
				self.SetSprite("%s/img_apply_head" % singlePart, friendData["head_image"])
			else:
				self.SetText("%s/lb_search_name" % singlePart, friendData["nickname"])
				self.SetSprite("%s/img_search_head" % singlePart, friendData["head_image"])
			self.DrawSinglePlayerState(uid, singlePart, now)

	def DrawSinglePlayerState(self, uid, singlePart, now=None):
		if now is None:
			now = int(time.time())
		hint = self.GetInProcessHintByUid(uid, self.mRecentPage, now)
		if self.mRecentPage == PageNearList:
			self.SetText("%s/lb_apply_notice" % singlePart, "")
			if hint:
				self.SetVisible("%s/btn_apply_refuse" % singlePart, False)
				self.SetVisible("%s/btn_apply_accept" % singlePart, False)
				self.SetVisible("%s/btn_apply_add" % singlePart, False)
				self.SetText("%s/lb_apply_state" % singlePart, hint)
			else:
				self.SetVisible("%s/btn_apply_refuse" % singlePart, False)
				self.SetVisible("%s/btn_apply_accept" % singlePart, False)
				self.SetVisible("%s/btn_apply_add" % singlePart, True)
				self.SetText("%s/lb_apply_state" % singlePart, "")
		elif self.mRecentPage == PageFindList:
			if hint:
				self.SetVisible("%s/btn_search_add" % singlePart, False)
				self.SetText("%s/lb_search_state" % singlePart, hint)
			else:
				self.SetVisible("%s/btn_search_add" % singlePart, True)
				self.SetText("%s/lb_search_state" % singlePart, "")
		else:
			if hint:
				self.SetVisible("%s/btn_apply_refuse" % singlePart, False)
				self.SetVisible("%s/btn_apply_accept" % singlePart, False)
				self.SetVisible("%s/btn_apply_add" % singlePart, False)
				self.SetText("%s/lb_apply_state" % singlePart, hint)
				self.SetText("%s/lb_apply_notice" % singlePart, "")
			else:
				self.SetVisible("%s/btn_apply_refuse" % singlePart, True)
				self.SetVisible("%s/btn_apply_accept" % singlePart, True)
				self.SetVisible("%s/btn_apply_add" % singlePart, False)
				self.SetText("%s/lb_apply_state" % singlePart, "")
				text = self.GetInviteWordByUid(uid)
				self.SetText("%s/lb_apply_notice" % singlePart, text)

	def DrawInviteHint(self, isShow):
		self.SetVisible("/main_pnl/pnl_invite/img_base_invite/btn_search/lb_noResults", isShow)

	def DrawInput(self, isShow):
		self.SetVisible("/main_pnl/pnl_invite/img_base_invite/btn_search", isShow)
		self.SetVisible("/main_pnl/pnl_invite/img_base_invite/text_edit_box", isShow)
			
	def DrawFindButton(self, enable=None):
		text = self.GetEditText("/main_pnl/pnl_invite/img_base_invite/text_edit_box")
		if not text:
			text = ""
		self.mTextInput = text.strip()
		if enable is None:
			if self.mTextInput:
				enable = True
			else:
				enable = False
		self.SetTouchEnable("/main_pnl/pnl_invite/img_base_invite/btn_search", enable)
		if enable:
			apiUtil.DrawButtonImage(self, "/main_pnl/pnl_invite/img_base_invite/btn_search", "btn01@3x")
		else:
			apiUtil.DrawButtonImage(self, "/main_pnl/pnl_invite/img_base_invite/btn_search", "btn01_select@3x")
	# ---------------------------------------------------------------------------------
	def Show(self):
		self.ChangeScreenVisible(True)
		self.ReDrawAll()

	def ReDrawAll(self):
		self.DrawPanelLeft()
		self.DrawPanelTop()
		self.DrawFindButton()
	# ---------------------------------------------------------------------------------
	def GetInProcessHintByUid(self, uid, page, now):
		if self.IsAlreadyFriend(uid):
			return "已加为好友"
		if self.IsYou(uid):
			return "这个是你"
		data = self.mUidInProcess.get((page, uid), None)
		if not data:
			return ""
		timestamp, hint = data
		if now - timestamp > self.mClientSystem.mClientCacheTime:
			return ""
		return hint

	def SaveInProcessHint(self, hint, uid, page, now=None):
		if now is None:
			now = int(time.time())
		self.mUidInProcess[(page, uid)] = (now, hint)
	# ---------------------------------------------------------------------------------
	def GetNearUidList(self):
		# if self.mNearUidList:
		# 	return self.mNearUidList
		# self.mNearUidList = []
		# for i in xrange(random.randint(3, 40)):
		# 	self.mNearUidList.append(1000*i + random.randint(1000, 1999))
		# return self.mNearUidList
		return self.mClientSystem.mFriendManager.mAroundFriendUid

	def GetFindUidList(self):
		# if self.mFindUidList:
		# 	return self.mFindUidList
		# self.mFindUidList = []
		# for i in xrange(random.randint(3, 40)):
		# 	self.mFindUidList.append(1000 * i + random.randint(1000, 1999))
		# return self.mFindUidList
		return self.mClientSystem.mFriendManager.mSearchFriendUid

	def GetInviteUidList(self):
		# if self.mInviteUidList:
		# 	return self.mInviteUidList
		# self.mInviteUidList = []
		# for i in xrange(random.randint(3, 40)):
		# 	self.mInviteUidList.append(1000 * i + random.randint(1000, 1999))
		# return self.mInviteUidList
		if self.mClientSystem.mFriendManager.mFriendData.GetFriendRequests() is None:
			return []
		else:
			return self.mClientSystem.mFriendManager.mFriendData.GetFriendRequests().keys()

	def GetInviteWordByUid(self, uid):
		return self.mClientSystem.mFriendManager.mFriendData.GetFriendRequests().get(uid).get("message")
		#return "我是申请加好友的附言"

	def IsAlreadyFriend(self, uid):
		temp_friend_list = self.mClientSystem.mFriendManager.mFriendData.GetFriends()
		if temp_friend_list and uid in temp_friend_list:
			return True
		return False
	
	def IsYou(self, uid):
		return self.mClientSystem.mMyPlayerUid == uid

	def GetPlayerDataByUid(self, uid):
		if self.mClientSystem.mPlayerManager.getPlayerData(uid) is not None:
			data = self.mClientSystem.mPlayerManager.getPlayerData(uid).GetPlayerData()
		else:
			data = {
				"nickname": "名字正在获取中",
				"head_image": "textures/ui/netease_friend/img01@3x"
			}
		if data is None:
			return {
				"nickname": "名字正在获取中",
				"head_image": "textures/ui/netease_friend/img01@3x"
			}
		return data

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

	def OnButtonShowNear(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeRecentPage(PageNearList)
			self.mClientSystem.mFriendManager.searchNear()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonShowInvite(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeRecentPage(PageInviteList)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonShowFind(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeRecentPage(PageFindList)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonFriendList(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeScreenVisible(False)
			apiUtil.GetClientModSystem().OpenFriendList()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClickInvitePlayer(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-2]
		line = line.split("_")
		idx = int(line[-1])
		if idx >= len(self.mRecentPlayerList):
			return
		uid = self.mRecentPlayerList[idx]
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ShowInviteConfirm(uid)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClickRefuseInvite(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-2]
		line = line.split("_")
		idx = int(line[-1])
		if idx >= len(self.mRecentPlayerList):
			return
		uid = self.mRecentPlayerList[idx]
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.RefuseInvite(uid)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnClickAcceptInvite(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-2]
		line = line.split("_")
		idx = int(line[-1])
		if idx >= len(self.mRecentPlayerList):
			return
		uid = self.mRecentPlayerList[idx]
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.AcceptInvite(uid)
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	# ---------------------------------------------------------------------------------
	def OnButtonSendFind(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.TrySendFind()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def TrySendFind(self):
		if not self.mTextInput:
			return
		#self.mTextInput = ""
		self.mClientSystem.mFriendManager.searchFriend(self.mTextInput)

	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_box(self, args):
		# print "SearchTextBox  ", args
		self.mTextInput = args["Text"]
		self.DrawFindButton()
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_InteractButtonClick)
	def ClearButtonClick(self, args):
		self.mTextInput = ""
		self.DrawFindButton()
		return ViewRequest.Refresh
	# ---------------------------------------------------------------------------------
	def ChangeRecentPage(self, page):
		if page == self.mRecentPage:
			return
		self.mRecentPage = page
		self.DrawPanelTop()

	def ShowInviteConfirm(self, uid):
		callback = lambda text: self.RealInvite(uid, self.mRecentPage, text)
		nickname = self.GetPlayerDataByUid(uid).get("nickname", "")
		myName = "查内姆"
		apiUtil.GetClientModSystem().ShowInvitePop(myName, nickname, callback)

	def RealInvite(self, uid, page, text):
		print "RealInvite", uid, page, text
		self.SaveInProcessHint("已发送加好友申请", uid, page)
		self.DrawPanelTop()
		self.mClientSystem.mFriendManager.addFriend(uid, text)

	def RefuseInvite(self, uid):
		self.SaveInProcessHint("已拒绝", uid, self.mRecentPage)
		self.DrawPanelTop()
		self.mClientSystem.mFriendManager.refuseFriend(uid)

	def AcceptInvite(self, uid):
		self.SaveInProcessHint("已发送同意申请", uid, self.mRecentPage)
		self.DrawPanelTop()
		self.mClientSystem.mFriendManager.acceptFriend(uid)
	# ---------------------------------------------------------------------------------


