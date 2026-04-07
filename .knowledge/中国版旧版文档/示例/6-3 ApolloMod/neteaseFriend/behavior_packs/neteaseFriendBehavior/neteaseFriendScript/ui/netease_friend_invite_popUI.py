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

class FriendInvitePopScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIFriendInvitePop
		self.mTextInput = ""
		self.mWordLimit = 10
		self.mOkCb = None
		self.mCancelCb = None

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			apiUtil.GetClientModSystem().GetUiMgr().RegisterUIClose(self.mUiKey)
			self.SetInputEnable(False)
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
	def ShowInvitePop(self, name, friendName, okCallback=None, cancelCallback=None):
		self.ChangeScreenVisible(True)
		self.SetText("/main_pnl/img_base/lb_title", "向【%s】发送好友申请" % friendName)
		text = "申请附言（限%d个字以内）" % self.mWordLimit
		self.SetText("/main_pnl/img_base/lb_hint", text)
		self.mTextInput = ""
		self.mOkCb = okCallback
		self.mCancelCb = cancelCallback

	@ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
	def message_text_box(self, args):
		text = self.GetEditText("/main_pnl/img_base/pnl_input/search_text_box")
		if not text:
			text = ""
		self.mTextInput = text.strip()
		return ViewRequest.Refresh
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
		length = apiUtil.GetUnicodeLength(self.mTextInput)
		if length > self.mWordLimit:
			text = "申请附言不能超过%d个字！" % self.mWordLimit
			self.SetText("/main_pnl/img_base/lb_hint", text)
			return
		if not apiUtil.IsWordValidClient(self.mTextInput):
			text = "申请附言中含有敏感词！"
			self.SetText("/main_pnl/img_base/lb_hint", text)
			return
		self.ChangeScreenVisible(False)
		callback = self.mOkCb
		self.mOkCb = None
		if callback:
			callback(self.mTextInput)
