# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()

from neteaseRoundScript.roundConst import ModName, ServerSampleSystemName, SampleClientEvent, SampleServerEvent
import neteaseRoundScript.roundConst as roundConst

class RoundSampleClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mUid = None
		
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnClientInitFinish)
		self.ListenForEvent(ModName, ServerSampleSystemName, SampleServerEvent.ServerReady, self, self.OnServerReady)
		self.ListenForEvent(ModName, ServerSampleSystemName, SampleServerEvent.SyncConfig, self, self.OnSyncConfig)
		
	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnLocalPlayerStopLoading", self, self.OnClientInitFinish)
		self.UnListenForEvent(ModName, ServerSampleSystemName, SampleServerEvent.ServerReady, self, self.OnServerReady)
		self.UnListenForEvent(ModName, ServerSampleSystemName, SampleServerEvent.SyncConfig, self, self.OnSyncConfig)

	def OnClientInitFinish(self, args):
		self.NotifyToServer(SampleClientEvent.ClientEnter, {"playerId":self.mPlayerId})
	
	def OnServerReady(self, data):
		# print "OnServerReady"
		self.mUid = data["uid"]

	def OnSyncConfig(self, data):
		keyword, identifier = data["keyword"], data["identifier"]
		configDict = roundConst.ConfigAllTypeMap[keyword]
		configDict[identifier] = data["config"]
		# print "OnSyncConfig keyword={} identifier={} config={}".format(keyword, identifier, configDict[identifier])
		


