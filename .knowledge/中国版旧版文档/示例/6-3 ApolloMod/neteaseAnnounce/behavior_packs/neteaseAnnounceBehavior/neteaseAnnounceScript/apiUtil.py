# -*- coding:utf-8 -*-
_clientModSystem = None

import client.extraClientApi as extraClientApi
from neteaseAnnounceScript.announceConsts import ModNameSpace, ClientSystemName

def GetClientModSystem():
	"""
	:return: neteaseAnnounceScript.announceClientSystem.AnnounceClientSystem
	:rtype: neteaseAnnounceScript.announceClientSystem.AnnounceClientSystem
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None

def GetMailMgr():
	"""
	:return: neteaseAnnounceScript.mgr.mailMgr.MailMgr
	:rtype: neteaseAnnounceScript.mgr.mailMgr.MailMgr
	"""
	return GetClientModSystem().GetMailMgr()

def GetUiMgr():
	"""
	:return: neteaseAnnounceScript.mgr.uiMgr.UIMgr
	:rtype: neteaseAnnounceScript.mgr.uiMgr.UIMgr
	"""
	return GetClientModSystem().GetUiMgr()

def GetMailUI():
	"""
	:return: neteaseAnnounceScript.ui.netease_announce_mailUi.MailScreen
	:rtype: neteaseAnnounceScript.ui.netease_announce_mailUi.MailScreen
	"""
	from neteaseAnnounceScript.ui.uiDef import UIDef
	return GetClientModSystem().GetUiMgr().GetUI(UIDef.UIMail)

def GetMailButtonUI():
	"""
	:return: neteaseAnnounceScript.ui.netease_announce_mailbtnUi.MailBtnScreen
	:rtype: neteaseAnnounceScript.ui.netease_announce_mailbtnUi.MailBtnScreen
	"""
	from neteaseAnnounceScript.ui.uiDef import UIDef
	return GetClientModSystem().GetUiMgr().GetUI(UIDef.UIDesk)

def GetLoginPopUI():
	"""
	:return: neteaseAnnounceScript.ui.netease_announce_noticeUi.LoginPopupScreen
	:rtype: neteaseAnnounceScript.ui.netease_announce_noticeUi.LoginPopupScreen
	"""
	from neteaseAnnounceScript.ui.uiDef import UIDef
	return GetClientModSystem().GetUiMgr().GetUI(UIDef.UILogin)

def GetFloatWinUI():
	"""
	:return: neteaseAnnounceScript.ui.netease_announce_carouselUI.FloatingWindowScreen
	:rtype: neteaseAnnounceScript.ui.netease_announce_carouselUI.FloatingWindowScreen
	"""
	from neteaseAnnounceScript.ui.uiDef import UIDef
	return GetClientModSystem().GetUiMgr().GetUI(UIDef.UIFloating)

def GetLeftTimeString(timestamp):
	if timestamp < 60:
		return "不足1分钟"
	elif timestamp < 3600:
		return "剩余%d分钟" % (timestamp//60, )
	elif timestamp < 86400:
		return "剩余%d小时" % (timestamp//3600, )
	else:
		return "剩余%d天" % (timestamp//86400, )

def SpiltSingleItem(item):
	if (type(item)) == str:
		try:
			result = SplitSingleItemFromString(item)
		except:
			return None
		return result
	if (type(item)) == dict:
		try:
			result = SplitSingleItemFromDict(item)
		except:
			return None
		return result
	return None

def SplitSingleItemFromString(item):
	params = item.split(":")
	if len(params) == 4:
		namespace, name, auxValue, count = params
		return {
			"itemName": "%s:%s"%(namespace,name),
			"auxValue": int(auxValue),
			"count": int(count),
		}
	else:
		return None

def SplitSingleItemFromDict(item):
	identifier = item.get("itemName", None)
	auxValue = item.get("auxValue", None)
	count = item.get("count", None)
	if (auxValue is None) or (identifier is None) or (count is None):
		return None
	return {
		"itemName": identifier,
		"auxValue": auxValue,
		"count": count,
	}

def ForbidGetBonus():
	import neteaseAnnounceScript.announceConsts as announceConsts
	if announceConsts.MailOpenGetItemWithoutYun:
		return False
	system = extraClientApi.GetSystem(announceConsts.YunModNameSpace, announceConsts.YunClientSystemName)
	if system:
		return False
	return True