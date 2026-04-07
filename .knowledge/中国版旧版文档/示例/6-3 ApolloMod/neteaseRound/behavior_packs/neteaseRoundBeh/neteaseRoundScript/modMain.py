# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import neteaseRoundScript.roundConst as roundConst


@Mod.Binding(name=roundConst.ModName, version=roundConst.ModVersion)
class NeteaseRoundClient(object):
	@Mod.InitClient()
	def DailyClientInit(self):
		print '==== neteaseRound initClient ===='
		clientApi.RegisterSystem(roundConst.ModName, roundConst.ClientSampleSystemName, roundConst.ClientSampleSystemClsPath)
		clientApi.RegisterSystem(roundConst.ModName, roundConst.ClientBattleSystemName, roundConst.ClientBattleSystemClsPath)

	@Mod.DestroyClient()
	def DailyClientDestroy(self):
		print '==== neteaseRound destroyClient ===='
