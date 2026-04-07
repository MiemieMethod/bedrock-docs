# -*- coding: utf-8 -*-

import neteaseDailyScript.dailyConst as dailyConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class DailyScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init DailyScreen'

		self.m_daily_panel = '/daily_panel'
		self.m_daily_panel_close_btn = '/daily_panel/daily_bg/close_btn'
		self.m_daily_panel_alive = False

		self.m_daily_reward_bg = '/daily_panel/daily_bg/prize_bg/time_{0}/prize_card_{0}'
		self.m_daily_reward_pic = '/daily_panel/daily_bg/prize_bg/time_{0}/prize_{0}'
		self.m_daily_reward_count_text = '/daily_panel/daily_bg/prize_bg/time_{0}/prize_count_{0}'
		self.m_daily_reward_status_text = '/daily_panel/daily_bg/prize_bg/time_{0}/prize_status_{0}'
		self.m_daily_reward_interact_btn = '/daily_panel/daily_bg/prize_bg/time_{0}/interact_btn_{0}'
		self.m_daily_reward_recv_btn = '/daily_panel/daily_bg/prize_bg/time_{0}/prize_btn_{0}'
		self.m_daily_reward_desc_text = '/daily_panel/daily_bg/prize_text'

		self.m_valid_date = None
		self.m_weekly_cache = None

		self.m_active = None
		self.m_focused = None
		self.m_selected = None
		self.m_count = 0

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'DailyScreen Create'

		self.AddTouchEventHandler(self.m_daily_panel_close_btn, self.on_touch_btn_close)
		for i in xrange(1, 8):
			self.AddTouchEventHandler(self.m_daily_reward_interact_btn.format(i), self.on_touch_btn_interact)
			self.AddTouchEventHandler(self.m_daily_reward_recv_btn.format(i), self.on_touch_btn_recv)

	def InitScreen(self):
		print '==== %s ====' % 'DailyScreen Init'

		if self.m_valid_date is None:
			self.SetVisible(self.m_daily_panel, False)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		self.m_count += 1

		if self.m_focused and self.m_weekly_cache:
			# 有选中
			if self.m_active:  # 初始是None
				# 切换了选中
				self.SetSprite(self.m_daily_reward_bg.format(self.m_active), 'textures/ui/netease_daily/bg03@3x.png')  # 屏蔽旧的选中，切换非选中状态的贴图
			self.m_active = self.m_focused  # 更新为最新选中的序号
			self.m_focused = None  # 清除变量，下次update就不会走进来了
			w = str(int(self.m_active) % 7)
			if w in self.m_weekly_cache:
				# 有配置的描述
				self.SetText(self.m_daily_reward_desc_text, self.m_weekly_cache[w]['display_desc'])
			else:
				self.SetText(self.m_daily_reward_desc_text, '')
			self.SetSprite(self.m_daily_reward_bg.format(self.m_active), 'textures/ui/netease_daily/bg03_active@3x.png')  # 当前选中的设置选中贴图

		if not self.m_count % 16:
			self.m_count = 0
			if self.m_selected:
				# 发请求
				self.recv()
				self.m_selected = None

	def on_touch_btn_interact(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			print '==== %s ====' % 'DailyScreen interact TouchUp'
			clientApi.SetResponse(True)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
			self.m_focused = args["ButtonPath"].split('/')[-1].split('_')[-1]  # 选中的序号，在update里面才改状态
			print self.m_focused
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def on_touch_btn_recv(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			print '==== %s ====' % 'DailyScreen recv TouchUp'
			clientApi.SetResponse(True)
			self.m_selected = args["ButtonPath"].split('/')[-1].split('_')[-1]  # 点击领取按钮，但不立刻发请求，在update里面发，防止连点多发
			print self.m_selected
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def on_touch_btn_close(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			self.close()
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def recv(self):
		print 'recv', self.m_valid_date
		clientApi.GetSystem(dailyConst.ModName, dailyConst.ClientSystemName).NotifyToServer(
			dailyConst.PlayerRecvEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'valid': self.m_valid_date}  # 传递服务端发送下来的日期过去验证，表示领取的是同一天的每日登录奖励
		)

	def open(self, data):
		# 打开界面
		valid = data.get('valid')
		weekly = data.get('weekly')
		recv = data.get('recv')
		if None in (valid, weekly, recv):
			print ''
			return
		self.m_valid_date = valid  # 服务端推下来的日期，类似于'1970-01-01'
		self.m_weekly_cache = weekly  # 奖励配置，详见mod.json
		if self.m_active:
			# 新打开界面不选中任何天
			self.SetSprite(self.m_daily_reward_bg.format(self.m_active), 'textures/ui/netease_daily/bg03@3x.png')
			self.SetText(self.m_daily_reward_desc_text, '')
			self.m_active = None
		for i in xrange(1, 8):
			w = str(i % 7)
			if w in weekly:
				self.SetVisible(self.m_daily_reward_pic.format(i), True)
				self.SetSprite(self.m_daily_reward_pic.format(i), weekly[w]['display_icon'])
				self.SetText(self.m_daily_reward_count_text.format(i), str(weekly[w]['display_count']))
				if recv[int(w)]:
					self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), False)
					self.SetText(self.m_daily_reward_status_text.format(i), '已领取')
				elif i < data['tm_wday'] + 1:
					self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), False)
					self.SetText(self.m_daily_reward_status_text.format(i), '已过期')
				elif i > data['tm_wday'] + 1:
					self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), False)
					self.SetVisible(self.m_daily_reward_recv_btn.format(i), False)
					self.SetVisible(self.m_daily_reward_status_text.format(i), False)
					continue
				else:
					self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), True)
					self.SetText(self.m_daily_reward_status_text.format(i), '领取')
				self.SetVisible(self.m_daily_reward_recv_btn.format(i), True)
				self.SetVisible(self.m_daily_reward_status_text.format(i), True)
			else:
				self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), False)
				self.SetVisible(self.m_daily_reward_recv_btn.format(i), False)
				self.SetVisible(self.m_daily_reward_status_text.format(i), False)
				self.SetVisible(self.m_daily_reward_pic.format(i), False)
				self.SetText(self.m_daily_reward_count_text.format(i), '无')
		self.m_daily_panel_alive = True
		self.SetVisible(self.m_daily_panel, self.m_daily_panel_alive)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)

	def refresh(self, data):
		valid = data.get('valid')
		if valid is None:
			return
		if self.m_valid_date != valid:  # 已经不是同一天了
			# TODO: 考虑重新打开界面
			return
		w = data.get('wday')
		if w is not None:
			i = w or 7
			self.SetTouchEnable(self.m_daily_reward_recv_btn.format(i), False)
			self.SetText(self.m_daily_reward_status_text.format(i), '已领取')
			self.m_selected = None

	def close(self):
		self.SetVisible(self.m_daily_panel, False)
		self.m_daily_panel_alive = False
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)
