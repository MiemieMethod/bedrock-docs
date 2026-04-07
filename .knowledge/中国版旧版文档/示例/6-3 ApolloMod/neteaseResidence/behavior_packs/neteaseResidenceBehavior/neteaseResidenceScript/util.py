# -*- coding: utf-8 -*-
"""
一些工具函数
"""

import client.extraClientApi as extraClientApi
import neteaseResidenceScript.residenceConsts as residenceConsts
_clientModSystem = None

# 返回客户端系统对象
def GetClientModSystem():
	"""
	:return: neteaseFriendScript.neteaseFriendClientSystem.FriendClientSystem
	:rtype: neteaseFriendScript.neteaseFriendClientSystem.FriendClientSystem
	"""
	global _clientModSystem
	if not _clientModSystem:
		_clientModSystem = extraClientApi.GetSystem(residenceConsts.ModNameSpace, residenceConsts.ClientSystemName)
	return _clientModSystem

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

# 某个区域是否没有被另外一个区域完全包含
def IsOutArea(subMinPos, subMaxPos, minPos, maxPos):
	if IsInArea(minPos, subMinPos, subMaxPos) or IsInArea(maxPos, subMinPos, subMaxPos):
		return False
	return True

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

residenceSystem = None
listenEventInfo = []
def SetResidenceSystem(system):
	global residenceSystem
	residenceSystem = system

def GetResidenceSystem():
	global residenceSystem
	return residenceSystem

def GetResidenceGacMgr():
	global  residenceSystem
	return residenceSystem.GetResidenceMgr()

def GetPlayerGac():
	global  residenceSystem
	return residenceSystem.GetPlayerGac()

def DefineEvent(eventName):
	global residenceSystem
	residenceSystem.DefineEvent(eventName)

def NotifyToServer(eventName, eventData):
	global  residenceSystem
	residenceSystem.NotifyToServer(eventName, eventData)

def ListenServerEvent(eventName, instance, func):
	global residenceSystem, listenEventInfo
	residenceSystem.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, eventName,
								instance, func)
	listenArgs = (residenceConsts.ModNameSpace, residenceConsts.ServerSystemName, eventName,
				instance, func)
	listenEventInfo.append(listenArgs)

def ListenEngineEvent(eventName, instance, func):
	import client.extraClientApi as extraClientApi
	global residenceSystem, listenEventInfo
	residenceSystem.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(), eventName,
								instance, func)
	listenArgs = (extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(), eventName,
				instance, func)
	listenEventInfo.append(listenArgs)

def GetLocalPlayerPos():
	import client.extraClientApi as extraClientApi
	global residenceSystem
	playerId = extraClientApi.GetLocalPlayerId()
	comp = residenceSystem.CreateComponent(playerId, "Minecraft", "pos")
	pos = comp.GetPos()
	if pos:
		return pos
	else:
		return (0, 0, 0)

def Destroy():
	global _clientModSystem
	_clientModSystem = None
	global residenceSystem, listenEventInfo
	for args in listenEventInfo:
		residenceSystem.UnListenForEvent(*args)
	residenceSystem = None

#配置相关
_modConf = None
def CacheModConf(data):
	global _modConf
	_modConf = data

def GetModConfByField(filed):
	global _modConf
	if not _modConf:
		return None
	return _modConf[filed]

def GetModJsonConfig():
	global _modConf
	return _modConf


def is_number(s):
	try:
		float(s) # for int, long, float and complex
		return True
	except ValueError:
		return False