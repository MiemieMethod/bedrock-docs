# -*- coding: utf-8 -*-
import time
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from neteaseStatisticsScript.statisticsConsts import ModNameSpace, ServerEvent
import lobbyGame.netgameApi as netgameApi

class StatisticsServerSys(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.mServerId = netgameApi.GetServerId()
		self.mPlayerIdToUid = {}
		self.mFrame = 0
		self.mCheckFrame = 450		# 每15（*30）秒检查一次是否需要发送在线事件
		self.mStepOnlineTime = 300	# 每5分钟发送一次在线事件
		#
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							"AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							"DelServerPlayerEvent", self, self.OnDelerverPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		# 调试用代码
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'ServerChatEvent', self, self.OnServerChatEvent)
		self.mTestObj = None

	def StopRunText(self):
		if self.mTestObj:
			self.mTestObj.Destroy()
			self.mTestObj = None

	def Destroy(self):
		self.StopRunText()
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							"AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							"DelServerPlayerEvent", self, self.OnDelerverPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							'ServerChatEvent', self, self.OnServerChatEvent)

	def OnServerChatEvent(self, data):
		messages = data['message'].split()
		command = messages[0]
		if command == "test":
			from neteaseStatisticsScript.statisticsTest import CStatisticsTest
			self.mTestObj = CStatisticsTest(self)
			self.mTestObj.StartRun(int(messages[1]), int(messages[2]))
	# --------------------------------------------------------------------------------------
	# 封装的事件发送函数
	# 登录事件
	def sendLoginEvent(self, uid, when):
		args = {
			"keyword": "login",
			"uid": uid,
			"when": when,
		}
		self.RequestToService(ModNameSpace, ServerEvent.SyncUserStatus, args)

	# 在线事件
	def sendOnlineEvent(self, uid, when, oltime, d_oltime):
		args = {
			"keyword": "online",
			"uid": uid,
			"when": when,
			"oltime": oltime,
			"d_oltime": d_oltime,
		}
		self.RequestToService(ModNameSpace, ServerEvent.SyncUserStatus, args)

	# 登出事件
	def sendLogoutEvent(self, uid, when, oltime, d_oltime):
		args = {
			"keyword": "logout",
			"uid": uid,
			"when": when,
			"oltime": oltime,
			"d_oltime": d_oltime,
		}
		self.RequestToService(ModNameSpace, ServerEvent.SyncUserStatus, args)

	# 付费事件
	def sendPayEvent(self, uid, when, pay, orderKey):
		args = {
			"keyword": "pay",
			"uid": uid,
			"when": when,
			"pay": pay,
			"orderkey": orderKey,
		}
		self.RequestToService(ModNameSpace, ServerEvent.SyncUserStatus, args)

	def sendPayEventByPlayerId(self, playerId, pay, orderKey):
		uid = netgameApi.GetPlayerUid(playerId)
		if uid <= 0:
			return
		self.sendPayEvent(uid, int(time.time()), pay, orderKey)
	# ------------------------------------------------------------------------------------
	def OnAddServerPlayer(self, data):
		playerId = data.get('id','-1')
		uid = netgameApi.GetPlayerUid(playerId)
		if uid <= 0:
			return
		now = int(time.time())
		isTransfer = data.get("isTransfer", False)
		if isTransfer:
			print "%s login for transfer do not send login event" % uid
		else:
			self.sendLoginEvent(uid, now)
			print "%s login real do send login event" % uid
		self.mPlayerIdToUid[playerId] = {
			"uid": uid,
			"login_time": now,
			"last_send_online": now,
		}

	def OnDelerverPlayer(self, data):
		playerId = data.get('id','-1')
		localData = self.mPlayerIdToUid.get(playerId, None)
		if localData is None:
			return
		now = int(time.time())
		uid, loginTime, lastSendOnlineTime = localData["uid"], localData["login_time"], localData["last_send_online"]
		isTransfer = data.get("isTransfer", False)
		if isTransfer:
			print "%s logout for transfer send online replace logout" % uid
			self.sendOnlineEvent(uid, now, now-loginTime, now-lastSendOnlineTime)
		else:
			self.sendLogoutEvent(uid, now, now-loginTime, now-lastSendOnlineTime)
		del self.mPlayerIdToUid[playerId]

	def OnServerWillShutDown(self, data):
		now = int(time.time())
		for playerId, localData in self.mPlayerIdToUid.iteritems():
			uid, loginTime, lastSendOnlineTime = localData["uid"], localData["login_time"], localData["last_send_online"]
			self.sendLogoutEvent(uid, now, now-loginTime, now-lastSendOnlineTime)
		self.mPlayerIdToUid.clear()

	def Update(self):
		self.mFrame += 1
		if self.mTestObj:
			self.mTestObj.Update(self.mFrame)
		if self.mFrame % self.mCheckFrame == 0:
			self.DoCheckAndSendOnline()

	def DoCheckAndSendOnline(self):
		now = int(time.time())
		for playerId, localData in self.mPlayerIdToUid.iteritems():
			uid, loginTime, lastSendOnlineTime = localData["uid"], localData["login_time"], localData["last_send_online"]
			passTime = now - lastSendOnlineTime
			if passTime < self.mStepOnlineTime:
				continue
			self.sendOnlineEvent(uid, now, now-loginTime, passTime)
			localData["last_send_online"] = now
