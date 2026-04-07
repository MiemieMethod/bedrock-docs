# -*- coding:utf-8 -*-
'''
匹配池
'''
class BasePool(object):
	def update(self):
		pass
#所有待匹配的玩家
class MatchingPool(BasePool):
	def __init__(self, onTimeout, onSuccess):
		self.freeRoomMap = {}
		self.players = []
		self.onTimeout = onTimeout
		self.onSuccess = onSuccess

	def isInPool(self, id):
		for data in self.players:
			if data['id'] == id:
				return True
		return False

	def addOneFreeRoom(self, serverId, room):
		if serverId not in self.freeRoomMap:
			self.freeRoomMap[serverId] = []
		if room not in self.freeRoomMap[serverId]:
			print 'Add one room.serverId:', serverId, ',roomId',room
			self.freeRoomMap[serverId].append(room)

	def setFreeRooms(self, serverId, rooms):
		print 'Add new romms.serverid:', serverId, ',rooms:', rooms
		self.freeRoomMap[serverId] = rooms

	def addPlayer(self, playerData):
		id = playerData['id']
		for data in self.players:
			if data['id'] == id:
				return
		self.players.append(playerData)

	def clearByServerId(self, serverId):
		if serverId in  self.freeRoomMap:
			del self.freeRoomMap[serverId]
		self.players = [data for data in self.players if data['lobbyId'] != serverId]

	def delPlayer(self, id):
		for idx, data in enumerate(self.players):
			if data['id'] == id:
				del self.players[idx]
				break

	def processTimeout(self):
		import time
		cnt = 0
		for idx, playerData in enumerate(self.players):
			if time.time() > playerData['matchExpireTime']:
				self.onTimeout(playerData)
				self.players[idx] = None
				cnt = cnt + 1
		for i in xrange(cnt):
			self.players.remove(None)

	def getFreeRoom(self):
		if not self.freeRoomMap:
			return (None, None)
		for serverId in self.freeRoomMap:
			if self.freeRoomMap[serverId]:
				roomId = self.freeRoomMap[serverId][0]
				del self.freeRoomMap[serverId][0]
				return (serverId, roomId)
		return (None, None)

	def generateRoom(self, serverId, roomId):
		from scripts_demo.matchRoom import MatchRoom
		room = MatchRoom(serverId, roomId)
		from scripts_demo.modCommon import MATCH_PLAYER_NUM
		for i in xrange(MATCH_PLAYER_NUM):
			room.addPlayer(self.players[0])
			del self.players[0]
		return room

	def match(self):
		from scripts_demo.modCommon import MATCH_PLAYER_NUM
		if len(self.players) < MATCH_PLAYER_NUM:
			return
		serverId, roomId = self.getFreeRoom()
		if roomId is None:
			return
		room = self.generateRoom(serverId, roomId)
		self.onSuccess(room)

	def update(self):
		self.processTimeout()
		self.match()
#匹配成功，等待分配房间的room的pool
class MatchSuccessPool(BasePool):
	def __init__(self, timeoutFunc, sendCheck, checkRoomSuccess, checkRoomFail):
		self.rooms = []
		self.onTimeout = timeoutFunc
		self.onSendCheckRequest = sendCheck
		self.onCheckSuccess= checkRoomSuccess
		self.onCheckFail = checkRoomFail

	def isInPool(self, id):
		for room in self.rooms:
			if room.isInRoom(id):
				return  True
		return False

	def addRooms(self, room):
		self.rooms.append(room)

	def processTimeout(self):
		cnt = 0
		for idx, room in enumerate(self.rooms):
			if room.isExpire():
				self.onTimeout(room)
				self.rooms[idx] = None
				cnt = cnt + 1
		for i in xrange(cnt):
			self.rooms.remove(None)

	def sendcheckGameRequest(self):
		for room in self.rooms:
			if room.getSendCheckFlag():
				continue
			data = {}

			data['roomId'] = room.getRoomId()
			lst = []
			players = room.getPlayers()
			for one in players:
				playerData = {}
				playerData['id'] = one['id']
				playerData['nickname'] = one['nickname']
				lst.append(playerData)
				data['players'] = lst
			self.onSendCheckRequest(room.getGameId(), data)
			room.setSendCheckFlag(True)

	def checkResponseFromGame(self, roomId, status):
		checkRoom = None
		for idx,room in enumerate(self.rooms):
			if room.getRoomId() == roomId:
				checkRoom = room
				del self.rooms[idx]
				break
		if checkRoom is None:
			return
		from scripts_demo.modCommon import CHECK_ROOM_STATUS
		if CHECK_ROOM_STATUS.FAIL == status:
			self.onCheckFail(checkRoom)
		else:
			self.onCheckSuccess(checkRoom)

	def update(self):
		self.processTimeout()
		self.sendcheckGameRequest()
#已经在房间中，战斗中room的pool
class PlayingPool(BasePool):
	def __init__(self):
		self.rooms = []

	def clearByServerId(self, serverId):
		cnt = 0
		for idx, room in enumerate(self.rooms):
			if room.getGameId() == serverId:
				self.rooms[idx] = None
				cnt = cnt + 1
		for i in xrange(cnt):
			self.rooms.remove(None)

	def addRoom(self, room):
		self.rooms.append(room)

	def popRoom(self, serverId, roomId):
		retRoom = None
		for idx, room in enumerate(self.rooms):
			if room.getGameId() == serverId and room.getRoomId() == roomId:
				retRoom = room
				del self.rooms[idx]
				break
		return  retRoom

	def update(self):
		pass
