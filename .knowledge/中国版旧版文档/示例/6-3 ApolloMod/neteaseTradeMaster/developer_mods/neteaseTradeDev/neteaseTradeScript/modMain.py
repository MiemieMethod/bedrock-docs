# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseTradeScript.tradeConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseTradeMaster(object):
	@Mod.InitMaster()
	def TradeMasterInit(self):
		print '==== neteaseTrade initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def TradeMasterDestroy(self):
		print '==== neteaseTrade destroyMaster ===='
