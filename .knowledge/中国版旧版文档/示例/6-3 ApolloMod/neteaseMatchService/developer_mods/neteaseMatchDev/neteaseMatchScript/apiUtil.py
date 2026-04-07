# -*- coding:utf-8 -*-
_matchServiceSystem = None

def SetSystem(system):
	global _matchServiceSystem
	_matchServiceSystem = system

def GetSystem():
	global _matchServiceSystem
	return _matchServiceSystem

def Destroy():
	global _matchServiceSystem
	_matchServiceSystem = None

def NotyfToServerByUID(uid, event, eventData):
	global _matchServiceSystem
	serverId = _matchServiceSystem.GetPlayerServerId(uid)
	if serverId is None:
		return
	eventData['uid'] = uid
	_matchServiceSystem.NotifyToServerNode(serverId, event, eventData)

def BroadcastToServer(uids, event, eventData):
	global _matchServiceSystem
	for uid in uids:
		serverId = _matchServiceSystem.GetPlayerServerId(uid)
		if serverId is None:
			continue
		eventData['uid'] = uid
		_matchServiceSystem.NotifyToServerNode(serverId, event, eventData)