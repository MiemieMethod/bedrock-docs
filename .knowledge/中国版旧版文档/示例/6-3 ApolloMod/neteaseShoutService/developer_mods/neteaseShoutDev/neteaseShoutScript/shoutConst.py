# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseShout"
ClientSystemName = "neteaseShoutBeh"
ClientSystemClsPath = "neteaseShoutScript.shoutClientSystem.ShoutClientSystem"
ServerSystemName = "neteaseShoutDev"
ServerSystemClsPath = "neteaseShoutScript.shoutServerSystem.ShoutServerSystem"
ServiceSystemName = "neteaseShoutService"
ServiceSystemClsPath = "neteaseShoutScript.shoutServiceSystem.ShoutServiceSystem"
MasterSystemName = "neteaseShoutMaster"
MasterSystemClsPath = "neteaseShoutScript.shoutMasterSystem.ShoutMasterSystem"

# UI
shoutUIName = "shoutUI"
shoutUIClsPath = "neteaseShoutScript.shoutUI.ShoutScreen"
shoutUIScreenDef = "shoutUI.main"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"

# 事件
DisplayShoutBoardEvent = 'DisplayShoutBoardEvent'
NewMsgEvent = 'NewMsgEvent'
PlayerAiringEvent = 'PlayerAiringEvent'


# 指令
class ShoutRequestMapping(object):
	Notice = "/send-new-notice"


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeInvalidUser = 2  # 用户不存在或不在线
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
