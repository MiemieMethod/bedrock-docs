# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseMixedBoardScript.mixedBoardConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseMixedBoardServer(object):
	@Mod.InitServer()
	def MixedBoardServerInit(self):
		print '==== neteaseMixedBoard initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def MixedBoardServerDestroy(self):
		print '==== neteaseMixedBoard destroyServer ===='
