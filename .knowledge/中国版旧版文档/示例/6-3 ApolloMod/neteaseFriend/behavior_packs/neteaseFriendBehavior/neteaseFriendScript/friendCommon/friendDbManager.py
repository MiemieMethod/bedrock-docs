# -*- coding: utf-8 -*-
import time
import timer
import logout
import apolloCommon.mysqlPool as mysqlPool
import neteaseFriendScript.friendCommon.friendData as friendData

class FriendDbManager(object):
	LOBBY_CACHE_TIME = 600

	def __init__(self):
		self.mFriends = {}
		import random
		# avoid all gc in the same time
		randTime = random.randint(1, self.LOBBY_CACHE_TIME)
		self.gcCacheTimer = timer.TimerManager.addTimer(randTime, self.StartGcCache)
		self.InitMysqlDb()
		
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_Friend fail when init mysql")
			return False
		return True
		
	def Destroy(self):
		self.mFriends.clear()
		if self.gcCacheTimer:
			self.gcCacheTimer.cancel()
			self.gcCacheTimer = None

	def StartGcCache(self):
		self.GcCache()
		self.gcCacheTimer = timer.TimerManager.addRepeatTimer(self.LOBBY_CACHE_TIME, self.GcCache)

	def GcCache(self):
		tempFriends = {}
		now = time.time()
		for uid, friendData in self.mFriends.iteritems():
			if friendData.GetLastUpdateTimestamp() + self.LOBBY_CACHE_TIME > now:
				tempFriends[uid] = friendData
		self.mFriends = tempFriends
		logout.info("gc_cache friend length=%s"%len(self.mFriends))
		
	def getFriendData(self, uid):
		return self.mFriends.get(uid, None)
	
	#======好友部分数据库操作
	def ServiceQueryFriendShip(self, uids, callback, params):
		'''
		service查找好友。service 是如果内存有就不需要查db
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetFriends() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendShip WHERE uid in %s'
		sqlparam = (needQueryIds, )
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.ServiceQueryFriendShipCallBack(args, callback, params))
	
	def ServiceQueryFriendShipCallBack(self, args, callback, params):
		for data in args:
			if data:
				uid = data[0] #mysql读出来是元组的形式
				fuid = data[1]
				isRNFriend  = data[2]
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddFriend(fuid)
					if isRNFriend:
						friend.AddRNFriend(fuid)
					self.mFriends[uid] = friend
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddFriend(fuid)
					if isRNFriend:
						self.getFriendData(uid).AddRNFriend(fuid)
		callback(params)
		
	def ServiceInsertFriendShip(self, uid, fuid, isRNFriend, callback = None):
		'''
		插入好友关系
		'''
		currentTime = time.time()
		sql = 'INSERT INTO neteaseFriendShip(uid, fuid, isRNFriend, time) VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE isRNFriend = %s, time = %s'
		sqlparam = (uid, fuid,isRNFriend,currentTime, isRNFriend, currentTime, )
		def ServiceInsertFriendShipCb(args, callback):
			logout.verbose("friend change in database uid=%s" % uid)
			if args is None:
				logout.error("[FRIEND] SAVE FRIEND DATA FOR [%d] FAIL" % uid)
			#logout.info("ServiceInsertFriendShip test test", self.getFriendData(uid).GetFriends())
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam, lambda args: ServiceInsertFriendShipCb(args, callback))
		
	def ServiceDeleteFriendShip(self,uid, fuid, callback = None):
		'''
		删除好友关系
		'''
		sql = 'DELETE FROM neteaseFriendShip WHERE uid = %s AND fuid = %s'
		sqlparam = (uid, fuid, )
		def ServiceDeleteFriendShipCb(args, callback):
			logout.verbose("friend delete in database uid=%s fuid=%s" % (uid,fuid))
			if args is None:
				logout.error("[FRIEND] DELETE FRIEND DATA FOR [%d] FAIL" % uid)
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam, lambda args: ServiceDeleteFriendShipCb(args, callback))
		
	def ServiceUpdateFriendShip(self, uid, fuids, isRNFriend, callback = None):
		sql = 'Update neteaseFriendShip SET isRNFriend = %s where (uid = %s and fuid in %s) or (uid in %s and fuid = %s)'
		sqlparam = (isRNFriend, uid, fuids, fuids, uid, )
		def ServiceUpdateFriendShipCb(args, callback):
			logout.verbose("friend change in database uid=%s" % uid)
			if args is None:
				logout.error("[FRIEND] SAVE FRIEND DATA FOR [%d] FAIL" % uid)
			#logout.info("ServiceUpdateFriendShipCb test test", self.getFriendData(uid).GetFriends())
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid]), sql, sqlparam, lambda args: ServiceUpdateFriendShipCb(args, callback))
		
	def ServerGetFriendShip(self, uid, useCache, callback, params):
		'''
		lobby/game 查找好友,lobby/game是直接从db取数据，不管现在有什么
		'''
		if useCache:
			friend = self.getFriendData(uid)
			if friend and friend.GetFriends() is not None:
				callback(friend.GetFriends(), params)
				return
		sql = 'SELECT * From neteaseFriendShip WHERE uid = %s'
		sqlparam = (uid, )
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetFriendShipCallBack(uid, args, callback, params))
		
	def ServerGetFriendShipCallBack(self, uid, args, callback, params):
		if self.getFriendData(uid) is None:
			friend = friendData.CFriendData()
			friend.SetUid(uid)
			self.mFriends[uid] = friend
		temp_friend_list = []
		temp_RNfriend = set()
		for data in args:
			if data:
				#uid = data[0] #mysql读出来是元组的形式
				fuid = data[1]
				isRNFriend = data[2]
				logout.info("isRNFriendaaaaaaaaaa", isRNFriend)
				if isRNFriend:
					logout.info("isRNFriendbbbbbbbbbb", isRNFriend, fuid)
					temp_RNfriend.add(fuid)
				temp_friend_list.append(fuid)
		self.mFriends[uid].SetFriends(temp_friend_list)
		self.mFriends[uid].SetRNFriend(temp_RNfriend)
		logout.info("ServerGetFriendShipCallBack", self.mFriends[uid].GetFriends())
		callback(self.mFriends[uid].GetFriends(), params)
	
	def ServerGetRNFriendShip(self, uid, callback, params):
		'''
		lobby/game 查找好友,lobby/game是直接从db取数据，不管现在有什么
		'''
		sql = 'SELECT * From neteaseFriendShip WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetRNFriendShipCallBack(uid, args, callback, params))
	
	def ServerGetRNFriendShipCallBack(self, uid, args, callback, params):
		if self.getFriendData(uid) is None:
			friend = friendData.CFriendData()
			friend.SetUid(uid)
			self.mFriends[uid] = friend
		temp_friend_list = []
		temp_RNfriend = set()
		for data in args:
			if data:
				# uid = data[0] #mysql读出来是元组的形式
				fuid = data[1]
				isRNFriend = data[2]
				logout.info("isRNFriendtttttt", isRNFriend)
				if isRNFriend:
					logout.info("isRNFriendooooo", isRNFriend, fuid)
					temp_RNfriend.add(fuid)
				temp_friend_list.append(fuid)
		self.mFriends[uid].SetFriends(temp_friend_list)
		self.mFriends[uid].SetRNFriend(temp_RNfriend)
		logout.info("ServerGetRNFriendShipCallBack", self.mFriends[uid].GetRNFriend())
		callback(self.mFriends[uid].GetRNFriend(), params)
	
	#=======
	#======= 黑名单部分数据库操作
	def ServiceQueryFriendBlackList(self, uids, callback, params):
		'''
		service查找黑名单。service 是如果内存有就不需要查db
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetBlackList() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendBlack WHERE uid in %s'
		sqlparam = (needQueryIds, )
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.ServiceQueryFriendShipCallBack(args, callback, params))
	
	def ServiceQueryFriendBlackCallBack(self, args, callback, params):
		for data in args:
			if data:
				uid = data[0] #mysql读出来是元组的形式
				buid = data[1]
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddblackList(buid)
					self.mFriends[uid] = friend
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddblackList(buid)
		callback(params)
		
	def ServiceInsertFriendBlack(self, uid, buid, callback):
		'''
		插入黑名单，黑名单是单向的
		'''
		logout.verbose("ServiceInsertFriendBlack", callback)
		currentTime = time.time()
		sql = 'INSERT INTO neteaseFriendBlack(uid, buid, time) VALUES (%s,%s,%s)'
		sqlparam = (uid, buid, currentTime, )
		def ServiceInsertFriendBlackCb(args):
			logout.verbose("friend black change in database uid=%s buid=%s" % (uid,buid))
			if args is None:
				logout.error("[FRIEND] SAVE FRIEND BLACK DATA FOR [%d] FAIL" % uid)
			callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, buid]), sql, sqlparam, lambda args: ServiceInsertFriendBlackCb(args))
	
	def ServiceDeleteFriendBlack(self, uid, buid, callback):
		'''
		删除好友关系
		'''
		sql = 'DELETE FROM neteaseFriendBlack WHERE uid = %s AND buid = %s'
		sqlparam = (uid, buid, )
		def ServiceDeleteFriendBlackCb(args):
			logout.verbose("friend delete in database uid=%s fuid=%s" % (uid, buid))
			if args is None:
				logout.error("[FRIEND] DELETE FRIEND DATA FOR [%d] FAIL" % uid)
			callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, buid]), sql, sqlparam, lambda args: ServiceDeleteFriendBlackCb(args))
	
	def ServerGetFriendBlack(self, uid, useCache, callback, params):
		'''
		lobby/game 查找好友,lobby/game是直接从db取数据，不管现在有什么
		'''
		logout.info("ServerGetFriendBlackCallBack1",  uid, useCache, callback, params)
		if useCache:
			friend = self.getFriendData(uid)
			if friend and friend.GetBlackList() is not None:
				callback(friend.GetBlackList(), params)
				return
		sql = 'SELECT * From neteaseFriendBlack WHERE uid = %s'
		sqlparam = (uid,)
		logout.info("ServerGetFriendBlackCallBack2", uid, useCache, callback, params)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetFriendBlackCallBack(uid, args, callback, params))
		
	def ServerGetFriendBlackCallBack(self, uid, args, callback, params):
		logout.info("ServerGetFriendBlackCallBack", uid, args, callback, params)
		if self.getFriendData(uid) is None:
			friend = friendData.CFriendData()
			friend.SetUid(uid)
			self.mFriends[uid] = friend
		temp_black_list = []
		for data in args:
			if data:
				#uid = data[0] #mysql读出来是元组的形式
				buid = data[1]
				temp_black_list.append(buid)
		self.mFriends[uid].SetBlackList(temp_black_list)
		logout.info("ServerGetFriendBlackCallBack", self.mFriends[uid].GetBlackList())
		callback(self.mFriends[uid].GetBlackList(), params)
		
	#=======
	#======= 申请列表部分数据库操作
	def ServiceQueryFriendRequest(self, uids, callback, params):
		'''
		service查找申请列表。service 是如果内存有就不需要查db
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetFriendRequests() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendApply WHERE uid in %s'
		sqlparam = (needQueryIds,)
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.ServiceQueryFriendRequestCallBack(args, callback, params))
		
	def ServiceQueryFriendRequestCallBack(self, args, callback, params):
		for data in args:
			if data:
				uid = data[0] #mysql读出来是元组的形式
				auid = data[1]
				message = data[3]
				request = self.RequestToDict(uid, auid, message)
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddFriendRequest(request)
					self.mFriends[uid] = friend
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddFriendRequest(request)
		callback(params)
		
	def ServiceInsertFriendRequest(self, requestDict, callback = None):
		uid = requestDict.get("uid")
		auid = requestDict.get("auid")
		message = requestDict.get("message")
		currentTime = time.time()
		request = self.RequestToDict(uid, auid, message)
		sql = 'INSERT INTO neteaseFriendApply(uid, auid, message,time) VALUES (%s,%s,%s,%s)'
		sqlparam = (uid, auid, message, currentTime,)
		def ServiceInsertFriendRequestCb(args, callback):
			logout.verbose("friend request change in database uid=%s auid=%s" % (uid, auid))
			if args is None:
				logout.error("[FRIEND] SAVE FRIEND REQUEST DATA FOR [%d] FAIL" % uid)
			# else:
			# 	#成功了，也插入内存里
			# 	if self.getFriendData(uid) is None:
			# 		friend = friendData.CFriendData()
			# 		friend.SetUid(uid)
			# 		friend.AddFriendRequest(request)
			# 		self.mFriends[uid] = friend
			# 	else:
			# 		self.getFriendData(uid).SetUid(uid)
			# 		self.getFriendData(uid).AddFriendRequest(request)
			logout.info("ServiceInsertFriendRequestCb test test", self.getFriendData(uid).GetFriendRequests())
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, auid]), sql, sqlparam, lambda args: ServiceInsertFriendRequestCb(args, callback))
		
	def ServiceDeleteFriendRequest(self, uid, auid, callback):
		'''
		删除申请关系
		'''
		sql = 'DELETE FROM neteaseFriendApply WHERE uid = %s AND auid = %s'
		sqlparam = (uid, auid,)
		def ServiceDeleteFriendRequestCb(args, callback):
			logout.verbose("friend request delete in database uid=%s auid=%s" % (uid, auid))
			if args is None:
				logout.error("[FRIEND] DELETE FRIEND REQUEST DATA FOR [%d] FAIL" % uid)
			callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, auid]), sql, sqlparam, lambda args: ServiceDeleteFriendRequestCb(args, callback))
		
	def ServerGetFriendRequest(self, uid, useCache, callback, params):
		'''
		lobby/game 查找申请,lobby/game是直接从db取数据，不管现在有什么
		'''
		if useCache:
			friend = self.getFriendData(uid)
			if friend and friend.GetFriendRequests() is not None:
				callback(friend.GetFriendRequests(), params)
				return
		sql = 'SELECT * From neteaseFriendApply WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetFriendRequestCallBack(uid, args, callback, params))
	
	def ServerGetFriendRequestCallBack(self, uid, args, callback, params):
		if self.getFriendData(uid) is None:
			friend = friendData.CFriendData()
			friend.SetUid(uid)
			self.mFriends[uid] = friend
		temp_friend_request = {}
		for data in args:
			if data:
				#uid = data[0] #mysql读出来是元组的形式
				auid = data[1]
				message = data[3]
				request = self.RequestToDict(uid, auid, message)
				temp_friend_request[auid] = request
		self.mFriends[uid].SetRequest(temp_friend_request)
		logout.info("ServerGetFriendRequestCallBack", self.mFriends[uid].GetFriendRequests())
		callback(self.mFriends[uid].GetFriendRequests(), params)
	
	def RequestToDict(self, uid, auid, message):
		dict = {}
		dict["uid"] = uid
		dict["auid"] = auid
		dict["message"] = message
		return dict
	
	def PrepareFriendData(self, uids, callback, params):
		'''
		从db读出数据到内存
		'''
		def getRequest(params):
			self.ServiceQueryFriendRequest(uids, callback, params)
		def getBlack(params):
			self.ServiceQueryFriendBlackList(uids, getRequest, params)
		self.ServiceQueryFriendShip(uids, getBlack, params)
		
	def ServerPrePareData(self, uid, callback, params):
		def getUnRead(a,params):
			self.ServerGetUnread(uid, False, callback, params)
		def getBlack(a,params):
			self.ServerGetFriendBlack(uid, False, getUnRead, params)
		def getRequest(a,params):
			self.ServerGetFriendRequest(uid, False, getBlack, params)
		self.ServerGetFriendShip(uid, False, getRequest, params)

	# =======
	# ======= 未读消息数据库操作
	def ServiceQueryUnReadList(self, uids, callback, params):
		'''
		service查找未读消息好友。service 是如果内存有就不需要查db
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetUnReadFriendList() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendUnread WHERE uid in %s'
		sqlparam = (needQueryIds,)
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam,
										 lambda args: self.ServiceQueryUnreadListCallBack(args, callback, params))

	def ServiceQueryUnreadListCallBack(self, args, callback, params):
		for data in args:
			if data:
				uid = data[0]  # mysql读出来是元组的形式
				fuid = data[1]
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddUnReadFriendList(fuid)
					self.mFriends[uid] = friend
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddUnReadFriendList(fuid)
		callback(params)

	def ServiceInsertUnread(self, uid, fuid, callback):
		'''
		插入未读
		'''
		logout.verbose("ServiceInsertUnread", callback)
		currentTime = time.time()
		sql = 'INSERT INTO neteaseFriendUnread(uid, fuid, time) VALUES (%s,%s,%s)'
		sqlparam = (uid, fuid, currentTime,)

		def ServiceInsertUnreadCb(args):
			logout.verbose("friend Unread in database uid=%s buid=%s" % (uid, fuid))
			if args is None:
				logout.error("[FRIEND] SAVE Unread FOR [%d] FAIL" % uid)
			callback()

		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam,
										 lambda args: ServiceInsertUnreadCb(args))

	def ServiceDelUnread(self, uid, fuid, callback):
		'''
		删除好友关系
		'''
		sql = 'DELETE FROM neteaseFriendUnread WHERE uid = %s AND fuid = %s'
		sqlparam = (uid, fuid,)

		def ServiceDeleteUnreadCb(args):
			logout.verbose("friend delete in database uid=%s fuid=%s" % (uid, fuid))
			if args is None:
				logout.error("[FRIEND] DELETE FRIEND DATA FOR [%d] FAIL" % fuid)
			callback()

		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam,
										 lambda args: ServiceDeleteUnreadCb(args))

	def ServerGetUnread(self, uid, useCache, callback, params):
		'''
		lobby/game 未读,lobby/game是直接从db取数据，不管现在有什么
		'''
		logout.info("ServerGetUnread", uid, useCache, callback, params)
		if useCache:
			friend = self.getFriendData(uid)
			if friend and friend.GetUnReadFriendList() is not None:
				callback(friend.GetUnReadFriendList(), params)
				return
		sql = 'SELECT * From neteaseFriendUnread WHERE uid = %s'
		sqlparam = (uid,)
		logout.info("ServerGetUnread", uid, useCache, callback, params)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam,
										 lambda args: self.ServerGetUnreadCallBack(uid, args, callback, params))

	def ServerGetUnreadCallBack(self, uid, args, callback, params):
		logout.info("ServerGetUnreadCallBack", uid, args, callback, params)
		if self.getFriendData(uid) is None:
			friend = friendData.CFriendData()
			friend.SetUid(uid)
			self.mFriends[uid] = friend
		temp_unread_list = []
		for data in args:
			if data:
				# uid = data[0] #mysql读出来是元组的形式
				fuid = data[1]
				temp_unread_list.append(fuid)
		self.mFriends[uid].SetUnReadFriend(temp_unread_list)
		logout.info("ServerGetUnreadCallBack", self.mFriends[uid].GetUnReadFriendList())
		callback(self.mFriends[uid].GetUnReadFriendList(), params)
			
		