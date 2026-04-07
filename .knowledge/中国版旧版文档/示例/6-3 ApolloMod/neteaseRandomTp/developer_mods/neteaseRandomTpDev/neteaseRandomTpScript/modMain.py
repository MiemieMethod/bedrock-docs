# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseRandomTpScript.randomTpConst import ModName, ModVersion, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseRandomTpServer(object):
	@Mod.InitServer()
	def ServerInit(self):
		print '==== neteaseRandomTp initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def ServerDestroy(self):
		print '==== neteaseRandomTp destroyServer ===='
