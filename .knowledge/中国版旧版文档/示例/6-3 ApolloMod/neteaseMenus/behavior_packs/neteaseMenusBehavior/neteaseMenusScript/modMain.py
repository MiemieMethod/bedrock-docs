# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseMenusScript.menusConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseMenusClient(object):
	@Mod.InitClient()
	def ClientInit(self):
		print '==== neteaseMenus initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def ClientDestroy(self):
		print '==== neteaseMenus destroyClient ===='
