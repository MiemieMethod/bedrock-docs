# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseSquadScript.squadConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseSquadService(object):
	@Mod.InitService()
	def SquadServiceInit(self):
		print '==== neteaseSquad initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def SquadServiceDestroy(self):
		print '==== neteaseSquad destroyService ===='
