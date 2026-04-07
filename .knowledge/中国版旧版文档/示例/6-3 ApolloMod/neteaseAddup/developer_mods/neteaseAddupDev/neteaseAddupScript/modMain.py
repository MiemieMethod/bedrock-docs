# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseAddupScript.addupConsts import ModName, ModVersion, ServerSystemName, ServerSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAddupServer(object):
	@Mod.InitServer()
	def AlertServerInit(self):
		print '==== neteaseAddup initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def AlertServerDestroy(self):
		print '==== neteaseAddup destroyServer ===='
