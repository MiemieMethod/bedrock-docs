# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
import master.netgameApi as netMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import neteaseResidenceScript.residenceConsts as residenceConsts
import neteaseResidenceScript.dbApi as dbApi
import json
import neteaseResidenceScript.util as util

class ResidenceMasterSys(MasterSystem):
	"""
	该mod的master类
	提供运营指令
	详见readme
	"""
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		print 'Init ResidenceMasterSys'
		dbApi.Init()
		self.DefineEvent(residenceConsts.QueryServerResidenceEvent)
		self.DefineEvent(residenceConsts.HttpDelResidenceEvent)
		masterHttp.RegisterMasterHttp(residenceConsts.QueryPlayerResidenceInfoUrl, self,
									self.OnQueryPlayerResidenceInfo)
		masterHttp.RegisterMasterHttp(residenceConsts.QueryServerResidenceInfoUrl, self,
									self.OnQueryServerResidenceInfo)
		masterHttp.RegisterMasterHttp(residenceConsts.SetResidenceInfoUrl, self,
									self.OnSetResidenceInfo)
		masterHttp.RegisterMasterHttp(residenceConsts.DelResidenceUrl, self,
									self.OnDelResidence)
		masterHttp.RegisterMasterHttp(residenceConsts.AddPlayerToResidenceUrl, self,
									  self.OnAddPlayerToResidence)
		masterHttp.RegisterMasterHttp(residenceConsts.RemovePlayerFromResidenceUrl, self,
									  self.OnRemovePlayerFromResidence)
		masterHttp.RegisterMasterHttp(residenceConsts.ChangeResidenceAuthorityUrl, self,
									  self.OnChangeResidenceAuthority)
		masterHttp.RegisterMasterHttp(residenceConsts.ChangePlayerResidenceAuthorityUrl, self,
									  self.OnChangePlayerResidenceAuthority)
		masterHttp.RegisterMasterHttp(residenceConsts.ReleasePlayerResidenceLockUrl, self,
									  self.OnReleasePlayerResidenceLock)
		masterHttp.RegisterMasterHttp(residenceConsts.ChangeResidenceBornPosUrl, self,
									  self.OnChangeResidenceBornPos)
		self.ListenForEvent(residenceConsts.ModNameSpace, residenceConsts.ServerSystemName,
									residenceConsts.HttpResponseEvent, self, self.OnHttpResponse)

	def OnQueryPlayerResidenceInfo(self, clientId, requestBody):
		'''
		运营指令：查询某个玩家的领地信息
		'''
		eventData = json.loads(requestBody)
		if 'uid' not in eventData:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
			masterHttp.SendHttpResponse(clientId, res)
			return
		uid = eventData['uid']
		dbApi.QueryResidenceByUid(uid, lambda records: self._QueryPlayerResidenceCb(uid, clientId, records))

	def _QueryPlayerResidenceCb(self, uid, clientId, records):
		if records is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'db error')
			masterHttp.SendHttpResponse(clientId, res)
			return
		residenceList = []
		for one in records:
			resInfo = {
				"id": one[0],
				"name": one[1],
				"serverType": one[2],
				"dimension": one[3],
				"resLevel": one[6],
				"parentResId": one[7],
				"authority": json.loads(one[8]),
			}
			resInfo['minPos'], resInfo['maxPos'] = util.AreaStringToPos(one[4])
			resInfo['bornPos'] = util.StringToList(one[5])
			residenceList.append(resInfo)
		res = self.makeResponse(residenceConsts.SuccessCode, '', residenceList)
		masterHttp.SendHttpResponse(clientId, res)

	# ------------------------------------------------------------------------------------------
	def GetServerIdByType(self, serverType):
		conf = netMasterApi.GetCommonConfig()
		serverlist = conf['serverlist']  # 获取serverlist配置
		for serverInfo in serverlist:
			if serverInfo['type'] == serverType:
				return serverInfo['serverid']
		return None

	def OnQueryServerResidenceInfo(self, clientId, requestBody):
		'''
		运营指令：查询服务器中的所有领地信息
		'''
		eventData = json.loads(requestBody)
		if 'type' not in eventData:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
			masterHttp.SendHttpResponse(clientId, res)
			return
		serverType = eventData['type']
		startId = eventData.get("startId", 0)
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'type not valid')
			masterHttp.SendHttpResponse(clientId, res)
			return
		self.NotifyToServerNode(serverId, residenceConsts.QueryServerResidenceEvent, {'clientId': clientId, "startId":startId})

	def OnHttpResponse(self, args):
		'''
		http结果返回给运营指令请求方
		'''
		res = self.makeResponse(args['code'], args['message'], args['entity'])
		masterHttp.SendHttpResponse(args['clientId'], res)

	def OnSetResidenceInfo(self, clientId, requestBody):
		"""
		运营指令：新建领地
		"""
		eventData = json.loads(requestBody)
		for key in ('name', 'type', 'minPos', 'maxPos'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		uid, parentResId = eventData.get("uid", None), eventData.get("parentResId", None)
		if uid is None and parentResId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'one residence must either has an owner or has parent')
			masterHttp.SendHttpResponse(clientId, res)
			return	
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.SetPlayerResidenceEvent, eventData)

	def OnAddPlayerToResidence(self, clientId, requestBody):
		"""
		运营指令：给已经存在的领地添加一个新的所有者
		"""
		eventData = json.loads(requestBody)
		for key in ('uid', 'resId', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.AddPlayerToResidenceEvent, eventData)

	def OnRemovePlayerFromResidence(self, clientId, requestBody):
		"""
		运营指令：为已经存在的领地移除一个所有者
		"""
		eventData = json.loads(requestBody)
		for key in ('uid', 'resId', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.RemovePlayerFromResidenceEvent, eventData)

	def OnDelResidence(self, clientId, requestBody):
		"""
		运营指令：删除指定领地
		"""
		eventData = json.loads(requestBody)
		for key in ('resId', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.HttpDelResidenceEvent, eventData)

	def OnChangeResidenceAuthority(self, clientId, requestBody):
		"""
		运营指令：修改指定领地权限
		"""
		eventData = json.loads(requestBody)
		for key in ('resId', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.ChangeResidenceAuthorityEvent, eventData)

	def OnChangePlayerResidenceAuthority(self, clientId, requestBody):
		"""
		运营指令：修改指定玩家在指定领地的权限
		"""
		eventData = json.loads(requestBody)
		for key in ('uid', 'resId', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.ChangePlayerResidenceAuthorityEvent, eventData)

	def OnReleasePlayerResidenceLock(self, clientId, requestBody):
		"""
		运营指令：强制释放玩家领地操作锁
		"""
		eventData = json.loads(requestBody)
		for key in ('uid', 'type'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.ReleasePlayerResidenceLockEvent, eventData)

	def OnChangeResidenceBornPos(self, clientId, requestBody):
		"""
		运营指令：修改一个领地的传送点
		"""
		eventData = json.loads(requestBody)
		for key in ('resId', 'type', 'pos'):
			if key not in eventData:
				res = self.makeFailResponse(residenceConsts.FailCode, 'wrong params')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(residenceConsts.FailCode, 'wrong type')
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, residenceConsts.ChangeResidenceBornPosEvent, eventData)

	def Destroy(self):
		print 'Destroy ResidenceMasterSys'
		dbApi.Destroy()