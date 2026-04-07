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

# =======================================================================================================
ALL_SERVER_CHANNEL = 0

class ChatType:
	Common = 0
	Item = 1
	Team = 2
	
BAG_ITEM_REGREX = r"/\[item ([0-9]{1,2})\]"
TEAM_REGREX = r"^/\[team\]$"

def GetSlotPos(mes):
	end_index = mes.rfind("]")
	slotPos = int(mes[7:end_index])
	return slotPos

def CheckPlayerSquad(uid, cb):
	squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
	if squadSystem is None:
		cb(False, None)
		return
	squadSystem.CheckPlayerSquad(uid, cb)
	
def OnSquadRecruitmentApply(data):
	squadSystem = serverApi.GetSystem("neteaseSquad", "neteaseSquadDev")
	squadSystem.OnSquadRecruitmentApply(data)


