# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseAddupScript.addupConsts import ModName, ModVersion, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAddupClient(object):
	@Mod.InitClient()
	def AlertClientInit(self):
		print '==== neteaseAddup initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def AlertClientDestroy(self):
		print '==== neteaseAddup destroyClient ===='
