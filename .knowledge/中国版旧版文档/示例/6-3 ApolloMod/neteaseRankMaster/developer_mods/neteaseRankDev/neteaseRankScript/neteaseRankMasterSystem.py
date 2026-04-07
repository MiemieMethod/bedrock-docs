# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import rankConsts
import logout
import json

class RankMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		masterHttp.RegisterMasterHttp("/delete-rank-data", self, self.HttpDeleteRankData)
		masterHttp.RegisterMasterHttp("/commit-rank-data", self, self.HttpCommitRankData)
	
	def HttpDeleteRankData(self, clientId, requestBody):
		"""
		运营指令：删除排行榜上指定名词的一条记录，检查参数之后转发给service
		"""
		eventData = json.loads(requestBody)
		index = eventData.get("index")
		def DeleteCb(suc, args):
			if not suc:
				self.SendResponse(clientId, 1, "请求超时！")
				return
			else:
				self.SendResponse(clientId, 0, "请求成功！")
		self.RequestToService(rankConsts.ModNameSpace, "DeleteRankDataFromMasterEvent", eventData, DeleteCb, 5)
		
	def HttpCommitRankData(self, clientId, requestBody):
		"""
		运营指令：向排行榜提交一条新的记录，直接转发给service
		"""
		eventData = json.loads(requestBody)
		def DeleteCb(suc, args):
			if not suc:
				self.SendResponse(clientId, 1, "请求超时！")
				return
			else:
				self.SendResponse(clientId, 0, "请求成功！")
		self.RequestToService(rankConsts.ModNameSpace, "CommitRankDataFromMasterEvent", eventData, DeleteCb, 5)
		
	def SendResponse(self, clientId, code, message):
		response = {}
		response['code'] = code
		response['message'] = message
		response['entity'] = []
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)