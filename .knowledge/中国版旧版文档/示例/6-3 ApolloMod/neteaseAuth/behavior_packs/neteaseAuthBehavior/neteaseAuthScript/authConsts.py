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
# ===========================================================================================
import client.extraClientApi as extraClientApi
_clientModSystem = None
def GetClientModSystem():
	"""
	获取客户端系统，全局一个单例。
	:return: 返回该Mod的客户端类对象
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None  # 清除引用