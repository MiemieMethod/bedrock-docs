# -*- coding: utf-8 -*-
import time
import json
import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import logout
import rankConsts
import timer
import datetime
import service.netgameApi as netServiceApi


class RankDataManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.mRankData = []
		self.mNeedSortedKeys = []
		self.mRankCol = []
		self.mRefreshFrequency = 3
		self.mAwardTime = {}
		self.mIdRankIndex = {}
		self.mIdRankData = {}
		self.mIsCover = True
		self.mLastSendSids = set()
		self.mDirty = True
		#self.mAlreadyAddId = set()
		#self.mAwardConfig = {}
		#self.mRankType = rankConsts.RankType.personal
		#json.load()
		#self.mAllSeverId = []
	
	def Init(self):
		mysqlPool.InitDB(30)
		# 1.初始化的时候，处理一下mod.json的排序优先级
		self.mRankCol = self.system.modConfig["rankCol"]
		self.mIsCover = self.system.modConfig["is_cover"]
		self.mNeedSortedKeys = []
		for oneRankColValue in self.mRankCol:
			if oneRankColValue["dataType"] == rankConsts.ColDataType.dataInt:
				# temp_dict = {oneRankColName: oneRankColValue["priority"]}
				self.mNeedSortedKeys.append(oneRankColValue)
		self.mNeedSortedKeys.sort(self.CmpPriority)
		# 2.记录一些参数
		self.mRankDataFromServer = self.system.modConfig["rank_data_from_server"]
		self.mRefreshFrequency = rankConsts.Refresh_Frequency.get(self.system.modConfig["refresh_frequency"], 3)
		self.mAwardTime = self.system.modConfig["award_time"]
		#self.mAwardConfig = self.system.modConfig["award_config"]
		#self.mRankType = self.system.modConfig["rank_type"]
		if self.mAwardTime["hour"] == "*":
			self.mAwardTime["hour"] = 0
		if self.mAwardTime["minute"] == "*":
			self.mAwardTime["minute"] = 0
		#开启一些定时器
		self.mRepeatedCalRank = timer.TimerManager.addRepeatTimer(self.mRefreshFrequency, self.CalRank)#刷新排行榜
		nextMinuteTime = rankConsts.CalNextFuncTime()
		self.mRepeatedAwardTimer = None
		self.mOneAwardTimer = timer.TimerManager.addTimer(nextMinuteTime, self.rankAward)
		#
		self.QueryAllRankData(self.mRankDataFromServer)
		
	def rankAward(self):
		'''
		结算
		'''
		if self.mRepeatedAwardTimer == None:
			self.mRepeatedAwardTimer = timer.TimerManager.addRepeatTimer(60, self.rankAward)
			self.mOneAwardTimer.cancel()
			self.mOneAwardTimer = None
		now_time = datetime.datetime.now()
		now_year = now_time.date().year
		now_month = now_time.date().month
		now_day = now_time.date().day
		now_hour = now_time.time().hour
		now_minute = now_time.time().minute
		now_weekday = now_time.weekday()
		if self.mAwardTime["year"] not in ("*", now_year):
			return
		if self.mAwardTime["month"] not in ("*", now_month):
			return
		if self.mAwardTime["hour"] not in ("*", now_hour):
			return
		if self.mAwardTime["minute"] not in ("*", now_minute):
			return
		if self.mAwardTime["day"] not in ("*", now_day):
			if self.mAwardTime["week"] not in ("*", now_weekday):
				return
		print "rankAward11111"
		self.realRankAward()
	
	def realRankAward(self, maxIndex = -1):
		"""
		结算完成，推送排行榜数据到全部server
		"""
		if maxIndex == -1:
			rankData = self.mRankData
		else:
			rankData = self.mRankData[0:maxIndex]
		self.system.BroadcastEvent("neteaseRankAwardFromServiceEvent", {"rankData":rankData})
		#self.ClearRankData(self.mRankDataFromServer)
		
	def realGetRankData(self):
		#print "realGetRankData", self.mRankData
		return self.mRankData
			
				
	# def SendMail(self, fromIdSets, mail_titile, mail_content, award_content, award_num):
	# 	print "SendMail", fromIdSets, self.mRankType,
	# 	if self.mRankType == rankConsts.RankType.personal:
	# 		self.realSendMail(list(fromIdSets), mail_titile, mail_content, award_content, award_num)
	# 	elif self.mRankType == rankConsts.RankType.guild:
	# 		import server.extraServiceApi as serviceApi
	# 		neteaseGuildServiceSystem = serviceApi.GetSystem("neteaseGuild", "neteaseGuildService")
	# 		if neteaseGuildServiceSystem:
	# 			for guildId in fromIdSets:
	# 				reMes = neteaseGuildServiceSystem.GetGuildUidsByGuilId(guildId)
	# 				if reMes["code"] == 0:
	# 					playerUids = reMes["players"]
	# 					self.realSendMail(playerUids, mail_titile, mail_content, award_content, award_num)
	#
	# def realSendMail(self, fromIds, mail_titile, mail_content, award_content, award_num):
	# 	import server.extraServiceApi as serviceApi
	# 	neteaseAnnounceServiceSystem = serviceApi.GetSystem("neteaseAnnounce", "neteaseAnnounceService")
	# 	itemDict = {
	# 		'itemName': award_content,
	# 		'count': award_num,
	# 		'auxValue': 0,
	# 	}
	# 	neteaseAnnounceServiceSystem.OutSendMailToMany(fromIds, mail_titile, mail_content, [itemDict, ], 86400)
		
		
	def CmpPriority(self, a, b):
		return cmp(a["priority"], b["priority"])
	
	def OutInsertRankData(self, oneRankData, rankDataFromServer, fromId):
		"""
		处理【新增一条排行榜记录】的请求，对新增记录进行数据合法性检查
		"""
		# 1.检查长度
		if len(oneRankData) != len(self.mRankCol):
			# 长度不等，格式不对
			logout.info("OutInsertRankData Length ERROR data:%s"%str(oneRankData))
			return
		saveDict = {}
		for i, val in enumerate(oneRankData):
			valType = rankConsts.typeof(val)
			if valType != self.mRankCol[i]["dataType"]:
				# 和配置的类型不对，返回
				logout.info("OutInsertRankData type ERROR index valType:%s %s" % (i, valType))
				return
			if valType == rankConsts.ColDataType.dataInt:
				saveDict[self.mRankCol[i]["colName"]] = val
				continue
			elif valType == rankConsts.ColDataType.dataStr:
				if len(val) >= 100:  # 字符串最长为7
					logout.info("OutInsertRankData length ERROR index len:%s %s" % (i, len(val)))
					return
				saveDict[self.mRankCol[i]["colName"]] = val
			elif valType == rankConsts.ColDataType.dataNone:
				saveDict[self.mRankCol[i]["colName"]] = ""
				continue
			else:
				logout.info("OutInsertRankData type not in ERROR index valType:%s %s" % (i, valType))
				# 不是int, str, None，类型不对，返回
				return
		self.InsertOneRankData(saveDict, rankDataFromServer, fromId)
	
	def CalRank(self):
		'''
		排行榜刷新
		'''
		if self.mIsCover:
			if len(self.mIdRankData) <= 0:
				return
		else:
			if len(self.mRankData) <= 0:
				return
		self.mRankData = self.mIdRankData.values() if self.mIsCover else self.mRankData
		self.mRankData.sort(self.CmpRank)
		#print "CalRank", self.mRankData
		#logout.info("refresh rank Data %s" % (str(self.mRankData)))
		currentSendSids = set()
		for sid, serverType in self.system.mConnectedSid.iteritems():
			currentSendSids.add(sid)
			if self.mDirty == True or sid not in self.mLastSendSids:
				if self.mRankDataFromServer in ("*", serverType):
					self.system.NotifyToServerNode(sid, "RefreshRankDataFromService", {"rankData": self.mRankData})
					self.mLastSendSids = currentSendSids
					self.mDirty = False
	
	def CmpRank(self, a, b):
		for oneConfig in self.mNeedSortedKeys:
			oneColName = oneConfig["colName"]
			if a[oneColName] > b[oneColName]:
				return -1
			elif a[oneColName] < b[oneColName]:
				return 1
			else:
				continue
		if a["insertTime"] > b["insertTime"]:
			return 1
		else:
			return -1
	
	def QueryAllRankData(self, queryFromServer="*"):
		"""
		从数据库读取排行榜历史信息（service启动时执行，从数据库恢复数据到内存）
		"""
		self.mRankData = []
		self.mIdRankData = {}
		if queryFromServer == "*":
			sql = 'SELECT * FROM neteaseRankData'
			sqlParam = ()
		else:
			#serverType = commonNetgameApi.GetServerType()
			sql = 'SELECT * FROM neteaseRankData WHERE serverType = %s'
			sqlParam = (queryFromServer,)
		
		def QueryAllRankDataCb(args):
			for data in args:
				if data:
					dataId = data[0]
					oneRankStr = data[1]
					serverType = data[2]
					fromId = data[3]
					insertTime = data[4]
					oneRankData = json.loads(oneRankStr)
					oneRankData["id"] = dataId
					oneRankData["serverType"] = serverType
					oneRankData["fromId"] = fromId
					oneRankData["insertTime"] = insertTime
					if self.mIsCover:
						self.mIdRankData[fromId] = oneRankData
					else:
						# nextRankIndex = len(self.mRankData)
						self.mRankData.append(oneRankData)
					#self.mRankData.append(oneRankData)
			self.mDirty = True
		mysqlPool.AsyncQueryWithOrderKey("QueryAllRankData", sql, sqlParam, lambda args: QueryAllRankDataCb(args))
	
	def InsertOneRankData(self, oneRankData, rankDataFromServer, fromId):
		"""
		插入一条新记录
		"""
		oneRankStr = json.dumps(oneRankData)
		#serverType = commonNetgameApi.GetServerType()
		insertTime = time.time()
		sql = 'INSERT INTO neteaseRankData(rankData, serverType, fromId, insertTime) VALUES (%s,%s,%s,%s)'
		sqlParam = (oneRankStr, rankDataFromServer,fromId,insertTime,)
		self.mDirty = True
		def InsertOneRankDataCb(args):
			if args is None:
				logout.error("Insert oneRankData ERROR %s" % str(oneRankData))
			else:
				dataId = args
				oneRankData["id"] = dataId
				oneRankData["serverType"] = rankDataFromServer
				oneRankData["fromId"] = fromId
				oneRankData["insertTime"] = insertTime
				if self.mIsCover:
					self.mIdRankData[fromId] = oneRankData
				else:
					#nextRankIndex = len(self.mRankData)
					self.mRankData.append(oneRankData)
					#self.mIdRankIndex[fromId] = nextRankIndex
		if self.mIsCover and self.mIdRankData.has_key(fromId):
			sqlDelete = 'Delete from neteaseRankData where fromId = %s'
			sqlDeleteParam = (fromId, )
			self.mIdRankData.pop(fromId)
			mysqlPool.AsyncQueryWithOrderKey("DeleteRankData", sqlDelete, sqlDeleteParam, None)
		mysqlPool.AsyncInsertOneWithOrderKey(str(oneRankData), sql, sqlParam, InsertOneRankDataCb)
	
	def ClearRankData(self, deleteFromServer="*"):
		'''
		结算的时候使用
		'''
		if deleteFromServer == "*":
			sql = 'TRUNCATE Table neteaseRankData'
			sqlParam = ()
		else:
			serverType = commonNetgameApi.GetServerType()
			sql = 'DELETE FROM neteaseRankData WHERE serverType = %s'
			sqlParam = (serverType,)
		
		def DeleteRankDataCb(args):
			if args is None:
				logout.error("DELETE RankData ERROR")
			else:
				self.QueryAllRankData(deleteFromServer)
				commonConfig = netServiceApi.GetCommonConfig()
				for conf in commonConfig.get("serverlist", []):
					if conf.get("app_type") in ("lobby", "game"):
						sid = conf.get('serverid')
						if self.mRankDataFromServer in ("*", conf.get("type")):
							self.system.NotifyToServerNode(sid, "RefreshRankDataFromService",
							                               {"rankData": self.mRankData})
		
		mysqlPool.AsyncQueryWithOrderKey("ClearRankData", sql, sqlParam, lambda args: DeleteRankDataCb(args))
		
	def DeleteRankData(self, rank):
		'''
		删除排行榜数据
		'''
		if rank > len(self.mRankData) or rank < 0:
			return False
		oneRankData = self.mRankData[rank - 1]
		dataId = oneRankData["id"]
		fromId = oneRankData["fromId"]
		if self.mIdRankData.has_key(fromId):
			self.mIdRankData.pop(fromId)
		del self.mRankData[rank - 1]
		sql = 'DELETE FROM neteaseRankData WHERE id = %s'
		sqlParam = (dataId,)
		mysqlPool.AsyncQueryWithOrderKey("DeleteRankData", sql, sqlParam, None)
		commonConfig = netServiceApi.GetCommonConfig()
		for conf in commonConfig.get("serverlist", []):
			if conf.get("app_type") in ("lobby", "game"):
				sid = conf.get('serverid')
				if self.mRankDataFromServer in ("*", conf.get("type")):
					self.system.NotifyToServerNode(sid, "RefreshRankDataFromService", {"rankData": self.mRankData})
		return True


