# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseShoutScript.shoutConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseShoutMaster(object):
	@Mod.InitMaster()
	def ShoutMasterInit(self):
		print '==== neteaseShout initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def ShoutMasterDestroy(self):
		print '==== neteaseShout destroyMaster ===='
