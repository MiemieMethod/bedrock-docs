# -*- coding: utf-8 -*-
import json

import server.extraMasterApi as mastarApi
MasterSystem = mastarApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import master.serverManager as serverManager
import apolloCommon.redisPool as redisPool
import apolloCommon.commonNetgameApi as commonNetgameApi

from neteaseAddupScript.addupConsts import ModName, ServerSystemName, ServerEvent, MasterRequest, MasterEvent
import neteaseAddupScript.dbApi as dbApi

class AddupMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self,namespace,systemName)
		dbApi.Init()
		redisPool.InitDB(20)
		masterHttp.RegisterMasterHttp(MasterRequest.GetAddupCharge, self, self.OnHttpGetAddupCharge)
		masterHttp.RegisterMasterHttp(MasterRequest.SetAddupCharge, self, self.OnHttpSetAddupCharge)
		masterHttp.RegisterMasterHttp(MasterRequest.SetAddupBonusState, self, self.OnHttpSetAddupBonusState)
		self.ListenForEvent(ModName, ServerSystemName, ServerEvent.HttpResponse, self, self.OnHttpResponse)

	def Destroy(self):
		redisPool.Finish()
		dbApi.Destroy()
		MasterSystem.Destroy(self)
	# ------------------------------------------------------------------------------------------
	def SendResponse(self, clientId, entity=None):
		response = {}
		response['suc'] = True
		response['message'] = ""
		response['entity'] = entity
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def SendFailResponse(self, clientId, message):
		response = {}
		response['suc'] = False
		response['message'] = message
		response['entity'] = None
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def OnHttpResponse(self, data):
		clientId = data["clientId"]
		suc = data.get("suc", False)
		message = data.get("message", "")
		entity = data.get("entity", None)
		if suc:
			self.SendResponse(clientId, entity)
		else:
			self.SendFailResponse(clientId, message)
	#------------------------------------------------------------------------------------------------
	def OnHttpGetAddupCharge(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		uid = eventData.get("uid", None)
		if not uid:
			self.SendFailResponse(clientId, "必须指定uid才能查询累积消费活动信息")
			return
		addupKey = eventData.get("addupKey", None)
		if not addupKey:
			self.SendFailResponse(clientId, "必须指定累积消费活动关键字，才能查询对应的活动信息")
			return
		def QueryPlayerAddupDataCallback(addupData):
			if not addupData:
				self.SendFailResponse(clientId, "查询失败，目标uid的玩家不存在，或者没有参与指定累积消费活动")
				return
			addupInfo = addupData.get(addupKey, None)
			if not addupInfo:
				self.SendFailResponse(clientId, "查询失败，指定累积消费活动不存在，或者目标uid的玩家没有参与目标活动")
				return
			payDiamonds = addupInfo.get("process", 0)
			alreadyGetBonusKeys = addupInfo.get("bonusList", [])
			data = {
				"uid": uid,
				"online": False,
				"payDiamonds": payDiamonds,
				"alreadyGetBonusKeys": alreadyGetBonusKeys,
			}
			self.SendResponse(clientId, data)
		def QueryPlayerOnlineCallback(record):
			if not record:
				dbApi.QueryPlayerData(uid, QueryPlayerAddupDataCallback)
				return
			serverId = record.get('serverid', None)
			if serverId is None:
				dbApi.QueryPlayerData(uid, QueryPlayerAddupDataCallback)
				return
			serverId = int(serverId)
			status = serverManager.GetOneServerStatus(serverId)
			if status != 2:
				dbApi.QueryPlayerData(uid, QueryPlayerAddupDataCallback)
				return
			eventData = {
				"clientId": clientId,
				"uid": uid,
				"addupKey": addupKey,
			}
			self.NotifyToServerNode(serverId, MasterEvent.GetAddupCharge, eventData)
		plKey = commonNetgameApi.GetOnlineKey(uid)
		redisPool.AsyncHgetall(plKey, QueryPlayerOnlineCallback)
	
	def OnHttpSetAddupCharge(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		uid = eventData.get("uid", None)
		if not uid:
			self.SendFailResponse(clientId, "必须指定uid才能设置玩家的累积消费活动消费进度")
			return
		addupKey = eventData.get("addupKey", None)
		try:
			payDiamonds = int(eventData.get("payDiamonds", 0))
		except:
			self.SendFailResponse(clientId, "payDiamonds参数必须为正整数")
			return
		if payDiamonds < 0:
			self.SendFailResponse(clientId, "payDiamonds参数必须为正整数")
			return
		def QueryPlayerOnlineCallback(record):
			if not record:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置累积消费活动消费进度")
				return
			serverId = record.get('serverid', None)
			if serverId is None:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置累积消费活动消费进度")
				return
			serverId = int(serverId)
			status = serverManager.GetOneServerStatus(serverId)
			if status != 2:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置累积消费活动消费进度")
				return
			eventData = {
				"clientId": clientId,
				"uid": uid,
				"addupKey": addupKey,
				"payDiamonds": payDiamonds,
			}
			self.NotifyToServerNode(serverId, MasterEvent.SetAddupCharge, eventData)
		plKey = commonNetgameApi.GetOnlineKey(uid)
		redisPool.AsyncHgetall(plKey, QueryPlayerOnlineCallback)
	
	def OnHttpSetAddupBonusState(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		uid = eventData.get("uid", None)
		if not uid:
			self.SendFailResponse(clientId, "必须指定uid才能设置玩家的奖励领取状态")
			return
		addupKey = eventData.get("addupKey", None)
		bonusKey = eventData.get("bonusKey", None)
		if not bonusKey:
			self.SendFailResponse(clientId, "必须指定奖励关键字，才能设置玩家的奖励领取状态")
			return
		alreadyGet = eventData.get("alreadyGet", None)
		if alreadyGet not in (0, 1):
			self.SendFailResponse(clientId, "alreadyGet 只能为0或者1")
			return
		def QueryPlayerOnlineCallback(record):
			if not record:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置玩家的奖励领取状态")
				return
			serverId = record.get('serverid', None)
			if serverId is None:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置玩家的奖励领取状态")
				return
			serverId = int(serverId)
			status = serverManager.GetOneServerStatus(serverId)
			if status != 2:
				self.SendFailResponse(clientId, "目标玩家不在线，无法设置玩家的奖励领取状态")
				return
			eventData = {
				"clientId": clientId,
				"uid": uid,
				"addupKey": addupKey,
				"bonusKey": bonusKey,
				"alreadyGet": alreadyGet,
			}
			self.NotifyToServerNode(serverId, MasterEvent.SetAddupBonusState, eventData)
		plKey = commonNetgameApi.GetOnlineKey(uid)
		redisPool.AsyncHgetall(plKey, QueryPlayerOnlineCallback)
