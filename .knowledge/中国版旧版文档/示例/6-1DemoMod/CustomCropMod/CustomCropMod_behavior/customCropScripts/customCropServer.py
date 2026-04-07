# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
import json

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()
'''
该mod同时使用了两种方式自定义农作物：
1）纯配置json的方式，涉及种子：customcrop:custom_wheat_seeds，
   第一阶段方块customcrop:customcrop_stage0，
   第二阶段方块customcrop:customcrop_stage1，
   第三阶段方块customcrop:customcrop_stage2
2）配置json + 脚本的方式，涉及到物品：customcrop:custom_item，
   第一阶段方块customcrop:customcrop_1_stage0，
   第二阶段方块customcrop:customcrop_1_stage1，
   第三阶段方块customcrop:customcrop_1_stage2
'''
class CustomCropServer(serverApi.GetServerSystemCls()):
	def __init__(self, namespace, name):
		super(CustomCropServer, self).__init__(namespace, name)
		self.playerId = None # need to set property
		self.blockNameToStageFunc = {}
		self.ListenEvent()
		self.Init()

	def ListenEvent(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
		                    self, self.OnAddServerPlayerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "BlockRandomTickServerEvent",
		                    self, self.OnBlockRandomTickServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "BlockNeighborChangedServerEvent",
		                    self, self.OnBlockNeighborChangedServerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerItemUseOnEvent",
		                    self, self.OnServerItemUseOnEvent)

	def Init(self):
		self.blockNameToStageFunc["customcrop:customcrop_1_stage0"] = self.OnStage0BlockTick
		self.blockNameToStageFunc["customcrop:customcrop_1_stage1"] = self.OnStage1BlockTick
		# add more stage here...


	def OnAddServerPlayerEvent(self, args):
		self.playerId = args["id"]
		print 'add server player:', self.playerId

	def OnBlockRandomTickServerEvent(self, args):
		# 如果通过脚本的方式实现自定义农作物的话，需要脚本层负责tick count的存档
		print "BlockRandomTickServerEvent:", args
		if args["fullName"] in self.blockNameToStageFunc:
			self.blockNameToStageFunc[args["fullName"]](args)
	
	def OnBlockNeighborChangedServerEvent(self, args):
		print "BlockNeighborChangedServerEvent:", args
		pos = (args['posX'], args['posY'], args['posZ'])
		neighPos = (args['neighborPosX'], args['neighborPosY'], args['neighborPosZ'])
		if (self.IsBelow(pos, neighPos)):
			comp = compFactory.CreateBlockInfo(self.playerId)
			blockDict = comp.GetBlockNew(neighPos)
			if blockDict["name"] == "minecraft:air": # 底下是空气
				blockDict = {
					'name': 'minecraft:air',
					'aux': 0
				}
				comp.SetBlockNew(pos, blockDict)
	
	def OnServerItemUseOnEvent(self, args):
		print "ServerItemUseOnEvent:", args
		if args["itemName"] == "customcrop:custom_item":
			# 使用自定义物品时生成自定义方块
			comp = compFactory.CreateBlockInfo(self.playerId)
			belowPos = (args["x"], args["y"], args["z"]) # below
			blockDict = comp.GetBlockNew(belowPos)
			if blockDict["name"] == "minecraft:dirt": # 底下为沙子才能种植，这里同种子的plant_at判断
				blockDict = {
					'name': 'customcrop:customcrop_1_stage0',
					'aux': 0
				}
				comp.SetBlockNew((args["x"], args["y"] + 1, args["z"]), blockDict)

	def OnStage0BlockTick(self, args):
		pos = (args["posX"], args["posY"], args["posZ"])
		comp = compFactory.CreateBlockInfo(self.playerId)
		lightlevel = comp.GetBlockLightLevel(pos)
		print 'lightlevel:', lightlevel
		if (15 >= lightlevel >= 0): # self define
			dimension = args["dimensionId"]
			blockEntitycomp = compFactory.CreateBlockEntityData(self.playerId)
			blockEntityData = blockEntitycomp.GetBlockEntityData(dimension, pos)
			if not blockEntityData:
				return
			growth = blockEntityData["growth"]
			print 'growth:', growth
			if not growth:
				growth = 0
			growth += 1
			# 使用blockEntity保存tick count数据
			blockEntityData["growth"] = growth
			
			if (growth >= 1): # self define
				comp = compFactory.CreateBlockInfo(self.playerId)  # 此处playerId为block的设置者
				blockDict = {
					'name': 'customcrop:customcrop_1_stage1',
					'aux': 0
				}
				comp.SetBlockNew(pos, blockDict)
	
	def OnStage1BlockTick(self, args):
		pos = (args["posX"], args["posY"], args["posZ"])
		comp = compFactory.CreateBlockInfo(self.playerId)
		lightlevel = comp.GetBlockLightLevel(pos)
		print 'lightlevel:', lightlevel
		if (15 >= lightlevel >= 0): # self define
			dimension = args["dimensionId"]
			pos = (args["posX"], args["posY"], args["posZ"])
			blockEntitycomp = compFactory.CreateBlockEntityData(self.playerId)
			blockEntityData = blockEntitycomp.GetBlockEntityData(dimension, pos)
			if not blockEntityData:
				return

			growth = blockEntityData["growth"]
			print 'growth:', growth
			if not growth:
				growth = 0
			growth += 1
			# 使用blockEntity保存tick count数据
			blockEntityData["growth"] = growth
			
			if (growth > 2): # self define
				comp = compFactory.CreateBlockInfo(self.playerId)  # 此处playerId为block的设置者
				blockDict = {
					'name': 'customcrop:customcrop_1_stage2',
					'aux': 0
				}
				comp.SetBlockNew(pos, blockDict)

	def IsBelow(self, pos, neighPos):
		return pos[0] == neighPos[0] and (pos[1] - 1 == neighPos[1]) and pos[2] == neighPos[2]