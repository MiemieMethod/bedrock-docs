# -*- coding: utf-8 -*-
from common.mod import Mod
import neteaseStatisticsScript.statisticsConsts as statisticsConsts

@Mod.Binding(name = statisticsConsts.ModNameSpace, version = statisticsConsts.ModVersion)
class NeteaseStatisticsServer(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		print '===========================NeteaseStatisticsServer initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(statisticsConsts.ModNameSpace, statisticsConsts.ServerSystemName,
														   statisticsConsts.ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================NeteaseStatisticsServer destroyServer==============================='