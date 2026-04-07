# -*- coding: utf-8 -*-
import random
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseFriendScript.apiUtil as apiUtil
from neteaseFriendScript.ui.uiDef import UIDef

class FriendConfirmPopScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIFriendConfirmPop
		self.mOkCb = None
		self.mCancelCb = None

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	def Destroy(self):
		pass

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.AddTouchEventHandler("/main_pnl/img_base/btn_cancel", self.OnButtonCancel)
		self.AddTouchEventHandler("/main_pnl/img_base/btn_ok", self.OnButtonOk)
	# ---------------------------------------------------------------------------------
	def ShowConfirmPop(self, title, desc, okCallback=None, cancelCallback=None):
		self.ChangeScreenVisible(True)
		self.SetText("/main_pnl/img_base/lb_title", title)
		self.SetText("/main_pnl/img_base/lb_hint", desc)
		self.mOkCb = okCallback
		self.mCancelCb = cancelCallback
	# ---------------------------------------------------------------------------------
	def OnButtonCancel(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoCancel()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass

	def OnButtonOk(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoOk()
		elif event == TouchEvent.TouchDown:
			pass
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			pass
	# ---------------------------------------------------------------------------------
	def DoCancel(self):
		self.ChangeScreenVisible(False)
		callback = self.mCancelCb
		self.mCancelCb = None
		if callback:
			callback()

	def DoOk(self):
		self.ChangeScreenVisible(False)
		callback = self.mOkCb
		self.mOkCb = None
		if callback:
			callback()
