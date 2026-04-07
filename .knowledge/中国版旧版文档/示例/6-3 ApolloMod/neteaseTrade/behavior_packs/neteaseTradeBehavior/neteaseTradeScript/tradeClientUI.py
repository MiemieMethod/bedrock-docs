# -*- coding: utf-8 -*-

import json
import neteaseTradeScript.tradeConst as tradeConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()


class TradeScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init TradeScreen'

		# '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel'

		self.m_trade_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel'

		self.m_grocery_board = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg'
		self.m_grocery_board_alive = False
		self.m_grocery_id = None
		self.m_grocery_desc_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/grocery_desc_text'
		self.m_grocery_close_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/close_btn'

		self.m_grocery_dough = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/coin_{}_bg'
		self.m_grocery_dough_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/coin_{}_bg/coin_{}_icon'
		self.m_grocery_dough_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/coin_{}_bg/coin_{}_text'
		self.m_grocery_doughs = {1: None, 2: None}  # 货币持有信息

		self.m_grocery_merch = '/merch_{0}_bg'
		self.m_grocery_merch_name_text = self.m_grocery_merch + '/merch_{0}_name_text'
		self.m_grocery_merch_pic = self.m_grocery_merch + '/good_{0}_bg/good_{0}_pic'
		self.m_grocery_merch_count_text = self.m_grocery_merch_pic + '/count'
		self.m_grocery_merch_limit_bar = self.m_grocery_merch_pic + '/good_{0}_limit_bg'
		self.m_grocery_merch_limit_text = self.m_grocery_merch_limit_bar + '/good_{0}_limit_text'
		self.m_grocery_merch_buy_btn = self.m_grocery_merch + '/merch_{0}_buy_btn'
		# self.m_grocery_merch_buy_btn_icons = ('textures/ui/netease_trade/btn02@3x', 'textures/ui/netease_trade/btn02_click@3x')
		self.m_grocery_merch_dough_icon = self.m_grocery_merch_buy_btn + '/unit_cost/c{1}/cost_coin'
		self.m_grocery_merch_dough_text = self.m_grocery_merch_buy_btn + '/unit_cost/c{1}/demand'
		self.m_grocery_merch_dough_kind = self.m_grocery_merch_buy_btn + '/unit_cost/c{1}'
		self.m_grocery_merchs = {i: None for i in xrange(1, 4)}

		self.m_selected = None
		self.m_count = 0

		self.m_confirm_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/confirm'
		self.m_minus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/minus'
		self.m_plus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/plus'
		self.m_up_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/up'

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'TradeScreen Create'

		self.m_grocery_dough_pos = self.GetPosition(self.m_grocery_dough.format(2))
		self.m_grocery_dough_offset = self.GetPosition(self.m_grocery_dough.format(1))[0] - self.m_grocery_dough_pos[0]

		mouse = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/merch_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/grocery_bg/merch_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.m_grocery_merch_panel = touch
		self.m_grocery_merch_panel_size = self.GetSize(self.m_grocery_merch_panel)
		if not self.m_grocery_merch_panel_size:
			self.m_grocery_merch_panel = mouse
			self.m_grocery_merch_panel_size = self.GetSize(self.m_grocery_merch_panel)
		self.m_grocery_merch_bar = self.m_grocery_merch_panel + '/merch_bar_panel'
		self.m_grocery_merch_bar_size = self.GetSize(self.m_grocery_merch_bar)
		self.m_grocery_merch_bar_pos = self.GetPosition(self.m_grocery_merch_bar)
		self.m_grocery_merch_bars = [self.m_grocery_merch_bar]

		self.AddTouchEventHandler(self.m_grocery_close_btn, self.on_touch_btn_close)
		self.AddTouchEventHandler(self.m_confirm_btn, self.on_touch_btn_confirm)
		self.AddTouchEventHandler(self.m_minus_btn, self.on_touch_btn_minus)
		self.AddTouchEventHandler(self.m_plus_btn, self.on_touch_btn_plus)
		self.AddTouchEventHandler(self.m_up_btn, self.on_touch_btn_up)
		self.AddTouchEventHandler('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/back', self.on_touch_btn_back)
		for i in xrange(1, 4):
			self.AddTouchEventHandler(self.m_grocery_merch_bar + self.m_grocery_merch_buy_btn.format(i), self.on_touch_btn_buy)

	def InitScreen(self):
		print '==== %s ====' % 'TradeScreen Init'

		self.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)

		if self.m_grocery_id is None:
			self.SetVisible(self.m_grocery_board, False)

			self.SetVisible("", False)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		self.m_count += 1

		if not self.m_count % 16:
			self.m_count = 0
			if self.m_selected:
				self.buy()
				self.m_selected = None

	def on_touch_btn_buy(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			print '==== %s ====' % 'TradeScreen buy TouchUp'
			clientApi.SetResponse(True)
			segment, index = args["ButtonPath"].split('/')[-3:-1]
			segment, index = int(segment[10:-6] or 0), int(index[6:-3])
			# print '"{}"'.format(segment), '"{}"'.format(index), '"{}"'.format(args["ButtonPath"])
			# self.m_selected = self.m_grocery_merchs[3 * segment + index][:2]

			i = 3 * segment + index
			self.selected_index = i
			args = self.args_cache[i]

			grocery_merch_pic = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/good_1_bg/good_1_pic'
			grocery_merch_count_text = grocery_merch_pic + '/count'
			grocery_merch_limit_bar = grocery_merch_pic + '/good_1_limit_bg'
			grocery_merch_limit_text = grocery_merch_limit_bar + '/good_1_limit_text'
			subtotal = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/subtotal/cost'
			rich = self.GetRichTextItem(subtotal)

			self.SetSprite(grocery_merch_pic, args[0])
			self.SetText('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/desc', args[1])
			self.SetText(grocery_merch_count_text, args[2])

			affordable, self.up = self.update_subtotal(args, rich, 1, True)

			result = args[-1]
			if result is None:
				self.SetVisible(grocery_merch_limit_bar, False)
			else:
				left = result[1]
				if left <= 0:
					affordable = False
				self.SetText(grocery_merch_limit_text, ('' if left > 0 else '§4') + result[0])
				self.SetVisible(grocery_merch_limit_bar, True)
			if affordable:
				self.SetTouchEnable(self.m_confirm_btn, True)
				self.SetSprite(self.m_confirm_btn + '/default', "textures/ui/netease_trade/btn01")
				self.SetText(self.m_confirm_btn + '/button_label', '购买')
			else:
				self.SetTouchEnable(self.m_confirm_btn, False)
				self.SetSprite(self.m_confirm_btn + '/default', "textures/ui/netease_trade/btn01_unuse")
				self.SetText(self.m_confirm_btn + '/button_label', '§f购买')
			self.SetText('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/input/qty', '1')
			self.qty = 1
			self.affordable = affordable

			self.SetVisible(self.m_trade_panel + '/detail_input_panel', True)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def update_subtotal(self, args, rich, qty, prime=False):
		mapping = args[3]
		if qty > 1:
			mapping = mapping.copy()
			for k, v in mapping.iteritems():
				mapping[k] = v * qty

		s = '花费合计： '
		l = []
		for ii in xrange(1, len(self.m_grocery_doughs) + 1):
			if ii in self.m_grocery_doughs and self.m_grocery_doughs[ii]:
				l.append(self.m_grocery_doughs[ii])
				continue
			break
		affordable = True
		for k, balance, coin in l:
			if k in mapping:
				poor = '§4' if balance < mapping[k] else ''
				if poor:
					affordable = False
				s += "<image>{}</image> ".format(json.dumps({
					"texture": coin,
					"x": 6,
					"y": 6
				})) + poor + str(mapping[k]) + '§r '
		#rich.readRichText('')
		comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
		comp.AddTimer(0.01, lambda: rich.readRichText(s))
		if prime:
			if affordable:
				up = float('inf')
				for k, balance, coin in l:
					if k in mapping:
						up = min(up, balance // mapping[k])
				return affordable, up
			return affordable, None
		return affordable

	def on_touch_btn_back(self, args):
		touch_event = args["TouchEvent"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			self.SetVisible(self.m_trade_panel + '/detail_input_panel', False)
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

	def on_touch_btn_confirm(self, args):
		touch_event = args["TouchEvent"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			if not self.affordable:
				return

			self.m_selected = tuple(self.m_grocery_merchs[self.selected_index][:2]) + (self.qty,)
			self.SetVisible(self.m_trade_panel + '/detail_input_panel', False)

	def on_touch_btn_minus(self, args):
		touch_event = args["TouchEvent"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			if not self.affordable:
				return

			m = False
			if self.qty < 1:
				self.qty = 1
				m = True
			elif self.qty > 1:
				self.qty -= 1
				m = True
			if m:
				i = self.selected_index
				args = self.args_cache[i]

				self._update_subtotal(args)

	def _update_subtotal(self, args):
		subtotal = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/subtotal/cost'
		rich = self.GetRichTextItem(subtotal)
		affordable = self.update_subtotal(args, rich, self.qty)
		if affordable:
			self.SetTouchEnable(self.m_confirm_btn, True)
			self.SetSprite(self.m_confirm_btn + '/default', "textures/ui/netease_trade/btn01")
			self.SetText(self.m_confirm_btn + '/button_label', '购买')
		else:
			self.SetTouchEnable(self.m_confirm_btn, False)
			self.SetSprite(self.m_confirm_btn + '/default', "textures/ui/netease_trade/btn01_unuse")
			self.SetText(self.m_confirm_btn + '/button_label', '§f购买')
		self.SetText('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/trade_panel/detail_input_panel/detail/board/input/qty', str(self.qty))

	def on_touch_btn_plus(self, args):
		touch_event = args["TouchEvent"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			if not self.affordable:
				return

			i = self.selected_index
			args = self.args_cache[i]
			m = False
			result = args[-1]
			if result is None:
				left = 64
			else:
				left = result[1]
			if self.qty < 0:
				self.qty = 1
				m = True
			elif self.qty < left:
				self.qty += 1
				m = True
			if m:
				self._update_subtotal(args)

	def on_touch_btn_up(self, args):
		touch_event = args["TouchEvent"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			if not self.affordable:
				return

			i = self.selected_index
			args = self.args_cache[i]
			result = args[-1]
			if result is None:
				left = 64
			else:
				left = result[1]
			up = min(self.up, left)
			if self.qty != up:
				self.qty = up
				self._update_subtotal(args)


	def buy(self):
		grocery_id, good_id, qty = self.m_selected
		clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
			tradeConst.PlayerPurchaseEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'groceryId': grocery_id, 'goodId': good_id, 'qty': qty}
		)

	def open(self, data):
		grocery = data.get('grocery')
		bought = data.get('bought')
		doughs = data.get('doughs')
		icons = data.get('icons')
		if None in (grocery, bought, doughs, icons):
			print ''
			return
		# bought = bought.copy()
		# doughs = doughs.copy()
		# goods = list(grocery.get('grocery_goods', []))
		goods = grocery.get('grocery_goods', [])
		icons_copy = icons.copy()
		grocery_id = grocery['grocery_id']
		if grocery_id is None:
			return
		# if self.m_grocery_id != grocery_id or data.get('reset'):
		if True:
			name = grocery.get('grocery_desc', '商店')
			desc = grocery.get('grocery_update_desc', '')
			count = 0
			for dough_id in icons:
				if None not in (icons[dough_id], doughs[dough_id]):
					count += 1
				else:
					icons_copy.pop(dough_id)
			if count > len(self.m_grocery_doughs):
				# 需要加
				for i in xrange(len(self.m_grocery_doughs) + 1, count + 1):
					self.Clone(self.m_grocery_dough.format(2), self.m_grocery_board, 'coin_{}_bg'.format(i))
					self.SetPosition(self.m_grocery_dough.format(i), (self.m_grocery_dough_pos[0] - self.m_grocery_dough_offset * (i - 2), self.m_grocery_dough_pos[-1]))
					self.m_grocery_doughs[i] = None
			for i in xrange(1, len(self.m_grocery_doughs) + 1):
				if i > count:
					self.SetVisible(self.m_grocery_dough.format(i), False)
				else:
					dough_id, icon = icons_copy.popitem()
					self.m_grocery_doughs[i] = [dough_id, doughs[dough_id], icon]
					self.SetSprite(self.m_grocery_dough_icon.format(i, i > 2 and 2 or i), icon)
					self.SetText(self.m_grocery_dough_text.format(i, i > 2 and 2 or i), str(doughs[dough_id]))
					self.SetVisible(self.m_grocery_dough.format(i), True)
			count = len(goods)
			total = (count - 1) // 3 + 1
			flag = False
			if count > len(self.m_grocery_merchs):
				# 需要加
				flag = True
				self.SetSize(self.m_grocery_merch_panel, (self.m_grocery_merch_panel_size[0], max(self.m_grocery_merch_bar_size[-1] * total + 4, self.m_grocery_merch_panel_size[-1])))
				for i in xrange(len(self.m_grocery_merch_bars), total):
					self.Clone(self.m_grocery_merch_bar, self.m_grocery_merch_panel, 'merch_bar_{}_panel'.format(i))
					self.m_grocery_merch_bars.append(self.m_grocery_merch_panel + '/merch_bar_{}_panel'.format(i))
					self.SetPosition(self.m_grocery_merch_bars[-1], (self.m_grocery_merch_bar_pos[0], self.m_grocery_merch_bar_pos[-1] + self.m_grocery_merch_bar_size[-1] * (len(self.m_grocery_merch_bars) - 1)))
					for i in xrange(3 * i + 1, 3 * i + 4):
						self.m_grocery_merchs[i] = None
			if not flag:
				self.SetSize(self.m_grocery_merch_panel, (self.m_grocery_merch_panel_size[0], max(self.m_grocery_merch_bar_size[-1] * total + 4, self.m_grocery_merch_panel_size[-1])))

			self.args_cache = {}

			for i in xrange(1, len(self.m_grocery_merchs) + 1):
				index = (i - 1) % 3 + 1
				segment = (i - 1) // 3
				if i > count:
					self.SetVisible(self.m_grocery_merch_bars[segment] + self.m_grocery_merch.format(index), False)
				else:
					self.m_grocery_merchs[i] = (grocery_id, goods[i - 1]['good_id'],)
					self.SetSprite(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_pic.format(index), goods[i - 1]['good_icon'])
					self.SetText(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_name_text.format(index), str(goods[i - 1]['good_desc']))
					self.SetText(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_count_text.format(index), str(goods[i - 1]['good_item_count']))

					mapping = goods[i - 1]['good_cost']
					l = []
					for ii in xrange(1, len(self.m_grocery_doughs) + 1):
						if ii in self.m_grocery_doughs and self.m_grocery_doughs[ii]:
							l.append(self.m_grocery_doughs[ii])
							continue
						break
					iii = 0
					for k, balance, coin in l:
						if k in mapping:
							self.SetSprite(
								self.m_grocery_merch_bars[segment] + self.m_grocery_merch_dough_icon.format(index, iii),
								coin)
							self.SetText(
								self.m_grocery_merch_bars[segment] + self.m_grocery_merch_dough_text.format(index, iii),
								str(mapping[k]))
							iii += 1
							self.SetVisible(
								self.m_grocery_merch_bars[segment] + self.m_grocery_merch_dough_kind.format(index, iii),
								True
							)
						if iii == 3:
							break
					for iii in xrange(iii, 3):
						self.SetVisible(
							self.m_grocery_merch_bars[segment] + self.m_grocery_merch_dough_kind.format(index, iii),
							False
						)

					result = None
					if 'good_limit' not in goods[i - 1]:
						self.SetVisible(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_limit_bar.format(index), False)
					else:
						limit = goods[i - 1]['good_limit']
						cur = bought.get(self.m_grocery_merchs[i][1], 0)
						self.m_grocery_merchs[i] += (limit, cur)
						# if cur >= limit:
						# 	self.SetTouchEnable(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_buy_btn.format(index), False)
						# else:
						# 	self.SetTouchEnable(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_buy_btn.format(index), True)
						result = "限购{0}次（{1}/{0}）".format(limit, cur)
						self.SetText(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_limit_text.format(index), result)
						self.SetVisible(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_limit_bar.format(index), True)
						result = result, limit - cur

					self.args_cache[i] = [
						goods[i - 1]['good_icon'],
						str(goods[i - 1]['good_desc']),
						str(goods[i - 1]['good_item_count']),
						mapping,
						result
					]

					self.SetVisible(self.m_grocery_merch_bars[segment] + self.m_grocery_merch.format(index), True)
			self.SetText(self.m_grocery_desc_text, (name + '（{}）'.format(desc)) if desc else name)
			self.m_grocery_id = grocery_id
		self.m_grocery_board_alive = True

		self.SetVisible("", True)

		self.SetVisible(self.m_grocery_board, self.m_grocery_board_alive)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)

	def refresh(self, data):
		if not self.m_grocery_board_alive:
			return
		bought = data.get('bought')
		doughs = data.get('doughs')
		if doughs is not None:
			for i in xrange(1, len(self.m_grocery_doughs) + 1):
				if self.m_grocery_doughs[i] and self.m_grocery_doughs[i][0] in doughs:
					cur = doughs[self.m_grocery_doughs[i][0]]
					if cur != self.m_grocery_doughs[i][1]:
						self.m_grocery_doughs[i][1] = cur
						self.SetText(self.m_grocery_dough_text.format(i, i > 2 and 2 or i), str(cur))
		if bought is not None:
			for i in xrange(1, len(self.m_grocery_merchs) + 1):
				if self.m_grocery_merchs[i] and len(self.m_grocery_merchs[i]) > 2:
					cur = bought.get(self.m_grocery_merchs[i][1], 0)
					if cur != self.m_grocery_merchs[i][-1]:
						self.m_grocery_merchs[i] = self.m_grocery_merchs[i][:-1] + (cur,)
						index = (i - 1) % 3 + 1
						segment = (i - 1) // 3
						limit = self.m_grocery_merchs[i][2]
						# if cur >= limit:
						# 	self.SetTouchEnable(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_buy_btn.format(index), False)
						# else:
						# 	self.SetTouchEnable(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_buy_btn.format(index), True)
						result = "限购{0}次（{1}/{0}）".format(limit, cur)
						self.SetText(self.m_grocery_merch_bars[segment] + self.m_grocery_merch_limit_text.format(index), result)
						result = result, limit - cur
						self.args_cache[i][-1] = result

	def close(self):
		self.SetVisible(self.m_grocery_board, False)
		self.m_grocery_board_alive = False
		clientApi.SetInputMode(0)
		clientApi.HideSlotBarGui(False)

		self.SetVisible("", False)
