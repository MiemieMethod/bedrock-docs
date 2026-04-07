# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import server.extraServerApi as serverApi
from CustomMapScripts.modCommon import modConfig

@Mod.Binding(name = modConfig.ModName, version = modConfig.ModVersion)
class CustommapMod(object):
	@Mod.InitServer()
	def CustommapServerInit(self):
		serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)

	@Mod.DestroyServer()
	def CustommapServerDestroy(self):
		pass

	@Mod.InitClient()
	def CustommapClientInit(self):
		clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)

	@Mod.DestroyClient()
	def CustommapClientDestroy(self):
		pass

