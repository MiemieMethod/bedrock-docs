# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class CustomBlocksServer(serverApi.GetServerSystemCls()):
	def __init__(self, namespace, name):
		super(CustomBlocksServer, self).__init__(namespace, name)

		self.ListenEvent()
		self.levelId = serverApi.GetLevelId()

	def ListenEvent(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', 
							self, self.LoadServerAddonScriptsAfter)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
							self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerPlaceBlockEntityEvent',
							self, self.ServerPlaceBlockEntityEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockEntityTickEvent",
							self, self.OnBlockEntityTick)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockUseEvent",
							self, self.ServerBlockUseEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlayerTryDestroyBlockEvent",
							self, self.ServerPlayerTryDestroyBlockEvent)
		
	def LoadServerAddonScriptsAfter(self, args):
		self.RegisterBlockPattern()

	def RegisterBlockPattern(self):
		levelId = serverApi.GetLevelId()
		# 方块组合
		comp = compFactory.CreateBlock(levelId)
		pattern = [
			' # ',
			'XXX',
			' X '
		]
		defines = {
			'#': 'customblocks:customblocks_test_ore',
			'X': 'customblocks:customblocks_test0'
		}
		print 'RegisterBlockPatterns', comp.RegisterBlockPatterns(pattern, defines, 'minecraft:chicken')

	def OnServerChat(self, args):
		playerId = args["playerId"]
		if args["message"] == "overworld":
			comp = compFactory.CreatePos(playerId)
			pos = comp.GetPos()
			comp = compFactory.CreateDimension(playerId)
			comp.ChangePlayerDimension(0, pos)
		elif args["message"] == "dm5":
			comp = compFactory.CreatePos(playerId)
			pos = comp.GetPos()
			comp = compFactory.CreateDimension(playerId)
			comp.ChangePlayerDimension(5, pos)

	def ServerBlockUseEvent(self, args):
		blockName = args['blockName']
		blockPos = (args['x'], args['y'], args['z'])
		playerId = args['playerId']
		dimensionComp = compFactory.CreateDimension(playerId)
		dimension = dimensionComp.GetPlayerDimensionId()
		if blockName == 'customblocks:customblocks_test_block_entity':
			comp = compFactory.CreateBlockEntityData(self.levelId)
			blockEntityData = comp.GetBlockEntityData(dimension, blockPos)
			if blockEntityData:
				blockEntityData['key'] = [1, 2, 3]

	def OnBlockEntityTick(self, args):
		# 避免在Tick中频繁输出，易造成卡顿
		# print 'blockEntityTick ', args
		pass

	def ServerPlaceBlockEntityEvent(self, args):
		print 'ServerPlaceBlockEntityEvent  ', args
		dimension = args['dimension']
		blockPos = (args['posX'], args['posY'], args['posZ'])
		blockName = args['blockName']
		comp = compFactory.CreateBlockEntityData(self.levelId)
		blockEntityData = comp.GetBlockEntityData(dimension, blockPos)
		if blockEntityData:
			blockEntityData['abc'] = {"1": True, "2": None, "3": "123"}

	def ServerPlayerTryDestroyBlockEvent(self, args):
		pos = (args["x"], args["y"], args["z"])
		playerId = args['playerId']
		dimensionComp = compFactory.CreateDimension(playerId)
		dimension = dimensionComp.GetPlayerDimensionId()
		comp = compFactory.CreateBlockEntityData(self.levelId)
		blockEntityData = comp.GetBlockEntityData(dimension, pos)
		if blockEntityData:
			# 根据key获取方块实体中对应的value
			value1 = blockEntityData['key']
			value2 = blockEntityData['abc']
			print 'value of "key" is', value1
			print 'value of "abc" is', value2
