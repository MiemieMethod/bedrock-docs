# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseChat"
ClientSystemName = "neteaseChatBehavior"
ClientSystemClsPath = "neteaseChatScript.neteaseChatClientSystem.ChatClientSystem"
ServerSystemName = "neteaseChatDev"
ServerSystemClsPath = "neteaseChatScript.neteaseChatServerSystem.ChatServerSystem"
ServiceSystemName = "neteaseChatService"
ServiceSystemClsPath = "neteaseChatScript.neteaseChatServiceSystem.ChatServiceSystem"

import server.extraServiceApi as serviceApi

_serviceModSystem = None

def GetServiceModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _serviceModSystem
	if not _serviceModSystem:
		_serviceModSystem = serviceApi.GetSystem(ModNameSpace, ServiceSystemName)
	return _serviceModSystem

def Destroy():
	global _serviceModSystem
	_serviceModSystem = None

# =======================================================================================================
ALL_SERVER_CHANNEL = 0
class ChatType:
	Common = 0
	Item = 1
	Team = 2
# =======================================================================================================

