# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseSquadScript.squadConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseSquadServer(object):
	@Mod.InitServer()
	def SquadServerInit(self):
		print '==== neteaseSquad initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def SquadServerDestroy(self):
		print '==== neteaseSquad destroyServer ===='
