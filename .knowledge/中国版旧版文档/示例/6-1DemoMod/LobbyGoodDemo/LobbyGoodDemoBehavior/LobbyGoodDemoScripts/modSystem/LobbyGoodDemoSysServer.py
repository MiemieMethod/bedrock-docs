# -*- coding: utf-8 -*-
#
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class LobbyGoodDemoServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)

		self.DefineEvent('DeliverbbParticle')
		self.ListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoClient', 'RequestbbParticle', self, self.OnRequestbbParticle)

		self.mDeliveredOwner = set()

	def CheckbbParticle(self, eid):
		return eid in self.mDeliveredOwner

	def OnRequestbbParticle(self, args):
		eid = args['eid']
		if self.CheckbbParticle(eid):
			deliverArgs = self.CreateEventData()
			deliverArgs['eid'] = eid
			self.NotifyToClient(args['from'], 'DeliverbbParticle', deliverArgs)

	def Update(self):
		pass

	def Deliver(self, entityId):
		deliverArgs = self.CreateEventData()
		deliverArgs['eid'] = entityId
		self.BroadcastToAllClient("DeliverbbParticle", deliverArgs)
		self.mDeliveredOwner.add(entityId)


	def Destroy(self):
		self.UnListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoClient', 'RequestbbParticle', self, self.OnRequestbbParticle)
