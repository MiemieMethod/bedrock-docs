# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import server.extraServerApi as serverApi
import apolloCommon.redisPool as redisPool
import json


class PlayerManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		#playerId和playerUid之间的对应关系
		self.mPlayerId2PlayerUid = {}
		
		# self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		#                     friendConsts.FriendsRefreshFromClientEvent, self, self.OnFriendsRefreshFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'ClientFriendStateRequestEvent', self, self.OnClientFriendStateRequestEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           'QueryPlayerDataFromClient', self, self.OnQueryPlayerDataFromClient)
		
		self.system.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent',
		                    self, self.OnPlayerLogin)
		self.system.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DelServerPlayerEvent',
		                    self, self.OnPlayerLogout)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,friendConsts.UpdatePlayerDataFromServiceEvent, self,
		                           self.OnUpdatePlayerDataFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,friendConsts.FriendStateResponseFromServiceEvent, self,
		                           self.OnFriendStateResponseFromServiceEvent)
	
	def OnQueryPlayerDataFromClient(self, args):
		"""
		client请求指定uid的玩家基本信息（昵称、头像等）
		"""
		entityId = args.get("id")
		uid = args.get("uid")
		def QueryPlayerDataCb(playerData):
			self.system.NotifyToClient(entityId, "UpdatePlayerDataFromServer", playerData)
		self.system.mPlayerDbManager.QueryPlayerData(uid, True, QueryPlayerDataCb)
		
	def OnUpdatePlayerDataFromServiceEvent(self, args):
		"""
		来自service的，更新指定玩家基本信息（昵称、头像等）的事件，转发给client
		"""
		logout.info("OnUpdatePlayerDataFromServiceEvent", args)
		changeUid = args.get("changeUid")
		selfUid = args.get("selfUid")
		#state = args.get("state")
		needChangeClient = args.get("needChangeClient", False)
		
		def OnQueryPlayerDataCb(playerData):
			#self.system.mPlayerDbManager.getPlayerCaches(changeUid).SetOnline(state)
			if needChangeClient == True and playerData is not None:
				entityId = netgameApi.GetPlayerIdByUid(selfUid)
				self.system.NotifyToClient(entityId, "UpdatePlayerDataFromServer", playerData)
		self.system.mPlayerDbManager.QueryPlayerData(changeUid, False, OnQueryPlayerDataCb)
		
	def OnFriendStateResponseFromServiceEvent(self, args):
		"""
		来自service的，玩家在线状态修改的事件（已经不再发送了，玩家上线下线时会主动推送事件给对应的client）
		"""
		logout.info("OnFriendStateResponseFromServiceEvent", args)
		changeUid = args.get("changeUid")
		selfUid = args.get("selfUid")
		state = args.get("state")
		def OnQueryPlayerDataCb(playerData):
			self.system.mPlayerDbManager.getPlayerCaches(changeUid).SetOnline(state)
			#args = uid, state
		# TODO 通知客户端修改？
		self.system.mPlayerDbManager.QueryPlayerData(changeUid, False, OnQueryPlayerDataCb)
		
	
	# def OnFriendsRefreshFromClientEvent(self, args):
	# 	'''
	# 	客户端请求获取player信息
	# 	'''
	# 	logout.info("OnFriendsRefreshFromClientEvent", args)
	# 	playerId = args["entityId"]
	# 	playerUid = netgameApi.GetPlayerUid(playerId)
	#
	# 	def GetFriendShipCb(friends, args):
	# 		logout.info("OnFriendsRefreshFromClientEvent, GetFriendShipCb", friends)
	# 		data = self.system.CreateEventData()
	# 		data['friends'] = friends
	# 		self.system.NotifyToClient(playerId, "", data)
	#
	# 	def GetFriendBlackCb(friends, args):
	# 		logout.info("OnFriendsRefreshFromClientEvent, GetFriendBlackCb", friends)
	# 		data = self.system.CreateEventData()
	# 		data['black'] = friends
	# 		self.system.NotifyToClient(playerId, "", data)
	#
	# 	def GetFriendRequestCb(friends, args):
	# 		logout.info("OnFriendsRefreshFromClientEvent, GetFriendRequestCb", friends)
	# 		data = self.system.CreateEventData()
	# 		data['friend_request'] = friends
	# 		self.system.NotifyToClient(playerId, "", data)
	#
	# 	self.system.mFriendDbManager.ServerGetFriendShip(playerUid, False, GetFriendShipCb, args)
	# 	self.system.mFriendDbManager.ServerGetFriendBlack(playerUid, False, GetFriendBlackCb, args)
	# 	self.system.mFriendDbManager.ServerGetFriendRequest(playerUid, False, GetFriendRequestCb, args)
	
	def OnPlayerLogin(self, args):
		"""
		玩家上线，通知service（主要是首次登录游戏时，会创建此玩家的基本信息记录），推送上线事件给在线好友的client
		"""
		playerId = args.get('id', '-1')
		playerUid = netgameApi.GetPlayerUid(playerId)
		self.mPlayerId2PlayerUid[playerId] = playerUid
		self.setFriendState(playerUid, friendConsts.PlayerState.online)
		self.system.mFriendManager.mNeedSyncRNFriendsUids.append(playerUid)
		# 名字
		nickName = netgameApi.GetPlayerNickname(playerId)
		data = self.system.CreateEventData()
		data['uid'] = playerUid
		data['nickName'] = nickName
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.AddPlayerFromServerEvent, data)
	
	def OnPlayerLogout(self, args):
		"""
		玩家离线，通知service（离线后，临时好友关系会被销毁），推送离线事件给在线好友的client
		"""
		playerId = args.get('id', '-1')
		playerUid = self.mPlayerId2PlayerUid.get(playerId)
		self.mPlayerId2PlayerUid.pop(playerId)
		self.setFriendState(playerUid, friendConsts.PlayerState.offline)
		if playerUid in self.system.mFriendManager.mNeedSyncRNFriendsUids:
			self.system.mFriendManager.mNeedSyncRNFriendsUids.remove(playerUid)
		# 名字
		nickName = netgameApi.GetPlayerNickname(playerId)
		data = self.system.CreateEventData()
		data['uid'] = playerUid
		data['nickName'] = nickName
		print "OnPlayerLogout", data
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.DelPlayerFromServerEvent, args)
		
	def setFriendState(self, uid, state):
		"""
		修改玩家在线状态，并推送给好友
		"""
		key = "netease_friend_state_%d" % uid
		data = {'uid': uid, 'state': state}
		redisPool.AsyncSet(key, json.dumps(data), lambda ret: self.setFriendStateCallback(uid, state))
	
	def setFriendStateCallback(self, uid, state):
		args = uid, state
		self.system.mFriendDbManager.ServerGetFriendShip(uid, True, self.NotifyFriendUpdateState, args)
		
	def NotifyFriendUpdateState(self, friendData, args):
		logout.info("NotifyFriendUpdateState", friendData, args)
		uid, state = args
		redata = self.system.CreateEventData()
		redata['friendState'] = {uid: state}
		def GetPlayersOnlineCb(args):
			for data in args:
				proxyId = data.get("proxyId")
				uid = data.get("uid")
				if proxyId:
					self.system.RemoteNotifyToClient(uid, proxyId, "FriendStateResponseEvent", redata)
		commonNetgameApi.GetOnlineServerInfoOfMultiPlayers(friendData, GetPlayersOnlineCb)
	
	def getFriendsState(self, uids, callback):
		keys = [("netease_friend_state_%d" % uid) for uid in uids]
		if len(keys) == 0:
			callback([])
			return
		redisPool.AsyncMget(keys, callback)
	
	def OnClientFriendStateRequestEvent(self, args):
		"""
		client批量请求uid列表中，玩家的在线状态
		"""
		self.getFriendsState(args['uids'], lambda state_list: self.ClientFriendStateRequestCallback(state_list, args))
		
	def ClientFriendStateRequestCallback(self, state_list, args):
		logout.verbose('ClientFriendStateRequestCallback', state_list, args)

		data = self.system.CreateEventData()
		data['friendState'] = {}
		if state_list is not None:
			for state_data_str in state_list:
				if state_data_str:
					try:
						state_data = json.loads(state_data_str)
						data['friendState'][state_data['uid']] = state_data['state']
					except:
						uid = args["uids"][state_list.index(state_data_str)]
						self.setFriendState(uid, friendConsts.PlayerState.offline)
		self.system.NotifyToClient(args["entityId"], "FriendStateResponseEvent", data)
		