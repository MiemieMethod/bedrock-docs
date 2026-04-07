# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseFeedback"
ClientSystemName = "neteaseFeedbackBehavior"
ClientSystemClsPath = "neteaseFeedbackScript.neteaseFeedbackClientSystem.FeedbackClientSystem"
ServerSystemName = "neteaseFeedbackDev"
ServerSystemClsPath = "neteaseFeedbackScript.neteaseFeedbackServerSystem.FeedbackServerSystem"
ServiceSystemName = "neteaseFeedbackService"
ServiceSystemClsPath = "neteaseFeedbackScript.neteaseFeedbackServiceSystem.FeedbackServiceSystem"

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