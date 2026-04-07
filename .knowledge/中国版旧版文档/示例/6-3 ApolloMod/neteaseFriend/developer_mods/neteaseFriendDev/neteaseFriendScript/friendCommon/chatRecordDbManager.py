# -*- coding: utf-8 -*-
import time
import timer
import logout
import apolloCommon.mysqlPool as mysqlPool
import neteaseFriendScript.friendCommon.chatRecordData as chatRecordData

class ChatDbManager(object):
	LOBBY_CACHE_TIME = 600
	
	def __init__(self):
		self.mPlayerChatRecords = {}
		import random
		self.RECORD_MAX_NUM = 200
		# avoid all gc in the same time
		randTime = random.randint(1, self.LOBBY_CACHE_TIME)
		self.gcCacheTimer = timer.TimerManager.addTimer(randTime, self.StartGcCache)
	
	# def InitMysqlDb(self):
	# 	# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
	# 	try:
	# 		mysqlPool.InitDB(20)
	# 	except:
	# 		logout.error("start_Friend fail when init mysql")
	# 		return False
	# 	return True
	
	def Destroy(self):
		self.mPlayerChatRecords.clear()
		if self.gcCacheTimer:
			self.gcCacheTimer.cancel()
			self.gcCacheTimer = None
	
	def StartGcCache(self):
		self.GcCache()
		self.gcCacheTimer = timer.TimerManager.addRepeatTimer(self.LOBBY_CACHE_TIME, self.GcCache)
	
	def GcCache(self):
		tempChatRecords = {}
		now = time.time()
		for uid, chatData in self.mPlayerChatRecords.iteritems():
			logout.info("GcCache", uid, chatData)
			if chatData.GetLastUpdateTimestamp() + self.LOBBY_CACHE_TIME > now:
				tempChatRecords[uid] = chatData
		self.mPlayerChatRecords = tempChatRecords
		logout.info("gc_cache chat record length=%s" % len(self.mPlayerChatRecords))
	
	def ChatRecordToDict(self, chatIndex, fromUid, toUid, message, chatTime):
		dict = {}
		dict["chatIndex"] = chatIndex
		dict["fromUid"] = fromUid
		dict["toUid"] = toUid
		dict["message"] = message
		dict["chatTime"] = chatTime
		return dict
		
	def InsertChatRecord(self, fromUid, toUid, message, currentTime, callback):
		'''
		记录聊天记录到db
		'''
		sql = 'INSERT INTO neteaseFriendChat(fromUid, toUid, message, time) VALUES (%s,%s,%s,%s)'
		sqlparam = (fromUid, toUid, message, currentTime,)
		def InsertChatRecordCb(ret, callback):
			logout.verbose("friend chat change in database fromuid=%s, touid=%s" % (fromUid,toUid))
			if ret is None:
				logout.error("insert_chat_record failed between %d, %d" % (fromUid, toUid))
				callback(ret)
				return
			chatIndex = ret
			temp_chatRecord = self.ChatRecordToDict(chatIndex, fromUid, toUid, message, currentTime)
			uid1 = fromUid
			uid2 = toUid
			if fromUid > toUid:
				temp_chatRecord["isSend"] = False
				uid1, uid2 = uid2, uid1
			else:
				temp_chatRecord["isSend"] = True
			recordData = self.mPlayerChatRecords.get(uid1, None)
			if recordData is not None:
				#recordData.InsertChatRecord(uid2, temp_chatRecord)
				self.RealInsertChat(uid1, uid2, temp_chatRecord)
			else:
				self.QueryChatRecord(fromUid, toUid, None)
			callback(ret)
		mysqlPool.AsyncInsertOneWithOrderKey(str([fromUid, toUid]), sql, sqlparam, lambda args: InsertChatRecordCb(args, callback))
		
	def DeleteChatRecord(self, fromUid, toUid, callback = None):
		'''
		删除和某个好友的聊天记录，一般是删除好友的时候发生
		'''
		sql = 'DELETE FROM neteaseFriendChat WHERE fromuid = %s AND touid = %s'
		sqlparam = (fromUid, toUid, )
		def DeleteChatRecordCb(args, callback):
			logout.verbose("friend chat change in database fromuid=%s, touid=%s" % (fromUid, toUid))
			if not args:
				logout.error("delete_chat_record failed between %d, %d" % (fromUid, toUid))
			else:
				#删除内存
				uid1 = fromUid
				uid2 = toUid
				if fromUid > toUid:
					uid1, uid2 = uid2, uid1
				chatRecordData = self.mPlayerChatRecords.get(uid1, None)
				if chatRecordData:
					chatRecordData.DelChatRecord(uid2)
			if callback is not None:
				callback()
		mysqlPool.AsyncQueryWithOrderKey(str([fromUid, toUid]), sql, sqlparam, lambda args: DeleteChatRecordCb(args, callback))
		
	def InsertChatRecordInCache(self, fromUid, toUid, message, chatIndex):
		currentTime = time.time()
		temp_chatRecord = self.ChatRecordToDict(chatIndex, fromUid, toUid, message, currentTime)
		uid1 = fromUid
		uid2 = toUid
		if fromUid > toUid:
			temp_chatRecord["isSend"] = False
			uid1, uid2 = uid2, uid1
		else:
			temp_chatRecord["isSend"] = True
		recordData = self.mPlayerChatRecords.get(uid1, None)
		if recordData is None:
			self.QueryChatRecord(fromUid, toUid, None)
			return
		else:
			#recordData.InsertChatRecord(uid2, temp_chatRecord)
			self.RealInsertChat(uid1, uid2, temp_chatRecord)

	def RealInsertChat(self, uid1, uid2, temp_chatRecord):
		recordData = self.mPlayerChatRecords.get(uid1, None)
		if recordData:
			recordData.InsertChatRecord(uid2, temp_chatRecord)
		if recordData and recordData.GetChatRecord(uid2) and len(recordData.GetChatRecord(uid2)) > self.RECORD_MAX_NUM:
			recordData.PopChatRecord(uid2)
		self.mPlayerChatRecords[uid1] = recordData
		logout.info("RealInsertChat", self.mPlayerChatRecords)
	
	def DeleteChatRecordInCache(self, fromUid, toUid):
		'''
		删除和某个好友的聊天记录，一般是删除好友的时候发生
		'''
		uid1 = fromUid
		uid2 = toUid
		if fromUid > toUid:
			uid1, uid2 = uid2, uid1
		chatRecordData = self.mPlayerChatRecords.get(uid1, None)
		if chatRecordData:
			chatRecordData.DelChatRecord(uid2)
	
	def PopChatRecord(self, fromUid, toUid):
		recordData = self.mPlayerChatRecords.get(fromUid, None)
		if recordData:
			recordData.PopChatRecord(toUid)
	
	def GetChatRecord(self, fromUid, toUid):
		uid1 = fromUid
		uid2 = toUid
		if fromUid > toUid:
			uid1, uid2 = uid2, uid1
		chatRecordData = self.mPlayerChatRecords.get(uid1, None)
		if chatRecordData:
			records = chatRecordData.GetChatRecord(uid2)
			return records
		return None
	
	def QueryChatRecord(self, selfUid, friendUid, callback, useCache = True):
		uida = selfUid
		uidb = friendUid
		if selfUid > friendUid:
			uida, uidb = uidb, uida
		playerChatRecordData = self.mPlayerChatRecords.get(uida, None)
		if playerChatRecordData and useCache == True:
			records = playerChatRecordData.GetChatRecord(uidb)
			if records:
				callback(records)
				return
		sql = 'SELECT * From neteaseFriendChat WHERE (fromuid = %s AND touid = %s) or (fromuid = %s AND touid = %s) order by id desc limit %s'
		sqlparam = (selfUid, friendUid, friendUid, selfUid, self.RECORD_MAX_NUM,)
		
		def QueryChatRecordCb(args, callback):
			if uida in self.mPlayerChatRecords:
				self.mPlayerChatRecords.pop(uida)
			logout.info("QueryChatRecordCb", args)
			for data in args:
				if data:
					chatIndex = data[0]
					fUid = data[1]
					tUid = data[2]
					time = data[3]
					message = data[4]
					uid1 = fUid
					uid2 = tUid
					temp_chatRecord = self.ChatRecordToDict(chatIndex, fUid, tUid, message, time)
					if fUid > tUid:
						temp_chatRecord["isSend"] = False
						uid1, uid2 = uid2, uid1
					else:
						temp_chatRecord["isSend"] = True
					recordData = self.mPlayerChatRecords.get(uid1, None)
					if recordData is None:
						recordData = chatRecordData.ChatData()
						recordData.SetUid(uid1)
					self.mPlayerChatRecords[uid1] = recordData
					#recordData.InsertChatRecord(uid2, temp_chatRecord)
					self.RealInsertChat(uid1, uid2, temp_chatRecord)
			if callback is not None:
				if self.mPlayerChatRecords.has_key(uida):
					callback(self.mPlayerChatRecords[uida].GetChatRecord(uidb))
				else:
					callback([])
		
		mysqlPool.AsyncQueryWithOrderKey(str([selfUid, friendUid]), sql, sqlparam,
		                                 lambda args: QueryChatRecordCb(args, callback))
	
	