# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------------------
# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseUniqueId"
ServiceSystemName = "neteaseUniqueIdService"
ServiceSystemClsPath = "neteaseUniqueIdScript.uniqueIdServiceSystem.UniqueIdServiceSystem"
#---------------------------------------------------------------------------------------
TryUseMysqlFirst = 1	# 先尝试初始化mysql
DefaultPlusSize = 200	# 每个关键字单次从数据库申请ID会占用多少个
ConfigurableDefineList = ["TryUseMysqlFirst", "DefaultPlusSize",
						  ]
#---------------------------------------------------------------------------------------
# 数据库表名
# 记录ID的域和对应已经分发出去的最大ID
TableUniqueId = "neteaseUniqueId"
#---------------------------------------------------------------------------------------
class UniqueIdEvent(object):
	AskNew = "UniqueIdAskNew"
#---------------------------------------------------------------------------------------
# 错误码
CodeSuc = 0
CodeAskNewEmptyKeyWord = 1
CodeAskNewEmptyNum = 2
CodeAskNewWrongNum = 3
CodeAskNewNotReady = 4
CodeAskNewMysqlFail = 5
CodeAskNewMongoFail = 6

ErrorText = {}
def ReloadErrorText():
	global ErrorText
	ErrorText[CodeSuc] = "请求成功"
	ErrorText[CodeAskNewEmptyKeyWord] = "请求失败，keyword不能为空"
	ErrorText[CodeAskNewEmptyNum] = "请求失败，requireNum不能为空"
	ErrorText[CodeAskNewWrongNum] = "请求失败，requireNum必须是正整数"
	ErrorText[CodeAskNewNotReady] = "请求失败，服务尚未初始化完成，请稍后重试"
	ErrorText[CodeAskNewMysqlFail] = "请求失败，数据库错误"
	ErrorText[CodeAskNewMongoFail] = "请求失败，数据库错误"
