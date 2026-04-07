# -*- coding: utf-8 -*-
from common.mod import Mod
import neteaseMapAttrsScript.mapAttrsConsts as mapAttrsConsts

@Mod.Binding(name = mapAttrsConsts.ModNameSpace, version = mapAttrsConsts.ModVersion)
class NeteaseResidenceServer(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		print '===========================NeteaseMapAttrs initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(mapAttrsConsts.ModNameSpace, mapAttrsConsts.ServerSystemName,
														   mapAttrsConsts.ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================NeteaseMapAttrs destroyServer==============================='