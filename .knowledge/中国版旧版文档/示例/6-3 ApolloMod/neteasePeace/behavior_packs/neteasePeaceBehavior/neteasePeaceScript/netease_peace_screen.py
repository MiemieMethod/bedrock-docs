# -*- coding: utf-8 -*-

import neteasePeaceScript.peaceConst as peaceConst
import client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()

class PeaceScreen(ScreenNode):
	"""
	PVP界面
	"""

	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		print '==== %s ====' % 'init PeaceScreen'

		self.m_peace_panel_path = '/peace_panel'
		self.m_peace_panel_alive = False

		self.m_defeat_bar_path_list = []
		self.m_enemy_bar_path_list =[]

		self.cache = {  # PVP的伤害开关
			'switch': 0,
			'hood': 0,
			'crew': 0,
			'gang': 0
		}
		self.left = 0  # 切换的冷却时间
		self.count = 0  # tick计时

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		print '==== %s ====' % 'PeaceScreen Create'

		# 主面板
		self.m_peace_panel = self.GetBaseUIControl(self.m_peace_panel_path)

		# 关闭按钮
		self.m_close_btn = self.m_peace_panel.GetChildByPath("/img_close_bg/btn_close").asButton()

		# 权限信息按钮
		self.m_authority_btn = self.m_peace_panel.GetChildByPath("/btn_authority").asButton()
		self.m_authority_selected = self.m_authority_btn.GetChildByPath("/img_authority_selected").asImage()

		# 权限信息面板
		self.m_authority_board = self.m_peace_panel.GetChildByPath("/img_authority_board").asImage()

		self.m_mode_btn = self.m_authority_board.GetChildByPath("/btn_mode").asButton()
		self.m_mode_btn_disable = self.m_mode_btn.GetChildByPath("/img_mode_disable").asImage()
		self.m_mode_btn_signal = self.m_mode_btn.GetChildByPath("/img_mode_signal").asImage()
		self.m_mode_btn_text = self.m_mode_btn.GetChildByPath("/lb_mode_text").asLabel()

		self.m_authority_friend = self.m_authority_board.GetChildByPath("/img_authority_friend").asImage()
		self.m_authority_friend_immurity_lb = self.m_authority_friend.GetChildByPath("/lb_friend_immunity").asLabel()
		self.m_authority_friend_immurity_switch = self.m_authority_friend.GetChildByPath("/switch_friend_immunity").asSwitchToggle()

		self.m_authority_teammate = self.m_authority_board.GetChildByPath("/img_authority_teammate").asImage()
		self.m_authority_teammate_immurity_lb = self.m_authority_teammate.GetChildByPath("/lb_teammate_immunity").asLabel()
		self.m_authority_teammate_immurity_switch = self.m_authority_teammate.GetChildByPath("/switch_teammate_immunity").asSwitchToggle()

		self.m_authority_guild_member = self.m_authority_board.GetChildByPath("/img_authority_guild_member").asImage()
		self.m_authority_guild_member_immurity_lb = self.m_authority_guild_member.GetChildByPath("/lb_guild_member_immunity").asLabel()
		self.m_authority_guild_member_immurity_switch = self.m_authority_guild_member.GetChildByPath("/switch_guild_member_immunity").asSwitchToggle()

		# 击败信息按钮
		self.m_defeat_btn = self.m_peace_panel.GetChildByPath("/btn_defeat").asButton()
		self.m_defeat_selected = self.m_defeat_btn.GetChildByPath("/img_defeat_selected").asImage()

		# 击败信息面板
		self.m_defeat_board = self.m_peace_panel.GetChildByPath("/img_defeat_board").asImage()
		self.m_defeat_empty_lb = self.m_defeat_board.GetChildByPath("/lb_defeat_empty").asLabel()
		self.m_defeat_list_scroll = self.m_defeat_board.GetChildByPath("/scroll_defeat_list").asScrollView()
		self.m_defeat_time_lb = self.m_defeat_board.GetChildByPath("/lb_defeat_time").asLabel()
		self.m_defeat_times_lb = self.m_defeat_board.GetChildByPath("/lb_defeat_times").asLabel()
		self.m_defeat_title_lb = self.m_defeat_board.GetChildByPath("/lb_defeat_title").asLabel()
		self.m_defeat_name_lb = self.m_defeat_board.GetChildByPath("/lb_defeat_name").asLabel()
		self.m_defeat_list_path = self.m_defeat_list_scroll.GetScrollViewContentPath()
		self.m_defeat_list_context = self.GetBaseUIControl(self.m_defeat_list_path)

		# 仇敌信息按钮
		self.m_enemy_btn = self.m_peace_panel.GetChildByPath("/btn_enemy").asButton()
		self.m_enemy_selected = self.m_enemy_btn.GetChildByPath("/img_enemy_selected").asImage()

		# 仇敌信息面板
		self.m_enemy_board = self.m_peace_panel.GetChildByPath("/img_enemy_board").asImage()
		self.m_enemy_empty_lb = self.m_enemy_board.GetChildByPath("/lb_enemy_empty").asLabel()
		self.m_enemy_list_scroll = self.m_enemy_board.GetChildByPath("/scroll_enemy_list").asScrollView()
		self.m_enemy_time_lb = self.m_enemy_board.GetChildByPath("/lb_enemy_time").asLabel()
		self.m_enemy_times_lb = self.m_enemy_board.GetChildByPath("/lb_enemy_times").asLabel()
		self.m_enemy_title_lb = self.m_enemy_board.GetChildByPath("/lb_enemy_title").asLabel()
		self.m_enemy_name_lb = self.m_enemy_board.GetChildByPath("/lb_enemy_name").asLabel()
		self.m_enemy_list_path = self.m_enemy_list_scroll.GetScrollViewContentPath()
		self.m_enemy_list_context = self.GetBaseUIControl(self.m_enemy_list_path)

		# 关闭按钮事件
		self.m_close_btn.AddTouchEventParams({"isSwallow": True})
		self.m_close_btn.SetButtonTouchUpCallback(self.on_touch_btn_close)

		# PVP开关按钮事件
		self.m_mode_btn.AddTouchEventParams({"isSwallow": True})
		self.m_mode_btn.SetButtonTouchUpCallback(self.on_touch_btn_mode)

		# 权限按钮事件
		self.m_authority_btn.AddTouchEventParams({"isSwallow": True})
		self.m_authority_btn.SetButtonTouchUpCallback(self.on_touch_btn_authority)

		# 击败按钮事件
		self.m_defeat_btn.AddTouchEventParams({"isSwallow": True})
		self.m_defeat_btn.SetButtonTouchUpCallback(self.on_touch_btn_defeat)

		# 仇敌按钮事件
		self.m_enemy_btn.AddTouchEventParams({"isSwallow": True})
		self.m_enemy_btn.SetButtonTouchUpCallback(self.on_touch_btn_enemy)

		defeat_bar0_path = "{}/img_sroll_bar0".format(self.m_defeat_list_path)
		defeat_bar0 = self.GetBaseUIControl(defeat_bar0_path).asImage()
		self.m_scroll_list_size = self.m_defeat_list_scroll.GetSize()
		self.m_bar_pos = defeat_bar0.GetPosition()
		self.m_bar_offset = defeat_bar0.GetSize()[1]
		self.m_defeat_bar_path_list.append(defeat_bar0_path)
	
		enemy_bar_path0 = "{}/img_sroll_bar0".format(self.m_enemy_list_path)
		# enemy_bar0 = self.GetBaseUIControl(enemy_bar_path0).asImage()
		self.m_enemy_bar_path_list.append(enemy_bar_path0)

	def InitScreen(self):
		print '==== %s ====' % 'PeaceScreen Init'

		self.m_peace_panel.SetVisible(False)
		self.m_peace_panel_alive = False

	def Update(self):
		if self.left > 0:
			self.count += 1
			if not self.count % 30:
				self.count = 0
				self.left -= 1
				self.m_mode_btn_disable.SetVisible(self.left > 0)
				self.m_mode_btn_text.SetText(
					(self.cache['switch'] and '关闭PVP' or '开启PVP') 
					+ ('({}s)'.format(self.left) if self.left > 0 else ''))
		else:
			self.count = 0

	def on_touch_btn_close(self, args):
		self.m_peace_panel.SetVisible(False)
		self.m_peace_panel_alive = False
		self.SetIsHud(1)
		clientApi.HideSlotBarGui(False)

	def on_touch_btn_mode(self, args):
		# PVP开关
		if self.left <= 0:
			# 非正数即客户端可判定为按钮可点击，未进入冷却，可发送请求切换pvp开关
			self.left = self.cd
			self.cache['switch'] = int(not self.cache['switch'])
		data = {'playerId': clientApi.GetLocalPlayerId()}
		data.update(self.cache)
		clientApi.GetSystem(peaceConst.ModName, peaceConst.ClientSystemName).NotifyToServer(
			'PVPSwitchEvent',
			data
		)
		self.m_mode_btn_signal.SetSprite(
			self.cache['switch'] and "textures/ui/netease_peace/tag03" or "textures/ui/netease_peace/tag02")
		self.m_mode_btn_disable.SetVisible(self.left > 0)

		self.m_mode_btn_text.SetText(
			(self.cache['switch'] and '关闭PVP' or '开启PVP') 
			+ ('({}s)'.format(self.left) if self.left > 0 else ''))


	def on_touch_btn_authority(self, args):
		# 权限设置

		self.m_authority_selected.SetVisible(True)
		self.m_defeat_selected.SetVisible(False)
		self.m_enemy_selected.SetVisible(False)

		self.m_authority_board.SetVisible(True)
		self.m_defeat_board.SetVisible(False)
		self.m_enemy_board.SetVisible(False)

		self.m_mode_btn_signal.SetSprite(
			self.cache['switch'] and "textures/ui/netease_peace/tag03" or "textures/ui/netease_peace/tag02")
		self.m_mode_btn_disable.SetVisible(self.left > 0)

		self.m_mode_btn_text.SetText((self.cache['switch'] and '关闭PVP' or '开启PVP') + (
			'({}s)'.format(self.left) if self.left > 0 else ''))

	def on_touch_btn_defeat(self, args):
		# 击败对象列表
		self.m_authority_selected.SetVisible(False)
		self.m_defeat_selected.SetVisible(True)
		self.m_enemy_selected.SetVisible(False)

		self.m_authority_board.SetVisible(False)
		self.m_defeat_board.SetVisible(True)
		self.m_enemy_board.SetVisible(False)

	def on_touch_btn_enemy(self, args):
		# 仇敌列表
		self.m_authority_selected.SetVisible(False)
		self.m_defeat_selected.SetVisible(False)
		self.m_enemy_selected.SetVisible(True)

		self.m_authority_board.SetVisible(False)
		self.m_defeat_board.SetVisible(False)
		self.m_enemy_board.SetVisible(True)

	# 切换好友免疫属性
	@ViewBinder.binding(ViewBinder.BF_ToggleChanged)
	def toggle_friend_immunity(self,args):
		flag = args["state"]
		if self.cache['hood'] != int(flag):
			print '==== %s ====' % 'toggle_friend_immunity'
			self.cache['hood'] = int(flag)
			data = {'playerId': clientApi.GetLocalPlayerId()}
			data.update(self.cache)
			clientApi.GetSystem(peaceConst.ModName, peaceConst.ClientSystemName).NotifyToServer(
							'PVPSwitchEvent',
							data
							)
		self.m_authority_friend_immurity_lb.SetText(self.cache['hood'] and "免疫" or "不免疫")

		return ViewRequest.Refresh

	# 获取好友免疫属性
	@ViewBinder.binding(ViewBinder.BF_BindBool)
	def get_friend_immunity(self):
		return bool(self.cache['hood'])

	# 切换队友免疫属性
	@ViewBinder.binding(ViewBinder.BF_ToggleChanged)
	def toggle_teammate_immunity(self,args):
		flag = args["state"]
		if self.cache['crew'] != int(flag):
			print '==== %s ====' % 'toggle_teammate_immunity'
			self.cache['crew'] = int(flag)
			data = {'playerId': clientApi.GetLocalPlayerId()}
			data.update(self.cache)
			clientApi.GetSystem(peaceConst.ModName, peaceConst.ClientSystemName).NotifyToServer(
							'PVPSwitchEvent',
							data
							)
		self.m_authority_teammate_immurity_lb.SetText(self.cache['crew'] and "免疫" or "不免疫")

		return ViewRequest.Refresh

	# 获取队友免疫属性
	@ViewBinder.binding(ViewBinder.BF_BindBool)
	def get_teammate_immunity(self):
		return bool(self.cache['crew'])

	# 切换公会成员免疫属性
	@ViewBinder.binding(ViewBinder.BF_ToggleChanged)
	def toggle_guild_member_immunity(self,args):
		flag = args["state"]
		if self.cache['gang'] != int(flag):
			print '==== %s ====' % 'toggle_guild_member_immunity'
			self.cache['gang'] = int(flag)
			data = {'playerId': clientApi.GetLocalPlayerId()}
			data.update(self.cache)
			clientApi.GetSystem(peaceConst.ModName, peaceConst.ClientSystemName).NotifyToServer(
							'PVPSwitchEvent',
							data
							)
		self.m_authority_guild_member_immurity_lb.SetText(self.cache['gang'] and "免疫" or "不免疫")

		return ViewRequest.Refresh

	# 获取公会成员免疫属性
	@ViewBinder.binding(ViewBinder.BF_BindBool)
	def get_guild_member_immunity(self):
		return bool(self.cache['gang'])

	def open(self, data):
		"""
		根据服务端下放的数据组成PVP界面
		"""

		self.cache = data['filter']  # 开关相关
		self.left = data['left']  # 剩余的冷却时间，每次服务端推送下来都会计算剩余多少秒能够切换PVP开关
		self.cd = data['cd']  # 切换一次pvp开关的冷却时间，配置于mod.json


		self.m_authority_selected.SetVisible(True)
		self.m_defeat_selected.SetVisible(False)
		self.m_enemy_selected.SetVisible(False)

		self.m_authority_board.SetVisible(True)
		self.m_defeat_board.SetVisible(False)
		self.m_enemy_board.SetVisible(False)

		haters = data['haters']  # 击败对象列表
		self.m_defeat_list_scroll.SetVisible(bool(haters))
		self.m_defeat_time_lb.SetVisible(bool(haters))
		self.m_defeat_times_lb.SetVisible(bool(haters))
		self.m_defeat_name_lb.SetVisible(bool(haters))
		self.m_defeat_empty_lb.SetVisible(not haters)
		if haters:
			demand = len(haters)
			cur = len(self.m_defeat_bar_path_list)
			if demand > cur:
				for i in xrange(cur, demand):
					bar_name = 'img_scorll_bar{}'.format(i)
					self.Clone(self.m_defeat_bar_path_list[0], self.m_defeat_list_path, bar_name)
					bar_path = "{}/{}".format(self.m_defeat_list_path, bar_name)
					bar = self.GetBaseUIControl(bar_path).asImage()
					bar.SetPosition((self.m_bar_pos[0], self.m_bar_pos[1] + self.m_bar_offset * i))
					self.m_defeat_bar_path_list.append(bar_path)
			self.m_defeat_list_context.SetSize((self.m_scroll_list_size[0], self.m_bar_offset * demand + 10))
			for i, bar_path in enumerate(self.m_defeat_bar_path_list):
				bar = self.GetBaseUIControl(bar_path).asImage()
				if i < demand:
					info = haters[i]
					bar.GetChildByPath("/lb_scroll_bar_name").asLabel().SetText(info['uname'])
					bar.GetChildByPath("/lb_scroll_bar_times").asLabel().SetText(str(info['ts']))
					bar.GetChildByPath("/lb_scroll_bar_time").asLabel().SetText(info['t'])
				bar.SetVisible(i < demand)

		fakers = data['fakers']  # 仇敌列表
		self.m_enemy_list_scroll.SetVisible(bool(fakers))
		self.m_enemy_time_lb.SetVisible(bool(fakers))
		self.m_enemy_times_lb.SetVisible(bool(fakers))
		self.m_enemy_name_lb.SetVisible(bool(fakers))
		self.m_enemy_empty_lb.SetVisible(not fakers)
		if fakers:
			demand = len(fakers)
			cur = len(self.m_enemy_bar_path_list)
			if demand > cur:
				for i in xrange(cur, demand):
					bar_name = 'img_scorll_bar{}'.format(i)
					self.Clone(self.m_enemy_bar_path_list[0], self.m_enemy_list_path, bar_name)
					bar_path = "{}/{}".format(self.m_enemy_list_path, bar_name)
					bar = self.GetBaseUIControl(bar_path).asImage()
					bar.SetPosition((self.m_bar_pos[0], self.m_bar_pos[1] + self.m_bar_offset * i))
					self.m_enemy_bar_path_list.append(bar_path)
			self.m_enemy_list_context.SetSize((self.m_scroll_list_size[0], self.m_bar_offset * demand + 10))
			for i, bar_path in enumerate(self.m_enemy_bar_path_list):
				bar = self.GetBaseUIControl(bar_path).asImage()
				if i < demand:
					info = fakers[i]
					bar.GetChildByPath("/lb_scroll_bar_name").asLabel().SetText(info['uname'])
					bar.GetChildByPath("/lb_scroll_bar_times").asLabel().SetText(str(info['ts']))
					bar.GetChildByPath("/lb_scroll_bar_time").asLabel().SetText(info['t'])
				bar.SetVisible(i < demand)

		self.m_authority_friend_immurity_switch.SetToggleState(self.cache['hood'])
		self.m_authority_teammate_immurity_switch.SetToggleState(self.cache['crew'])
		self.m_authority_guild_member_immurity_switch.SetToggleState(self.cache['gang'])

		self.m_mode_btn_signal.SetSprite(
			self.cache['switch'] and "textures/ui/netease_peace/tag03" or "textures/ui/netease_peace/tag02")
		self.m_mode_btn_disable.SetVisible(self.left > 0)

		self.m_mode_btn_text.SetText((self.cache['switch'] and '关闭PVP' or '开启PVP') + (
			'({}s)'.format(self.left) if self.left > 0 else ''))

		self.m_peace_panel.SetVisible(True)
		self.m_peace_panel_alive = True
		self.SetIsHud(0)
		clientApi.HideSlotBarGui(True)
