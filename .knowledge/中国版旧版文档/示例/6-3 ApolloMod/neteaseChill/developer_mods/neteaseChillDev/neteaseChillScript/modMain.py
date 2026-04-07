# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseChillScript.chillConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseChillServer(object):
	@Mod.InitServer()
	def ChillServerInit(self):
		print '==== neteaseChill initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def ChillServerDestroy(self):
		print '==== neteaseChill destroyServer ===='
