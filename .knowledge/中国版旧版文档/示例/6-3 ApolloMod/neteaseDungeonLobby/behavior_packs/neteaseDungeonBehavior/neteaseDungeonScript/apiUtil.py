# -*- coding:utf-8 -*-
_clientModSystem = None
import client.extraClientApi as extraClientApi
import neteaseDungeonScript.dungeonConsts as dungeonConsts

def GetClientModSystem():
	"""
	:return: neteaseAnnounce.announceClientSystem.AnnounceClientSystem
	:rtype: neteaseAnnounce.announceClientSystem.AnnounceClientSystem
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(dungeonConsts.ModNameSpace, dungeonConsts.LobbyClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None

def GetUiMgr():
	"""
	:return: neteaseAnnounce.mgr.uiMgr.UIMgr
	:rtype: neteaseAnnounce.mgr.uiMgr.UIMgr
	"""
	return GetClientModSystem().GetUiMgr()
