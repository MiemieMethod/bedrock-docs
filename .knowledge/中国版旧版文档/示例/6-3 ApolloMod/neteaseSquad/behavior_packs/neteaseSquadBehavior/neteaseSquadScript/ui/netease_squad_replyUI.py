# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseSquadScript.squadConst as squadConst
import json
import uiDef

class SquadReplyScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "SquadReplyScreen", namespace, name, param
		
		self.m_uid = None
		self.m_squad_cache = None
		
		self.m_reply_board_alive = False
		self.m_reply_board = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg'
		self.m_reply_board_close_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg/reply_board_close_btn'
		self.m_reply_board_empty_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg/reply_board_empty_text'
		self.m_reply_board_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg/reply_board_panel'
		self.m_reply_bar_count = 1
		self.m_reply_bar = 'reply_bar_{}'
		self.m_applicant_name_text = 'reply_bar_{}/applicant_name_text'
		self.m_applicant_lv_text = 'reply_bar_{}/applicant_lv_text'
		self.m_agree_btn = 'reply_bar_{}/agree_btn'
		self.m_reject_btn = 'reply_bar_{}/reject_btn'
		self.m_reply_consequence_text = 'reply_bar_{}/reply_consequence_text'
		self.m_reply_board_clear_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg/reply_board_clear_btn'
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def activate(self):
		self.ChangeScreenVisible(True)
	
	def deactivate(self):
		self.ChangeScreenVisible(False)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.m_reply_board_alive = flag
		if flag:
			clientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			clientApi.SetInputMode(0)
			self.SetInputEnable(False)
	
	def Create(self):
		print '==== %s ====' % 'SquadReplyScreen Create'

		reply_list_view = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/reply_board_bg/reply_board_panel/reply_list_view'
		mouse = '{}/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		touch = '{}/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.m_reply_list_panel = touch.format(reply_list_view)
		reply_list_panel_size = self.GetSize(self.m_reply_list_panel)
		if not reply_list_panel_size:
			self.m_reply_list_panel = mouse.format(reply_list_view)
		self.m_reply_list_panel_size = self.GetSize(self.m_reply_list_panel)
		reply_bar = '{}/{}'.format(self.m_reply_list_panel, self.m_reply_bar.format(1))
		reply_bar_size = self.GetSize(reply_bar)
		self.m_reply_bar_offset = reply_bar_size[-1]
		self.m_reply_bar_pos = self.GetPosition(reply_bar)
		self.AddTouchEventHandler(self.m_reply_board_close_btn, self.on_touch_btn_reply_board_close)
		self.AddTouchEventHandler('{}/{}'.format(self.m_reply_list_panel, self.m_agree_btn.format(1)), self.on_touch_btn_agree)
		self.AddTouchEventHandler('{}/{}'.format(self.m_reply_list_panel, self.m_reject_btn.format(1)), self.on_touch_btn_reject)
		self.AddTouchEventHandler(self.m_reply_board_clear_btn, self.on_touch_btn_reply_board_clear)
		
	def on_touch_btn_reply_board_close(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			if self.m_reply_board_alive:
				self.m_reply_board_alive = False
				self.ChangeScreenVisible(False)
				clientApi.SetInputMode(0)
				clientApi.HideSlotBarGui(False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_agree(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			uid = self.m_applicants_cache[int(args["ButtonPath"][::-1].split('/', 2)[1].split('_', 1)[0][::-1]) - 1]['uid']
			print uid
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SquadAppendPlayerEvent,
				{'playerId': clientApi.GetLocalPlayerId(), 'uid': uid}
			)
			reply_consequence_text = '{}{}'.format(args["ButtonPath"][:-9], 'reply_consequence_text')
			self.SetText(reply_consequence_text, '处理中')
			self.SetVisible(reply_consequence_text, True)
			self.SetVisible('{}{}'.format(args["ButtonPath"][:-9], 'reject_btn'), False)
			self.SetVisible(args["ButtonPath"], False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_01_click@3x")
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_01@3x")
			
	def on_touch_btn_reject(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			uid = self.m_applicants_cache[int(args["ButtonPath"][::-1].split('/', 2)[1].split('_', 1)[0][::-1]) - 1]['uid']
			print uid
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SquadRejectPlayerEvent,
				{'playerId': clientApi.GetLocalPlayerId(), 'uid': uid}
			)
			reply_consequence_text = '{}{}'.format(args["ButtonPath"][:-10], 'reply_consequence_text')
			self.SetText(reply_consequence_text, '已拒绝')
			self.SetVisible(reply_consequence_text, True)
			self.SetVisible('{}{}'.format(args["ButtonPath"][:-10], 'agree_btn'), False)
			self.SetVisible(args["ButtonPath"], False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_02_click@3x")
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_02@3x")
			
	def on_touch_btn_reply_board_clear(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SquadApplicantsClearEvent,
				{'playerId': clientApi.GetLocalPlayerId()}
			)
			self.SetTouchEnable(self.m_reply_board_clear_btn, False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def update_reply_board(self, data):
		if not self.m_reply_board_alive:
			return
		uid = data['entity']['uid']
		for i in xrange(len(self.m_applicants_cache)):
			if self.m_applicants_cache[i]['uid'] == uid:
				if data['code'] == squadConst.RespCodeSuccess:
					consequence = '已同意'
				else:
					# consequence = '无法加入队伍'
					consequence = data['message']
				self.SetText('{}/{}'.format(self.m_reply_list_panel, self.m_reply_consequence_text.format(i + 1)), consequence)
				break

	def display_reply_board(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid != self.m_uid:
			self.m_uid = uid
		applicants = data.get('applicants', [])
		self.m_applicants_cache = applicants
		if applicants:
			count = len(applicants)
			if count > self.m_reply_bar_count:
				# 需要加
				for i in xrange(self.m_reply_bar_count, count):
					self.Clone('{}/{}'.format(self.m_reply_list_panel, self.m_reply_bar.format(1)), self.m_reply_list_panel, self.m_reply_bar.format(i + 1))
					self.SetPosition('{}/{}'.format(self.m_reply_list_panel, self.m_reply_bar.format(i + 1)), (self.m_reply_bar_pos[0], self.m_reply_bar_pos[-1] + self.m_reply_bar_offset * i))
				self.m_reply_bar_count = count
			self.SetSize(self.m_reply_list_panel, (self.m_reply_list_panel_size[0], (self.m_reply_bar_offset * count) if self.m_reply_bar_offset * count > self.m_reply_list_panel_size[-1] else self.m_reply_list_panel_size[-1]))
			for i in xrange(1, self.m_reply_bar_count + 1):
				reply_bar = '{}/{}'.format(self.m_reply_list_panel, self.m_reply_bar.format(i))
				if i > count:
					self.SetVisible(reply_bar, False)
				else:
					line = applicants[i - 1]
					self.SetText('{}/{}'.format(self.m_reply_list_panel, self.m_applicant_name_text.format(i)), line['name'])
					self.SetText('{}/{}'.format(self.m_reply_list_panel, self.m_applicant_lv_text.format(i)), str(line['lv']))
					self.SetVisible('{}/{}'.format(self.m_reply_list_panel, self.m_reply_consequence_text.format(i)), False)
					self.SetSprite('{}/{}'.format(self.m_reply_list_panel, self.m_agree_btn.format(i)) + '/pretender', "textures/ui/netease_squad/btn_operation_01@3x")
					self.SetSprite('{}/{}'.format(self.m_reply_list_panel, self.m_reject_btn.format(i)) + '/pretender', "textures/ui/netease_squad/btn_operation_02@3x")
					self.SetVisible('{}/{}'.format(self.m_reply_list_panel, self.m_agree_btn.format(i)), True)
					self.SetVisible('{}/{}'.format(self.m_reply_list_panel, self.m_reject_btn.format(i)), True)
					self.SetVisible(reply_bar, True)
			self.SetVisible(self.m_reply_board_panel, True)
			self.SetVisible(self.m_reply_board_empty_text, False)
		else:
			self.SetVisible(self.m_reply_board_panel, False)
			self.SetVisible(self.m_reply_board_empty_text, True)
		self.m_reply_board_alive = True
		self.ChangeScreenVisible(True)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)
		self.SetTouchEnable(self.m_reply_board_clear_btn, True)
		clsbtn_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadClsBtn)
		clsbtn_ui_node.SetVisible(clsbtn_ui_node.m_notice_icon, False)
		
	def clear_reply_board(self):
		if not self.m_reply_board_alive:
			return
		self.SetVisible(self.m_reply_board_panel, False)
		self.SetVisible(self.m_reply_board_empty_text, True)
		clsbtn_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadClsBtn)
		clsbtn_ui_node.SetVisible(clsbtn_ui_node.m_notice_icon, False)
		
	def dispose(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		squad = data.get('squad')
		self.m_squad_cache = squad
		if not squad:
			if self.m_reply_board_alive:
				self.m_reply_board_alive = False
				#self.SetVisible(self.m_reply_board, False)
				self.ChangeScreenVisible(False)
				clientApi.SetInputMode(0)
				clientApi.HideSlotBarGui(False)
		else:
			if squad['chief'] != self.m_uid:
				if self.m_reply_board_alive:
					self.m_reply_board_alive = False
					self.ChangeScreenVisible(False)
					clientApi.SetInputMode(0)
					clientApi.HideSlotBarGui(False)
		
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

