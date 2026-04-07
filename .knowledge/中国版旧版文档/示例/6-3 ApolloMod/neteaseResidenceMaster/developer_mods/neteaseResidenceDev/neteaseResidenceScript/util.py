# -*- coding: utf-8 -*-
"""
一些工具函数
"""
import neteaseResidenceScript.residenceConsts as residenceConsts

# 辅助函数 -- 把unicode编码的字符串、字典或列表转换成utf8编码
def UnicodeConvert(input):
	if isinstance(input, dict):
		return {UnicodeConvert(key): UnicodeConvert(value) for key, value in input.iteritems()}
	elif isinstance(input, list):
		return [UnicodeConvert(element) for element in input]
	elif isinstance(input, tuple):
		tmp = [UnicodeConvert(element) for element in input]
		return tuple(tmp)
	elif isinstance(input, unicode):
		return input.encode('utf-8')
	else:
		return input

# 把string转回坐标信息
def StringToList(str):
	lst = str.split(',')
	return [int(i) for i in lst]

# 把坐标信息转化为string
def ListToString(lst):
	strLst = [str(i) for i in lst]
	return ','.join(strLst)

# AABB包围盒信息从string转回两个坐标点的形式
def AreaStringToPos(area):
	posList = area.split(',')
	minPos = [int(posList[i]) for i in xrange(0, 3, 1)]
	maxPos = [int(posList[i]) for i in xrange(3, 6, 1)]
	return minPos, maxPos

# AABB包围盒信息，从两个坐标点形式转为string形式
def PosToAeraString(minPos, maxPos):
	return ','.join([str(i) for i in minPos]) + ',' + ','.join([str(i) for i in maxPos])

# AABB碰撞检查
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

# 某个位置坐标是否处于某个区域内（基于AABB包围盒）
def IsInArea(pos, minPos, maxPos):
	for i in xrange(3):
		if minPos[i] > pos[i] or maxPos[i] < pos[i]:
			return False
	return True

# 某个区域是否被另外一个区域完全包含（均基于AABB包围盒）
def IsSubArea(parentMinPos, parentMaxPos, minPos, maxPos):
	if IsInArea(minPos, parentMinPos, parentMaxPos) and IsInArea(maxPos, parentMinPos, parentMaxPos):
		return True
	return False

residenceSystem = None
listenEventInfo = []
def SetResidenceSystem(system):
	global residenceSystem
	residenceSystem = system

def GetResidenceSystem():
	global residenceSystem
	return residenceSystem

def GetResidenceGasMgr():
	global  residenceSystem
	return residenceSystem.GetResidenceMgr()

def GetPlayerMgr():
	global  residenceSystem
	return residenceSystem.GetPlayerMgr()

def NotifyToClient(playerId, eventName, eventData):
	global  residenceSystem
	residenceSystem.NotifyToClient(playerId, eventName, eventData)

def GetPlayerPos(playerId):
	global residenceSystem
	comp = residenceSystem.CreateComponent(playerId, "Minecraft", "pos")
	return comp.GetPos()

def GetEntityPos(entityId):
	global residenceSystem
	comp = residenceSystem.CreateComponent(entityId, "Minecraft", "pos")
	if not comp:
		return None
	return comp.GetPos()

def GetEntityDimensionId(entityId):
	global residenceSystem
	comp = residenceSystem.CreateComponent(entityId, "Minecraft", "dimension")
	if not comp:	# 领地限制主世界生效，无法获知具体维度情况下一律认为处于主世界
		return residenceConsts.DimensionIdOverWorld
	return comp.GetPlayerDimensionId()

def GetEntityIdentifier(entityId):
	global residenceSystem
	comp = residenceSystem.CreateComponent(entityId, "Minecraft", "engineType")
	if not comp:
		return residenceConsts.IdentifierAir
	return comp.GetEngineTypeStr()

def ListenClientEvent(eventName, instance, func):
	global residenceSystem, listenEventInfo
	residenceSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName, eventName,
								instance, func)
	listenArgs = (residenceConsts.ModNameSpace, residenceConsts.ClientSystemName, eventName,
				instance, func)
	listenEventInfo.append(listenArgs)

def ListenEngineEvent(eventName, instance, func):
	import server.extraServerApi as serverApi
	global residenceSystem, listenEventInfo
	residenceSystem.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), eventName,
								instance, func)
	listenArgs = (serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), eventName,
				instance, func)
	listenEventInfo.append(listenArgs)

def Destroy():
	global residenceSystem, listenEventInfo
	for args in listenEventInfo:
		residenceSystem.UnListenForEvent(*args)
	residenceSystem = None

#配置相关
_modConf = None
def LoadModConf():
	global _modConf
	import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
	_modConf = commonNetgameApi.GetModJsonConfig("neteaseResidenceScript")

def GetModConfByField(filed):
	return _modConf[filed]

def GetModJsonConfig():
	global _modConf
	return _modConf
