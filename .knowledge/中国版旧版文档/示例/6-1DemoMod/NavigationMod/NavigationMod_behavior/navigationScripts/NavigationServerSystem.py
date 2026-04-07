# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
from mod_log import logger
ServerSystem = serverApi.GetServerSystemCls()

compFactory = serverApi.GetEngineCompFactory()

class NavigationServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenEvent()
		self.playerId = None
		self.entityId = None

	def ListenEvent(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.ServerChatEvent)

	def ServerChatEvent(self, args):
		self.playerId = args['playerId']
		message = args['message']
		identifier = None
		if message == 'walk':
			# 使用minecraft:navigation.walk导航的僵尸示例
			identifier = 'navigationmod:zombie'
		elif message == 'generic':
			# 使用minecraft:navigation.generic导航的溺尸示例
			identifier = 'navigationmod:drowned'
		elif message == 'climb':
			# 使用minecraft:navigation.climb导航的蜘蛛示例
			identifier = 'navigationmod:spider'		
		elif message == 'fly':
			# 使用minecraft:navigation.fly导航的鹦鹉示例
			identifier = 'navigationmod:parrot'
		elif message == 'go':
			# 让上次生成的生物导航到玩家当前位置
			self.MoveEntityToPlayer()
			return
		
		if identifier:
			pos = compFactory.CreatePos(self.playerId).GetFootPos()
			dimId = compFactory.CreateDimension(self.playerId).GetEntityDimensionId()
			self.entityId = self.CreateEngineEntityByTypeStr(identifier, pos, (0,0), dimId)
			logger.info('spawn %s success', identifier)

	def MoveEntityToPlayer(self):
		if self.entityId:
			def myCallback(entityId, result):
				if result in (-1,-2,-3):
					logger.info('[error] [SetMoveSetting] failed: %s', result)
				elif result==0:
					logger.info('[info] [SetMoveSetting] success')
				elif result in (1,2,3):
					logger.info('[warn] [SetMoveSetting] terminated: %s', result)

			pos = compFactory.CreatePos(self.playerId).GetFootPos()
			compFactory.CreateMoveTo(self.entityId).SetMoveSetting(pos, 1.0, 2000, myCallback)
