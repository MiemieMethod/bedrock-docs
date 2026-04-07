# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseAlertScript.alertConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAlertServer(object):
	@Mod.InitServer()
	def AlertServerInit(self):
		print '==== neteaseAlert initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def AlertServerDestroy(self):
		print '==== neteaseAlert destroyServer ===='
