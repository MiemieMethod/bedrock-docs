# -*- coding: utf-8 -*-

import weakref
import random

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger

import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.skill.roundSkill as roundSkill
import  neteaseRoundScript.battleServer.effect.roundEffect as roundEffect

# 创建一个新的战斗角色
# 暂时所有战斗角色共享一个类
def CreateMonsterByIdentifier(uniqueId, control, side, pos, identifier):
	return Monster(uniqueId, control, side, pos, identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Monster(object):
	def __init__(self, uniqueId, control, side, pos, identifier):
		super(Monster, self).__init__()
		self.mId = uniqueId
		self.mAlreadyDie = False
		self.mSystem = None
		self.mBattle = None
		self.mControl = control		# 隶属哪个玩家 or AI
		self.mSide = side			# 隶属哪个阵营
		self.mPos = pos				# 站位
		self.mIdentifier = identifier	# 唯一ID
		self.mConfig = roundConst.ConfigMonsterMap[identifier]	# 配置字典
		self.mBaseAttr = self.mConfig.get("battleAttr", {})		# 原始配置属性
		# 临时属性，主要是持续效果带来的属性变化，
		# 以roundConst.BattleEffectType作为key，相同类型的key，后上的会顶掉先上的
		# 每个value都是一个字典，【uniqueId】代表效果的唯一ID，【attrName】代表影响的属性、【multi】代表基于基础值的乘数加成、【extra】代表加/减数加成
		self.mExtraAttr = {}
		# 特殊状态效果，类似晕眩、睡眠等
		# 以roundConst.BattleEffectType作为key，相同类型的key，后上的会顶掉先上的
		# 每个value都是一个字典，【uniqueId】代表效果的唯一ID
		self.mSpecStatus = {}		
		# 拥有的技能
		self.mSkillMap = {}
		self.mHasSelectNextSkill = False
		self.mNextSkillIndex = None
		self.mNextSkillTargets = []
		# 被挂上的effect
		self.mEffectDict = {}
		#
		self.mHitPoint = self.health
		self.mEnergyPoint = roundConst.BattleStartEnergy
	
	def PackSyncData(self):
		eventData = {
			"mId": self.mId,
			"mAlreadyDie": self.mAlreadyDie,
			"mControl": self.mControl,
			"mSide": self.mSide,
			"mPos": self.mPos,
			"mIdentifier": self.mIdentifier,
			"mExtraAttr": self.mExtraAttr,
			"mSpecStatus": self.mSpecStatus,
			"mEffectDict": {},
			"mHitPoint": self.mHitPoint,
			"mEnergyPoint": self.mEnergyPoint,
		}
		for uniqueId, effect in self.mEffectDict.iteritems():
			eventData["mEffectDict"][uniqueId] = effect.PackSyncData()
		return eventData

	def InitFromBattle(self, system, battle):
		self.mSystem = system
		self.mBattle = weakref.proxy(battle)
		for idx, identifier in enumerate(self.mConfig.get("skill", [])):
			skill = roundSkill.CreateSkill(identifier)
			skill.InitFromMonster(self)
			self.mSkillMap[idx] = skill
	
	def Destroy(self):
		for skill in self.mSkillMap.itervalues():
			skill.Destroy()
		self.mSkillMap.clear()
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def IsDie(self):
		return self.mAlreadyDie

	def GotoDie(self):
		self.mAlreadyDie = True
		for uniqueId in self.mEffectDict.keys():
			self.mEffectDict[uniqueId].OnRemove(self, False)
		self.mBattle.OnMobDie(self.mId)
		self.SendUpdateToAll(["mAlreadyDie"])

	def IsForbidAction(self):
		if self.mSpecStatus.has_key(roundConst.BattleEffectType.Stun1):
			return True
		return False
	# -----------------------------------------------------------------------------------------------------------------------------------------
	# 属性相关逻辑
	def __setattr__(self, key, value):
		if key in roundConst.BattleAttrKeys:
			raise "setattr {} fail, cannot changed attr".format(key)
		super(Monster, self).__setattr__(key, value)

	def __getattr__(self, key):
		if key in roundConst.BattleAttrKeys:
			return self.GetAttribute(key)
		return getattr(self, key)

	def GetAttribute(self, attrName):
		baseValue = self.mBaseAttr.get(attrName, 0)
		fMulti = 0.0
		fExtra = 0
		for data in self.mExtraAttr.itervalues():
			if data["attrName"] != attrName:
				continue
			fMulti += data.get("multi", 0.0)
			fExtra += data.get("extra", 0)
		if abs(fMulti) >= 0.0001:
			value = baseValue * (1 + fMulti) + fExtra
		else:
			value = baseValue + fExtra
		if attrName in roundConst.BattleIntAttrKeys:
			return int(value)
		else:
			return value
	
	def OnDamage(self, point):
		self.mHitPoint -= point
		if self.mHitPoint <= 0:
			self.GotoDie()

	def OnHeal(self, point):
		self.mHitPoint += point
		if self.mHitPoint > self.health:
			self.mHitPoint = self.health

	def OnEnergyRestore(self, point):
		self.mEnergyPoint += point
		if self.mEnergyPoint > self.energy:
			self.mEnergyPoint = self.energy
		self.SendEnergyRestoreToAll(point)

	def OnEnergyUse(self, point):
		self.mEnergyPoint -= point
		if self.mEnergyPoint < 0:
			self.mEnergyPoint = 0
	# -----------------------------------------------------------------------------------------------------------------------------------------
	# 持续效果相关逻辑
	def OnAddAttrEffect(self, attrType, uniqueId, attrName, multi, extra):
		data = {
			"attrType": attrType,
			"uniqueId": uniqueId,
			"attrName": attrName,
			"multi": multi,
			"extra": extra,
		}
		oldData = self.mExtraAttr.get(attrType, None)
		self.mExtraAttr[attrType] = data
		self.SendUpdateToAll(["mExtraAttr"])
		return oldData
	
	def OnDiscardAttrEffect(self, uniqueId):
		needRemove = []
		needRemoveData = []
		for attrType, data in self.mExtraAttr.iteritems():
			if data["uniqueId"] == uniqueId:
				needRemove.append(attrType)
				needRemoveData.append(data)
		for attrType in needRemove:
			del self.mExtraAttr[attrType]
		self.SendUpdateToAll(["mExtraAttr"])
		return needRemoveData
	
	def OnAddStatusEffect(self, attrType, uniqueId):
		data = {
			"attrType": attrType,
			"uniqueId": uniqueId,
		}
		oldData = self.mSpecStatus.get(attrType, None)
		self.mSpecStatus[attrType] = data
		self.SendUpdateToAll(["mSpecStatus"])
		return oldData
	
	def OnDiscardStatusEffect(self, uniqueId):
		needRemove = []
		needRemoveData = []
		for attrType, data in self.mSpecStatus.iteritems():
			if data["uniqueId"] == uniqueId:
				needRemove.append(attrType)
				needRemoveData.append(data)
		for attrType in needRemove:
			del self.mSpecStatus[attrType]
		self.SendUpdateToAll(["mSpecStatus"])
		return needRemoveData

	def OnEffectAdd(self, actor, identifier, fromSkill=False):
		uniqueId = self.mBattle.GetNewId()
		effect = roundEffect.CreateEffect(uniqueId, identifier)
		effect.InitFromMonster(actor)
		needRemove = self.RemoveEffectByIdentifier(effect.mReplaceList, fromSkill)
		self.mEffectDict[uniqueId] = effect
		effect.OnAdd(self)
		# 随技能释放获得的持续效果，需要随技能演出动画延时播放
		if not fromSkill:
			eventData = {
				"mobId": self.mId,
				"effectData": effect.PackSyncData(),
			}
			self.mBattle.SendToAll(roundConst.BattleServerEvent.MonsterAddEffect, eventData)
		return needRemove, effect

	def OnEffectDiscard(self, uniqueId, fromSkill=False):
		if self.mEffectDict.has_key(uniqueId):
			del self.mEffectDict[uniqueId]
			# 随技能释放导致的持续效果变化，需要随技能演出动画延时播放
			if not fromSkill:
				eventData = {
					"mobId": self.mId,
					"effectId": uniqueId,
				}
				self.mBattle.SendToAll(roundConst.BattleServerEvent.MonsterDiscardEffect, eventData)

	def RemoveEffectByIdentifier(self, identifierList, fromSkill):
		needRemove = []
		for uniqueId, effect in self.mEffectDict.iteritems():
			if effect.mIdentifier in identifierList:
				needRemove.append(uniqueId)
		for uniqueId in needRemove:
			self.mEffectDict[uniqueId].OnRemove(self, fromSkill)
		return needRemove
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def OnRoundStartBegin(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnRoundStartBegin(self)

	def OnRoundStartEnd(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnRoundStartEnd(self)
	
	def OnActionStartBegin(self):
		if self.mAlreadyDie:
			return
		self.OnEnergyRestore(roundConst.RoundStartEnergy)
		self.mHasSelectNextSkill = False
		self.mNextSkillIndex = None
		self.mNextSkillTargets = []
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnActionStartBegin(self)
	
	def OnActionStartEnd(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnActionStartEnd(self)
	
	def OnActionPlayBegin(self):
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnActionPlayBegin(self)
		if self.mAlreadyDie:
			return {"useSkill":None}
		if self.mNextSkillIndex is None:
			return {"useSkill":None}
		skill = self.mSkillMap.get(self.mNextSkillIndex, None)
		if not skill:
			return {"useSkill":None}
		targetList = []
		targetIdList = []
		for targetId in self.mNextSkillTargets:
			mob = self.mBattle.GetMobById(targetId)
			if not mob or mob.IsDie():
				continue
			targetList.append(mob)
			targetIdList.append(targetId)
		if not targetList:
			return {"useSkill":None}
		self.OnEnergyUse(skill.mCostEnergy)
		result = skill.ApplyOnTargets(targetList)
		data = {
			"actorId": self.mId,
			"useSkill": self.mNextSkillIndex,
			"targetIdList": targetIdList,
			"costEnergy": skill.mCostEnergy,
			"mEnergyPoint": self.mEnergyPoint,
			"result": result,
		}
		return data

	def OnActionPlayEnd(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnActionPlayEnd(self)

	def OnActionFinish(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnActionFinish(self)

	def OnBattleRoundFinish(self):
		if self.mAlreadyDie:
			return
		effectList = self.mEffectDict.values()
		for effect in effectList:
			effect.OnBattleRoundFinish(self)
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def SendUpdateToAll(self, attrNameList):
		eventData = {"mobId":self.mId}
		for attrName in attrNameList:
			eventData[attrName] = getattr(self, attrName)
		self.mBattle.SendToAll(roundConst.BattleServerEvent.MonsterUpdate, eventData)
	
	def SendEffectUpdateToAll(self, effect, attrNameList):
		eventData = {
			"mobId": self.mId,
			"effectId": effect.mId,
		}
		for attrName in attrNameList:
			eventData[attrName] = getattr(effect, attrName)
		self.mBattle.SendToAll(roundConst.BattleServerEvent.EffectUpdate, eventData)
	
	def SendEffectActionToAll(self, effect, data):
		eventData = {
			"mobId": self.mId,
			"effectId": effect.mId,
		}
		eventData.update(data)
		self.mBattle.SendToAll(roundConst.BattleServerEvent.EffectAction, eventData)
	
	def SendEnergyRestoreToAll(self, point):
		eventData = {
			"mobId": self.mId,
			"point": point,
			"mEnergyPoint": self.mEnergyPoint,
		}
		self.mBattle.SendToAll(roundConst.BattleServerEvent.EnergyRestore, eventData)
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def AIDoBattleActionSelect(self):
		self.mHasSelectNextSkill = True
		friendList, enemyList = self.mBattle.GetTargetAble(self.mSide)
		propSkillList = []
		for idx, skill in self.mSkillMap.iteritems():
			if self.mEnergyPoint < skill.mCostEnergy:
				continue
			targetList = skill.RandomTarget(friendList, enemyList)
			if not targetList:
				continue
			propSkillList.append((idx, skill, targetList))
		if not propSkillList:
			return
		result = random.choice(propSkillList)
		idx, skill, targetList = result
		self.mNextSkillIndex = idx
		self.mNextSkillTargets = []
		for mob in targetList:
			self.mNextSkillTargets.append(mob.mId)

	def CheckSelectSkill(self, skillIndex, skillTargets):
		skill = self.mSkillMap.get(skillIndex, None)
		if not skill:
			return False, "选择使用技能失败，目标技能不存在"
		targetSet = set()
		targetList = []
		for targetId in skillTargets:
			mob = self.mBattle.GetMobById(targetId)
			if not mob or mob.IsDie():
				return False, "选择使用技能失败，目标已经死亡了"
			targetList.append(mob)
			targetSet.add(targetId)
		if not targetList:
			return False, "选择使用技能失败，技能释放对象不能为空"
		if len(targetSet) != len(skillTargets):
			return False, "选择使用技能失败，技能释放对象不能重复"
		if not skill.CheckSkillTarget(targetList):
			return False, "选择使用技能失败，技能释放对象错误"
		return True, ""

	def SaveSelectSkill(self, skillIndex, skillTargets):
		self.mHasSelectNextSkill = True
		self.mNextSkillIndex = skillIndex
		self.mNextSkillTargets = skillTargets


