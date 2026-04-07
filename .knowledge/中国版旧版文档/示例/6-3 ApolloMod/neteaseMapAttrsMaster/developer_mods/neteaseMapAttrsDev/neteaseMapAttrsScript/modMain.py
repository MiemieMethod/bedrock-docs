# -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseMapAttrsScript.mapAttrsConsts as mapAttrsConsts

@Mod.Binding(name = mapAttrsConsts.ModNameSpace, version = mapAttrsConsts.ModVersion)
class NeteaseResidenceMaster(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initServer(self):
		print '===========================NeteaseMapAttrs initMaster==============================='
		import server.extraMasterApi as extraMasterApi
		self.mServerSystem = extraMasterApi.RegisterSystem(mapAttrsConsts.ModNameSpace, mapAttrsConsts.MasterSystemName,
														   mapAttrsConsts.MasterSystemClsPath)

	@Mod.DestroyMaster()
	def destroyService(self):
		print '===========================NeteaseMapAttrs destroyMaster==============================='