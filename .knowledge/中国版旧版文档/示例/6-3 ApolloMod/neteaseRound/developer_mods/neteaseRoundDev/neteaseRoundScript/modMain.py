# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
import neteaseRoundScript.roundConst as roundConst

@Mod.Binding(name=roundConst.ModName, version=roundConst.ModVersion)
class NeteaseRoundServer(object):
	@Mod.InitServer()
	def ServerInit(self):
		print '==== neteaseRound initServer ===='
		serverApi.RegisterSystem(roundConst.ModName, roundConst.ServerSampleSystemName, roundConst.ServerSampleSystemClsPath)
		serverApi.RegisterSystem(roundConst.ModName, roundConst.ServerBattleSystemName, roundConst.ServerBattleSystemClsPath)

	@Mod.DestroyServer()
	def ServerDestroy(self):
		print '==== neteaseRound destroyServer ===='
