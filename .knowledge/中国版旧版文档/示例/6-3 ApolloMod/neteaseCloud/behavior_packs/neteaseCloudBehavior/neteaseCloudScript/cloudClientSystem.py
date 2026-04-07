# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseCloudScript.cloudConsts as cloudConsts

class CloudClientSystem(ClientSystem):
	"""
	该Mod的客户端
	仅通知服务端客户端玩家已进入游戏
	服务端负责同步并还原玩家云端信息
	"""

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print 'Init CloudClientSystem', namespace, systemName
		# 引擎事件
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnCarriedNewItemChangedClientEvent", self, self.OnCarriedNewItemChanged)
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnLocalPlayerStopLoading", self, self.LocalPlayerStopLoading)

	def Destroy(self):
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnCarriedNewItemChangedClientEvent", self, self.OnCarriedNewItemChanged)
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"OnLocalPlayerStopLoading", self, self.LocalPlayerStopLoading)

	def GetLeftHandSlot(self):
		playerId = extraClientApi.GetLocalPlayerId()
		comp = extraClientApi.CreateComponent(playerId, "Minecraft", "item")
		return comp.GetSlotId()

	def OnCarriedNewItemChanged(self, data):
		print 'OnCarriedNewItemChanged', data
		self.SyncRightHandSlot()

	def LocalPlayerStopLoading(self, data):
		# 通知服务端客户端玩家已经就绪
		print "LocalPlayerStopLoading"
		params = {
			'playerId': extraClientApi.GetLocalPlayerId()
		}
		self.NotifyToServer(cloudConsts.LoginCloudServerEvent, params)
		self.SyncRightHandSlot()

	def SyncRightHandSlot(self):
		playerId = extraClientApi.GetLocalPlayerId()
		params = {
			'playerId' : playerId,
			'slot' : self.GetLeftHandSlot()
		}
		self.NotifyToServer(cloudConsts.SyncRightHandSlotEvent, params)