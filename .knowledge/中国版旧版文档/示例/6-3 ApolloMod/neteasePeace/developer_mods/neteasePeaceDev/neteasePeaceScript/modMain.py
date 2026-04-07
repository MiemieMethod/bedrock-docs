# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteasePeaceScript.peaceConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteasePeaceServer(object):
	@Mod.InitServer()
	def PeaceServerInit(self):
		print '==== neteasePeace initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def PeaceServerDestroy(self):
		print '==== neteasePeace destroyServer ===='
