# -*- coding: utf-8 -*-

import server.extraMasterApi as masterApi
MasterSystem = masterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import master.masterConf as masterConf
import master.serverManager as serverManager
from awesomeScripts.modCommon import modConfig
import apolloCommon.redisPool as redisPool
from mod_log import logger

class AwesomeMaster(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		logger.info('init AwesomeMaster')
		#初始化redis连接池
		redisPool.InitDB(30)
		# 注册gm指令
		masterHttp.RegisterMasterHttp('/get-user-info', self, self.OnGetUserInfo)
		#监听lobby服务器事件，用于返回http请求
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.GetUserInfoResponseEvent, self, self.OnGetUserInfoResponse)
		# 监听lobby服务器事件，请求获取玩家数量
		self.ListenForEvent(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.GetPlayerNumOfGameEvent, self, self.GetPlayerNumOfGame)
		
	def GetPlayerNumOfGame(self,args):
		'''
		请求获取服务器人数
		'''
		serverlistConf = masterConf.netgameConf['serverlist']
		print "OnGetPlayerNumOfGameResponse",args
		checkServeridList = []
		for serverConf in serverlistConf:
			if serverConf['type'] == args["game"]:
				serverid = serverConf['serverid']
				checkServeridList.append(serverid)
		playernum = 0
		for serverid in checkServeridList:
			playernum += serverManager.GetOnlineNumByServerId(serverid)
		request_data = {'game': args["game"], 'playernum': playernum,'player_id':args["player_id"]}
		self.NotifyToServerNode(args["client_id"], modConfig.GetPlayerNumOfGameRequestEvent, request_data)
		

	def OnGetUserInfo(self, client_id, request_body):
		'''
		获取gm指令
		'''
		import ujson as json
		request = json.loads(request_body)
		uid = request['uid']
		redis_key_player = "online_user_%d" % uid
		#获取玩家在线状态
		redisPool.AsyncHgetall(redis_key_player, lambda record: self._GetUserInfoCb(client_id, uid, record))

	def _GetUserInfoCb(self, client_id, uid, record):
		'''
		回调函数。获取目标lobby，向lobby请求在线人数。
		'''
		serverid = None
		serverlistConf = masterConf.netgameConf['serverlist']
		if record:
			#获取玩家所在目标服务器，若玩家在game中，则随机从一个lobby获取在线人数。
			serverid = record.get('serverid', None)
			tmpServerConf = masterConf.serverListMap.get(serverid, None)
			if not tmpServerConf or tmpServerConf['type'] != 'lobby':
				serverid = None
		if not serverid:
			for serverConf in serverlistConf:
				#服务器可用且是lobby
				if serverConf['type'] == 'lobby' and serverManager.IsValidServer(serverConf['serverid']):
					serverid = serverConf['serverid']
					break
		if not serverid:
			response = self.makeFailResponse(masterHttp.HTTP_CODE_FAIL, 'no valid lobby.')
			masterHttp.SendHttpResponse(client_id, response)
			return
		request_data = {'uid' : uid, 'client_id' : client_id}
		self.NotifyToServerNode(serverid, modConfig.GetUserInfoRequestEvent, request_data)

	def OnGetUserInfoResponse(self, args):
		'''
		接收玩家数据，返回http请求。
		'''
		client_id = args['client_id']
		entity = args['user_info']
		response = self.makeResponse(masterHttp.HTTP_CODE_SUCCESS, '', entity)
		masterHttp.SendHttpResponse(client_id, response)
