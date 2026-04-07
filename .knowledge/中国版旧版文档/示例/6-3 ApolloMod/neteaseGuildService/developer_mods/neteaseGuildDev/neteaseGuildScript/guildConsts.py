# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseGuild"
ClientSystemName = "neteaseGuildBehavior"
ClientSystemClsPath = "neteaseGuildScript.neteaseGuildClientSystem.GuildClientSystem"
ServerSystemName = "neteaseGuildDev"
ServerSystemClsPath = "neteaseGuildScript.neteaseGuildServerSystem.GuildServerSystem"
ServiceSystemName = "neteaseGuildService"
ServiceSystemClsPath = "neteaseGuildScript.neteaseGuildServiceSystem.GuildServiceSystem"

import server.extraServiceApi as serviceApi
_serviceModSystem = None
def GetServiceModSystem():
	"""
	返回功能服系统对象（功能服只有服务端系统对象），缓存实例提高性能。
	"""
	global _serviceModSystem
	if not _serviceModSystem:
		_serviceModSystem = serviceApi.GetSystem(ModNameSpace, ServiceSystemName)
	return _serviceModSystem

def Destroy():
	"""
	释放对功能服系统对象的引用
	"""
	global _serviceModSystem
	_serviceModSystem = None

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [UnicodeConvert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

#"============================================================================================="
class DutyType(object):
	"""
	公会的职务宏定义
	"""
	President = 2	# 会长
	Elder = 1		# 长老
	Common = 0		# 普通会员

class GuildAttrType(object):
	"""
	公会的信息存储字段宏定义
	"""
	GuildId = 0 		# 公会的ID
	Name = 1 			# 名字
	Activity = 2		# 总活跃度
	ApplicationQueue = 3	# 申请列表
	PresidentPlayerDict = 4	# 会长玩家列表
	ElderPlayerDict = 5		# 长老玩家列表
	CommonPlayerDict = 6	# 平民玩家列表
	MapId = 7				# 地图标识
	MaxNum = 8				# 公会上限人数
	UnActivityDay = 9		# 不活跃的天数
	CurrentNum = 10		# 当前人数

# 职务==>存储到哪个公会属性	
DutyTypeToGuildDict = {
	DutyType.President : GuildAttrType.PresidentPlayerDict,
	DutyType.Elder : GuildAttrType.ElderPlayerDict,
	DutyType.Common : GuildAttrType.CommonPlayerDict
}
	
class PlayerAttrType(object):
	"""
	单个公会成员的信息存储字段宏定义
	"""
	Uid = 0		# uid
	Name = 1 	# 名字
	Activity = 2	# 活跃度
	GuildId = 3		# 所在公会的ID
	Duty = 4		# 职务：普通，会长，长老
	Online = 5		# 是否在线
	ServerId = 6	# 所在服务器ID
	Level = 7		# 等级
	LastLoginTime = 8	# 上次登录时间
#=======================================================================================================
#判断两个时间戳是否为同一天
def IsOneDay(time1, time2):
	import time
	t1_str = time.strftime("%Y-%m-%d", time.localtime(time1))
	t2_str = time.strftime("%Y-%m-%d", time.localtime(time2))
	return t1_str == t2_str

# 计算距离下一个需要执行函数的时间间隔，单位为秒
def CalNextFuncTime(dayTime):
	import datetime
	now_time = datetime.datetime.now()
	# 获取时间
	next_time = now_time + datetime.timedelta(days=+1)
	next_year = next_time.date().year
	next_month = next_time.date().month
	next_day = next_time.date().day
	# 获取时间
	next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " " + dayTime, "%Y-%m-%d %H:%M:%S")
	# 获取距离时间，单位为秒
	timer_start_time = (next_time - now_time).total_seconds()
	return timer_start_time
#=======================================================================================================
#一些事件
SyncGuildAttrsFromServiceEvent = "SyncGuildAttrsFromServiceEvent"		# service向server同步公会信息
SyncPlayerAttrsFromServiceEvent = "SyncPlayerAttrsFromServiceEvent"		# service向server同步公会成员信息
AddServerPlayerEvent = "AddServerPlayerEvent"			# 引擎事件
DelServerPlayerEvent = "DelServerPlayerEvent"			# 引擎事件
AddPlayerFromServerEvent = "AddPlayerFromServerEvent"			# server向client、service通知有玩家上线
DelPlayerFromServerEvent = "DelPlayerFromServerEvent"			# server向client、service通知有玩家下线
SyncGuildAttrsFromServerEvent = "SyncGuildAttrsFromServerEvent"		# server向client同步公会信息
SyncPlayerAttrsFromServerEvent = "SyncPlayerAttrsFromServerEvent"	# server向client同步公会成员信息
LoadServerAddonScriptsAfter = "LoadServerAddonScriptsAfter"		# 引擎事件
CreateGuildFromServerEvent = "CreateGuildFromServerEvent"			# server向service请求创建新公会
CreateGuildSuccessFromServerEvent = "CreateGuildSuccessFromServerEvent"		# server向service发送创建新公会完毕（扣除代币成功）
GetGuildBriefFromServerEvent = "GetGuildBriefFromServerEvent"		# client向server，或者server向service请求公会的快照信息
GetGuildBriefFromServiceEvent = "GetGuildBriefFromServiceEvent"		# service向server同步公会快照信息
JoinGuildFromServerEvent = "JoinGuildFromServerEvent"			# server向service请求加入指定公会
AgreePlayerFromServerEvent = "AgreePlayerFromServerEvent"		# server向service发送同意玩家的加入公会请求
AppointPlayerFromServerEvent = "AppointPlayerFromServerEvent"	# server向service请求调整公会成员的职务
KickPlayerFromServerEvent = "KickPlayerFromServerEvent"			# server向service请求踢掉指定公会成员
ExitGuildFromServerEvent = "ExitGuildFromServerEvent"			# server向service请求离开公会
DisMissGuildFromMasterEvent = "DisMissGuildFromMasterEvent"		# master向service要求解散公会
ShowTipsFromServiceEvent = "ShowTipsFromServiceEvent"			# service向server发送弹出提示
ReturnGuildMapFromServerEvent = "ReturnGuildMapFromServerEvent"		# server向service请求公会驻地坐标

#=======================================================================================================
#返回码，和返回消息
ResponseText = {}
CodeSuc = 0
ResponseText[CodeSuc] = "成功!"

CodeServiceGuildNumOutOfLimit = 1
ResponseText[CodeServiceGuildNumOutOfLimit] = "服务器公会数量已经达到最大"
CodePlayerNone = 2
ResponseText[CodePlayerNone] = "玩家不存在"
CodePlayerHasGuild = 3
ResponseText[CodePlayerHasGuild] = "玩家已有公会"
CodeCreateSuccess = 4
ResponseText[CodeCreateSuccess] = "创建成功"
CodeParamError = 5
ResponseText[CodeParamError] = "参数错误"
CodeDutyNotEnough = 6
ResponseText[CodeDutyNotEnough] = "权限不足"
CodeGuildDiff = 7
ResponseText[CodeGuildDiff] = "公会不同"
CodeGuildNone = 8
ResponseText[CodeGuildNone] = "公会不存在"
CodeGuildPeopleMaxNum = 9
ResponseText[CodeGuildPeopleMaxNum] = "公会已达最大人数"
CodePlayerNotInGuild = 10
ResponseText[CodePlayerNotInGuild] = "玩家不在公会"
CodePresidentCannotLeaveGuild = 11
ResponseText[CodePresidentCannotLeaveGuild] = "会长无法退出公会，请转让会长后再退出公会。"
CodeGuildDisMiss = 12
ResponseText[CodeGuildDisMiss] = "公会解散"
CodeDBError = 13
ResponseText[CodeDBError] = "数据库操作失败"
CodeGuildNameNotLegal = 14
ResponseText[CodeGuildNameNotLegal] = "名字不合法"
CodeDiamondNotEnough = 15
ResponseText[CodeDiamondNotEnough] = "砖石数量不足"
CodeOutOfTime = 16
ResponseText[CodeOutOfTime] = "请求超时"
CodeKick = 17
ResponseText[CodeKick] = "你已经离开公会"
CodeAddSuccess = 18
ResponseText[CodeAddSuccess] = "你已经加入公会"
CodeApplicationMaxNum = 19
ResponseText[CodeApplicationMaxNum] = "该公会人数已满，看看其他公会吧"
CodeApplicationSuccess = 20
ResponseText[CodeApplicationSuccess] = "申请成功，请等待公会审批"
CodeGuildNameRepeated = 21
ResponseText[CodeGuildNameRepeated] = "名字重复"

#==============================================================================================================
# 每日刷新时间
CHECK_ACTIVITY_TIME = "00:00:00"
# 一天有多少秒
ONE_DAY_TIME = 86400
