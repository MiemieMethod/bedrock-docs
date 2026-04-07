# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseRandomTpScript.randomTpConst import ModName, ModVersion, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseRandomTpServer(object):
	@Mod.InitService()
	def ServerInit(self):
		print '==== neteaseRandomTp initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def ServerDestroy(self):
		print '==== neteaseRandomTp destroyService ===='
