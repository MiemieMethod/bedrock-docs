# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseChillScript.chillConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseChillService(object):
	@Mod.InitService()
	def ChillServiceInit(self):
		print '==== neteaseChill initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def ChillServiceDestroy(self):
		print '==== neteaseChill destroyService ===='
