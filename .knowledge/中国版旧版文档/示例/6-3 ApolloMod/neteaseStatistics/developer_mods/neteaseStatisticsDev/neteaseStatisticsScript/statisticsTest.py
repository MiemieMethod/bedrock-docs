# -*- coding: utf-8 -*-
import time
import weakref
import random

class CStatisticsTest(object):
	# 在线，可能的行为：更新在线|下线|付费|顶号|啥都不干
	ONLINE_PROPS = ['online', 'logout', 'pay', 'double_login', 'nothing']
	# 不在线，可能的行为：上线|啥都不干
	OFFLINE_PROPS = ['login', 'nothing', 'nothing', 'nothing']
	def __init__(self, system):
		super(CStatisticsTest, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mCheckFrame = 10
		self.mFakeNow = 0
		self.mFakePlayers = {}

	def Destroy(self):
		self.mSystem = None

	def StartRun(self, uidBegin, playerNumber):
		self.mFakePlayers.clear()
		self.mFakeNow = int(time.time()) - 86400 * 15
		for i in xrange(playerNumber):
			uid = uidBegin + i
			self.mFakePlayers[uid] = {
				"is_online": False,
				"login_time": 0,
				"last_send_online": 0,
				"serverId": 0,
				"orderkey": 1,
			}
		print "CStatisticsTest StartRun"

	def StopRun(self):
		print "CStatisticsTest StopRun"
		self.mSystem.StopRunText()
	# --------------------------------------------------------------------------------------
	def Update(self, mFrame):
		if mFrame % self.mCheckFrame == 0:
			self.RunTestFrame()

	def RunTestFrame(self):
		passTime = random.randint(1200, 1800)
		self.mFakeNow += passTime
		if self.mFakeNow >= int(time.time()):
			self.StopRun()
			return
		for uid, localData in self.mFakePlayers.iteritems():
			if localData['is_online']:
				self.DoWhenPlayerOnline(self.mFakeNow, uid, localData)
			else:
				self.DoWhenPlayerOffline(self.mFakeNow, uid, localData)

	def DoWhenPlayerOnline(self, now, uid, localData):
		action = random.choice(self.ONLINE_PROPS)
		if action == 'online':
			oltime = now - localData['login_time']
			d_oltime = now - localData['last_send_online']
			localData['last_send_online'] = now
			factor = random.randint(1, 100)
			if factor <= 90:  # 10%几率丢包
				self.mSystem.sendOnlineEvent(uid, now, oltime, d_oltime)
		elif action == 'logout':
			oltime = now - localData['login_time']
			d_oltime = now - localData['last_send_online']
			localData['is_online'] = False
			factor = random.randint(1, 100)
			if factor <= 90:  # 10%几率丢包
				self.mSystem.sendLogoutEvent(uid, now, oltime, d_oltime)
		elif action == 'pay':
			pay = random.randint(1, 10) * 100
			serverId = localData['serverId']
			factor = random.randint(1, 100)
			orderkey = localData['orderkey']
			localData['orderkey'] += 1
			if factor <= 90:  # 10%几率丢包
				self.mSystem.sendPayEvent(uid, now, pay, orderkey)
		elif action == 'double_login':
			oltime = now - localData['login_time']
			d_oltime = now - localData['last_send_online']
			localData['login_time'] = now
			localData['last_send_online'] = now
			factor = random.randint(1, 100)
			if factor <= 90:  # 10%几率消息错位
				self.mSystem.sendLogoutEvent(uid, now, oltime, d_oltime)
				self.mSystem.sendLoginEvent(uid, now)
			else:
				self.mSystem.sendLoginEvent(uid, now)
				self.mSystem.sendLogoutEvent(uid, now, oltime, d_oltime)

	def DoWhenPlayerOffline(self, now, uid, localData):
		action = random.choice(self.OFFLINE_PROPS)
		if action == 'login':
			localData['is_online'] = True
			localData['login_time'] = now
			localData['last_send_online'] = now
			factor = random.randint(1, 100)
			if factor <= 90:  # 10%几率丢包
				self.mSystem.sendLoginEvent(uid, now)
