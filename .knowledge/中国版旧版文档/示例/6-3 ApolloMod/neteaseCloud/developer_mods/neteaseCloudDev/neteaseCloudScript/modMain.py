# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseCloudScript.cloudConsts import ModVersion, ModNameSpace, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseCloudServer(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseCloud initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(ModNameSpace, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================neteaseCloud destroyServer==============================='