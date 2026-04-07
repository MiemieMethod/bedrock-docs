# -*- coding: utf-8 -*-
import server.extraMasterApi as masterApi
MasterSystem = masterApi.GetMasterSystemCls()
import netease_server.redispool as redispool
import master_api.login_net as login_net
import master_api.master_http as master_http
import  ujson as json
'''
功能：gm指令，登录顶号。
demo展示了：
	redis线程池使用方法。
	异步存档实例。
	注册gm指令。
'''
class ServerHandlerSys(MasterSystem):
	HTTP_CODE_SUCCESS = 1
	HTTP_CODE_FAIL = 2

	def __init__(self,namespace,systemName):
		MasterSystem.__init__(self,namespace,systemName)
		print 'init ServerHandlerSys'
		#【玩家登录事件】
		self.ListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'PlayerLoginServerEvent',
		                    self, self.onPlayerLoginServer)
		#【自定义事件，给lobb/game发公告事件】
		self.DefineEvent('AnnounceEvent')
		#注册gm指令，使用post方式，踢人gm指令。url:/kickout-user
		master_http.register_master_http('/kickout-user', self, self.kickoutUserCmd)#顶号
		#注册gm指令，使用post方式，公告gm指令。url:/broadcast-message
		master_http.register_master_http('/broadcast-message', self, self.broadcastMessage)  #公告

	def makeResponse(self, code, message = '', entity = None):
		response = {}
		response['code'] = code
		response['message'] = message
		response['entity'] = entity
		return json.dumps(response)

	def makeFailResponse(self, code, message):
		response = {}
		response['code'] = code
		response['message'] = message
		response['entity'] = None
		return json.dumps(response)
	'''
	公告gm指令。clientId是请求唯一id，返回一定要携带这个id，支持异步返回，通过clientID识别是哪个请求的返回。
	http server是只能顺序处理http请求，因此若前一个请求没返回会阻塞后面一个请求。
	服务端http请求超时时间为5s，若超过5s，会强制返回超时。
	requestBody是post请求的内容，是一个json字符串。
	一个请求实例：
	post请求
	http://123.456.789:9001/broadcast-message
	请求内容：
	{
		"message":"broadcast test"
	}
	返回:
	{
	    "message": "",
   	 	"code": 1,
    	"entity": null
	}
	'''
	def broadcastMessage(self, clientId, requestBody):
		request =  json.loads(requestBody)
		message = request.get('message', None)
		if message is None:
			response = self.makeFailResponse(ServerHandlerSys.HTTP_CODE_FAIL, 'Invalid Param.wrong message.')
			master_http.send_http_response(clientId, response)
		import master_api.server_manager as server_manager
		#获取所有同master建立连接的lobby/game的serverid列表。
		serveridLst = server_manager.get_connected_lobby_and_game_ids()
		broadcastData = self.CreateEventData()
		broadcastData['message'] = message
		for id in serveridLst:
			#给serverId为id的lobby/game发请求。
			self.NotifyToServerNode(id, "AnnounceEvent", broadcastData)
		#http的返回，返回是json格式。clientId与请求保持一样。
		master_http.send_http_response(clientId, self.makeResponse(self.HTTP_CODE_SUCCESS))

	#踢人gm指令
	def kickoutUserCmd(self, clientId, requestBody):
		import  ujson as json
		request =  json.loads(requestBody)
		neteaseId = request.get('neteaseId', -1)
		if neteaseId < 0:
			response = self.makeFailResponse(ServerHandlerSys.HTTP_CODE_FAIL, 'Invalid Param.wrong neteaseId.')
			master_http.send_http_response(clientId, response)
		key_player = "online_user_%d" % neteaseId
		master_http.send_http_response(clientId, self.makeResponse(ServerHandlerSys.HTTP_CODE_SUCCESS))
		#redis线程池。支持异步回调。在线程池中执行redis hgetall操作，这里获取redis key为key_player的值，主线程执行回调。record为查询结果。
		#回调函数最少有一个参数，它的最后一个参数表示执行结果，例如这里的record。
		#redis线程池执行错误会重试3次，若执行还是失败则返回None。
		#redis线程池，对于相同redis key的请求，会按照先后顺序处理。
		redispool.async_hgetall(key_player, lambda record: self.kickoutUserCmdCb(neteaseId, record))

	#kickoutUserCmd的回调。record为redis查询结果。
	#record为None，则表示执行错误。这里没考虑错误情况。
	def kickoutUserCmdCb(self, neteaseId, record):
		#若玩家在线，则开始顶号。
		if record:
			serverId = record.get('serverid', None)
			if serverId is None:
				return
			serverId = int(serverId)
			import master_api.server_manager as server_manager
			#master是否与server建立连接，可能服务器已经关闭了。
			if server_manager.is_connected_server(serverId):
				#将玩家顶下线。
				login_net.send_kickout_packet_for_duplicate_login(serverId, neteaseId)
	#玩家登录事件
	def onPlayerLoginServer(self, data):
		neteaseId = int(data['neteaseId'])
		proxyServerId = int(data['serverId'])
		key_player = "online_user_%d" % neteaseId
		#redis线程池，查询redis key为key_player的值。这里获取玩家在线信息
		redispool.async_hgetall(key_player, lambda record: self.getOnlineUserCb(proxyServerId, neteaseId, record))

	def getOnlineUserCb(self, proxyServerId, neteaseId, record):
		if record:
			#玩家确实在线，则开始顶号，
			#玩家进入lobby或game后，会把在线信息写入redis，对应key：online_user_%d + neteaseId
			#玩家离线，会将这个key删除。
			#获取所在服务器serverid。
			serverId = record.get('serverid', None)
			if serverId is None:
				#若在线信息不正确，完成登录，理论上不存在这种情况。
				login_net.login_server(proxyServerId, neteaseId)
				return
			serverId = int(serverId)
			import master_api.server_manager as server_manager
			#若被顶server与master建立了连接，则继续顶号。否则server可能崩溃了，则不管，继续登录。
			if server_manager.is_connected_server(serverId):
				#顶号。
				login_net.send_kickout_packet_for_duplicate_login(serverId, neteaseId)
			else:
				login_net.login_server(proxyServerId, neteaseId)
		else:
			#玩家不在线，则登录
			login_net.login_server(proxyServerId, neteaseId)

	def Destroy(self):
		print 'Destroy #########yyyyyyyyyyyyyyyyyyyyyyyyyyy#######ServerHandlerSys################'
		self.UnListenForEvent(masterApi.GetEngineNamespace(), masterApi.GetEngineSystemName(), 'PlayerLoginServerEvent',
		                    self, self.onPlayerLoginServer)
