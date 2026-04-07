# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseInputBoardscript.inputBoardConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseInputBoardClient(object):
	@Mod.InitClient()
	def InputBoardClientInit(self):
		print '==== neteaseInputBoard initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def InputBoardClientDestroy(self):
		print '==== neteaseInputBoard destroyClient ===='
