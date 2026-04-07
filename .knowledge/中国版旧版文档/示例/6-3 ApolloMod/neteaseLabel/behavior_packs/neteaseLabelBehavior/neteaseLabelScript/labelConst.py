# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.3"
ModName = "neteaseLabel"
ClientSystemName = "neteaseLabelBeh"
ClientSystemClsPath = "neteaseLabelScript.labelClientSystem.LabelClientSystem"
ServerSystemName = "neteaseLabelDev"
ServerSystemClsPath = "neteaseLabelScript.labelServerSystem.LabelServerSystem"
ServiceSystemName = "neteaseLabelService"
ServiceSystemClsPath = "neteaseLabelScript.labelServiceSystem.LabelServiceSystem"
MasterSystemName = "neteaseLabelMaster"
MasterSystemClsPath = "neteaseLabelScript.labelMasterSystem.LabelMasterSystem"

# UI
labelUIName = "labelMainUI"
labelUIClsPath = "neteaseLabelScript.labelMainUI.LabelMainScreen"
labelUIScreenDef = "netease_label_mainUI.main"

# 数据库表名
TableLabelData = "neteaseLabelDataInfo"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
AddServerPlayerEvent = 'AddServerPlayerEvent'
DelServerPlayerEvent = 'DelServerPlayerEvent'

# 事件
QueryAllLabelsInUseEvent = 'QueryAllLabelsInUseEvent'
DisplayLabelBoardEvent = 'DisplayLabelBoardEvent'
PlayerPutOnLabelEvent = 'PlayerPutOnLabelEvent'
PlayerTakeOffLabelEvent = 'PlayerTakeOffLabelEvent'


# 指令
class LabelRequestMapping(object):
	Insert = "/insert-one-label"
	Delete = "/delete-one-label"


# 错误码
RespCodeSuccess = 1  # 请求成功
RespCodeInvalidParameter = 4  # 请求参数有误
RespCodeTimeout = 2  # 请求超时
RespCodeDBError = 3  # 数据库操作失败
