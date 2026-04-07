# -*- coding: utf-8 -*-

import weakref
import random

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger

import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleClient.skill.roundSkill as roundSkill
import neteaseRoundScript.battleClient.effect.roundEffect as roundEffect

# 创建一个新的战斗角色
# 暂时所有战斗角色共享一个类
def CreateMonsterByIdentifier(identifier):
	return Monster(identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Monster(object):
	def __init__(self, identifier):
		super(Monster, self).__init__()
		self.mIdentifier = identifier
		self.mSystem = None
		self.mBattle = None
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
		# 被挂上的effect
		self.mEffectDict = {}
		#
		self.mLinkUI = None

	def UnPackSyncData(self, data):
		self.mId = data["mId"]
		self.mAlreadyDie = data["mAlreadyDie"]
		self.mControl = data["mControl"]
		self.mSide = data["mSide"]
		self.mPos = data["mPos"]
		self.mExtraAttr = data["mExtraAttr"]
		self.mSpecStatus = data["mSpecStatus"]
		self.mHitPoint = data["mHitPoint"]
		self.mEnergyPoint = data["mEnergyPoint"]
		#
		self.mEffectDict = {}
		for uniqueId, effectData in data["mEffectDict"].iteritems():
			effect = roundEffect.CreateEffect(effectData["mIdentifier"])
			effect.UnPackSyncData(effectData)
			effect.InitFromMonster(self)
			self.mEffectDict[uniqueId] = effect

	def InitFromBattle(self, system, battle):
		self.mSystem = system
		self.mBattle = weakref.proxy(battle)
		for idx, identifier in enumerate(self.mConfig.get("skill", [])):
			skill = roundSkill.CreateSkill(identifier)
			skill.InitFromMonster(self, battle)
			self.mSkillMap[idx] = skill
	
	def Destroy(self):
		for skill in self.mSkillMap.itervalues():
			skill.Destroy()
		self.mSkillMap.clear()
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def IsDie(self):
		return self.mAlreadyDie
	
	def IsAlive(self):
		return (not self.mAlreadyDie)

	def IsForbidAction(self):
		if self.mSpecStatus.has_key(roundConst.BattleEffectType.Stun1):
			return True
		return False
	
	def GetSkillByIndex(self, idx):
		return self.mSkillMap.get(idx, None)
	
	def GetHeadImage(self):
		default = "textures/ui/netease_round/img09"
		return self.mConfig.get("headIcon", default)

	def GetNickName(self):
		name = self.mConfig.get("showName", "")
		return name
		# if self.mSide == self.mBattle.mMySide:
		#	return "我方%s%s" % (name, self.mPos)
		# else:
		#	return "敌方%s%s" % (name, self.mPos)
	
	def GetAllEffects(self):
		effectList = self.mEffectDict.values()
		effectList.sort(self.CmpEffect)
		return effectList
	
	def CmpEffect(self, a, b):
		return cmp(a.mId, b.mId)
	
	def LinkUIInstance(self, ui):
		self.mLinkUI = weakref.proxy(ui)
	
	def UpdateHeadUI(self):
		if not self.mLinkUI:
			return
		self.mLinkUI.UpdateByMonster(self)
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
	
	def UpdateAttribute(self, data):
		for attrName, attrValue in data.iteritems():
			if attrName in ("mobId", "battleId"):
				continue
			setattr(self, attrName, attrValue)
		if data.has_key("mHitPoint") or data.has_key("health"):
			self.UpdateHeadUI()
	# -----------------------------------------------------------------------------------------------------------------------------------------
	# 持续效果相关逻辑
	def OnEffectAdd(self, effectData):
		effect = roundEffect.CreateEffect(effectData["mIdentifier"])
		effect.UnPackSyncData(effectData)
		effect.InitFromMonster(self)
		self.mEffectDict[effect.mId] = effect
		return effect

	def OnEffectDiscard(self, uniqueId):
		effect = self.mEffectDict.get(uniqueId, None)
		if effect:
			del self.mEffectDict[uniqueId]
		return effect
	
	def OnEffectUpdate(self, data):
		effect = self.mEffectDict.get(data["effectId"], None)
		if not effect:
			return
		for attrName, attrValue in data.iteritems():
			if attrName in ("mobId", "effectId", "battleId"):
				continue
			setattr(effect, attrName, attrValue)
		self.UpdateHeadUI()
	
	def OnEffectAction(self, data):
		if data["actionStyle"] == "heal":
			point = data["point"]
			self.mHitPoint = data["mHitPoint"]
		self.UpdateHeadUI()
	# -----------------------------------------------------------------------------------------------------------------------------------------



