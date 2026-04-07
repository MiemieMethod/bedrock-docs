# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseDanmuScript.danmuConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDanmuMaster(object):
	@Mod.InitMaster()
	def DanmuMasterInit(self):
		print '==== neteaseDanmu initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def DanmuMasterDestroy(self):
		print '==== neteaseDanmu destroyMaster ===='
