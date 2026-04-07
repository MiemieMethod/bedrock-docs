# -*- coding: utf-8 -*-
import time
import server.extraServiceApi as extraServiceApi
ServiceSystem = extraServiceApi.GetServiceSystemCls()
import service.serviceConf as serviceConf
import service.timermanager as timermanager
import neteaseMonitor.monitor as monitor
from neteaseStatisticsScript.statisticsConsts import ModNameSpace
import neteaseStatisticsScript.mysqlStatisticsMgr as StatisticsMgr
import neteaseStatisticsScript.mysqlStatisticsCacheMgr as StatisticsCacheMgr

class StatisticsServiceSys(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		self.InitDb()
		self.mActiveMgrs = {}
		self.mUseMonitorHandlers = []
		for moduleName in serviceConf.get_module_names():
			if not moduleName.startswith(ModNameSpace):
				continue
			manager = StatisticsMgr.CStatisticsMgr(self, moduleName, 0)
			self.mActiveMgrs[moduleName] = manager
			handlerName = "NeteaseStatsLogGetter"
			monitor.RegisterTaskGetter(handlerName, manager.NeteaseMonitorGetter)
			self.mUseMonitorHandlers.append(handlerName)
			# 负责每日、每月的统计逻辑
			realModuleName = "%s_daily" % moduleName
			manager = StatisticsCacheMgr.CStatisticsCacheMgr(self, realModuleName, 0)
			self.mActiveMgrs[realModuleName] = manager
			handlerName = "NeteaseStatsDailyGetter"
			monitor.RegisterTaskGetter(handlerName, manager.NeteaseMonitorGetter)
			self.mUseMonitorHandlers.append(handlerName)

	def Destroy(self):
		for manager in self.mActiveMgrs.itervalues():
			manager.Destroy()
		self.mActiveMgrs.clear()
		for handlerName in self.mUseMonitorHandlers:
			monitor.UnregisterTaskGetter(handlerName)
		self.mUseMonitorHandlers = []
		#
		import apolloCommon.mysqlPool as mysqlPool
		mysqlPool.Finish()
		ServiceSystem.Destroy(self)

	def InitDb(self):
		import apolloCommon.mysqlPool as mysqlPool
		mysqlPool.InitDB(20)
		return True

	def Update(self):
		timermanager.timerManager.tick()
	# ------------------------------------------------------------------------------------

