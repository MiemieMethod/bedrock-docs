# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
import neteaseTransactionScript.transactionClientConsts as transactionConsts

ClientSystem = clientApi.GetClientSystemCls()

class TransactionClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.ListenEvents()
		self.mTransactionScreenUINode = None
		self.mTransactionHudUINode = None

	def Destroy(self):
		# 引擎事件
		self.UnListenEvents()
		ClientSystem.Destroy(self)

	def ListenEvents(self):
		self.ListenForEvent('neteaseChat', 'neteaseChatBehavior', 'ChatClickExBtnEvent', self, self.OnChatClickExBtn)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.RequestTransactionServerEvent,
							self, self.OnServerRequestTransaction)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.ShowTipsEvent,
							self, self.OnShowTips)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.InitiateTransactionEvent,
							self, self.OnTransactionStart)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.PartnerLockEvent,
							self, self.OnPartnerLocked)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.PartnerConfirmEvent,
							self, self.OnPartnerConfirmed)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.TransactionCompleteEvent,
							self, self.OnTransactionComplete)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.CancelTransactionEvent,
							self, self.OnTransactionCanceled)

	def UnListenEvents(self):
		self.UnListenForEvent('neteaseChat', 'neteaseChatBehavior', 'ChatClickExBtnEvent', self, self.OnChatClickExBtn)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.RequestTransactionServerEvent,
							self, self.OnServerRequestTransaction)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.ShowTipsEvent,
							self, self.OnShowTips)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.InitiateTransactionEvent,
							self, self.OnTransactionStart)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.PartnerLockEvent,
							self, self.OnPartnerLocked)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.PartnerConfirmEvent,
							self, self.OnPartnerConfirmed)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.TransactionCompleteEvent,
							self, self.OnTransactionComplete)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.CancelTransactionEvent,
							self, self.OnTransactionCanceled)

	def OnServerRequestTransaction(self, args):
		self.mTransactionHudUINode.ShowConfirmPanel(args)

	def OnShowTips(self, args):
		msg = args.get("tips", "")
		self.mTransactionHudUINode.ShowTips(msg)

	def OnTransactionStart(self, args):
		print 'OnTransactionStart', args
		self.CreateTransactionScreenUI()
		self.mTransactionScreenUINode.UpdateBagInfo(args)

	def OnPartnerLocked(self, args):
		print 'OnPartnerLocked', args
		if self.mTransactionScreenUINode is None:
			print "Transaction not opened, partner locked failed!"
			return
		self.mTransactionScreenUINode.UpdatePartnerLockedInfo(args)

	def OnPartnerConfirmed(self, args):
		print 'OnPartnerConfirmed', args
		if self.mTransactionScreenUINode is None:
			print "Transaction not opened, partner confirmed failed!"
			return
		self.mTransactionScreenUINode.UpdatePartnerConfirmedInfo()

	def OnUiInitFinished(self, args):
		print "On Transaction UiInitFinished"
		clientApi.RegisterUI(transactionConsts.ModName, "transactionScreenUI", "neteaseTransactionScript.ui.transactionScreenUI.TransactionScreenUI", "transactionScreenUI.main")
		clientApi.RegisterUI(transactionConsts.ModName, "transactionHudUI", "neteaseTransactionScript.ui.transactionHudUI.TransactionHudUI", "transactionHudUI.main")
		self.mTransactionHudUINode = clientApi.CreateUI(transactionConsts.ModName, "transactionHudUI", {"isHud": 1})
		if not self.mTransactionHudUINode:
			print "[Error]Create Transaction Hud UI failed!!!"
		self.mTransactionHudUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.DeskFloat)
		self.mTransactionHudUINode.InitScreen()

	def CreateTransactionScreenUI(self):
		self.mTransactionScreenUINode = clientApi.CreateUI(transactionConsts.ModName, "transactionScreenUI", {"isHud": 1})
		if not self.mTransactionScreenUINode:
			print "[Error]Create transactionScreen UI failed!!!"
		self.mTransactionScreenUINode.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
		self.mTransactionScreenUINode.InitScreen()

	def OnTransactionComplete(self, args):
		print "OnTransactionComplete"
		self.mTransactionScreenUINode.SetRemove()
		self.mTransactionScreenUINode = None
		self.mTransactionHudUINode.ShowTips("交易完成")

	def OnTransactionCanceled(self, args):
		print "OnTransactionCanceled"
		self.mTransactionScreenUINode.SetRemove()
		self.mTransactionScreenUINode = None
		msg = args.get("tips", "交易取消")
		self.mTransactionHudUINode.ShowTips(msg)

	def OnChatClickExBtn(self, args):
		# 聊天插件发起面对面交易
		config = args["cfg"]
		if config.get("key") == "transaction":
			partnerUid = args["friendUid"]
			eventData = {
				"playerId": clientApi.GetLocalPlayerId(),
				"partnerUid": partnerUid
			}
			self.NotifyToServer(transactionConsts.RequestTransactionClientEvent, eventData)