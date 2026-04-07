# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseShoutScript.shoutConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseShoutService(object):
	@Mod.InitService()
	def ShoutServiceInit(self):
		print '==== neteaseShout initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def ShoutServiceDestroy(self):
		print '==== neteaseShout destroyService ===='
