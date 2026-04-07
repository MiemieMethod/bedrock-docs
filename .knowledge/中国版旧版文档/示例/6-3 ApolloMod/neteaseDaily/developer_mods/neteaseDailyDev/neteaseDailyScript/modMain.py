# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseDailyScript.dailyConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDailyServer(object):
	@Mod.InitServer()
	def DailyServerInit(self):
		print '==== neteaseDaily initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def DailyServerDestroy(self):
		print '==== neteaseDaily destroyServer ===='
