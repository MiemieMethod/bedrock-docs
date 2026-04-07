# -*- coding: utf-8 -*-

import client.extraClientApi as extraClientApi

ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseChatScript.chatConsts as chatConsts
import json


def post_json_loads(p_object):
	if isinstance(p_object, dict):
		return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
	elif isinstance(p_object, list):
		return [post_json_loads(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object


class ChatMainScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "ChatMainScreen", namespace, name, param
		#self.mUiKey = UIDef.UIChatDesk
		self.mLocalPlayerId = extraClientApi.GetLocalPlayerId()
		self.mClientSystem = None

		self.mSideChatZoneAlive = True
		self.mSideChat = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/side_chat'
		self.mChatPanel = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel"
		self.mSendButton = self.mChatPanel + "/send_button"
		self.mTabelImg = self.mChatPanel + "/table_img"
		self.mKeyboardButton = self.mChatPanel + "/keyboard_button"
		self.mSettingButton = self.mChatPanel + "/setting_button"
		self.mSendTextBox = self.mChatPanel + "/send_text_box"
		self.mChatBgImage = self.mChatPanel + "/chat_bg_image"
		self.mMenuPanel = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/menu_panel"
		self.mMenuButton0 = self.mMenuPanel + "/menu_button0"
		self.mMenuButton1 = self.mMenuPanel + "/menu_button1"
		self.mMenuButton2 = self.mMenuPanel + "/menu_button2"
		self.mMenuButtons = [self.mMenuButton0, self.mMenuButton1, self.mMenuButton2]
		self.mExBtnListCmp = []
		self.mChatScrollView = self.mChatBgImage + "/chat_scroll_view"
		self.mCloseButton = self.mTabelImg + "/button0"
		self.mClsBtn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel/chat_bg_image/cls_btn'
		self.mClsMainBtn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/main_cls_btn'
		
		self.mChatMessage = ""
		#self.mAllChatRecords = []
		self.mFriendUid = None

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print "ChatMainScreen Create"

		mChatScrollTouch = self.mChatScrollView + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		chatScroll_size = self.GetSize(mChatScrollTouch)
		if chatScroll_size:
			self.mFatherChatPanel = mChatScrollTouch
			self.mFatherChatSize = chatScroll_size

			self.mChannelBar = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel/channel_bg/channel_bar/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
			self.mSideChatZone = self.mSideChat + '/side_chat_scroll_view' + "/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
		else:
			mChatScrollTouch = self.mChatScrollView + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
			chatScroll_size = self.GetSize(mChatScrollTouch)
			self.mFatherChatPanel = mChatScrollTouch
			self.mFatherChatSize = chatScroll_size

			self.mChannelBar = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel/channel_bg/channel_bar/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
			self.mSideChatZone = self.mSideChat + '/side_chat_scroll_view' + "/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"

		self.mSideChatZoneSize = self.GetSize(self.mSideChatZone)
		self.mSideChatLine = self.mSideChatZone + "/one_chat_panel0"
		self.mSideChatLines, self.mSideChatLineItems, self.mSideChatCache = [], [], []

		self.AddTouchEventHandler(self.mClsBtn, self.Cls)
		self.AddTouchEventHandler(self.mClsMainBtn, self.Cls)
		self.AddTouchEventHandler(self.mChannelBar + '/c0', self.C0)
		self.AddTouchEventHandler(self.mChannelBar + '/c1', self.C1)

		self.mMenuBtnPos = self.GetPosition(self.mMenuButton0)
		self.SetVisible(self.mMenuPanel, False)

		self.mOneChatPanel0 = self.mFatherChatPanel + "/one_chat_panel0"
		#self.mOneChatPanel1 = self.mFatherChatPanel + "/one_chat_panel1"
		self.mOneChatPanels = [
			#self.mOneChatPanel1
		]
		self.mOneChatPanel0Pos = self.GetPosition(self.mFatherChatPanel + "/one_chat_hidden")
		self.mD = self.GetSize(self.mOneChatPanel0)[1]
		#print "mOneChatPanel1Posaa", self.mOneChatPanel1Pos
		#self.SetPosition(self.mOneChatPanel1, (self.mOneChatPanel1Pos[0], self.mOneChatPanel1Pos[1]))
		#print "mOneChatPanel1Posbb", self.GetPosition(self.mOneChatPanel1)
		#self.mOneChatPanelItem1 = self.GetRichTextItem(self.mOneChatPanel1)
		self.mOneChatPanelItems = [
			#self.mOneChatPanelItem1
		]
		#self.mOneChatPanelItem1.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
		
		self.AddTouchEventHandler(self.mSendButton, self.OnSendButton)
		self.AddTouchEventHandler(self.mCloseButton, self.OnCloseButton)
		
		for index, menuButton in enumerate(self.mMenuButtons):
			self.AddTouchEventHandler(menuButton, self.OnMenuButton)
		
		#self.TestSetChatPanel()
		self.ChangeScreenVisible(False)
	
	def OnMenuButton(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			menuButtonIndex = self.GetMenuBtnIndex(args["ButtonPath"])
			if menuButtonIndex in xrange(3):
				menuEvent = self.GetMenuEvent(menuButtonIndex)
				eventName = menuEvent["eventName"]
				baseArgs = menuEvent["baseArgs"]
				self.mClientSystem.NotifyToServer(eventName, baseArgs)

				if not menuButtonIndex:
					comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
					comp.AddTimer(0.1, lambda: self.ChangeScreenVisible(False))
			else:
				idx = menuButtonIndex - 3
				self.mClientSystem.BroadcastEvent('ChatClickExBtnEvent', {'idx': idx, 'cfg': self.mExBtnListCmp[idx], 'friendUid': self.mFriendUid})
			self.SetVisible(self.mMenuPanel, False)
			self.SetVisible(self.mClsBtn, False)
			self.SetVisible(self.mClsMainBtn, False)
			
	def GetMenuBtnIndex(self, path):
		# for index, btnPath in enumerate(self.mMenuButtons):
		# 	if btnPath == path:
		# 		return index
		# return -1
		return self.mMenuButtons.index(path)

	def C0(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			if self.mClientSystem.mServerid is not None:
				self.SetVisible(self.mMenuPanel, False)
				self.SetVisible(self.mClsBtn, False)
				self.SetVisible(self.mClsMainBtn, False)
				if self.mClientSystem.GetPlayerCurrentChannel() != 0:
					self.SetSprite(self.mChannelBar + '/c0/default', "textures/ui/netease_chat/btn01_select")
					self.SetSprite(self.mChannelBar + '/c1/default', "textures/ui/netease_chat/btn01")
					self.mClientSystem.ChangeChannel(0)

	def C1(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			if self.mClientSystem.mServerid is not None:
				self.SetVisible(self.mMenuPanel, False)
				self.SetVisible(self.mClsBtn, False)
				self.SetVisible(self.mClsMainBtn, False)
				if self.mClientSystem.GetPlayerCurrentChannel() == 0:
					self.SetSprite(self.mChannelBar + '/c1/default', "textures/ui/netease_chat/btn01_select")
					self.SetSprite(self.mChannelBar + '/c0/default', "textures/ui/netease_chat/btn01")
					self.mClientSystem.ChangeChannel(self.mClientSystem.mServerid)

	def Cls(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchDown:
			self.SetVisible(self.mMenuPanel, False)
			self.SetVisible(self.mClsBtn, False)
			self.SetVisible(self.mClsMainBtn, False)

	def TestSetChatPanel(self):
		self.mOneChatPanelItem = self.GetRichTextItem(self.mOneChatPanel0)
		self.mOneChatPanelItem.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
		self.mOneChatPanelItem.readRichText('§e[lv.15]§r <link>{"text" : "pl", "format_code":"§2"}</link> 说: <link>{"text" : "钻石剑", "format_code":"§2"}</link>')
	
	def OnLocalNewChatRecord(self, args):
		# if self.mIsShow == False:
		# 	return
		if args["chatChannel"] != self.mClientSystem.GetPlayerCurrentChannel():
			return
		chatRecords = self.mClientSystem.GetCurrentChannelChatManager().GetUnReadChatRecords()
		print "OnLocalNewChatRecord", chatRecords
		chatRecordsNum = len(chatRecords)
		# if chatRecordsNum <= 0:
		# 	self.SetVisible(self.mChatScrollView, False)
		# else:
		# self.SetVisible(self.mChatScrollView, True)
		currentOneChatPanelNum = len(self.mSideChatLines if self.mSideChatZoneAlive else self.mOneChatPanels)
		#deltaNum = chatRecordsNum - currentOneChatPanelNum
		if chatRecordsNum > 0:
			for i in xrange(currentOneChatPanelNum + 1, currentOneChatPanelNum + chatRecordsNum + 1):
				if not self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mFatherChatPanel, oneChatPanel)
					self.Clone(self.mOneChatPanel0, self.mFatherChatPanel, oneChatPanel)
					self.SetVisible(oneChatPanelPath, True)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					oneChatPanelItem.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
					self.mOneChatPanelItems.append(oneChatPanelItem)
					self.mOneChatPanels.append(oneChatPanelPath)

				if self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mSideChatZone, oneChatPanel)
					self.Clone(self.mSideChatLine, self.mSideChatZone, oneChatPanel)
					self.SetVisible(oneChatPanelPath, True)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					oneChatPanelItem.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
					self.mSideChatLineItems.append(oneChatPanelItem)
					self.mSideChatLines.append(oneChatPanelPath)
		print "self.mOneChatPanelItems", self.mOneChatPanelItems
		print "self.mOneChatPanels", self.mOneChatPanels

		# yd = 0
		# for i, oneChatPanels in enumerate(self.mOneChatPanels):
		# 	self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + yd))
		# 	if i + 1 != len(self.mOneChatPanels):
		# 		yd += self.GetSize(oneChatPanels)[1]
		# 	else:
		# 		yd = yd, oneChatPanels
		# syd = 0
		# for i, oneChatPanels in enumerate(self.mSideChatLines):
		# 	self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + syd))
		# 	if i + 1 != len(self.mSideChatLines):
		# 		syd += self.GetSize(oneChatPanels)[1]
		# 	else:
		# 		syd = syd, oneChatPanels
		#self.mAllChatRecords = []
		i = currentOneChatPanelNum + 1
		for idx, chatData in enumerate(chatRecords):
			#self.mAllChatRecords.append(chatData)
			#self.mOneChatPanelItems[i].readRichText()
			print "chatData", i
			if not self.mSideChatZoneAlive:
				self.SetChatRichText(self.mOneChatPanelItems[i - 1], chatData)
			if self.mSideChatZoneAlive:
				self.SetChatRichText(self.mSideChatLineItems[i - 1], chatData)
			i = i + 1

		# tyd = yd
		# if yd:
		# 	tyd = yd[0] + self.GetSize(yd[1])[1]
		# tsyd = syd
		# if syd:
		# 	tsyd = syd[0] + self.GetSize(syd[1])[1]
		#
		# height = tyd
		# height = max(height, self.mFatherChatSize[1])
		#
		# loca = int(self.GetScrollViewPos(self.mChatScrollView))
		# if int(height - self.mFatherChatSize[1]) in xrange(loca - 14, loca + int(self.mFatherChatSize[1] / 2.0)):
		# 	comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		# 	comp.AddTimer(0.1, lambda: self.SetScrollViewPercentValue(self.mChatScrollView, 100))
		#
		# self.SetSize(self.mFatherChatPanel, (self.mFatherChatSize[0], height))
		#
		# height = tsyd
		# height = max(height, self.mSideChatZoneSize[1])
		#
		# loca = int(self.GetScrollViewPos(self.mSideChat + '/side_chat_scroll_view'))
		# if int(height - self.mSideChatZoneSize[1]) in xrange(loca - 14, loca + int(self.mSideChatZoneSize[1] / 2.0)):
		# 	comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		# 	comp.AddTimer(0.1, lambda: self.SetScrollViewPercentValue(self.mSideChat + '/side_chat_scroll_view', 100))
		#
		# self.SetSize(self.mSideChatZone, (self.mSideChatZoneSize[0], height))

		def delay_for_draw():
			yd = 0
			if not self.mSideChatZoneAlive:
				for i, oneChatPanels in enumerate(self.mOneChatPanels):
					self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + yd))
					if i + 1 != len(self.mOneChatPanels):
						yd += self.GetSize(oneChatPanels)[1]
					else:
						yd = yd, oneChatPanels
			syd = 0
			if self.mSideChatZoneAlive:
				for i, oneChatPanels in enumerate(self.mSideChatLines):
					self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + syd))
					if i + 1 != len(self.mSideChatLines):
						syd += self.GetSize(oneChatPanels)[1]
					else:
						syd = syd, oneChatPanels

			if yd:
				yd = yd[0] + self.GetSize(yd[1])[1]
			if syd:
				syd = syd[0] + self.GetSize(syd[1])[1]

			if not self.mSideChatZoneAlive:
				self.SetSize(self.mFatherChatPanel, (self.mFatherChatSize[0], yd + 2))
				loca = int(self.GetScrollViewPos(self.mChatScrollView))
				if int(yd - self.mFatherChatSize[1]) in xrange(loca - 14, loca + int(self.mFatherChatSize[1] / 2.0)):
					comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
					comp.AddTimer(0.1, lambda: self.SetScrollViewPercentValue(self.mChatScrollView, 100))

			if self.mSideChatZoneAlive:
				self.SetSize(self.mSideChatZone, (self.mSideChatZoneSize[0], syd + 2))
				loca = int(self.GetScrollViewPos(self.mSideChat + '/side_chat_scroll_view'))
				if int(syd - self.mSideChatZoneSize[1]) in xrange(loca - 14, loca + int(self.mSideChatZoneSize[1] / 2.0)):
					comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
					comp.AddTimer(0.1, lambda: self.SetScrollViewPercentValue(self.mSideChat + '/side_chat_scroll_view', 100))

		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		comp.AddTimer(0.6, delay_for_draw)
		
	def OnLocalChannelChange(self, args):
		# if self.mIsShow == False:
		# 	return
		chatRecords = self.mClientSystem.GetCurrentChannelChatManager().GetAllChatRecords()
		print "OnLocalChannelChange", chatRecords
		allChatRecordsNum = len(chatRecords)
		# if chatRecordsNum <= 0:
		# 	self.SetVisible(self.mChatScrollView, False)
		# else:
		# self.SetVisible(self.mChatScrollView, True)
		currentOneChatPanelNum = len(self.mSideChatLines if self.mSideChatZoneAlive else self.mOneChatPanels)
		deltaNum = allChatRecordsNum - currentOneChatPanelNum
		if deltaNum > 0:
			for i in xrange(currentOneChatPanelNum + 1, allChatRecordsNum + 1):
				if not self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mFatherChatPanel, oneChatPanel)
					self.Clone(self.mOneChatPanel0, self.mFatherChatPanel, oneChatPanel)
					self.SetVisible(oneChatPanelPath, True)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					oneChatPanelItem.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
					self.mOneChatPanelItems.append(oneChatPanelItem)
					self.mOneChatPanels.append(oneChatPanelPath)

				if self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mSideChatZone, oneChatPanel)
					self.Clone(self.mSideChatLine, self.mSideChatZone, oneChatPanel)
					self.SetVisible(oneChatPanelPath, True)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					oneChatPanelItem.registerLinkItemClickCallback(self.OnOneChatPanelItemClickCallback)
					self.mSideChatLineItems.append(oneChatPanelItem)
					self.mSideChatLines.append(oneChatPanelPath)
		else:
			for i in xrange(allChatRecordsNum + 1, currentOneChatPanelNum + 1):
				if not self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mFatherChatPanel, oneChatPanel)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					self.mOneChatPanelItems.remove(oneChatPanelItem)
					self.mOneChatPanels.remove(oneChatPanelPath)
					self.RemoveComponent(oneChatPanelPath, self.mFatherChatPanel)

				if self.mSideChatZoneAlive:
					oneChatPanel = "one_chat_panel%s" % i
					oneChatPanelPath = "%s/%s" % (self.mSideChatZone, oneChatPanel)
					oneChatPanelItem = self.GetRichTextItem(oneChatPanelPath)
					self.mSideChatLineItems.remove(oneChatPanelItem)
					self.mSideChatLines.remove(oneChatPanelPath)
					self.RemoveComponent(oneChatPanelPath, self.mSideChatZone)
		# yd = 0
		# for i, oneChatPanels in enumerate(self.mOneChatPanels):
		# 	self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + yd))
		# 	if i + 1 != len(self.mOneChatPanels):
		# 		yd += self.GetSize(oneChatPanels)[1]
		# 	else:
		# 		yd = yd, oneChatPanels
		# syd = 0
		# for i, oneChatPanels in enumerate(self.mSideChatLines):
		# 	self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + syd))
		# 	if i + 1 != len(self.mSideChatLines):
		# 		syd += self.GetSize(oneChatPanels)[1]
		# 	else:
		# 		syd = syd, oneChatPanels
		# self.mAllChatRecords = []
		i = 0
		for idx, chatData in enumerate(chatRecords):
			# self.mAllChatRecords.append(chatData)
			# self.mOneChatPanelItems[i].readRichText()
			print "chatData", i
			if not self.mSideChatZoneAlive:
				self.SetChatRichText(self.mOneChatPanelItems[i], chatData)
			if self.mSideChatZoneAlive:
				self.SetChatRichText(self.mSideChatLineItems[i], chatData)
			i = i + 1

		def delay_for_draw():
			yd = 0
			if not self.mSideChatZoneAlive:
				for i, oneChatPanels in enumerate(self.mOneChatPanels):
					self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + yd))
					if i + 1 != len(self.mOneChatPanels):
						yd += self.GetSize(oneChatPanels)[1]
					else:
						yd = yd, oneChatPanels
			syd = 0
			if self.mSideChatZoneAlive:
				for i, oneChatPanels in enumerate(self.mSideChatLines):
					self.SetPosition(oneChatPanels, (self.mOneChatPanel0Pos[0], self.mOneChatPanel0Pos[1] + syd))
					if i + 1 != len(self.mSideChatLines):
						syd += self.GetSize(oneChatPanels)[1]
					else:
						syd = syd, oneChatPanels

			if yd:
				yd = yd[0] + self.GetSize(yd[1])[1]
			if syd:
				syd = syd[0] + self.GetSize(syd[1])[1]

			if not self.mSideChatZoneAlive:
				self.SetSize(self.mFatherChatPanel, (self.mFatherChatSize[0], yd + 2))
				comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
				comp.AddTimer(1, lambda: self.SetScrollViewPercentValue(self.mChatScrollView, 100))

			if self.mSideChatZoneAlive:
				self.SetSize(self.mSideChatZone, (self.mSideChatZoneSize[0], syd + 2))
				comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
				comp.AddTimer(1, lambda: self.SetScrollViewPercentValue(self.mSideChat + '/side_chat_scroll_view', 100))

		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		comp.AddTimer(1.6, delay_for_draw)

	def SetChatRichText(self, richItem, chatData):
		playerLevel = chatData["playerLevel"]
		playerUid = chatData["playerUid"]
		nickName = chatData["nickName"]
		#richText = "§e[lv.%s]§r%s 说: "%(str(playerLevel), nickName)
		chatType = chatData["chatType"]
		infoDict = chatData["infoDict"]
		mes = chatData["mes"]
		playerInfoDict = {
			"text": "[%s]" % nickName,
			"playerUid":playerUid,
			"format_code": "§f",
		}
		playerText = "<link>%s</link>" % json.dumps(playerInfoDict)
		if chatType == chatConsts.ChatType.Item:
			# richText = "§e[lv.%s]§r%s 说: " % (str(playerLevel), playerText) + re.sub(r"/\[item ([0-9]{1,2})\]$", '', mes)

			comp = extraClientApi.CreateComponent('', "Minecraft", "item")
			pretty = comp.GetItemFormattedHoverText(
				infoDict['itemName'], infoDict['auxValue'], True, infoDict.get('userData')).split('\n')
			if '' in pretty:
				pretty = pretty[:pretty.index('')]
			name = pretty[0]

			linkDict = {
				"text":"[%s§2]§r" % name,
				"format_code": "§2",
				"chatType":chatType,
				"infoDict":infoDict
			}

			linkText = json.dumps(linkDict)
			linkDict = None
			import re
			richText = "§e[lv.%s]§r%s 说: " % (str(playerLevel), playerText) + re.sub(r"/\[item ([0-9]{1,2})\]", "<link>%s</link>" % linkText.replace('\n', '\\n'), mes)
		elif chatType == chatConsts.ChatType.Common:
			richText = "§e[lv.%s]§r%s 说: " % (str(playerLevel), playerText) + mes
			# linkDict = {
			# 	"text": "%s" % mes,
			# 	"format_code": "§f",
			# 	"chatType": chatType
			# }
			linkDict = None
		elif chatType == chatConsts.ChatType.Team:
			richText = "§e[lv.%s]§r%s 邀请大家一起加入队伍。%s" % (str(playerLevel), playerText, mes)
			linkDict = {
				"text": "【申请入队】",
				"format_code": "§9",
				"chatType": chatType,
				"teamLeaderUid":playerUid
			}
		else:
			return
		if linkDict is not None:
			linkText = json.dumps(linkDict)
			richText += "<link>%s</link>" % linkText
		print "SetChatRichText", richItem, richText
		richItem.readRichText(richText)

	def OnOneChatPanelItemClickCallback(self, data, touchX, touchY):
		if touchY > self.mOneChatPanel0Pos[1] + self.mFatherChatSize[1] / 2.0 - 14:
			touchY /= 2.0

		print("---OnOneChatPanelItemClickCallback---", data, touchX, touchY, type(data))
		if data.has_key("chatType"):
			chatType = data["chatType"]
			if chatType == chatConsts.ChatType.Item:
				infoDict = data["infoDict"]
				infoDict = post_json_loads(infoDict)
				attrsSystem = extraClientApi.GetSystem("neteaseAttrs", "neteaseAttrsBeh")
				if not attrsSystem:
					return

				_system = extraClientApi.GetSystem("neteaseBattle", "neteaseBattleBeh")
				if _system:
					node = extraClientApi.GetUI('neteaseBattle', 'battleUi')
					if node:
						node.ShowDetail(infoDict, touchX, touchY)
						return

				detail = {}
				comp = extraClientApi.CreateComponent('', "Minecraft", "item")
				pretty = comp.GetItemFormattedHoverText(
					infoDict['itemName'], infoDict['auxValue'], True, infoDict.get('userData')).split('\n')
				if '' in pretty:
					pretty = pretty[:pretty.index('')]
				name = pretty[0]
				part = pretty[1]
				enchantData = map(lambda s: '§7{}'.format(s), pretty[2:])

				detail['name'] = name
				detail['pinzhi'] = ('', part)
				if 'durability' in infoDict:
					detail['naijiu'] = ('耐久', str(infoDict['durability']))
				if enchantData:
					detail['fumo'] = enchantData

				attrsSystem.Detail(detail, touchX, touchY)
			elif chatType == chatConsts.ChatType.Team:
				teamLeaderUid = data["teamLeaderUid"]
				self.mClientSystem.NotifyToServer("JoinTeamFromClientEvent", {"teamLeaderUid":teamLeaderUid, "joinTeamPlayerId":self.mLocalPlayerId})
		else:
			#self.mClientSystem.NotifyToServer("JoinTeamFromClientEvent", {"friendUid": data["playerUid"], "selfPlayerId": self.mLocalPlayerId})
			self.mFriendUid = data.get("playerUid")

			if not self.mClientSystem.mMyPlayerUid or self.mFriendUid == self.mClientSystem.mMyPlayerUid:
				return

			exBtnList = self.mClientSystem.mExBtnList
			if exBtnList is not None and exBtnList != self.mExBtnListCmp:
				self.mExBtnListCmp = exBtnList
				demand = len(exBtnList)
				total = len(self.mMenuButtons) - 3
				if demand > total:
					for i in xrange(total, demand):
						i += 3
						s = 'menu_button{}'.format(i)
						self.Clone(self.mMenuButton0, self.mMenuPanel, s)
						self.mMenuButtons.append(self.mMenuPanel + '/{}'.format(s))
						self.SetPosition(
							self.mMenuButtons[-1], (self.mMenuBtnPos[0], self.mMenuBtnPos[1] + 21 * i))
				demand += 3
				for i in xrange(3, len(self.mMenuButtons)):
					b = i < demand
					if b:
						self.SetText(self.mMenuButtons[i] + '/label3', exBtnList[i - 3]['label'])
					self.SetVisible(self.mMenuButtons[i], b)

			self.SetVisible(self.mMenuPanel, True)
			self.SetPosition(self.mMenuPanel, (touchX, touchY))
			self.SetVisible(self.mClsBtn, not self.mSideChatZoneAlive)
			self.SetVisible(self.mClsMainBtn, self.mSideChatZoneAlive)

	def OnSendButton(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			# s = self.mChatMessage.strip()
			s = (self.GetEditText('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel/send_text_box') or '').strip()
			if s:
				currentChannel = self.mClientSystem.GetPlayerCurrentChannel()
				print "OnSendButton", currentChannel
				self.mClientSystem.NotifyToServer("PlayerChatFromClientEvent", {"playerId":self.mLocalPlayerId, "message":s, "chatChannel":currentChannel})
				# self.mChatMessage = ''
				self.SetEditText('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/chat_panel/send_text_box', '')

	
	def OnCloseButton(self, args):
		print "======%s========" % "ClosePanel"
		if args:
			touchEvent = args["TouchEvent"]
			touch_event_enum = extraClientApi.GetMinecraftEnum().TouchEvent
			if touchEvent == touch_event_enum.TouchUp:
				self.ChangeScreenVisible(False)
				self.mClientSystem.BroadcastEvent("ChatUICloseEvent", {})
		else:
			self.ChangeScreenVisible(False)
	
	# @ViewBinder.binding(ViewBinder.BF_BindString)
	# def message_text_box_content(self):
	# 	# print "name_text_box_content", self.mApplicatorName
	# 	return self.mChatMessage
    #
	# @ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	# def message_text_box(self, args):
	# 	#print "message_text_box", args
	# 	self.SetInputEnable(True)
	# 	if args['Finish'] and args['Mode'] == 'Finished':
	# 		self.SetInputEnable(False)
	# 	self.mChatMessage = args["Text"]
	# 	return ViewRequest.Refresh

	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def InitSystem(self, system):
		self.mClientSystem = weakref.proxy(system)
		self.mClientSystem.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'LocalNewChatRecord', self, self.OnLocalNewChatRecord)
		self.mClientSystem.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ClientSystemName, 'LocalChannelChange', self, self.OnLocalChannelChange)

	def Destroy(self):
		pass

	def ChangeScreenVisible(self, flag):
		self.mIsShow = flag
		if flag:
			self.mSideChatZoneAlive = False
			self.SetVisible(self.mSideChat, False)
			self.SetScrollViewPercentValue(self.mChatScrollView, 100)
			extraClientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			self.mSideChatZoneAlive = True
			self.SetVisible(self.mSideChat, True)
			extraClientApi.SetInputMode(0)
			self.SetInputEnable(False)

			comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
			comp.AddTimer(0.2, lambda: self.SetScrollViewPercentValue(self.mChatScrollView, 100))

		def refresh():
			try:
				self.OnLocalChannelChange(None)
			except:
				pass

		comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
		comp.AddTimer(0.1, refresh)
		self.SetVisible(self.mChatPanel, flag)
		
	def Show(self, flag):
		self.ChangeScreenVisible(flag)

	def CtrlSideZone(self, flag):
		if self.mSideChatZoneAlive:
			if flag:
				self.SetVisible(self.mSideChat, True)
				comp = extraClientApi.CreateComponent(extraClientApi.GetLevelId(), "Minecraft", "game")
				comp.AddTimer(0.1, lambda: self.OnLocalChannelChange(None))
				comp.AddTimer(0.2, lambda: self.SetScrollViewPercentValue(self.mChatScrollView, 100))
			else:
				self.SetVisible(self.mSideChat, False)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
	
	def GetMenuEvent(self, menuIdx):
		MenuEvent = {
			0: {"eventName": "TempChatFromClientEvent", "baseArgs": {"entityId":self.mLocalPlayerId, "friendUid":self.mFriendUid}},
			1: {"eventName": "AddFriendFromClientEvent", "baseArgs": {"message": "【%s】请求加你为好友"%self.mClientSystem.GetNickName() ,"entityId":self.mLocalPlayerId, "friendUid":self.mFriendUid}},
			2: {"eventName": "AddBlackFromClientEvent", "baseArgs": {"entityId":self.mLocalPlayerId, "friendUid":self.mFriendUid}}
		}
		return MenuEvent[menuIdx]
		

