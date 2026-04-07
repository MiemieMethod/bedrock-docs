# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServiceApi as serviceApi
from neteaseTradeScript.tradeConst import ModVersion, ModName, ServiceSystemName, ServiceSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTradeService(object):
	@Mod.InitService()
	def TradeServiceInit(self):
		print '==== neteaseTrade initService ===='
		serviceApi.RegisterSystem(ModName, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def TradeServiceDestroy(self):
		print '==== neteaseTrade destroyService ===='
