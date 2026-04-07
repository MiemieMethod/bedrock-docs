# -*- coding: utf-8 -*-

import neteaseTradeScript.tradeConst as tradeConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class TradeClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mTradeUINode = None
		self.mSaleUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), tradeConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.DisplayGroceryEvent, self, self.OnDisplayGrocery)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerPurchaseEvent, self, self.OnRefreshGrocery)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.UpdatePlayerDoughsEvent, self, self.OnRefreshGrocery)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.DisplayStallEvent, self, self.OnDisplayStall)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerWithdrawMerchEvent, self, self.OnPlayerWithdrawMerch)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerOpenStallEvent, self, self.OnPlayerOpenStall)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnPlayerCloseStall)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.StallSaleUpdateEvent, self, self.OnStallSaleUpdate)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerSpotMerchEvent, self, self.OnPlayerSpotMerch)
		self.ListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.MerchOnSaleEvent, self, self.OnMerchOnSale)

		self.ListenForEvent(tradeConst.ModName, 'bag', 'SyncPlayerInventoryEvent', self, self.OnSyncPlayerInventory)

	def Destroy(self):
		self.mTradeUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), tradeConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.DisplayGroceryEvent, self, self.OnDisplayGrocery)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerPurchaseEvent, self, self.OnRefreshGrocery)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.UpdatePlayerDoughsEvent, self, self.OnRefreshGrocery)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.DisplayStallEvent, self, self.OnDisplayStall)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerWithdrawMerchEvent, self, self.OnPlayerWithdrawMerch)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerOpenStallEvent, self, self.OnPlayerOpenStall)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerCloseStallEvent, self, self.OnPlayerCloseStall)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.StallSaleUpdateEvent, self, self.OnStallSaleUpdate)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.PlayerSpotMerchEvent, self, self.OnPlayerSpotMerch)
		self.UnListenForEvent(tradeConst.ModName, tradeConst.ServerSystemName, tradeConst.MerchOnSaleEvent, self, self.OnMerchOnSale)

		self.UnListenForEvent(tradeConst.ModName, 'bag', 'SyncPlayerInventoryEvent', self, self.OnSyncPlayerInventory)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(tradeConst.ModName, tradeConst.tradeUIName, tradeConst.tradeUIClsPath, tradeConst.tradeUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(tradeConst.ModName, tradeConst.tradeUIName, {"isHud": 1})
		self.mTradeUINode = clientApi.GetUI(tradeConst.ModName, tradeConst.tradeUIName)
		if self.mTradeUINode:
			self.mTradeUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % tradeConst.tradeUIScreenDef
		self.NotifyToServer(tradeConst.QueryPlayerDoughsEvent, {
			'playerId': self.mPlayerId
		})
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(tradeConst.ModName, tradeConst.saleUIName, tradeConst.saleUIClsPath, tradeConst.saleUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(tradeConst.ModName, tradeConst.saleUIName, {"isHud": 1})
		self.mSaleUINode = clientApi.GetUI(tradeConst.ModName, tradeConst.saleUIName)
		if self.mSaleUINode:
			self.mSaleUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % tradeConst.saleUIScreenDef

	def OnDisplayGrocery(self, data):
		print 'OnDisplayGrocery', data
		if self.mTradeUINode:
			self.mTradeUINode.open(data)

	def OnDisplayStall(self, data):
		print 'OnDisplayStall', data
		if self.mSaleUINode:
			self.mSaleUINode.open(data)

	def OnPlayerWithdrawMerch(self, data):
		print 'OnPlayerWithdrawMerch', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(3, data)

	def OnPlayerOpenStall(self, data):
		print 'OnPlayerOpenStall', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(1, data)

	def OnPlayerCloseStall(self, data):
		print 'OnPlayerCloseStall', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(0, data)

	def OnStallSaleUpdate(self, data):
		print 'OnStallSaleUpdate', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(4, data)

	def OnPlayerSpotMerch(self, data):
		print 'OnPlayerSpotMerch', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(5, data)

	def OnMerchOnSale(self, data):
		print 'OnMerchOnSale', data
		if self.mSaleUINode:
			self.mSaleUINode.feedback(data)

	def OnSyncPlayerInventory(self, data):
		print 'OnSyncPlayerInventory', data
		if self.mSaleUINode:
			self.mSaleUINode.refresh(2, data)

	def OnRefreshGrocery(self, data):
		print 'OnRefreshGrocery', data
		if self.mTradeUINode:
			self.mTradeUINode.refresh(data)
