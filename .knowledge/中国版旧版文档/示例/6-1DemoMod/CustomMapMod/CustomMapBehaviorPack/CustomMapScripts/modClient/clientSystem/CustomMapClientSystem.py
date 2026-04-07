# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from CustomMapScripts.modCommon import modConfig
import clientlevel

class CustommapClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mNode = None
		self.playerId = clientApi.GetLocalPlayerId()
		self.mTick = 0
		self.DefineEvent(modConfig.SC_ATTACK_ENTITY_EVENT)
		self.ListenEvent()

	def ListenEvent(self):
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUIInitFinished)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'OnScriptTickClient', self, self.onScriptTick)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'RemoveEntityClientEvent', self, self.RemoveEntityClientEvent)
		self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.SC_ATTACK_ENTITY_EVENT, self, self.OnAttackEntity)

	def OnUIInitFinished(self, args):
		clientApi.RegisterUI(modConfig.ModName, modConfig.UIMiniMapUIName, modConfig.UIMiniMapUIPyClsPath, modConfig.UIMiniMapUIScreenDef)
		self.mNode = clientApi.CreateUI(modConfig.ModName, modConfig.UIMiniMapUIName, {"isHud": 1, "mini_map_root_path": "/mainPanel"})
		self.mNode.AddEntityMarker(self.playerId, "textures/blocks/border", (2,2), True)
		
	def onScriptTick(self):
		self.mTick = self.mTick + 1

	def RemoveEntityClientEvent(self, args):
		if self.mNode:
			self.mNode.RemoveEntityMarker(args["id"])

	def OnAttackEntity(self, args):
		if self.mNode:
			self.mNode.AddEntityMarker(args["victimId"], "textures/blocks/glazed_terracotta_magenta", (2,2), True)
			comp = clientApi.GetEngineCompFactory().CreatePos(args["victimId"])
			pos = comp.GetPos()
			self.mNode.AddStaticMarker(args["victimId"], (pos[0], pos[2]), "textures/blocks/blue_ice", (2,2))
