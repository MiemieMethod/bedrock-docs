import friendConsts as friendConsts
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import neteaseFriendScript.apiUtil as apiUtil
import neteaseFriendScript.ui.uiMgr as uiMgr
import neteaseFriendScript.ui.uiDef as uiDef
import friendManager
import chatManager
import playerManager

class FriendClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		
		self.mClientCacheTime = 200
		self.mMyPlayerUid = 0
		
		self.mFriendManager = friendManager.FriendManager(self)
		self.mChatManager = chatManager.ChatManager(self)
		self.mPlayerManager = playerManager.PlayerManager(self)
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), friendConsts.UiInitFinished, self, self.OnUiInitFinished)
		self.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, "ModConfigResponseFromServerEvent", self, self.OnModConfigResponseFromServerEvent)
		self.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, "TellYourPlayerUidEvent", self, self.OnTellYourPlayerUidEvent)
		self.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, "OpenFriendList", self, self.OnOpenFriendList)
		self.mUIMgr = uiMgr.UIMgr()

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), friendConsts.UiInitFinished, self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()
		apiUtil.Destroy()
		
	def OnModConfigResponseFromServerEvent(self, modConfig):
		self.modConfig = modConfig
		self.mChatManager.RECORD_MAX_NUM = modConfig.get("RECORD_MAX_NUM")
		self.mChatManager.RECORD_MAX_LENGTH = modConfig.get("RECORD_MAX_LENGTH")
		self.mFriendManager.FRIENDS_MAX_NUM = modConfig.get("FRIENDS_MAX_NUM")
		self.mFriendManager.TEMP_MAX_NUM = modConfig.get("TEMP_MAX_NUM")
		self.mClientCacheTime = modConfig.get("CLIENT_CACHE_TIME")
		
	def OnTellYourPlayerUidEvent(self, args):
		self.mMyPlayerUid = args.get("playerUid")
		self.BroadcastEvent('LocalLoadYourPlayerData', {})
		
	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		# ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendDesk)
		# if ui:
		# 	ui.ReInit()
		data = self.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		self.NotifyToServer("ClientUiInitFinished", data)
		self.mFriendManager.Init()

	# -------------------------------------------------------------------------------------
	def OnOpenFriendList(self, args):
		self.OpenFriendList(args)
	
	def OpenFriendList(self, args = None):
		print "OpenFriendList", args
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendList)
		if ui:
			ui.Show()
			if args:
				if args.get("openTemp") == True:
					timer = None
					timerComp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
					def openTempList():
						#print "openTempList1"
						#ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendList)
						if args["uid"] in ui.ori_temp_uid_list:
							#print "openTempList2", args["uid"] , ui.ori_temp_uid_list
							ui.ForceShowTempList()
							ui.ChangeSelectTemp(args["uid"])
							if timer is not None:
								timerComp.CancelTimer(timer)
					timer = timerComp.AddRepeatedTimer(0.5, openTempList)
				else:
					ui.ForceShowFriendList()
					ui.ChangeSelectFriend(args["uid"])
				return

	def OpenFriendInvite(self):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendInvite)
		if ui:
			ui.Show()
	
	def GetFriendListUIisShow(self):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendList)
		if ui:
			return ui.GetIsShow()
		else:
			return False

	def ShowConfirmPop(self, title, desc, okCallback=None, cancelCallback=None):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendConfirmPop)
		if ui:
			ui.ShowConfirmPop(title, desc, okCallback, cancelCallback)

	def ShowInvitePop(self, name, friendName, okCallback=None, cancelCallback=None):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendInvitePop)
		if ui:
			ui.ShowInvitePop(name, friendName, okCallback, cancelCallback)
			
	def ShowInviteConfirm(self, uid):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFriendInvite)
		if ui:
			ui.ShowInviteConfirm(uid)
	# -------------------------------------------------------------------------------------
	def GetUiMgr(self):
		return self.mUIMgr
		
		
