# -*- coding: utf-8 -*-

import time
import json
import neteaseTradeScript.tradeConst as tradeConst
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class SaleScreen(ScreenNode):
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def set_input_string(self, args):
		# print 'set_input_string', args
		comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
		if comp:
			if comp.CheckWordsValid(args["Text"]):
				self.m_input_string = args["Text"]
			else:
				self.m_input_string = '***'
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def get_input_string(self):
		# print 'get_input_string', self.m_input_string
		return self.m_input_string

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init SaleScreen'

		# '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel'

		self.m_sale_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel'
		self.m_alert_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg'
		self.m_alert_board_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_title_text'
		self.m_cancel_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/cancel_btn'
		self.m_confirm_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/confirm_btn'
		self.m_alert_board_fee_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_fee_panel'
		self.m_alert_fee_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_fee_panel/alert_fee_bg/alert_fee_panel/alert_fee_icon'
		self.m_alert_fee_count_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_fee_panel/alert_fee_bg/alert_fee_panel/alert_fee_count_text'
		self.m_alert_fee_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_fee_panel/alert_fee_text', '需要消耗以上货币摆摊 {} 小时，是否确定？'
		self.m_alert_board_merch_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel'
		self.m_alert_price_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_bg/alert_price_text'
		self.m_alert_price_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_bg/alert_price_text/alert_unit_panel/alert_price_icon'
		self.m_alert_price_count_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_bg/alert_price_text/alert_unit_panel/alert_price_count_text'
		self.m_alert_qty_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_bg/alert_qty_text', '总数： {}'
		self.m_alert_slot_item_img = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_bg/alert_slot_bg/item_img'
		self.m_alert_merch_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_board_merch_panel/alert_merch_text'
		self.m_left_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/left_title_text'
		self.m_right_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/right_title_text'
		self.m_close_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/close_btn'
		self.m_interact_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/interact_bg'
		self.m_interact_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/interact_bg/interact_btn'
		self.m_interact_mask_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/interact_bg/interact_btn/interact_mask_bg'
		self.m_op_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_{}'
		self.m_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/title_text'
		self.m_duration_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/duration_text'
		self.m_fee_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/fee_text'
		self.m_plain_text_bg = '/plain_text_bg'
		self.m_plain_text = '/plain_text_bg/plain_text'
		self.m_input_string = '出售摊位'
		self.m_duration_minus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/duration_minus_btn'
		self.m_duration_plus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/duration_plus_btn'
		self.m_duration_edit_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/duration_edit_btn'
		self.m_duration_input_string = ''
		self.m_fee_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/fee_bg/fee_panel/fee_icon'
		self.m_fee_count_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_1/fee_bg/fee_panel/fee_count_text'
		self.m_slot_item_img = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/slot_bg/item_img'
		self.m_left_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/left_btn'
		self.m_right_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/right_btn'
		self.m_currency_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/currency_bg/currency_panel/currency_icon'
		self.m_currency_name_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/currency_bg/currency_panel/currency_name_text'
		self.m_unit_minus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/unit_minus_btn'
		self.m_unit_plus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/unit_plus_btn'
		self.m_unit_edit_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/unit_edit_btn'
		self.m_unit_input_string = ''
		self.m_qty_minus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/qty_minus_btn'
		self.m_qty_plus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/qty_plus_btn'
		self.m_qty_edit_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/qty_edit_btn'
		self.m_qty_input_string = ''
		self.m_resp_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/resp_bg'
		self.m_resp_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/resp_bg/resp_text'
		self.m_mask_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_2/mask_bg'
		self.m_option_list = ['option_1']
		self.m_consequence_text = '/option_info_bg/consequence_text'
		self.m_withdraw_btn = '/option_info_bg/withdraw_btn'
		self.m_option_shortcut_item_img = '/option_shortcut_bg/item_img'
		self.m_option_unit_icon = '/option_unit_text/option_unit_panel/option_unit_icon'
		self.m_option_unit_count_text = '/option_unit_text/option_unit_panel/option_unit_count_text'
		self.m_option_subtotal_icon = '/option_subtotal_text/option_subtotal_panel/option_subtotal_icon'
		self.m_option_subtotal_count_text = '/option_subtotal_text/option_subtotal_panel/option_subtotal_count_text'
		self.m_option_sale_text = '/option_sale_text', '售出： {} / {}'
		self.m_deal_list = ['deal_1']
		self.m_rich_name_text = '/deal_info_bg/rich_name_text'
		self.m_datetime_text = '/deal_info_bg/datetime_text'
		self.m_deal_shortcut_item_img = '/deal_shortcut_bg/item_img'
		self.m_deal_unit_icon = '/deal_unit_text/deal_unit_panel/deal_unit_icon'
		self.m_deal_unit_count_text = '/deal_unit_text/deal_unit_panel/deal_unit_count_text'
		self.m_deal_subtotal_icon = '/deal_subtotal_text/deal_subtotal_panel/deal_subtotal_icon'
		self.m_deal_subtotal_count_text = '/deal_subtotal_text/deal_subtotal_panel/deal_subtotal_count_text'
		self.m_deal_sale_text = '/deal_sale_text', '数量： {}'
		self.m_merch_item_img = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/merch_bg/item_img'
		self.m_cost_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/cost_text/cost_panel/cost_icon'
		self.m_cost_count_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/cost_text/cost_panel/cost_count_text'
		self.m_count_minus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/count_minus_btn'
		self.m_count_plus_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/count_plus_btn'
		self.m_count_peak_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/count_peak_btn'
		self.m_count_edit_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/count_edit_btn'
		self.m_count_input_string = ''
		self.m_cost_resp_bg = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/cost_resp_bg'
		self.m_cost_resp_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_5/cost_resp_bg/cost_resp_text'
		self.m_tab_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/btn_{}'
		self.m_empty_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/empty_text'
		self.m_bag_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/bag_panel'
		self.m_merch_list_empty_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/merch_list_empty_text'
		self.m_merch_list = ['merch_1']
		self.m_merch_shortcut_item_img = '/merch_shortcut_bg/item_img'
		self.m_merch_stock_text = '/merch_stock_text', '库存： {}'
		self.m_price_icon = '/price_text/price_panel/price_icon'
		self.m_price_count_text = '/price_text/price_panel/price_count_text'
		self.m_alert_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_bg/alert_board_bg/alert_text'
		self.m_calculator_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/calculator_panel'

		self.m_debut = False
		self.m_countdown_cache = None
		self.m_tab_btn_handlers = {
			1: self.f1,
			2: self.f2,
			3: self.f3,
			4: self.f4,
		}

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'SaleScreen Create'

		mouse = '{}/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '{}/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		for k, v in {
			'm_merch_list_panel': '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/merch_list_view',
			'm_manage_panel': '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_3/manage_view',
			'm_deal_list_panel': '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/panel_4/deal_list_view',
		}.items():
			setattr(self, k, touch.format(v))
			_size = self.GetSize(getattr(self, k))
			if not _size:
				setattr(self, k, mouse.format(v))
				setattr(self, '{}_size'.format(k), self.GetSize(getattr(self, k)))
			else:
				setattr(self, '{}_size'.format(k), _size)

		self.m_option_pos = self.GetPosition('{}/{}'.format(self.m_manage_panel, self.m_option_list[0]))
		self.m_option_offset = self.GetSize('{}/{}'.format(self.m_manage_panel, self.m_option_list[0]))[-1]
		self.m_deal_pos = self.GetPosition('{}/{}'.format(self.m_deal_list_panel, self.m_deal_list[0]))
		self.m_deal_offset = self.GetSize('{}/{}'.format(self.m_deal_list_panel, self.m_deal_list[0]))[-1]
		self.m_merch_pos = self.GetPosition('{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[0]))
		self.m_merch_offset = self.GetSize('{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[0]))[-1]
		self.m_calculator_panel_offset = self.GetSize(self.m_calculator_panel)[-1]

		self.AddTouchEventHandler(self.m_confirm_btn, self.on_touch_btn_confirm)
		self.AddTouchEventHandler(self.m_cancel_btn, self.on_touch_btn_cancel)
		self.AddTouchEventHandler(self.m_close_btn, self.on_touch_btn_close)
		for i in xrange(1, 5):
			self.AddTouchEventHandler(self.m_tab_btn.format(i), self.on_touch_btn_tab)
		self.AddTouchEventHandler(self.m_duration_minus_btn, self.on_touch_btn_duration_minus)
		self.AddTouchEventHandler(self.m_duration_plus_btn, self.on_touch_btn_duration_plus)
		self.AddTouchEventHandler(self.m_duration_edit_btn, self.on_touch_btn_duration_edit)
		self.AddTouchEventHandler(self.m_left_btn, self.on_touch_btn_left)
		self.AddTouchEventHandler(self.m_right_btn, self.on_touch_btn_right)
		self.AddTouchEventHandler(self.m_unit_minus_btn, self.on_touch_btn_unit_minus)
		self.AddTouchEventHandler(self.m_unit_plus_btn, self.on_touch_btn_unit_plus)
		self.AddTouchEventHandler(self.m_unit_edit_btn, self.on_touch_btn_unit_edit)
		self.AddTouchEventHandler(self.m_qty_minus_btn, self.on_touch_btn_qty_minus)
		self.AddTouchEventHandler(self.m_qty_plus_btn, self.on_touch_btn_qty_plus)
		self.AddTouchEventHandler(self.m_qty_edit_btn, self.on_touch_btn_qty_edit)
		self.AddTouchEventHandler(self.m_count_minus_btn, self.on_touch_btn_count_minus)
		self.AddTouchEventHandler(self.m_count_plus_btn, self.on_touch_btn_count_plus)
		self.AddTouchEventHandler(self.m_count_peak_btn, self.on_touch_btn_count_peak)
		self.AddTouchEventHandler(self.m_count_edit_btn, self.on_touch_btn_count_edit)
		self.AddTouchEventHandler(self.m_interact_btn, self.on_touch_btn_interact)
		self.AddTouchEventHandler('{}/{}'.format(self.m_manage_panel, self.m_option_list[0]) + self.m_withdraw_btn, self.on_touch_btn_withdraw)
		self.AddTouchEventHandler('{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[0]), self.on_touch_btn_select)
		for i in xrange(10):
			self.AddTouchEventHandler(self.m_calculator_panel + '/num_{}'.format(i), self.on_touch_btn_num)
		self.AddTouchEventHandler(self.m_calculator_panel + '/C', self.on_touch_btn_c)
		self.AddTouchEventHandler(self.m_calculator_panel + '/OK', self.on_touch_btn_ok)

	def InitScreen(self):
		print '==== %s ====' % 'SaleScreen Init'

		self.SetVisible(self.m_calculator_panel, False)
		self.m_calculator_panel_alive = False
		self.SetVisible(self.m_bag_panel, False)
		self.SetVisible(self.m_alert_bg, False)
		self.SetInputEnable(False)
		self.SetVisible(self.m_sale_panel, False)

		self.SetLayer("", clientApi.GetMinecraftEnum().UiBaseLayer.PopUpLv1)
		self.SetVisible("", False)

		self.m_sale_panel_alive = False

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	def f1(self):
		for i in (2, 3, 4):
			self.SetVisible(self.m_op_panel.format(i), False)
		self.hide_calculator()
		self.m_focus = 1
		self.SetVisible(self.m_empty_text, False)
		self.SetText(self.m_right_title_text, '摊位')
		self.SetVisible(self.m_op_panel.format(1), True)
		self.SetVisible(self.m_interact_bg, True)
		self.SetVisible(self.m_interact_mask_bg, False)
		self.SetTouchEnable(self.m_interact_btn, True)
		if self.m_countdown_cache:
			self.off()
		else:
			self.on()

	def off(self):
		self.m_interact = lambda: self.alert(0)
		self.SetVisible(self.m_op_panel.format(1) + '/title_input_field', False)
		self.SetVisible(self.m_title_text + self.m_plain_text_bg, True)
		self.SetVisible(self.m_duration_text + self.m_plain_text_bg, True)
		self.SetVisible(self.m_duration_minus_btn, False)
		self.SetVisible(self.m_duration_plus_btn, False)
		self.SetVisible(self.m_duration_edit_btn, False)
		self.SetVisible(self.m_fee_text + self.m_plain_text_bg, True)
		self.SetVisible(self.m_op_panel.format(1) + '/fee_bg', False)
		self.SetText(self.m_fee_text, "剩余时间：")
		countdown = '0分0秒'
		left = self.m_countdown_cache[-1]
		if left > 0:
			if left < 3600:
				countdown = '{}分{}秒'.format(left // 60, left % 60)
			else:
				countdown = '{}时{}分'.format(left // 3600, left % 3600 // 60)
		self.SetText(self.m_fee_text + self.m_plain_text, countdown)
		self.SetText(self.m_interact_btn + '/button_label', '结束摆摊')

	def on(self):
		self.m_interact = lambda: self.alert(1)
		self.SetVisible(self.m_op_panel.format(1) + '/title_input_field', True)
		self.SetVisible(self.m_title_text + self.m_plain_text_bg, False)
		self.SetVisible(self.m_duration_text + self.m_plain_text_bg, False)
		self.SetVisible(self.m_duration_minus_btn, True)
		self.SetVisible(self.m_duration_plus_btn, True)
		self.SetVisible(self.m_duration_edit_btn, True)
		self.SetText(self.m_duration_text, "摆摊时间： （小时）")
		self.SetVisible(self.m_fee_text + self.m_plain_text_bg, False)
		self.SetVisible(self.m_op_panel.format(1) + '/fee_bg', True)
		self.SetText(self.m_fee_text, "摆摊费用：")
		self.SetText(self.m_interact_btn + '/button_label', '开始摆摊')

	def f2(self):
		for i in (1, 3, 4):
			self.SetVisible(self.m_op_panel.format(i), False)
		self.hide_calculator()
		self.m_focus = 2
		self.m_interact = lambda: self.alert(2)
		if self.m_selected_slot_index is not None:
			self.SetVisible('{}/selectedImg'.format(self.m_slot_list[self.m_selected_slot_index]), False)
			self.m_selected_slot_index = None
		for i in xrange(len(self.m_merchs_cache) - 1, -1, -1):
			if self.m_merchs_cache[i] is None:
				del self.m_merchs_cache[i]
		self.SetVisible(self.m_empty_text, False)
		self.SetText(self.m_right_title_text, '选择要上架的商品')
		self.SetVisible(self.m_op_panel.format(2), True)
		self.SetVisible(self.m_interact_bg, True)
		self.m_selected_currency_index = 0
		self.SetSprite(self.m_currency_icon, self.m_sale_rules['currencyoptions'][0][1])
		self.SetText(self.m_currency_name_text, self.m_sale_rules['currencyoptions'][0][-1])
		self.SetVisible(self.m_slot_item_img, False)
		self.m_unit_input_string = '0'
		self.SetText(self.m_unit_edit_btn + '/button_label', self.m_unit_input_string)
		self.m_qty_input_string = '0'
		self.SetText(self.m_qty_edit_btn + '/button_label', self.m_qty_input_string)
		self.SetVisible(self.m_mask_bg, True)
		self.SetVisible(self.m_interact_mask_bg, True)
		self.SetTouchEnable(self.m_interact_btn, False)
		self.SetText(self.m_interact_btn + '/button_label', '上架（{} / {}）'.format(len(self.m_merchs_cache), self.m_sale_rules['merchcount']))
		self.SetVisible(self.m_resp_bg, True)
		if not (self.m_countdown_cache and self.m_countdown_cache[-1] > 0):
			self.SetText(self.m_resp_text, '§c未开摊，无法上架')
		else:
			self.SetText(self.m_resp_text, '§e请在左侧选择要上架的商品')

	def f3(self):
		for i in (2, 1, 4):
			self.SetVisible(self.m_op_panel.format(i), False)
		self.hide_calculator()
		self.m_focus = 3
		for i in xrange(len(self.m_merchs_cache) - 1, -1, -1):
			if self.m_merchs_cache[i] is None:
				del self.m_merchs_cache[i]
		self.SetText(self.m_right_title_text, '已上架的商品')
		self.SetVisible(self.m_interact_bg, False)
		self.SetVisible(self.m_op_panel.format(3), bool(self.m_merchs_cache))
		if not self.m_merchs_cache:
			self.SetVisible(self.m_empty_text, True)
			self.SetText(self.m_empty_text, "还没有上架的商品\n去选择一些商品上架吧")
			return
		self.SetVisible(self.m_empty_text, False)
		demand = len(self.m_merchs_cache)
		cur = len(self.m_option_list)
		if demand > cur:
			for i in xrange(cur + 1, demand + 1):
				s = 'option_{}'.format(i)
				self.Clone('{}/{}'.format(self.m_manage_panel, self.m_option_list[0]), self.m_manage_panel, s)
				self.SetPosition('{}/{}'.format(self.m_manage_panel, s), (self.m_option_pos[0], self.m_option_pos[1] + self.m_option_offset * (i - 1)))
				self.m_option_list.append(s)
		self.SetSize(self.m_manage_panel, (self.m_manage_panel_size[0], self.m_option_offset * demand + 10))
		for i, s in enumerate(self.m_option_list):
			s = '{}/{}'.format(self.m_manage_panel, s)
			if i < demand:
				item_dict = json.loads(self.m_merchs_cache[i]['stuff'])
				self.SetUiItem(s + self.m_option_shortcut_item_img, item_dict['itemName'], item_dict['auxValue'])
				self.SetSprite(s + self.m_option_unit_icon, self.m_merchs_cache[i]['currency'])
				self.SetSprite(s + self.m_option_subtotal_icon, self.m_merchs_cache[i]['currency'])
				self.SetText(s + self.m_option_unit_count_text, str(self.m_merchs_cache[i]['unit']))
				self.SetText(s + self.m_option_subtotal_count_text, str((self.m_merchs_cache[i]['init'] - self.m_merchs_cache[i]['qty']) * self.m_merchs_cache[i]['unit']))
				self.SetText(s + self.m_option_sale_text[0], self.m_option_sale_text[1].format(self.m_merchs_cache[i]['init'] - self.m_merchs_cache[i]['qty'], self.m_merchs_cache[i]['init']))
				self.SetVisible(s + self.m_withdraw_btn, True)
			self.SetVisible(s, i < demand)

	def f4(self):
		for i in (2, 3, 1):
			self.SetVisible(self.m_op_panel.format(i), False)
		self.hide_calculator()
		self.m_focus = 4
		if not self.m_deals_cache:
			self.SetVisible(self.m_empty_text, True)
			self.SetText(self.m_empty_text, "暂无出售记录\n待会再来看看吧")
		else:
			self.SetVisible(self.m_empty_text, False)
		self.SetText(self.m_right_title_text, '出售记录')
		self.SetVisible(self.m_interact_bg, False)
		self.SetVisible(self.m_op_panel.format(4), True)

	def edit_duration(self):
		try:
			result = int(self.m_duration_input_string)
			if result > self.m_sale_rules['timelimit']:
				self.m_duration_input_string = str(self.m_sale_rules['timelimit'])
		except ValueError:
			self.m_duration_input_string = '1'
		self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
		self.SetText(self.m_fee_count_text, str(int(self.m_duration_input_string) * self.m_sale_rules['hourlyfee']))

	def on_touch_btn_duration_edit(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if getattr(self, 'm_edit_target', None) and self.m_edit_target[0] == 'm_duration_input_string':
				return
			self.hide_calculator()
			self.m_edit_target = ['m_duration_input_string', self.m_duration_edit_btn + '/button_label']
			self.m_edit = self.edit_duration
			self.show_calculator((args['TouchPosX'], args['TouchPosY'] - self.m_calculator_panel_offset))

	def edit_unit(self):
		try:
			result = int(self.m_unit_input_string)
			if result > self.m_sale_rules['unitlimit']:
				self.m_unit_input_string = str(self.m_sale_rules['unitlimit'])
		except ValueError:
			self.m_unit_input_string = '0'
		self.SetText(self.m_unit_edit_btn + '/button_label', self.m_unit_input_string)

	def on_touch_btn_unit_edit(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if getattr(self, 'm_edit_target', None) and self.m_edit_target[0] == 'm_unit_input_string':
				return
			self.hide_calculator()
			self.m_edit_target = ['m_unit_input_string', self.m_unit_edit_btn + '/button_label']
			self.m_edit = self.edit_unit
			self.show_calculator((args['TouchPosX'], args['TouchPosY'] - self.m_calculator_panel_offset))

	def edit_qty(self):
		try:
			result = int(self.m_qty_input_string)
			try:
				item_dict = json.loads(self.m_inventory_cache[self.m_selected_slot_index])
				limit = item_dict['count']
			except:
				raise ValueError
			if result > limit:
				self.m_qty_input_string = str(limit)
		except ValueError:
			self.m_qty_input_string = '1'
		self.SetText(self.m_qty_edit_btn + '/button_label', self.m_qty_input_string)

	def on_touch_btn_qty_edit(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if getattr(self, 'm_edit_target', None) and self.m_edit_target[0] == 'm_qty_input_string':
				return
			self.hide_calculator()
			self.m_edit_target = ['m_qty_input_string', self.m_qty_edit_btn + '/button_label']
			self.m_edit = self.edit_qty
			self.show_calculator((args['TouchPosX'], args['TouchPosY'] - self.m_calculator_panel_offset))

	def edit_count(self):
		try:
			result = int(self.m_count_input_string)
			if result > (self.m_merchs_cache[self.m_selected_merch_index]['qty'] or 1):
				self.m_count_input_string = str(self.m_merchs_cache[self.m_selected_merch_index]['qty'] or 1)
		except ValueError:
			self.m_count_input_string = '1'
		self.SetText(self.m_count_edit_btn + '/button_label', self.m_count_input_string)
		self.SetText(
			self.m_cost_count_text,
			str(self.m_merchs_cache[self.m_selected_merch_index]['unit'] * int(self.m_count_input_string)))

	def on_touch_btn_count_edit(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if getattr(self, 'm_edit_target', None) and self.m_edit_target[0] == 'm_count_input_string':
				return
			self.hide_calculator()
			self.m_edit_target = ['m_count_input_string', self.m_count_edit_btn + '/button_label']
			self.m_edit = self.edit_count
			self.show_calculator((args['TouchPosX'], args['TouchPosY'] - self.m_calculator_panel_offset))

	def on_touch_btn_confirm(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.m_confirm()
			self.SetVisible(self.m_alert_bg, False)

	def on_touch_btn_cancel(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.cancel()

	def on_touch_btn_close(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.SetInputEnable(False)
			self.SetVisible(self.m_sale_panel, False)
			self.m_sale_panel_alive = False
			clientApi.SetInputMode(0)
			clientApi.HideSlotBarGui(False)

			self.SetVisible("", False)

	def on_touch_btn_tab(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			index = int(args["ButtonPath"][-1])
			if self.m_focus == index:
				return
			self.SetSprite(args["ButtonPath"] + '/default', index == 4 and "textures/ui/netease_sale/tab02_click@3x" or "textures/ui/netease_sale/tab01_click@3x")
			for i in {1, 2, 3, 4}.difference([index]):
				self.SetSprite(args["ButtonPath"][:-1] + '{}/default'.format(i), i == 4 and "textures/ui/netease_sale/tab02@3x" or "textures/ui/netease_sale/tab01@3x")
			self.m_tab_btn_handlers[index]()

	def on_touch_btn_duration_minus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_duration_input_string
			try:
				result = int(self.m_duration_input_string)
				if result > 1:
					result -= 1
					self.m_duration_input_string = str(result)
			except ValueError:
				print pre
				self.m_duration_input_string = '1'
			if pre != self.m_duration_input_string:
				self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
				self.SetText(self.m_fee_count_text, str(int(self.m_duration_input_string) * self.m_sale_rules['hourlyfee']))

	def on_touch_btn_duration_plus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_duration_input_string
			try:
				result = int(self.m_duration_input_string)
				if result < self.m_sale_rules['timelimit']:
					result += 1
					self.m_duration_input_string = str(result)
			except ValueError:
				print pre
				self.m_duration_input_string = '1'
			if pre != self.m_duration_input_string:
				self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
				self.SetText(self.m_fee_count_text, str(int(self.m_duration_input_string) * self.m_sale_rules['hourlyfee']))

	def on_touch_btn_left(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.m_selected_currency_index -= 1
			self.m_selected_currency_index %= len(self.m_sale_rules['currencyoptions'])
			self.SetSprite(self.m_currency_icon, self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][1])
			self.SetText(self.m_currency_name_text, self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][-1])

	def on_touch_btn_right(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.m_selected_currency_index += 1
			self.m_selected_currency_index %= len(self.m_sale_rules['currencyoptions'])
			self.SetSprite(self.m_currency_icon, self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][1])
			self.SetText(self.m_currency_name_text, self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][-1])

	def on_touch_btn_unit_minus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_unit_input_string
			try:
				result = int(self.m_unit_input_string)
				if result > 0:
					result -= 1
					self.m_unit_input_string = str(result)
			except ValueError:
				print pre
				self.m_unit_input_string = '0'
			if pre != self.m_unit_input_string:
				self.SetText(self.m_unit_edit_btn + '/button_label', self.m_unit_input_string)

	def on_touch_btn_unit_plus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_unit_input_string
			try:
				result = int(self.m_unit_input_string)
				if result < self.m_sale_rules['unitlimit']:
					result += 1
					self.m_unit_input_string = str(result)
			except ValueError:
				print pre
				self.m_unit_input_string = '1'
			if pre != self.m_unit_input_string:
				self.SetText(self.m_unit_edit_btn + '/button_label', self.m_unit_input_string)

	def on_touch_btn_qty_minus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_qty_input_string
			try:
				result = int(self.m_qty_input_string)
				if result > 1:
					result -= 1
					self.m_qty_input_string = str(result)
			except ValueError:
				print pre
				self.m_qty_input_string = '1'
			if pre != self.m_qty_input_string:
				self.SetText(self.m_qty_edit_btn + '/button_label', self.m_qty_input_string)

	def on_touch_btn_qty_plus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_qty_input_string
			try:
				result = int(self.m_qty_input_string)
				try:
					item_dict = json.loads(self.m_inventory_cache[self.m_selected_slot_index])
					limit = item_dict['count']
				except:
					return
				if result < limit:
					result += 1
					self.m_qty_input_string = str(result)
			except ValueError:
				print pre
				self.m_qty_input_string = '1'
			if pre != self.m_qty_input_string:
				self.SetText(self.m_qty_edit_btn + '/button_label', self.m_qty_input_string)

	def on_touch_btn_count_minus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_count_input_string
			try:
				result = int(self.m_count_input_string)
				if result > 1:
					result -= 1
					self.m_count_input_string = str(result)
			except ValueError:
				print pre
				self.m_count_input_string = '1'
			if pre != self.m_count_input_string:
				self.SetText(self.m_count_edit_btn + '/button_label', self.m_count_input_string)
				self.SetText(
					self.m_cost_count_text,
					str(self.m_merchs_cache[self.m_selected_merch_index]['unit'] * int(self.m_count_input_string)))

	def on_touch_btn_count_plus(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_count_input_string
			try:
				result = int(self.m_count_input_string)
				if result < self.m_merchs_cache[self.m_selected_merch_index]['qty']:
					result += 1
					self.m_count_input_string = str(result)
			except ValueError:
				print pre
				self.m_count_input_string = '1'
			if pre != self.m_count_input_string:
				self.SetText(self.m_count_edit_btn + '/button_label', self.m_count_input_string)
				self.SetText(
					self.m_cost_count_text,
					str(self.m_merchs_cache[self.m_selected_merch_index]['unit'] * int(self.m_count_input_string)))

	def on_touch_btn_count_peak(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			pre = self.m_count_input_string
			try:
				result = int(self.m_count_input_string)
				if result != (self.m_merchs_cache[self.m_selected_merch_index]['qty'] or 1):
					result = self.m_merchs_cache[self.m_selected_merch_index]['qty'] or 1
					self.m_count_input_string = str(result)
			except ValueError:
				print pre
				self.m_count_input_string = '1'
			if pre != self.m_count_input_string:
				self.SetText(self.m_count_edit_btn + '/button_label', self.m_count_input_string)
				self.SetText(
					self.m_cost_count_text,
					str(self.m_merchs_cache[self.m_selected_merch_index]['unit'] * int(self.m_count_input_string)))

	def on_touch_btn_interact(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			self.hide_calculator()
			self.m_interact()

	def on_touch_btn_withdraw(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			_id = self.m_merchs_cache[int(args["ButtonPath"][::-1].split('/', 3)[-2].split('_', 1)[0][::-1]) - 1]['_id']
			print _id
			clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
				tradeConst.PlayerWithdrawMerchEvent,
				{'playerId': clientApi.GetLocalPlayerId(), '_id': _id}
			)
			self.SetText(args["ButtonPath"][:-12] + 'consequence_text', '下架中')
			self.SetVisible(args["ButtonPath"], False)

	def on_touch_btn_select(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			selected_merch_index = int(args["ButtonPath"][::-1].split('_', 1)[0][::-1]) - 1
			s = '{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[selected_merch_index])
			self.SetSprite(s + '/default', "textures/ui/netease_sale/btn01_select@3x")
			if self.m_selected_merch_index is not None and self.m_selected_merch_index != selected_merch_index:
				s = '{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[self.m_selected_merch_index])
				self.SetSprite(s + '/default', "textures/ui/netease_sale/btn01@3x")
			self.m_selected_merch_index = selected_merch_index
			item_dict = json.loads(self.m_merchs_cache[selected_merch_index]['stuff'])
			self.SetUiItem(self.m_merch_item_img, item_dict['itemName'], item_dict['auxValue'])
			self.SetSprite(self.m_cost_icon, self.m_merchs_cache[selected_merch_index]['currency'])
			self.SetText(self.m_cost_count_text, str(self.m_merchs_cache[selected_merch_index]['unit']))
			self.m_count_input_string = '1'
			self.SetText(self.m_count_edit_btn + '/button_label', self.m_count_input_string)
			self.SetVisible(self.m_cost_resp_bg, False)
			self.SetVisible(self.m_empty_text, False)
			self.SetVisible(self.m_interact_bg, True)
			self.SetVisible(self.m_op_panel.format(5), True)

	def on_touch_btn_num(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if not (self.m_calculator_panel_alive and self.m_edit_target):
				return
			num = int(args["ButtonPath"][-1])
			if not num and not getattr(self, self.m_edit_target[0]):
				return
			if '0' == getattr(self, self.m_edit_target[0]):
				setattr(self, self.m_edit_target[0], str(num))
			else:
				setattr(self, self.m_edit_target[0], getattr(self, self.m_edit_target[0]) + str(num))
			self.m_edit()

	def on_touch_btn_c(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if not (self.m_calculator_panel_alive and self.m_edit_target):
				return
			setattr(self, self.m_edit_target[0], '')
			self.SetText(self.m_edit_target[1], '')

	def on_touch_btn_ok(self, args):
		if args["TouchEvent"] == clientApi.GetMinecraftEnum().TouchEvent.TouchUp:
			if not self.m_calculator_panel_alive:
				return
			self.hide_calculator()

	def hide_calculator(self):
		if self.m_calculator_panel_alive:
			if self.m_edit_target:
				self.m_edit()
				self.m_edit_target = None
				self.m_edit = None
			self.m_calculator_panel_alive = False
			self.SetVisible(self.m_calculator_panel, False)

	def show_calculator(self, p):
		self.SetPosition(self.m_calculator_panel, p)
		self.m_calculator_panel_alive = True
		self.SetVisible(self.m_calculator_panel, True)

	@ViewBinder.binding(ViewBinder.BF_ButtonClickDown)
	def opt(self, args):
		if not self.m_debut:
			return
		if self.m_selected_slot_index is None:
			selected_slot_index = self.m_slot_list.index(args["ButtonPath"])
			item_dict = json.loads(self.m_inventory_cache[selected_slot_index])
			if not item_dict:
				return
			self.SetVisible('{}/selectedImg'.format(args["ButtonPath"]), True)
			if self.m_focus == 2 and self.m_countdown_cache and self.m_countdown_cache[-1] > 0:
				self.SetVisible(self.m_slot_item_img, True)
				self.SetVisible(self.m_mask_bg, False)
				self.SetVisible(self.m_resp_bg, False)
				self.SetVisible(self.m_interact_mask_bg, False)
				self.SetTouchEnable(self.m_interact_btn, True)
				self.SetUiItem(self.m_slot_item_img, item_dict['itemName'], item_dict['auxValue'])
				self.m_qty_input_string = '1'
				self.SetText(self.m_qty_edit_btn + '/button_label', self.m_qty_input_string)
			self.m_selected_slot_index = selected_slot_index
		else:
			selected_slot_index = self.m_slot_list.index(args["ButtonPath"])
			if self.m_selected_slot_index == selected_slot_index:
				self.SetVisible('{}/selectedImg'.format(args["ButtonPath"]), False)
				self.m_selected_slot_index = None
				if self.m_focus == 2:
					self.f2()
				return
			clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
				'SOS',
				{
					'playerId': clientApi.GetLocalPlayerId(),
					'f': self.m_selected_slot_index,
					't': selected_slot_index
				}
			)
			self.SetVisible('{}/selectedImg'.format(self.m_slot_list[self.m_selected_slot_index]), False)
			self.SetVisible('{}/selectedImg'.format(args["ButtonPath"]), True)
			self.m_selected_slot_index = selected_slot_index

	def alert(self, op):
		if not op:
			self.SetVisible(self.m_alert_text, True)
			self.SetText(self.m_alert_board_title_text, '结束摆摊')
			self.SetVisible(self.m_alert_board_merch_panel, False)
			self.SetVisible(self.m_alert_board_fee_panel, False)
			self.SetVisible(self.m_alert_bg, True)
			self.m_confirm = self.pack
		elif op == 1:
			self.SetVisible(self.m_alert_text, False)
			self.SetText(self.m_alert_board_title_text, '开始摆摊')
			self.SetVisible(self.m_alert_board_merch_panel, False)
			self.SetVisible(self.m_alert_board_fee_panel, True)
			self.SetSprite(self.m_alert_fee_icon, self.m_sale_rules['feetype'])
			self.SetText(self.m_alert_fee_count_text, str(self.m_sale_rules['hourlyfee'] * int(self.m_duration_input_string)))
			self.SetText(self.m_alert_fee_text[0], self.m_alert_fee_text[1].format(self.m_duration_input_string))
			self.SetVisible(self.m_alert_bg, True)
			self.m_confirm = self.turn
		elif op == 2:
			self.SetVisible(self.m_alert_text, False)
			self.SetText(self.m_alert_board_title_text, '上架商品')
			self.SetVisible(self.m_alert_board_fee_panel, False)
			self.SetVisible(self.m_alert_board_merch_panel, True)
			try:
				item_dict = json.loads(self.m_inventory_cache[self.m_selected_slot_index])
				self.SetUiItem(self.m_alert_slot_item_img, item_dict['itemName'], item_dict['auxValue'])
			except:
				return
			self.SetSprite(self.m_alert_price_icon, self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][1])
			self.SetText(self.m_alert_price_text, "单价：")
			self.SetText(self.m_alert_price_count_text, self.m_unit_input_string)
			self.SetText(self.m_alert_qty_text[0], self.m_alert_qty_text[1].format(self.m_qty_input_string))
			self.SetText(self.m_alert_merch_text, '是否上架以上商品？')
			self.SetVisible(self.m_alert_bg, True)
			self.m_confirm = self.load
		else:
			self.SetVisible(self.m_alert_text, False)
			self.SetText(self.m_alert_board_title_text, '购买商品')
			self.SetVisible(self.m_alert_board_fee_panel, False)
			self.SetVisible(self.m_alert_board_merch_panel, True)
			item_dict = json.loads(self.m_merchs_cache[self.m_selected_merch_index]['stuff'])
			self.SetUiItem(self.m_alert_slot_item_img, item_dict['itemName'], item_dict['auxValue'])
			self.SetSprite(self.m_alert_price_icon, self.m_merchs_cache[self.m_selected_merch_index]['currency'])
			self.SetText(self.m_alert_price_text, "总价：")
			self.SetText(self.m_alert_price_count_text, str(self.m_merchs_cache[self.m_selected_merch_index]['unit'] * int(self.m_count_input_string)))
			self.SetText(self.m_alert_qty_text[0], self.m_alert_qty_text[1].format(self.m_count_input_string))
			self.SetText(self.m_alert_merch_text, '是否购买以上商品？')
			self.SetVisible(self.m_alert_bg, True)
			self.m_confirm = self.rich

	def cancel(self):
		self.SetVisible(self.m_alert_bg, False)

	def turn(self):
		clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
			tradeConst.PlayerOpenStallEvent,
			{
				'playerId': clientApi.GetLocalPlayerId(),
				'label': self.m_input_string,
				'duration': int(self.m_duration_input_string),
			}
		)

	def pack(self):
		clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
			tradeConst.PlayerCloseStallEvent,
			{
				'playerId': clientApi.GetLocalPlayerId(),
			}
		)

	def fill(self):
		if not self.m_debut:
			slot_list = self.GetChildrenName(self.m_bag_panel + '/bag_grid')
			if not slot_list:
				return
			self.m_slot_list = ['{}/bag_grid/{}'.format(self.m_bag_panel, s) for s in slot_list]
			self.m_selected_slot_index = None
			self.m_debut = True
		for i, s in enumerate(self.m_slot_list):
			item_dict = json.loads(self.m_inventory_cache[i])
			if not item_dict:
				self.SetVisible('{}/itemImg'.format(s), False)
			else:
				self.SetVisible('{}/itemImg'.format(s), True)
				self.SetUiItem('{}/itemImg'.format(s), item_dict['itemName'], item_dict['auxValue'])
				self.SetText('{}/itemImg/itemNum'.format(s), str(item_dict['count']))

	def load(self):
		clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
			tradeConst.MerchOnSaleEvent,
			{
				'playerId': clientApi.GetLocalPlayerId(),
				'slot': self.m_selected_slot_index,
				'qty': int(self.m_qty_input_string),
				'stuff': self.m_inventory_cache[self.m_selected_slot_index],
				'currency': self.m_sale_rules['currencyoptions'][self.m_selected_currency_index][0],
				'unit': int(self.m_unit_input_string)
			}
		)

	def rich(self):
		clientApi.GetSystem(tradeConst.ModName, tradeConst.ClientSystemName).NotifyToServer(
			tradeConst.PlayerSpotMerchEvent,
			{
				'playerId': clientApi.GetLocalPlayerId(),
				'_id': self.m_merchs_cache[self.m_selected_merch_index]['_id'],
				'qty': int(self.m_count_input_string)
			}
		)

	def feedback(self, data):
		if not self.m_sale_panel_alive or self.m_focus != 2:
			return
		if data.get('reset'):
			self.f2()
		if 'merch' in data:
			self.m_merchs_cache.append(data['merch'])
			self.SetText(self.m_interact_btn + '/button_label', '上架（{} / {}）'.format(len(self.m_merchs_cache), self.m_sale_rules['merchcount']))
		self.SetText(self.m_resp_text, '§{}'.format(data['msg']))
		self.SetVisible(self.m_resp_bg, True)

	def open(self, data):
		uid = data['uid']
		owner = data['owner']
		stall = data['stall']
		self.m_deals_cache = stall and stall['deals'] or []
		merchs = data['merchs']
		self.m_merchs_cache = merchs
		rules = data['rules']
		if rules:
			self.m_sale_rules = rules
		self.hide_calculator()
		self.SetVisible(self.m_op_panel.format(5), False)
		if uid != owner:
			self.m_focus = 5
			self.m_selected_merch_index = None
			self.SetText(self.m_right_title_text, '购买')
			self.SetText(self.m_left_title_text, stall['label'])
			self.SetVisible(self.m_bag_panel, False)
			self.SetVisible(self.m_interact_bg, False)
			self.SetVisible(self.m_empty_text, True)
			self.SetText(self.m_empty_text, '请在左侧选择商品')
			for i in xrange(1, 5):
				self.SetVisible(self.m_tab_btn.format(i), False)
				self.SetVisible(self.m_op_panel.format(i), False)
			if not merchs:
				self.SetVisible('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/merch_list_view', False)
				self.SetVisible(self.m_merch_list_empty_text, True)
			else:
				self.m_interact = lambda: self.alert(5)
				self.SetText(self.m_interact_btn + '/button_label', '购买')
				self.SetTouchEnable(self.m_interact_btn, True)
				self.SetVisible(self.m_interact_mask_bg, False)
				self.SetVisible(self.m_merch_list_empty_text, False)
				# self.m_merchs_cache = merchs
				demand = len(merchs)
				cur = len(self.m_merch_list)
				if demand > cur:
					for i in xrange(cur + 1, demand + 1):
						s = 'merch_{}'.format(i)
						self.Clone('{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[0]), self.m_merch_list_panel, s)
						self.SetPosition('{}/{}'.format(self.m_merch_list_panel, s), (self.m_merch_pos[0], self.m_merch_pos[1] + self.m_merch_offset * (i - 1)))
						self.m_merch_list.append(s)
				self.SetSize(self.m_merch_list_panel, (self.m_merch_list_panel_size[0], self.m_merch_offset * demand + 10))
				for i, s in enumerate(self.m_merch_list):
					s = '{}/{}'.format(self.m_merch_list_panel, s)
					if i < demand:
						self.SetSprite(s + '/default', "textures/ui/netease_sale/btn01@3x")
						item_dict = json.loads(merchs[i]['stuff'])
						self.SetUiItem(s + self.m_merch_shortcut_item_img, item_dict['itemName'], item_dict['auxValue'])
						self.SetText(s + self.m_merch_stock_text[0], self.m_merch_stock_text[1].format((merchs[i]['qty'] > 0 and '{}' or '§c{}').format(merchs[i]['qty'])))
						self.SetText(s + self.m_price_count_text, str(merchs[i]['unit']))  # TODO: 有后续的货币显示列表界面就可以做判断余额不足标红显示
						self.SetSprite(s + self.m_price_icon, merchs[i]['currency'])
					self.SetVisible(s, i < demand)
				self.SetVisible('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/merch_list_view', True)
		else:
			self.m_focus = 1
			self.SetInputEnable(True)
			self.m_sale_panel_alive = True
			self.refresh(2, {'inventory': data['inventory']})
			demand = len(self.m_deals_cache)
			cur = len(self.m_deal_list)
			if demand > cur:
				for i in xrange(cur + 1, demand + 1):
					s = 'deal_{}'.format(i)
					self.Clone('{}/{}'.format(self.m_deal_list_panel, self.m_deal_list[0]), self.m_deal_list_panel, s)
					self.SetPosition('{}/{}'.format(self.m_deal_list_panel, s), (self.m_deal_pos[0], self.m_deal_pos[1] + self.m_deal_offset * (i - 1)))
					self.m_deal_list.append(s)
			self.SetSize(self.m_deal_list_panel, (self.m_deal_list_panel_size[0], self.m_deal_offset * demand + 10))
			for i, s in enumerate(self.m_deal_list):
				s = '{}/{}'.format(self.m_deal_list_panel, s)
				if i < demand:
					item_dict = json.loads(self.m_deals_cache[i][1])
					self.SetUiItem(s + self.m_deal_shortcut_item_img, item_dict['itemName'], item_dict['auxValue'])
					self.SetSprite(s + self.m_deal_unit_icon, self.m_deals_cache[i][3])
					self.SetSprite(s + self.m_deal_subtotal_icon, self.m_deals_cache[i][3])
					self.SetText(s + self.m_deal_unit_count_text, str(self.m_deals_cache[i][-3]))
					self.SetText(s + self.m_deal_subtotal_count_text, str(self.m_deals_cache[i][-1]))
					self.SetText(s + self.m_deal_sale_text[0], self.m_deal_sale_text[1].format(self.m_deals_cache[i][-2]))
					self.SetText(s + self.m_rich_name_text, self.m_deals_cache[i][2])
					self.SetText(s + self.m_datetime_text, self.m_deals_cache[i][0])
				self.SetVisible(s, i < demand)
			self.SetText(self.m_right_title_text, '摊位')
			self.SetText(self.m_left_title_text, '可出售的商品')
			self.SetVisible('/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/sale_bg/select_panel/merch_list_view', False)
			self.SetVisible(self.m_merch_list_empty_text, False)
			self.SetVisible(self.m_empty_text, False)
			self.SetVisible(self.m_interact_bg, True)
			self.SetTouchEnable(self.m_interact_btn, True)
			self.SetVisible(self.m_interact_mask_bg, False)
			for i in xrange(1, 5):
				self.SetSprite(self.m_tab_btn.format(i) + '/default', i == 1 and "textures/ui/netease_sale/tab01_click@3x" or (i == 4 and "textures/ui/netease_sale/tab02@3x" or "textures/ui/netease_sale/tab01@3x"))
				self.SetVisible(self.m_op_panel.format(i), i == 1)
				self.SetVisible(self.m_tab_btn.format(i), True)
			self.SetSprite(self.m_fee_icon, self.m_sale_rules['feetype'])
			if not stall:
				self.on()
				self.m_duration_input_string = '1'
				self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
				self.SetText(self.m_fee_count_text, str(self.m_sale_rules['hourlyfee']))
			else:
				self.m_input_string = stall['label']
				self.SetText(self.m_title_text + self.m_plain_text, stall['label'])
				self.m_duration_input_string = str(stall['duration'])
				self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
				self.SetText(self.m_fee_count_text, str(stall['duration'] * self.m_sale_rules['hourlyfee']))
				self.SetText(self.m_duration_text, '摆摊总时间：')
				self.SetText(self.m_duration_text + self.m_plain_text, '{}小时'.format(stall['duration']))
				self.m_countdown_cache = [time.time(), stall['deadline'] - data['time'] - 4]
				self.off()

		self.SetVisible("", True)

		self.SetVisible(self.m_sale_panel, True)
		self.m_sale_panel_alive = True
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)

	def refresh(self, op, data):
		if not self.m_sale_panel_alive:
			return
		if not op:
			self.m_countdown_cache = None
			if self.m_focus == 1:
				self.f1()
			if self.m_focus == 2:
				self.f2()
		if op == 1:
			if not data.get('uid'):
				return
			self.m_input_string = data['label']
			self.SetText(self.m_title_text + self.m_plain_text, data['label'])
			self.m_duration_input_string = str(data['duration'])
			self.SetText(self.m_duration_edit_btn + '/button_label', self.m_duration_input_string)
			# self.SetText(self.m_fee_count_text, str(data['duration'] * self.m_sale_rules['hourlyfee']))
			self.SetText(self.m_duration_text, '摆摊总时间：')
			self.SetText(self.m_duration_text + self.m_plain_text, '{}小时'.format(data['duration']))
			self.m_countdown_cache = [time.time(), data['deadline'] - data['time'] - 4]
			self.SetText(self.m_resp_text, '§e请在左侧选择要上架的商品')
			if self.m_focus == op:
				self.off()
		if op == 2 and self.m_focus != 5:
			self.m_inventory_cache = data['inventory']
			self.SetVisible(self.m_bag_panel, True)
			if not self.m_debut:
				comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
				comp.AddTimer(1, self.fill)
			else:
				self.fill()
		if op == 3:
			_id = data['_id']
			if op == self.m_focus or data.get('upgradable'):
				for i in xrange(len(self.m_merchs_cache)):
					if self.m_merchs_cache[i] and self.m_merchs_cache[i]['_id'] == _id:
						if data.get('upgradable'):
							if op == self.m_focus:
								self.m_merchs_cache[i] = None
								self.SetText('{}/{}'.format(self.m_manage_panel, self.m_option_list[i]) + self.m_consequence_text, '已下架')
							else:
								del self.m_merchs_cache[i]
								if self.m_focus == 2:
									self.SetText(self.m_interact_btn + '/button_label', '上架（{} / {}）'.format(len(self.m_merchs_cache), self.m_sale_rules['merchcount']))
						else:
							self.SetText('{}/{}'.format(self.m_manage_panel, self.m_option_list[i]) + self.m_consequence_text, '下架失败')
						break
		if op == self.m_focus == 5:
			if not data.get('_id'):
				self.SetInputEnable(False)
				if self.m_sale_panel_alive:
					self.SetVisible(self.m_sale_panel, False)

					self.SetVisible("", False)

					self.m_sale_panel_alive = False
					clientApi.SetInputMode(0)
					clientApi.HideSlotBarGui(False)
				return
			self.SetText(self.m_cost_resp_text, 'msg' in data and '§c{}'.format(data['msg']) or '§a购买成功！')
			self.SetVisible(self.m_cost_resp_bg, True)
			for i, merch in enumerate(self.m_merchs_cache):
				if merch and merch['_id'] == data['_id']:
					if 'msg' in data:
						merch['qty'] = data['qty']
					else:
						merch['qty'] -= data['qty']
					s = '{}/{}'.format(self.m_merch_list_panel, self.m_merch_list[i])
					self.SetText(s + self.m_merch_stock_text[0], self.m_merch_stock_text[1].format((self.m_merchs_cache[i]['qty'] > 0 and '{}' or '§c{}').format(self.m_merchs_cache[i]['qty'])))
					break
		if op == 4:
			self.m_deals_cache.append(data['deal'])
			if self.m_focus == op:
				self.SetVisible(self.m_empty_text, False)
			demand = len(self.m_deals_cache)
			cur = len(self.m_deal_list)
			if demand > cur:
				for i in xrange(cur + 1, demand + 1):
					s = 'deal_{}'.format(i)
					self.Clone('{}/{}'.format(self.m_deal_list_panel, self.m_deal_list[0]), self.m_deal_list_panel, s)
					self.SetPosition('{}/{}'.format(self.m_deal_list_panel, s), (self.m_deal_pos[0], self.m_deal_pos[1] + self.m_deal_offset * (i - 1)))
					self.m_deal_list.append(s)
			self.SetSize(self.m_deal_list_panel, (self.m_deal_list_panel_size[0], self.m_deal_offset * demand + 10))
			i = demand - 1
			s = '{}/{}'.format(self.m_deal_list_panel, self.m_deal_list[i])
			item_dict = json.loads(self.m_deals_cache[i][1])
			self.SetUiItem(s + self.m_deal_shortcut_item_img, item_dict['itemName'], item_dict['auxValue'])
			self.SetSprite(s + self.m_deal_unit_icon, self.m_deals_cache[i][3])
			self.SetSprite(s + self.m_deal_subtotal_icon, self.m_deals_cache[i][3])
			self.SetText(s + self.m_deal_unit_count_text, str(self.m_deals_cache[i][-3]))
			self.SetText(s + self.m_deal_subtotal_count_text, str(self.m_deals_cache[i][-1]))
			self.SetText(s + self.m_deal_sale_text[0], self.m_deal_sale_text[1].format(self.m_deals_cache[i][-2]))
			self.SetText(s + self.m_rich_name_text, self.m_deals_cache[i][2])
			self.SetText(s + self.m_datetime_text, self.m_deals_cache[i][0])
			self.SetVisible(s, True)
			for i, merch in enumerate(self.m_merchs_cache):
				if merch and merch['_id'] == data['deal'][4]:
					merch['qty'] -= data['deal'][-2]
					s = '{}/{}'.format(self.m_manage_panel, self.m_option_list[i])
					self.SetText(s + self.m_option_subtotal_count_text, str((self.m_merchs_cache[i]['init'] - self.m_merchs_cache[i]['qty']) * self.m_merchs_cache[i]['unit']))
					self.SetText(s + self.m_option_sale_text[0], self.m_option_sale_text[1].format(self.m_merchs_cache[i]['init'] - self.m_merchs_cache[i]['qty'], self.m_merchs_cache[i]['init']))
					break
