# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseChillScript.chillConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseChillClient(object):
	@Mod.InitClient()
	def ChillClientInit(self):
		print '==== neteaseChill initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def ChillClientDestroy(self):
		print '==== neteaseChill destroyClient ===='
