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

import client.extraClientApi as clientApi
_clientModSystem = None
def GetClientModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = clientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem


def Destroy():
	global _clientModSystem
	_clientModSystem = None

# ======================================================================================================
ALL_SERVER_CHANNEL = 0
class ChatType:
	Common = 0
	Item = 1
	Team = 2
MAX_CHAT_LEN = 100
# =======================================================================================================
def ShowItemDetail(detail, x, y):
	#print "ShowItemDetail", detail, x, y
	attrsSystem = clientApi.GetSystem("neteaseAttrs", "neteaseAttrsBeh")
	print "ShowItemDetail", detail, x, y, attrsSystem
	attrsSystem.Detail(detail, x, y)
