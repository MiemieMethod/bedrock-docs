# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseSquadScript.squadConst as squadConst
import json

class SquadApplyScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "SquadApplyScreen", namespace, name, param
		
		self.m_apply_board_alive = False
		self.m_squad_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel'
		self.m_squad_standard_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/squad_standard_panel'
		self.m_apply_board = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/apply_board_bg'
		self.m_apply_board_close_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/apply_board_bg/apply_board_close_btn'
		self.m_apply_board_empty_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/apply_board_bg/apply_board_empty_text'
		self.m_apply_board_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/apply_board_bg/apply_board_panel'
		self.m_apply_bar_count = 1
		self.m_apply_bar = 'apply_bar_{}'
		self.m_squad_leader_name_text = 'apply_bar_{}/squad_leader_name_text'
		self.m_squad_count_text = 'apply_bar_{}/squad_count_text'
		self.m_apply_comment_text = 'apply_bar_{}/apply_comment_text'
		self.m_apply_btn = 'apply_bar_{}/apply_btn'
		self.m_apply_consequence_text = 'apply_bar_{}/apply_consequence_text'
		
		self.m_uid = None
		self.m_squad_cache = None
	
	def InitScreen(self):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			#self.SetVisible(self.m_squad_panel, False)
			self.ChangeScreenVisible(False)
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				'EnableUI',
				{'playerId': clientApi.GetLocalPlayerId()}
			)
			
	def activate(self):
		self.ChangeScreenVisible(False)
		#self.SetVisible(self.m_squad_panel, True)

	def deactivate(self):
		self.ChangeScreenVisible(False)
		#self.SetVisible(self.m_squad_panel, False)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		self.m_apply_board_alive = flag
		if flag:
			clientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			clientApi.SetInputMode(0)
			self.SetInputEnable(False)
	
	def Create(self):
		apply_list_view = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/apply_board_bg/apply_board_panel/apply_list_view'
		touch = '{}/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content'
		mouse = '{}/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content'
		self.m_apply_list_panel = touch.format(apply_list_view)
		apply_list_panel_size = self.GetSize(self.m_apply_list_panel)
		if not apply_list_panel_size:
			self.m_apply_list_panel = mouse.format(apply_list_view)
		self.m_apply_list_panel_size = self.GetSize(self.m_apply_list_panel)
		apply_bar = '{}/{}'.format(self.m_apply_list_panel, self.m_apply_bar.format(1))
		apply_bar_size = self.GetSize(apply_bar)
		self.m_apply_bar_offset = apply_bar_size[-1]
		self.m_apply_bar_pos = self.GetPosition(apply_bar)
		self.AddTouchEventHandler(self.m_apply_board_close_btn, self.on_touch_btn_apply_board_close)
		self.AddTouchEventHandler('{}/{}'.format(self.m_apply_list_panel, self.m_apply_btn.format(1)), self.on_touch_btn_apply)
		
	def on_touch_btn_apply_board_close(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			if self.m_apply_board_alive:
				self.m_apply_board_alive = False
				#self.SetVisible(self.m_apply_board, False)
				self.ChangeScreenVisible(False)
				clientApi.SetInputMode(0)
				clientApi.HideSlotBarGui(False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)

	def on_touch_btn_apply(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			order = self.m_recruitment_cache[int(args["ButtonPath"][-11::-1].split('/', 1)[0].split('_', 1)[0][::-1]) - 1]['order']
			print order
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SquadRecruitmentApplyEvent,
				{'playerId': clientApi.GetLocalPlayerId(), 'order': order}
			)
			self.SetTouchEnable(args["ButtonPath"], False)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_03_click@3x")
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			self.SetSprite(args["ButtonPath"] + '/pretender', "textures/ui/netease_squad/btn_operation_03@3x")
			
	def update_apply_board(self, data):
		if not self.m_apply_board_alive:
			return
		order = data['entity']['order']
		for i in xrange(len(self.m_recruitment_cache)):
			if self.m_recruitment_cache[i]['order'] == order:
				self.SetVisible('{}/{}'.format(self.m_apply_list_panel, self.m_apply_btn.format(i + 1)), False)
				apply_consequence_text = '{}/{}'.format(self.m_apply_list_panel, self.m_apply_consequence_text.format(i + 1))
				if data['code'] == squadConst.RespCodeSuccess:
					consequence = '已申请'
				else:
					consequence = '申请失败'
				self.SetText(apply_consequence_text, consequence)
				self.SetVisible(apply_consequence_text, True)
				break
				
	def display_apply_board(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		print "display_apply_board", data
		uid = data.get('uid')
		if uid != self.m_uid:
			self.m_uid = uid
		recruitment = data.get('recruitment', [])
		recruitment.reverse()
		self.m_recruitment_cache = recruitment
		if recruitment:
			count = len(recruitment)
			if count > self.m_apply_bar_count:
				# 需要加
				for i in xrange(self.m_apply_bar_count, count):
					self.Clone('{}/{}'.format(self.m_apply_list_panel, self.m_apply_bar.format(1)), self.m_apply_list_panel, self.m_apply_bar.format(i + 1))
					self.SetPosition('{}/{}'.format(self.m_apply_list_panel, self.m_apply_bar.format(i + 1)), (self.m_apply_bar_pos[0], self.m_apply_bar_pos[-1] + self.m_apply_bar_offset * i))
				self.m_apply_bar_count = count
			self.SetSize(self.m_apply_list_panel, (self.m_apply_list_panel_size[0], (self.m_apply_bar_offset * count) if self.m_apply_bar_offset * count > self.m_apply_list_panel_size[-1] else self.m_apply_list_panel_size[-1]))
			for i in xrange(1, self.m_apply_bar_count + 1):
				apply_bar = '{}/{}'.format(self.m_apply_list_panel, self.m_apply_bar.format(i))
				if i > count:
					self.SetVisible(apply_bar, False)
				else:
					line = recruitment[i - 1]
					self.SetText('{}/{}'.format(self.m_apply_list_panel, self.m_squad_leader_name_text.format(i)), line['name'])
					self.SetText('{}/{}'.format(self.m_apply_list_panel, self.m_squad_count_text.format(i)), str(line['count']))
					self.SetText('{}/{}'.format(self.m_apply_list_panel, self.m_apply_comment_text.format(i)), line['label'])
					consequence = None
					if isinstance(line['applicable'], int) and line['applicable'] > 0:
						applicable = True
					else:
						applicable = False
						if isinstance(line['applicable'], bool):
							consequence = '已申请'
						else:
							consequence = '申请人数过多'
					apply_btn = '{}/{}'.format(self.m_apply_list_panel, self.m_apply_btn.format(i))
					self.SetVisible(apply_btn, applicable)
					applicable and (self.SetTouchEnable(apply_btn, applicable), self.SetSprite(apply_btn + '/pretender', "textures/ui/netease_squad/btn_operation_03@3x"))
					apply_consequence_text = '{}/{}'.format(self.m_apply_list_panel, self.m_apply_consequence_text.format(i))
					if consequence:
						self.SetText(apply_consequence_text, consequence)
					self.SetVisible(apply_consequence_text, not applicable)
					self.SetVisible(apply_bar, True)
			self.SetVisible(self.m_apply_board_panel, True)
			self.SetVisible(self.m_apply_board_empty_text, False)
		else:
			self.SetVisible(self.m_apply_board_panel, False)
			self.SetVisible(self.m_apply_board_empty_text, True)
		#self.SetVisible(self.m_squad_panel, True)
		self.m_apply_board_alive = True
		#self.SetVisible(self.m_apply_board, True)
		self.ChangeScreenVisible(True)
		clientApi.SetInputMode(1)
		clientApi.HideSlotBarGui(True)
		
	def dispose(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		squad = data.get('squad')
		turn = squad and not self.m_squad_cache
		self.m_squad_cache = squad
		if turn:
			self.SetVisible(self.m_squad_standard_panel, False)
			if self.m_apply_board_alive:
				self.m_apply_board_alive = False
				#self.SetVisible(self.m_apply_board, False)
				self.ChangeScreenVisible(False)
				clientApi.SetInputMode(0)
				clientApi.HideSlotBarGui(False)
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

