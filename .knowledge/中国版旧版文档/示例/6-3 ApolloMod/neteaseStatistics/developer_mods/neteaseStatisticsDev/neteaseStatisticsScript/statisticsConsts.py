# -*- coding: utf-8 -*-

#整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseStatistics"
ServerSystemName = "neteaseStatisticsServer"
ServiceSystemName = "neteaseStatisticsService"
ServerSystemClsPath = 'neteaseStatisticsScript.statisticsServerSys.StatisticsServerSys'
ServiceSystemClsPath = 'neteaseStatisticsScript.statisticsServiceSys.StatisticsServiceSys'

#event
class ServerEvent(object):
	SyncUserStatus = "SyncUserStatus"
