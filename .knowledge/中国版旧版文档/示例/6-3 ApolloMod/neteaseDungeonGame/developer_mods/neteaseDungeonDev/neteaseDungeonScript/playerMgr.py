# -*- coding: utf-8 -*-
class PlayerDungeon(object):
	def __init__(self, playerId, uid, dungeonType, dungeonId):
		self.mUid = uid
		self.mDungeonId = dungeonId
		self.mPlayerId = playerId
		self.mDungeonType = dungeonType

class PlayerMgr(object):
	'''
	管理副本中玩家
	'''
	def __init__(self):
		self.mPlayers = {} #uid => PlayerDungeon

	def JoninDungeon(self, playerId, uid, dungenType ,dungeonId):
		player = PlayerDungeon(playerId, uid, dungenType, dungeonId)
		self.mPlayers[uid] = player

	def GetPlayerDungeon(self, uid):
		return self.mPlayers.get(uid, None)

	def QuitDungeon(self, uid):
		if uid in self.mPlayers:
			del self.mPlayers[uid]

	def GetPlayerUidsByDungeonId(self, dungeonId):
		uids = []
		for player in self.mPlayers.itervalues():
			if player.mDungeonId == dungeonId:
				uids.append(player.mUid)
		return uids

	def GetPlayerDungeonListByDungeonId(self, dungeonId):
		lst = []
		for player in self.mPlayers.itervalues():
			if player.mDungeonId == dungeonId:
				lst.append(player)
		return lst