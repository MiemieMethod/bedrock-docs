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

import server.extraServerApi as serverApi
_serverModSystem = None

def GetServerModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _serverModSystem
	if not _serverModSystem:
		print "GetServerModSystem", serverApi.GetSystem(ModNameSpace, ServerSystemName)
		_serverModSystem = serverApi.GetSystem(ModNameSpace, ServerSystemName)
	return _serverModSystem

def Destroy():
	global _serverModSystem
	_serverModSystem = None
	
def ShowAlert(playerId, mes):
	alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
	if alertSystem:
		alertSystem.Alert(playerId, mes, 2, 0.5, 0.5)

# =======================================================================================================


