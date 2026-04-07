# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from CustomMapScripts.modCommon import modConfig

class CustommapServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenEvent()

	def ListenEvent(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.PlayerAttackEntityEvent, self, self.PlayerAttackEntityEvent)

	def PlayerAttackEntityEvent(self, args):
		self.NotifyToClient(args["playerId"], modConfig.SC_ATTACK_ENTITY_EVENT, args)

