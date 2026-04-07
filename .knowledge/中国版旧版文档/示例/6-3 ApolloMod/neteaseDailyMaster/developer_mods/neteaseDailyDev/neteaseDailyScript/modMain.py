# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseDailyScript.dailyConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDailyMaster(object):
	@Mod.InitMaster()
	def DailyMasterInit(self):
		print '==== neteaseDaily initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def DailyMasterDestroy(self):
		print '==== neteaseDaily destroyMaster ===='
