# -*- coding:utf-8 -*-

# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseChest"
ClientSystemName = "neteaseChestBehavior"
ClientSystemClsPath = "neteaseChestScript.neteaseChestClientSystem.ChestClientSystem"
ServerSystemName = "neteaseChestDev"
ServerSystemClsPath = "neteaseChestScript.neteaseChestServerSystem.ChestServerSystem"
MasterSystemName = "neteaseChestMaster"
MasterSystemClsPath = "neteaseChestScript.neteaseChestMasterSystem.ChestMasterSystem"

import client.extraClientApi as clientApi

_clientModSystem = None

def GetClientModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = clientApi.GetSystem(ModNameSpace, ClientSystemName)
	return _clientModSystem

def Destroy():
	global _clientModSystem
	_clientModSystem = None

class UIDef:
	UI_TIPS = {
		'ui_key': 'TipsUI',
		'ui_cls_path': 'neteaseChestScript.modUI.tipsUI.TipsScreen',
		'ui_def': 'TipsUI.main'
	}
	UI_MANAGE = {
		'ui_key': 'ManageUI',
		'ui_cls_path': 'neteaseChestScript.modUI.manageUI.ManageScreen',
		'ui_def': 'ManageUI.main'
	}

class NotifyDef:
	TIPS = {
		'notify_type': '提示',
		'title': '提示',
		'message': '',
		'confirm': '确定',
		'cancel': '取消'
	}

# =======================================================================================================
# 一些事件
UiInitFinishedEvent = 'UiInitFinished'
ShowApplicationTipsFromServerEvent = "ShowApplicationTipsFromServerEvent"
ApplicateFromClientEvent = "ApplicateFromClientEvent"
ShowChestManageFromServerEvent = "ShowChestManageFromServerEvent"
DeletUserFromClientEvent = "DeletUserFromClientEvent"
AcceptUserFromClientEvent = "AcceptUserFromClientEvent"
RefuseUserFromClientEvent = "RefuseUserFromClientEvent"