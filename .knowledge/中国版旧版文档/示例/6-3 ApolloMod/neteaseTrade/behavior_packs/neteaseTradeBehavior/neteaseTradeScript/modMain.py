# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from neteaseTradeScript.tradeConst import ModVersion, ModName, ClientSystemName, ClientSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTradeClient(object):
	@Mod.InitClient()
	def TradeClientInit(self):
		print '==== neteaseTrade initClient ===='
		clientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def TradeClientDestroy(self):
		print '==== neteaseTrade destroyClient ===='
