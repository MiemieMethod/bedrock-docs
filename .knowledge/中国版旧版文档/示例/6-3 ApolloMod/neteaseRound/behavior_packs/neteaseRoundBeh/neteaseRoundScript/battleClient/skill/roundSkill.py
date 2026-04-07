# -*- coding: utf-8 -*-

import random
import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst

# 创建新的技能对象
def CreateSkill(identifier):
	return Skill(identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Skill(object):
	def __init__(self, identifier):
		super(Skill, self).__init__()
		self.mIdentifier = identifier
		self.mCaster = None
		self.mBattle = None
		self.mConfig = roundConst.ConfigSkillMap[identifier]	# 配置字典
		self.mCostEnergy = self.mConfig.get("costEnergy", 1)
		self.mTargetType = self.mConfig.get("targetType", roundConst.SkillTargetType.Self)
		self.mTargetNum = self.mConfig.get("targetNum", 1)
	
	def InitFromMonster(self, monster, battle):
		self.mCaster = weakref.proxy(monster)
		self.mBattle = weakref.proxy(battle)
	
	def Destroy(self):
		pass

	def GetName(self):
		return self.mConfig.get("showName", "")

	def GetImage(self):
		default = "textures/ui/netease_round/img08_01"
		return self.mConfig.get("icon", default)
	
	def GetDisableImage(self):
		default = "textures/ui/netease_round/img08_01"
		return self.mConfig.get("iconDisable", default)
	
	def GetDesc(self):
		return self.mConfig.get("desc", "")
	
	def GetPerformIdentifier(self):
		return self.mConfig.get("perform", "")
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def GetPossibleTarget(self, friendList, enemyList):
		if self.mTargetType == roundConst.SkillTargetType.Self:
			return True, [self.mCaster,]
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceFriendOne:
			return False, friendList
		elif self.mTargetType == roundConst.SkillTargetType.ChoiceEnemyOne:
			return False, enemyList
		elif self.mTargetType == roundConst.SkillTargetType.RandomFriendSome:
			if friendList:
				random.shuffle(friendList)
				return True, friendList[:self.mTargetNum]
			else:
				return True, []
		elif self.mTargetType == roundConst.SkillTargetType.RandomEnemySome:
			if enemyList:
				random.shuffle(enemyList)
				return True, enemyList[:self.mTargetNum]
			else:
				return True, []
		else:
			return False, []
	