# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import neteaseDungeonScript.playerMgr as playerMgr
import neteaseDungeonScript.util as util
import lobbyGame.netgameApi as lobbyGameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import ujson as json

class DungeonGameSys(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.ServiceConnectEvent, self, self.OnServiceRegisterModule)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.DelServerPlayerEvent, self, self.DelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.ServerChatEvent, self, self.OnServerChat)
		self.mPlayMgr = playerMgr.PlayerMgr()

	def OnServiceRegisterModule(self, args):
		'''
		向service注册可用副本
		'''
		moduleName = args['modulename']
		if moduleName == dungeonConsts.ServiceModuleName:
			self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.RegisterGameDungeonsEvent, {})

	def OnAddServerPlayer(self, args):
		'''
		玩家登录到副本
		'''
		try:
			transferParam = args['transferParam']
			transData = json.loads(transferParam)
			dungeonId = transData['dungeonId']
		except:
			return
		print 'OnAddServerPlayer', args
		playerId = args['id']
		uid = args['uid']
		#告知service，玩家进入副本了
		joinDungeonData = {}
		joinDungeonData['uid'] = uid
		joinDungeonData['dungeonId'] = dungeonId
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.PlayerJoinDungeonEvent, joinDungeonData)
		#设置玩家出生点
		serverType = commonNetgameApi.GetServerType()
		oneGameDungeonData = util.GetOneGameDungeon(serverType, dungeonId)
		dungeonTypeData = oneGameDungeonData.mDungeonType
		bornPos = [dungeonTypeData.mBornPos[i] + oneGameDungeonData.mOffset[i] for i in xrange(3)]
		posComp = self.CreateComponent(playerId, "Minecraft", "pos")
		posComp.SetPos(tuple(bornPos))
		#记录玩家信息
		self.mPlayMgr.JoninDungeon(playerId, uid, dungeonTypeData.mType, dungeonId)
		#触发加入副本事件
		loginData = {}
		loginData['uid'] = uid
		loginData['dungeonId'] = dungeonId
		self.BroadcastEvent(dungeonConsts.PlayerLoginDungeonEvent, loginData)

	def DelServerPlayer(self, args):
		'''
		玩家离开游戏，处理离开副本逻辑
		'''
		print 'DelServerPlayer', args
		uid = args['uid']
		self.QuitDungeon(uid)

	def GetDungeonConfById(self, dungeonId):
		'''
		获取指定ID的副本类型及各项配置项
		'''
		serverType = commonNetgameApi.GetServerType()
		oneGameDungeonData = util.GetOneGameDungeon(serverType, dungeonId)
		return oneGameDungeonData

	def GetDungeonConfByPos(self, position):
		'''
		获取当前位置的副本类型及各项配置项
		'''
		serverType = commonNetgameApi.GetServerType()
		dungeonData = util.GetDungeonDataByPos(serverType, position)
		return dungeonData

	def GetDungeonOffsetByPos(self, position):
		'''
		获取当前所在副本区域的位置偏移
		'''
		serverType = commonNetgameApi.GetServerType()
		dungeonData = util.GetDungeonDataByPos(serverType, position)
		if not dungeonData:
			return (0, 0, 0)
		return dungeonData['offset']

	def QuitDungeon(self, uid):
		'''
		玩家退出副本。
		'''
		print 'QuitDungeon', uid
		playerDungeon = self.mPlayMgr.GetPlayerDungeon(uid)
		quitData = {}
		quitData['uid'] = uid
		quitData['dungeonId'] = playerDungeon.mDungeonId
		self.BroadcastEvent(dungeonConsts.PlayerLogoutDungeonEvent, quitData)
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.PlayerQuitDungeonEvent, quitData)
		self.mPlayMgr.QuitDungeon(uid)

	def ResetDungeon(self, dungeonId):
		'''
		重置副本，副本变为空闲状态，其他玩家可以进入副本。
		'''
		playerDungeonList = self.mPlayMgr.GetPlayerDungeonListByDungeonId(dungeonId)
		#将副本中玩家转到lobby
		for playerDungeon in playerDungeonList:
			lobbyGameApi.TransferToOtherServer(playerDungeon.mPlayerId, 'lobby')
		#告知service重置副本
		resetData = {}
		resetData['dungeonId'] = dungeonId
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.ResetDungeonEvent, resetData)

	def GetDungeonIdByUid(self, uid):
		'''
		获取玩家所在副本的ID
		'''
		dungeon = self.mPlayMgr.GetPlayerDungeon(uid)
		if not dungeon:
			return -1
		return dungeon.mDungeonId

	def GetPlayerUidsByDungeonId(self, dungeonId):
		return self.mPlayMgr.GetPlayerUidsByDungeonId(dungeonId)

	def OnServerChat(self, args):
		'''
		不同副本中的聊天互相不可见，同一副本内的玩家聊天互相可见
		'''
		playerId = args['playerId']
		uid = lobbyGameApi.GetPlayerUid(playerId)
		dungeonId = self.GetDungeonIdByUid(uid)
		playerDungeonLst = self.mPlayMgr.GetPlayerDungeonListByDungeonId(dungeonId)
		toPlayerIds = [info.mPlayerId for info in playerDungeonLst]
		if args['bChatById']:
			fromPlayerIds = args
			toPlayerIds = [id for id in toPlayerIds if id in fromPlayerIds]
		args['bChatById'] = True
		args['toPlayerIds'] = toPlayerIds

	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.ServiceConnectEvent, self, self.OnServiceRegisterModule)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.DelServerPlayerEvent, self, self.DelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							dungeonConsts.ServerChatEvent, self, self.OnServerChat)
		self.mPlayMgr = None