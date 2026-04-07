# -*- coding: utf-8 -*-
from mod_log import engine_logger as logger
import client.extraClientApi as clientApi  # MODSDK提供的库模块
ClientSystem = clientApi.GetClientSystemCls()  # MODSDK提供的客户端基类

from neteaseAddupScript.addupConsts import ModName, ServerSystemName, ClientEvent, ServerEvent
import neteaseAddupScript.addupConsts as addupConsts
import neteaseAddupScript.addupClientPlayer as addupClientPlayer

class AddupClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUid = None
		self.mMe = addupClientPlayer.Player(self.mPlayerId)
		#
		self.mOpenedUI = set()
		self.mBonusUI = None
		self.mGotoButtonText = None
		self.mGotoButtonCallback = None
		#
		self.mActiveAddupKey = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)  # 监听原生UI初始化完毕事件
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnLocalPlayerStopLoading)  # 监听原生UI初始化完毕事件
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.ServerReady, self, self.OnServerReady)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.SyncAddupInfo, self, self.OnSyncAddupInfo)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.UpdateActiveAddup, self, self.OnUpdateActiveAddup)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.GetAddupBonusRet, self, self.OnGetAddupBonusRet)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.OpenBonusUI, self, self.OnOpenBonusUI)

	def Destroy(self):
		self.mBonusUI = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)  # 监听原生UI初始化完毕事件
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnLocalPlayerStopLoading)  # 监听原生UI初始化完毕事件
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.ServerReady, self, self.OnServerReady)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.SyncAddupInfo, self, self.OnSyncAddupInfo)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.UpdateActiveAddup, self, self.OnUpdateActiveAddup)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.GetAddupBonusRet, self, self.OnGetAddupBonusRet)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.OpenBonusUI, self, self.OnOpenBonusUI)

	def OnUiInitFinished(self, args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(ModName, "bonus", "neteaseAddupScript.addupBonusUi.BonusScreen", "netease_addup_consumeUI.main")
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(ModName, "bonus", {"isHud" : 1})
		self.mBonusUI = clientApi.GetUI(ModName, "bonus")
		if self.mBonusUI:
			self.mBonusUI.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
			self.mBonusUI.InitScreen()
			self.mBonusUI.InitSystem(self)
	
	def RegisterUIOpen(self, uiKey):
		self.mOpenedUI.add(uiKey)
		clientApi.SetResponse(False)
		clientApi.SetInputMode(1)

	def RegisterUIClose(self, uiKey):
		self.mOpenedUI.discard(uiKey)
		if not self.mOpenedUI:
			clientApi.SetResponse(True)
			clientApi.SetInputMode(0)

	def OnLocalPlayerStopLoading(self, args):
		self.NotifyToServer(ClientEvent.ClientEnter, {"playerId":self.mPlayerId})

	def OnServerReady(self, data):
		print "OnServerReady"
		self.mUid = data["uid"]
		self.mMe.OnServerReady(data["uid"])
		self.mMe.OnUpdateAddupInfo(data["addupInfo"])
		self.mActiveAddupKey = data["addupKey"]
		# 加载配置
		addupConsts.AllActivityData = data["AllActivityData"]
		# for actKey, data in addupConsts.AllActivityData.iteritems():
		#	print "actkey={}".format(actKey)
		#	for k, v in data.iteritems():
		#		print "{} value is {}".format(k, v)
	
	def OnSyncAddupInfo(self, data):
		self.mActiveAddupKey = data["addupKey"]
		self.mMe.OnUpdateAddupInfo(data["addupInfo"])
		if self.mBonusUI:
			self.mBonusUI.DrawAddupAll()

	def OnUpdateActiveAddup(self, data):
		print "OnUpdateActiveAddup", data
		self.mActiveAddupKey = data["addupKey"]

	def OnGetAddupBonusRet(self, data):
		self.mActiveAddupKey = data["addupKey"]
		self.mMe.OnUpdateAddupInfo(data["addupInfo"])
		if data["suc"] and self.mBonusUI:
			self.mBonusUI.DrawAddupAll()
			self.mBonusUI.ShowGetBonusSuc()
	
	def OnOpenBonusUI(self, data):
		if not self.mActiveAddupKey or not self.mBonusUI:
			return
		print "OnOpenBonusUI", self.mActiveAddupKey
		self.mBonusUI.Show(self.mActiveAddupKey)

	def RegisterGotoButton(self, text, cbFunc):
		self.mGotoButtonText = text
		self.mGotoButtonCallback = cbFunc
		if self.mBonusUI:
			self.mBonusUI.DrawGotoButton()
	
	def GetGotoButtonText(self):
		if self.mGotoButtonText:
			return self.mGotoButtonText
		else:
			return "前往消费"
	
	def GetGotoButtonCallback(self):
		if self.mGotoButtonCallback:
			return self.mGotoButtonCallback
		else:
			return self.OpenNeteaseShop
	
	def OpenNeteaseShop(self):
		self.NotifyToServer(ClientEvent.OpenNeteaseShop, {"playerId":self.mPlayerId,})


		

