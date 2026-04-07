# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseAlert"
ClientSystemName = "neteaseAlertBeh"
ClientSystemClsPath = "neteaseAlertScript.alertClientSystem.AlertClientSystem"
ServerSystemName = "neteaseAlertDev"
ServerSystemClsPath = "neteaseAlertScript.alertServerSystem.AlertServerSystem"
ServiceSystemName = "neteaseAlertService"
ServiceSystemClsPath = "neteaseAlertScript.alertServiceSystem.AlertServiceSystem"
MasterSystemName = "neteaseAlertMaster"
MasterSystemClsPath = "neteaseAlertScript.alertMasterSystem.AlertMasterSystem"

# UI
alertUIName = "netease_alert_screen"
alertUIClsPath = "neteaseAlertScript.netease_alert_screen.AlertScreen"
alertUIScreenDef = "netease_alert_screen.main"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"

# 事件
NewAlertEvent = 'NewAlertEvent'
ModConfigResponseFromServerEvent = 'ModConfigResponseFromServerEvent'
ClientUiInitFinished = 'ClientUiInitFinished'

