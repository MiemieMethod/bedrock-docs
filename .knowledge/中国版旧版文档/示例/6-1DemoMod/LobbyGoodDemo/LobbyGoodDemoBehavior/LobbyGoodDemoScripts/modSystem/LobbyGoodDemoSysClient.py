# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()
compFactory = clientApi.GetEngineCompFactory()

class LobbyGoodDemoClient(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.DefineEvent('RequestbbParticle')
		self.ListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoServer', 'DeliverbbParticle', self, self.OnDeliverbbParticle)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "AddPlayerEvent",
		                    self, self.RequestbbParticle)


	def OnDeliverbbParticle(self, args):
		eid = args['eid']
		# 获取位置 并检查是否存在
		posComp = compFactory.CreatePos(eid)
		if not posComp.GetPos():
			return
		# 创建粒子
		particleEntityId = self.CreateEngineParticle("effects/bb.json", posComp.GetPos())
		# 播放
		ctrlComp = compFactory.CreateParticleControl(particleEntityId)
		ctrlComp.Play()
		#绑定粒子
		bindComp = compFactory.CreateParticleEntityBind(particleEntityId)
		bindComp.Bind(eid, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0))

	def RequestbbParticle(self, args):
		eid = args.get("id")
		if eid:
			checkArgs = self.CreateEventData()
			checkArgs['from'] = clientApi.GetLocalPlayerId()
			checkArgs['eid'] = eid
			self.NotifyToServer("RequestbbParticle", checkArgs)

	def Update(self):
		pass


	def Destroy(self):
		self.UnListenForEvent('LobbyGoodDemo', 'LobbyGoodDemoServer', 'DeliverbbParticle', self, self.OnDeliverbbParticle)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "AddPlayerEvent",
		                    self, self.RequestbbParticle)











