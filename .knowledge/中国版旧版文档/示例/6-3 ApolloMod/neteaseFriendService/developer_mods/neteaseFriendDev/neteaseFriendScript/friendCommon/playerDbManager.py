# -*- coding: utf-8 -*-
import time
import timer
import logout
import apolloCommon.mysqlPool as mysqlPool
import neteaseFriendScript.friendCommon.playerData as PlayerData

class PlayerDbManager(object):
	LOBBY_CACHE_TIME = 600
	
	def __init__(self):
		self.mPlayerCaches = {}
		import random
		# avoid all gc in the same time
		randTime = random.randint(1, self.LOBBY_CACHE_TIME)
		self.gcCacheTimer = timer.TimerManager.addTimer(randTime, self.StartGcCache)
	
	def Destroy(self):
		self.mPlayerCaches.clear()
		if self.gcCacheTimer:
			self.gcCacheTimer.cancel()
			self.gcCacheTimer = None
	
	def StartGcCache(self):
		self.GcCache()
		self.gcCacheTimer = timer.TimerManager.addRepeatTimer(self.LOBBY_CACHE_TIME, self.GcCache)
	
	def GcCache(self):
		"""
		定制执行，按照最后访问时间为标准，清理内存缓存中的缓存信息，防止长时间运行时内存无限增长
		"""
		tempCache = {}
		now = time.time()
		for uid, playerCache in self.mPlayerCaches.iteritems():
			if playerCache.GetLastUpdateTimestamp() + self.LOBBY_CACHE_TIME > now:
				tempCache[uid] = playerCache
		self.mPlayerCaches = tempCache
		logout.info("gc_cache player cache record length=%s" % len(self.mPlayerCaches))
		
	def getPlayerCaches(self, uid):
		return self.mPlayerCaches.get(uid, None)
		
	def QueryPlayerData(self, uid, useCache, callback):
		"""
		查询指定uid的玩家的基本信息，可指定是否优先从内存缓存中读取，实现的功能有：
		1、假如愿意优先从内存缓存中读取玩家基本信息，且内存缓存中存在对应的信息，直接调用参数中的回调函数返回
		2、否则向数据库查询指定uid的玩家的基本信息
		3、查询返回后，更新内存缓存中的聊天历史记录
		4、调用参数中的回调函数返回符合指定uid玩家的基本信息（不存在目标玩家时返回None）
		"""
		if useCache:
			player = self.getPlayerCaches(uid)
			if player and player.GetPlayerData() is not None:
				callback(player.GetPlayerData())
				return
		def QueryPlayerDataCb(uid, args, callback):
			exist = False
			for data in args:
				if data:
					exist = True
					if self.getPlayerCaches(uid) is None:
						player = PlayerData.PlayerData()
						self.mPlayerCaches[uid] = player
					self.mPlayerCaches[uid].SetPlayerData(data[0], data[1], data[2])
			if exist:
				callback(self.mPlayerCaches[uid].GetPlayerData())
			else:
				callback(None)
		sql = 'SELECT * From neteaseFriendPlayerData WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: QueryPlayerDataCb(uid, args, callback))
		
	def InSertPlayerData(self, playerDict, callback):
		"""
		向玩家基本信息数据库，插入一条新的记录，插入完成后更新内存缓存，无论是否插入成功，都会调用参数中的回调函数（插入失败后仅记录错误日志）
		"""
		sql = "INSERT INTO neteaseFriendPlayerData(uid, username, head_image)VALUES(%s, %s, %s)"
		sqlparam = (playerDict.get("uid"), playerDict.get("username"), playerDict.get("head_image"), )
		def InsertPlayerDataCb(playerDict, args, callback):
			uid = playerDict.get("uid")
			logout.info("InSertPlayerData1", args)
			if args is not None:
				if self.getPlayerCaches(uid) is None:
					player = PlayerData.PlayerData()
					player.SetPlayerData(playerDict.get("uid"), playerDict.get("username"), playerDict.get("head_image"))
					self.mPlayerCaches[uid] = player
				else:
					self.mPlayerCaches[uid].SetPlayerData(playerDict.get("uid"), playerDict.get("username"), playerDict.get("head_image"))
				logout.info("InSertPlayerData, test.test", args, self.getPlayerCaches(uid).GetPlayerData())
			else:
				logout.error("[FRIEND] INSERT PLAYER DATA FOR [%d] FAIL" % uid)
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str(playerDict), sql, sqlparam, lambda args: InsertPlayerDataCb(playerDict, args, callback))
	
	def GetPlayerDataByUserName(self, nickName, callback, params):
		"""
		查询指定昵称的玩家的基本信息，优先从内存缓存中读取，实现的功能有：
		"""
		for player in self.mPlayerCaches.itervalues():
			if player.GetNickName().encode("utf-8") == nickName:
				callback(player.GetPlayerData(), params)
				return
		def QueryPlayerDataByUserNameCb(args, callback, params):
			player = None
			for data in args:
				if data:
					uid = data[0]
					userName = data[1]
					headImage = data[2]
					if self.getPlayerCaches(uid) is None:
						player = PlayerData.PlayerData()
						self.mPlayerCaches[uid] = player
					else:
						player = self.getPlayerCaches(uid)
					player.SetPlayerData(uid, userName, headImage)
					self.mPlayerCaches[uid] = player
			callback(player.GetPlayerData() if player is not None else {}, params)
		sql = 'SELECT * From neteaseFriendPlayerData WHERE username = %s'
		sqlparam = (nickName,)
		mysqlPool.AsyncQueryWithOrderKey(str(nickName), sql, sqlparam,
		                                 lambda args: QueryPlayerDataByUserNameCb(args, callback, params))
	
	# ======批量查找好友数据库操作
	def SerciceQueryPlayerData(self, uids, callback):
		"""
		批量查询uid列表中玩家的基本信息，实现的功能有：
		1、遍历输入的uid列表，过滤掉内存中已经有基本信息缓存的uid
		2、假如所有的uid的基本信息都已经加载进内存了，直接调用参数中的回调函数
		3、否则向数据库查询过滤后的uid列表中的玩家的基本信息记录，并把结果传递给【SerciceQueryPlayerDataCallBack】函数
		"""
		needQueryIds = []
		for uid in uids:
			if self.getPlayerCaches(uid) is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback()
			return
		sql = 'SELECT * From neteaseFriendPlayerData WHERE uid in %s'
		sqlparam = (needQueryIds,)
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.SerciceQueryPlayerDataCallBack(args, callback))
	
	def SerciceQueryPlayerDataCallBack(self, args, callback):
		"""
		从数据库查询指定uid列表玩家基本信息记录后的回调函数，实现的功能有：
		1、把查询到的玩家基本信息缓存到内存中。
		2、调用参数中的回调函数
		"""
		for data in args:
			if data:
				uid = data[0]  # mysql读出来是元组的形式
				username = data[1]
				headImage = data[2]
				if self.getPlayerCaches(uid) is None:
					player = PlayerData.PlayerData()
					self.mPlayerCaches[uid] = player
				self.mPlayerCaches[uid].SetPlayerData(uid, username, headImage)
		callback()
		
	def ChangePlayerHeadImage(self, playerDict, callback):
		"""
		更新指定uid玩家的头像信息，实现的步骤：
		1、更新玩家基本信息数据库中，对应玩家的头像信息
		2、假如更新成功，同时更新内存缓存中的玩家的头像信息
		3、无论是否更新成功，都会调用参数中的回调函数（失败时仅记录错误日志）
		"""
		sql = "UPDATE neteaseFriendPlayerData SET head_image = %s WHERE uid = %s"
		sqlparam = (playerDict.get("head_image"), playerDict.get("uid"), )
		def UpdatePlayerDataCb(args, callback):
			uid = playerDict.get("uid")
			logout.info("UpdatePlayerData1", args)
			if args is not None:
				if self.getPlayerCaches(uid) is not None:
					self.mPlayerCaches[uid].SetHeadImage(playerDict.get("head_image"))
					logout.info("UpdatePlayerData1, test.test", args, self.getPlayerCaches(uid).GetPlayerData())
			else:
				logout.error("[FRIEND] UPDATE PLAYER DATA FOR [%d] FAIL" % uid)
			if callback is not None:
				callback(args)
		mysqlPool.AsyncQueryWithOrderKey(str(playerDict), sql, sqlparam, lambda args: UpdatePlayerDataCb(args, callback))
		
		
		
		