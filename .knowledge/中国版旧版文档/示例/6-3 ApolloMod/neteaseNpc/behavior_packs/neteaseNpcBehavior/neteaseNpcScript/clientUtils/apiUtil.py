# -*- coding:utf-8 -*-
_clientModSystem = None
import client.extraClientApi as clientApi

def GetClientModSystem():
	'''
	获取客户端系统
	:return:
	'''
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = clientApi.GetSystem("neteaseNpc", "npcClient")
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None