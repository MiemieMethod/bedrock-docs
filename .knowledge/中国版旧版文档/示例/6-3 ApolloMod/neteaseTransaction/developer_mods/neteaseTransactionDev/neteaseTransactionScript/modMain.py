# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
import neteaseTransactionScript.transactionServerConsts as transactionConsts

@Mod.Binding(name = transactionConsts.ModName, version = transactionConsts.ModVersion)
class NeteaseTransactionMod(object):
	@Mod.InitServer()
	def NeteaseTransactionServerInit(self):
		print '===========================neteaseTransaction initServer==============================='
		serverApi.RegisterSystem(transactionConsts.ModName, transactionConsts.ServerSystemName, transactionConsts.ServerSystemClsPath)

	@Mod.DestroyServer()
	def NeteaseTransactionServerDestroy(self):
		print '===========================neteaseTransaction destroyServer==============================='
