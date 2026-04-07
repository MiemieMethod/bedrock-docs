# -*- coding: utf-8 -*-
#
import time
import weakref
#
import service.timermanager as timermanager
from service.serviceConf import netgameConf
import neteaseStatisticsScript.statisticsConsts as statisticsConsts
from neteaseStatisticsScript.statisticsConsts import PlayerStaticTable, PlayerDailyTable, ServerEvent
import neteaseMonitor.monitor as monitor
import apolloCommon.mysqlPool as mysqlPool
#
import neteaseStatisticsScript.mysqlStatisticsCacheObjs as StatisticsCacheObj
#---------------------------------------------------------------------------------
class CStatisticsMgr(object):
	def __init__(self, system, moduleName, idx):
		super(CStatisticsMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mModuleIdx = idx
		self.mMonitorMergedData = {}
		self.mEnv = netgameConf.get("env", "unknown")
		self.mMonitorVer = 0
		self.mSystem.RegisterRpcMethod(moduleName, ServerEvent.SyncUserStatus, self.OnUserStats)
		# 每个事件的修改处理函数
		self.mLogHandlers = {
			'login': self.UpdateDailyOnLogin,
			'online': self.UpdateDailyOnOnline,
			'logout': self.UpdateDailyOnLogout,
			'pay': self.UpdateDailyOnPay,
		}
		# 正在排队等待query每日记录表结果后才能进一步处理的事件列表
		self.mOnQueryingEventsMap = {}
		# 内存缓存一定量的每日记录数据，提升性能
		self.mPlayerDailyCache = {}
		# 定期清理内存缓存
		self.mCacheDropTimer = timermanager.timerManager.addRepeatTimer(1000, self.DealCacheDrop)
		print "CREATE_SERVICE_SUCCESS CStatisticsMgr module_name=%s use Mysql" % moduleName
		
	def Destroy(self):
		if self.mCacheDropTimer:
			timermanager.timerManager.delTimer(self.mCacheDropTimer)
			self.mCacheDropTimer = None
		self.mSystem = None
	#-----------------------------------------------------------------------------
	def NeteaseMonitorGetter(self):
		tsks = []
		tsks.append(self.GetRecentData)
		return tsks

	def GetRecentData(self, totalTick):
		self.mMonitorVer += 1
		ver = "%s_%s" % (self.mModuleIdx, self.mMonitorVer)
		ps = []
		for key, data in self.mMonitorMergedData.iteritems():
			dbName, fitTime = key
			point = monitor.Point().measurement(dbName).tag("env", self.mEnv).tag("ver", ver).change_time(fitTime)
			for k, v in data.iteritems():
				point.field(k, v)
			ps.append(point)
		self.mMonitorMergedData.clear()
		return ps
	
	def MonitorAccountNew(self, uid, ctime):
		fitTime = (ctime//10) * 10
		key = ('account_new', fitTime)
		point = self.mMonitorMergedData.get(key, None)
		if not point:
			point = {'num':0, }
			self.mMonitorMergedData[key] = point
		point['num'] += 1
	
	def MonitorAccountLogin(self, uid, fLoginTime):
		fitTime = (fLoginTime//10) * 10
		key = ('account_login', fitTime)
		point = self.mMonitorMergedData.get(key, None)
		if not point:
			point = {'num':0, }
			self.mMonitorMergedData[key] = point
		point['num'] += 1
	
	def MonitorAccountPay(self, uid, when, pay, orderkey):
		fitTime = (when//10) * 10
		key = ('account_pay', fitTime)
		point = self.mMonitorMergedData.get(key, None)
		if not point:
			point = {'pay':0, }
			self.mMonitorMergedData[key] = point
		point['pay'] += pay
	#------------------------------------------------------------------------------
	def OnUserStats(self, serverId, callbackId, args):
		# print "OnUserStats", serverId, callbackId, args
		keyword = args.get('keyword', None)
		if not keyword:
			return
		# 额外打印一份特殊日志存档
		fields = statisticsConsts.GetLogFields(keyword)
		if fields is None:
			return
		data = {'serverId':serverId, }
		for key in fields:
			data[key] = args[key]
		# 仅仅处理玩家行为的事件，所以hashkey锁定为uid
		uid = args.get('uid', 0)
		data["uid"] = uid
		print "[STATS][%s] %s" % (keyword, str(data))
		# 登录、登出、在线、付费日志需要额外处理逻辑
		handler = self.mLogHandlers.get(keyword, None)
		if handler is None:
			return
		# 假如此uid的每日记录已经在内存缓存中了，直接执行处理函数
		playerDaily = self.GetPlayerDailyFromCache(uid)
		if playerDaily:
			handler(data, playerDaily)
			return
		# 假如已经有针对这个uid的query请求执行中了，那么当前事件直接排队
		event = (data, handler)
		if self.mOnQueryingEventsMap.has_key(uid):
			self.mOnQueryingEventsMap[uid].append(event)
			return
		# 生成一个新的query事件队列，并且开启一个query任务
		self.mOnQueryingEventsMap[uid] = [event,]
		self.QueryPlayerDailyFromMysql(uid)
	#---------------------------------------------------------------------------
	def QueryPlayerStaticFromMysql(self, uid):
		sql = "SELECT uid, ctime, login_cnt, otime, pay, uptime FROM %s " % PlayerStaticTable
		sql += "WHERE uid=%s"
		params = (uid, )
		callback = lambda records:self.QueryPlayerStaticCallback(uid, records)
		mysqlPool.AsyncQueryWithOrderKey("daily%s"%uid, sql, params, callback)

	def QueryPlayerStaticCallback(self, uid, records):
		if records:
			playerStatic = StatisticsCacheObj.CPlayerStatic()
			playerStatic.OnCreateFromDatabase(records[0])
		else:
			playerStatic = None
		# 获取排队的事件列表
		eventList = self.mOnQueryingEventsMap.get(uid, None)
		if eventList is None:
			return
		# 需要查询每个玩家的唯一记录，说明每日记录肯定没查到
		for data, handler in eventList:
			handler(data, None, playerStatic)
		del self.mOnQueryingEventsMap[uid]

	def CreatePlayerStaticAndInsert(self, uid, ctime, loginCnt=0, online=0, pay=0):
		playerStatic = StatisticsCacheObj.CPlayerStatic()
		playerStatic.OnCreate(uid, ctime, loginCnt, online, pay)
		sql = "INSERT INTO %s (uid, ctime, login_cnt, otime, pay, uptime) " % PlayerStaticTable
		sql += "VALUES (%s, %s, %s, %s, %s, %s)"
		params = playerStatic.GetSqlParams()
		callback = lambda suc:self.CreatePlayerStaticCallback(suc, params)
		mysqlPool.AsyncExecuteWithOrderKey("daily%s"%uid, sql, params, callback)
		# 上传统计数据，新增玩家
		self.MonitorAccountNew(uid, ctime)
		return playerStatic.mCTime

	def CreatePlayerStaticCallback(self, suc, params):
		if not suc:
			print "create_player_static fail params=%s"%str(params)

	def UpdatePlayerStatic(self, uid, keyname, dvalue, uptime):
		sql = "UPDATE %s SET %s=%s" % (PlayerStaticTable, keyname, keyname)
		sql += "+%s, uptime=%s WHERE uid=%s"
		params = (dvalue, uptime, uid)
		callback = lambda suc:self.UpdatePlayerStaticCallback(uid, keyname, dvalue, uptime, suc)
		mysqlPool.AsyncExecuteWithOrderKey("daily%s"%uid, sql, params, callback)
	
	def UpdatePlayerStaticCallback(self, uid, keyname, dvalue, uptime, suc):
		if not suc:
			print "update_player_static fail uid=%s %s+=%s uptime=%s"%(uid, keyname, dvalue, uptime)
	#---------------------------------------------------------------------------
	def QueryPlayerDailyFromMysql(self, uid):
		sql = "SELECT _id, uid, day_str, flogin_time, ctime, login_cnt, otime, pay, uptime FROM %s " % PlayerDailyTable
		sql += "WHERE uid=%s ORDER BY uptime DESC LIMIT 1"
		params = (uid, )
		callback = lambda records:self.QueryPlayerDailyCallback(uid, records)
		mysqlPool.AsyncQueryWithOrderKey("daily%s"%uid, sql, params, callback)

	def QueryPlayerDailyCallback(self, uid, records):
		# 数据库中没查询到每日记录，有两种情况
		# 1、此玩家是首次登录
		# 2、此玩家上次登录非常久远，久远到每日记录已经过期删除了
		# 要判断是哪种情况，需要从玩家唯一静态表中查询
		if not records:
			self.QueryPlayerStaticFromMysql(uid)
			return
		# 数据库中查询到了最近一条每日记录
		playerDaily = StatisticsCacheObj.CPlayerDaily()
		playerDaily.OnCreateFromDatabase(records[0])
		self.CachePlayerDaily(uid, playerDaily)
		# 获取排队的事件列表
		eventList = self.mOnQueryingEventsMap.get(uid, None)
		if eventList is None:
			return
		for data, handler in eventList:
			handler(data, playerDaily)
		del self.mOnQueryingEventsMap[uid]
		
	def InsertPlayerDaily(self, uid, playerDaily):
		sql = "INSERT INTO %s (uid, day_str, flogin_time, ctime, login_cnt, otime, pay, uptime) " % PlayerDailyTable
		sql += "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
		params = playerDaily.GetSqlParams()
		callback = lambda newId:self.InsertPlayerDailyCallback(uid, playerDaily, params, newId)
		mysqlPool.AsyncInsertOneWithOrderKey("daily%s"%uid, sql, params, callback)
	
	def InsertPlayerDailyCallback(self, uid, playerDaily, params, newId):
		if not newId:
			print "insert_obs_daily fail params=%s"%str(params)
			return
		playerDaily.SetUniqueId(newId)

	def UpdatePlayerDaily(self, uid, dayStr, keyname, dvalue, uptime):
		sql = "UPDATE %s SET %s=%s" % (PlayerDailyTable, keyname, keyname)
		sql += "+%s, uptime=%s WHERE uid=%s AND day_str=%s"
		params = (dvalue, uptime, uid, dayStr)
		callback = lambda suc:self.UpdatePlayerDailyCallback(suc, uid, dayStr, keyname, dvalue, uptime)
		mysqlPool.AsyncExecuteWithOrderKey("daily%s"%uid, sql, params, callback)
	
	def UpdatePlayerDailyCallback(self, suc, uid, dayStr, keyname, dvalue, uptime):
		if not suc:
			print "update_obs_daily fail uid=%s, date=%s key=%s dvalue=%s uptime=%s"%(uid, dayStr, keyname, dvalue, uptime)
	#---------------------------------------------------------------------------
	def DealCacheDrop(self):
		needRemoveUids = []
		now = int(time.time())
		for uid, playerDaily in self.mPlayerDailyCache.iteritems():
			if (now - playerDaily.uptime) > statisticsConsts.PlayerDailyMemoryKeepTime:
				needRemoveUids.append(uid)
		if needRemoveUids:
			print "deal_cache_drop length=%s, drop_length=%s" % (len(self.mPlayerDailyCache), len(needRemoveUids))
		for uid in needRemoveUids:
			del self.mPlayerDailyCache[uid]
		
	def GetPlayerDailyFromCache(self, uid):
		return self.mPlayerDailyCache.get(uid, None)
	
	def CachePlayerDaily(self, uid, playerDaily):
		self.mPlayerDailyCache[uid] = playerDaily
	#---------------------------------------------------------------------------
	# 处理login事件
	def UpdateDailyOnLogin(self, data, playerDaily, playerStatic=None):
		uid, when, serverId = data['uid'], data['when'], data['serverId']
		# 无法查到最新的每日记录
		if not playerDaily:
			# 能查询到每个玩家的唯一记录，那么ctime就以唯一记录为准
			if playerStatic:
				ctime = playerStatic.mCTime
				# 全局数据登录次数+1
				self.UpdatePlayerStatic(uid, "login_cnt", 1, when)
			else:	# 否则需要新建每个玩家的唯一记录，ctime就是当前登录事件的发生时间
				ctime = self.CreatePlayerStaticAndInsert(uid, when, loginCnt=1)
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByLogin(uid, when, ctime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			return
		# 检查最新的每日记录和登录事件是不是同一天的
		# 假如是同一天的，那么需要更新每日记录
		if playerDaily.IsSameDay(when):
			keyname, dvalue = playerDaily.UpdateByLogin(when, serverId)
			self.UpdatePlayerDaily(uid, playerDaily.mDate, keyname, dvalue, playerDaily.mUpTime)
			# 全局数据登录次数+1
			self.UpdatePlayerStatic(uid, keyname, dvalue, playerDaily.mUpTime)
			return
		# 假如已经不是当天了
		if playerDaily.IsFutureDay(when):
			# 新的日期，生成新的每日记录
			# 角色创建时间沿用上一个每日记录中的日期
			# 同时缓存中的每日记录，更新到最新日期的
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByLogin(uid, when, playerDaily.mCTime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			# 全局数据登录次数+1
			self.UpdatePlayerStatic(uid, "login_cnt", 1, when)
			return
		# 是过去一天的日志，那么说明出现了日志顺序倒挂
		# 目前直接丢弃
	#---------------------------------------------------------------------------
	# 处理online事件（online事件是定时发送的在线事件，用于刷新在线时间）
	def UpdateDailyOnOnline(self, data, playerDaily, playerStatic=None):
		uid, when, serverId = data['uid'], data['when'], data['serverId']
		oltime, d_oltime = data['oltime'], data['d_oltime']
		# 无法查到最新的每日记录，说明应该有的login事件在不明原因下丢掉了
		if not playerDaily:
			# 能查询到每个玩家的唯一记录，那么ctime就以唯一记录为准
			if playerStatic:
				ctime = playerStatic.mCTime
				# 全局数据在线时间累积
				self.UpdatePlayerStatic(uid, "otime", d_oltime, when)
			else:	# 否则需要新建每个玩家的唯一记录，ctime为事件时间减去总在线时间
				ctime = self.CreatePlayerStaticAndInsert(uid, when-oltime, online=oltime)
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByOnline(uid, when, ctime, oltime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			return
		# 检查最新的每日记录和在线事件是不是同一天的
		# 假如是同一天的，那么需要更新每日记录
		if playerDaily.IsSameDay(when):
			keyname, dvalue = playerDaily.UpdateByOnline(when, d_oltime, serverId)
			self.UpdatePlayerDaily(uid, playerDaily.mDate, keyname, dvalue, playerDaily.mUpTime)
			# 全局数据在线时间累积
			self.UpdatePlayerStatic(uid, keyname, dvalue, playerDaily.mUpTime)
			return
		# 假如已经不是当天了
		if playerDaily.IsFutureDay(when):
			# 新的日期，生成新的每日记录
			# 角色创建时间沿用上一个每日记录中的日期
			# 同时缓存中的每日记录，更新到最新日期的
			# 新记录最初在线时间，会算上一天最后一次online之后的时间，但是误差不大，所以不搞那么精确了
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByOnline(uid, when, playerDaily.mCTime, d_oltime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			# 全局数据在线时间累积
			self.UpdatePlayerStatic(uid, "otime", d_oltime, when)
			return
		# 是过去一天的日志，那么说明出现了日志顺序倒挂
		# 目前直接丢弃
	#---------------------------------------------------------------------------
	# 处理logout事件
	def UpdateDailyOnLogout(self, data, playerDaily, playerStatic=None):
		uid, when, serverId = data['uid'], data['when'], data['serverId']
		oltime, d_oltime = data['oltime'], data['d_oltime']
		# 无法查到最新的每日记录，说明应该有的login事件在不明原因下丢掉了
		if not playerDaily:
			# 能查询到每个玩家的唯一记录，那么ctime就以唯一记录为准
			if playerStatic:
				ctime = playerStatic.mCTime
				# 全局数据在线时间累积
				self.UpdatePlayerStatic(uid, "otime", d_oltime, when)
			else:	# 否则需要新建每个玩家的唯一记录，ctime为事件时间减去总在线时间
				ctime = self.CreatePlayerStaticAndInsert(uid, when-oltime, online=oltime)
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByLogout(uid, when, ctime, oltime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			return
		# 检查最新的每日记录和在线事件是不是同一天的
		# 假如是同一天的，那么需要更新每日记录
		if playerDaily.IsSameDay(when):
			# 这里需要考虑到事件顺序倒挂的情况，酌情更新mLastStateServer
			keyname, dvalue = playerDaily.UpdateByLogout(when, d_oltime, serverId)
			self.UpdatePlayerDaily(uid, playerDaily.mDate, keyname, dvalue, playerDaily.mUpTime)
			# 全局数据在线时间累积
			self.UpdatePlayerStatic(uid, keyname, dvalue, playerDaily.mUpTime)
			return
		# 假如已经不是当天了
		if playerDaily.IsFutureDay(when):
			# 新的日期，生成新的每日记录
			# 角色创建时间沿用上一个每日记录中的日期
			# 同时缓存中的每日记录，更新到最新日期的
			# 新记录最初在线时间，会算上一天最后一次online之后的时间，但是误差不大，所以不搞那么精确了
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByLogout(uid, when, playerDaily.mCTime, d_oltime, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			# 全局数据在线时间累积
			self.UpdatePlayerStatic(uid, "otime", d_oltime, when)
			return
		# 是过去一天的日志，那么说明出现了日志顺序倒挂
		# 目前直接丢弃
	#---------------------------------------------------------------------------
	# 处理pay事件（每次订单发货，发送pay事件）
	def UpdateDailyOnPay(self, data, playerDaily, playerStatic=None):
		uid, when, pay, orderkey, serverId = data['uid'], data['when'], data['pay'], data['orderkey'], data['serverId']
		# 上传统计数据，玩家支付
		self.MonitorAccountPay(uid, when, pay, orderkey)
		# 无法查到最新的每日记录，说明应该有的login事件在不明原因下丢掉了
		if not playerDaily:
			# 能查询到每个玩家的唯一记录，那么ctime就以唯一记录为准
			if playerStatic:
				ctime = playerStatic.mCTime
				# 全局支付总数累积
				self.UpdatePlayerStatic(uid, "pay", pay, when)
			else:	# 否则需要新建每个玩家的唯一记录，ctime就是事件时间（并不精确）
				ctime = self.CreatePlayerStaticAndInsert(uid, when, pay=pay)
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByPay(uid, when, ctime, pay, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			return
		# 检查最新的每日记录和在线事件是不是同一天的
		# 假如是同一天的，那么需要更新每日记录
		if playerDaily.IsSameDay(when):
			# 这里需要考虑到事件顺序倒挂的情况，酌情更新mLastStateServer
			keyname, dvalue = playerDaily.UpdateByPay(when, pay, serverId)
			self.UpdatePlayerDaily(uid, playerDaily.mDate, keyname, dvalue, playerDaily.mUpTime)
			# 全局支付总数累积
			self.UpdatePlayerStatic(uid, keyname, dvalue, playerDaily.mUpTime)
			return
		# 假如已经不是当天了
		if playerDaily.IsFutureDay(when):
			# 新的日期，生成新的每日记录
			# 角色创建时间沿用上一个每日记录中的日期
			# 同时缓存中的每日记录，更新到最新日期的
			newPlayerDaily = StatisticsCacheObj.CPlayerDaily()
			newPlayerDaily.OnCreateByPay(uid, when, playerDaily.mCTime, pay, serverId)
			self.CachePlayerDaily(uid, newPlayerDaily)
			self.InsertPlayerDaily(uid, newPlayerDaily)
			# 上传统计数据，玩家每日第一次登录
			self.MonitorAccountLogin(uid, when)
			# 全局支付总数累积
			self.UpdatePlayerStatic(uid, "pay", pay, when)
			return
		# 是过去一天的日志，那么说明出现了日志顺序倒挂
		# 目前直接丢弃
	#---------------------------------------------------------------------------
	




