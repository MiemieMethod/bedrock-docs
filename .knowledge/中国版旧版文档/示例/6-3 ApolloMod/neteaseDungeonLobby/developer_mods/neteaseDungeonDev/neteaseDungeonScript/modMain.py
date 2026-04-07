# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi
import neteaseDungeonScript.dungeonConsts as dungeonConsts

@Mod.Binding(name=dungeonConsts.ModNameSpace, version=dungeonConsts.ModVersion)
class DungeonServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_DungeonServerMod!==============================='
		self.server = serverApi.RegisterSystem(dungeonConsts.ModNameSpace, dungeonConsts.LobbyServerSystemName,
											dungeonConsts.LobbySystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_DungeonServerMod==============='