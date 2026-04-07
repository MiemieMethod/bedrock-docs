# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseAddupScript.addupConsts import ModName, ModVersion, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAddupMaster(object):
	@Mod.InitMaster()
	def initService(self):
		print '===========================neteaseAddup initMaster==============================='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def destroyService(self):
		print '===========================neteaseAddup destroyMaster==============================='