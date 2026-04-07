# -*- coding: utf-8 -*-
import weakref
import time
import client.extraClientApi as extraClientApi
ViewBinder = extraClientApi.GetViewBinderCls()
ViewRequest = extraClientApi.GetViewViewRequestCls()
ScreenNode = extraClientApi.GetScreenNodeCls()
TouchEvent = extraClientApi.GetMinecraftEnum().TouchEvent

import neteaseRoundScript.roundConst as roundConst
from neteaseRoundScript.ui.uiDef import UIDef

class BattleWinScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIBattleWin
		self.mSystem = None
		self.mShowTimeStamp = None
		self.mLastSec = None

	def ChangeScreenVisible(self, flag):
		self.mBShow = flag
		if flag:
			if self.mSystem:
				self.mSystem.GetUiMgr().RegisterUIOpen(self.mUiKey)
		else:
			if self.mSystem:
				self.mSystem.GetUiMgr().RegisterUIClose(self.mUiKey)
		self.SetVisible("", flag)
	
	def GetIsShow(self):
		return self.mBShow

	def InitScreen(self):
		self.ChangeScreenVisible(False)
	
	def InitSystem(self, system):
		self.mSystem = weakref.proxy(system)

	def Destroy(self):
		pass

	def Update(self):
		if not self.mShowTimeStamp:
			return
		left = max(0, self.mShowTimeStamp + 10 - time.time())
		left = int(left)
		button = "/pnl_result/img_backgroud/btn_continue"
		if self.mLastSec is None or self.mLastSec != left:
			self.mLastSec = left
			if left > 0:
				text = "继续(%d秒)" % left
				self.ChangeButtonText(button, text)
				self.ChangeButtonTextColor(button, (178.0/256, 178.0/256, 178.0/256, 1))
				self.ChangeButtonImage(button, "btn01_unuse", True)
				self.SetTouchEnable(button, False)
			else:
				self.ChangeButtonText(button, "继续")
				self.ChangeButtonTextColor(button, (66.0/256, 66.0/256, 66.0/256, 1))
				self.ChangeButtonImage(button, "btn01", False)
				self.SetTouchEnable(button, True)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def Show(self, itemList):
		self.ChangeScreenVisible(True)
		self.mShowTimeStamp = time.time()
		self.mLastSec = None
		length = len(itemList)
		if length % 2 == 0:
			use = self.mEvenItemMap
			nouse = self.mOddItemMap
		else:
			use = self.mOddItemMap
			nouse = self.mEvenItemMap
		for idx, part in nouse.iteritems():
			self.SetVisible(part, False)
		for idx, part in use.iteritems():
			if idx >= length:
				self.SetVisible(part, False)
				continue
			self.SetVisible(part, True)
			itemDict = itemList[idx]
			itemName, auxValue, count = itemDict["itemName"], itemDict["auxValue"], itemDict["count"]
			self.SetUiItem("%s/item_renderer" % part, itemName, auxValue)
			self.SetText("%s/lb_item_num" % part, "%d" % count)
		self.Update()
	# ----------------------------------------------------------------------------------------------------------------------------------
	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.AddTouchEventHandler("/pnl_result/img_backgroud/btn_close", self.OnButtonCancel)
		self.SetVisible("/pnl_result/img_backgroud/btn_close", False)
		self.AddTouchEventHandler("/pnl_result/img_backgroud/btn_continue", self.OnButtonOk)
		#
		base = "/pnl_result/img_backgroud/img_reward_base"
		baseSize = self.GetSize(base)
		baseSize = (baseSize[0]+2, baseSize[1])
		basePos = self.GetPosition(base)
		parent = "/pnl_result/img_backgroud"
		self.mOddItemMap = {}
		for idx in xrange(5):
			name = "OddItem_%d" % idx
			self.Clone(base, parent, name)
			fullName = "%s/%s" % (parent, name)
			self.mOddItemMap[idx] = fullName
			x, y = basePos
			if idx % 2 == 0:
				x = x + (idx//2)*baseSize[0]
			else:
				x = x - (idx//2)*baseSize[0] - baseSize[0]
			self.SetPosition(fullName, (x, y))
		self.mEvenItemMap = {}
		for idx in xrange(6):
			name = "EvenItem_%d" % idx
			self.Clone(base, parent, name)
			fullName = "%s/%s" % (parent, name)
			self.mEvenItemMap[idx] = fullName
			x, y = basePos
			if idx % 2 == 0:
				x = x - (idx//2)*baseSize[0] - baseSize[0]/2
			else:
				x = x + (idx//2)*baseSize[0] + baseSize[0]/2
			self.SetPosition(fullName, (x, y))
		self.SetVisible(base, False)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def ChangeButtonImage(self, button, image, isSame=True):
		if not image.startswith("textures/ui/"):
			image = "textures/ui/netease_round/%s" % image
		self.SetSprite("%s/default" % button, image)
		if isSame:
			self.SetSprite("%s/hover" % button, image)
			self.SetSprite("%s/pressed" % button, image)
		else:
			self.SetSprite("%s/hover" % button, image+"_hover")
			self.SetSprite("%s/pressed" % button, image+"_click")
	
	def ChangeButtonText(self, button, text):
		self.SetText("%s/button_label" % button, text)
	
	def ChangeButtonTextColor(self, button, color):
		self.SetTextColor("%s/button_label" % button, color)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def OnButtonCancel(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoClose()
			
	def OnButtonOk(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoClose()
	# ---------------------------------------------------------------------------------
	def DoClose(self):
		self.ChangeScreenVisible(False)
		self.mSystem.OnBattleClientFinish()

