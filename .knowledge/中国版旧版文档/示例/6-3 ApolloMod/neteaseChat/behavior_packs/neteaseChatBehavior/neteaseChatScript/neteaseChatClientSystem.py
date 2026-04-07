# -*- coding: utf-8 -*-
import chatConsts as chatConsts
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import neteaseChatScript.ui.uiMgr as uiMgr
import neteaseChatScript.ui.uiDef as uiDef
import chatManager

class ChatClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print namespace, systemName, "====init===="
		self.mClientCacheTime = 200
		self.mMyPlayerUid = 0
		self.mServerid = None
		self.mChatManagers = {}
		self.mCurrentChannel = 0 #当前聊天频道
		#self.mChatManager = chatManager.ChatManager(self)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServerSystemName, "ModConfigResponseFromServerEvent", self, self.OnModConfigResponseFromServerEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServerSystemName, "TellYourPlayerUidAndSidEvent", self, self.OnTellYourPlayerUidAndSidEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServerSystemName, "TellCilentScreenUidsEvent", self, self.OnTellCilentScreenUidsEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServerSystemName, "newChatFromServerEvent", self, self.OnNewChatFromServerEvent)
		self.ListenForEvent(chatConsts.ModNameSpace, chatConsts.ServerSystemName, "OpenChatList", self, self.OnOpenChatList)
		self.mUIMgr = uiMgr.UIMgr()

		self.mExBtnList = None

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()

	def OnOpenChatList(self, args = None):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIChatMain)
		if ui:
			ui.Show(True)

	def OnTellCilentScreenUidsEvent(self, args):
		chatChannel = args.get("chatChannel")
		screenUids = args.get("screenUids")
		if self.mChatManagers.has_key(chatChannel):
			self.mChatManagers[chatChannel].SetScreenUids(screenUids)

	def OnModConfigResponseFromServerEvent(self, modConfig):
		self.modConfig = modConfig

	def OnTellYourPlayerUidAndSidEvent(self, args):
		self.mMyPlayerUid = args.get("playerUid")
		self.mNickName = args.get("nickName")
		self.mServerid = args.get("serverid")
		self.mChatManagers[self.mServerid] = chatManager.ChatManager(self, self.mServerid)
		self.mChatManagers[chatConsts.ALL_SERVER_CHANNEL] = chatManager.ChatManager(self, chatConsts.ALL_SERVER_CHANNEL)
		self.mCurrentChannel = self.mServerid

		exBtnList = args.get('exBtnList')
		if isinstance(exBtnList, list) and exBtnList != self.mExBtnList:
			self.mExBtnList = exBtnList

	def ChangeChannel(self, channel):
		self.mCurrentChannel = channel
		self.BroadcastEvent('LocalChannelChange', {"chatChannel": self.mCurrentChannel})

	def GetNickName(self):
		return self.mNickName

	def GetPlayerCurrentChannel(self):
		return self.mCurrentChannel

	def GetCurrentChannelChatManager(self):
		return self.mChatManagers[self.mCurrentChannel]

	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		# ui = self.mUIMgr.GetUI(uiDef.UIDef.UIChatDesk)
		# if ui:
		# 	ui.ReInit()
		data = self.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		self.NotifyToServer("ClientUiInitFinished", data)
		# self.OnOpenChatList()

	def OnNewChatFromServerEvent(self, chatDict):
		#print "OnNewChatFromServerEvent", chatDict
		#print "self.mChatManagers", self.mChatManagers
		chatChannel = chatDict["chatChannel"]
		if self.mChatManagers.has_key(chatChannel):
			self.mChatManagers[chatChannel].InsertChatMes(chatDict)

	# -------------------------------------------------------------------------------------
	def GetUiMgr(self):
		return self.mUIMgr

	def ShowFullChatPane(self, show):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIChatMain)
		if ui:
			ui.Show(show)

	def ShowSideChatPane(self, show):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIChatMain)
		if ui:
			ui.CtrlSideZone(show)
