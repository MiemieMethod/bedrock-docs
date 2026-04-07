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
		"""
		定制执行，按照最后访问时间为标准，清理内存缓存中的缓存信息，防止长时间运行时内存无限增长
		"""
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
		查询指定uid列表玩家现有好友的记录的函数，实现的功能有：
		1、遍历输入的uid列表，过滤掉内存中已经有好友信息缓存的uid
		2、假如所有的uid的现有好友都已经加载进内存了，直接调用参数中的回调函数
		3、否则向数据库查询过滤后的uid列表中的玩家的好友记录，并把结果传递给【ServiceQueryFriendShipCallBack】函数
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
		"""
		从数据库查询指定uid列表玩家现有好友的记录后的回调函数，实现的功能有：
		1、把查询到的好友信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
	
	# ======好友部分数据库操作
	def ServiceQueryFriendShipNew(self, uid, callback, params):
		'''
		查询指定uid的一个玩家现有好友的记录的函数，实现的功能有：
		1、假如目标uid的玩家的现有好友已经加载进内存了，直接调用参数中的回调函数
		2、否则向数据库查询目标uid的玩家的好友记录，并把结果传递给【ServiceQueryFriendShipCallBackNew】函数
		'''
		if self.getFriendData(uid) is not None and self.getFriendData(uid).GetFriends() is not None:
			callback(self.getFriendData(uid).GetFriends(), params)
			return
		sql = 'SELECT * From neteaseFriendShip WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam,
		                                 lambda args: self.ServiceQueryFriendShipCallBackNew(args, callback, params))
	
	def ServiceQueryFriendShipCallBackNew(self, args, callback, params):
		"""
		从数据库查询指定uid的玩家现有好友的记录后的回调函数，实现的功能有：
		1、把查询到的好友信息缓存到内存中。
		2、调用参数中的回调函数
		"""
		reFriends = []
		for data in args:
			if data:
				uid = data[0]  # mysql读出来是元组的形式
				fuid = data[1]
				isRNFriend = data[2]
				reFriends.append(fuid)
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
		callback(reFriends, params)
	
	def ServiceInsertFriendShip(self, uid, fuid, isRNFriend, callback = None):
		'''
		向好友关系数据库，插入一条新的好友关系记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		
	def ServiceInsertHasSyncFriendShip(self, uid, fuid, callback = None):
		'''
		向RN好友关系转化记录数据库，插入一条好友关系已经转化完毕的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
		'''
		currentTime = time.time()
		sql = 'INSERT INTO neteaseFriendShipRNAlreadySync(uid, fuid, time) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE fuid = %s, time = %s'
		sqlparam = (uid, fuid, currentTime, fuid, currentTime, )
		def ServiceInsertHasSyncFriendShipCb(args, callback):
			logout.verbose("friend sync change in database uid=%s" % uid)
			if args is None:
				logout.error("[FRIEND] SAVE SYNC FRIEND DATA FOR [%d] FAIL" % uid)
			#logout.info("ServiceInsertFriendShip test test", self.getFriendData(uid).GetFriends())
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam, lambda args: ServiceInsertHasSyncFriendShipCb(args, callback))
		
	def ServiceDeleteFriendShip(self,uid, fuid, callback = None):
		'''
		从好友关系数据库，删除一条代表好友关系的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		"""
		更新好友关系数据库，刷新指定uid玩家的部分好友是否为RN好友的标识位，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
		"""
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
		查询指定uid的玩家的好友列表，可指定是否优先从内存缓存中读取（lobby/game用），实现的功能有：
		1、假如愿意优先从内存缓存中读取好友数据，且内存缓存中存在目标uid的好友信息，直接调用参数中的回调函数返回好友信息
		2、否则向数据库查询目标uid的玩家的好友记录，并把结果传递给【ServerGetFriendShipCallBack】函数
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
		"""
		从数据库查询指定uid的玩家现有好友的记录后的回调函数（lobby/game用），实现的功能有：
		1、把查询到的好友信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
		查询指定uid的玩家的RN好友列表（lobby/game用），实现的功能有：
		1、向数据库查询目标uid的玩家的好友记录，并把结果传递给【ServerGetRNFriendShipCallBack】函数
		'''
		sql = 'SELECT * From neteaseFriendShip WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetRNFriendShipCallBack(uid, args, callback, params))
	
	def ServerGetRNFriendShipCallBack(self, uid, args, callback, params):
		"""
		从数据库查询指定uid的玩家现有好友的记录后的回调函数（lobby/game用），实现的功能有：
		1、把查询到的好友信息缓存到内存中，并区分是否RN好友
		2、调用参数中的回调函数
		"""
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
		查询指定uid的一个玩家现有黑名单信息的函数，实现的功能有：
		1、假如目标uid的玩家的现有黑名单信息已经加载进内存了，直接调用参数中的回调函数
		2、否则向数据库查询目标uid的玩家的好友记录，并把结果传递给【ServiceQueryFriendBlackCallBack】函数
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
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.ServiceQueryFriendBlackCallBack(args, callback, params))
	
	def ServiceQueryFriendBlackCallBack(self, args, callback, params):
		"""
		从数据库查询指定uid玩家的黑名单信息后的回调函数，实现的功能有：
		1、缓存黑名单信息到内存
		2、调用参数中的回调函数
		"""
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
		向黑名单数据库，插入一条新的黑名单关系记录（单向），无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		从黑名单数据库，删除一条指定的黑名单关系记录（单向），无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		查询指定uid的玩家的黑名单列表，可指定是否优先从内存缓存中读取（lobby/game用），实现的功能有：
		1、假如愿意优先从内存缓存中读取黑名单数据，且内存缓存中存在目标uid的黑名单信息，直接调用参数中的回调函数返回黑名单信息
		2、否则向数据库查询目标uid的玩家的黑名单记录，并把结果传递给【ServerGetFriendBlackCallBack】函数
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
		"""
		从数据库查询指定uid的玩家的黑名单记录后的回调函数（lobby/game用），实现的功能有：
		1、把查询到的黑名单信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
	def ServiceQueryRNFriendAlreadySync(self, uids, callback, params):
		'''
		查询指定uid列表玩家已经同步完毕的RN好友的记录的函数，实现的功能有：
		1、遍历输入的uid列表，过滤掉内存中已经有RN好友信息缓存的uid
		2、假如所有的uid的RN好友信息都已经加载进内存了，直接调用参数中的回调函数
		3、否则向数据库查询过滤后的uid列表中的玩家的RN好友同步记录，并把结果传递给【ServiceQueryRNFriendAlreadySyncCallBack】函数
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetHasSyncUids() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendShipRNAlreadySync WHERE uid in %s'
		sqlparam = (needQueryIds,)
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam,
		                                 lambda args: self.ServiceQueryRNFriendAlreadySyncCallBack(args, callback, params))
		
	def ServiceQueryRNFriendAlreadySyncCallBack(self, args, callback, params):
		"""
		查询指定uid列表玩家的RN好友同步记录的回调函数，实现的功能有：
		1、把RN好友同步记录的信息更新到内存缓存
		2、调用参数中的回调函数
		"""
		for data in args:
			if data:
				uid = data[0] #mysql读出来是元组的形式
				fuid = data[1]
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddHasSyncUids(fuid)
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddHasSyncUids(fuid)
		callback(params)
	
	#======= 申请列表部分数据库操作
	def ServiceQueryFriendRequest(self, uids, callback, params):
		'''
		查询指定uid列表玩家的申请加好友的记录的函数，实现的功能有：
		1、遍历输入的uid列表，过滤掉内存中已经有好友申请信息缓存的uid
		2、假如所有的uid的好友申请信息都已经加载进内存了，直接调用参数中的回调函数
		3、否则向数据库查询过滤后的uid列表中的玩家的好友申请记录，并把结果传递给【ServiceQueryFriendRequestCallBack】函数
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
		"""
		查询指定uid列表玩家的好友申请记录的回调函数，实现的功能有：
		1、把好友申请记录的信息更新到内存缓存
		2、调用参数中的回调函数
		"""
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
		'''
		向好友申请数据库，插入一条新的好友申请记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
		'''
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
		从好友申请数据库，删除指定的的好友申请记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		"""
		查询面向指定uid的玩家的好友申请信息，可指定是否优先从内存缓存中读取（lobby/game用），实现的功能有：
		1、假如愿意优先从内存缓存中读取好友申请数据，且内存缓存中存在目标uid的好友申请信息，直接调用参数中的回调函数返回好友申请信息
		2、否则向数据库查询目标uid的玩家的好友申请记录，并把结果传递给【ServerGetFriendRequestCallBack】函数
		"""
		if useCache:
			friend = self.getFriendData(uid)
			if friend and friend.GetFriendRequests() is not None:
				callback(friend.GetFriendRequests(), params)
				return
		sql = 'SELECT * From neteaseFriendApply WHERE uid = %s'
		sqlparam = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(str(uid), sql, sqlparam, lambda args: self.ServerGetFriendRequestCallBack(uid, args, callback, params))
	
	def ServerGetFriendRequestCallBack(self, uid, args, callback, params):
		"""
		从数据库查询面向指定uid的玩家的好友申请记录后的回调函数（lobby/game用），实现的功能有：
		1、把查询到的黑名单信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
		从数据库读出指定uid列表的玩家的好友相关数据到内存缓存，具体步骤是：
		1、从【neteaseFriendShip】表中读取已经组成好友关系的记录，并缓存到内存
		2、从【neteaseFriendBlack】表中读取黑名单的记录，并缓存到内存
		3、从【neteaseFriendApply】表中读取好友申请的记录，并缓存到内存
		4、从【neteaseFriendTemp】表中读取临时好友的记录，并缓存到内存
		5、调用参数中的回调函数
		'''
		def getTemp(params):
			self.ServiceQueryTempFriend(uids, callback, params)
		def getRequest(params):
			self.ServiceQueryFriendRequest(uids, getTemp, params)
		def getBlack(params):
			self.ServiceQueryFriendBlackList(uids, getRequest, params)
		self.ServiceQueryFriendShip(uids, getBlack, params)
		
	def SyncRNPrepareFriendData(self, uids, callback, params):
		'''
		从数据库读出指定uid列表的玩家的好友相关数据到内存缓存（包括RN好友的同步记录），具体步骤是：
		1、从【neteaseFriendShip】表中读取已经组成好友关系的记录，并缓存到内存
		2、从【neteaseFriendBlack】表中读取黑名单的记录，并缓存到内存
		3、从【neteaseFriendApply】表中读取好友申请的记录，并缓存到内存
		4、从【neteaseFriendShipRNAlreadySync】表中读取RN好友的同步记录，并缓存到内存
		5、调用参数中的回调函数
		'''
		def getAlreadySync(params):
			self.ServiceQueryRNFriendAlreadySync(uids, callback, params)
		def getRequest(params):
			self.ServiceQueryFriendRequest(uids, getAlreadySync, params)
		def getBlack(params):
			self.ServiceQueryFriendBlackList(uids, getRequest, params)
		self.ServiceQueryFriendShip(uids, getBlack, params)
		
	def ServerPrePareData(self, uid, callback, params):
		'''
		从数据库读出指定uid列表的玩家的好友相关数据到内存缓存（lobby/game用），具体步骤是：
		1、从【neteaseFriendShip】表中读取已经组成好友关系的记录，并缓存到内存
		2、从【neteaseFriendApply】表中读取好友申请的记录，并缓存到内存
		3、从【neteaseFriendBlack】表中读取黑名单的记录，并缓存到内存
		4、从【neteaseFriendUnread】表中读取尚有未读聊天记录的好友的uid的信息，并缓存到内存
		5、调用参数中的回调函数
		'''
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
		"""
		查询指定uid列表的玩家的有未读聊天消息的好友信息，实现的功能有：
		1、假如内存缓存中存在目标uid列表的的未读聊天消息好友列表信息，直接调用参数中的回调函数返回
		2、否则向数据库查询目标uid列表玩家的未读聊天消息好友信息，并把结果传递给【ServiceQueryUnreadListCallBack】函数
		"""
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
		"""
		从数据库查询指定uid列表中的玩家的未读聊天消息好友信息后的回调函数，实现的功能有：
		1、把查询到的未读聊天消息好友信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
		向未读聊天消息数据库，插入一条新的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		从未读聊天消息数据库，删除一条新的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
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
		"""
		查询指定uid的玩家的存在未读聊天消息的好友，可指定是否优先从内存缓存中读取（lobby/game用），实现的功能有：
		1、假如愿意优先从内存缓存中读取数据，且内存缓存中存在目标uid的未读聊天消息好友信息，直接调用参数中的回调函数返回
		2、否则向数据库查询目标uid的玩家的存在未读聊天消息的好友，并把结果传递给【ServerGetUnreadCallBack】函数
		"""
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
		"""
		从数据库查询指定uid的玩家的存在未读聊天消息的好友的信息（lobby/game用），实现的功能有：
		1、把查询到的存在未读聊天消息好友的信息缓存到内存中。
		2、调用参数中的回调函数
		"""
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
	
	def ServiceInsertTempFriends(self, fromUid, toUid, callback):
		'''
		向临时好友数据库，插入一条新的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
		'''
		currentTime = time.time()
		sql = 'INSERT INTO neteaseFriendTemp(uid, fuid, time) VALUES (%s,%s,%s)'
		sqlparam = (fromUid, toUid, currentTime,)
		
		def ServiceInsertTempCb(args):
			logout.verbose("friend Temp in database uid=%s buid=%s" % (fromUid, toUid))
			if args is None:
				logout.error("[FRIEND] SAVE Temp FOR [%d] FAIL" % fromUid)
			callback()
		
		mysqlPool.AsyncQueryWithOrderKey(str([fromUid, toUid]), sql, sqlparam, lambda args: ServiceInsertTempCb(args))
		
	def ServiceQueryTempFriend(self, uids, callback, params):
		"""
		查询指定uid列表的玩家的临时好友信息，实现的功能有：
		1、遍历输入的uid列表，过滤掉内存中已经有临时好友信息缓存的uid
		2、假如所有的uid的临时好友都已经加载进内存了，直接调用参数中的回调函数
		3、否则向数据库查询过滤后的uid列表中的玩家的临时好友记录，并把结果传递给【ServiceQueryTempFriendCallBack】函数
		"""
		'''
		service查找未临时好友。service 是如果内存有就不需要查db
		'''
		needQueryIds = []
		for uid in uids:
			if self.getFriendData(uid) is None or self.getFriendData(uid).GetTempFriends() is None:
				needQueryIds.append(uid)
		if len(needQueryIds) == 0:
			callback(params)
			return
		sql = 'SELECT * From neteaseFriendTemp WHERE uid in %s'
		sqlparam = (needQueryIds,)
		mysqlPool.AsyncQueryWithOrderKey(str(uids), sql, sqlparam, lambda args: self.ServiceQueryTempFriendCallBack(args, callback, params))

	def ServiceQueryTempFriendCallBack(self, args, callback, params):
		"""
		查询指定uid列表玩家的临时好友记录的回调函数，实现的功能有：
		1、把临时好友记录的信息更新到内存缓存
		2、调用参数中的回调函数
		"""
		for data in args:
			if data:
				uid = data[0]  # mysql读出来是元组的形式
				fuid = data[1]
				if self.getFriendData(uid) is None:
					friend = friendData.CFriendData()
					friend.SetUid(uid)
					friend.AddTempFriend(fuid)
					self.mFriends[uid] = friend
				else:
					self.getFriendData(uid).SetUid(uid)
					self.getFriendData(uid).AddTempFriend(fuid)
		callback(params)
		
	def ServiceDelTemp(self, uid, fuid, callback = None):
		'''
		从临时好友数据库，删除指定的的记录，无论是否成功，都会调用参数中的回调函数（失败仅记录错误日志）
		'''
		sql = 'DELETE FROM neteaseFriendTemp WHERE uid = %s AND fuid = %s'
		sqlparam = (uid, fuid,)

		def ServiceDeleteTempCb(args):
			logout.verbose("temp delete in database uid=%s fuid=%s" % (uid, fuid))
			if args is None:
				logout.error("[FRIEND] DELETE TEMP DATA FOR [%d] FAIL" % fuid)
			if callback is not None:
				callback()

		mysqlPool.AsyncQueryWithOrderKey(str([uid, fuid]), sql, sqlparam,
										 lambda args: ServiceDeleteTempCb(args))
		
	
			
		