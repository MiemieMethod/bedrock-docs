# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseJewelScript.jewelConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseJewelClient(object):
	@Mod.InitClient()
	def JewelClientInit(self):
		print '==== neteaseJewel initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)
		clientApi.RegisterSystem(ModName, 'calc', "neteaseJewelScript.calcClientSystem.CalcClientSystem")

	@Mod.DestroyClient()
	def JewelClientDestroy(self):
		print '==== neteaseJewel destroyClient ===='
