# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteasePeaceScript.peaceConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteasePeaceClient(object):
	@Mod.InitClient()
	def PeaceClientInit(self):
		print '==== neteasePeace initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def PeaceClientDestroy(self):
		print '==== neteasePeace destroyClient ===='
