 # -*- coding: utf-8 -*-

from common.mod import Mod
import simpleScript.simpleConsts as simpleConsts

@Mod.Binding(name = simpleConsts.ModNameSpace, version = simpleConsts.ModVersion)
class SimpleClientMod(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================SimpleClientMod initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(simpleConsts.ModNameSpace, simpleConsts.ClientSystemName, simpleConsts.ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================SimpleClientMod destroyClient==============================='