# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
import neteaseTransactionScript.transactionClientConsts as transactionConsts

@Mod.Binding(name = transactionConsts.ModName, version = transactionConsts.ModVersion)
class NeteaseTransactionMod(object):
	@Mod.InitClient()
	def NeteaseTransactionClientInit(self):
		print '===========================neteaseTransaction initClient==============================='
		clientApi.RegisterSystem(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.ClientSystemClsPath)

	@Mod.DestroyClient()
	def NeteaseTransactionClientDestroy(self):
		print '===========================neteaseTransaction destroyClient==============================='

