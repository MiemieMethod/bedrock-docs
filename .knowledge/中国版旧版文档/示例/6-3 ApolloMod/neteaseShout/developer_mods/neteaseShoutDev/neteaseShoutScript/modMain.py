# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseShoutScript.shoutConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseShoutServer(object):
	@Mod.InitServer()
	def ShoutServerInit(self):
		print '==== neteaseShout initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def ShoutServerDestroy(self):
		print '==== neteaseShout destroyServer ===='
