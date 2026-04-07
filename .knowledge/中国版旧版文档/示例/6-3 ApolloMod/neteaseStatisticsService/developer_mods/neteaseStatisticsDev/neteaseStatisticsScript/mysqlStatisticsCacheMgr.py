# -*- coding: utf-8 -*-
#
import time
import weakref
#
import service.timermanager as timermanager
from service.serviceConf import netgameConf
import apolloCommon.mysqlPool as mysqlPool
import neteaseMonitor.monitor as monitor
from neteaseStatisticsScript.statisticsConsts import OneDayDelayTime, OneDaySecond
from neteaseStatisticsScript.statisticsConsts import PlayerDailyTable, PlayerStaticTable
#---------------------------------------------------------------------------------
class CStatisticsCacheMgr(object):
	def __init__(self, system, moduleName, idx):
		super(CStatisticsCacheMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mModuleIdx = idx
		self.mMonitorTasks = []
		self.mEnv = netgameConf.get("env", "unknown")
		#
		self.mWorkTimer = None
		self.InitWorkStartTime()
		self.mOnQueryingDailyWork = {}
		print "CREATE_SERVICE_SUCCESS CStatisticsCacheMgr module_name=%s use Mysql" % moduleName
		
	def Destroy(self):
		if self.mWorkTimer:
			timermanager.timerManager.delTimer(self.mWorkTimer)
			self.mWorkTimer = None
		self.mSystem = None
	
	def NeteaseMonitorGetter(self):
		tsks = []
		tsks.append(self.GetRecentData)
		return tsks
	
	def GetRecentData(self, totalTick):
		ps = []
		for point in self.mMonitorTasks:
			ps.append(point)
		self.mMonitorTasks = []
		return ps
	#------------------------------------------------------------------------------		
	def InitWorkStartTime(self):
		maxFollowUpTime = int(time.time())
		# 调试代码：追溯时间
		maxFollowUpTime -= 86400 * 15
		# 每日起点时间戳，同时也是上一次统计时间
		local = time.localtime(maxFollowUpTime)
		self.mLastFullDailyTime = time.mktime((local.tm_year,local.tm_mon,local.tm_mday,0,0,0,0,0,0))
		self.mLastFullDailyTime = int(self.mLastFullDailyTime)
		# 注册驱动缓存检查逻辑的时钟
		self.mWorkTimer = timermanager.timerManager.addRepeatTimer(10, self.DealWorkTimer)
	#------------------------------------------------------------------------------
	def DealWorkTimer(self):
		now = int(time.time())
		# 为了防止日志等数据尚未同步到数据库
		# 统计数据生成的逻辑，需要强制延后一段时间才执行
		# 每日统计
		needWorkTime = self.mLastFullDailyTime + OneDaySecond
		if (now - OneDayDelayTime) >= needWorkTime:
			self.DoOneDayWork(now, needWorkTime)
	#----------------------------------------------------------------------------------------------
	def DoOneDayWork(self, now, needWorkTime):
		self.mLastFullDailyTime = needWorkTime
		print "DoOneDayWork", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(needWorkTime))
		# needWorkTime 是凌晨零点零分零秒，对应统计时间范围为
		# needWorkTime-86400 -- needWorkTime-1
		todayStart = needWorkTime - OneDaySecond
		todayEnd = needWorkTime - 1
		local = time.localtime(todayStart)
		date = "%04d-%02d-%02d" % (local.tm_year, local.tm_mon, local.tm_mday)
		cacheData = {"today_start":todayStart,}
		# 每月1日统计MAU
		if (local.tm_mday == 1):
			lastMonthStart = self.GetLastMonthStart(local.tm_year, local.tm_mon)
			self.QueryMonthAccountLogin("account_month_login", cacheData, date, lastMonthStart, todayStart-1)
		# 每日统计
		self.QueryDailyAccountNew("account_new", cacheData, date, todayStart, todayEnd)
		self.QueryDailyAccountLogin("account_login", cacheData, date, todayStart, todayEnd)
		self.QueryDailyAccountPayCount("account_pay_count", cacheData, date, todayStart, todayEnd)
		self.QueryDailyPay("account_pay", cacheData, date, todayStart, todayEnd)
		self.QueryDailyOltime("account_oltime", cacheData, date, todayStart, todayEnd)
		self.QueryDailyOltimeNew("account_new_oltime", cacheData, date, todayStart, todayEnd)
		self.QueryDailyLoginCnt("account_login_cnt", cacheData, date, todayStart, todayEnd)
		self.mOnQueryingDailyWork[date] = cacheData
		# 留存率比较特殊，排队干吧
		# 次日留存率：每日登录账号中，昨日新建账号的数量|昨日新建账号的数量
		ctimeStart = todayStart - OneDaySecond
		ctimeEnd = ctimeStart + OneDaySecond - 1
		self.StartRetainSingleQuery("retain1", date, ctimeStart, ctimeEnd)
		# 三日留存率：每日登录账号中，-2day新建账号的数量|-2day新建账号的数量
		ctimeStart = todayStart - OneDaySecond*2
		ctimeEnd = ctimeStart + OneDaySecond - 1
		self.StartRetainSingleQuery("retain3", date, ctimeStart, ctimeEnd)
		# 七日留存率：每日登录账号中，-6day新建账号的数量|-6day新建账号的数量
		ctimeStart = todayStart - OneDaySecond*6
		ctimeEnd = ctimeStart + OneDaySecond - 1
		self.StartRetainSingleQuery("retain7", date, ctimeStart, ctimeEnd)

	# 每日新增账号数
	def QueryDailyAccountNew(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT count(*) FROM %s " % PlayerStaticTable
		sql += "WHERE ctime>=%s AND ctime<=%s"
		params = (todayStart, todayEnd)
		callback = lambda records:self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日登录账号数
	def QueryDailyAccountLogin(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT count(*) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s"
		params = (date, )
		callback = lambda records:self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日付费账号数
	def QueryDailyAccountPayCount(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT count(*) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s AND pay>0"
		params = (date,)
		callback = lambda records: self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日总付费
	def QueryDailyPay(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT sum(pay) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s AND pay>0"
		params = (date,)
		callback = lambda records: self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日在线总时长
	def QueryDailyOltime(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT sum(otime) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s"
		params = (date,)
		callback = lambda records: self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日新增用户在线总时长
	def QueryDailyOltimeNew(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT sum(otime) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s AND ctime>=%s AND ctime<=%s"
		params = (date, todayStart, todayEnd)
		callback = lambda records: self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	# 每日登录总人次
	def QueryDailyLoginCnt(self, keyword, cacheData, date, todayStart, todayEnd):
		cacheData[keyword] = None
		sql = "SELECT sum(login_cnt) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s"
		params = (date, )
		callback = lambda records: self.DailySingleQueryCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	def DailySingleQueryCallback(self, records, keyword, date):
		cacheData = self.mOnQueryingDailyWork.get(date, None)
		if cacheData is None:
			return
		if records and records[0] and records[0][0]:
			value = int(records[0][0])
		else:
			value = 0
		cacheData[keyword] = value
		# 只要还有一个数值没有返回，就还不能开始统计
		for k, v in cacheData.iteritems():
			if v is None:
				return
		self.DoDailyWorkFinal(date, cacheData)
	
	# 付费率|人均付费值（钻石）|平均在线时长|新增用户平均在线时长|平均进入次数
	def DoDailyWorkFinal(self, date, cacheData):
		work_time = cacheData['today_start']
		if cacheData['account_login'] <= 0:
			payRate = 0.0
			payDiamand = 0.0
			avgOltime = 0.0
			avgLoginCnt = 0.0
		else:
			payRate = float(cacheData['account_pay_count']) / cacheData['account_login']
			payDiamand = float(cacheData['account_pay']) / cacheData['account_login']
			avgOltime = float(cacheData['account_oltime']) / cacheData['account_login']
			avgLoginCnt = float(cacheData['account_login_cnt']) / cacheData['account_login']
		if cacheData['account_new'] <= 0:
			avg_new_oltime = 0.0
		else:
			avg_new_oltime = float(cacheData['account_new_oltime']) / cacheData['account_new']
		payRate = round(payRate, 4)
		payDiamand = round(payDiamand, 2)
		avgOltime = int(round(avgOltime, 0))
		avg_new_oltime = int(round(avg_new_oltime, 0))
		avgLoginCnt = round(avgLoginCnt, 2)
		# 新增账号数
		ps = monitor.Point().measurement('daily_account_new').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('num', cacheData['account_new'])
		self.mMonitorTasks.append(ps)
		# 登录账号数
		ps = monitor.Point().measurement('daily_account_login').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('num', cacheData['account_login'])
		self.mMonitorTasks.append(ps)
		# 付费总值（钻石）
		ps = monitor.Point().measurement('daily_account_pay').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('pay', cacheData['account_pay'])
		self.mMonitorTasks.append(ps)
		# 付费率
		ps = monitor.Point().measurement('daily_pay_rate').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('pay_rate', payRate)
		self.mMonitorTasks.append(ps)
		# 人均付费值（钻石）
		ps = monitor.Point().measurement('daily_pay_diamand').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('pay_diamand', payDiamand)
		self.mMonitorTasks.append(ps)
		# 平均在线时长
		ps = monitor.Point().measurement('daily_avg_oltime').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('avg_oltime', avgOltime)
		self.mMonitorTasks.append(ps)
		# 新增用户平均在线时长
		ps = monitor.Point().measurement('daily_avg_new_oltime').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('avg_new_oltime', avg_new_oltime)
		self.mMonitorTasks.append(ps)
		# 平均进入次数
		ps = monitor.Point().measurement('daily_avg_login_cnt').tag("env", self.mEnv).change_time(work_time).tag('date', date).field('avg_login_cnt', avgLoginCnt)
		self.mMonitorTasks.append(ps)
		# MAU
		if cacheData.has_key("account_month_login"):
			accountMonthLogin = cacheData["account_month_login"]
			ps = monitor.Point().measurement('month_account_login').tag("env", self.mEnv).change_time(work_time).tag(
				'date', date).field('account_month_login', accountMonthLogin)
			self.mMonitorTasks.append(ps)
			# print "accountMonthLogin done number = %s" % accountMonthLogin
	#---------------------------------------------------------------------------
	# 次日留存率：每日登录账号中，昨日新建账号的数量|昨日新建账号的数量
	# 三日留存率：每日登录账号中，-2day新建账号的数量|-2day新建账号的数量
	# 七日留存率：每日登录账号中，-6day新建账号的数量|-6day新建账号的数量
	def StartRetainSingleQuery(self, keyword, date, ctimeStart, ctimeEnd):
		sql = "SELECT count(*) FROM %s " % PlayerDailyTable
		sql += "WHERE day_str=%s AND ctime>=%s AND ctime<=%s"
		params = (date, ctimeStart, ctimeEnd)
		callback = lambda records:self.QueryDailyRetainCallback(records, keyword, date, ctimeStart, ctimeEnd)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)
	
	def QueryDailyRetainCallback(self, records, keyword, date, ctimeStart, ctimeEnd):
		if records:
			retain = int(records[0][0])
		else:
			retain = 0
		sql = "SELECT count(*) FROM %s " % PlayerStaticTable
		sql += "WHERE ctime>=%s AND ctime<=%s"
		params = (ctimeStart, ctimeEnd)
		callback = lambda records: self.QueryAccountNewByRetainCallback(records, keyword, date, ctimeStart, retain)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	def QueryAccountNewByRetainCallback(self, records, keyword, date, ctimeStart, retain):
		if records:
			accountNew = int(records[0][0])
		else:
			accountNew = 0
		if accountNew <= 0:
			retain_rate = 0.0
		else:
			retain_rate = float(retain) / accountNew
		retain_rate = round(retain_rate, 4)
		# 留存率
		ps = monitor.Point().measurement('daily_%s'%keyword).tag("env", self.mEnv).change_time(ctimeStart).tag('date', date).field('retain_rate', retain_rate)
		self.mMonitorTasks.append(ps)
	#---------------------------------------------------------------------------
	def GetLastMonthStart(self, tm_year, tm_mon):
		if tm_mon > 1:
			year, month = tm_year, tm_mon-1
		else:
			year, month = tm_year-1, 12
		return int(time.mktime((year, month, 1, 0, 0, 0, 0, 0, 0)))

	def QueryMonthAccountLogin(self, keyword, cacheData, date, lastMonthStart, lastMonthEnd):
		cacheData[keyword] = None
		sql = "SELECT count(*) FROM %s " % PlayerStaticTable
		sql += "WHERE uptime>=%s"
		params = (lastMonthStart, )
		callback = lambda records: self.QueryMonthCallback(records, keyword, date)
		mysqlPool.AsyncQueryWithOrderKey(keyword, sql, params, callback)

	def QueryMonthCallback(self, records, keyword, date):
		cacheData = self.mOnQueryingDailyWork.get(date, None)
		if cacheData is None:
			return
		if records and records[0] and records[0][0]:
			value = int(records[0][0])
		else:
			value = 0
		cacheData[keyword] = value
		# 只要还有一个数值没有返回，就还不能开始统计
		for k, v in cacheData.iteritems():
			if v is None:
				return
		self.DoDailyWorkFinal(date, cacheData)
	




