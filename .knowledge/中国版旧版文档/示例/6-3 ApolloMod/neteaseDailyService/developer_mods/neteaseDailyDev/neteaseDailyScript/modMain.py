# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseDailyScript.dailyConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDailyService(object):
	@Mod.InitService()
	def DailyServiceInit(self):
		print '==== neteaseDaily initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def DailyServiceDestroy(self):
		print '==== neteaseDaily destroyService ===='
