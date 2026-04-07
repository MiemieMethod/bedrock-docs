# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServiceApi as serviceApi
import simpleScript.simpleConsts as simpleConsts

@Mod.Binding(name=simpleConsts.ModNameSpace, version=simpleConsts.ModVersion)
class SimpleServiceMod(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initServer(self):
		print '===========================init_SimpleServiceMod!==============================='
		self.server = serviceApi.RegisterSystem(simpleConsts.ModNameSpace, simpleConsts.ServiceSystemName,
												simpleConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyServer(self):
		print 'destroy_SimpleServiceMod==============='