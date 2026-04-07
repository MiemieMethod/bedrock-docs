# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.effect.roundEffect as roundEffect

class Effect(roundEffect.Effect):
	def __init__(self, uniqueId, identifier):
		super(Effect, self).__init__(uniqueId, identifier)
		self.mEffectType = roundConst.BattleEffectType.Empty

	def OnActionStartBegin(self, target):
		target.OnHeal(self.mDamage)
		data = {
			"actionStyle": "heal",
			"point": self.mDamage,
			"mHitPoint": target.mHitPoint,
		}
		target.SendEffectActionToAll(self, data)

	def OnActionStartEnd(self, target):
		self.OnReduce(target)
		




