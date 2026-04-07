# -*- coding: utf-8 -*-

import random
from mod_log import engine_logger as logger

import neteaseRoundScript.roundConst as roundConst

class ServerPlayer(object):
	def __init__(self, playerId, uid):
		super(ServerPlayer, self).__init__()
		self.mPlayerId = playerId
		self.mUid = uid
		self.mClientReady = False
	
	def SetClientReady(self):
		self.mClientReady = True
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	def GetBattleMobs(self):
		base = ["neteaseRound:yohko", "neteaseRound:yohko", "neteaseRound:yohko", "neteaseRound:yuki", "neteaseRound:yuki", "neteaseRound:yuki"]
		random.shuffle(base)
		return base[:5]
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	# ---------------------------------------------------------------------------------------------------------------------------------------------
	

	
		
		




