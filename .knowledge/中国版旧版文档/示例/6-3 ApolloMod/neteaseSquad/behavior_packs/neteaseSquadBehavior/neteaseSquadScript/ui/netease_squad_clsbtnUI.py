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

class SquadClsBtnScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print "SquadClsBtnScreen", namespace, name, param
		
		self.m_uid = None
		self.m_squad_cache = None
		
		self.m_cls_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn'
		self.m_clear_btn = self.m_cls_btn + '/clear_btn'
		self.m_cls_btn_alive = None
		self.m_squad_optional_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel'
		self.m_leave_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/leave_btn'
		self.m_find_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/find_btn'
		self.m_dude = 0
		self.m_dude_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/dude_{}'
		self.m_dude_name_text = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/dude_{0}/name_text_{0}'
		self.m_notice_icon = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/dude_1/notice_icon'
		self.m_leader_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/leader_panel'
		self.m_recruit_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/leader_panel/recruit_btn'
		self.m_approve_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/leader_panel/approve_btn'
		self.m_dissolve_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/leader_panel/dissolve_btn'
		self.m_member_panel = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/member_panel'
		self.m_transfer_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/member_panel/transfer_btn'
		self.m_kick_btn = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/scope_panel/cls_btn/squad_optional_panel/member_panel/kick_btn'
	
	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def activate(self):
		self.ChangeScreenVisible(True)
	
	def deactivate(self):
		self.ChangeScreenVisible(False)
	
	def ChangeScreenVisible(self, flag):
		self.SetVisible("", flag)
		if flag:
			clientApi.SetInputMode(1)
			self.SetInputEnable(True)
		else:
			clientApi.SetInputMode(0)
			self.SetInputEnable(False)
			
	def Create(self):
		self.AddTouchEventHandler(self.m_clear_btn, self.on_touch_btn_cls)
		self.AddTouchEventHandler(self.m_find_btn, self.on_touch_btn_recruit)
		self.AddTouchEventHandler(self.m_leave_btn, self.on_touch_btn_leave)
		for i in xrange(1, 6):
			self.AddTouchEventHandler(self.m_dude_btn.format(i), self.on_touch_btn_dude)
		self.AddTouchEventHandler(self.m_recruit_btn, self.on_touch_btn_call)
		self.AddTouchEventHandler(self.m_approve_btn, self.on_touch_btn_approve)
		self.AddTouchEventHandler(self.m_dissolve_btn, self.on_touch_btn_dissolve)
		self.AddTouchEventHandler(self.m_transfer_btn, self.on_touch_btn_transfer)
		self.AddTouchEventHandler(self.m_kick_btn, self.on_touch_btn_kick)
		
		dude_pos = self.GetPosition(self.m_dude_btn.format(1))
		self.m_dude_offset = self.GetPosition(self.m_dude_btn.format(2))[-1] - dude_pos[-1]
		self.m_member_panel_pos = self.GetPosition(self.m_member_panel)
		
	def on_touch_btn_recruit(self, args):
		print "on_touch_btn_recruit"
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			# self.SetTouchEnable(self.m_cls_btn, False)
			self.m_cls_btn_alive = -1
			alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
			if alert_ui_node:
				alert_ui_node.pre_input_string()
			alert_ui_node.SetText(alert_ui_node.m_title_text, '队员招募')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '发布')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '取消')
			alert_ui_node.SetVisible(alert_ui_node.m_alert_text, False)
			alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, True)
			self.SetVisible(self.m_leader_panel, False)
			self.SetVisible(self.m_member_panel, False)
			self.SetVisible(self.m_clear_btn, False)
			alert_ui_node.SetVisible("", True)
			alert_ui_node.m_alert = self.recruit
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def recruit(self):
		input_string = '不得超过七个字'
		alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
		if alert_ui_node:
			input_string = alert_ui_node.post_input_string()
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.SquadPlayerRecruitEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'label': input_string}
		)
		# self.SetTouchEnable(self.m_cls_btn, True)
		self.m_cls_btn_alive = 1
		
	def leave(self):
		print "leave SquadPlayerLeaveEvent"
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.SquadPlayerLeaveEvent,
			{'playerId': clientApi.GetLocalPlayerId()}
		)
			
	def on_touch_btn_leave(self, args):
		print "on_touch_btn_leave"
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
			if alert_ui_node:
				alert_ui_node.pre_input_string()
			alert_ui_node.SetText(alert_ui_node.m_title_text, '离开队伍')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '离开')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '取消')
			alert_ui_node.SetText(alert_ui_node.m_alert_text, '是否离开队伍？')
			alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
			alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
			self.SetVisible(self.m_leader_panel, False)
			self.SetVisible(self.m_member_panel, False)
			self.SetVisible(self.m_clear_btn, False)
			alert_ui_node.SetVisible("", True)
			alert_ui_node.m_alert = self.leave
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_dude(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			self.m_dude = index = int(args["ButtonPath"][-1])
			print "on_touch_btn_dude", self.m_dude, self.m_squad_cache, self.m_squad_cache['chief']
			if self.m_squad_cache and self.m_squad_cache['chief'] == self.m_uid:
				if index == 1:
					self.SetVisible(self.m_member_panel, False)
					self.SetVisible(self.m_leader_panel, True)
				else:
					self.SetVisible(self.m_leader_panel, False)
					self.SetPosition(self.m_member_panel, (self.m_member_panel_pos[0], self.m_member_panel_pos[-1] + self.m_dude_offset * (index - 1)))
					self.SetVisible(self.m_member_panel, True)
				self.SetVisible(self.m_clear_btn, True)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_call(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
			if not alert_ui_node.m_alert:
				self.SetVisible(self.m_leader_panel, False)
				self.SetVisible(self.m_member_panel, False)
				self.SetVisible(self.m_clear_btn, False)
				clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
					squadConst.AssembleEvent,
					{'playerId': clientApi.GetLocalPlayerId()}
				)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_approve(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
			reply_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadReply)
			if not (alert_ui_node.m_alert and reply_ui_node.m_reply_board_alive):
				self.SetVisible(self.m_leader_panel, False)
				self.SetVisible(self.m_member_panel, False)
				self.SetVisible(self.m_clear_btn, False)
				clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
					squadConst.SquadApplyListEvent,
					{'playerId': clientApi.GetLocalPlayerId()}
				)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def on_touch_btn_dissolve(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
			alert_ui_node.SetText(alert_ui_node.m_title_text, '解散队伍')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '是')
			alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '否')
			alert_ui_node.SetText(alert_ui_node.m_alert_text, '是否确定解散队伍？')
			alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
			alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
			self.SetVisible(self.m_leader_panel, False)
			self.SetVisible(self.m_member_panel, False)
			self.SetVisible(self.m_clear_btn, False)
			alert_ui_node.SetVisible("", True)
			alert_ui_node.m_alert = self.dissolve
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def dissolve(self):
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.DissolveSquadEvent,
			{'playerId': clientApi.GetLocalPlayerId()}
		)
			
	def on_touch_btn_transfer(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			if self.m_dude:
				dude = self.m_dudes[self.m_dude - 1]
				alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
				if dude:
					alert_ui_node.SetText(alert_ui_node.m_title_text, '转让队长')
					alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '是')
					alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '否')
					alert_ui_node.SetText(alert_ui_node.m_alert_text, '是否确定将队长转让给成员`{}`？'.format(dude['name']))
					alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
					alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
					self.SetVisible(self.m_leader_panel, False)
					self.SetVisible(self.m_member_panel, False)
					self.SetVisible(self.m_clear_btn, False)
					alert_ui_node.SetVisible("", True)
					alert_ui_node.m_alert = lambda uid=dude['uid']: self.transfer(uid)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def transfer(self, uid):
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.SquadChiefTransferEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'uid': uid}
		)
			
	def on_touch_btn_kick(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			clientApi.SetResponse(True)
			if self.m_dude:
				dude = self.m_dudes[self.m_dude - 1]
				alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
				if dude:
					alert_ui_node.SetText(alert_ui_node.m_title_text, '踢出队伍')
					alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '是')
					alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '否')
					alert_ui_node.SetText(alert_ui_node.m_alert_text, '是否确定将成员`{}`踢出队伍？'.format(dude['name']))
					alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
					alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
					self.SetVisible(self.m_leader_panel, False)
					self.SetVisible(self.m_member_panel, False)
					self.SetVisible(self.m_clear_btn, False)
					alert_ui_node.SetVisible("", True)
					alert_ui_node.m_alert = lambda uid=dude['uid']: self.kick(uid)
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			clientApi.SetResponse(False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			clientApi.SetResponse(True)
			
	def kick(self, uid):
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.KickSquadPlayerEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'uid': uid}
		)
		
	def on_touch_btn_cls(self, args):
		touch_event = args["TouchEvent"]
		touch_pos = args["TouchPosX"], args["TouchPosY"]

		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touch_event == touch_event_enum.TouchUp:
			# 触控在按钮范围内弹起时
			pass
		elif touch_event == touch_event_enum.TouchDown:
			# 按钮按下时
			self.SetVisible(self.m_leader_panel, False)
			self.SetVisible(self.m_member_panel, False)
			self.SetVisible(self.m_clear_btn, False)
		elif touch_event == touch_event_enum.TouchCancel:
			# 触控在按钮范围外弹起时
			pass
		
	def gray(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		offline = data.get('offline')
		if offline and self.m_squad_cache:
			for i, dude in enumerate(self.m_dudes):
				if dude and dude['uid'] == offline:
					dude_btn = self.m_dude_btn.format(i + 1)
					self.SetSprite('{}/default'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
					self.SetSprite('{}/hover'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
					self.SetSprite('{}/pressed'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
					break

	def recover(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		online = data.get('online')
		if online and self.m_squad_cache:
			for i, dude in enumerate(self.m_dudes):
				if dude and dude['uid'] == online:
					dude_btn = self.m_dude_btn.format(i + 1)
					self.SetSprite('{}/default'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
					self.SetSprite('{}/hover'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
					self.SetSprite('{}/pressed'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
					break
					
	def join(self, order):
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.JoinSquadEvent,
			{'playerId': clientApi.GetLocalPlayerId(), 'order': order}
		)
					
	def invite(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
		if uid and uid != self.m_uid:
			self.m_uid = uid
		alert_ui_node.SetText(alert_ui_node.m_title_text, '组队邀请')
		alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '同意')
		alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '拒绝')
		alert_ui_node.SetText(alert_ui_node.m_alert_text, data['msg'])
		alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
		alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
		self.SetVisible(self.m_leader_panel, False)
		self.SetVisible(self.m_member_panel, False)
		self.SetVisible(self.m_clear_btn, False)
		alert_ui_node.SetVisible("", True)
		alert_ui_node.m_alert = lambda order=data['order']: self.join(order)
		
	def assemble(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		alert_ui_node = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
		if uid and uid != self.m_uid:
			self.m_uid = uid
		alert_ui_node.SetText(alert_ui_node.m_title_text, '全体起立')
		alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_confirm_btn), '同意')
		alert_ui_node.SetText('{}/button_label'.format(alert_ui_node.m_cancel_btn), '拒绝')
		alert_ui_node.SetText(alert_ui_node.m_alert_text, data['msg'])
		alert_ui_node.SetVisible(alert_ui_node.m_alert_text, True)
		alert_ui_node.SetVisible(alert_ui_node.m_recruit_panel, False)
		self.SetVisible(self.m_leader_panel, False)
		self.SetVisible(self.m_member_panel, False)
		self.SetVisible(self.m_clear_btn, False)
		alert_ui_node.SetVisible(alert_ui_node.m_alert_board, True)
		alert_ui_node.SetVisible("", True)
		alert_ui_node.m_alert = self.forward
		
	def forward(self):
		clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).NotifyToServer(
			squadConst.ForwardEvent,
			{'playerId': clientApi.GetLocalPlayerId()}
		)
	
	def dispose(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		uid = data.get('uid')
		if uid and uid != self.m_uid:
			self.m_uid = uid
		squad = data.get('squad')
		turn = squad and not self.m_squad_cache
		self.m_squad_cache = squad
		self.SetVisible(self.m_member_panel, False)
		if not squad:
			self.SetVisible(self.m_cls_btn, False)
		else:
			if squad['chief'] != self.m_uid:
				self.SetVisible(self.m_leader_panel, False)
				self.SetVisible(self.m_find_btn, False)
				self.SetVisible(self.m_notice_icon, False)
			else:
				self.SetVisible(self.m_find_btn, True)
			self.m_dudes = [None for i in xrange(5)]
			self.m_dudes[0] = squad['members'][squad['chief']]
			self.SetText(self.m_dude_name_text.format(1), self.m_dudes[0]['name'])
			count = 1
			for member in squad['members'].itervalues():
				if count > 4:
					break
				if member['uid'] != squad['chief']:
					self.m_dudes[count] = member
					count += 1
					self.SetText(self.m_dude_name_text.format(count), member['name'])
			for i in xrange(5):
				dude_btn = self.m_dude_btn.format(i + 1)
				if self.m_dudes[i] and self.m_dudes[i].get('offline'):
					self.SetSprite('{}/default'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
					self.SetSprite('{}/hover'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
					self.SetSprite('{}/pressed'.format(dude_btn), "textures/ui/netease_squad/img01_leave@3x")
				else:
					self.SetSprite('{}/default'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
					self.SetSprite('{}/hover'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
					self.SetSprite('{}/pressed'.format(dude_btn), "textures/ui/netease_squad/img01@3x")
				self.SetVisible(dude_btn, bool(self.m_dudes[i]))
			if turn:
				self.SetVisible(self.m_cls_btn, True)
				
	def notice(self, data):
		if not clientApi.GetSystem(squadConst.ModName, squadConst.ClientSystemName).EnableUI:
			return
		chief = data.get('chief')
		self.SetVisible(self.m_notice_icon, bool(chief and chief == self.m_uid))
	
	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass
		

