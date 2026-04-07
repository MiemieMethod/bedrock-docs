# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseAttrsScript.attrsConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAttrsClient(object):
	@Mod.InitClient()
	def AttrsClientInit(self):
		print '==== neteaseAttrs initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def AttrsClientDestroy(self):
		print '==== neteaseAttrs destroyClient ===='
