# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseSquadScript.squadConst as squadConst
import json

class SquadAlertScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "SquadAlertScreen", namespace, name, param
		
		self.m_input_text_field = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/recruit_panel/input_text_field'
		self.m_input_string = '不得超过七个字'
		
		self.m_squad_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel'
		self.m_alert = None
		self.m_alert_board = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg'
		self.m_confirm_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/confirm_btn'
		self.m_cancel_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/cancel_btn'
		self.m_title_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/title_text'
		self.m_recruit_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/recruit_panel'
		self.m_alert_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/alert_board_bg/alert_text'
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
		
		self.AddTouchEventHandler(self.m_confirm_btn, self.on_touch_btn_confirm)
		self.AddTouchEventHandler(self.m_cancel_btn, self.on_touch_btn_cancel)
		
		self.post_input_string()
		
	def activate(self):
		self.ChangeScreenVisible(True)

	def deactivate(self):
		self.ChangeScreenVisible(False)
	
	def on_touch_btn_confirm(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			if self.m_alert:
				self.m_alert()
			self.ChangeScreenVisible(False)
			self.m_alert = None
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def on_touch_btn_cancel(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			input_ui_node = clientApi.GetUI(squadConst.ModName, 'inputUI')
			if input_ui_node:
				input_ui_node.post_input_string()
			self.ChangeScreenVisible(False)
			# self.SetTouchEnable(self.m_cls_btn, True)
			self.m_cls_btn_alive = 1
			self.m_alert = None
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		if flag:
			clientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			clientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def set_input_string(self, args):
		self.m_input_string = args["Text"]
		return ViewRequest.Refresh

	@ViewBinder.binding(ViewBinder.BF_BindString)
	def get_input_string(self):
		return self.m_input_string

	def pre_input_string(self):
		print 'pre_input_string'
		self.SetInputEnable(True)
		#self.SetVisible(self.m_input_text_field, True)

	def post_input_string(self):
		print 'post_input_string'
		self.SetInputEnable(False)
		#self.SetVisible(self.m_input_text_field, False)
		return self.m_input_string
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

