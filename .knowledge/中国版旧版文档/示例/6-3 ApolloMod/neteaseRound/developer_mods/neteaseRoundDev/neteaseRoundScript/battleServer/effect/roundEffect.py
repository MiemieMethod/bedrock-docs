# -*- coding: utf-8 -*-

import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst

# 创建新的持续效果对象
def CreateEffect(uniqueId, identifier):
	if identifier == "neteaseRound:haste":
		import neteaseRoundScript.battleServer.effect.effectHaste as effectHaste
		return effectHaste.Effect(uniqueId, identifier)
	elif identifier == "neteaseRound:regain":
		import neteaseRoundScript.battleServer.effect.effectRegain as effectRegain
		return effectRegain.Effect(uniqueId, identifier)
	elif identifier == "neteaseRound:slow":
		import neteaseRoundScript.battleServer.effect.effectSlow as effectSlow
		return effectSlow.Effect(uniqueId, identifier)
	elif identifier == "neteaseRound:stun":
		import neteaseRoundScript.battleServer.effect.effectStun as effectStun
		return effectStun.Effect(uniqueId, identifier)
	elif identifier == "neteaseRound:weak":
		import neteaseRoundScript.battleServer.effect.effectWeak as effectWeak
		return effectWeak.Effect(uniqueId, identifier)
	else:
		raise "not exist effect identifier={}".format(identifier)
# ---------------------------------------------------------------------------------------------------------------------------------------------
class Effect(object):
	def __init__(self, uniqueId, identifier):
		super(Effect, self).__init__()
		self.mId = uniqueId
		self.mIdentifier = identifier	# 唯一ID
		self.mCaster = None				# 效果释放者
		self.mDamage = 0
		self.mConfig = roundConst.ConfigEffectMap[identifier]	# 配置字典
		self.mRound = self.mConfig.get("round", 1)
		self.mReplaceList = self.mConfig.get("replaceList", [])
		self.mEffectType = roundConst.BattleEffectType.Empty
	
	def PackSyncData(self):
		return {
			"mId": self.mId,
			"mIdentifier": self.mIdentifier,
			"mRound": self.mRound,
			"mEffectType": self.mEffectType,
		}

	def InitFromMonster(self, monster):
		self.mCaster = monster
		damageConfig = self.mConfig.get("damage")
		style = damageConfig.get("style", roundConst.DamageStyle.StyleNone)
		if style == roundConst.DamageStyle.StyleNone:
			self.mDamage = 0
		else:
			multi = damageConfig.get("multi", 0.0)
			extra = damageConfig.get("extra", 0.0)
			if abs(multi) > 0.0001:
				self.mDamage = int(multi * monster.attack + extra)
			else:
				self.mDamage = int(extra)

	def Destroy(self):
		self.mCaster = None
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def OnAdd(self, target):
		pass

	def OnRemove(self, target, fromSkill=False):
		target.OnEffectDiscard(self.mId, fromSkill)

	def OnReduce(self, target):
		self.mRound -= 1
		target.SendEffectUpdateToAll(self, ["mRound"])
		if self.mRound <= 0:
			self.OnRemove(target, False)
	# -----------------------------------------------------------------------------------------------------------------------------------------
	def OnRoundStartBegin(self, target):
		pass

	def OnRoundStartEnd(self, target):
		pass

	def OnActionStartBegin(self, target):
		pass

	def OnActionStartEnd(self, target):
		pass

	def OnActionPlayBegin(self, target):
		pass

	def OnActionPlayEnd(self, target):
		pass

	def OnActionFinish(self, target):
		pass

	def OnBattleRoundFinish(self, target):
		pass
	# -----------------------------------------------------------------------------------------------------------------------------------------

	
		
		




