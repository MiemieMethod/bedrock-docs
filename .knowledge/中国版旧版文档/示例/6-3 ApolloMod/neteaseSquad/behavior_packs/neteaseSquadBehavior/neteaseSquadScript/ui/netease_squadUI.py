# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
import weakref
import neteaseSquadScript.squadConst as squadConst
import json

class SquadMainScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "SquadMainScreen", namespace, name, param
		
		self.m_uid = None
		self.m_squad_cache = None
		
		self.m_squad_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel'
		self.m_squad_standard_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/squad_standard_panel'
		self.m_squad_create_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/squad_standard_panel/squad_create_btn'
		self.m_squad_search_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/squad_standard_panel/squad_search_btn'
	
	def InitScreen(self):
		self.ChangeScreenVisible(True)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		if flag:
			#clientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			#clientApi.SetInputMode(0)
			self.SetInputEnable(False)
	
	def activate(self):
		self.ChangeScreenVisible(True)
	
	def deactivate(self):
		self.ChangeScreenVisible(False)
			
	def Create(self):
		self.AddTouchEventHandler(self.m_squad_create_btn, self.on_touch_btn_squad_create)
		self.AddTouchEventHandler(self.m_squad_search_btn, self.on_touch_btn_squad_search)
		
	def on_touch_btn_squad_create(self, args):
		print "on_touch_btn_squad_create =============================="
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SetupSquadEvent,
				{'playerId': clientApi.GetLocalPlayerId()}
			)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_squad_search(self, args):
		print "on_touch_btn_squad_search =============================="
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
				squadConst.SquadRecruitListEvent,
				{'playerId': clientApi.GetLocalPlayerId()}
			)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def dispose(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		squad = data.get('squad')
		turn = squad and not self.m_squad_cache
		self.m_squad_cache = squad
		if not squad:
			self.ChangeScreenVisible(True)
		else:
			if turn:
				self.ChangeScreenVisible(False)
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

