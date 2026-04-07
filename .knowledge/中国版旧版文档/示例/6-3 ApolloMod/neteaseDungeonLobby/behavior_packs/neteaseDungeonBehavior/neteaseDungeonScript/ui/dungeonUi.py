# -*- coding: utf-8 -*-
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
import neteaseDungeonScript.apiUtil as apiUtil

class DungeonFullMsgScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)

	def ChangeScreenVisible(self, flag):
		if flag:
			extraClientApi.SetInputMode(1)
		else:
			extraClientApi.SetInputMode(0)
		self.SetVisible("", flag)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		pass
		
	def InitScreen(self):
		self.AddTouchEventHandler("/dungeon_pnl/tips_img/confirm_btn", self.OnClose)
		self.AddTouchEventHandler("/dungeon_pnl/tips_img/close_btn", self.OnClose)
		self.ChangeScreenVisible(False)

	def Show(self, dungeonName):
		print 'Show DungeonFullMsgScreen.dungeon name:', dungeonName
		msg = '“%s”副本已经爆满，请稍后再尝试进入。' % dungeonName
		self.SetText('/dungeon_pnl/tips_img/tips_text_lbl', msg)
		self.ChangeScreenVisible(True)

	def OnClose(self, data):
		print 'OnClose'
		self.ChangeScreenVisible(False)

	def Destroy(self):
		pass