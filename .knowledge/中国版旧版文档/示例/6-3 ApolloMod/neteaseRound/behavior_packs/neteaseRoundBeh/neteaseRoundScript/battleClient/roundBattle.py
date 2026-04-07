# -*- coding: utf-8 -*-

import time
import weakref

import client.extraClientApi as clientApi
from mod_log import engine_logger as logger

import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.monster.roundMonster as roundMonster
import neteaseRoundScript.battleClient.perform.roundPerform as roundPerform
from neteaseRoundScript.ui.uiDef import UIDef

# 创建一场新的战斗
# 暂时所有类型的战斗共享一个类
def CreateBattle(battleStyle):
	if battleStyle == roundConst.BattleStyle.PVP:
		return RoundBattle(battleStyle)
	elif battleStyle == roundConst.BattleStyle.PVE:
		return RoundBattle(battleStyle)
	else:
		raise "CreateBattle fail by wrong battleStyle [{}]".format(battleStyle)
# --------------------------------------------------------------------------------------------------------------------------------------
class RoundBattle(object):
	def __init__(self, battleStyle):
		super(RoundBattle, self).__init__()
		self.mBattleStyle = battleStyle
		self.mSystem = None 
		self.mMySide = None
		# 当前回合/下个回合的行动顺序
		self.mMobOrders = []
		self.mMobOrdersNextRound = []
		# 当前回合，轮到第几个角色行动
		self.mActionIndex = None 
		# 战斗结果
		self.mBattleResult = None
		# 是否初始化场景完成
		self.mSceneComplete = False
		# 技能演出
		self.mMaxUsedId = 0
		self.mActivePerforms = {}
		# 缓存结算
		self.mCacheBattleResult = None
	
	def GetUniqueId(self):
		self.mMaxUsedId += 1
		return self.mMaxUsedId

	def UnPackSyncData(self, data):
		self.mId = data["mId"]
		self.mControlSideA = data["mControlSideA"]
		self.mControlSideB = data["mControlSideB"]
		if self.mControlSideA == clientApi.GetLocalPlayerId():
			self.mMySide = roundConst.BattleSide.SideA
		else:
			self.mMySide = roundConst.BattleSide.SideB
		self.mRoundState = data["mRoundState"]
		self.mRoundStateTick = 0
		self.mMaxRoundCountdown = 0
		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		self.mRoundTimer = comp.AddRepeatedTimer(1.0, self.Tick)
		self.mRoundNum = data["mRoundNum"]
		#
		self.mMobDict = {}
		self.mMobPos2Id = {}
		for uniqueId, mobData in data["mMobDict"].iteritems():
			mob = roundMonster.CreateMonsterByIdentifier(mobData["mIdentifier"])
			mob.UnPackSyncData(mobData)
			mob.InitFromBattle(self.mSystem, self)
			self.mMobDict[uniqueId] = mob
			self.mMobPos2Id[(mob.mSide, mob.mPos)] = uniqueId
	
	def InitScene(self, system):
		self.mSystem = system
		self.mControlUI = weakref.proxy(system.GetUiMgr().GetUI(UIDef.UIBattleControl))

	def DeclareInitSceneComplete(self):
		self.mSceneComplete = True
		self.SendToServer(roundConst.BattleClientEvent.BattleStartAck)

	def Destroy(self):
		if self.mRoundTimer:
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			comp.CancelTimer(self.mRoundTimer)
			self.mRoundTimer = None
		for mob in self.mMobDict.itervalues():
			mob.Destroy()
		self.mMobDict.clear()
		self.mMobPos2Id.clear()
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def Tick(self):
		self.mRoundStateTick += 1
		if self.mRoundState == roundConst.BattleState.BattleActionSelect:
			mob = self.GetActionMob()
			if mob.mControl != clientApi.GetLocalPlayerId():
				return
			leftTick = max(0, self.mMaxRoundCountdown - self.mRoundStateTick)
			self.mControlUI.DrawSelectCountdown(leftTick)
			if leftTick == 0:
				text = "%s行动超时" % mob.GetNickName()
				self.mControlUI.DrawNotice("", "", text)
				self.mControlUI.LeaveSkillSelect()
		# elif self.mRoundState == roundConst.BattleState.BattleActionPlay:
		#	if self.mRoundStateTick == 6:
		#		self.SendToServer(roundConst.BattleClientEvent.ActionSkillAck)
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def GetThisRoundMobs(self):
		mobList = []
		for mobId in self.mMobOrders[self.mActionIndex:]:
			mob = self.mMobDict.get(mobId, None)
			if mob and mob.IsAlive():
				mobList.append(mob)
		return mobList
	
	def GetNextRoundMobs(self):
		mobList = []
		thisRoundMobs = self.mMobOrders[self.mActionIndex:]
		for mobId in self.mMobOrdersNextRound:
			if mobId in thisRoundMobs:
				continue
			mob = self.mMobDict.get(mobId, None)
			if mob and mob.IsAlive():
				mobList.append(mob)
		return mobList
	
	def CheckMonsterControlAble(self, mob):
		if not mob or mob.IsDie():
			return False
		if mob.mSide != self.mMySide:
			return False
		if mob.mControl != clientApi.GetLocalPlayerId():
			return False 
		return True

	def FindNextControlMob(self):
		if self.mRoundState == roundConst.BattleState.BattleActionSelect:
			mobId = self.mMobOrders[self.mActionIndex]
			mob = self.mMobDict.get(mobId, None)
			if self.CheckMonsterControlAble(mob):
				return mob, True
		if self.mRoundState <= roundConst.BattleState.BattleActionFin:
			propList = self.mMobOrders[self.mActionIndex:]
		else:
			propList = self.mMobOrders[self.mActionIndex+1:]
		for mobId in propList:
			mob = self.mMobDict.get(mobId, None)
			if self.CheckMonsterControlAble(mob):
				return mob, False
		for mobId in self.mMobOrdersNextRound:
			mob = self.mMobDict.get(mobId, None)
			if self.CheckMonsterControlAble(mob):
				return mob, False
		return None, False
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def OnRoundStart(self, data):
		self.ChangeRoundState(data["mRoundState"])
		self.mRoundNum = data["mRoundNum"]
		self.mMobOrders = data["mMobOrders"]
		self.mMobOrdersNextRound = data["mMobOrders"]
		self.mActionIndex = data["mActionIndex"]
		#
		self.mControlUI.DrawTimeline()
		self.mControlUI.DrawControl()
		left = "第%d回合" % self.mRoundNum
		right = "开始"
		text = "%s%s\n" % (left, right)
		self.mControlUI.DoShowSkillPerform(text)
	
	def OnActionStart(self, data):
		self.ChangeRoundState(data["mRoundState"])
		self.mRoundNum = data["mRoundNum"]
		self.mActionIndex = data["mActionIndex"]
		self.mMaxRoundCountdown = data["BattleActionSelectClientTick"]
		#
		self.mControlUI.DrawTimeline()
		self.mControlUI.DrawControl(True)
		mob = self.GetActionMob()
		self.mSystem.GetBattleScene().ChangeActiveMonster(mob)
		if mob.mControl == clientApi.GetLocalPlayerId():
			self.mControlUI.DrawNotice(mob.GetNickName(), "等待行动中", "")
			text = "%s 等待行动中" % mob.GetNickName()
		else:
			self.mControlUI.DrawNotice(mob.GetNickName(), "正在进攻", "")
			text = "%s正在进攻" % mob.GetNickName()
		self.mControlUI.DoShowSkillPerform("%s的行动回合开始了" % mob.GetNickName())
		self.mControlUI.DoShowSkillPerform(text)
	
	def OnSkillSelectResponse(self, data):
		if not data["suc"]:
			self.mControlUI.DoShowSkillPerform("%s\n" % data["message"])
			return
		self.mControlUI.DoShowSkillPerform("选择释放技能成功\n")

	def IsOnPerforming(self):
		if self.mActivePerforms:
			return True
		else:
			return False

	def OnPerformFinish(self, uniqueId):
		# print "OnPerformFinish uniqueId={}".format(uniqueId)
		performInst = self.mActivePerforms.get(uniqueId, None)
		if not performInst:
			return
		self.SendToServer(roundConst.BattleClientEvent.ActionSkillAck)
		del self.mActivePerforms[uniqueId]
		performInst.Destroy()
		# 战斗是否结束
		if self.mCacheBattleResult:
			self.OnBattleFinish(self.mCacheBattleResult)

	def OnSkillPlayStart(self, data):
		self.ChangeRoundState(roundConst.BattleState.BattleActionPlay)
		self.mControlUI.DrawNotice("", "", "技能释放中")
		if data["useSkill"] is None:
			self.SendToServer(roundConst.BattleClientEvent.ActionSkillAck)
			return
		mob = self.GetMobById(data["actorId"])
		skill = mob.GetSkillByIndex(data["useSkill"])
		if not skill:
			self.SendToServer(roundConst.BattleClientEvent.ActionSkillAck)
			return
		mob.mEnergyPoint = data["mEnergyPoint"]
		self.mControlUI.DrawControl()
		#
		costEnergy = data["costEnergy"]
		text = "[%s]消耗[%d]点能量，释放技能[%s]\n" % (mob.GetNickName(), costEnergy, skill.GetName())
		performInst = roundPerform.CreatePerform(skill.GetPerformIdentifier())
		uniqueId = self.GetUniqueId()
		self.mActivePerforms[uniqueId] = performInst
		performInst.InitSkillPlay(uniqueId, self, mob, data)
		# for oneRet in data["result"]:
		#	for one in oneRet:
		#		resultType = one["resultType"]
		#		if resultType == roundConst.SkillResultType.Damage:
		#			text += self.FormatDamageResult(one)
		#		elif resultType == roundConst.SkillResultType.Heal:
		#			text += self.FormatHealResult(one)
		#		elif resultType == roundConst.SkillResultType.Effect:
		#			text += self.FormatEffectResult(one)
	
	def FormatDamageResult(self, one):
		target = self.GetMobById(one["mobId"])
		target.mHitPoint = one["mHitPoint"]
		target.mAlreadyDie = one["mAlreadyDie"]
		target.UpdateHeadUI()
		self.mSystem.GetBattleScene().CreateFlyingDamage(target, one["isCrit"], one["point"])
		if target.mAlreadyDie:
			self.mSystem.GetBattleScene().PlayMonsterDie(target)
		if one["isCrit"]:
			text = "技能命中并造成了暴击，"
		else:
			text = "技能命中了，"
		if target.mAlreadyDie:
			text += "对[%s]造成[%d]点伤害，[%s]死亡\n" % (target.GetNickName(), one["point"], target.GetNickName())
		else:
			text += "对[%s]造成[%d]点伤害，剩余[%d]点生命\n" % (target.GetNickName(), one["point"], target.mHitPoint)
		return text
	
	def FormatHealResult(self, one):
		target = self.GetMobById(one["mobId"])
		target.mHitPoint = one["mHitPoint"]
		target.mAlreadyDie = one["mAlreadyDie"]
		target.UpdateHeadUI()
		self.mSystem.GetBattleScene().CreateFlyingHeal(target, one["isCrit"], one["point"])
		if one["isCrit"]:
			text = "为[%s]恢复了[%d]点生命值（暴击），现在[%s]的生命值为[%d]\n" % (target.GetNickName(), one["point"], target.GetNickName(),  target.mHitPoint)
		else:
			text = "为[%s]恢复了[%d]点生命值，现在[%s]的生命值为[%d]\n" % (target.GetNickName(), one["point"], target.GetNickName(),  target.mHitPoint)
		return text

	def FormatEffectResult(self, one):
		target = self.GetMobById(one["mobId"])
		if one["isHit"]:
			for effectId in one["needRemove"]:
				target.OnEffectDiscard(effectId)
			newEffect = target.OnEffectAdd(one["effectData"])
			target.UpdateHeadUI()
			text = "技能附加的持续效果[%s]命中了[%s]，持续[%d]回合\n" % (newEffect.GetName(), target.GetNickName(), newEffect.mRound)
			self.mSystem.GetBattleScene().CreateFlyingEffect(target, newEffect.GetColor(), newEffect.GetName())
		else:
			text = "[%s]抵抗了技能附加的持续效果\n" % target.GetNickName()
			self.mSystem.GetBattleScene().CreateFlyingEffect(target, (1, 1, 1, 0.8), "未命中")
		return text

	def OnActionFinish(self, data):
		self.ChangeRoundState(data["mRoundState"])
		self.mRoundNum = data["mRoundNum"]
		self.mActionIndex = data["mActionIndex"]
		#
		self.mControlUI.DrawTimeline()
		self.mControlUI.DrawControl()

	def OnRoundFinish(self, data):
		self.ChangeRoundState(data["mRoundState"])
		#
		text = "第%d回合结束了\n" % self.mRoundNum
		self.mControlUI.DoShowSkillPerform(text)

	def OnBattleFinish(self, data):
		if self.IsOnPerforming():
			self.mCacheBattleResult = data
			return
		self.ChangeRoundState(data["mRoundState"])
		battleResult = data["battleResult"]
		self.mSystem.DoShowBattleResult(data)

	def OnMonsterAddEffect(self, data):
		mob = self.GetMobById(data["mobId"])
		newEffect = mob.OnEffectAdd(data["effectData"])
		text = "[%s]受到了持续效果[%s]的影响，持续[%d]回合\n" % (mob.GetNickName(), newEffect.GetName(), newEffect.mRound)
		self.mControlUI.DoShowSkillPerform(text)
		mob.UpdateHeadUI()

	def OnMonsterDiscardEffect(self, data):
		mob = self.GetMobById(data["mobId"])
		delEffect = mob.OnEffectDiscard(data["effectId"])
		if not delEffect:
			return
		text = "[%s]身上的持续效果[%s]结束了\n" % (mob.GetNickName(), delEffect.GetName())
		self.mControlUI.DoShowSkillPerform(text)
		mob.UpdateHeadUI()

	def OnMonsterUpdate(self, data):
		mob = self.GetMobById(data["mobId"])
		mob.UpdateAttribute(data)

	def OnEffectUpdate(self, data):
		mob = self.GetMobById(data["mobId"])
		mob.OnEffectUpdate(data)

	def OnEffectAction(self, data):
		mob = self.GetMobById(data["mobId"])
		mob.OnEffectAction(data)

	def OnEnergyRestore(self, data):
		mob = self.GetMobById(data["mobId"])
		point = data["point"]
		mob.mEnergyPoint = data["mEnergyPoint"]
	
	def OnUpdateNextOrder(self, data):
		old = tuple(self.mMobOrdersNextRound)
		new = tuple(data["mobOrders"])
		if old == new:
			return
		self.mMobOrdersNextRound = data["mobOrders"]
		self.mControlUI.DrawTimeline()
		self.mControlUI.DrawControl()
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def ChangeRoundState(self, state):
		self.mRoundState = state
		self.mRoundStateTick = 0

	def SendToServer(self, eventName, eventData={}):
		eventData["playerId"] = clientApi.GetLocalPlayerId()
		self.mSystem.NotifyToServer(eventName, eventData)
	
	def GetActionMob(self):
		if self.mActionIndex >= len(self.mMobOrders):
			return None
		mobId = self.mMobOrders[self.mActionIndex]
		return self.mMobDict.get(mobId, None)
	
	def GetTargetAble(self):
		friendList = []
		enemyList = []
		for mob in self.mMobDict.itervalues():
			if mob.IsDie():
				continue
			if mob.mSide == self.mMySide:
				friendList.append(mob)
			else:
				enemyList.append(mob)
		return friendList, enemyList
	# -------------------------------------------------------------------------------------------------------------------------------------------
	def GetMobById(self, mobId):
		return self.mMobDict.get(mobId, None)
	# -------------------------------------------------------------------------------------------------------------------------------------------
