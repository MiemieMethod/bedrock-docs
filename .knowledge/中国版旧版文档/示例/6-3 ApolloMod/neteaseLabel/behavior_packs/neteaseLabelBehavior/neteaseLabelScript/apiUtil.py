# -*- coding:utf-8 -*-

import client.extraClientApi as clientApi
from functools import wraps
_labelClientSystem = None

def SetSystem(clientSystem):
	global _labelClientSystem
	_labelClientSystem = clientSystem

def GetPopUpUI():
	global _labelClientSystem
	return _labelClientSystem.mPopUpUINode

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

def Destroy():
	global _labelClientSystem
	_labelClientSystem = None