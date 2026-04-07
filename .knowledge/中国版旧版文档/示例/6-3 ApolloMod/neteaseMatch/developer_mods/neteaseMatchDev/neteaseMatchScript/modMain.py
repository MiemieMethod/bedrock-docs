# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
import neteaseMatchScript.serverConsts as serverConsts

@Mod.Binding(name = serverConsts.ModName, version = serverConsts.ModVersion)
class MatchServerMod(object):
	@Mod.InitServer()
	def MatchServerInit(self):
		print '===========================neteaseMatch initServer==============================='
		serverApi.RegisterSystem(serverConsts.ModName, serverConsts.ServerSystemName, serverConsts.ServerSystemClsPath)

	@Mod.DestroyServer()
	def MatchServerDestroy(self):
		print '===========================neteaseMatch destroyServer==============================='
