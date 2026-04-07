# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraMasterApi as extraMasterApi
import simpleScript.simpleConsts as simpleConsts

@Mod.Binding(name=simpleConsts.ModNameSpace, version=simpleConsts.ModVersion)
class SimpleMasterMod(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initServer(self):
		print '===========================init_SimpleMasterMod!==============================='
		self.server = extraMasterApi.RegisterSystem(simpleConsts.ModNameSpace, simpleConsts.MasterSystemName,
												simpleConsts.MasterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyServer(self):
		print 'destroy_SimpleMasterMod==============='