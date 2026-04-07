# -*- coding: utf-8 -*-

import neteaseAddupScript.addupConsts as addupConsts

class Player(object):
	def __init__(self, playerId):
		super(Player, self).__init__()
		self.mPlayerId = playerId
		self.mUid = None
		self.mAddupInfo = None
	
	def OnServerReady(self, uid):
		self.mUid = uid
	
	def OnUpdateAddupInfo(self, addupInfo):
		self.mAddupInfo = addupInfo
	
	def GetAddupInfoByKey(self, actKey):
		return self.mAddupInfo.get(actKey, {})