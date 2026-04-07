# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi
import authConsts as authConsts

@Mod.Binding(name=authConsts.ModNameSpace, version=authConsts.ModVersion)
class AuthServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_AuthServer!==============================='
		self.server = serverApi.RegisterSystem(authConsts.ModNameSpace, authConsts.ServerSystemName, authConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='