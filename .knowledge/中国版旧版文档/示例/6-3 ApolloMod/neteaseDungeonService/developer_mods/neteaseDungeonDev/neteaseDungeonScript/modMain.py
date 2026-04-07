# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServiceApi as serviceApi
import neteaseDungeonScript.dungeonConsts as dungeonConsts

@Mod.Binding(name=dungeonConsts.ModNameSpace, version=dungeonConsts.ModVersion)
class DungeonServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initServer(self):
		print '===========================init_DungeonServerMod!==============================='
		self.server = serviceApi.RegisterSystem(dungeonConsts.ModNameSpace, dungeonConsts.ServiceSystemName,
												dungeonConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyServer(self):
		print 'destroy_DungeonServerMod==============='