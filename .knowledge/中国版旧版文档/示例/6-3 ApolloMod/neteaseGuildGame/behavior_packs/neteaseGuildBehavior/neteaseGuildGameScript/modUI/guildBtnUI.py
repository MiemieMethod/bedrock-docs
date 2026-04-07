# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
import guildConsts as guildConsts

class GuildBtnScreen(ScreenNode):
	"""
	公会的入口按钮
	"""
	def __init__(self,namespace,name,param):
		ScreenNode.__init__(self, namespace, name, param)
		print "===%s===" % "init GuildBtnScreen"
		
		self.mGuildBtnPanel = "/GuildBtnPanel"
		self.mGuildBtn = self.mGuildBtnPanel + "/party_btn"
		
	def ShowPanel(self, isShow):
		self.SetVisible(self.mGuildBtnPanel, isShow)
		
	def Create(self):
		#self.ShowPanel(False)
		self.AddTouchEventHandler(self.mGuildBtn, self.EnterGuild)
		
	def EnterGuild(self, args):
		touchEvent = args["TouchEvent"]
		touch_event_enum = clientApi.GetMinecraftEnum().TouchEvent
		if touchEvent == touch_event_enum.TouchUp:
			guildConsts.GetClientModSystem().GetGuildMgrGac().OnShowGuild()
	
	def InitScreen(self):
		pass