# -*- coding: utf-8 -*-

from Queue import PriorityQueue
import logout
import neteaseShoutScript.shoutConst as shoutConst
import neteaseShoutScript.timermanager as timermanager
import apolloCommon.commonNetgameApi as commonNetgameApi
import time
import weakref
import json


class ShoutMgr(object):
	def __init__(self, system, moduleName):
		super(ShoutMgr, self).__init__()
		self.mInvolvedServers = set()
		self.mFormerUsers = {}
		self.mPriorityQueue = PriorityQueue()
		self.mSystem = weakref.proxy(system)
		self.mModuleName = moduleName
		self.mPopOneAndPushTimer = timermanager.timerManager.addTimer(1, self.PopOneAndPush)

		self.mSystem.RegisterRpcMethod(moduleName, shoutConst.PlayerAiringEvent, self.OnPlayerAiringReq)

	def PopOneAndPush(self):
		"""
		从等待广播的喇叭信息中，根据优先级POP最前的一条消息，群发给server转发给client显示，
		每次执行的延时为喇叭显示时间的一半，是为了保证client的等待显示队列不会比service中真实的等待显示队列先被清空
		"""
		if not self.mPriorityQueue.empty():
			try:
				msg = self.mPriorityQueue.get_nowait()[-1]
				for serverId in self.mInvolvedServers.copy():
					self.mSystem.NotifyToServerNode(serverId, shoutConst.NewMsgEvent, {
						'name': msg[0],
						'content': msg[1],
						'duration': msg[2],
						'bg': msg[3]
					})
				self.mPopOneAndPushTimer = timermanager.timerManager.addTimer(msg[2] // 2 or 1, self.PopOneAndPush)
				return
			except:
				pass
		self.mPopOneAndPushTimer = timermanager.timerManager.addTimer(1, self.PopOneAndPush)

	def Destroy(self):
		if self.mPopOneAndPushTimer:
			timermanager.timerManager.delTimer(self.mPopOneAndPushTimer)
			self.mPopOneAndPushTimer = None
		self.mInvolvedServers = None
		self.mFormerUsers = None
		self.mPriorityQueue = None
		self.mSystem = None

	def OnPlayerAiringReq(self, serverId, callbackId, data):
		"""
		来自server/master的发送喇叭消息事件，根据是否含有admin参数判定是否来自master，事实上拥有很不一样的处理逻辑
		来自server的事件，当【activate=1】时，表示是某个服务器注册自己使用了喇叭插件的事件，用于增加推送事件的发送目标
		"""
		if not data.get('admin'):
			self.mInvolvedServers.add(serverId)
			if data.get('activate'):
				self.mSystem.ResponseToServer(serverId, callbackId, {})
				return
		now = time.time()
		uid = data.get('uid')
		content = data.get('content')
		priority = data.get('priority')
		name = data.get('name')
		duration = data.get('duration', 10)
		bg = data.get('bg', 0)
		if not (uid or data.get('admin')) or not (isinstance(priority, int) and isinstance(bg, int) and isinstance(duration, int) and duration > 0 and isinstance(name, str) and isinstance(content, str) and len(
				content.decode('utf-8')) <= self.mSystem.GetContentWordCountLimit()):
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': shoutConst.RespCodeInvalidParameter,
				'message': '参数有误'
			})
			return
		if not commonNetgameApi.CheckNameValid(content):
			logout.info('OnPlayerAiringReq invalid content: {}'.format(content))
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': shoutConst.RespCodeInvalidParameter,
				'message': '内容存在敏感词'
			})
			return
		if not data.get('admin') and now - self.mFormerUsers.get(uid, 0) < self.mSystem.GetShoutInterval():
			self.mSystem.ResponseToServer(serverId, callbackId, {
				'code': shoutConst.RespCodeInvalidUser,
				'message': '使用频繁'
			})
			return
		if self.mPriorityQueue.qsize() < self.mSystem.GetPendingCountLimit():
			try:
				self.mPriorityQueue.put_nowait(((-priority, now), (name, content, duration, bg)))
				self.mFormerUsers[uid] = now
				self.mSystem.ResponseToServer(serverId, callbackId, {
					'code': shoutConst.RespCodeSuccess,
					'message': '发送成功',
					'entity': {} if data.get('admin') else {'uid': uid}
				})
				return
			except:
				pass
		logout.warning('OnPlayerAiringReq full queue gotta be resolved')
		self.mSystem.ResponseToServer(serverId, callbackId, {
			'code': shoutConst.RespCodeInvalidUser,
			'message': '当前使用喇叭人数过多'
		})
