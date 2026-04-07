 # -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseBattleScript.battleCommon.battleConsts import ModVersion, ModNameSpace, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseBattleClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================NeteaseBattle initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(ModNameSpace, ClientSystemName, ClientSystemClsPath)
		self.mClientSystem.Init()

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================NeteaseBattle destroyClient==============================='