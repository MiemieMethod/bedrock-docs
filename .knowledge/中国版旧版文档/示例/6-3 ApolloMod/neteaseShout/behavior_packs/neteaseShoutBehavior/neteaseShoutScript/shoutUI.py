# -*- coding: utf-8 -*-

import neteaseShoutScript.shoutConst as shoutConst
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class ShoutScreen(ScreenNode):
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def set_input_string(self, args):
		self.m_input_string = args["Text"]
		cur = len(self.m_input_string.decode('utf-8'))
		self.SetText(self.m_title_text, '喇叭（{}§r / {}）'.format(
			(cur < self.wc and '§a{}' or (cur == self.wc and '§e{}' or '§c{}')).format(cur), self.wc))
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def get_input_string(self):
		return self.m_input_string

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init ShoutScreen'

		self.m_input_string = ''
		self.m_input_board = '/image0'
		self.m_input_board_alive = False
		self.m_cancel_btn = '/image0/button0'
		self.m_submit_btn = '/image0/button1'
		self.m_title_text = '/image0/label1'
		self.m_content_bg = '/image1'
		self.m_name_text = '/image1/label2'  # 27
		self.m_content_text = '/image1/label3'  # 70

		self._quad = None
		self.wc = 100

		self.producer = None
		self.task = None

	@property
	def quad(self):
		return self._quad

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'ShoutScreen Create'

		self._quad = (
			self.GetSize(self.m_name_text),
			self.GetPosition(self.m_name_text),
			self.GetSize(self.m_content_text),
			self.GetPosition(self.m_content_text)
		)

		self.AddTouchEventHandler(self.m_cancel_btn, self.on_touch_btn_cancel)
		self.AddTouchEventHandler(self.m_submit_btn, self.on_touch_btn_submit)

	def InitScreen(self):
		print '==== %s ====' % 'ShoutScreen Init'

		self.SetVisible(self.m_content_bg, False)
		self.SetVisible(self.m_input_board, False)
		self.m_input_board_alive = False
		self.SetInputEnable(False)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if not self.task:
			if not self.producer:
				self.producer = clientApi.GetSystem(shoutConst.ModName, shoutConst.ClientSystemName)
			task = self.producer.produce()
			if task:
				task.prepare(self)
				self.task = task
		else:
			self.task = self.task.tick(self)

	def on_touch_btn_cancel(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetVisible(self.m_input_board, False)
			self.m_input_board_alive = False
			self.SetInputEnable(False)
			clientApi.SetInputMode(0)

	def on_touch_btn_submit(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			cur = len(self.m_input_string.decode('utf-8'))
			if cur > self.wc:
				print 'too long', cur, self.wc
				return
			clientApi.GetSystem(shoutConst.ModName, shoutConst.ClientSystemName).NotifyToServer(
				shoutConst.PlayerAiringEvent,
				{'playerId': clientApi.GetLocalPlayerId(), 'content': self.m_input_string}
			)
			self.SetVisible(self.m_input_board, False)
			self.m_input_board_alive = False
			self.SetInputEnable(False)
			clientApi.SetInputMode(0)

	def open(self, data):
		wc = data['wc']
		if isinstance(wc, int) and wc != self.wc:
			self.wc = wc
			self.SetEditTextMaxLength('/image0/label0/text_edit_box0', self.wc)
		cur = len(self.m_input_string.decode('utf-8'))
		self.SetText(self.m_title_text, '喇叭（{}§r / {}）'.format(
			(cur < self.wc and '§a{}' or (cur == self.wc and '§e{}' or '§c{}')).format(cur), self.wc))
		self.SetVisible(self.m_input_board, True)
		self.m_input_board_alive = True
		self.SetInputEnable(True)
		clientApi.SetInputMode(1)
