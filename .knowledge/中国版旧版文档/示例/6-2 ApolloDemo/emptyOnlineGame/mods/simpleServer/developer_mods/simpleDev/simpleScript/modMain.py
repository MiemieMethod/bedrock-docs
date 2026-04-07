# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi
import simpleScript.simpleConsts as simpleConsts

@Mod.Binding(name=simpleConsts.ModNameSpace, version=simpleConsts.ModVersion)
class SimpleServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_SimpleServerMod!==============================='
		self.server = serverApi.RegisterSystem(simpleConsts.ModNameSpace, simpleConsts.ServerSystemName,
											simpleConsts.GameSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_SimpleServerMod==============='