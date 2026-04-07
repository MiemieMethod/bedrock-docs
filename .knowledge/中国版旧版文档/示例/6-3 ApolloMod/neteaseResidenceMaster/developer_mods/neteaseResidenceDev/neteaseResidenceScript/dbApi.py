# -*- coding: utf-8 -*-
import json
import apolloCommon.mysqlPool as mysqlPool
from neteaseResidenceScript.residenceConsts import FetchLimitOnce

def Init():
	mysqlPool.InitDB(30)

# 获取本服务器全部的领地信息，同步阻塞执行
def QueryAllServerResidence(serverType):
	result = []
	minId = 0
	while True:
		sql = 'SELECT resId, dimension, area, name, resLevel, parentResId, authority, bornPos FROM neteaseResidence WHERE serverType=%s AND resId>%s ORDER BY resId LIMIT %s'
		params = (serverType, minId, FetchLimitOnce)
		records = mysqlPool.SyncFetchAll(sql, params)
		if not records:
			break
		result.extend(records)
		minId = records[-1][0]
	return result

# 查询某个玩家在整个服务器组的领地信息
def QueryPlayerResidence(uid, cb):
	sql = "SELECT A.resId, A.name, A.serverType, A.resLevel FROM neteaseResidence as A, neteasePlayerResidence as B \
WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = %s"
	params = (uid, )
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询指定领地的尚未处理的外部玩家权限申请
def QueryOutPlayerResidenceApplication(uid, serverType, cb):
	sql = "SELECT _id, resId, authority FROM neteaseOutPlayerResidenceApplication WHERE uid=%s AND serverType=%s"
	params = (uid, serverType)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 删除指定uid玩家针对指定领地的特殊权限申请	
def DeleteOutPlayerResidenceApplication(uid, resIdList, cb=None):
	sql = "DELETE FROM neteaseOutPlayerResidenceApplication WHERE uid=%s AND resId=%s"
	paramsList = []
	for resId in resIdList:
		paramsList.append((uid, resId))
	mysqlPool.AsyncExecutemanyWithOrderKey("global", sql, paramsList, cb)

# 插入一条外部玩家申请领地特殊权限的记录	
def InsertOutPlayerResidenceApplication(serverType, uid, resId, authority, cb=None):
	sql = "INSERT INTO neteaseOutPlayerResidenceApplication (resId, serverType, uid, authority) VALUES (%s, %s, %s, %s)"
	params = (resId, serverType, uid, json.dumps(authority, ensure_ascii=False))
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)
	
# 查询玩家在本服务器进程的特殊权限限制，lobby/game用
def QueryPlayerResidenceAuthority(uid, serverType, cb):
	sql = "SELECT _id, resId, authority FROM neteaseOutPlayerResidenceAuthority WHERE uid=%s AND serverType=%s"
	params = (uid, serverType)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询某个玩家在整个服务器组的领地信息，master用
def QueryResidenceByUid(uid, cb=None):
	sql = 'SELECT A.resId, A.name, A.serverType, A.dimension, A.area, A.bornPos, A.resLevel, A.parentResId, A.authority FROM neteaseResidence as A, neteasePlayerResidence as B \
WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = %s'
	params = (uid, )
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询指定Id的领地的信息，master用
def QueryResidenceById(id, serverType, cb=None):
	sql = 'SELECT resId, serverType FROM neteaseResidence WHERE resId = %s and serverType = %s'
	params = (id, serverType)
	mysqlPool.AsyncQueryWithOrderKey("res%s" % id, sql, params, cb)

# 创建一个新的领地，参数uid是用于保序的key
def CreateNewResidence(uid, resId, serverType, name, dimension, area, bornPos, resLevel, parentResId, cb=None):
	sql = "INSERT INTO neteaseResidence (resId, serverType, name, dimension, area, bornPos, resLevel, parentResId, authority) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	params = (resId, serverType, name, dimension, area, bornPos, resLevel, parentResId, json.dumps({}, ensure_ascii=False))
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)

# 给已经存在的领地新增一个所有者
def AddPlayerToResidence(uid, resId, serverType, cb=None):
	sql = "INSERT INTO neteasePlayerResidence (resId, serverType, uid) \
VALUES (%s, %s, %s)"
	params = (resId, serverType, uid)
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)

# 删除指定的领地
def DeleteResidence(serverType, resIdList, cb=None):
	sql = "DELETE FROM neteaseResidence WHERE serverType=%s AND resId=%s"
	paramsList = []
	for resId in resIdList:
		paramsList.append((serverType, resId))
	mysqlPool.AsyncExecutemanyWithOrderKey("global", sql, paramsList, cb)

# 删除指令领地所有者信息(只有零级领地有所有者)
def DeletePlayerResidence(serverType, resId, cb=None):
	sql = "DELETE FROM neteasePlayerResidence WHERE serverType=%s AND resId=%s"
	params = (serverType, resId)
	mysqlPool.AsyncExecuteWithOrderKey("global", sql, params, cb)

# 删除领地外部玩家特殊权限设置
def DeleteOutPlayerAuthority(serverType, resIdList, cb=None):
	sql = "DELETE FROM neteaseOutPlayerResidenceAuthority WHERE serverType=%s AND resId=%s"
	paramsList = []
	for resId in resIdList:
		paramsList.append((serverType, resId))
	mysqlPool.AsyncExecutemanyWithOrderKey("global", sql, paramsList, cb)

# 把一个玩家从领地所有者中删除
def RemovePlayerFromResidence(serverType, uid, resId, cb=None):
	sql = 'DELETE FROM neteasePlayerResidence WHERE uid=%s AND resId=%s AND serverType=%s'
	params = (uid, resId, serverType)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)

# 修改领地的权限设置
def ChangeResidenceAuthority(serverType, resId, authority, cb=None):
	sql = "UPDATE neteaseResidence SET authority = %s WHERE serverType=%s AND resId=%s"
	params = (json.dumps(authority, ensure_ascii=False), serverType, resId)
	mysqlPool.AsyncExecuteWithOrderKey("res%s" % resId, sql, params, cb)

# 修改领地的传送点
def ChangeResidenceTeleportPos(serverType, resId, posStr, cb=None):
	sql = "UPDATE neteaseResidence SET bornPos = %s WHERE serverType=%s AND resId=%s"
	params = (posStr, serverType, resId)
	mysqlPool.AsyncExecuteWithOrderKey("res%s" % resId, sql, params, cb)

# 新增领地外部玩家特殊权限设置
def InsertOutPlayerResidenceAuthority(serverType, uid, resId, authority, cb=None):
	sql = "INSERT INTO neteaseOutPlayerResidenceAuthority (resId, serverType, uid, authority) VALUES (%s, %s, %s, %s)"
	params = (resId, serverType, uid, json.dumps(authority, ensure_ascii=False))
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)

# 修改领地外部玩家特殊权限设置
def UpdateOutPlayerResidenceAuthority(serverType, uid, resId, authority, cb=None):
	sql = "UPDATE neteaseOutPlayerResidenceAuthority SET authority=%s WHERE serverType=%s AND resId=%s AND uid=%s"
	params = (json.dumps(authority, ensure_ascii=False), serverType, resId, uid)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询指定领地的全部玩家id
def QueryAllOwnersByResId(serverType, resId, cb=None):
	sql = "SELECT uid FROM neteasePlayerResidence WHERE serverType=%s AND resId=%s"
	params = (serverType, resId)
	mysqlPool.AsyncQueryWithOrderKey("res%s" % id, sql, params, cb)

def Destroy():
	mysqlPool.Finish()
