# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import logout
import neteaseChillScript.chillConst as chillConst
import json
import server.extraMasterApi as masterApi

MasterSystem = masterApi.GetMasterSystemCls()


class ChillMasterSystem(MasterSystem):
	"""
	该mod的master类
	提供了运营指令供查询玩家活动奖励的领取情况
	"""
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		masterHttp.RegisterMasterHttp(chillConst.ChillRequestMapping.Query, self, self.OnQueryPlayerChillReq)  # 运营指令/query-player-chill，详见readme

	def Destroy(self):
		# MasterSystem.Destroy(self)
		super(ChillMasterSystem, self).Destroy()

	def ChillMasterRender(self, clientId, respData):
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnQueryPlayerChillReq(self, clientId, requestBody):
		"""
		运营指令：【查询一个玩家是否拥有领取活动奖励资格】
		"""
		reqData = json.loads(requestBody)
		print 'OnQueryPlayerChillReq', reqData
		if 'uid' not in reqData or not isinstance(reqData['uid'], int):
			return self.ChillMasterRender(clientId, {
				'code': chillConst.RespCodeInvalidParameter,
				'message': '参数 uid 有误',
			})
		self.RequestToService(  # 请求service
			chillConst.ModName,
			chillConst.QueryPlayerChillEvent,
			reqData,
			lambda rtn, data: self.ChillMasterRender(clientId, data if rtn else {
				'code': chillConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)
