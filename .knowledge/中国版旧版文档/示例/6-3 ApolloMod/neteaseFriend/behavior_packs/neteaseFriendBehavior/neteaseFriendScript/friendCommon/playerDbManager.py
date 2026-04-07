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
		'''
		service查找玩家数据。service 是如果内存有就不需要查db
		'''
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
		
		
		
		