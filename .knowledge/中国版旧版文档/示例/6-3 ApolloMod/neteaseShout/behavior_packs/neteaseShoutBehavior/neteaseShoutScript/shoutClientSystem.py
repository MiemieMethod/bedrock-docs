# -*- coding: utf-8 -*-

import math, time
import neteaseShoutScript.shoutConst as shoutConst
import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()


class MyMsg:
	def __init__(self, name, content, duration, bg):
		self.name = name + '：'  # 27
		self.content = content + ' ' * 44  # 33, 70
		self.duration = duration
		self.bg = bg

	def prepare(self, node):
		ls, lp, rs, rp = node.quad
		x = math.ceil(len(self.name) / 27.0 * ls[0])
		node.SetSize(node.m_name_text, (x, ls[1]))
		node.SetSize(node.m_content_text, (rs[0] + ls[0] - x, rs[1]))
		node.SetPosition(node.m_content_text, (1 + rp[0] + x - ls[0], rp[1]))
		node.SetSprite(node.m_content_bg, self.bg)
		# r = int(1.0 * (rs[0] + ls[0] - x) / rs[0] * 70)
		idle = [None for i in xrange(16)]
		head = [self.debut] + idle
		tail = [lambda node: node.SetVisible(node.m_content_bg, False)] + idle
		# if len(self.content[:33].decode('utf-8')) == len(self.content[:33]):
		# 	r = 33
		if len(self.content.strip()) < 33:
			# static
			self.chain = head + [None for i in xrange(self.duration * 30)] + tail
		else:
			now = time.time()
			choices = []
			least = len(self.content.decode('utf-8'))
			total = self.duration * 30
			# for peak in xrange(1, total):
			peak = math.floor(total / 2.0)
			per = int(math.ceil(1.0 * least / peak))
			if peak < least:
				body = [self.flip for i in xrange(least // per + (least % per and 1))]
			else:
				body = [self.flip for i in xrange(least)]
			need = len(body)
			interval = total // need - 1
			if need > 1:
				body = reduce(lambda front, back: (isinstance(front, list) and front or [front]) + [None for i in xrange(interval)] + [back], body)
			body += [None for i in xrange(total - len(body))]
			# 	choices.append((0 - 1.0 * interval / per, per, body))
			# prime = min(choices, key=lambda item: (item[0], item[1]))
			# per = prime[1]
			# body = prime[2]
			self.inc = per
			self.count = per
			self.chain = head + body + tail
			print 'prepare() cost {}s'.format(time.time() - now)

	def debut(self, node):
		node.SetText(node.m_name_text, self.name)
		node.SetText(node.m_content_text, self.content)
		node.SetVisible(node.m_content_bg, True)

	def flip(self, node):
		real = self.content.decode('utf-8')
		node.SetText(node.m_content_text, (real[self.count:] + real[:self.count]).encode('utf-8'))
		self.count += self.inc

	def tick(self, node):
		if self.chain:
			do = self.chain.pop(0)
			do and do(node)
			return self


class ShoutClientSystem(ClientSystem):
	def produce(self):
		try:
			if self.mPendingMsgList:
				return self.mPendingMsgList.pop(0)
		except:
			pass
		return None

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPendingMsgList = []
		self.mShoutUINode = None

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), shoutConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(shoutConst.ModName, shoutConst.ServerSystemName, shoutConst.DisplayShoutBoardEvent, self, self.OnDisplayShoutBoard)
		self.ListenForEvent(shoutConst.ModName, shoutConst.ServerSystemName, shoutConst.NewMsgEvent, self, self.OnNewMsg)

	def Destroy(self):
		self.mShoutUINode = None
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), shoutConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(shoutConst.ModName, shoutConst.ServerSystemName, shoutConst.DisplayShoutBoardEvent, self, self.OnDisplayShoutBoard)
		self.UnListenForEvent(shoutConst.ModName, shoutConst.ServerSystemName, shoutConst.NewMsgEvent, self, self.OnNewMsg)

	def OnUiInitFinished(self, *args):
		# 注册UI 详细解释参照《UI API》
		clientApi.RegisterUI(shoutConst.ModName, shoutConst.shoutUIName, shoutConst.shoutUIClsPath, shoutConst.shoutUIScreenDef)
		# 创建UI 详细解释参照《UI API》
		clientApi.CreateUI(shoutConst.ModName, shoutConst.shoutUIName, {"isHud": 1})
		self.mShoutUINode = clientApi.GetUI(shoutConst.ModName, shoutConst.shoutUIName)
		if self.mShoutUINode:
			self.mShoutUINode.InitScreen()
		else:
			print '==== %s ====' % 'create UI: %s failed' % shoutConst.shoutUIScreenDef

	def OnDisplayShoutBoard(self, data):
		print 'OnDisplayShoutBoard', data
		if self.mShoutUINode:
			self.mShoutUINode.open(data)

	def OnNewMsg(self, msg):
		print 'OnNewMsg', msg
		if msg['duration']:
			self.mPendingMsgList.append(MyMsg(msg['name'], msg['content'], msg['duration'], msg['bg']))
