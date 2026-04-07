# -*- coding: utf-8 -*-

import neteaseDanmuScript.danmuConst as danmuConst
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class DanmuFrame(ScreenNode):
	"""
	弹幕操作面板界面
	"""

	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def set_input_string(self, args):
		self.m_input_string = args["Text"]
		self.SetText(self.m_send + '/button_label', str(20 - len(self.m_input_string.decode('utf-8'))))
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def get_input_string(self):
		return self.m_input_string

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init DanmuFrame'

		# '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel'

		self.m_input_string = ''
		self.m_op_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel'
		self.m_op_panel_alive = False
		self.m_back = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/headbar/back'
		self.m_switch = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/headbar/switch'
		self.m_settings = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/footbar/settings'
		self.m_send = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/footbar/send'
		self.m_mask = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask'
		self.m_close = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/close'
		self.m_single = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/single'
		self.m_double = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/double'
		self.m_color = '/{0}_slot{1}/{0}_color{1}'
		self.m_icon = '/{}_icon{}'
		self.m_icons = []

		self.m_cancel_btn = '/image0/button0'
		self.m_submit_btn = '/image0/button1'
		self.m_title_text = '/image0/label1'
		self.m_content_bg = '/image1'
		self.m_name_text = '/image1/label2'  # 27
		self.m_content_text = '/image1/label3'  # 70

		self.color = None
		self.selected_color_order = 0
		self.selected_icon_order = 0

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'DanmuFrame Create'

		self.AddTouchEventHandler(self.m_back, self.on_touch_btn_back)  # 操作界面退出
		self.AddTouchEventHandler(self.m_switch, self.on_touch_btn_switch)  # 弹幕开关
		self.AddTouchEventHandler(self.m_settings, self.on_touch_btn_settings)  # 弹幕设置
		self.AddTouchEventHandler(self.m_send, self.on_touch_btn_send)  # 发送
		self.AddTouchEventHandler(self.m_close, self.on_touch_btn_close)  # 弹幕设置界面退出

		mouse = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/single/single_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/single/single_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.m_single_view = touch
		self.m_single_view_size = self.GetSize(self.m_single_view)
		if not self.m_single_view_size:
			self.m_single_view = mouse
			self.m_single_view_size = self.GetSize(self.m_single_view)
		for i in xrange(5):
			self.AddTouchEventHandler(self.m_single_view + self.m_color.format('single', i), self.on_touch_btn_color)
		self.AddTouchEventHandler(self.m_single_view + self.m_icon.format('single', 0), self.on_touch_btn_icon)
		self.m_single_icon_pos = self.GetPosition(self.m_single_view + self.m_icon.format('single', 0))

		mouse = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/double/double_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/mask/board/double/double_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.m_double_view = touch
		self.m_double_view_size = self.GetSize(self.m_double_view)
		if not self.m_double_view_size:
			self.m_double_view = mouse
			self.m_double_view_size = self.GetSize(self.m_double_view)
		for i in xrange(10):
			self.AddTouchEventHandler(self.m_double_view + self.m_color.format('double', i), self.on_touch_btn_color)
		self.AddTouchEventHandler(self.m_double_view + self.m_icon.format('double', 0), self.on_touch_btn_icon)
		self.m_double_icon_pos = self.GetPosition(self.m_double_view + self.m_icon.format('double', 0))

		x, y = self.GetPosition(self.m_double_view + '/double_slot0')
		self.m_offset = (
			self.GetPosition(self.m_double_view + '/double_slot1')[0] - x,
			self.GetPosition(self.m_double_view + '/double_slot5')[1] - y
		)

	def InitScreen(self):
		print '==== %s ====' % 'DanmuFrame Init'

		self.SetVisible(self.m_op_panel, False)
		self.m_op_panel_alive = False
		self.SetInputEnable(False)
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)

	def on_touch_btn_back(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetVisible(self.m_op_panel, False)
			self.m_op_panel_alive = False
			self.SetInputEnable(False)
			clientApi.SetInputMode(0)
			clientApi.HideSlotBarGui(False)

	def on_touch_btn_close(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetVisible(self.m_mask, False)

	def on_touch_btn_settings(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetVisible(self.m_mask, True)

	def on_touch_btn_switch(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			switch = clientApi.GetSystem(danmuConst.ModName, danmuConst.ClientSystemName).Switch
			switch = not switch
			if switch:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_danmu/switch_on")
				self.SetText(args["ButtonPath"] + '/label1', "弹幕  开")
				self.SetVisible('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/footbar/lame', False)
			else:
				self.SetSprite(args["ButtonPath"] + '/default', "textures/ui/netease_danmu/switch_off")
				self.SetText(args["ButtonPath"] + '/label1', "弹幕  关")
				self.SetVisible('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/op_panel/footbar/lame', True)
			clientApi.GetSystem(danmuConst.ModName, danmuConst.ClientSystemName).Switch = switch

	def on_touch_btn_send(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			print self.m_input_string
			if not self.m_input_string:
				return
			clientApi.GetSystem(danmuConst.ModName, danmuConst.ClientSystemName).NotifyToServer(
				'DanmuPublishEvent',
				{
					'playerId': clientApi.GetLocalPlayerId(),
					'content': '{}{}'.format(self.color or '§f', self.m_input_string),
					'iconId': self.cache[self.selected_icon_order][0]
				}
			)
			print {
				'playerId': clientApi.GetLocalPlayerId(),
				'content': '{}{}'.format(self.color or '§f', self.m_input_string),
				'iconId': self.cache[self.selected_icon_order][0]
			}

	def on_touch_btn_icon(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchDown:
			order = int(args["ButtonPath"][::-1].split('_', 1)[0][::-1][4:])
			lock = self.cache[order][-1]
			if lock:
				clientApi.GetSystem(danmuConst.ModName, danmuConst.ClientSystemName).NotifyToServer(
					'HintIconUnlockTextEvent',
					{
						'playerId': clientApi.GetLocalPlayerId(),
						'iconId': self.cache[order][0]
					}
				)
			else:
				if order == self.selected_icon_order:
					return
				self.SetVisible(self.m_icons[self.selected_icon_order] + '/highlight', False)
				self.selected_icon_order = order
				self.SetVisible(args["ButtonPath"] + '/highlight', True)

	def on_touch_btn_color(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchDown:
			order = int(args["ButtonPath"][-1])
			if order == self.selected_color_order:
				return
			self.color = self.colors[order]
			self.SetVisible(self.view + '/{}_slot{}/highlight'.format(self.ns, self.selected_color_order), False)
			self.selected_color_order = order
			self.SetVisible(args["ButtonPath"][::-1].split('/', 1)[1][::-1] + '/highlight', True)

	def open(self, data):
		if self.color is None:
			colors = data['colors']
			if not colors:
				self.color = '§f'
			else:
				self.color = colors[0]['color']
				self.colors = [item['color'] for item in colors]
			demand = len(colors)
			if demand > 5:
				self.ns = 'double'
				c = 10
				self.view = self.m_double_view
				self.SetVisible(self.m_single, False)
			else:
				self.ns = 'single'
				c = 5
				self.view = self.m_single_view
				self.SetVisible(self.m_double, False)
			self.m_icons.append(self.view + self.m_icon.format(self.ns, 0))
			for i in xrange(c):
				if i < demand:
					path = colors[i]['pic']
					self.SetSprite(self.view + self.m_color.format(self.ns, i) + '/default', path)
					self.SetSprite(self.view + self.m_color.format(self.ns, i) + '/hover', path)
					self.SetSprite(self.view + self.m_color.format(self.ns, i) + '/pressed', path)
					self.SetVisible(self.view + '/{}_slot{}/highlight'.format(self.ns, i), not i)
				else:
					self.SetVisible(self.view + '/{}_slot{}'.format(self.ns, i), False)

		icons = data['icons']
		self.cache = [(-1, None, 0)] + icons
		total = len(self.m_icons) - 1
		demand = len(icons)
		if demand > total:
			pos = self.ns == 'single' and self.m_single_icon_pos or self.m_double_icon_pos
			for i in xrange(total + 1, demand + 1):
				self.Clone(self.m_icons[0], self.view, self.m_icon.format(self.ns, i)[1:])
				self.m_icons.append(self.view + self.m_icon.format(self.ns, i))
				dx = i % 5
				dy = i // 5
				self.SetPosition(self.m_icons[-1], (pos[0] + self.m_offset[0] * dx, pos[1] + self.m_offset[1] * dy))
		size = self.ns == 'single' and self.m_single_view_size or self.m_double_view_size
		self.SetSize(self.view, (size[0], size[1] + (len(self.m_icons) - 0.1) // 5 * self.m_offset[1] + 44))
		for i, p in enumerate(self.m_icons[1:]):
			if i < demand:
				lock = icons[i][-1]
				self.SetSprite(p + '/default', icons[i][1])
				self.SetSprite(p + '/hover', icons[i][1])
				self.SetSprite(p + '/pressed', icons[i][1])
				self.SetVisible(p + '/lock', bool(lock))
				if self.selected_icon_order == i + 1:
					if lock:
						self.selected_icon_order = 0
						self.SetVisible(self.m_icons[0] + '/highlight', True)
						self.SetVisible(p + '/highlight', False)
				else:
					self.SetVisible(p + '/highlight', False)
			self.SetVisible(p, i < demand)
		if self.selected_icon_order > demand:
			self.selected_icon_order = 0
			self.SetVisible(self.m_icons[0] + '/highlight', True)

		self.SetVisible(self.m_mask, False)
		self.SetVisible(self.m_op_panel, True)
		self.m_op_panel_alive = True
		self.SetInputEnable(True)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)
