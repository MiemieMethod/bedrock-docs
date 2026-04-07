# -*- coding:utf-8 -*-
_transactionClientSystem = None

import client.extraClientApi as clientApi
from functools import wraps
from neteaseTransactionScript.transactionClientConsts import ClientSystemName, ModName


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

def GetTransactionClientSystem():
	"""
	:return: neteaseFly.flyClientSystem.FlyClientSystem
	:rtype: neteaseFly.flyClientSystem.FlyClientSystem
	"""
	global _transactionClientSystem
	if not _transactionClientSystem:
		_transactionClientSystem = clientApi.GetSystem(ModName, ClientSystemName)
	return _transactionClientSystem

def Destroy():
	global _transactionClientSystem
	_transactionClientSystem = None
