# -*- coding: utf-8 -*-

import random
import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst

# 创建新的技能对象
def CreateSkill(identifier):
	if identifier == "neteaseRound:heal":
		import neteaseRoundScript.battleServer.skill.skillHeal as skillHeal
		return skillHeal.Skill(identifier)
	else:
		return Skill(identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Skill(object):
	def __init__(self, identifier):
		super(Skill, self).__init__()
		self.mIdentifier = identifier
		self.mCaster = None
		self.mConfig = roundConst.ConfigSkillMap[identifier]	# 配置字典
		self.mCostEnergy = self.mConfig.get("costEnergy", 1)
		self.mTargetType = self.mConfig.get("targetType", roundConst.SkillTargetType.Self)
		self.mTargetNum = self.mConfig.get("targetNum", 1)
	
	def InitFromMonster(self, monster):
		self.mCaster = weakref.proxy(monster)
	
	def Destroy(self):
		pass
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def RandomTarget(self, friendList, enemyList):
		if self.mTargetType == roundConst.SkillTargetType.Self:
			return [self.mCaster,]
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceFriendOne:
			if friendList:
				random.shuffle(friendList)
				return friendList[:1]
			else:
				return []
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceEnemyOne:
			if enemyList:
				random.shuffle(enemyList)
				return enemyList[:1]
			else:
				return [] 
		elif self.mTargetType == roundConst.SkillTargetType.RandomFriendSome:
			if friendList:
				random.shuffle(friendList)
				return friendList[:self.mTargetNum]
			else:
				return []
		elif self.mTargetType == roundConst.SkillTargetType.RandomEnemySome:
			if enemyList:
				random.shuffle(enemyList)
				return enemyList[:self.mTargetNum]
			else:
				return []
		else:
			return []
	
	def CheckSkillTarget(self, targetList):
		if self.mTargetType == roundConst.SkillTargetType.Self:
			if len(targetList) != 1:
				return False
			mob = targetList[0]
			if mob.mId != self.mCaster.mId:
				return False
			return True
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceFriendOne:
			if len(targetList) != 1:
				return False
			mob = targetList[0]
			if mob.mSide != self.mCaster.mSide:
				return False
			return True
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceEnemyOne:
			if len(targetList) != 1:
				return False
			mob = targetList[0]
			if mob.mSide == self.mCaster.mSide:
				return False
			return True
		elif self.mTargetType == roundConst.SkillTargetType.RandomFriendSome:
			if len(targetList) > self.mTargetNum:
				return False
			for mob in targetList:
				if mob.mSide != self.mCaster.mSide:
					return False
			return True
		elif self.mTargetType == roundConst.SkillTargetType.RandomEnemySome:
			if len(targetList) > self.mTargetNum:
				return False
			for mob in targetList:
				if mob.mSide == self.mCaster.mSide:
					return False
			return True
		else:
			return False
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def ApplyDamageOnTargets(self, targetList):
		result = []
		damageList = self.mConfig.get("damageList", [])
		attack = self.mCaster.attack
		for oneHit in damageList:
			singleHitResult = []
			multi = oneHit.get("multi", 0.0)
			extra = oneHit.get("extra", 0)
			if abs(multi) > 0.0001:
				baseDamage = attack * multi + extra
			else:
				baseDamage = extra
			for mob in targetList:
				if mob.IsDie():
					continue
				crit = max(0, self.mCaster.crit - mob.tough)
				factor = random.random()
				if crit > factor:
					isCrit = True 
				else:
					isCrit = False
				damage = max(baseDamage - mob.defence, 1)
				if isCrit:
					critDamage = max(1, self.mCaster.critDamage - mob.critImmune)
					damage = damage * critDamage
				damage = int(damage)
				mob.OnDamage(damage)
				singleResult = {
					"resultType": roundConst.SkillResultType.Damage,
					"mobId": mob.mId,
					"isCrit": isCrit,
					"point": damage,
					"mHitPoint": mob.mHitPoint,
					"mAlreadyDie": mob.mAlreadyDie,
				}
				singleHitResult.append(singleResult)
			result.append(singleHitResult)
		return result

	def ApplyHealOnTargets(self, targetList):
		result = []
		damageList = self.mConfig.get("damageList", [])
		attack = self.mCaster.attack
		for oneHit in damageList:
			singleHitResult = []
			multi = oneHit.get("multi", 0.0)
			extra = oneHit.get("extra", 0)
			if abs(multi) > 0.0001:
				baseDamage = attack * multi + extra
			else:
				baseDamage = extra
			for mob in targetList:
				if mob.IsDie():
					continue
				# 治疗效果暴击率不需要减去目标韧性
				crit = self.mCaster.crit
				factor = random.random()
				if crit > factor:
					isCrit = True 
				else:
					isCrit = False
				# 治疗效果不需要减去目标防御
				damage = baseDamage
				if isCrit:
					# 治疗效果的暴击伤害不需要减去目标暴击伤害减免
					critDamage = max(1, self.mCaster.critDamage)
					damage = damage * critDamage
				damage = int(damage)
				mob.OnHeal(damage)
				singleResult = {
					"resultType": roundConst.SkillResultType.Heal,
					"mobId": mob.mId,
					"isCrit": isCrit,
					"point": damage,
					"mHitPoint": mob.mHitPoint,
					"mAlreadyDie": mob.mAlreadyDie,
				}
				singleHitResult.append(singleResult)
			result.append(singleHitResult)
		return result

	def ApplyEffectOnTargets(self, targetList):
		result = []
		effectList = self.mConfig.get("effectList", [])
		effectHit = self.mCaster.effectHit
		for oneEffect in effectList:
			singleEffectResult = []
			identifier = oneEffect.get("identifier", None)
			if identifier is None:
				continue
			hitStyle = oneEffect.get("hitStyle", roundConst.HitStyle.StyleMustHit)
			multi = oneEffect.get("multi", 1.0)
			extra = oneEffect.get("extra", 0.0)
			for mob in targetList:
				if mob.IsDie():
					continue
				if hitStyle == roundConst.HitStyle.StyleMustHit:
					isHit = True 
				else:
					hitRate = effectHit * multi + extra
					hitRate = 1 + hitRate - mob.effectResist
					factor = random.random()
					if hitRate > factor:
						isHit = True 
					else:
						isHit = False
				if isHit:
					needRemove, effect = mob.OnEffectAdd(self.mCaster, identifier, True)
					singleResult = {
						"resultType": roundConst.SkillResultType.Effect,
						"mobId": mob.mId,
						"isHit": isHit,
						"needRemove": needRemove,
						"effectData": effect.PackSyncData(),
					}
				else:
					singleResult = {
						"resultType": roundConst.SkillResultType.Effect,
						"mobId": mob.mId,
						"isHit": isHit,
					}
				singleEffectResult.append(singleResult)
			result.append(singleEffectResult)
		return result

	def ApplyOnTargets(self, targetList):
		result = []
		result.extend(self.ApplyDamageOnTargets(targetList))
		result.extend(self.ApplyEffectOnTargets(targetList))
		return result
	# -----------------------------------------------------------------------------------------------------------------------------------------

