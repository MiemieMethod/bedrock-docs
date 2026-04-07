# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.effect.roundEffect as roundEffect


class Effect(roundEffect.Effect):
	def __init__(self, uniqueId, identifier):
		super(Effect, self).__init__(uniqueId, identifier)
		self.mEffectType = roundConst.BattleEffectType.Weak1
	
	def OnAdd(self, target):
		super(Effect, self).OnAdd(target)
		target.OnAddAttrEffect(self.mEffectType, self.mId, "attack", 0, self.mDamage)

	def OnRemove(self, target, fromSkill):
		target.OnDiscardAttrEffect(self.mId)
		super(Effect, self).OnRemove(target, fromSkill)

	def OnActionFinish(self, target):
		self.OnReduce(target)
		