# -*- coding:utf-8 -*-
import client.extraClientApi as clientApi
from functools import wraps
import neteaseMatchScript.clientConsts as clientConsts

def touch_filter(touchType):
	def touchFilter(func):
		@wraps(func)
		def decorated(*args, **kwargs):
			touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
			touchEvent = args[1]["TouchEvent"]
			if touchType == "up":
				if touchEvent == touchEventEnum.TouchUp:
					value = func(*args, **kwargs)
					return value
			if touchType == "down":
				if touchEvent == touchEventEnum.TouchDown:
					value = func(*args, **kwargs)
					return value
			if touchType == "cancel":
				if touchEvent == touchEventEnum.TouchCancel:
					value = func(*args, **kwargs)
					return value
			if touchType == "move":
				if touchEvent == touchEventEnum.TouchMove:
					value = func(*args, **kwargs)
					return value
		return decorated
	return touchFilter

_matchClientSystem = None
_localPlayerId = None
_localUserId = None

def Init(system):
	global _matchClientSystem
	_matchClientSystem = system

def InitLocalUser(uid):
	global _localPlayerId, _localUserId
	_localPlayerId = clientApi.GetLocalPlayerId()
	_localUserId = uid

def GetLocalUID():
	global _localUserId
	return _localUserId

def GetMatchClientSystem():
	global _matchClientSystem
	if not _matchClientSystem:
		_matchClientSystem = clientApi.GetSystem(clientConsts.ModName, clientConsts.ClientSystemName)
	return _matchClientSystem

def DoNotifyToServer(event, data):
	global _matchClientSystem, _localPlayerId, _localUserId
	data['id'] = _localPlayerId
	data['uid'] = _localUserId
	_matchClientSystem.NotifyToServer(event, data)

def GetActivityData():
	global _matchClientSystem
	return _matchClientSystem.mModJsonData

def Destroy():
	global _matchClientSystem
	_matchClientSystem = None

def IsShieldApplyMatch(activityId):
	global _matchClientSystem
	return _matchClientSystem.IsShieldApplyMatch(activityId)