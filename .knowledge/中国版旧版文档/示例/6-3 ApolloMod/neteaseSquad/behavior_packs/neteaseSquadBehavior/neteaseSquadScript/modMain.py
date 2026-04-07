# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseSquadScript.squadConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseSquadClient(object):
	@Mod.InitClient()
	def SquadClientInit(self):
		print '==== neteaseSquad initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def SquadClientDestroy(self):
		print '==== neteaseSquad destroyClient ===='
