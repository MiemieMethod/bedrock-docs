# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import neteaseFriendScript.friendManager as friendManager
import neteaseFriendScript.playerManager as playerManager
import neteaseFriendScript.chatManager as chatManager
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import neteaseFriendScript.friendCommon.httpApi as httpApi
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi

class FriendServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")

		#modConfig = commonNetgameApi.GetModJsonConfig('neteaseFriendScript')
		
		self.mFriendManager = friendManager.FriendManager(self)
		self.mChatManager = chatManager.ChatManager(self)
		self.mPlayerManager = playerManager.PlayerManager(self)
		
		self.mFriendDbManager = friendDbManager.FriendDbManager()
		self.mPlayerDbManager = playerDbManager.PlayerDbManager()
		self.mChatRecordDbManager = chatRecordDbManager.ChatDbManager()
		
		self.mHttpApi = httpApi.HttpApi()

		self.Init()
		self.InitRedis()
		
		# self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChatEvent)
		self.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, 'ClientUiInitFinished', self, self.OnClientUiInitFinished)

	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseFriendScript')
		self.mChatRecordDbManager.RECORD_MAX_NUM = self.modConfig.get("RECORD_MAX_NUM")
		import lobbyGame.netgameApi as lobbyGameApi
		commonConfig = lobbyGameApi.GetCommonConfig()
		self.mGameId = commonConfig.get("gameId", 0)
		self.mGameKey = commonConfig.get("gameKey", '').encode('utf-8')
		self.mHttpApi.SetGameKey(self.mGameKey)
		
	def OnClientUiInitFinished(self, args):
		"""
		client初始化完成，发送的第一条给server的消息，server返回配置信息，以及对应玩家的uid给client
		"""
		playerId = args.get("entityId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		self.NotifyToClient(playerId, "ModConfigResponseFromServerEvent", self.modConfig)
		self.NotifyToClient(playerId, "TellYourPlayerUidEvent", {"playerId":playerId, "playerUid":playerUid})
		

	def InitRedis(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			redisPool.InitDB(30)
		except:
			logout.error("start_Friend fail when init redisPool")
			return False
		return True
	
	#=============================对外接口===============================================
	def OpenFriendListUI(self, args):
		"""
		通知指定uid对应的client，显示好友主界面
		"""
		selfUid = args.get("selfUid")
		if selfUid is None:
			return
		entityId = netgameApi.GetPlayerIdByUid(selfUid)
		self.NotifyToClient(entityId, "OpenFriendList", {})
		
	def CreateTempChat(self, args, callback = None):
		"""
		创建一个临时聊天，需要传入发起者的uid(selfUid)，和目标玩家uid(friendUid)
		"""
		self.mFriendManager.RealCreateTempChat(args, callback)
		
	def ServerAddFriend(self, args):
		"""
		发出一个建立好友关系的申请，需要传入发起者的uid(selfUid)或playerId(entityId)，目标玩家的uid(friendUid)，以及附言(message)
		"""
		self.mFriendManager.ServerDoAddFriend(args)
	
	def ServerAddBlack(self, args):
		"""
		把目标玩家加入到自己的黑名单中，需要传入发起者的uid(selfUid)或playerId(entityId)，目标玩家的uid(friendUid)
		"""
		self.mFriendManager.ServerDoAddBlack(args)
		
	def OnServerChatEvent(self, args):
		"""
		打开好友界面，调试用界面入口
		"""
		playerId = args.get("playerId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		logout.info("OnServerChatEvent", playerUid)
		dict = {}
		self.NotifyToClient(playerId, "OpenFriendList", {})
   
		



		
		
	