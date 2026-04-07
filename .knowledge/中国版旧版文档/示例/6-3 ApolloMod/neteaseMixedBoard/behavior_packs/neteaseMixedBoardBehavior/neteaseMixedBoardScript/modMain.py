# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseMixedBoardscript.mixedBoardConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseMixedBoardClient(object):
	@Mod.InitClient()
	def MixedBoardClientInit(self):
		print '==== neteaseMixedBoard initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def MixedBoardClientDestroy(self):
		print '==== neteaseMixedBoard destroyClient ===='
