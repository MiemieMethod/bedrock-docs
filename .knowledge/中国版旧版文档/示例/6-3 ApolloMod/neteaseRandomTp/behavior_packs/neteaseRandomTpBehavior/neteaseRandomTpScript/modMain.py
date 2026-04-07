 # -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseRandomTpScript.randomTpConst import ModName, ModVersion, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseRandomTpClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseRandomTp initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(ModName, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseRandomTp destroyClient==============================='