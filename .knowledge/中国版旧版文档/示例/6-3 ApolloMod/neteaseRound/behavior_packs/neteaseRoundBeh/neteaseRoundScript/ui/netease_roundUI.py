# -*- coding: utf-8 -*-
import weakref
import time

import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
TouchEvent = clientApi.GetMinecraftEnum().TouchEvent

import neteaseRoundScript.roundConst as roundConst
from neteaseRoundScript.ui.uiDef import UIDef

class BattleControlScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.mUiKey = UIDef.UIBattleControl
		self.mSystem = None
		self.mIsShowNickname = True
		self.mCanUseSkill = False
		self.mControlMob = None
		self.mPropSkillIndex = None
		self.mPropSkillTargetIds = []
		self.mAlreadySendSkill = False
		self.mThisRoundMobs = []
		self.mNextRoundMobs = []
	
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
	# ----------------------------------------------------------------------------------------------------------------------------------
	def Update(self):
		if not self.mSkillButtonDownInfo:
			return
		if self.mSkillButtonDownInfo["alreadyShow"]:
			return
		if time.time() - self.mSkillButtonDownInfo["startTp"] >= 0.25:
			self.mSkillButtonDownInfo["alreadyShow"] = True
			self.DoShowSkillTips(self.mSkillButtonDownInfo["idx"])

	def DoShowSkillTips(self, idx):
		if not self.mControlMob:
			return
		skill = self.mControlMob.GetSkillByIndex(idx)
		if not skill:
			return
		self.SetVisible("/main_pnl/pnl_skill_tips", True)
		self.SetText("/main_pnl/pnl_skill_tips/pnl_skill_detail/lb_skill_name", skill.GetName())
		self.SetText("/main_pnl/pnl_skill_tips/pnl_skill_detail/img_en_icon/lb_en_cost", "%d" % skill.mCostEnergy)
		self.SetText("/main_pnl/pnl_skill_tips/pnl_skill_detail/lb_skill_desp", skill.GetDesc())

	def DoHideSkillTips(self):
		self.mSkillButtonDownInfo = None
		self.SetVisible("/main_pnl/pnl_skill_tips", False)
	
	def SendUseSkill(self, idx, mobIds):
		eventData = {
			"playerId": clientApi.GetLocalPlayerId(),
			"skillIndex": idx,
			"skillTargets": mobIds,
		}
		self.mSystem.NotifyToServer(roundConst.BattleClientEvent.ActionSkillSelect, eventData)
		self.mAlreadySendSkill = True
		self.DoShowSkillPerform("技能已经选择完毕，等待服务端回应")
		self.DrawControl()
		print "SendUseSkill", eventData

	def TrySkillTarget(self, mobId):
		if mobId not in self.mPropSkillTargetIds:
			return
		self.SendUseSkill(self.mPropSkillIndex, [mobId,])
	
	def TryUseSkill(self, idx):
		print "TryUseSkill idx={}".format(idx)
		if not self.mCanUseSkill:
			return
		if not self.mControlMob:
			return
		skill = self.mControlMob.GetSkillByIndex(idx)
		if not skill:
			return
		if self.mAlreadySendSkill:
			print "TryUseSkill fail. mAlreadySendSkill is True"
			return
		if skill.mCostEnergy > self.mControlMob.mEnergyPoint:
			print "TryUseSkill fail. not enough energy"
			return
		friendList, enemyList = self.mBattle.GetTargetAble()
		autoTarget, propList = skill.GetPossibleTarget(friendList, enemyList)
		if not propList:
			print "TryUseSkill fail. prop target list is empty"
			return
		propMobIds = []
		for mob in propList:
			propMobIds.append(mob.mId)
		if autoTarget:
			self.SendUseSkill(idx, propMobIds)
			return
		self.DoHideMobTips()
		# 可选技能对象用场景表现
		self.EnterSkillSelect(idx, propMobIds)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def Show(self, battle):
		self.mBattle = weakref.proxy(battle)
		self.ChangeScreenVisible(True)
		self.ChangeNicknameShow(self.mIsShowNickname)
		self.DoHideMobTips()
		self.DoHideSkillTips()
		self.HideNotice()
		self.HideControl()
	
	def RegisterBattleScene(self, scene):
		self.mBattleScene = weakref.proxy(scene)
	
	def Close(self):
		self.mBattle = None
		self.ChangeScreenVisible(False)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def ChangeButtonImage(self, button, image):
		if not image.startswith("textures/ui/"):
			image = "textures/ui/netease_round/%s" % image
		self.SetSprite("%s/default" % button, image)
		self.SetSprite("%s/hover" % button, image)
		self.SetSprite("%s/pressed" % button, image)
	
	def ChangeButtonText(self, button, text):
		self.SetText("%s/button_label" % button, text)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def ChangeNicknameShow(self, isShow=None):
		if isShow is None:
			self.mIsShowNickname = not self.mIsShowNickname
		else:
			self.mIsShowNickname = isShow
		if self.mIsShowNickname:
			self.ChangeButtonImage("/main_pnl/img_time_line/btn_show_nickname", "icon_block_05")
		else:
			self.ChangeButtonImage("/main_pnl/img_time_line/btn_show_nickname", "icon_block_05_active")
		self.mBattleScene.UpdateNicknameShow()

	def ChangeTimelineSize(self, thisRoundSize, nextRoundLength):
		if thisRoundSize < 1:
			thisRoundSize = 1
		if thisRoundSize > 10:
			thisRoundSize = 10
		nextRoundSize = 11 - thisRoundSize
		realNextRoundSize = min(nextRoundLength, nextRoundSize)
		basePos, baseOffset = self.mTimelineData["basePos"], self.mTimelineData["offset"]
		leakThisRoundSize = (nextRoundSize - realNextRoundSize) * baseOffset
		for idx in xrange(1, 10):
			part = self.mMobOrderDict[idx]
			if idx >= thisRoundSize:
				self.SetVisible(part, False)
			else:
				self.SetVisible(part, True)
			self.SetPosition(part, (basePos[0], basePos[1]-idx*baseOffset+baseOffset-leakThisRoundSize))
		self.SetPosition(self.mActiveMob, (self.mTimelineData["activePos"][0], self.mTimelineData["activePos"][1]-leakThisRoundSize))
		parent, parentSize = self.mTimelineData["parent"], self.mTimelineData["parentSize"]
		self.SetSize(parent, (parentSize[0], parentSize[1]-leakThisRoundSize))
		#
		width, height = self.mTimelineData["bgSize"]
		bgName, offset = self.mTimelineData["bgName"], self.mTimelineData["offset"]
		self.SetSize(bgName, (width, height+offset*realNextRoundSize))
		#
		lbX, lbY = self.mTimelineData["lbPos"]
		lbWidth, lbHeight = self.mTimelineData["lbPos"]
		baseX, baseY = self.mTimelineData["basePos"]
		lbName = self.mTimelineData["lbName"]
		self.SetPosition(lbName, (lbX, lbY+offset*realNextRoundSize+2))
		nextRoundLength = min(nextRoundLength, realNextRoundSize)
		for idx in xrange(10):
			part = self.mMobNextOrderDict[idx]
			y = lbY + offset*realNextRoundSize - lbHeight - 7 - offset*idx
			self.SetPosition(part, (baseX, y))
			if idx >= nextRoundLength:
				self.SetVisible(part, False)
			else:
				self.SetVisible(part, True)
	
	def DoShowMobTips(self, mob):
		self.SetVisible("/main_pnl/pnl_mob_tips", True)
		headRect, headIcon, mobName = self.mMobTipsData["headRect"], self.mMobTipsData["headIcon"], self.mMobTipsData["mobName"]
		image = self.GetMobSelectImage(mob)
		self.SetSprite(headRect, image)
		image = mob.GetHeadImage()
		self.SetSprite(headIcon, image)
		hp = max(0, mob.mHitPoint)
		text = "%s(%d/%d)" % (mob.GetNickName(), hp, mob.health)
		self.SetText(mobName, text)
		#
		partList = self.mMobTipsData["effectList"]
		effectList = mob.GetAllEffects()
		for idx, part in enumerate(partList):
			if idx >= len(effectList):
				self.SetVisible(part, False)
				continue
			self.SetVisible(part, True)
			effect = effectList[idx]
			self.SetText("%s/lb_effect_name" % part, effect.GetName())
			self.SetText("%s/lb_effect_desc" % part, effect.GetDesc())
			self.SetSprite("%s/img_effect_icon" % part, effect.GetImage())

	def DoHideMobTips(self):
		self.SetVisible("/main_pnl/pnl_mob_tips", False)
		self.SetVisible("%s/img_active_select" % self.mActiveMob, False)
		for part in self.mMobOrderDict.itervalues():
			self.SetVisible("%s/img_mob_select" % part, False)
		for part in self.mMobNextOrderDict.itervalues():
			self.SetVisible("%s/img_mob_select" % part, False)
	
	def DoShowSkillPerform(self, text):
		print "DoShowSkillPerform", text
	# ----------------------------------------------------------------------------------------------------------------------------------
	def OnShowMobTips(self, isNextRound, idx):
		print "OnShowMobTips isNextRound={} idx={}".format(isNextRound, idx)
		if isNextRound:
			mob = self.mNextRoundMobs[idx]
		else:
			mob = self.mThisRoundMobs[idx]
		# 使用技能状态，暂时处理
		if (not isNextRound) and (idx == 0):
			self.SetVisible("%s/img_active_select" % self.mActiveMob, True)
		else:
			self.SetVisible("%s/img_active_select" % self.mActiveMob, False)
		for partIdx, part in self.mMobOrderDict.iteritems():
			if (not isNextRound) and (idx == partIdx):
				self.SetVisible("%s/img_mob_select" % part, True)
			else:
				self.SetVisible("%s/img_mob_select" % part, False)
		for partIdx, part in self.mMobNextOrderDict.iteritems():
			if isNextRound and (idx == partIdx):
				self.SetVisible("%s/img_mob_select" % part, True)
			else:
				self.SetVisible("%s/img_mob_select" % part, False)
		self.DoShowMobTips(mob)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def DrawTimeline(self):
		thisRoundMobs = self.mBattle.GetThisRoundMobs()
		if not thisRoundMobs:
			return
		# 正在行动的角色
		activeMob = thisRoundMobs[0]
		image = self.GetMobSelectImage(activeMob)
		self.ChangeButtonImage(self.mActiveMob, image)
		image = activeMob.GetHeadImage()
		self.SetSprite("%s/img_active_head_icon" % self.mActiveMob, image)
		# 当前回合等待行动角色
		for idx, mob in enumerate(thisRoundMobs):
			if idx == 0:
				continue
			part = self.mMobOrderDict[idx]
			image = self.GetMobSelectImage(mob)
			self.ChangeButtonImage(part, image)
			image = mob.GetHeadImage()
			self.SetSprite("%s/img_mob_head" % part, image)
		# 下个回合行动角色
		nextRoundMobs = self.mBattle.GetNextRoundMobs()
		for idx, mob in enumerate(nextRoundMobs):
			part = self.mMobNextOrderDict[idx]
			image = self.GetMobSelectImage(mob)
			self.ChangeButtonImage(part, image)
			image = mob.GetHeadImage()
			self.SetSprite("%s/img_mob_head" % part, image)
		# 调整角色显示位置
		self.ChangeTimelineSize(len(thisRoundMobs), len(nextRoundMobs))
		self.mThisRoundMobs = thisRoundMobs
		self.mNextRoundMobs = nextRoundMobs

	def DrawNotice(self, leftTxt, rightTxt, centerTxt):
		self.SetVisible("/main_pnl/img_notice", True)
		if leftTxt:
			self.SetVisible("/main_pnl/img_notice/lb_notice_left", True)
			self.SetText("/main_pnl/img_notice/lb_notice_left", leftTxt)
		else:
			self.SetVisible("/main_pnl/img_notice/lb_notice_left", False)
		if rightTxt:
			self.SetVisible("/main_pnl/img_notice/lb_notice_right", True)
			self.SetText("/main_pnl/img_notice/lb_notice_right", rightTxt)
		else:
			self.SetVisible("/main_pnl/img_notice/lb_notice_right", False)
		if centerTxt:
			self.SetVisible("/main_pnl/img_notice/lb_center", True)
			self.SetText("/main_pnl/img_notice/lb_center", centerTxt)
		else:
			self.SetVisible("/main_pnl/img_notice/lb_center", False)
	
	def HideNotice(self):
		self.SetVisible("/main_pnl/img_notice", False)
	
	def EnterSkillSelect(self, selectIdx, mobIds):
		self.mPropSkillIndex = selectIdx
		self.mPropSkillTargetIds = mobIds
		for idx in xrange(4):
			part = "/main_pnl/pnl_control/btn_use_skill_%d" % idx
			if idx == selectIdx:
				self.SetVisible("%s/img_skill_select_%d" % (part, idx), True)
			else:
				self.SetVisible("%s/img_skill_select_%d" % (part, idx), False)
		self.mBattleScene.EnterSkillSelect(mobIds)
	
	def LeaveSkillSelect(self):
		self.mPropSkillIndex = None
		self.mPropSkillTargetIds = []
		for idx in xrange(4):
			part = "/main_pnl/pnl_control/btn_use_skill_%d" % idx
			self.SetVisible("%s/img_skill_select_%d" % (part, idx), False)
		self.mBattleScene.LeaveSkillSelect()

	def ChangeSkillButtonAlpha(self, part, idx, alpha):
		self.SetAlpha("%s/default" % part, alpha)
		self.SetAlpha("%s/hover" % part, alpha)
		self.SetAlpha("%s/pressed" % part, alpha)
		self.SetAlpha("%s/img_skill_icon_%d" % (part, idx), alpha)
		self.SetAlpha("%s/img_skill_en_bg_%d" % (part, idx), alpha)
		self.SetAlpha("%s/img_skill_en_bg_%d/img_skill_en_icon_%d" % (part, idx, idx), alpha)
		self.SetAlpha("%s/img_skill_en_bg_%d/lb_skill_en_cost_%d" % (part, idx, idx), alpha)

	def DrawControl(self, onActionStart=False):
		mob, isActive = self.mBattle.FindNextControlMob()
		if not mob:
			self.HideControl()
			return
		self.SetVisible("/main_pnl/pnl_control", True)
		self.mCanUseSkill = isActive
		self.mControlMob = mob
		if isActive and onActionStart:
			self.mAlreadySendSkill = False
		self.LeaveSkillSelect()
		self.DrawCountdownVisible()
		image = mob.GetHeadImage()
		self.SetSprite("/main_pnl/pnl_control/img_control_head/img_control_head_icon", image)
		# 技能按钮
		for idx in xrange(4):
			part = "/main_pnl/pnl_control/btn_use_skill_%d" % idx
			skill = mob.GetSkillByIndex(idx)
			if not skill:
				self.SetVisible(part, False)
				continue
			self.SetVisible(part, True)
			self.SetText("%s/img_skill_en_bg_%d/lb_skill_en_cost_%d" % (part, idx, idx), "%d" % skill.mCostEnergy)
			if mob.mEnergyPoint >= skill.mCostEnergy:
				image = skill.GetImage()
				self.SetSprite("%s/img_skill_en_bg_%d/img_skill_en_icon_%d" % (part, idx, idx), "textures/ui/netease_round/img_fire_01")
				self.SetTextColor("%s/img_skill_en_bg_%d/lb_skill_en_cost_%d" % (part, idx, idx), (1,1,1,1))
			else:
				image = skill.GetDisableImage()
				self.SetSprite("%s/img_skill_en_bg_%d/img_skill_en_icon_%d" % (part, idx, idx), "textures/ui/netease_round/img_fire_02")
				self.SetTextColor("%s/img_skill_en_bg_%d/lb_skill_en_cost_%d" % (part, idx, idx), (1,0,0,1))
			self.SetSprite("%s/img_skill_icon_%d" % (part, idx), image)
			self.SetVisible("%s/img_skill_select_%d" % (part, idx), False)
			if isActive and onActionStart:
				self.ChangeSkillButtonAlpha(part, idx, 1.0)
			else:
				self.ChangeSkillButtonAlpha(part, idx, 0.5)
		# 生命值
		fullName, size = self.mHpBarData["name"], self.mHpBarData["size"]
		maxHp, recentHp = mob.health, mob.mHitPoint
		if recentHp <= 0:
			recentHp = 0
			self.SetVisible(fullName, False)
		else:
			self.SetVisible(fullName, True)
			width = max(1, size[0] * recentHp / maxHp)
			self.SetSize(fullName, (width, size[1]))
		text = "%d/%d" % (recentHp, maxHp)
		self.SetText("/main_pnl/pnl_control/lb_hp", text)
		# 能量值
		for idx in xrange(1, 9):
			fullName = "/main_pnl/pnl_control/pnl_energy/img_energy0%d" % idx
			if mob.mEnergyPoint >= idx:
				self.SetSprite(fullName, "textures/ui/netease_round/img_fire_01")
			else:
				self.SetSprite(fullName, "textures/ui/netease_round/img_fire_02")
	
	def HideControl(self):
		self.SetVisible("/main_pnl/pnl_control", False)
		self.mCanUseSkill = False
		self.mControlMob = None
	
	def DrawCountdownVisible(self):
		if not self.mCanUseSkill:
			self.SetVisible("/main_pnl/pnl_control/pnl_countdown", False)
			return
		if self.mAlreadySendSkill:
			self.SetVisible("/main_pnl/pnl_control/pnl_countdown", False)
			return
		self.SetVisible("/main_pnl/pnl_control/pnl_countdown", True)
	
	def DrawSelectCountdown(self, num):
		num = int(num)
		if num < 0:
			num = 0
		if num < 10:
			self.SetVisible("/main_pnl/pnl_control/pnl_countdown/img_1", False)
			self.SetSprite("/main_pnl/pnl_control/pnl_countdown/img_0", "textures/ui/netease_round/img_num_0%d" % num)
		else:
			viewNum = num // 10
			self.SetVisible("/main_pnl/pnl_control/pnl_countdown/img_1", True)
			self.SetSprite("/main_pnl/pnl_control/pnl_countdown/img_1", "textures/ui/netease_round/img_num_0%d" % viewNum)
			viewNum = num % 10
			self.SetSprite("/main_pnl/pnl_control/pnl_countdown/img_0", "textures/ui/netease_round/img_num_0%d" % viewNum)
	# ----------------------------------------------------------------------------------------------------------------------------------
	def GetMobSelectImage(self, mob):
		if mob.mSide == self.mBattle.mMySide:
			return "textures/ui/netease_round/header_03"
		else:
			return "textures/ui/netease_round/header_02"
	# ----------------------------------------------------------------------------------------------------------------------------------
	# Create函数是继承自ScreenNode，会在UI创建完成后被调用
	def Create(self):
		parent = "/main_pnl/img_time_line"
		bgName = "/main_pnl/img_time_line/img_next_round_bg"
		bgSize = self.GetSize(bgName)
		lbName = "/main_pnl/img_time_line/lb_next"
		lbPos = self.GetPosition(lbName)
		lbSize = self.GetSize(lbName)
		baseName = "/main_pnl/img_time_line/btn_round_base"
		basePos = self.GetPosition(baseName)
		baseSize = self.GetSize(baseName)
		baseOffset = baseSize[1] + 1
		self.mActiveMob = "/main_pnl/img_time_line/btn_active_head"
		self.mTimelineData = {
			"parent": parent,
			"parentSize": self.GetSize(parent),
			"bgName": bgName,
			"bgSize": bgSize,
			"offset": baseOffset,
			"lbName": lbName,
			"lbPos": lbPos,
			"lbSize": lbSize,
			"basePos": basePos,
			"activePos": self.GetPosition(self.mActiveMob),
			"activeSize": self.GetSize(self.mActiveMob),
		}
		# 当前回合的参战角色头像，最多10个
		
		self.AddTouchEventHandler(self.mActiveMob, self.OnTimelineActiveHead)
		self.mMobOrderDict = {}
		for idx in xrange(1, 10):
			name = "btnThisRound_%d" % idx
			self.Clone(baseName, parent, name)
			fullName = "%s/%s" % (parent, name)
			self.mMobOrderDict[idx] = fullName
			self.SetPosition(fullName, (basePos[0], basePos[1]-idx*baseOffset+baseOffset))
			self.AddTouchEventHandler(fullName, self.OnTimelineHead)
		# 下一回合的参战角色头像，最多10个
		self.mMobNextOrderDict = {}
		for idx in xrange(10):
			name = "btnNextRound_%d" % idx
			self.Clone(baseName, parent, name)
			fullName = "%s/%s" % (parent, name)
			self.mMobNextOrderDict[idx] = fullName
			self.AddTouchEventHandler(fullName, self.OnTimelineHeadNext)
		self.SetVisible(baseName, False)
		self.AddTouchEventHandler("/main_pnl/img_time_line/btn_show_nickname", self.OnChangeShowNickname)
		# 参战角色tips
		self.AddTouchEventHandler("/main_pnl/pnl_mob_tips/btn_mob_tips", self.OnHideMobTips)
		scrollInfo = {}
		parent = "/main_pnl/pnl_mob_tips/btn_mob_tips/img_tips_bg"
		scrollInfo["headRect"] = parent + "/img_mob_tips_head_rect"
		scrollInfo["headIcon"] = parent + "/img_mob_tips_head_rect/img_mob_tips_head_icon"
		scrollInfo["mobName"] = parent + "/lb_mob_tips_name"
		base = parent + "/pnl_mob_effect_base"
		basePos = self.GetPosition(base)
		baseSize = self.GetSize(base)
		scrollInfo["effectList"] = []
		for idx in xrange(5):
			name = "pnl_mob_effect_%d" % idx
			self.Clone(base, parent, name)
			fullName = "%s/%s" % (parent, name)
			scrollInfo["effectList"].append(fullName)
			x = basePos[0]
			y = basePos[1] + idx * (baseSize[1] + 2)
			self.SetPosition(fullName, (x, y))
		self.SetVisible(base, False)
		self.mMobTipsData = scrollInfo
		# 4个技能按钮
		self.mSkillButtonDownInfo = None
		for idx in xrange(4):
			fullName = "/main_pnl/pnl_control/btn_use_skill_%d" % idx
			self.AddTouchEventHandler(fullName, self.OnSkillButton)
		# 生命值
		hpBar = "/main_pnl/pnl_control/img_hp_bg/img_hp_recent"
		self.mHpBarData = {
			"name": hpBar,
			"size": self.GetSize(hpBar),
			"pos": self.GetPosition(hpBar),
		}
	# ----------------------------------------------------------------------------------------------------------------------------------
	def OnChangeShowNickname(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.ChangeNicknameShow()
	
	def OnTimelineActiveHead(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnShowMobTips(False, 0)
	
	def OnTimelineHead(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnShowMobTips(False, idx)
	
	def OnTimelineHeadNext(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.OnShowMobTips(True, idx)
	
	def OnHideMobTips(self, args):
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			self.DoHideMobTips()
	
	def OnSkillButton(self, args):
		line = args["ButtonPath"].split("/")
		line = line[-1]
		line = line.split("_")
		idx = int(line[-1])
		event = args["TouchEvent"]
		if event == TouchEvent.TouchUp:
			if not self.mSkillButtonDownInfo:
				return
			downIdx, alreadyShow = self.mSkillButtonDownInfo["idx"], self.mSkillButtonDownInfo["alreadyShow"]
			if downIdx != idx:
				return
			self.mSkillButtonDownInfo = None
			if alreadyShow:
				self.DoHideSkillTips()
			else:
				self.TryUseSkill(idx)
		elif event == TouchEvent.TouchDown:
			self.mSkillButtonDownInfo = {
				"startTp": time.time(),
				"idx": idx,
				"alreadyShow": False,
			}
		elif event == TouchEvent.TouchMove:
			pass
		elif event == TouchEvent.TouchCancel:
			self.DoHideSkillTips()
		elif event == TouchEvent.TouchMoveOut:
			self.DoHideSkillTips()
	# ----------------------------------------------------------------------------------------------------------------------------------
	


