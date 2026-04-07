# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseTextBoardscript.textBoardConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTextBoardClient(object):
	@Mod.InitClient()
	def TextBoardClientInit(self):
		print '==== neteaseTextBoard initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def TextBoardClientDestroy(self):
		print '==== neteaseTextBoard destroyClient ===='
