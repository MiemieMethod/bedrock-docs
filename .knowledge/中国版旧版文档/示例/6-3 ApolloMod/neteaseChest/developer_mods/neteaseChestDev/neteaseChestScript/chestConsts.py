# -*- coding:utf-8 -*-
# =========================================================================================
# 整个Mod的一些绑定配置
ModVersion = "1.0.0"
ModNameSpace = "neteaseChest"
ClientSystemName = "neteaseChestBehavior"
ClientSystemClsPath = "neteaseChestScript.neteaseChestClientSystem.ChestClientSystem"
ServerSystemName = "neteaseChestDev"
ServerSystemClsPath = "neteaseChestScript.neteaseChestServerSystem.ChestServerSystem"
MasterSystemName = "neteaseChestMaster"
MasterSystemClsPath = "neteaseChestScript.neteaseChestMasterSystem.ChestMasterSystem"
# ===========================================================================================
import server.extraServerApi as serverApi
_serverModSystem = None
def GetServerModSystem():
	"""
	获取服务端系统，全局一个单例。
	"""
	global _serverModSystem
	if not _serverModSystem:
		_serverModSystem = serverApi.GetSystem(ModNameSpace, ServerSystemName)
	return _serverModSystem

def Destroy():
	global _serverModSystem
	_serverModSystem = None
	

#================================一些事件
UiInitFinishedEvent = 'UiInitFinished'
ShowApplicationTipsFromServerEvent = "ShowApplicationTipsFromServerEvent"
ApplicateFromClientEvent = "ApplicateFromClientEvent"
ShowChestManageFromServerEvent = "ShowChestManageFromServerEvent"
ShowTipsFromServerEvent = "ShowTipsFromServerEvent"
DeletUserFromClientEvent = "DeletUserFromClientEvent"
AcceptUserFromClientEvent = "AcceptUserFromClientEvent"
RefuseUserFromClientEvent = "RefuseUserFromClientEvent"
ChangeChestAuthFromMasterEvent = "ChangeChestAuthFromMasterEvent"

#返回码，和返回消息
#返回码，和返回消息
ResponseText = {}
CodeSuc = 0
ResponseText[CodeSuc] = "成功!"

CodeParamError = 1
ResponseText[CodeParamError] = "参数错误"

CidNotExist = 1
ResponseText[CidNotExist] = "箱子id不存在"

DbError = 2
ResponseText[DbError] = "数据库错误"

PlayerNotExist = 3
ResponseText[PlayerNotExist] = "玩家不在线"

UserNumLimit = 4
ResponseText[UserNumLimit] = "使用者到达上限"

BoxMoved = 5
ResponseText[BoxMoved] = "容器被移动了！操作失败！"