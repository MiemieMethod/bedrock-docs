# -*- coding: utf-8 -*-
from common.mod import Mod
import neteaseResidenceScript.residenceConsts as residenceConsts

@Mod.Binding(name = residenceConsts.ModNameSpace, version = residenceConsts.ModVersion)
class NeteaseResidenceServer(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		print '===========================NeteaseResidenceServer initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, 
			residenceConsts.ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================NeteaseResidenceServer destroyServer==============================='