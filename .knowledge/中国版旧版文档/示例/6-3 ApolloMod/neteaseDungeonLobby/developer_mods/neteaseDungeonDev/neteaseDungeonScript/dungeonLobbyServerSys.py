# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import neteaseDungeonScript.util as util
import lobbyGame.netgameApi as lobbyGameApi
import ujson as json
import logout

class DungeonLobbySys(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
		# 					self, self.OnServerChat)
		self.ListenForEvent(dungeonConsts.ModNameSpace, dungeonConsts.ServiceSystemName,
							dungeonConsts.PlayerTransferToDungeonEvent, self, self.PlayerTransferToDungeon)
		# self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
		# 					self, self.Test)
		self.DefineEvent(dungeonConsts.DungeonFullMessageEvent)

	# def OnServerChat(self, args):
	# 	'''
	# 	for test
	# 	'''
	# 	playerId = args['playerId']
	# 	msg = args['message']
	# 	uid = lobbyGameApi.GetPlayerUid(playerId)
	# 	if 'A' == msg:
	# 		self.TransferToDungeon(playerId, 'dungeonA')
	# 	elif 'C' == msg:
	# 		def _TestCb1(uid, serverId, dungenoId):
	# 			print '_TestCb1', uid, serverId, dungenoId
	# 		self.GetPreDungeonInfoByUid(uid, _TestCb1)
	# 	elif 'D' == msg:
	# 		def _TestCb2(bCanJoin):
	# 			print '_TestCb2', bCanJoin
	# 		self.TransferToDungeonById(uid, 3000000, 0, _TestCb2)
	# 	else:
	# 		self.TransferToDungeon(playerId, 'dungeonB')

	# def Test(self, args):
	# 	playerId =args['id']
	# 	fullMessageData = {}
	# 	fullMessageData['dungeonName'] = 'yfgtest'
	# 	print 'yfgteste', playerId, dungeonConsts.DungeonFullMessageEvent, fullMessageData
	# 	self.NotifyToClient(playerId, dungeonConsts.DungeonFullMessageEvent, fullMessageData)

	def AskAndLockDungeonByType(self, dungeonType, uidList, overtime, cbFunc):
		'''
		申请并锁定一个指定类型的副本，并通过回调函数返回结果, 
		cbFunc的参数有2个，第1个参数是int类型，表示对应副本所在的serverid（返回负数代表没有找到可用的副本），
		第2个参数是int类型，表示对应副本大的唯一ID（返回负数代表没有找到可用的副本）
		'''
		data = {
			"uidList": uidList,
			"overtime": overtime,
			"dungeonType": dungeonType,
		}
		def AskAndLockGungeonCallback(suc, args):
			if not suc:
				cbFunc(True, -1, -1)
				return
			descServerId = args['serverId']
			descDungeonId = args['dungeonId']
			cbFunc(args['suc'], descServerId, descDungeonId)
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.AskAndLockForDungeonByTypeEvent, data, AskAndLockGungeonCallback)

	def ReleaseLockedDungeon(self, serverId, dungeonId, cbFunc=None):
		'''
		释放一个通过【AskAndLockDungeonByType】申请的副本，
		cbFunc的参数有2个，第1个参数是bool类型，表示是否找到符合条件的副本；
		第2个参数也是bool类型，表示是否成功删除副本的锁定（当副本中有残留玩家时，删除会失败）
		'''
		data = {
			"serverId": serverId,
			"dungeonId": dungeonId,
		}
		if cbFunc:
			def ReleaseLockedDungeonCallback(suc, args):
				if not suc:
					cbFunc(False, False)
					return
				find = args['find']
				suc = args['suc']
				cbFunc(find, suc)
			self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.UnlockDungeonEvent, data, ReleaseLockedDungeonCallback)
		else:
			self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.UnlockDungeonEvent, data)

	def PlayerTransferToDungeon(self, args):
		'''
		玩家开始切服到副本
		'''
		uid = args['uid']
		descServerId = args['descServerId']
		descDungeonId = args['descDungeonId']
		playerId = lobbyGameApi.GetPlayerIdByUid(uid)
		if playerId:
			transParam = {'dungeonId' : descDungeonId}
			lobbyGameApi.TransferToOtherServerById(playerId, descServerId, json.dumps(transParam))

	def TransferToDungeon(self, playerId, dungeonType):
		'''
		请求切服到某个副本
		'''
		data = {}
		uid = lobbyGameApi.GetPlayerUid(playerId)
		data['uid'] = uid
		data['dungeonType'] = dungeonType
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.TransferToDungeonByDungeonTypeEvent, data,
							lambda suc, args: self.OnTransferDungeonCb(playerId, uid, dungeonType, suc, args), 2)

	def OnTransferDungeonCb(self, playerId, uid, dungeonType, suc, args):
		'''
		开始切服到副本中
		'''
		if not suc:
			logout.error('TransferToDungeon callback error!uid:%s, dungeon type:%s'% (uid, dungeonType))
			return
		descServerId = args['serverId']
		descDungeonId = args['dungeonId']
		if descServerId < 0:
			fullMessageData = {}
			dungeonTypData = util.GetDungeonTypeData(dungeonType)
			if not dungeonTypData:
				print 'OnTransferDungeonCb.no dungeon type found.dungeon type:', dungeonType
				return
			fullMessageData['dungeonName'] = dungeonTypData.mName
			self.NotifyToClient(playerId, dungeonConsts.DungeonFullMessageEvent, fullMessageData)
			return
		transParam = {'dungeonId': descDungeonId}
		lobbyGameApi.TransferToOtherServerById(playerId, descServerId, json.dumps(transParam))

	def GetPreDungeonInfoByUid(self, uid, cb):
		'''
		获取玩家上一次进入副本信息。
		'''
		def _GetDungeonInfoCb(suc, args, uid, callback):
			gameId = -1
			dungeonId = -1
			if suc:
				gameId = args['serverId']
				dungeonId = args['dungeonId']
			callback(uid, gameId, dungeonId)
		eventData = {'uid' : uid}
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.GetPreDungeonInfoEvent, eventData,
							lambda suc, args: _GetDungeonInfoCb(suc, args, uid, cb), 2)

	def TransferToDungeonById(self, uid, serverId, dungeonId, cb):
		'''
		玩家切服到指定副本
		'''
		applyData = {}
		applyData['uid'] = uid
		applyData['serverId'] = serverId
		applyData['dungeonId'] = dungeonId
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.ApplyToDungeonIdEvent, applyData,
							lambda suc, args: self._TransToDungeonByIdCb(suc, args, uid, serverId, dungeonId, cb), 2)

	def _TransToDungeonByIdCb(self, suc, args, uid, serverId, dungeonId, callback):
		if not suc:
			callback(False)
			return
		bCanJoin = args['isCanJoin']
		if not bCanJoin:
			callback(False)
			return
		callback(True)
		playerId = lobbyGameApi.GetPlayerIdByUid(uid)
		if playerId:
			transParam = {'dungeonId': dungeonId}
			lobbyGameApi.TransferToOtherServerById(playerId, serverId, json.dumps(transParam))

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
							self, self.OnServerChat)