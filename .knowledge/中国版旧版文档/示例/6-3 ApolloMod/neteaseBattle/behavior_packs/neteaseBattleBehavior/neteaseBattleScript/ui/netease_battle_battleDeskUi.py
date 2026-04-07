# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent
import neteaseBattleScript.battleCommon.apiUtil as apiUtil
from neteaseBattleScript.battleCommon.battleConsts import CInterEvent
import neteaseBattleScript.battleCommon.battleConsts as battleConsts

class BattleDeskScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)

	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.AddTouchEventHandler("/main_pnl/gamer_btn", self.OnOpenStatus)
		self.OnEnemyDraw({"guid":None})

	def InitScreen(self):
		self.ChangeScreenVisible(True)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIDeskOpen, self.OnOpen)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIDeskClose, self.OnClose)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIDeskReinit, self.OnDeskReinit)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIDeskHealth, self.OnHealthChange)
		apiUtil.GetClientSystem().RegisterInterEvent(CInterEvent.UIEnemyDraw, self.OnEnemyDraw)
		self.SetVisible("/main_pnl/progressbar_bg", True)
		self.SetVisible("/main_pnl/progressbar_bg/progressbar_img", True)
		self.mProSize = self.GetSize("/main_pnl/progressbar_bg/progressbar_img")
		self.mEnemySize = self.GetSize("/main_pnl/progressbar_enemy/progressbar_enemy_img")
		print "Desk InitScreen", self.mProSize, self.mEnemySize

	def Destroy(self):
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIDeskOpen, self.OnOpen)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIDeskClose, self.OnClose)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIDeskHealth, self.OnHealthChange)
		apiUtil.GetClientSystem().UnRegisterInterEvent(CInterEvent.UIEnemyDraw, self.OnEnemyDraw)

	def OnDeskReinit(self, data):
		if battleConsts.ShowStatusBtnOnDesk:
			self.SetVisible("/main_pnl/gamer_btn", True)
		else:
			self.SetVisible("/main_pnl/gamer_btn", False)

	def OnOpen(self, data):
		self.ChangeScreenVisible(True)

	def OnClose(self, data):
		self.ChangeScreenVisible(False)

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		self.SetVisible("", flag)

	# 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
	def Update(self):
		pass

	def OnHealthChange(self, data):
		# 我方血条
		entity = apiUtil.GetClientSystem().GetObjMgr().GetObject(data["guid"])
		if not entity:
			self.SetVisible("/main_pnl/progressbar_bg", False)
			return
		if entity.propMaxHp <= 0:
			self.SetVisible("/main_pnl/progressbar_bg", False)
			return
		self.SetVisible("/main_pnl/progressbar_bg", True)
		width = self.mProSize[0] * entity.propRecentHp / entity.propMaxHp
		self.SetSize("/main_pnl/progressbar_bg/progressbar_img", (width, self.mProSize[1]))

	def OnEnemyDraw(self, data):
		# 敌方血条
		entity = apiUtil.GetClientSystem().GetObjMgr().GetObject(data["guid"])
		if not entity:
			self.SetVisible("/main_pnl/progressbar_enemy", False)
			return
		if entity.propMaxHp <= 0:
			self.SetVisible("/main_pnl/progressbar_enemy", False)
			return
		self.SetVisible("/main_pnl/progressbar_enemy", True)
		text = "%s/%s" % (entity.propRecentHp, entity.propMaxHp)
		self.SetText("/main_pnl/progressbar_enemy/enemy_name_label", text)
		width = self.mEnemySize[0] * entity.propRecentHp / entity.propMaxHp
		self.SetSize("/main_pnl/progressbar_enemy/progressbar_enemy_img", (width, self.mEnemySize[1]))

	def OnOpenStatus(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			extraClientApi.SetResponse(True)
			apiUtil.GetClientSystem().GetEventMgr().NotifyEvent(CInterEvent.UIStatusOpen, {"guid":apiUtil.GetClientSystem().GetLocalPlayer()})  # 打开玩家面板
		elif event == TouchEvent.TouchDown:
			extraClientApi.SetResponse(False)
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			extraClientApi.SetResponse(True)
