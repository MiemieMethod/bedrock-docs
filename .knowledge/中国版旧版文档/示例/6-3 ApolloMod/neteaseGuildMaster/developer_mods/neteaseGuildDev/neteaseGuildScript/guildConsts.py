# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseGuild"
ClientSystemName = "neteaseGuildBehavior"
ClientSystemClsPath = "neteaseGuildScript.neteaseGuildClientSystem.GuildClientSystem"
ServerSystemName = "neteaseGuildDev"
ServerSystemClsPath = "neteaseGuildScript.neteaseGuildServerSystem.GuildServerSystem"
ServiceSystemName = "neteaseService"
ServiceSystemClsPath = "neteaseGuildScript.neteaseGuildServiceSystem.GuildServiceSystem"
MasterSystemName = "neteaseMaster"
MaterSystemClsPath = "neteaseGuildScript.neteaseGuildMasterSystem.GuildMasterSystem"

import server.extraMasterApi as masterApi
_masterModSystem = None
def GetMasterModSystem():
	"""
	返回管理服系统对象（管理服只有服务端系统对象），缓存实例提高性能。
	"""
	global _masterModSystem
	if not _masterModSystem:
		_masterModSystem = masterApi.GetSystem(ModNameSpace, MasterSystemName)
	return _masterModSystem

def Destroy():
	"""
	释放对管理服系统对象的引用
	"""
	global _masterModSystem
	_masterModSystem = None
	
#=======================================================================================================
#一些事件
DisMissGuildFromMasterEvent = "DisMissGuildFromMasterEvent"		# master向service发送解散指定公会的指令

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
