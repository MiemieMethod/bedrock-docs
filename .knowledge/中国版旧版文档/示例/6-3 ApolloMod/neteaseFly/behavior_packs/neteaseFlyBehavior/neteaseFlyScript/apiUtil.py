# -*- coding:utf-8 -*-
_clientModSystem = None

import client.extraClientApi as extraClientApi
from neteaseFlyScript.flyClientConsts import ClientSystemName, ModNameSpace


def GetClientModSystem():
	"""
	:return: neteaseFly.flyClientSystem.FlyClientSystem
	:rtype: neteaseFly.flyClientSystem.FlyClientSystem
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None

def GetUiMgr():
	"""
	:return: neteaseFly.mgr.uiMgr.UIMgr
	:rtype: neteaseFly.mgr.uiMgr.UIMgr
	"""
	return GetClientModSystem().GetUiMgr()

def GetFlyPluginUI():
	"""
	:return: neteaseFly.ui.mailUi.MailScreen
	:rtype: neteaseFly.ui.mailUi.MailScreen
	"""
	return GetClientModSystem().GetFlyPluginUI()
