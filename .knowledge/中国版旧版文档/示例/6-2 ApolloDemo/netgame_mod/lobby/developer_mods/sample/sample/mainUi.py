# -*- coding: utf-8 -*-
import time

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
# ClientSystem = clientApi.GetClientSystemCls()


class MainUi(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.scoreBoardList = []
		self.ranking_cancel_callback = None
		self.ranking_is_show = False
		self.menu_is_show = False
		self.menu_ok_callback = None
		self.menu_cancel_callback = None
		self.menu_button_ok_down = False
		self.menu_button_cancel_down = False
		
	def initUi(self):
		self.label_medical = "/label_medical"
		self.hide_center_message()
		
		self.ranking_panel = "/ranking_panel"
		self.hide_ranking_panel()
		
		self.hideMenuPanel()
	#-----------------------------------------------------------------------------------------
	def show_center_message(self, message):
		self.SetText(self.label_medical, message)
		self.SetVisible(self.label_medical, True)
	
	def hide_center_message(self):
		self.SetVisible(self.label_medical, False)
	#-------------------------------------------------------------------------------------------	
	def show_ranking_panel(self, callback, title, content):
		self.ranking_cancel_callback = callback
		self.SetVisible(self.ranking_panel, True)
		self.SetText("/ranking_panel/label_ranking_title", title)
		self.ranking_is_show = True
		#
		self.scoreBoardList = []
		for idx, data in enumerate(content):
			nickname, score = data["nickname"], data["score"]
			_string = "第%d名: %s -- %d" % (idx+1, nickname, score)
			self.scoreBoardList.append(_string)
	
	def hide_ranking_panel(self):
		self.SetVisible(self.ranking_panel, False)
		self.ranking_is_show = False
	
	def IsRankingShow(self):
		return self.ranking_is_show
	
	@ViewBinder.binding(ViewBinder.BF_ButtonClick)
	def OnRankingButtonExit(self, args):
		print "OnRankingButtonExit", args
		if args['ButtonState'] == 0:
			self.hide_ranking_panel()
			if self.ranking_cancel_callback:
				self.ranking_cancel_callback()
		return ViewRequest.Refresh
	
	@ViewBinder.binding(ViewBinder.BF_BindInt, "#scoreboard_grid.item_count")
	def OnStarkGridResize(self):
		return len(self.scoreBoardList)

	@ViewBinder.binding_collection(ViewBinder.BF_BindString, "scoreboard_stackgrid", "#label_score_board.text")
	def OnRefreshScoreBoardLabel(self, index):
		return self.scoreBoardList[index] if len(self.scoreBoardList) > index else ""
	#-------------------------------------------------------------------------------------------
	def showMenuPanel(self, callback, cancel_callback, title, txt_go, txt_leave):
		self.menu_ok_callback = callback
		self.menu_cancel_callback = cancel_callback
		self.SetVisible("/menu_panel", True)
		self.SetText("/menu_panel/label_menu_title", title)
		self.SetText("/menu_panel/menu_button_go/button_label", txt_go)
		self.SetText("/menu_panel/menu_button_exit/button_label", txt_leave)
		self.menu_is_show = True
		
	def hideMenuPanel(self):
		self.SetVisible("/menu_panel", False)
		self.menu_is_show = False
	
	def IsMenuShow(self):
		return self.menu_is_show
	
	@ViewBinder.binding(ViewBinder.BF_ButtonClick)
	def OnMenuButtonGo(self, args):
		print "OnMenuButtonGo", args
		if self.menu_button_ok_down:
			if args['ButtonState'] == 0:
				self.hideMenuPanel()
				if self.menu_ok_callback:
					self.menu_ok_callback()
		else:
			if args['ButtonState'] == 1:
				self.menu_button_ok_down = True
		return ViewRequest.Refresh
	
	@ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name='OnMenuButtonGo')
	def OnMenuButtonGoCancel(self, args):
		print "OnMenuButtonGo Cancel", args
		return ViewRequest.Refresh
	
	@ViewBinder.binding(ViewBinder.BF_ButtonClick)
	def OnMenuButtonExit(self, args):
		print "OnMenuButtonExit", args
		if self.menu_button_cancel_down:
			if args['ButtonState'] == 0:
				self.hideMenuPanel()
				if self.menu_cancel_callback:
					self.menu_cancel_callback()
		else:
			if args['ButtonState'] == 1:
				self.menu_button_cancel_down = True
		return ViewRequest.Refresh
		
	@ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name='OnMenuButtonExit')
	def OnMenuButtonExitCancel(self, args):
		print "OnMenuButtonExit Cancel", args
		return ViewRequest.Refresh
	#-------------------------------------------------------------------------------------------
	
	

	