# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from neteaseAppearScript.appearConst import ModName, ServerSystemName, ClientEvent, ServerEvent
import neteaseAppearScript.appearConst as appearConst
import neteaseAppearScript.appearClientPlayer as appearClientPlayer
import neteaseAppearScript.appearAvatarManager as appearAvatarManager

class AppearClientSystem(ClientSystem):
	"""
	客户端系统类
	"""
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUid = None
		self.mPlayerData = {}
		self.mMe = appearClientPlayer.PlayerAppear(self.mPlayerId)
		self.mPlayerData[self.mPlayerId] = self.mMe
		self.mAvatarMgr = appearAvatarManager.AppearAvatarManager(self)

		self.mOpenedUI = set()
		self.mShopUI = None
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnClientInitFinish)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.ServerReady, self, self.OnServerReady)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.ChangeUseAppearRet, self, self.OnChangeUseAppearRet)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.BuyAppearRet, self, self.OnBuyAppearRet)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.SyncAppearInfo, self, self.OnSyncAppearInfo)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.UpdateUseAppear, self, self.OnUpdateUseAppear)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.ShowShop, self, self.OnShowShop)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.SyncMoney, self, self.OnSyncMoney)
		
	def Destroy(self):
		if self.mAvatarMgr:
			self.mAvatarMgr.Destroy()
			self.mAvatarMgr = None
		#
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnClientInitFinish)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.ServerReady, self, self.OnServerReady)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.ChangeUseAppearRet, self, self.OnChangeUseAppearRet)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.BuyAppearRet, self, self.OnBuyAppearRet)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.SyncAppearInfo, self, self.OnSyncAppearInfo)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.UpdateUseAppear, self, self.OnUpdateUseAppear)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.ShowShop, self, self.OnShowShop)
		self.UnListenForEvent(ModName, ServerSystemName, ServerEvent.SyncMoney, self, self.OnSyncMoney)

	def GetPlayerByEntityId(self, playerId):
		return self.mPlayerData.get(playerId, None)
	
	def GetModelEntity(self, entityId):
		player = self.mPlayerData.get(entityId, None)
		if player:
			return player, False
		for player in self.mPlayerData.itervalues():
			if player.mMountId == entityId:
				return player, True
		return None, False

	def OnUiInitFinished(self, args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(ModName, "shop", "neteaseAppearScript.appearShopUi.ShopScreen", "netease_appear_shopUI.main")
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(ModName, "shop", {"isHud" : 1})
		self.mShopUI = clientApi.GetUI(ModName, "shop")
		print "mShopUI", self.mShopUI
		if self.mShopUI:
			self.mShopUI.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
			self.mShopUI.InitSystem(self)

	def OnShowShop(self, data):
		print "OnShowShop"
		self.mShopUI.Show(data["moneyData"])
		
	def RegisterUIOpen(self, uiKey):
		self.mOpenedUI.add(uiKey)
		clientApi.SetResponse(False)
		clientApi.SetInputMode(1)

	def RegisterUIClose(self, uiKey):
		self.mOpenedUI.discard(uiKey)
		if not self.mOpenedUI:
			clientApi.SetResponse(True)
			clientApi.SetInputMode(0)

	def OnClientInitFinish(self, args):
		self.NotifyToServer(ClientEvent.ClientEnter, {"playerId":self.mPlayerId})
	
	def OnServerReady(self, data):
		print "OnServerReady"
		self.mUid = data["uid"]
		self.mMe.OnServerReady(data["uid"])
		appearConst.PropModels = data["PropModels"]
		appearConst.PropEffects = data["PropEffects"]
		appearConst.PropAppears = data["PropAppears"]
		appearConst.FreeAppears = data["FreeAppears"]
		appearConst.AllAppearTypes = data["AllAppearTypes"]
		appearConst.EmptyAppearData = data["EmptyAppearData"]
		#
		self.mAvatarMgr.OnServerReady()
		self.mAvatarMgr.OnAddPlayer({"playerId":self.mPlayerId,})
		
	def OnChangeUseAppearRet(self, data):
		print "OnChangeUseAppearRet", data
		if self.mShopUI:
			self.mShopUI.OnChangeUseAppearRet()
	
	def OnBuyAppearRet(self, data):
		print "OnBuyAppearRet", data
		if self.mShopUI:
			self.mShopUI.OnBuyAppearRet()
	
	def OnSyncMoney(self, data):
		print "OnSyncMoney", data
		if self.mShopUI:
			self.mShopUI.OnSyncMoney(data["moneyData"])

	def OnSyncAppearInfo(self, data):
		self.mMe.OnSyncAppearInfo(data["appearInfo"])
		self.mAvatarMgr.OnPlayerDirty(self.mPlayerId)

	def OnUpdateUseAppear(self, data):
		playerId = data["playerId"]
		otherPlayer = self.mPlayerData.get(playerId, None)
		if otherPlayer is None:
			otherPlayer = appearClientPlayer.PlayerAppear(playerId)
			self.mPlayerData[playerId] = otherPlayer
		otherPlayer.OnUpdateUseAppear(data["useData"], data["mountId"])
		self.mAvatarMgr.OnPlayerDirty(playerId)


