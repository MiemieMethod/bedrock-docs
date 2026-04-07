# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseDanmu"
ClientSystemName = "neteaseDanmuBeh"
ClientSystemClsPath = "neteaseDanmuScript.danmuClientSystem.DanmuClientSystem"
ServerSystemName = "neteaseDanmuDev"
ServerSystemClsPath = "neteaseDanmuScript.danmuServerSystem.DanmuServerSystem"
ServiceSystemName = "neteaseDanmuService"
ServiceSystemClsPath = "neteaseDanmuScript.danmuServiceSystem.DanmuServiceSystem"
MasterSystemName = "neteaseDanmuMaster"
MasterSystemClsPath = "neteaseDanmuScript.danmuMasterSystem.DanmuMasterSystem"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"


# 指令
class DanmuRequestMapping(object):
	Notice = "/send-new-notice"		# 已废弃


# 错误码
RespCodeSuccess = 1  			# 请求成功
RespCodeInvalidParameter = 4 	# 请求参数有误
RespCodeTimeout = 2 			# 请求超时
RespCodeDBError = 3 			# 数据库操作失败
