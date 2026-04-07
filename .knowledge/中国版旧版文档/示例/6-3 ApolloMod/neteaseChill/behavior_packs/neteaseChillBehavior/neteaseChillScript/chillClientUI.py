# -*- coding: utf-8 -*-

import neteaseChillScript.chillConst as chillConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class ChillScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init ChillScreen'

		self.m_chill_panel = '/money_panel'
		self.m_chill_panel_close_btn = '/money_panel/money_bg/close_btn'
		self.m_chill_panel_alive = False

		self.m_chill_reward_banner = '/money_panel/money_bg/money_banner'
		self.m_chill_reward_bg = '/money_panel/money_bg/prize_bg_{0}'
		self.m_chill_reward_pic = '/money_panel/money_bg/prize_bg_{0}/prize_{0}'
		self.m_chill_reward_count_text = '/money_panel/money_bg/prize_bg_{0}/prize_count_{0}'
		self.m_chill_reward_title_text = '/money_panel/money_bg/money_title'
		self.m_chill_reward_desc_text = '/money_panel/money_bg/prize_text'
		self.m_chill_reward_interact_btn = '/money_panel/money_bg/interact_btn'
		self.m_chill_reward_status_text = '/money_panel/money_bg/interact_btn/prize_status_text'

		self.m_qualified = 0

		self.m_selected = None
		self.m_count = 0

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'ChillScreen Create'

		self.AddTouchEventHandler(self.m_chill_panel_close_btn, self.on_touch_btn_close)
		self.AddTouchEventHandler(self.m_chill_reward_interact_btn, self.on_touch_btn_interact)

	def InitScreen(self):
		print '==== %s ====' % 'ChillScreen Init'

		self.SetVisible(self.m_chill_panel, False)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		self.m_count += 1

		if not self.m_count % 16:
			self.m_count = 0
			if self.m_selected:  # 这个标志的作用为防止瞬间多次点击导致多发送请求，所以发请求的逻辑统一在此处理
				if self.m_qualified == 1:
					self.recv()
				else:
					self.achv()
				self.m_selected = None

	def on_touch_btn_interact(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			print '==== %s ====' % 'ChillScreen interact TouchUp'
			clientApi.SetResponse(True)
			if self.m_qualified == 1:
				self.m_selected = True
			elif self.m_qualified == -1:
				self.SetTouchEnable(self.m_chill_reward_interact_btn, False)
				self.SetText(self.m_chill_reward_status_text, '已领取')
			else:
				self.m_selected = True
			print self.m_qualified
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

	def achv(self):
		# 跳转充值商城
		if not self.m_qualified:
			clientApi.GetSystem(chillConst.ModName, chillConst.ClientSystemName).NotifyToServer(
				chillConst.NavigateToShopEvent,
				{'playerId': clientApi.GetLocalPlayerId()}
			)

	def recv(self):
		if self.m_qualified == 1:
			clientApi.GetSystem(chillConst.ModName, chillConst.ClientSystemName).NotifyToServer(
				chillConst.PlayerRecvChillRewardEvent,
				{'playerId': clientApi.GetLocalPlayerId()}
			)

	def open(self, data):
		qualified = data.get('qualified')
		exhibits = data.get('exhibits')
		desc = data.get('desc', '')
		title = data.get('title', '')
		if None in (qualified, exhibits):
			print ''
			return
		exhibits = list(exhibits)
		d = {  # 不同数量的奖励使用格子的位置不一样
			1: (3,),
			2: (2, 3,),
			3: (2, 3, 4,),
			4: (1, 2, 3, 4,),
			5: (1, 2, 3, 4, 5,)
		}.get(len(exhibits) > 5 and 5 or len(exhibits), ())
		for i in xrange(1, 6):
			if i in d:
				e = exhibits.pop(0)
				self.SetVisible(self.m_chill_reward_bg.format(i), True)
				self.SetSprite(self.m_chill_reward_pic.format(i), e['display_icon'])
				self.SetText(self.m_chill_reward_count_text.format(i), str(e['display_count']))
			else:
				self.SetVisible(self.m_chill_reward_bg.format(i), False)
		self.SetText(self.m_chill_reward_desc_text, desc)
		self.SetText(self.m_chill_reward_title_text, title)
		self.refresh({'qualified': qualified})
		self.m_chill_panel_alive = True
		self.SetVisible(self.m_chill_panel, self.m_chill_panel_alive)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)

	def refresh(self, data):
		# 奖励领取状态更新
		qualified = data.get('qualified')
		if qualified is None:
			return
		if self.m_qualified == qualified:
			return
		self.m_qualified = qualified
		if self.m_qualified == 1:
			self.SetTouchEnable(self.m_chill_reward_interact_btn, True)
			self.SetText(self.m_chill_reward_status_text, '领取')
		elif self.m_qualified == -1:
			self.SetTouchEnable(self.m_chill_reward_interact_btn, False)
			self.SetText(self.m_chill_reward_status_text, '已领取')
		else:
			self.SetTouchEnable(self.m_chill_reward_interact_btn, True)
			self.SetText(self.m_chill_reward_status_text, '前往兑换')

	def close(self):
		self.SetVisible(self.m_chill_panel, False)
		self.m_chill_panel_alive = False
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)
		# clientApi.GetSystem(chillConst.ModName, chillConst.ClientSystemName).NotifyToServer(
		# 	'PlayerChillOutEvent',
		# 	{'playerId': clientApi.GetLocalPlayerId()}
		# )
		pass
