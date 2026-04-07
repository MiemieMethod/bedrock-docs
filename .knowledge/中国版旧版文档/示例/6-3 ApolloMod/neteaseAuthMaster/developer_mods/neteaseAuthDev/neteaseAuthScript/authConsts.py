# -*- coding:utf-8 -*-
# =========================================================================================
# 整个Mod的一些绑定配置
ModVersion = "1.0.2"
ModNameSpace = "neteaseAuth"
ClientSystemName = "neteaseAuthBeh"
ClientSystemClsPath = "neteaseAuthScript.neteaseAuthClientSystem.AuthClientSystem"
ServerSystemName = "neteaseAuthDev"
ServerSystemClsPath = "neteaseAuthScript.neteaseAuthServerSystem.AuthServerSystem"
MasterSystemName = "neteaseAuthMaster"
MasterSystemClsPath = "neteaseAuthScript.neteaseAuthMasterSystem.AuthMasterSystem"
ServiceSystemName = "neteaseAuthService"
ServiceSystemClsPath = "neteaseAuthScript.neteaseAuthServiceSystem.AuthServiceSystem"
# ===========================================================================================
ChangePlayerGroupEvent = "ChangePlayerGroupEvent"
# ===========================================================================================
import server.extraServerApi as serverApi
_serverModSystem = None
def GetMasterModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _serverModSystem
	if not _serverModSystem:
		_serverModSystem = serverApi.GetSystem(ModNameSpace, MasterSystemName)
	return _serverModSystem

def Destroy():
	global _serverModSystem
	_serverModSystem = None

#op新增的命令
BAN_COMMAND = 'ban'
UNBAN_COMMAND = 'unban'
SILENT_COMMAND = 'silent'
UNSILENT_COMMAND = 'unsilent'