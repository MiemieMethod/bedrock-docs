# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseStatistics"
ServerSystemName = "neteaseStatisticsServer"
ServiceSystemName = "neteaseStatisticsService"
ServerSystemClsPath = 'neteaseStatisticsScript.statisticsServerSys.StatisticsServerSys'
ServiceSystemClsPath = 'neteaseStatisticsScript.statisticsServiceSys.StatisticsServiceSys'

# event
class ServerEvent(object):
	SyncUserStatus = "SyncUserStatus"

# database
PlayerStaticTable = "neteaseStatsUser"
PlayerDailyTable = "neteaseStatsUserDaily"


# 一些配置参数，核心参数考虑过性能和及时性的平衡，不建议修改
MaxFollowUpTime = 3600			# 开机之后，追朔尚未完成的统计任务的上限时效
PlayerDailyDelayTime = 60		# 为了防止有日志等数据未同步，统计开始的延时
PlayerDailyRunInterval = 300	# 每5分钟统计一次
PlayerDailyMemoryCacheSize = 10000	# 缓存数据高于多少，才会清理缓存
PlayerDailyMemoryKeepTime = 900		# 多久没有数据更新的缓存数据，会被清理出内存
OneDaySecond = 3600 * 24		# 一天有多少秒
OneDayDelayTime = 600			# 每日统计延时个10分钟开始

# 辅助函数 -- 通用
def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

def GetTodayPassTime(timestamp):
	import time
	local = time.localtime(timestamp)
	return local.tm_hour*3600 + local.tm_min*60 + local.tm_sec

LOG_FIELDS_MAP = {
	'login': ('uid', 'when'),
	'online': ('uid', 'when', 'oltime', 'd_oltime'),
	'logout': ('uid', 'when', 'oltime', 'd_oltime'),
	'pay': ('uid', 'when', 'pay', 'orderkey'),
}
def GetLogFields(keyword):
	global LOG_FIELDS_MAP
	return LOG_FIELDS_MAP.get(keyword, None)
