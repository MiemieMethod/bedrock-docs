# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraMasterApi as extraMasterApi
import neteaseDungeonScript.dungeonConsts as dungeonConsts

@Mod.Binding(name=dungeonConsts.ModNameSpace, version=dungeonConsts.ModVersion)
class DungeonMasterMod(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initServer(self):
		print '===========================init_DungeonMasterMod!==============================='
		self.server = extraMasterApi.RegisterSystem(dungeonConsts.ModNameSpace, dungeonConsts.MasterSystemName,
												dungeonConsts.MasterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyServer(self):
		print 'destroy_DungeonMasterMod==============='