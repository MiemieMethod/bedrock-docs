# -*- coding: utf-8 -*-
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import neteaseDungeonScript.util as util
import server.extraServiceApi as serviceApi
import neteaseDungeonScript.timermanager as timermanager
import logout
import time

class Dungeon(object):
	def __init__(self, id, data):
		self.mId = id
		self.mDungenData = data#副本数据
		self.mPlayerList = []#正在副本玩家
		self.mOfflienUidList = []#离开副本玩家
		#正在切服玩家
		self.mTransUidList = []#正准备切服玩家
		# 此副本被申请锁定了
		self.mAskForLock = False
		self.mAskForLockOvertime = 0

	def SetBeAskForLock(self, overtime):
		self.mAskForLock = True 
		self.mAskForLockOvertime = int(time.time() + overtime)
	
	def SetBeUnlock(self):
		self.mAskForLock = False
		self.mAskForLockOvertime = 0
	
	def IsBeAskForLock(self):
		if self.mAskForLock and time.time() < self.mAskForLockOvertime:
			return True 
		return False

	def GetDungeonData(self):
		return self.mDungenData

	def GetDungeonTypeData(self):
		return self.mDungenData.mDungeonType

	def IsOccupied(self):
		'''
		副本被强制锁定，或者
		副本至少有一个人进入过，则表示被占用。正在切服玩家
		'''
		if self.IsBeAskForLock():
			return True 
		return self.mPlayerList or self.mOfflienUidList or self.mTransUidList

	def IsFull(self):
		'''
		是否可以进入新玩家
		'''
		if self.IsBeAskForLock():
			return True 
		typeData = self.mDungenData.mDungeonType
		return typeData.mMaxNum <= len(self.mPlayerList) + len(self.mOfflienUidList) + len(self.mTransUidList)

	def IsQuitDungeon(self, uid):
		'''
		是否进入过副本
		'''
		return uid in self.mOfflienUidList

	def AddTransPlayer(self, uid):
		if uid not in self.mTransUidList:
			self.mTransUidList.append(uid)

	def DelTransPlayer(self, uid):
		if uid in self.mTransUidList:
			self.mTransUidList.remove(uid)

	def Join(self, uid):
		'''
		加入副本。需要删除切服玩家信息
		'''
		self.DelTransPlayer(uid)
		if uid not in self.mPlayerList:
			self.mPlayerList.append(uid)
		if uid in self.mOfflienUidList:
			self.mOfflienUidList.remove(uid)

	def Quit(self, uid):
		'''
		退出副本。需要删除在副本玩家信息。
		'''
		if uid in self.mPlayerList:
			logout.info('QuitDungeon.uid:%s, dungeon id:%s' % (uid, self.mId))
			self.mPlayerList.remove(uid)
			if uid not in self.mOfflienUidList:
				self.mOfflienUidList.append(uid)

	def Reset(self):
		self.mAskForLock = False
		self.mAskForLockOvertime = 0
		self.mOfflienUidList = []
		self.mPlayerList = []
		self.mUid2TransTime = {}

	def GetJoinedUidList(self):
		return self.mPlayerList + self.mOfflienUidList

class GameDungeon(object):
	'''
	管理一个game的游戏副本
	'''
	def __init__(self, id):
		self.mId2Dungeon = {}
		self.mDungeonType2Ids = {}
		self.mGameId = id
		self.mGameType = util.GetServerTypeByServerId(id)

	def AddDungeon(self, dungeon):
		'''
		新增一个副本
		'''
		id = dungeon.mId
		self.mId2Dungeon[id] = dungeon
		dungeonTypeData = dungeon.GetDungeonTypeData()
		dungeonType = dungeonTypeData.mType
		ids = self.mDungeonType2Ids.get(dungeonType, [])
		ids.append(id)
		self.mDungeonType2Ids[dungeonType] = ids

	def GetDungeon(self, id):
		return self.mId2Dungeon.get(id, None)

	def GetDungeonNumInfo(self, dungeonType):
		'''
		获取空闲和占用副本数量
		'''
		freeNum = 0
		occupiedNum = 0
		ids = self.mDungeonType2Ids.get(dungeonType, [])
		for id in ids:
			dungeon = self.mId2Dungeon[id]
			if dungeon.IsOccupied():
				occupiedNum += 1
			else:
				freeNum += 1
		return (freeNum, occupiedNum)

	def GetGameType(self):
		return self.mGameType

	def ApplyNewGameDungeon(self, uid, dungeonType):
		'''
		申请一个新副本，不能进入前一次进入副本。
		'''
		ids = self.mDungeonType2Ids.get(dungeonType, [])
		for id in ids:
			dungeon = self.mId2Dungeon[id]
			if dungeon.IsQuitDungeon(uid):
				continue
			if not dungeon.IsFull():
				dungeon.AddTransPlayer(uid)
				return id
		return None
	
	def AskAndLockNewGameDungeon(self, dungeonType, overtime):
		'''
		申请并锁定一个新副本
		'''
		ids = self.mDungeonType2Ids.get(dungeonType, [])
		for id in ids:
			dungeon = self.mId2Dungeon[id]
			if dungeon.IsOccupied():
				continue
			dungeon.SetBeAskForLock(overtime)
			return id
		return None

class DungeonManager(object):
	'''
	管理所有的游戏副本
	'''
	def __init__(self, serviceSys):
		import weakref
		self.mGameId2Dungeon = {}
		self.mDungeonType2GameIds = {}
		self.mUid2TransInfo = {}#uid => (gameId, dungeonId, transferTime)
		self.mUid2PreDungeonInfo = {}#uid => (gameId, dungeonId) 玩家进入过的副本记录，这些副本还没结束
		self.mUid2LockedDungeonInfo = {} #uid => (gameId, dungeonId) 玩家申请锁定的副本记录
		self.mLockedDungeon2Uids = {} #(gameId, dungeonId) => uidList 玩家申请锁定的副本记录
		self.mGameStatusMap = {}
		self.mSystem = weakref.proxy(serviceSys)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.RegisterGameDungeonsEvent,
									self.OnRegisterGameDungeons)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.PlayerJoinDungeonEvent,
									self.OnPlayerJoinDungeon)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.PlayerQuitDungeonEvent,
									self.OnPlayerQuitDungeon)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.TransferToDungeonByDungeonTypeEvent,
									self.OnTransferToDungeonByDungeonType)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.AskAndLockForDungeonByTypeEvent,
									self.OnAskAndLockForDungeonByTypeEvent)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.UnlockDungeonEvent,
									self.OnUnlockDungeonEvent)
		self.mSystem.ListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(),
									dungeonConsts.UpdateServerStatusEvent, self, self.OnUpdateServerStatus)
		self.mSystem.ListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(),
							dungeonConsts.ServerDisconnectEvent, self, self.OnServerDisconnect)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.HttpRequestJoinDungeonEvent,
									self.OnHttpRequestJoinDungeon)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.HttpGetDungeonNumInfoEvent,
									self.OnHttpHttpGetDungeonNumInfo)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.ResetDungeonEvent,
									self.OnResetDungeon)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.GetPreDungeonInfoEvent,
									self.OnGetPreDungeonInfo)
		self.mSystem.RegisterRpcMethod(dungeonConsts.ServiceModuleName, dungeonConsts.ApplyToDungeonIdEvent,
									self.OnApplyToDungeonId)
		self.mTransferGcTimer = timermanager.timerManager.addRepeatTimer(30, self.OnGcTransfer)
		self.Init()

	def Init(self):
		'''
		所有服可用状态
		'''
		import service.netgameApi as netServiceApi
		conf = netServiceApi.GetCommonConfig()
		serverList = conf['serverlist']
		for serverInfo in serverList:
			serverId = serverInfo['serverid']
			self.mGameStatusMap[serverId] = 1

	def GetGameDungeonById(self, gameId, dungeonId):
		if gameId not in self.mGameId2Dungeon:
			return None
		gameDungeon = self.mGameId2Dungeon[gameId]
		return gameDungeon.GetDungeon(dungeonId)

	def OnGcTransfer(self):
		'''
		删除超时transfer玩家的信息
		'''
		for uid in self.mUid2TransInfo:
			gameId, dungeonId, transferTime = self.mUid2TransInfo[uid]
			if time.time() >= transferTime + dungeonConsts.DungeonTransferTimeout:
				self.RemoveTransferUser(uid)
				break

	def RemoveTransferUser(self, uid):
		'''
		删除正在transfer玩家的信息
		'''
		print 'RemoveTransferUser.uid:', uid
		if uid not in self.mUid2TransInfo:
			return
		gameId, dungeonId, transferTime = self.mUid2TransInfo[uid]
		del self.mUid2TransInfo[uid]
		dungeon = self.GetGameDungeonById(gameId, dungeonId)
		if dungeon:
			dungeon.DelTransPlayer(uid)

	def OnRegisterGameDungeons(self, serverId, callbackId, args):
		'''
		game向service注册副本
		'''
		print 'OnRegisterGameDungeons', serverId, args
		serverType = util.GetServerTypeByServerId(serverId)
		gameDungeonMap = util.dungeonData.mType2GameDungeonDataList
		dungeonDataList = gameDungeonMap.get(serverType, [])
		dungeonNum = len(dungeonDataList)
		for id in xrange(dungeonNum):
			data = dungeonDataList[id]
			dungeon = Dungeon(id, data)
			self.AddDungeon(serverId, dungeon)
	
	def SaveLockedDungeonInfo(self, uidList, descGameId, descDungeonId):
		for uid in uidList:
			self.mUid2LockedDungeonInfo[uid] = (descGameId, descDungeonId)
		self.mLockedDungeon2Uids[(descGameId, descDungeonId)] = uidList

	def ReleaseLockedDungeonInfo(self, descGameId, descDungeonId):
		uidList = self.mLockedDungeon2Uids.get((descGameId, descDungeonId), None)
		if uidList is None:
			return
		del self.mLockedDungeon2Uids[(descGameId, descDungeonId)]
		for uid in uidList:
			if uid in self.mUid2LockedDungeonInfo:
				del self.mUid2LockedDungeonInfo[uid]

	def CheckUidLockedInDungeon(self, uidList):
		for uid in uidList:
			dungeonData = self.mUid2LockedDungeonInfo.get(uid, None)
			if dungeonData is None:
				continue
			descGameId, descDungeonId = dungeonData
			dungeon = self.GetGameDungeonById(descGameId, descDungeonId)
			if dungeon and dungeon.IsOccupied():
				return True 
		return False

	def OnAskAndLockForDungeonByTypeEvent(self, serverId, callbackId, args):
		'''
		申请并锁定一个指定类型的副本
		'''
		dungeonType = args['dungeonType']
		overtime = args.get('overtime', 600)
		uidList = args.get('uidList', [])
		isLocked = self.CheckUidLockedInDungeon(uidList)
		if isLocked:
			responseData = {
				"dungeonType": dungeonType,
				"suc": False,
				"serverId": -1,
				"dungeonId": -1,
			}
		else:
			descGameId, descDungeonId = self.AskAndLockNewGameDungeon(dungeonType, overtime)
			responseData = {
				"dungeonType": dungeonType,
				"suc": True,
				"serverId": descGameId,
				"dungeonId": descDungeonId,
			}
			if descDungeonId >= 0 and descDungeonId >= 0:
				self.SaveLockedDungeonInfo(uidList, descGameId, descDungeonId)
		self.mSystem.ResponseToServer(serverId, callbackId, responseData)

	def AskAndLockNewGameDungeon(self, dungeonType, overtime):
		# 选择可用副本
		gameIds = self.mDungeonType2GameIds.get(dungeonType, [])
		for gameId in gameIds:
			#game是就绪的
			status = self.mGameStatusMap.get(gameId, None)
			if status != 1:
				continue
			gameDungeon = self.mGameId2Dungeon[gameId]
			dungeonId = gameDungeon.AskAndLockNewGameDungeon(dungeonType, overtime)
			if dungeonId is None:
				continue
			return (gameId, dungeonId)
		return (-1, -1)

	def OnUnlockDungeonEvent(self, serverId, callbackId, args):
		'''
		解锁一个通过【AskAndLockForDungeonByTypeEvent】申请的副本
		'''
		descServerId = args['serverId']
		descDungeonId = args['dungeonId']
		dungeon = self.GetGameDungeonById(descServerId, descDungeonId)
		find = False
		suc = False
		if dungeon and dungeon.IsBeAskForLock():
			find = True
			uids = dungeon.GetJoinedUidList()
			if not uids:
				suc = True
				dungeon.Reset()
		self.ReleaseLockedDungeonInfo(descServerId, descDungeonId)
		responseData = {}
		responseData['serverId'] = descServerId
		responseData['dungeonId'] = descDungeonId
		responseData['find'] = find
		responseData['suc'] = suc
		self.mSystem.ResponseToServer(serverId, callbackId, responseData)

	def OnTransferToDungeonByDungeonType(self, serverId, callbackId, args):
		'''
		转移到指定类型副本中
		'''
		print 'OnTransferToDungeonByDungeonType', serverId, args
		uid = args['uid']
		dungeonType = args['dungeonType']
		descGameId, descDungeonId = self.ApplyNewDungeon(uid, dungeonType)
		responseData = {}
		responseData['dungeonType'] = dungeonType
		responseData['serverId'] = descGameId
		responseData['dungeonId'] = descDungeonId
		self.mSystem.ResponseToServer(serverId, callbackId, responseData)

	def ApplyNewDungeon(self, uid, dungeonType):
		'''
		申请新的可用副本
		:return: (serverId, dungeonId)
		'''
		#是否还在切服中
		if uid in self.mUid2TransInfo:
			transTime = self.mUid2TransInfo[uid][2]
			if time.time() < transTime + dungeonConsts.ReDungeonTransferTime:
				logout.warning('OnTransferToDungeonByDungeonType error!frequent requests, please wait.')
				return (-1, -1)
			#删除上次切服记录
			self.RemoveTransferUser(uid)
		#选择可用副本
		gameIds = self.mDungeonType2GameIds.get(dungeonType, [])
		descDungeonId = -1
		descGameId = -1
		for gameId in gameIds:
			#game是就绪的
			if gameId in self.mGameStatusMap and 1 == self.mGameStatusMap[gameId]:
				gameDungeon = self.mGameId2Dungeon[gameId]
				dungeonId = gameDungeon.ApplyNewGameDungeon(uid, dungeonType)
				if dungeonId is None:
					continue
				descDungeonId = dungeonId
				descGameId = gameId
				self.mUid2TransInfo[uid] = (descGameId, descDungeonId, time.time())
				break
		return (descGameId, descDungeonId)

	def AddDungeon(self, gameId, dungeon):
		if gameId not in self.mGameId2Dungeon:
			self.mGameId2Dungeon[gameId] = GameDungeon(gameId)
		gameDungeon = self.mGameId2Dungeon[gameId]
		gameDungeon.AddDungeon(dungeon)
		typeData = dungeon.mDungenData.mDungeonType
		dungeonType = typeData.mType
		if dungeonType not in self.mDungeonType2GameIds:
			self.mDungeonType2GameIds[dungeonType] = []
		gameIds = self.mDungeonType2GameIds[dungeonType]
		if gameId not in gameIds:
			gameIds.append(gameId)
		logout.info('AddDungeon.game id:%s, dungeon id:%s, dungeon type:%s' % (gameId, dungeon.mId, dungeonType))
		delUids = []
		for uid, v in self.mUid2TransInfo.iteritems():
			serverId, dungeonId, transferTime = v
			if serverId == gameId:
				delUids.append(uid)
		for uid in delUids:
			del self.mUid2TransInfo[uid]

	def DelDungeonByGameId(self, gameId):
		print 'DelDungeonByGameId', gameId
		#删除玩家副本信息
		if gameId in self.mGameId2Dungeon:
			del self.mGameId2Dungeon[gameId]
		for k in self.mDungeonType2GameIds.iterkeys():
			gameIds = self.mDungeonType2GameIds[k]
			if id in gameIds:
				gameIds.remove(id)
		delUids = []
		#清空切服记录
		for uid, v in self.mUid2TransInfo.iteritems():
			serverId, dungeonId, transferTime = v
			if serverId == gameId:
				delUids.append(uid)
		for uid in delUids:
			del self.mUid2TransInfo[uid]
		#清除玩家进入副本历史记录
		delUids = []
		for uid in self.mUid2PreDungeonInfo:
			srcId, tmpId = self.mUid2PreDungeonInfo[uid]
			if srcId == gameId:
				delUids.append(uid)
		for uid in delUids:
			del self.mUid2PreDungeonInfo[uid]

	def OnUpdateServerStatus(self, args):
		'''
		清除已下架副本信息
		'''
		self.mGameStatusMap = {}
		for k, v in args.iteritems():
			id = int(k)
			status = int(v)
			self.mGameStatusMap[id] = status

	def OnServerDisconnect(self, args):
		'''
		清除断开连接服务器副本信息
		'''
		print 'OnServerDisconnect', args
		serverId = args['serverId']
		self.DelDungeonByGameId(serverId)

	def OnPlayerJoinDungeon(self, serverId, callbackId, args):
		'''
		game告知service，玩家已经加入到副本了
		'''
		print 'OnPlayerJoinDungeon', serverId, args
		uid = args['uid']
		dungeonId = args['dungeonId']
		if uid in self.mUid2TransInfo:
			gameId, dungeonId, tmpTime = self.mUid2TransInfo[uid]
			dungeon = self.GetGameDungeonById(gameId, dungeonId)
			dungeon.Join(uid)
			del self.mUid2TransInfo[uid]
		self.mUid2PreDungeonInfo[uid] = (serverId, dungeonId)

	def OnPlayerQuitDungeon(self, serverId, callbackId, args):
		'''
		game告知service，玩家退出了副本。其他玩家可以申请加入该副本。
		'''
		print 'OnPlayerQuitDungeon', serverId, args
		uid = args['uid']
		dungeonId = args['dungeonId']
		dungeon = self.GetGameDungeonById(serverId, dungeonId)
		if not dungeon:
			return
		dungeon.Quit(uid)

	def OnHttpRequestJoinDungeon(self, serverId, callbackId, args):
		'''
		请求进入副本。
		'''
		print 'OnHttpRequestJoinDungeon', serverId, args
		uid = args['uid']
		dungeonType = args['dungeonType']
		lobbyServerId = args['serverId']
		descGameId, descDungeonId = self.ApplyNewDungeon(uid, dungeonType)
		#告知lobby中玩家切服
		if descGameId > 0:
			transData = {}
			transData['uid'] = uid
			transData['descServerId'] = descGameId
			transData['descDungeonId'] = descDungeonId
			self.mSystem.NotifyToServerNode(lobbyServerId, dungeonConsts.PlayerTransferToDungeonEvent, transData)
		#http执行结果返回给master
		entityData = {}
		if descGameId > 0:
			entityData['code'] = dungeonConsts.SuccessCode
			entityData['message'] = ""
			resEntity = {}
			resEntity['gameId'] = descGameId
			resEntity['dungeonId'] = descDungeonId
			entityData['entity'] = resEntity
		else:
			entityData['code'] = dungeonConsts.FailCode
			entityData['message'] = "no free dungeon"
			entityData['entity'] = ''
		self.mSystem.ResponseToServer(serverId, callbackId, entityData)

	def OnHttpHttpGetDungeonNumInfo(self, serverId, callbackId, args):
		'''
		查询某个副本类型当前的占用数量和闲置数量
		'''
		print 'OnHttpHttpGetDungeonNumInfo', serverId, args
		dungeonType = args['dungeonType']
		gameIds = self.mDungeonType2GameIds.get(dungeonType, [])
		freeNum = 0
		occupiedNum = 0
		for gameId in gameIds:
			gameDungeon = self.mGameId2Dungeon.get(gameId, None)
			if not gameDungeon:
				continue
			free, occupied = gameDungeon.GetDungeonNumInfo(dungeonType)
			freeNum += free
			occupiedNum += occupied
		#http执行结果返回给master
		entityData = {}
		entityData['code'] = dungeonConsts.SuccessCode
		entityData['message'] = ""
		resEntity = {}
		resEntity['free'] = freeNum
		resEntity['occupied'] = occupiedNum
		entityData['entity'] = resEntity
		self.mSystem.ResponseToServer(serverId, callbackId, entityData)

	def OnResetDungeon(self, serverId, callbackId, args):
		'''
		重置副本，副本变为可用状态
		'''
		print 'OnResetDungeon', serverId, args
		dungeonId = args['dungeonId']
		dungeon = self.GetGameDungeonById(serverId, dungeonId)
		self.ReleaseLockedDungeonInfo(serverId, dungeonId)
		if dungeon:
			uids = dungeon.GetJoinedUidList()
			#清除历史记录
			for uid in uids:
				if uid in self.mUid2PreDungeonInfo:
					preGame, preDungeon = self.mUid2PreDungeonInfo[uid]
					if preGame == serverId and  preDungeon == dungeonId:
						del self.mUid2PreDungeonInfo[uid]
			dungeon.Reset()

	def OnGetPreDungeonInfo(self, serverId, callbackId, args):
		'''
		获取玩家上一次进入副本信息，要求上一次副本战斗还未结束。若上次战斗不存在或结束，则返回dungeonId 为-1
		'''
		uid = args['uid']
		gameId, dungeonId = self.mUid2PreDungeonInfo.get(uid, (-1, -1))
		dungeonId = {'serverId' : gameId, 'dungeonId' : dungeonId, 'uid' : uid}
		self.mSystem.ResponseToServer(serverId, callbackId, dungeonId)

	def OnApplyToDungeonId(self, serverId, callbackId, args):
		'''
		申请进入某副本
		'''
		uid = args['uid']
		gameId = args['serverId']
		dungeonId = args['dungeonId']
		dungeon = self.GetGameDungeonById(gameId, dungeonId)
		resultData = {'isCanJoin' : False}
		#服务是可用的且副本是存在的
		if gameId in self.mGameStatusMap and 1 == self.mGameStatusMap[gameId] and dungeon:
			if dungeon.IsQuitDungeon(uid):
				# 不用添加到dungeon的切服队列中，否则会多占用一个名额
				resultData['isCanJoin'] = True
				self.mUid2TransInfo[uid] = (gameId, dungeonId, time.time())
			elif not dungeon.IsFull():
				resultData['isCanJoin'] = True
				self.mUid2TransInfo[uid] = (gameId, dungeonId, time.time())
				dungeon.AddTransPlayer(uid)
		self.mSystem.ResponseToServer(serverId, callbackId, resultData)

	def Destroy(self):
		if self.mTransferGcTimer:
			timermanager.timerManager.delTimer(self.OnGcTransfer)
			self.mTransferGcTimer = None
		self.mSystem.UnListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(),
									  dungeonConsts.UpdateServerStatusEvent, self, self.OnUpdateServerStatus)
		self.mSystem.UnListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(),
									  dungeonConsts.ServerDisconnectEvent, self, self.OnServerDisconnect)
		self.mSystem = None