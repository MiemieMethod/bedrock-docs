# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseTextBoardScript.textBoardConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTextBoardServer(object):
	@Mod.InitServer()
	def TextBoardServerInit(self):
		print '==== neteaseTextBoard initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def TextBoardServerDestroy(self):
		print '==== neteaseTextBoard destroyServer ===='
