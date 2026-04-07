# -*- coding: utf-8 -*-
#
from common.mod import Mod
import authConsts as authConsts

@Mod.Binding(name=authConsts.ModNameSpace, version=authConsts.ModVersion)
class AuthMasterMod(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initMaster(self):
		print '===========================init_AuthMaster!==============================='
		import server.extraMasterApi as extraMasterApi
		self.server = extraMasterApi.RegisterSystem(authConsts.ModNameSpace, authConsts.MasterSystemName, authConsts.MasterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyMaster(self):
		print 'destroy_server==============='