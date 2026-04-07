# -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseResidenceScript.residenceConsts as residenceConsts

@Mod.Binding(name = residenceConsts.ModNameSpace, version = residenceConsts.ModVersion)
class NeteaseResidenceMaster(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initServer(self):
		print '===========================NeteaseResidenceMaster initServer==============================='
		import server.extraMasterApi as extraMasterApi
		self.mServerSystem = extraMasterApi.RegisterSystem(residenceConsts.ModNameSpace, residenceConsts.MasterSystemName,
			residenceConsts.MasterSystemClsPath)

	@Mod.DestroyMaster()
	def destroyService(self):
		print '===========================NeteaseResidenceMaster destroyServer==============================='