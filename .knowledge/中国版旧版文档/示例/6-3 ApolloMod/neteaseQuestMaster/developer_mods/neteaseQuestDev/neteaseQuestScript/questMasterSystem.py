# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import logout
import neteaseQuestScript.questConst as questConst
import json
import server.extraMasterApi as masterApi

MasterSystem = masterApi.GetMasterSystemCls()


class QuestMasterSystem(MasterSystem):
	"""
	该mod的master类
	提供了运营指令
	详见readme
	"""

	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		self.ListenForEvent('QuestMod', 'questServerSystem', questConst.QueryQuestDataEvent, self, self.OnQueryQuestData)
		self.ListenForEvent('QuestMod', 'questServerSystem', questConst.UpdateQuestDataEvent, self, self.OnUpdateQuestData)

		masterHttp.RegisterMasterHttp(questConst.QuestRequestMapping.Query, self, self.OnQueryQuestDataReq)
		masterHttp.RegisterMasterHttp(questConst.QuestRequestMapping.Update, self, self.OnUpdateQuestDataReq)

	def Destroy(self):
		self.UnListenForEvent('QuestMod', 'questServerSystem', questConst.QueryQuestDataEvent, self, self.OnQueryQuestData)
		self.UnListenForEvent('QuestMod', 'questServerSystem', questConst.UpdateQuestDataEvent, self, self.OnUpdateQuestData)
		# MasterSystem.Destroy(self)
		super(QuestMasterSystem, self).Destroy()

	def OnUpdateQuestData(self, data):
		"""
		运营指令：更改一个玩家的任务数据的最终返回信息，来自对应的service
		"""
		logout.info('OnUpdateQuestData data: {}'.format(data))
		responseBody = json.dumps({
			'code': questConst.RespCodeSuccess,
			'message': '操作成功',
			'entity': {}
		})
		masterHttp.SendHttpResponse(data['clientId'], responseBody)

	def OnQueryQuestData(self, data):
		"""
		运营指令：查询一个玩家所有的的任务数据的最终返回信息，来自对应的service
		"""
		logout.info('OnQueryQuestData data: {}'.format(data))
		responseBody = json.dumps({
			'code': questConst.RespCodeSuccess,
			'message': '请求成功',
			'entity': {
				'uid': data['uid'],
				'doing': data['doing'],
				'done': data['done']
			}
		})
		masterHttp.SendHttpResponse(data['clientId'], responseBody)

	def QuestMasterRender(self, clientId, respData):
		"""
		运营指令直接返回，一般是参数错误等
		"""
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnUpdateQuestDataReq(self, clientId, requestBody):
		"""
		运营指令：更改一个玩家的任务数据，检查参数之后转发给service
		"""
		reqData = json.loads(requestBody)
		print 'OnUpdateQuestDataReq', reqData
		if not ('uid' in reqData and isinstance(reqData['uid'], int) and 'mod' in reqData and isinstance(reqData['mod'], dict)):
			return self.QuestMasterRender(clientId, {
				'code': questConst.RespCodeInvalidParameter,
				'message': '请求参数不合法',
			})
		self.RequestToService(questConst.ModName, questConst.UpdateQuestDataEvent, {'clientId': clientId, 'requestBody': requestBody})

	def OnQueryQuestDataReq(self, clientId, requestBody):
		"""
		运营指令：查询一个玩家的任务数据，检查参数之后转发给service
		"""
		reqData = json.loads(requestBody)
		print 'OnQueryQuestDataReq', reqData
		if not ('uid' in reqData and isinstance(reqData['uid'], int)):
			return self.QuestMasterRender(clientId, {
				'code': questConst.RespCodeInvalidParameter,
				'message': '参数 uid 有误',
			})
		self.RequestToService(questConst.ModName, questConst.QueryQuestDataEvent, {'clientId': clientId, 'uid': reqData['uid']})
