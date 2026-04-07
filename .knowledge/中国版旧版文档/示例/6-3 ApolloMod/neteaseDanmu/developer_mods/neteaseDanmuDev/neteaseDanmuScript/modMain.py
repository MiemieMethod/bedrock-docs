# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseDanmuScript.danmuConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDanmuServer(object):
	@Mod.InitServer()
	def DanmuServerInit(self):
		print '==== neteaseDanmu initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def DanmuServerDestroy(self):
		print '==== neteaseDanmu destroyServer ===='
