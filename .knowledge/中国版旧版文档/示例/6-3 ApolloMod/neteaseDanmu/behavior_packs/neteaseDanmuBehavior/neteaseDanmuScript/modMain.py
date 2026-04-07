# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseDanmuScript.danmuConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDanmuClient(object):
	@Mod.InitClient()
	def DanmuClientInit(self):
		print '==== neteaseDanmu initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def DanmuClientDestroy(self):
		print '==== neteaseDanmu destroyClient ===='
