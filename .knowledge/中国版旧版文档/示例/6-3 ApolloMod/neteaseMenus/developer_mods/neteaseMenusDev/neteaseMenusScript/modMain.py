# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseMenusScript.menusConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseMenusServer(object):
	@Mod.InitServer()
	def ServerInit(self):
		print '==== neteaseMenus initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def ServerDestroy(self):
		print '==== neteaseMenus destroyServer ===='
