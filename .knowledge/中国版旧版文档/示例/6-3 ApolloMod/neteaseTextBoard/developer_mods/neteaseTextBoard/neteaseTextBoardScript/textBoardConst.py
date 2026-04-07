# -*- coding: utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModName = "neteaseTextBoard"
ClientSystemName = "neteaseTextBoardBeh"
ClientSystemClsPath = "neteaseTextBoardScript.textBoardClientSystem.TextBoardClientSystem"
ServerSystemName = "neteaseTextBoardDev"
ServerSystemClsPath = "neteaseTextBoardScript.textBoardServerSystem.TextBoardServerSystem"

# 引擎事件
UiInitFinishedEvent = "UiInitFinished"
ServerChatEvent = "ServerChatEvent"

# Mod 事件
# 服务端事件
SetTextContentEvent = "SetTextContent"
GetTextContentEvent = "GetTextContent"
OpenTextBoardEvent = "OpenTextBoard"
CloseTextBoardEvent = "CloseTextBoard"

# 客户端事件
SendTextContentEvent = "SendTextContentEvent"