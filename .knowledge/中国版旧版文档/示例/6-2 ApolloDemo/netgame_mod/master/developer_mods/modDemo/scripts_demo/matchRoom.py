# -*- coding:utf-8 -*-
'''
匹配用的一个房间
'''
class MatchRoom(object):

	def __init__(self, gameId, roomId):
		import time
		self.players = []#房间里面的所有玩家
		self.roomId = roomId#房间id
		self.gameId = gameId#匹配到的服务器id
		self.bSendCheck =False#是否需要发送请求，核对房间是否可用。
		from scripts_demo.modCommon import MATCHSUCCESS_TIMEOUT
		self.matchSuccessExpireTime = int(time.time()) + MATCHSUCCESS_TIMEOUT#核对房间的超时时间

	def addPlayer(self, playerData):
		self.players.append(playerData)

	def isInRoom(self, id):
		for data in self.players:
			if data['id'] == id:
				return True
		return False

	def getGameId(self):
		return self.gameId

	def getRoomId(self):
		return self.roomId

	def getSendCheckFlag(self):
		return self.bSendCheck

	def setSendCheckFlag(self, flag):
		self.bSendCheck = flag

	def getPlayers(self):
		return self.players

	def isExpire(self):
		import time
		return time.time() > self.matchSuccessExpireTime