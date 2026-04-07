# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import json
import logout

class DungeonMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		#注册http指令
		masterHttp.RegisterMasterHttp(dungeonConsts.TransferToDungeonUrl, self,  self.OnTransferToDungeon)
		masterHttp.RegisterMasterHttp(dungeonConsts.GetDungeonNumInfoByTypeUrl, self, self.OnGetDungeonNumInfoByType)

	def OnTransferToDungeon(self, clientId, requestBody):
		'''
		将玩家转服到指定副本游戏中。
		'''
		eventData = json.loads(requestBody)
		if 'uid' not in eventData or 'dungeonType' not in eventData:
			res = self.makeFailResponse(dungeonConsts.FailCode, 'wrong params')
			masterHttp.SendHttpResponse(clientId, res)
			return
		uid = eventData['uid']
		import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
		commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, lambda onlineInfo : self.RequestPlayerToDungeon(onlineInfo, clientId, eventData))

	def RequestPlayerToDungeon(self, onlineInfo, clientId, eventData):
		if not onlineInfo['serverId']:
			res = self.makeFailResponse(dungeonConsts.FailCode, 'player not online')
			masterHttp.SendHttpResponse(clientId, res)
			return
		serverId = onlineInfo['serverId']
		import master.netgameApi as netMasterApi
		conf = netMasterApi.GetCommonConfig()
		serverList = conf['serverlist']  # 获取serverlist配置
		for serverInfo in serverList:
			if serverInfo['serverid'] == serverId:
				if 'lobby' == serverInfo['type']:
					joinData = eventData
					joinData['httpId'] = clientId
					joinData['serverId'] = serverId
					self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.HttpRequestJoinDungeonEvent,
										joinData, lambda suc, args: self.OnSendHttpResponseCb(clientId, suc, args), 2)
					self.NotifyToServerNode(serverId, dungeonConsts.HttpRequestJoinDungeonEvent, joinData)
					return
				break
		res = self.makeFailResponse(dungeonConsts.FailCode, 'player not in  lobby')
		masterHttp.SendHttpResponse(clientId, res)

	def OnGetDungeonNumInfoByType(self, clientId, requestBody):
		'''
		获取空闲和被占用副本数量
		'''
		eventData = json.loads(requestBody)
		if 'dungeonType' not in eventData:
			res = self.makeFailResponse(dungeonConsts.FailCode, 'wrong params')
			masterHttp.SendHttpResponse(clientId, res)
			return
		self.RequestToService(dungeonConsts.ServiceModuleName, dungeonConsts.HttpGetDungeonNumInfoEvent,
							eventData, lambda suc, args: self.OnSendHttpResponseCb(clientId, suc, args), 2)

	def OnSendHttpResponseCb(self, clientId, suc, args):
		'''
		结果返回给http客户端事件
		'''
		if not suc:
			res = self.makeFailResponse(dungeonConsts.FailCode, 'unknown error')
			masterHttp.SendHttpResponse(clientId, res)
			return
		ret = self.makeResponse(args['code'], args['message'], args['entity'])
		masterHttp.SendHttpResponse(clientId, ret)
