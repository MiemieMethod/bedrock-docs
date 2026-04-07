# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import json
import logout
import neteaseCloudScript.cloudConsts as cloudConsts
from neteaseCloudScript.cloudConsts import CloudItemType
import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import neteaseCloudScript.cloudDbApi as cloudDbApi

class CloudMasterSystem(MasterSystem):
	"""
	该mod的master类
	"""
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self,namespace,systemName)
		masterHttp.RegisterMasterHttp(cloudConsts.QUERY_CLOUD, self, self.OnQueryCloudItems)  # 查询玩家云端信息
		masterHttp.RegisterMasterHttp(cloudConsts.SET_INVENTORY_TO_CLOUD, self, self.OnSetInventoryItems)  # 设置云端背包槽位物品
		self.ListenForEvent(cloudConsts.ModNameSpace, cloudConsts.ServerSystemName,
							cloudConsts.SetUserInventoryResultEvent, self, self.OnSetUserInventoryResult)  # 上面那个接口，服务端处理完毕后返回发送的事件，用于响应http请求
		mysqlPool.InitDB(30)

	def OnSetUserInventoryResult(self, data):
		useExit = data['user_exit']
		if not useExit:
			self.SetUserInventoryDb(data['clientId'], data)
			return
		self.SendResponse(data['clientId'], data['suc'])

	def OnMasterHttpResult(self, data):
		self.SendResponse(data['clientId'], data['isSuc'], data['entity'], data['message'])

	def SendResponse(self, clientId, suc, entity = '', message = ''):
		code = cloudConsts.HTTP_SUCCESS_CODE if suc else cloudConsts.HTTP_FAIL_CODE
		response = self.makeResponse(code, message, entity)
		masterHttp.SendHttpResponse(clientId, response)

	def OnQueryCloudItems(self, clientId, requestBody):
		requetData = json.loads(requestBody)
		uid = requetData['uid']
		apply_tag = requetData.get('apply_tag', "")
		cloudDbApi.GetCloudItems(uid, apply_tag, lambda records: self.ResponseCloudItemsCb(clientId, records))

	def ResponseCloudItemsCb(self, clientId, records):
		if not records:
			self.SendResponse(clientId, False, '', 'db error')
			return
		userRecord = cloudDbApi.UnicodeConvert(records[0])
		userCloud = json.loads(userRecord[0])
		#删掉"itemId"
		if 'hands' in userCloud and 'left' in userCloud['hands'] and userCloud['hands']['left']:
			del userCloud['hands']['left']['itemId']
		if 'inventory' in userCloud and userCloud['inventory']:
			for slot in userCloud['inventory']:
				del userCloud['inventory'][slot]['itemId']
		self.SendResponse(clientId, True, userCloud, '')

	def OnSetInventoryItems(self, clientId, requestBody):
		requetData = json.loads(requestBody)
		uid = requetData['uid']
		commonNetgameApi.GetOnlineServerInfoOfPlayer(uid,
			lambda data : self.SetUserCloud(clientId, requetData, data))

	def SetUserCloud(self, clientId, requestData, onlineData):
		serverId = onlineData['serverId']
		if not serverId:
			# 玩家不在线
			self.SetUserInventoryDb(clientId, requestData)
			#return
		requestData['clientId'] = clientId
		self.NotifyToServerNode(serverId, cloudConsts.SetUserInventoryEvent, requestData)  # 发到mod的服务端类执行

	def SetUserInventoryDb(self, clientId, requestData):
		cloudDbApi.GetCloudItems(requestData['uid'], requestData.get('apply_tag', ""),
				lambda records: self._SetUserCloudCb(clientId, requestData, records))

	def _SetUserCloudCb(self, clientId, requestData, records):
		slot = requestData['slot']
		item = requestData['inventory']
		bInsert = False
		if not records:
			userCloud = {CloudItemType.INVENTORY : {}}
			bInsert = True
		else:
			userRecord = records[0]
			userCloud = cloudDbApi.UnicodeConvert(json.loads(userRecord[0]))
		if not item['count'] and slot in userCloud[CloudItemType.INVENTORY]:
			del userCloud[CloudItemType.INVENTORY][slot]
		else:
			userCloud[CloudItemType.INVENTORY][slot] = requestData['inventory']
		if bInsert:
			cloudDbApi.InsertCloudItems(requestData['uid'], userCloud, requestData.get('apply_tag', ""))
		else:
			cloudDbApi.UpdateCloudItems(requestData['uid'], userCloud, requestData.get('apply_tag', ""))
		self.SendResponse(clientId, True)

	def Destroy(self):
		MasterSystem.Destroy(self)