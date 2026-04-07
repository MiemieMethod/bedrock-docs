# -*- coding: utf-8 -*-
import json
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
from mod_log import engine_logger as logger
from neteaseResidenceScript.residenceConsts import FetchLimitOnce



def Init():
	mysqlPool.InitDB(30)
	redisPool.InitDB(20)

# 获取玩家全局领地操作锁
def TryGetPlayerActionLock(conn, uid):
	keyword = "resLock%s" % uid
	suc = conn.setnx(keyword, 1)
	conn.expire(keyword, 60)
	return suc

def GetPlayerResidenceActionLock(uid, cbFunc):
	redisPool.AsyncFuncWithKey(TryGetPlayerActionLock, "user%s" % uid, cbFunc, uid)

# 释放玩家全局领地操作锁
def TryReleasePlayerActionLock(conn, uid):
	keyword = "resLock%s" % uid
	suc = conn.delete(keyword)
	return suc

def ReleasePlayerResideneActionLock(uid, repeat=0):
	cbFunc = lambda suc:ReleasePlayerResideneActionLockCallback(suc, uid, repeat)
	redisPool.AsyncFuncWithKey(TryReleasePlayerActionLock, "user%s" % uid, cbFunc, uid)

def ReleasePlayerResideneActionLockCallback(suc, uid, repeat):
	if suc:
		return
	if repeat <= 2:
		ReleasePlayerResideneActionLock(uid, repeat+1)
	else:
		logger.error("ReleasePlayerResideneActionLock for {} fail".format(uid))

# 申请可用的领地ID第一步，查询当前用到的最大领地ID
def QueryMaxUsedResidenceId(cbFunc):
	sql = "SELECT askIndex, usedResId FROM neteaseResidenceUniqueId ORDER BY askIndex DESC LIMIT 1"
	params = ()
	def callback(records):
		if records is None:
			cbFunc(False, None, None)
			return
		if not records:
			cbFunc(True, None, None)
			return
		askIndex, usedResId = records[0][0], records[0][1]
		cbFunc(True, usedResId, askIndex)
	mysqlPool.AsyncQueryWithOrderKey("queryResId", sql, params, callback)

# 申请可用领地ID的第二步，插入新的记录
def InsertMaxUsedResidenceId(usedResId, askIndexOld, cbFunc):
	askIndexNew = askIndexOld + 1
	sql = "INSERT INTO neteaseResidenceUniqueId (askIndex, usedResId) VALUES (%s, %s)"
	params = (askIndexNew, usedResId)
	mysqlPool.AsyncExecuteWithOrderKey("queryResId", sql, params, cbFunc)

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

# 查询某个玩家在整个服务器组的领地信息，lobby/game用
def QueryPlayerResidence(uid, cb):
	sql = "SELECT A.resId, A.name, A.serverType, A.resLevel FROM neteaseResidence as A, neteasePlayerResidence as B \
WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = %s"
	params = (uid,)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)
	
# def QueryPlayerResidenceByResId(uid, resId, cb):
# 	sql = "SELECT A.resId, A.name, A.serverType, A.resLevel FROM neteaseResidence as A, neteasePlayerResidence as B \
# WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = %s AND A.resId = %s"
# 	params = (uid,resId,)
# 	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询指定ID列表中的领地的快照信息和所有者昵称
def QueryPlayerResidenceByResId(resIdList, cb):
	sql = "SELECT A.resId, A.name, A.serverType, A.resLevel, B.uid, C.username FROM neteaseResidence as A, neteasePlayerResidence as B, \
neteaseResidencePlayerData as C WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = C.uid AND B.resId in %s"
	params = (resIdList,)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % str(resIdList), sql, params, cb)


# 查询指定领地的尚未处理的外部玩家权限申请
def QueryOutPlayerResidenceApplication(resId, serverType, cb):
	sql = "SELECT _id, uid, resId, authority FROM neteaseOutPlayerResidenceApplication WHERE resId=%s and serverType=%s"
	params = (resId, serverType)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % resId, sql, params, cb)

# 查询指定服务器全部领地的所有尚未处理的外部玩家权限申请
def QueryAllOutPlayerResidenceApplication(serverType):
	result = []
	minId = 0
	while True:
		#sql = 'SELECT resId, dimension, area, name, resLevel, parentResId, authority, bornPos FROM neteaseResidence WHERE serverType=%s AND resId>%s ORDER BY resId LIMIT %s'
		sql = "SELECT _id, uid, resId, applicationMessage, authority, userName FROM neteaseOutPlayerResidenceApplication WHERE serverType=%s AND _id>%s ORDER BY _id LIMIT %s"
		params = (serverType, minId, FetchLimitOnce)
		records = mysqlPool.SyncFetchAll(sql, params)
		if not records:
			break
		result.extend(records)
		minId = records[-1][0]
	return result

# 查询玩家在本服务器进程的特殊权限限制，lobby/game用
def QueryAllOutPlayerResidenceMainAuthority(serverType):
	result = []
	minId = 0
	while True:
		# sql = 'SELECT resId, dimension, area, name, resLevel, parentResId, authority, bornPos FROM neteaseResidence WHERE serverType=%s AND resId>%s ORDER BY resId LIMIT %s'
		sql = "SELECT _id, uid, resId, mainAuth, userName FROM neteaseOutPlayerResidenceMainAuth WHERE serverType=%s AND _id>%s ORDER BY _id LIMIT %s"
		params = (serverType, minId, FetchLimitOnce)
		records = mysqlPool.SyncFetchAll(sql, params)
		if not records:
			break
		result.extend(records)
		minId = records[-1][0]
	return result
	# sql = "SELECT _id, resId, authority FROM neteaseOutPlayerResidenceAuthority WHERE uid=%s AND serverType=%s"
	# params = (uid, serverType)
	# mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 删除指定uid玩家针对指定领地的特殊权限申请
def DeleteOutPlayerResidenceApplication(uid, resId, cb=None):
	sql = "DELETE FROM neteaseOutPlayerResidenceApplication WHERE uid=%s AND resId=%s"
	params = (uid, resId)
	mysqlPool.AsyncQueryWithOrderKey("global", sql, params, cb)

# 插入一条外部玩家申请领地特殊权限的记录
def InsertOutPlayerResidenceApplication(serverType, uid, resId, applicationMessage, userName, authority, cb=None):
	sql = "INSERT INTO neteaseOutPlayerResidenceApplication (resId, serverType, uid, applicationMessage, authority, username) VALUES (%s, %s, %s, %s, %s, %s)"
	params = (resId, serverType, uid, applicationMessage, json.dumps(authority, ensure_ascii=False), userName)
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)
	

# 查询玩家在本服务器进程的特殊权限限制
def QueryPlayerResidenceAuthority(uid, serverType, cb = None):
	sql = "SELECT _id, resId, authority FROM neteaseOutPlayerResidenceAuthority WHERE uid=%s AND serverType=%s"
	params = (uid, serverType)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)

# 查询指定玩家的个人信息	
def QueryPlayerDataByUid(uid, callback = None):
	sql = 'SELECT * From neteaseResidencePlayerData WHERE uid = %s'
	sqlparam = (uid,)
	mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, callback)

# 根据昵称查询对应玩家的个人信息	
def QueryPlayerDataByUserName(username, callback = None):
	sql = 'SELECT * From neteaseResidencePlayerData WHERE username = %s'
	sqlparam = (username,)
	mysqlPool.AsyncQueryWithOrderKey(username, sql, sqlparam, callback)

# 插入一条玩家个人信息记录	
def InSertPlayerData(playerDict, callback = None):
	sql = "INSERT INTO neteaseResidencePlayerData(uid, username)VALUES(%s, %s) ON DUPLICATE KEY UPDATE username = %s"
	sqlparam = (playerDict.get("uid"), playerDict.get("username"), playerDict.get("username"), )
	mysqlPool.AsyncQueryWithOrderKey(str(playerDict), sql, sqlparam, callback)

# 插入一条领地传送申请未读提示记录
def InSertTransferUnread(uid, resId, cb = None):
	sql = "INSERT INTO neteaseResidenceTransferUnread(uid, resId)VALUES(%s, %s)"
	sqlparam = (uid, resId,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)

# 插入一条外部玩家申请特殊权限未读提示记录	
def InSertApplicationUnread(uid, resId, applicatorUid, cb = None):
	sql = "INSERT INTO neteaseResidenceApplicationUnread(uid, resId, applicatorUid)VALUES(%s, %s)"
	sqlparam = (uid, resId, applicatorUid,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)

# 查询指定玩家的所有领地传送申请未读提示	
def QueryTransferUnread(uid, cb = None):
	sql = "SELECT * FROM neteaseResidenceTransferUnread WHERE uid = %s"
	sqlparam = (uid,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)

# 查询指定玩家的所有特殊权限申请未读提示	
def QueryApplicationUnread(uid, cb = None):
	sql = "SELECT * FROM neteaseResidenceApplicationUnread WHERE uid = %s"
	sqlparam = (uid,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)

# 删除指定玩家的领地传送申请未读提示（等价于标识为已读）	
def DeleteTransferUnread(uid, cb = None):
	sql = "DELETE FROM neteaseResidenceTransferUnread WHERE uid = %s"
	sqlparam = (uid,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)

# 删除指定玩家的特殊权限申请未读提示（等价于标识为已读）	
def DeleteApplicationUnread(uid, resId, cb= None):
	sql = "DELETE FROM neteaseResidenceApplicationUnread WHERE uid = %s AND resId = %s"
	sqlparam = (uid,resId,)
	mysqlPool.AsyncQueryWithOrderKey(uid, sql, sqlparam, cb)


# 查询某个玩家在整个服务器组的领地信息
def QueryResidenceByUid(uid, cb=None):
	sql = 'SELECT A.resId, A.name, A.serverType, A.dimension, A.area, A.bornPos, A.resLevel, A.parentResId, A.authority FROM neteaseResidence as A, neteasePlayerResidence as B \
WHERE A.resId = B.resId And A.serverType = B.serverType AND B.uid = %s'
	params = (uid,)
	mysqlPool.AsyncQueryWithOrderKey("pl%s" % uid, sql, params, cb)
	
# 查询某个玩家在整个服务器组的领地信息
def QueryPlayerResidenceMainAuthByUid(uid, cb=None):
	sql = 'SELECT A.resId, A.name, A.serverType, A.dimension, A.area, A.bornPos,B.userName,C.mainAuth FROM neteaseResidence as A, neteasePlayerResidence as B, \
neteaseOutPlayerResidenceMainAuth as C WHERE A.resId = B.resId AND A.resId = C.resId And A.serverType = B.serverType AND A.serverType = C.serverType AND C.uid = %s'
	params = (uid,)
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
	params = (
	resId, serverType, name, dimension, area, bornPos, resLevel, parentResId, json.dumps({}, ensure_ascii=False))
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)

# 修改指定领地占据的区域	
def ChangeResidencePos(resId, serverType, area, cb = None):
	sql = "UPDATE neteaseResidence SET area = %s WHERE resId = %s AND serverType = %s"
	params = (area, resId, serverType)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % resId, sql, params, cb)


# 给已经存在的领地新增一个所有者
def AddPlayerToResidence(uid, resId, serverType, userName, cb=None):
	sql = "INSERT INTO neteasePlayerResidence (resId, serverType, uid, userName) \
VALUES (%s, %s, %s, %s)"
	params = (resId, serverType, uid, userName)
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
	
# 删除领地外部玩家特殊权限设置
def DeleteOutPlayerAuthorityByUid(serverType, resIdList, uid, cb=None):
	sql = "DELETE FROM neteaseOutPlayerResidenceAuthority WHERE serverType=%s AND resId=%s AND uid = %s"
	paramsList = []
	for resId in resIdList:
		paramsList.append((serverType, resId, uid, ))
	mysqlPool.AsyncExecutemanyWithOrderKey("global", sql, paramsList, cb)


# 把一个玩家从领地所有者中删除
def RemovePlayerFromResidence(serverType, uid, resId, cb=None):
	sql = 'DELETE FROM neteasePlayerResidence WHERE uid=%s AND resId=%s AND serverType=%s'
	params = (uid, resId, serverType)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)
	
# 修改领地权限
def ChangePlayerResidence(serverType, uid, userName, oriuid, resId, cb=None):
	sql = 'Update neteasePlayerResidence set uid = %s, userName = %s WHERE uid=%s AND resId=%s AND serverType=%s'
	params = (uid, userName, oriuid, resId, serverType)
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
	params = (resId, serverType, uid, json.dumps(authority, ensure_ascii=False),)
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)
	
# 新增领地外部玩家特殊权限设置
def InsertOutPlayerResidenceMainAuthority(serverType, uid, resId, mainAuthority, userName, cb=None):
	sql = "INSERT INTO neteaseOutPlayerResidenceMainAuth (resId, serverType, uid, mainAuth, userName) VALUES (%s, %s, %s, %s, %s)ON DUPLICATE KEY UPDATE mainAuth = %s"
	params = (resId, serverType, uid, json.dumps(mainAuthority, ensure_ascii=False), userName, json.dumps(mainAuthority, ensure_ascii=False), )
	mysqlPool.AsyncInsertOneWithOrderKey("pl%s" % uid, sql, params, cb)
	
# 新增领地外部玩家特殊权限设置
def DeleteOutPlayerResidenceMainAuthority(serverType, uid, resId, cb=None):
	sql = "DELETE FROM neteaseOutPlayerResidenceMainAuth WHERE uid = %s and resId = %s and serverType=%s"
	params = (uid, resId, serverType, )
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)

# 修改指定外部玩家在指定领地的简化版权限（即放置/摧毁方块、使用门/箱子、进入领地）
def UpdateOutPlayerResidenceMainAuthority(serverType, uid, resId, mainAuthority, cb=None):
	sql = "UPDATE neteaseOutPlayerResidenceMainAuth SET mainAuth=%s WHERE serverType=%s AND resId=%s AND uid=%s"
	params = (json.dumps(mainAuthority, ensure_ascii=False), serverType, resId, uid)
	mysqlPool.AsyncExecuteWithOrderKey("pl%s" % uid, sql, params, cb)


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
	redisPool.Finish()
