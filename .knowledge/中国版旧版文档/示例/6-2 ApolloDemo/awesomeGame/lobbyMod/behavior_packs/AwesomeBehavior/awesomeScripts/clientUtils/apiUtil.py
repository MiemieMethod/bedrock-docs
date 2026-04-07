# -*- coding:utf-8 -*-
_clientModSystem = None
import mod.client.extraClientApi as clientApi
from awesomeScripts.modCommon import modConfig

def GetClientModSystem():
	'''
	
	:return:
	'''
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = clientApi.GetSystem(modConfig.Minecraft, modConfig.LobbyClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None