# -*- coding: utf-8 -*-

import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import logout
import master.masterHttp as masterHttp
import authConsts as authConsts
#import netease_server.redispool as redispool
import apolloCommon.redisPool as redisPool
import json
from mysqlOperation import MysqlOperation
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi

class ServerOpType(object):
	DEOP = 2  # 删除玩家管理员身份
	OP = 1  # 添加玩家管理员身份

class AuthMasterSystem(MasterSystem):
	"""
	该mod的master类
	用于管理玩家权限
	对外提供http接口
	详见readme.txt了解如何使用
	"""
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		print '====init AuthMasterSystem=====',namespace,systemName
		self.mysqlMgr = MysqlOperation()
		self.mGroupNames = {} #分组名字列表 {"0":"normal","1":"vip","2":"op"}
		masterHttp.RegisterMasterHttp("/change-player-group", self, self.HttpChangePlayerGroup)
		masterHttp.RegisterMasterHttp("/op-player", self, self.doOpPlayer)
		self.ListenForEvent(authConsts.ModNameSpace, authConsts.ServerSystemName,
		                    'OpCommandEvent', self, self.OnOpCommand)
		self.Init()

	def OnOpCommand(self, args):
		logout.info('OnOpCommand.args:%s' % args)
		import master.netgameApi as netMasterApi
		import apolloCommon.launcherApi as launcherApi
		command = args['op']
		if authConsts.BAN_COMMAND == command:
			def _ban(response):
				if response and 0 == response['code']:
					netMasterApi.BanUser(response['entity']['uid'], args['banTime'], args['reason'])
				else:
					logout.error('OnOpCommand fail.GetUIDByNickname fail.args:%s' % args)
			launcherApi.GetUIDByNickname(args['nickname'], _ban)
		elif authConsts.UNBAN_COMMAND == command:
			def _unban(response):
				if response and 0 == response['code']:
					netMasterApi.UnBanUser(response['entity']['uid'])
				else:
					logout.error('OnOpCommand fail.GetUIDByNickname fail.args:%s' % args)
			launcherApi.GetUIDByNickname(args['nickname'], _unban)
		elif authConsts.SILENT_COMMAND == command:
			def _silent(response):
				if response and 0 == response['code']:
					netMasterApi.SilentByUID(response['entity']['uid'], args['banTime'], args['reason'])
				else:
					logout.error('OnOpCommand fail.GetUIDByNickname fail.args:%s' % args)
			launcherApi.GetUIDByNickname(args['nickname'], _silent)
		elif authConsts.UNSILENT_COMMAND == command:
			def _unsilent(response):
				if response and 0 == response['code']:
					netMasterApi.UnSilentByUID(response['entity']['uid'])
				else:
					logout.error('OnOpCommand fail.GetUIDByNickname fail.args:%s' % args)
			launcherApi.GetUIDByNickname(args['nickname'], _unsilent)
		
	def GetOpPlayerKey(self, uid):
		return "user:op:%d" % uid
	
	def doOpPlayer(self, clientId, requestBody):
		import ujson as json
		request = json.loads(requestBody)
		neteaseId = request['neteaseId'] if 'neteaseId' in request else request.get('uid', -1)
		opTime = request.get('opTime', -1)
		opType = request.get('opType', 0)
		if opType not in (ServerOpType.DEOP, ServerOpType.OP):
			masterHttp.SendHttpResponse(clientId, self.makeResponse(1, "op类型不正确"))
			return
		# 给op的玩家，将op信息写入redis
		op_key = self.GetOpPlayerKey(neteaseId)
		redisPool.AsyncFuncWithKey(lambda conn, k, v, ex: conn.set(k, v, ex), op_key, None, op_key, opType, opTime)
		masterHttp.SendHttpResponse(clientId, self.makeResponse(0, "成功！"))
		
		# 通过redis查询玩家所在服务器， 获取结果后发送禁言消息
		key_online_player = commonNetgameApi.GetOnlineKey(neteaseId)
		redisPool.AsyncHgetall(key_online_player, lambda record: self.doOpPlayerCb(neteaseId, record, opType))
		
	def doOpPlayerCb(self, neteaseId, record, opType):
		if record:
			serverId = record.get('serverid', None)
			if serverId is None:
				return
			serverId = int(serverId)
			import master.serverManager as serverManager
			# master是否与server建立连接，可能服务器已经关闭了。
			if serverManager.IsConnectedServer(serverId):
				# 通知服务器玩家被禁言。
				data = self.CreateEventData()
				data["neteaseId"] = neteaseId
				data["opType"] = opType
				self.NotifyToServerNode(serverId, "OpPlayerFromMasterEvent", data)
		
	def Init(self):
		# 初始化时的一些逻辑，例如初始化数据库连接池，初始化配置
		self.mysqlMgr.InitMysqlDb()
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseAuthScript')
		self.mGroupNames = modConfig.get("group", {})
		
	def HttpChangePlayerGroup(self, clientId, requestBody):
		# master指令/change-player-group修改玩家权限组
		eventData = json.loads(requestBody)
		uid = eventData.get("uid", -1)
		authGroup = eventData.get("authGroup", -1)
		if isinstance(uid, int) == False or isinstance(authGroup, int) == False:
			self.SendResponse(clientId, 2, "参数错误")
			return
		if self.mGroupNames.has_key(str(authGroup)) == False:
			self.SendResponse(clientId, 2, "分组不存在")
			return
		def changePlayerGroupCb(success):
			if success:
				self.SendResponse(clientId, 0, "改变成功")
				#数据库改变成功才让lobbygame改变权限
				commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, lambda args:self.NotifyLobbyGameChangeGroup(authGroup,args))
			else:
				self.SendResponse(clientId, 1, "改变失败")
		def queryPlayerGroupCb(sqlResult):
			newAuthData = {"uid": uid,
			               "authGroup": authGroup
			               }
			if len(sqlResult) <= 0:
				#数据库没有，插入新的
				self.mysqlMgr.InsertPlayerGroup(uid, newAuthData, lambda success: changePlayerGroupCb(success))
			else:
				self.mysqlMgr.SavePlayerGroupByUid(uid, newAuthData, lambda success: changePlayerGroupCb(success))
		self.mysqlMgr.QueryPlayerGroup(uid,queryPlayerGroupCb)
	
	def NotifyLobbyGameChangeGroup(self, authGroup, args):
		serverId = args.get("serverId",None)
		#玩家在线，才通知修改权限
		if serverId != None:
			args["authGroup"] = authGroup
			self.NotifyToServerNode(serverId,"ChangeGroupEvent",args)
	
	def SendResponse(self, clientId, code,message):
		# 统一响应请求函数，精简代码
		response = {}
		response['code'] = code
		response['message'] = message
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def Destroy(self):
		pass