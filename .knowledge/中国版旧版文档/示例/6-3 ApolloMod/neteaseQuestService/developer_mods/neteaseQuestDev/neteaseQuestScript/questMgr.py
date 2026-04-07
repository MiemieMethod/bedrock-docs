# -*- coding: utf-8 -*-

import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import logout
import neteaseQuestScript.questConst as questConst
# import neteaseQuestScript.timermanager as timermanager
import time
import weakref
import json


class QuestMgr(object):
	"""
	该mod的service逻辑类
	主要用于处理中转master的运营指令请求到各游戏服进程
	处理玩家转服时查询数据库的问题
	"""

	def __init__(self, system, moduleName):
		super(QuestMgr, self).__init__()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mQuestInvolvedServers = set()
		self.mQuestSwitchedPlayers = set()
		self.mQuestRecordedPlayers = set()

		self.mSystem.RegisterRpcMethod(moduleName, questConst.PushQuestDataEvent, self.OnPushQuestDataReq)
		self.mSystem.RegisterRpcMethod(moduleName, questConst.PullQuestDataEvent, self.OnPullQuestDataReq)
		self.mSystem.RegisterRpcMethod(moduleName, questConst.QueryQuestDataEvent, self.OnQueryQuestDataReq)
		self.mSystem.RegisterRpcMethod(moduleName, questConst.UpdateQuestDataEvent, self.OnUpdateQuestDataReq)

	def Destroy(self):
		self.mSystem = None

	def OnUpdateQuestDataReq(self, serverId, callbackId, data):
		# 中转更新任务数据请求
		logout.info('OnUpdateQuestDataReq data: {}'.format(data))
		clientId = data.get('clientId')
		requestBody = data.get('requestBody')
		for serverId in self.mQuestInvolvedServers.copy():
			self.mSystem.NotifyToServerNode(serverId, questConst.UpdateQuestDataEvent, {'clientId': clientId, 'requestBody': requestBody})

	def OnQueryQuestDataReq(self, serverId, callbackId, data):
		# 中转查询任务数据请求
		logout.info('OnQueryQuestDataReq data: {}'.format(data))
		uid = data.get('uid')
		clientId = data.get('clientId')
		if not (uid and clientId):
			return
		for serverId in self.mQuestInvolvedServers.copy():
			self.mSystem.NotifyToServerNode(serverId, questConst.QueryQuestDataEvent, {'clientId': clientId, 'uid': uid})

	def OnPushQuestDataReq(self, serverId, callbackId, data):
		uid = data.get('uid')
		if not uid:
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': questConst.RespCodeInvalidParameter,
				'message': ''
			})
			return
		if uid in self.mQuestSwitchedPlayers:
			self.mQuestSwitchedPlayers.discard(uid)
			data = {'uid': uid}
			if data.get('debut'):
				data['debut'] = 1
			for serverId in self.mQuestInvolvedServers.copy():
				self.mSystem.NotifyToServerNode(serverId, questConst.PushQuestDataEvent, data)
		else:
			if data.get('debut'):
				self.mQuestSwitchedPlayers.add((uid, 1))
			self.mQuestSwitchedPlayers.add((uid,))
		self.mSystem.ResponseToServer(serverId, callbackId, {})

	def OnPullQuestDataReq(self, serverId, callbackId, data):
		logout.info('OnPullQuestDataReq data: {}'.format(data))
		uid = data.get('uid')
		if not uid:
			logout.error('[neteaseQuest] can not get uid OnPullQuestDataReq')
			return
		self.mQuestInvolvedServers.add(serverId)
		if data.get('debut'):
			self.mQuestRecordedPlayers.add(uid)
			self.mQuestSwitchedPlayers.discard((uid, 1))
			self.mQuestSwitchedPlayers.discard((uid,))
			self.mQuestSwitchedPlayers.discard(uid)
			return
		if uid not in self.mQuestRecordedPlayers:
			self.mQuestRecordedPlayers.add(uid)
			self.mQuestSwitchedPlayers.discard((uid, 1))
			self.mQuestSwitchedPlayers.discard((uid,))
			self.mQuestSwitchedPlayers.discard(uid)
			data = {'uid': uid, 'debut': 1}
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': questConst.RespCodeSuccess,
				'message': '',
				'entity': data
			})
			return
		if (uid,) in self.mQuestSwitchedPlayers:
			self.mQuestSwitchedPlayers.discard((uid,))
			data = {'uid': uid}
			if (uid, 1) in self.mQuestSwitchedPlayers:
				self.mQuestSwitchedPlayers.discard((uid, 1))
				data['debut'] = 1
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': questConst.RespCodeSuccess,
				'message': '',
				'entity': data
			})
		else:
			self.mQuestSwitchedPlayers.add(uid)
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': questConst.RespCodeInvalidUser,
			})
