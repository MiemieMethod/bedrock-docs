# -*- coding: utf-8 -*-

import time
from neteaseStatisticsScript.statisticsConsts import UnicodeConvert
#--------------------------------------------------------------------------------------
class CPlayerDaily(object):
	def __init__(self):
		super(CPlayerDaily, self).__init__()
		self.mLastStateOnline = False
		self.mLastStateServer = 0
	
	def OnCreateFromDatabase(self, record):
		record = UnicodeConvert(record)
		self.mId = record[0]
		self.mUid = record[1]
		date = record[2]
		self.mFloginTime = record[3]
		self.mCTime = record[4]
		self.mLoginCnt = record[5]
		self.mOnline = record[6]
		self.mPay = record[7]
		self.mUpTime = record[8]
		if date is None:
			self.MakeDate(self.mUpTime)
		else:
			try:
				line = date.split("-")
				self.mYear = int(line[0])
				self.mMonth = int(line[1])
				self.mDay = int(line[2])
				self.mDate = date
			except:
				import traceback
				traceback.print_exc()
				self.MakeDate(self.mUpTime)
	
	def GetSqlParams(self):
		return (self.mUid, self.mDate, self.mFloginTime, self.mCTime, self.mLoginCnt, self.mOnline, self.mPay, self.mUpTime)

	def SetUniqueId(self, _id):
		self.mId = _id
	#----------------------------------------------------------------------------------
	def IsSameDay(self, timestamp):
		local = time.localtime(timestamp)
		if self.mYear == local.tm_year and self.mMonth == local.tm_mon and self.mDay == local.tm_mday:
			return True
		else:
			return False
	
	# 应用环境上，首先排除了同一天的情况
	# 所以这里不判断是不是同一天了
	def IsFutureDay(self, timestamp):
		return timestamp > self.mUpTime
	
	def MakeDate(self, timestamp):
		local = time.localtime(timestamp)
		self.mYear = local.tm_year
		self.mMonth = local.tm_mon
		self.mDay = local.tm_mday
		self.mDate = "%04d-%02d-%02d" % (self.mYear, self.mMonth, self.mDay)
	#----------------------------------------------------------------------------------
	def IncrOnlineToDayEnd(self):
		dayEnd = int(time.mktime((self.mYear, self.mMonth, self.mDay, 23, 59, 59, 0, 0, 0)))
		plus = dayEnd - self.mUpTime
		self.mOnline += plus
		self.mUpTime = dayEnd
		return {'$inc':{'online':plus}, '$set':{'uptime':self.mUpTime}}
	#----------------------------------------------------------------------------------
	def OnCreateByLogin(self, uid, when, ctime, serverId):
		self.mUid = uid
		self.mUpTime = when
		self.mFloginTime = when
		self.mCTime = ctime
		self.mLoginCnt = 1
		self.mOnline = 0
		self.mPay = 0
		self.MakeDate(when)
		self.mLastStateOnline = True
		self.mLastStateServer = serverId

	def UpdateByLogin(self, when, serverId):
		self.mUpTime = when
		self.mLoginCnt += 1
		self.mLastStateOnline = True
		self.mLastStateServer = serverId
		return "login_cnt", 1
	#----------------------------------------------------------------------------------
	def OnCreateByOnline(self, uid, when, ctime, plusOltime, serverId):
		self.mUid = uid
		self.mUpTime = when
		self.mFloginTime = when
		self.mCTime = ctime
		self.mLoginCnt = 1	# 在线状态下过了一天，那么第二天就自动算登录一次
		self.mOnline = plusOltime
		self.mPay = 0
		self.MakeDate(when)
		self.mLastStateOnline = True
		self.mLastStateServer = serverId

	def UpdateByOnline(self, when, plusOltime, serverId):
		self.mUpTime = when
		self.mOnline += plusOltime
		self.mLastStateOnline = True
		self.mLastStateServer = serverId
		return "otime", plusOltime
	#----------------------------------------------------------------------------------
	def OnCreateByLogout(self, uid, when, ctime, plusOltime, serverId):
		self.mUid = uid
		self.mUpTime = when
		self.mFloginTime = when
		self.mCTime = ctime
		self.mLoginCnt = 1	# 在线状态下过了一天，那么第二天就自动算登录一次
		self.mOnline = plusOltime
		self.mPay = 0
		self.MakeDate(when)
		self.mLastStateOnline = False
		self.mLastStateServer = serverId

	def UpdateByLogout(self, when, plusOltime, serverId):
		self.mUpTime = when
		self.mOnline += plusOltime
		self.mLastStateOnline = False
		return "otime", plusOltime
	#----------------------------------------------------------------------------------
	def OnCreateByPay(self, uid, when, ctime, pay, serverId):
		self.mUid = uid
		self.mUpTime = when
		self.mFloginTime = when
		self.mCTime = ctime
		self.mLoginCnt = 1	# 在线状态下过了一天，那么第二天就自动算登录一次
		self.mOnline = 0
		self.mPay = pay
		self.MakeDate(when)
		self.mLastStateOnline = True
		self.mLastStateServer = serverId

	def UpdateByPay(self, when, pay, serverId):
		self.mUpTime = when
		self.mPay += pay
		self.mLastStateOnline = True
		self.mLastStateServer = serverId
		return "pay", pay
#--------------------------------------------------------------------------------------
class CPlayerStatic(object):
	def __init__(self):
		super(CPlayerStatic, self).__init__()
		self.mLastStateOnline = False
		self.mLastStateServer = 0

	def OnCreateFromDatabase(self, record):
		record = UnicodeConvert(record)
		self.mUid = record[0]
		self.mCTime = record[1]
		self.mLoginCnt = record[2]
		self.mOnline = record[3]
		self.mPay = record[4]
		self.mUpTime = record[5]

	def OnCreate(self, uid, ctime, loginCnt, online, pay):
		self.mUid = uid
		self.mUpTime = ctime+online
		self.mCTime = ctime
		self.mLoginCnt = loginCnt
		self.mOnline = online
		self.mPay = pay

	def GetSqlParams(self):
		return (self.mUid, self.mCTime, self.mLoginCnt, self.mOnline, self.mPay, self.mUpTime)
	#-----------------------------------------------------------------------------
	#-----------------------------------------------------------------------------
	
	
	
	
	
	