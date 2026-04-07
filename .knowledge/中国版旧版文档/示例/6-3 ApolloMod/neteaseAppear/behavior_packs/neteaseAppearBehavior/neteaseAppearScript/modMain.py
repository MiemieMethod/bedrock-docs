# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseAppearScript.appearConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseDailyClient(object):
	@Mod.InitClient()
	def DailyClientInit(self):
		print '==== neteaseAppear initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def DailyClientDestroy(self):
		print '==== neteaseAppear destroyClient ===='
