# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from mod_log import engine_logger as logger
from functools import wraps

def touch_filter(touchType):
	def touchFilter(func):
		@wraps(func)
		def decorated(*args, **kwargs):
			touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
			touchEvent = args[1]["TouchEvent"]
			if touchType == "up":
				if touchEvent == touchEventEnum.TouchUp:
					value = func(*args, **kwargs)
					return value
			if touchType == "down":
				if touchEvent == touchEventEnum.TouchDown:
					value = func(*args, **kwargs)
					return value
			if touchType == "cancel":
				if touchEvent == touchEventEnum.TouchCancel:
					value = func(*args, **kwargs)
					return value
			if touchType == "move":
				if touchEvent == touchEventEnum.TouchMove:
					value = func(*args, **kwargs)
					return value
		return decorated
	return touchFilter


class MainScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		#PopScreen按钮
		self.mCloseBtnPath = "/mainPanel/closeBtn"
		#PushScreen按钮
		self.mPushBtnPath = "/mainPanel/pushBtn"
		self.gridExplain = "/mainPanel/gridExplain"

		print("===== MainScreen __init__ =====")

	def Create(self):
		self.AddTouchEventHandler(self.mCloseBtnPath, self.OnCloseBtnClick, {"isSwallow": True})
		self.AddTouchEventHandler(self.mPushBtnPath, self.PushScreenBtnClick, {"isSwallow": True})
		print("===== MainScreen Create =====")
		
	@touch_filter('up')
	def OnCloseBtnClick(self, args):
		clientApi.PopScreen()
	
	@touch_filter('up')
	def PushScreenBtnClick(self, args):
		from uidemoScripts.modCommon import modConfig
		clientApi.RegisterUI(modConfig.ModName, modConfig.PushScreenDemoUIName, modConfig.PushScreenPyClsPath, modConfig.PushScreenScreenDef)
		clientApi.PushScreen(modConfig.ModName, modConfig.PushScreenDemoUIName)

        
	def Destroy(self):
		print("===== MainScreen Destroy =====")