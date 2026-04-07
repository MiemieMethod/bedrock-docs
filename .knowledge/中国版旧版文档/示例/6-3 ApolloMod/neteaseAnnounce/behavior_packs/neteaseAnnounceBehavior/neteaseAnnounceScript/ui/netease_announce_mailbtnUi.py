# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseAnnounceScript.apiUtil as apiUtil
import neteaseAnnounceScript.announceConsts as announceConsts

class MailBtnScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.AddTouchEventHandler("/main_pnl/btn_mail", self.OnOpenMailMain)

	def InitScreen(self):
		self.ChangeScreenVisible(False)

	def ReInit(self):
		if announceConsts.MailShowButtonOnDesk:
			self.ChangeScreenVisible(True)
		else:
			self.ChangeScreenVisible(False)

	def OnMailMainClose(self):
		if announceConsts.MailShowButtonOnDesk:
			self.ChangeScreenVisible(True)

	def Destroy(self):
		pass

	def Show(self):
		self.ChangeScreenVisible(True)

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		self.SetVisible("", flag)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	def OnOpenMailMain(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			apiUtil.GetClientModSystem().ShowMailMain()
			self.ChangeScreenVisible(False)
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)
