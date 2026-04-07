# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import lobbyGame.netgameApi as netgameApi
import lobby.netgameApi as lobbyNetgameApi
import apolloCommon.mongoPool as mongoPool
import modCommon.playerData as playerData
import npcManager
from awesomeScripts.modCommon.coroutineMgrGas import CoroutineMgr
from awesomeScripts.modCommon import modConfig
from awesomeScripts.modCommon.modConfig import TipType
from mod_log import logger
from awesomeScripts.mongoOperation import MongoOperation
from awesomeScripts.mysqlOperation import MysqlOperation

class DbType(object):
	#使用的数据库种类
	Mongo = 1
	Mysql = 2
 
class AwesomeServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logger.info('--------AwesomeServer====start!!!!!~~~~~')
		
		self.mMongoMgr = MongoOperation()
		self.mMysqlMgr = MysqlOperation()
		self.mDBType = 0
		#初始化连接池，mysql和mongo都支持。
		if self.mMongoMgr.InitMongoDb() == True:
			self.mDBType = DbType.Mongo
		elif self.mMysqlMgr.InitMysqlDb() == True:
			self.mDBType = DbType.Mysql
		else:
			logger.error("[DATABASE_ERROR]db not exist!")
			
		netgameApi.SetUseDatabaseSave(True, "awesome", 120)#定时存档，时间间隔是120s
		netgameApi.SetNonePlayerSaveMode(True)#若设置定时存档，则一定要执行本行代码
		#主城模式打开
		lobbyNetgameApi.SetCityMode(True)
		#设置为创造模式 0生存模式，1创造模式，2冒险模式
		netgameApi.SetLevelGameType(2)
		# 注册事件
		#触发时机：玩家加入时触发该事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		#创建玩家对象过程中，设置玩家出生位置时触发本事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerPlayerBornPosEvent,self, self.OnPlayerBornPosEvent)
		#保存玩家数据事件，玩家下线时也会触发该事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.savePlayerDataEvent,self, self.OnSavePlayerData)
		#游戏强制关闭过程中，玩家下线时会触发本事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.savePlayerDataOnShutDownEvent,self, self.OnSavePlayerData)
		#删除玩家时触发该事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		#游戏即将强制关闭触发本事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerWillShutDownEvent,self, self.OnServerWillShutDown)
		#entity被敲击事件
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.EntityBeKnockEvent, self, self.OnNpcTouched)
		#玩家发送聊天信息时触发
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent, self,self.OnServerChat)
		#监听客户端自定义事件，处理切服
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.OnSureGameEvent, self, self.OnSureGame)
		#监听客户端自定义事件，处理取消逻辑
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.OnCancelGameEvent, self, self.OnCancelGame)
		# 监听客户端自定义事件，处理玩家登录逻辑
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.LoginRequestEvent, self,self.OnLoginRequest)
		# 监听service自定义事件，处理处理匹配结果
		self.ListenForEvent(modConfig.Minecraft, modConfig.ServiceSystemName, modConfig.MatchResultEvent, self, self.OnMatchResultEvent)
		# 监听service自定义事件，获取匹配人数
		self.ListenForEvent(modConfig.Minecraft, modConfig.ServiceSystemName, modConfig.MatchNumEvent, self, self.OnMatchNum)
		# 监听master自定义事件，获取获取玩家数据
		self.ListenForEvent(modConfig.Minecraft, modConfig.MasterSystemName, modConfig.GetUserInfoRequestEvent, self, self.OnGetUserInfoRequest)
		# 监听master自定义事件，获取获取玩家数量
		self.ListenForEvent(modConfig.Minecraft, modConfig.MasterSystemName, modConfig.GetPlayerNumOfGameRequestEvent, self, self.OnGetPlayerNumOfGame)
		# 玩家对象管理
		self.mPlayerMap = {}
		#玩家player id到uid的映射
		self.mPlayerid2uid = {}
		#玩家uid到dimension的映射
		self.mUid2dimension = {}
		self.mNpcMgr = npcManager.NpcManager(self)
		
		self.mTransferPlayerQueue = []
		#玩家初始在dimension 4，需要创建dimension
		dimensionComp = self.CreateComponent(serverApi.GetLevelId(), "Minecraft", "dimension")
		dimensionComp.CreateDimension(4)

	def Destroy(self):
		'''
		服务器退出会调用Destroy函数，主要做清理工作
		'''
		# 注销事件
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.ServerPlayerBornPosEvent, self, self.OnPlayerBornPosEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.savePlayerDataEvent, self, self.OnSavePlayerData)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.savePlayerDataOnShutDownEvent, self, self.OnSavePlayerData)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.ServerWillShutDownEvent, self, self.OnServerWillShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
							modConfig.EntityBeKnockEvent, self, self.OnNpcTouched)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent,
							self, self.OnServerChat)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.OnSureGameEvent, self,
							self.OnSureGame)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.OnCancelGameEvent, self,
							self.OnCancelGame)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.ServiceSystemName, modConfig.MatchResultEvent, self,
							self.OnMatchResultEvent)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.ServiceSystemName, modConfig.MatchNumEvent, self,
							self.OnMatchNum)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.MasterSystemName, modConfig.GetUserInfoRequestEvent,
							self, self.OnGetUserInfoRequest)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.MasterSystemName,
							modConfig.GetPlayerNumOfGameRequestEvent, self, self.OnGetPlayerNumOfGame)
		self.UnListenForEvent(modConfig.Minecraft, modConfig.LobbyClientSystemName, modConfig.LoginRequestEvent, self,
							self.OnLoginRequest)
		# 清空内存数据
		self.mPlayerMap = {}
		self.mPlayerid2uid = {}
		self.mUid2dimension = {}
		# 结束数据库线程池，确保相关异步任务全部执行完。
		if self.mDBType == DbType.Mongo:
			self.mMongoMgr.Destroy()
		elif self.mDBType == DbType.Mysql:
			self.mMysqlMgr.Destroy()

	def OnServerChat(self, args):
		'''
		监听ServerChatEvent的回调函数
		'''
		#设置自己拥有op权限
		logger.info("OnServerChat {}".format(args))
		if args["message"] == "op":
			username = args.get('username', '')
			commandComp = self.CreateComponent(serverApi.GetLevelId(), modConfig.Minecraft, "command")
			commandComp.SetCommand('/op %s' % username)
	
	def OnAddServerPlayer(self, args):
		'''
		添加玩家的监听函数
		'''
		playerId = args.get('id','-1')
		uid = netgameApi.GetPlayerUid(playerId)
		self.mPlayerid2uid[playerId] = uid
		logger.info("player login.uid: %s",uid)
		self.QueryPlayerData(playerId, uid)
		
		
	def OnPlayerBornPosEvent(self, data):
		'''
		设置player出生点和dimension
		'''
		uid = data['userId']
		BORN_POS = (1395.664, 5.2, 51.441)#出生点
		data['posx'] = BORN_POS[0]
		data['posy'] = BORN_POS[1]
		data['posz'] = BORN_POS[2]
		data['dimensionId'] = 4 #设置dimension
		data['ret'] = True
		self.mUid2dimension[uid] = data['dimensionId']

	def QueryPlayerData(self, player_id, uid):
		'''
		db中获取玩家数据
		'''
		if self.mDBType == DbType.Mongo :
			self.mMongoMgr.QueryPlayerData(player_id,uid,lambda data: self.QuerySinglePlayerCallback(player_id, uid, data))
		elif self.mDBType == DbType.Mysql :
			self.mMysqlMgr.QueryPlayerData(player_id,uid,lambda data: self.QuerySinglePlayerCallback(player_id, uid, data))

	def QuerySinglePlayerCallback(self, player_id, uid, data):
		'''
		回调函数。若玩家存在，则注册玩家；否则记录玩家信息
		'''
		# 数据库请求返回时，玩家已经主动退出了
		if not self.mPlayerid2uid.has_key(player_id):
			return
		if not data: # 找不到玩家数据，注册一个新玩家
			nickname = netgameApi.GetPlayerNickname(player_id)
			data = playerData.PlayerData.getNewPlayerInfo(uid, nickname)
			self.InsertPlayerData(player_id, uid)
		#记录玩家数据
		player = playerData.PlayerData()
		if isinstance(data,tuple):
			data = player.changeMysqlTupleToPlayerDict(data)
		player.initPlayer(player_id, data)
		#刷新玩家登录事件
		player.refreshLoginTime()
		self.mPlayerMap[uid] = player

	def OnLoginRequest(self, data):
		'''
		玩家登录逻辑
		'''
		import lobbyGame.netgameApi as lobbyGameApi
		player_id = data['id']
		uid = lobbyGameApi.GetPlayerUid(player_id)
		CoroutineMgr.StartCoroutine(self._DoSendLoginResponseData(player_id, uid))

	def _DoSendLoginResponseData(self, player_id, uid):
		'''
		将玩家数据推送给客户端。若还没从db获取玩家数据，则延迟5帧再试
		'''
		if uid in self.mPlayerMap:
			player = self.mPlayerMap[uid]
			event_data = player.toSaveDict()
			event_data['player_id'] = player_id
			self.NotifyToClient(player_id, modConfig.LoginResponseEvent, event_data)
			return
		yield -5

	def InsertPlayerData(self, player_id, uid):
		'''
		把玩家数据插入db
		'''
		nickname = netgameApi.GetPlayerNickname(player_id)
		new_player_data = playerData.PlayerData.getNewPlayerInfo(uid, nickname)
		if self.mDBType == DbType.Mongo:
			self.mMongoMgr.InsertPlayerData(player_id,uid,new_player_data)
		elif self.mDBType == DbType.Mysql:
			self.mMysqlMgr.InsertPlayerData(player_id, uid, new_player_data)

	def Update(self):
		'''
		每帧执行。
		'''
		CoroutineMgr.Tick()

	def OnSavePlayerData(self, args):
		'''
		把玩家数据存档。这个函数一定要调用save_player_data_result函数，把存档状态告知引擎。
		'''
		uid = int(args["playerKey"])
		cpp_callback_idx = int(args["idx"])
		player_data = self.mPlayerMap.get(uid, None)
		if not player_data:
			#告知引擎，存档状态。注意传入回调函数id
			netgameApi.SavePlayerDataResult(cpp_callback_idx, True)
		def _SavePlayerCb(args):
			ret = args
			if ret:
				netgameApi.SavePlayerDataResult(cpp_callback_idx, True)
			else:
				netgameApi.SavePlayerDataResult(cpp_callback_idx, False)
		self.SavePlayerByUid(uid, _SavePlayerCb)

	def SavePlayerByUid(self, uid, cb = None):
		'''
		保存玩家数据
		'''
		player = self.mPlayerMap.get(uid, None)
		if not player:
			return
		player_dict = player.toSaveDict()
		if self.mDBType == DbType.Mongo:
			self.mMongoMgr.SavePlayerByUid(uid,player_dict,cb)
		elif self.mDBType == DbType.Mysql:
			self.mMysqlMgr.SavePlayerByUid(uid,player_dict,cb)

	def OnDelServerPlayer(self, args):
		'''
		清除玩家内存数据。
		'''
		logger.info("OnDelServerPlayer {}".format(args))
		playerId = args.get('id','-1')
		uid = self.mPlayerid2uid.get(playerId, None)
		logger.info("OnDelServerPlayer player uid=%s" % uid)
		if not uid:
			return
		del self.mPlayerid2uid[playerId]
		if uid in self.mPlayerMap:
			del self.mPlayerMap[uid]
		if uid in self.mUid2dimension:
			del self.mUid2dimension[uid]
		#玩家离线，把自己playerId在待传送队列里清掉
		if playerId in self.mTransferPlayerQueue:
			self.mTransferPlayerQueue.remove(playerId)
		#玩家离线，告诉server把自己从匹配队清掉
		request_data = {'uid': uid, 'player_id': playerId}
		self.RequestToService(modConfig.AwesomeMatch, modConfig.RequestMatchCancel, request_data)
		

	def OnServerWillShutDown(self, args):
		logger.info("OnServerWillShutDown {}".format(args))
		# 即将关机，先给所有还在线玩家挂一个存档任务
		for uid, player in self.mPlayerMap.iteritems():
			self.SavePlayerByUid(uid)
		# 同步完成所有还挂着的异步数据库操作
		if self.mDBType == DbType.Mongo:
			self.mMongoMgr.Destroy()
		elif self.mDBType == DbType.Mysql:
			self.mMysqlMgr.Destroy()

	def OnNpcTouched(self, args):
		'''
		点击npc回调函数。
		'''
		npc_entity_id = args['entityId']
		npc_data = self.mNpcMgr.GetNpcData(npc_entity_id)
		if not npc_data:
			return
		player_entity_id = args['srcId']
		uid = self.mPlayerid2uid[player_entity_id]
		if npc_data.name == 'gameA':
			logger.info("%s touch NPC gameA",player_entity_id)
			#请求gameA玩家人数
			request_data = {'game': 'gameA', 'player_id': player_entity_id,'uid': uid,'client_id':netgameApi.GetServerId()}
			self.NotifyToMaster(modConfig.GetPlayerNumOfGameEvent,request_data)
		elif npc_data.name == 'gameB':
			logger.info("%s touch NPC gameB",player_entity_id)
			#请求gameB玩家人数
			request_data = {'game': 'gameB', 'player_id': player_entity_id, 'uid': uid,
							'client_id': netgameApi.GetServerId()}
			self.NotifyToMaster(modConfig.GetPlayerNumOfGameEvent, request_data)
		elif npc_data.name == 'gameC':
			logger.info("%s touch NPC gameC",player_entity_id)
			# 请求gameC匹配队列人数
			request_data = {'uid': uid, 'player_id': player_entity_id, 'game': 'gameC'}
			self.RequestToService(modConfig.AwesomeMatch, modConfig.RequestMatchNum, request_data)
			
	def OnGetPlayerNumOfGame(self,args):
		'''
		告诉客户端，显示玩家数量的提示页面
		'''
		logger.info("OnGetPlayerNumOfGame {}".format(args))
		self.NotifyToClient(args['player_id'], modConfig.SureEnterGameEvent, args)
	
	def OnMatchNum(self,args):
		'''
		告诉客户端，显示匹配队列人数的提示页面
		'''
		logger.info("OnMatchNum {}".format(args))
		self.NotifyToClient(args['player_id'], modConfig.SureMatchGameEvent, args)
		
	def OnSureGame(self,args):
		'''
		切服逻辑，如果是gameA和gameB则直接传去对应服，如果是gameC则加入匹配队列
		:param args:
		:return:
		'''
		logger.info("OnSureGame {}".format(args))
		if args['game'] == "gameA":
			netgameApi.TransferToOtherServer(args['playerId'], "gameA")
		elif args['game'] == "gameB":
			netgameApi.TransferToOtherServer(args['playerId'], "gameB")
		elif args['game'] == "gameC":
			playerId = args['playerId']
			uid = self.mPlayerid2uid[playerId]
			levelcomp = self.CreateComponent(playerId, modConfig.Minecraft, "lv")
			playerLevel = levelcomp.GetPlayerLevel()
			if playerLevel >= 0:#大于0级才能匹配
				request_data = {'uid': uid, 'player_id': playerId,'game':args["game"]}
				self.RequestToService(modConfig.AwesomeMatch, modConfig.RequestMatch, request_data)
				tipData = {'tipType' : TipType.matching} #1匹配中
				self.NotifyToClient(playerId, modConfig.MatchResultTip, tipData)
			else:
				tipData = {'tipType': TipType.levelNotEnough} #0等级不够
				self.NotifyToClient(playerId, modConfig.MatchResultTip, tipData)
			
	def OnCancelGame(self,args):
		'''
		取消匹配，暂时只有gameC取消匹配的功能
		:return:
		'''
		if args['game'] == "gameC":
			playerId = args['playerId']
			uid = self.mPlayerid2uid[playerId]
			request_data = {'uid': uid, 'player_id': playerId,'game':args["game"]}
			self.RequestToService(modConfig.AwesomeMatch, modConfig.RequestMatchCancel, request_data)

	def OnMatchResultEvent(self, args):
		'''
		处理匹配结果。切到指定服务器。
		'''
		logger.info("OnMatchResultEvent {}".format(args))
		playerId = args['player_id']
		desc_game = args['desc_game']
		if args['game'] == 'gameC':
			#如果是gameC则延时1S传送
			tipData = {'tipType': TipType.toTransfer}  # 2 即将传送
			self.NotifyToClient(playerId, modConfig.MatchResultTip, tipData)
			self.mTransferPlayerQueue.append(playerId)
			CoroutineMgr.StartCoroutine(self.Transfer2Server(playerId, desc_game))
		
	def Transfer2Server(self,playerId,descGame):
		'''
		把玩家传送至对应的服
		:return:
		'''
		yield -30#延迟30帧，也即1s
		#判断玩家是否在待传送队列里，若玩家中途下线，则不作处理
		if playerId in self.mTransferPlayerQueue:
			logger.info("%s go to %s", playerId,descGame)
			netgameApi.TransferToOtherServerById(playerId, descGame)
			self.mTransferPlayerQueue.remove(playerId)
	
	def OnGetUserInfoRequest(self, args):
		'''
		获取玩家数据。
		'''
		uid = args['uid']
		client_id = args['client_id']
		player_data = self.mPlayerMap.get(uid, None)
		if not player_data:
			if self.mDBType == DbType.Mongo:
				self.mMongoMgr.QueryPlayerData(uid, uid,
											  lambda data: self._OnGetUserInfoRequestCb(client_id, data))
			elif self.mDBType == DbType.Mysql:
				self.mMysqlMgr.QueryPlayerData(uid, uid,
											  lambda data: self._OnGetUserInfoRequestCb(client_id, data))
		else:
			self._GetUserInfoResponse(client_id, player_data.toSaveDict())

	def _OnGetUserInfoRequestCb(self, client_id, record):
		'''
		回调函数，处理db操作结果，把玩家数据告知master。
		'''
		if record:
			player_data = playerData.PlayerData()
			if isinstance(record, tuple):
				record = player_data.changeMysqlTupleToPlayerDict(record)
			player_data.initPlayer(-1, record)
			self._GetUserInfoResponse(client_id, player_data.toSaveDict())
		else:
			self._GetUserInfoResponse(client_id, {})

	def _GetUserInfoResponse(self, client_id, player_info):
		'''
		玩家数据告知master。
		'''
		response_data = {'client_id' : client_id, 'user_info' : player_info}
		self.NotifyToMaster(modConfig.GetUserInfoResponseEvent, response_data)

