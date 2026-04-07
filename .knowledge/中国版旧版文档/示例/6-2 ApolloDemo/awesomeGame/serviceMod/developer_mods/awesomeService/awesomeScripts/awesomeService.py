# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
from awesomeScripts.modCommon import modConfig
from mod_log import logger
import service.serviceConf as serviceConf

ServiceSystem = serviceApi.GetServiceSystemCls()
class EServerStatus:
	NO_EXIST = -1
	OK = 1
	STOP = 2
	PREPARE = 3

class AwesomeService(ServiceSystem):

	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		print 'init AwesomeService'
		self.mFrameCnt = 0
		self.mPlayerServer = {} #玩家对应的serverid
		self.mGameCMatchingPlayer = []#gameC的匹配玩家
		self.mActiveGameServerIds = [] #可用game列表
		self.mGameStatus = {}#serverid => server status.server status:1, 表示可用，其他不能分配。
		#lobby/game/proxy状态发生变化时触发，用于保存服务器状态
		self.ListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(), modConfig.UpdateServerStatusEvent, self, self.OnUpdateServerStatusEvent)
		#注册service接口
		self.RegisterRpcMethod(modConfig.AwesomeMatch, modConfig.RequestMatch, self.OnRequestMatch)
		self.RegisterRpcMethod(modConfig.AwesomeMatch, modConfig.RequestMatchCancel, self.OnRequestMatchCancel)
		self.RegisterRpcMethod(modConfig.AwesomeMatch, modConfig.RequestMatchNum, self.OnRequestMatchNum)

	def OnRequestMatchCancel(self,serverId, callbackId,args):
		'''
		取消匹配
		'''
		logger.info("OnRequestMatchCancel {}".format(args))
		player_id = args["player_id"]
		if player_id in self.mGameCMatchingPlayer:
			self.mGameCMatchingPlayer.remove(player_id)

	def OnRequestMatchNum(self,serverId, callbackId, args):
		'''
		返回匹配队列人数
		'''
		logger.info("OnRequestMatchNum {}".format(args))
		resultData = {'uid': args["uid"], 'player_id': args["player_id"],'playernum':len(self.mGameCMatchingPlayer),"game": args["game"]}
		self.NotifyToServerNode(serverId, modConfig.MatchNumEvent, resultData)
	
	def OnRequestMatch(self, server_id, callback_id, args):
		'''
		请求匹配进入gameC的游戏
		'''
		logger.info("OnRequestMatch {}".format(args))
		player_id = args['player_id']
		self.mPlayerServer[player_id] = server_id
		#如果已经在匹配队列，则不加入匹配队列
		if player_id in self.mGameCMatchingPlayer:
			return
		else:
			logger.info("%s matching",player_id)
			self.mGameCMatchingPlayer.append(player_id)
	
	def GameCMatch(self):
		'''
		检查匹配队列，匹配成功，清空匹配队列
		'''
		if not self.mGameCMatchingPlayer:
			return
		descGame = -1
		if len(self.mGameCMatchingPlayer) >=2:
			descGame = self.MatchAlgorithm()
		if descGame == -1:
			return
		for i in range(len(self.mGameCMatchingPlayer)):
			playerId = self.mGameCMatchingPlayer[i]
			self.NotifyToServerNode(self.mPlayerServer[playerId], modConfig.MatchResultEvent, {'player_id': playerId,'desc_game':desc_game,'game':'gameC'})
		self.mGameCMatchingPlayer = []#清空匹配队列
		
	def Update(self):
		self.mFrameCnt += 1
		if self.mFrameCnt % 10 == 0:#10帧匹配一次
			self.GameCMatch()
		
	def MatchAlgorithm(self):
		'''
		匹配算法
		'''
		serverid = -1
		serverlistConf = serviceConf.netgameConf['serverlist']
		for serverConf in serverlistConf:
			if serverConf['type'] == "gameC":
				serverid = serverConf['serverid']
				break
		return serverid

	def OnUpdateServerStatusEvent(self, args):
		'''
		记录服务器状态
		'''
		logger.info("OnUpdateServerStatusEvent {}".format(args))
		self.mGameStatus = {}
		self.mActiveGameServerIds = []
		for server_id, status in args.iteritems():
			id = int(server_id)
			int_status = int(status)
			self.mGameStatus[id] = int_status
			if int_status == EServerStatus.OK:
				self.mActiveGameServerIds.append(id)

	def Destroy(self):
		self.UnListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(), modConfig.UpdateServerStatusEvent, self, self.OnUpdateServerStatusEvent)