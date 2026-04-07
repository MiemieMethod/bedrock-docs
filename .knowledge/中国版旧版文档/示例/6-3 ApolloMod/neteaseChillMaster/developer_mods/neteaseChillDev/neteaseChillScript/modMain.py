# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseChillScript.chillConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseChillMaster(object):
	@Mod.InitMaster()
	def ChillMasterInit(self):
		print '==== neteaseChill initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def ChillMasterDestroy(self):
		print '==== neteaseChill destroyMaster ===='
