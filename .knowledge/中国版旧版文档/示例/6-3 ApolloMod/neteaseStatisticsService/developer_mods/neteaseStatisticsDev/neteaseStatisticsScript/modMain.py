# -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseStatisticsScript.statisticsConsts as statisticsConsts

@Mod.Binding(name = statisticsConsts.ModNameSpace, version = statisticsConsts.ModVersion)
class NeteaseStatisticsService(object):
	def __init__(self):
		pass

	@Mod.InitService()
	def initServer(self):
		print '===========================NeteaseStatisticsService initServer==============================='
		import server.extraServiceApi as extraServiceApi
		self.mServerSystem = extraServiceApi.RegisterSystem(statisticsConsts.ModNameSpace, statisticsConsts.ServiceSystemName,
															statisticsConsts.ServiceSystemClsPath)

	@Mod.DestroyService()
	def destroyService(self):
		print '===========================NeteaseStatisticsService destroyServer==============================='