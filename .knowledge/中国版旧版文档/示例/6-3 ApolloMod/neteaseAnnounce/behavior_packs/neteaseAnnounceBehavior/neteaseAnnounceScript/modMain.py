 # -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseAnnounceScript.announceConsts import ModVersion, ModNameSpace, ClientSystemName, ClientSystemClsPath

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseAnnounceClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseAnnounce initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(ModNameSpace, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseAnnounce destroyClient==============================='