# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseInputBoard"
ClientSystemName = "neteaseInputBoardBeh"
ClientSystemClsPath = "neteaseInputBoardScript.inputBoardClientSystem.InputBoardClientSystem"
ServerSystemName = "neteaseInputBoardDev"
ServerSystemClsPath = "neteaseInputBoardScript.inputBoardServerSystem.InputBoardServerSystem"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
ServerChatEvent = "ServerChatEvent"
DelServerPlayerEvent = "DelServerPlayerEvent"

# Mod事件
# 服务端事件
OpenInputBoardEvent = "OpenInputBoardEvent"
CloseInputBoardEvent = "CloseInputBoardEvent"
SetInputTextEvent = "SetInputTextEvent"

# 客户端事件
ButtonCallbackEvent = "ButtonCallbackEvent"