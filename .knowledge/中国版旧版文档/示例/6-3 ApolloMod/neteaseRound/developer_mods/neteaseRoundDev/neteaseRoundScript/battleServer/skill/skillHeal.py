# -*- coding: utf-8 -*-

import random
import weakref

import server.extraServerApi as serverApi
from mod_log import engine_logger as logger
import neteaseRoundScript.roundConst as roundConst
import neteaseRoundScript.battleServer.skill.roundSkill as roundSkill

class Skill(roundSkill.Skill):
	def ApplyOnTargets(self, targetList):
		result = []
		result.extend(self.ApplyHealOnTargets(targetList))
		result.extend(self.ApplyEffectOnTargets(targetList))
		return result
	# -----------------------------------------------------------------------------------------------------------------------------------------

