# -*- coding: utf-8 -*-
from neteaseMapAttrsScript.mapAttrsConsts import ModNameSpace, ClientSystemName, ServerSystemName, MasterSystemName
from neteaseMapAttrsScript.mapAttrsConsts import DimensionIdOverWorld

def StringToList(str):
	lst = str.split(',')
	return [int(i) for i in lst]

def ListToString(lst):
	strLst = [str(i) for i in lst]
	return ','.join(strLst)

def AreaStringToPos(area):
	posList = area.split(',')
	minPos = [float(posList[i]) for i in xrange(0, 3, 1)]
	maxPos = [float(posList[i]) for i in xrange(3, 6, 1)]
	return minPos, maxPos

def PosToAeraString(minPos, maxPos):
	return ','.join([str(i) for i in minPos]) + ',' + ','.join([str(i) for i in maxPos])

def AabbIntersects(vmaxA, vminA, vmaxB, vminB):
	"""
	AABB碰撞检查
	:param vmaxA:包围盒A最大坐标
	:type vmaxA:tuple
	:param vminA:包围盒A最小坐标
	:type vminA:tuple
	:param vmaxB:包围盒B最大坐标
	:type vmaxB:tuple
	:param vminB:包围盒B最小坐标
	:type vminB:tuple
	:return:
	:rtype: Bool
	"""
	if vmaxA[0] < vminB[0] or vminA[0] > vmaxB[0]:
		return False
	if vmaxA[1] < vminB[1] or vminA[1] > vmaxB[1]:
		return False
	if vmaxA[2] < vminB[2] or vminA[2] > vmaxB[2]:
		return False
	return True

def IsInArea(pos, minPos, maxPos):
	for i in xrange(3):
		if minPos[i] > pos[i] or maxPos[i] < pos[i]:
			return False
	return True

recentSystem = None
listenEventInfo = []
def SetSystem(system):
	global recentSystem
	recentSystem = system

def GetSystem():
	global recentSystem
	return recentSystem

def NotifyToClient(playerId, eventName, eventData):
	global recentSystem
	recentSystem.NotifyToClient(playerId, eventName, eventData)

def NotifyToServer(eventName, eventData):
	global  recentSystem
	recentSystem.NotifyToServer(eventName, eventData)

def GetEntityPos(entityId):
	global recentSystem
	comp = recentSystem.CreateComponent(entityId, "Minecraft", "pos")
	if not comp:
		return None
	return comp.GetPos()

def GetEntityDimensionId(entityId):
	global recentSystem
	comp = recentSystem.CreateComponent(entityId, "Minecraft", "dimension")
	if not comp:	# 领地限制主世界生效，无法获知具体维度情况下一律认为处于主世界
		return DimensionIdOverWorld
	return comp.GetEntityDimensionId()

def ListenClientEvent(eventName, instance, func):
	global recentSystem, listenEventInfo
	recentSystem.ListenForEvent(ModNameSpace, ClientSystemName, eventName, instance, func)
	listenArgs = (ModNameSpace, ClientSystemName, eventName, instance, func)
	listenEventInfo.append(listenArgs)

def ListenServerEvent(eventName, instance, func):
	global recentSystem, listenEventInfo
	recentSystem.ListenForEvent(ModNameSpace, ServerSystemName, eventName, instance, func)
	listenArgs = (ModNameSpace, ServerSystemName, eventName, instance, func)
	listenEventInfo.append(listenArgs)

def ListenMasterEvent(eventName, instance, func):
	global recentSystem, listenEventInfo
	recentSystem.ListenForEvent(ModNameSpace, MasterSystemName, eventName, instance, func)
	listenArgs = (ModNameSpace, MasterSystemName, eventName, instance, func)
	listenEventInfo.append(listenArgs)

def ListenClientEngineEvent(eventName, instance, func):
	import client.extraClientApi as extraClientApi
	global recentSystem, listenEventInfo
	recentSystem.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
								eventName, instance, func)
	listenArgs = (extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
				  eventName, instance, func)
	listenEventInfo.append(listenArgs)

def ListenServerEngineEvent(eventName, instance, func):
	import server.extraServerApi as extraServerApi
	global recentSystem, listenEventInfo
	recentSystem.ListenForEvent(extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
								eventName, instance, func)
	listenArgs = (extraServerApi.GetEngineNamespace(), extraServerApi.GetEngineSystemName(),
				  eventName, instance, func)
	listenEventInfo.append(listenArgs)

def Destroy():
	global recentSystem, listenEventInfo
	for args in listenEventInfo:
		recentSystem.UnListenForEvent(*args)
	listenEventInfo = []
	recentSystem = None

# 配置
_modConf = None
def LoadModConf():
	global _modConf
	import apolloCommon.commonNetgameApi as commonNetgameApi
	_modConf = commonNetgameApi.GetModJsonConfig("neteaseMapAttrsScript")

def GetModConfByField(field):
	global _modConf
	return _modConf[field]
