 # -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseMapAttrsScript.mapAttrsConsts as mapAttrsConsts

@Mod.Binding(name = mapAttrsConsts.ModNameSpace, version = mapAttrsConsts.ModVersion)
class NeteaseResidenceClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================NeteaseMapAttrs initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(mapAttrsConsts.ModNameSpace,
														   mapAttrsConsts.ClientSystemName, mapAttrsConsts.ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================NeteaseMapAttrs destroyClient==============================='