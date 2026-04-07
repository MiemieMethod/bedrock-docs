# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseInputBoardScript.inputBoardConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseInputBoardServer(object):
	@Mod.InitServer()
	def InputBoardServerInit(self):
		print '==== neteaseInputBoard initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def InputBoardServerDestroy(self):
		print '==== neteaseInputBoard destroyServer ===='
