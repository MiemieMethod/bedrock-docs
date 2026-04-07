# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseAppearScript.appearConst import ModName, ModVersion, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDailyServer(object):
	@Mod.InitServer()
	def ServerInit(self):
		print '==== neteaseAppear initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def ServerDestroy(self):
		print '==== neteaseAppear destroyServer ===='
