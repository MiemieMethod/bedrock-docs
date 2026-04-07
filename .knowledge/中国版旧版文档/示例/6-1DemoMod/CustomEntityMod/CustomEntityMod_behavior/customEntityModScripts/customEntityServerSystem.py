# -*- coding: utf-8 -*-
#
import mod.server.extraServerApi as serverApi

compFactory = serverApi.GetEngineCompFactory()

class CustomEntityServerSystem(serverApi.GetServerSystemCls()):
	def __init__(self, namespace, name):
		super(CustomEntityServerSystem, self).__init__(namespace, name)
		self.DefineEvent("ChangeMaterial")
		self.ListenEvent()


	def ListenEvent(self):
		self.ListenForEvent('customEntityMod', 'customEntityClientSystem', "ShowMsgEvent",
		                    self, self.OnShowMsgEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnAddServerPlayerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
							self, self.OnServerChatEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerAttackEntityEvent",
							self, self.OnPlayerAttackEntityServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerItemUseOnEvent",
							self, self.OnServerItemUseOnEvent)
							
	
	def createEntity(self, playerId):
		comp = compFactory.CreatePos(playerId)
		pos = comp.GetPos()
		pos = (pos[0] + 1, pos[1], pos[2] + 1)
		comp = compFactory.CreateRot(playerId)
		rot = comp.GetRot()
		result = self.CreateEngineEntityByTypeStr("netease:squirrel", pos, rot)

	def OnServerChatEvent(self, args):
		if args['message'] == 'summon':
			# 测试创建自定义生物实体
			self.createEntity(args['playerId'])

	def OnAddServerPlayerEvent(self, args):
		# 玩家进入世界时创建自定义生物
		comp = compFactory.CreateGame(serverApi.GetLevelId())
		comp.AddTimer(3.0, self.createEntity, args['id'])
		
	def OnPlayerAttackEntityServerEvent(self, args):
		# 玩家攻击生物
		playerId = args['playerId']
		victimId = args['victimId']
		self.BroadcastToAllClient("ChangeMaterial", {"entityId": playerId })
		self.BroadcastToAllClient("ChangeMaterial", {"entityId": victimId })
	
	def OnServerItemUseOnEvent(self, args):
		if args["itemName"] in ["minecraft:apple", "minecraft:egg", "minecraft:snowball", "minecraft:diamond", "minecraft:stick"]:
			args["ret"] = True
	
	def OnShowMsgEvent(self, args):
		comp = compFactory.CreateMsg(args["playerId"])
		comp.NotifyOneMessage(args["playerId"], args["msg"])