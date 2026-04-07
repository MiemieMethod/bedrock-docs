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

class HeadScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mIsShowNickname = True
	
	def InitScreen(self):
		self.SetVisible("", False)
		self.SetLayer("", 0)
		
	def Destroy(self):
		pass
	# ----------------------------------------------------------------------------------------------------------------------------------
	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		self.mProtoSize = self.GetSize("/main_pnl/img_hp_base/img_hp_recent")
		self.mNameBgSize = self.GetSize("/main_pnl/img_name_bg")

	def ChangeNicknameShow(self, flag):
		self.SetVisible("", True)
		self.mIsShowNickname = flag
		self.SetVisible("/main_pnl/img_name_bg", self.mIsShowNickname)
	
	def InitOnGameStart(self, nickname, isFriend):
		self.SetText("/main_pnl/img_name_bg/lb_name", nickname)
		length = len(nickname)
		print "InitOnGameStart", length
		self.SetSize("/main_pnl/img_name_bg", (self.mNameBgSize[0]*length/16, self.mNameBgSize[1]))
		if isFriend:
			self.SetSprite("/main_pnl/img_hp_base/img_hp_recent", "textures/ui/netease_round/progressbar01_01")
			self.SetSprite("/main_pnl/img_hp_base", "textures/ui/netease_round/progressbar01_bg")
		else:
			self.SetSprite("/main_pnl/img_hp_base/img_hp_recent", "textures/ui/netease_round/progressbar02_02")
			self.SetSprite("/main_pnl/img_hp_base", "textures/ui/netease_round/progressbar02_bg")
	
	def UpdateByMonster(self, monster):
		self.DrawHealth(monster.mHitPoint, monster.health)
		effectList = monster.GetAllEffects()
		for i in xrange(5):
			if i >= len(effectList):
				self.DrawSingleEffect(i, "")
				continue
			effect = effectList[i]
			self.DrawSingleEffect(i, effect.GetImage())
	# ----------------------------------------------------------------------------------------------------------------------------------
	def DrawSingleEffect(self, index, image):
		if not image:
			self.SetVisible("/main_pnl/img_effect_%d" % index, False)
			return
		self.SetVisible("/main_pnl/img_effect_%d" % index, True)
		if not image.startswith("textures/"):
			image = "textures/ui/netease_round/%s" % image
		self.SetSprite("/main_pnl/img_effect_%d" % index, image)
	
	def DrawHealth(self, hp, maxhp):
		if hp <= 0:
			self.SetVisible("/main_pnl/img_hp_base/img_hp_recent", False)
		else:
			self.SetVisible("/main_pnl/img_hp_base/img_hp_recent", True)
			width = self.mProtoSize[0] * hp / maxhp
			width = max(1, width)
			size = (width, self.mProtoSize[1])
			self.SetSize("/main_pnl/img_hp_base/img_hp_recent", size)

