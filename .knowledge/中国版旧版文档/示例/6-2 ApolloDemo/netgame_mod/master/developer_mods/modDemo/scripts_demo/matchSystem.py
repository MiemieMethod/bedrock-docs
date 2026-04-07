# -*- coding: utf-8 -*-
import server.extraMasterApi as masterApi
MasterSystem = masterApi.GetMasterSystemCls()
import scripts_demo.matchPool as matchPool
'''
匹配逻辑。
demo展示了：
	master和game通信逻辑。
'''
class MatchSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		print 'init MatchSystem'
		#待匹配玩家pool
		self.matchingPool = matchPool.MatchingPool(self.onMatchingTimeout, self.onMatchSuccess)
		#匹配成功房间pool，等待分配房间
		self.matchOKPool = matchPool.MatchSuccessPool(self.onMatchSuccessTimeout, self.onSendCheckRequest,
			self.onCheckRoomFromGameSuccess, self.onCheckRoomFromGameFail)
		#成功分配玩家，战斗中房间pool
		self.playingPool = matchPool.PlayingPool()
		#【自定义事件，告知lobby玩家匹配状态】
		self.DefineEvent('PlayerMatchingStatus')
		#【自定义事件，向game核对房间是否可用，demo不会触发该事件】
		self.DefineEvent('CheckRoomRequestEvent')
		#【自定义事件，告知lobby匹配结果，demo不会触发该事件】
		self.DefineEvent('PlayerMatchingResult')
		#【自定义事件，积分发生变化事件，demo不会触发该事件】
		self.DefineEvent('ChangeScoreEvent')
		#【初始化空闲房间事件， demo不会触发该事件】
		self.ListenForEvent('idv', 'idvGameServer', 'InitServerRoomsEvent', self, self.initServerRooms)
		#【开始匹配事件】
		self.ListenForEvent('Minecraft', 'SampleServer', 'StartMatchingEvent', self, self.startMatching)
		#【取消匹配事件】
		self.ListenForEvent('Minecraft', 'SampleServer', 'CancelMatchEvent', self, self.cancelMatch)
		#【房间是否可用事件， demo不会触发该事件】
		self.ListenForEvent('idv', 'idvGameServer', 'CheckRoomResponseEvent', self, self.checkRoomResponse)
		#【结束战斗事件， demo不会触发该事件】
		self.ListenForEvent('idv', 'idvGameServer', 'EndBattleEvent', self, self.endBattle)
		#【服务器断开连接事件】
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'ServerDisconnectEvent',
		                    self, self.disconnectServer)
		#玩家登出事件
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'PlayerLogoutServerEvent',
	                        self, self.logoutServer)
		#test
		'''
		data = {}
		data['serverId'] = 1
		data['roomId'] = 2
		data['players'] = []
		player = {}
		player['id'] = 22
		player['nickname'] = 'nickname22'
		player['isWin'] = 1
		data['players'].append(player)
		self.endBattle(data)
		'''
	#服务器每帧执行。
	def Update(self):
		self.matchingPool.update()
		self.matchOKPool.update()
		self.playingPool.update()
	#取消匹配，从匹配池中删除玩家。
	def cancelMatch(self, data):
		id = data['id']
		serverId = data['serverId']
		self.matchingPool.delPlayer(id)
		self.notifyMatchStatusEvent(serverId, id, False, True, '')
	#初始空闲房间，相应game启动后，需要发送消息告知master空闲房间。
	def initServerRooms(self, data):
		print 'Matching:init server rooms.', data
		serverId = data['serverId']
		freeRooms = data['freeRooms']
		self.matchingPool.setFreeRooms(serverId, freeRooms)
	#玩家申请开始匹配。
	def startMatching(self, data):
		import time
		playerData = {}
		id = data['id']
		playerData['id'] = id
		playerData['lobbyId'] = data['serverId']
		playerData['nickname'] = "testname" + str(id)
		from scripts_demo.modCommon import MATCHING_TIMEOUT
		playerData['matchExpireTime'] = int(time.time()) + MATCHING_TIMEOUT
		if self.matchingPool.isInPool(id) or self.matchOKPool.isInPool(id):
			self.notifyMatchStatusEvent(playerData['lobbyId'], id, True, False, '不能重复匹配')
		else:
			self.matchingPool.addPlayer(playerData)
			self.notifyMatchStatusEvent(playerData['lobbyId'], id, True, True, '')
	#服务器断开连接，删除服务器相关房间。
	def disconnectServer(self, data):
		serverId = int(data['serverId'])
		self.matchingPool.clearByServerId(serverId)
		self.playingPool.clearByServerId(serverId)
	#玩家登出，将玩家从正匹配pool中删除。
	def logoutServer(self, data):
		id = data['serverId']
		self.matchingPool.delPlayer(id)
	#匹配超时
	def onMatchingTimeout(self, playerData):
		self.notifyPlayerMatchingResult(playerData['lobbyId'], -1, playerData['id'],
		    False, '匹配超时')
	#master与lobby通信。
	def notifyMatchStatusEvent(self, serverId, id, bStart, bSuc, reason):
		data = self.CreateEventData()
		data['id'] = id
		data['is_start'] = bStart
		data['suc'] =bSuc
		data['reason'] = reason
		self.NotifyToServerNode(serverId, 'PlayerMatchingStatus', data)
	#匹配超时回调。
	def onMatchSuccessTimeout(self, room):
		players = room.getPlayers()
		for playerData in players:
			self.notifyPlayerMatchingResult(playerData['lobbyId'], -1, playerData['id'],
			    False, '匹配超时')
	#匹配成功回调
	def onMatchSuccess(self, room):
		self.matchOKPool.addRooms(room)
	#核对房间请求
	def onSendCheckRequest(self, serverId, data):
		self.NotifyToServerNode(serverId, 'CheckRoomRequestEvent', data)

	def checkRoomResponse(self, data):
		roomId = data['roomId']
		status = data['status']
		self.matchOKPool.checkResponseFromGame(roomId, status)

	def onCheckRoomFromGameSuccess(self, room):
		players = room.getPlayers()
		for playerData in players:
			self.notifyPlayerMatchingResult(playerData['lobbyId'], room.getGameId(),
			    playerData['id'], True, '')
		self.playingPool.addRoom(room)

	def notifyPlayerMatchingResult(self, serverId, matchServerId, id, bSuc, reason):
		data = self.CreateEventData()
		data['serverId'] = matchServerId
		data['id'] = id
		data['suc'] = bSuc
		data['reason'] = reason
		self.NotifyToServerNode(serverId, 'PlayerMatchingResult', data)

	def onCheckRoomFromGameFail(self, room):
		players = room.getPlayers()
		for playerData in players:
			self.notifyPlayerMatchingResult(playerData['lobbyId'], -1, playerData['id'],
			    False, '创建房间失败')
	#结束战斗
	def endBattle(self, data):
		print 'endBattle.data:', data
		serverId = data['serverId']
		roomId = data['roomId']
		self.playingPool.popRoom(serverId, roomId)
		self.matchingPool.addOneFreeRoom(serverId, roomId)
		players = data['players']
		for playerData in players:
			data = self.CreateEventData()
			data['uid'] = playerData['id']
			data['nickname'] = playerData['nickname']
			data['score'] = 1 if playerData['isWin'] else 0
			self.BroadcastEvent('ChangeScoreEvent', data)

	def Destroy(self):
		print 'Destroy #########yyyyyyyyyyyyyyyyyyyyyyyyyyy#######MatchSystem################'
		self.UnListenForEvent('idv', 'idvGameServer', 'InitServerRoomsEvent', self, self.initServerRooms)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'StartMatchingEvent', self, self.startMatching)
		self.UnListenForEvent('Minecraft', 'SampleServer', 'CancelMatchEvent', self, self.cancelMatch)
		self.UnListenForEvent('idv', 'idvGameServer', 'CheckRoomResponseEvent', self, self.checkRoomResponse)
		self.UnListenForEvent('idv', 'idvGameServer', 'EndBattleEvent', self, self.endBattle)
		self.UnListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'ServerDisconnectEvent',
		                    self, self.disconnectServer)
		self.UnListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'PlayerLogoutServerEvent',
		                    self, self.logoutServer)