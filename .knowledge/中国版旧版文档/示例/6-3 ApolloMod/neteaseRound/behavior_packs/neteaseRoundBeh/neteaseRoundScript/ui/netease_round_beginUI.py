# -*- coding: utf-8 -*-
import weakref
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent
from neteaseRoundScript.ui.uiDef import UIDef

class BattleStartScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIBattleStart
		self.mSystem = None
		self.mTimer = None
		self.mFrame = 0

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			if self.mSystem:
				self.mSystem.GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			if self.mSystem:
				self.mSystem.GetUiMgr().RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)

	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def InitSystem(self, system):
		self.mSystem = weakref.proxy(system)

	def Destroy(self):
		pass

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.mReady = "/pnl_begin/img_mask_begin/lb_ready"
		self.mCountdown = "/pnl_begin/img_mask_begin/lb_time"
		self.mStart = "/pnl_begin/img_mask_begin/lb_start"
	
	def Show(self):
		self.ChangeScreenVisible(True)
		if not self.mTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			self.mTimer = comp.AddRepeatedTimer(1.0, self.OnTick)
		self.mFrame = 0
		self.SetVisible(self.mReady, True)
		self.SetVisible(self.mCountdown, False)
		self.SetVisible(self.mStart, False)
	
	def OnTick(self):
		self.mFrame += 1
		if self.mFrame == 2:
			self.SetVisible(self.mReady, False)
			self.SetVisible(self.mCountdown, True)
			self.SetText(self.mCountdown, "5")
			self.SetVisible(self.mStart, False)
		elif self.mFrame >= 3 and self.mFrame < 7:
			num = 7 - self.mFrame
			self.SetText(self.mCountdown, "%d" % num)
		elif self.mFrame == 7:
			self.SetVisible(self.mReady, False)
			self.SetVisible(self.mCountdown, False)
			self.SetVisible(self.mStart, True)
		elif self.mFrame >= 9:
			self.Hide()

	def Hide(self):
		self.ChangeScreenVisible(False)
		if self.mTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			comp.CancelTimer(self.mTimer)
			self.mTimer = None
		self.mSystem.OnBattleStartSuccess()
		
		
