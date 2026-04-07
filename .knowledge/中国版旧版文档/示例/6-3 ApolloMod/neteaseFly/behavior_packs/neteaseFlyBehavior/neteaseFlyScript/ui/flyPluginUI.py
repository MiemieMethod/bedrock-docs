# -*- coding: utf-8 -*-
import time

import client.extraClientApi as clientApi
import neteaseFlyScript.apiUtil as apiUtil
import neteaseFlyScript.flyClientConsts as flyConsts


ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class FlyPluginUIScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mChangeFlyStateButtonPath = "/changeFlyStateBtn"
		self.mTipsPanelPath = "/tipsPanel"
		# True：开启飞行 False：关闭飞行
		self.mFlyState = False
		# True：允许飞行 False：禁止飞行
		self.mFlyEnable = True
		self.mFrame = 0
		self.mStartTimestamp = 0
		# 提示框透明度
		self.mTipsAlpha = 0.0

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		pass

	def InitScreen(self):
		self.RegisterButtonEvent()

	def RegisterButtonEvent(self):
		self.AddTouchEventHandler(self.mChangeFlyStateButtonPath, self.OnChangeFlyStateButtonClick, {"isSwallow": True})

	def SyncConfig(self, config):
		self.ChangeFlyState(config.get("flyState", False))
		self.ChangeFlyEnable(config.get("flyEnable", True))

	def OnChangeFlyStateButtonClick(self, args):
		touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
		touchEvent = args["TouchEvent"]
		if touchEvent == touchEventEnum.TouchUp:
			data = {
				"playerId": clientApi.GetLocalPlayerId(),
				"state": not self.mFlyState
			}
			apiUtil.GetClientModSystem().NotifyToServer(flyConsts.ChangeFlyStateEvent, data)

	def ChangeFlyState(self, state):
		self.mFlyState = state
		if self.mFlyState:
			self.SetText(self.mChangeFlyStateButtonPath + "/default/label", "关闭飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/hover/label", "关闭飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/locked/label", "关闭飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/pressed/label", "关闭飞行")
		else:
			self.SetText(self.mChangeFlyStateButtonPath + "/default/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/hover/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/locked/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/pressed/label", "开启飞行")

	def ShowTips(self, msg):
		self.SetVisible(self.mTipsPanelPath, True)
		self.SetText(self.mTipsPanelPath + "/tipsText", msg)
		self.mTipsAlpha = 3.0

	def ChangeFlyEnable(self, enabled):
		self.mFlyEnable = enabled
		self.SetTouchEnable(self.mChangeFlyStateButtonPath, enabled)
		if not enabled:
			self.SetText(self.mChangeFlyStateButtonPath + "/default/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/hover/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/locked/label", "开启飞行")
			self.SetText(self.mChangeFlyStateButtonPath + "/pressed/label", "开启飞行")

	def Destroy(self):
		pass

	@ViewBinder.binding(ViewBinder.BF_BindFloat, "#tipsAlpha")
	def OnDetailShow(self):
		if self.mTipsAlpha > 1:
			return 1.0
		return self.mTipsAlpha

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		if self.mTipsAlpha > 0:
			self.mTipsAlpha -= 0.04