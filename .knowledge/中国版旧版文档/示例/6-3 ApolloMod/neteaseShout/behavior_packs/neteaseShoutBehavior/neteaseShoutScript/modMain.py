# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseShoutScript.shoutConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseShoutClient(object):
	@Mod.InitClient()
	def ShoutClientInit(self):
		print '==== neteaseShout initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def ShoutClientDestroy(self):
		print '==== neteaseShout destroyClient ===='
