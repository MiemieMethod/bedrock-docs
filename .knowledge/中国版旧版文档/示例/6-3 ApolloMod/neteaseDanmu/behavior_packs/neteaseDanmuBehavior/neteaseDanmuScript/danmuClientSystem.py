# -*- coding: utf-8 -*-

import math
import neteaseDanmuScript.danmuConst as danmuConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class MyMsg:
	"""
	单条消息的封装
	"""

	def __init__(self, icon, content, mode, rand, fake=False):
		self.icon = icon
		self.content = content
		self.mode = mode
		self.rand = rand
		self.fake = False

	def prepare(self, node, w):
		if self.mode == 'r':
			node.SetPosition(w.p, node.pm[w.o])
			if self.icon == -1:
				node.SetVisible(w.p + '/icon', False)
			else:
				node.SetSprite(w.p + '/icon', self.icon)
				node.SetVisible(w.p + '/icon', True)
		tp = self.mode == 'r' and (w.p + '/text') or w.p
		node.SetText(tp, self.content)
		u = tp + (self.mode == 'r' and '/tru' or '/tmu')
		node.SetVisible(u, self.fake)
		if self.mode == 'r':
			width = 190.0 + node.width  # json中文本框的长度为190.0
			pos = node.pm[w.o]
			dt = self.rand / 30.0  # 每帧移动的量
			self.chain = [lambda node, w, i=i: node.SetPosition(w.p, (pos[0] - dt * (i + 1), pos[1])) for i in xrange(int(math.ceil(width / self.rand) * 30))]  # 直接生成每一帧需要执行的任务序列
		else:
			self.chain = [None for i in xrange(self.rand * 30)]  # 中部消息不需要做什么

	def tick(self, node, w):
		if self.chain:
			do = self.chain.pop(0)
			do and do(node, w)
		else:
			# 播放完毕完毕
			w.msg = None  # 清除通道内自身的引用，通道就会判定为运作结束


class DanmuClientSystem(ClientSystem):
	"""
	该mod的客户端类
	接收并消费弹幕
	"""

	def shift(self, msg):
		"""
		没有弹幕通道可以播放本条消息
		放回列表中
		"""

		if msg.fake:
			# 自己发的弹幕是一个“伪造”的消息，服务端成功接收一条消息会直接返回本地玩家发的弹幕消息，以达到自己的发言较快能够显示出来的效果
			self.mPretendMsgList.insert(0, msg)
		else:
			self.mPendingMsgList.insert(1, msg)

	def produce(self, closure={}):
		"""
		按照特定的规则返回一条弹幕信息（以MyMsg对象的方式）
		"""
		if closure.get('skip'):
			closure['skip'] = False  # 上次取的是自己的消息，这次取其他的
		else:
			try:
				if self.mPretendMsgList:
					msg = self.mPretendMsgList.pop(0)
					closure['skip'] = True  # 自己的消息不连着两条发出来，下次取先取其他的
					return MyMsg(msg['icon'], msg['content'], msg['mode'], msg['rand'], True)
			except:
				pass

		try:
			if self.mPendingMsgList:
				msg = self.mPendingMsgList.pop(0)
				if msg['playerId'] == self.mPlayerId:
					# 自己的消息不用再显示了
					return None
				return MyMsg(msg['icon'], msg['content'], msg['mode'], msg['rand'])
		except:
			return None

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mPartition = None
		self.mSwitch = False
		self.mPendingMsgList = []
		self.mPretendMsgList = []

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), danmuConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DisplayDanmuFrameEvent', self, self.OnDisplayDanmuFrame)  # 服务端通知打开弹幕操作界面
		self.ListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DanmuPollEvent', self, self.OnDanmuPoll)  # 正常弹幕推送
		self.ListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DanmuPublishEvent', self, self.OnDanmuPublish)  # 自己发的弹幕成功发送，需要作优先显示

	@property
	def Partition(self):
		return self.mPartition  # 弹幕可用屏幕范围，详见mod.json

	@property
	def Switch(self):
		return self.mSwitch  # 弹幕开关

	@Switch.setter
	def Switch(self, flag):
		if flag:
			if not self.Switch:
				# 之前是关闭现在要开启
				self.mDanmuViewUINode.appear()
		elif self.Switch:
			# 之前是开启现在要关闭
			self.mPretendMsgList = []
			self.mPendingMsgList = []
			self.mDanmuViewUINode.disable()  # 关闭显示，但不影响正在运作的通道依旧正常运作，所以能够再短时间内瞬间打开依然看到有弹幕在播放

		self.mSwitch = flag

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), danmuConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DisplayDanmuFrameEvent', self, self.OnDisplayDanmuFrame)
		self.UnListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DanmuPollEvent', self, self.OnDanmuPoll)
		self.UnListenForEvent(danmuConst.ModName, danmuConst.ServerSystemName, 'DanmuPublishEvent', self, self.OnDanmuPublish)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(danmuConst.ModName, 'danmuUI', "neteaseDanmuScript.danmuUI.DanmuFrame", 'danmuUI.main')
		# 创建UI 详细解释参照《UI API》
		self.mDanmuUINode = clientApi.CreateUI(danmuConst.ModName, 'danmuUI', {"isHud": 1})
		if self.mDanmuUINode:
			self.mDanmuUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: danmuUI.main failed'
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(danmuConst.ModName, 'danmuViewUI', "neteaseDanmuScript.danmuViewUI.DanmuScreen", 'danmuViewUI.main')
		# 创建UI 详细解释参照《UI API》
		self.mDanmuViewUINode = clientApi.CreateUI(danmuConst.ModName, 'danmuViewUI', {"isHud": 1})
		if self.mDanmuViewUINode:
			self.mDanmuViewUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: danmuViewUI.main failed'

	def Update(self):
		pass

	def OnDisplayDanmuFrame(self, data):
		"""
		服务端通知打开弹幕操作界面
		"""
		print 'OnDisplayDanmuFrame', data
		if self.mDanmuUINode:
			self.mDanmuUINode.open(data)

	def OnDanmuPoll(self, data):
		"""
		普通弹幕推送
		"""
		print 'OnDanmuPoll', data
		self.mPartition = data['protocol']
		if self.Switch:
			# 开关是开启中才将消息存入
			self.mPendingMsgList.extend(data['latest'])
			if len(self.mPendingMsgList) > 100:
				self.mPendingMsgList = self.mPendingMsgList[-100:]  # 最多只保留最新的100条，由于自己的消息优先显示了（在PretendMsgList列表中），不会出现自己发的消息被清掉的情况

	def OnDanmuPublish(self, msg):
		"""
		自己发的弹幕成功发送，需要作优先显示
		"""
		print 'OnDanmuPublish', msg
		if self.Switch:
			self.mPretendMsgList.append(msg)  # 自己发的消息的列表
