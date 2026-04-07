# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseTradeScript.tradeConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTradeServer(object):
	@Mod.InitServer()
	def TradeServerInit(self):
		print '==== neteaseTrade initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)
		serverApi.RegisterSystem(ModName, 'bag', "neteaseTradeScript.bagServerSystem.BagServerSystem")

	@Mod.DestroyServer()
	def TradeServerDestroy(self):
		print '==== neteaseTrade destroyServer ===='
