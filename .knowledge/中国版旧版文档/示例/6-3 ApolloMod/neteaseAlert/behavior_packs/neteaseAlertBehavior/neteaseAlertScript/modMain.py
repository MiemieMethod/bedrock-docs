# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseAlertScript.alertConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseAlertClient(object):
	@Mod.InitClient()
	def AlertClientInit(self):
		print '==== neteaseAlert initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def AlertClientDestroy(self):
		print '==== neteaseAlert destroyClient ===='
