# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import logout
import neteaseDailyScript.dailyConst as dailyConst
import json
import server.extraMasterApi as masterApi

MasterSystem = masterApi.GetMasterSystemCls()


class DailyMasterSystem(MasterSystem):
	"""
	该mod的master类
	提供一个http接口（运营指令）
	查询玩家本周每日签到奖励的领取情况
	详见readme
	"""

	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		masterHttp.RegisterMasterHttp(dailyConst.DailyRequestMapping.Query, self, self.OnQueryPlayerRecvReq)

	def Destroy(self):
		# MasterSystem.Destroy(self)
		super(DailyMasterSystem, self).Destroy()

	def DailyMasterRender(self, clientId, respData):
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnQueryPlayerRecvReq(self, clientId, requestBody):
		reqData = json.loads(requestBody)
		print 'OnQueryPlayerRecvReq', reqData
		if 'uid' not in reqData or not isinstance(reqData['uid'], int):
			return self.DailyMasterRender(clientId, {
				'code': dailyConst.RespCodeInvalidParameter,
				'message': '参数 uid 有误',
			})
		self.RequestToService(
			dailyConst.ModName,
			dailyConst.QueryPlayerRecvEvent,
			reqData,
			lambda rtn, data: self.DailyMasterRender(clientId, data if rtn else {
				'code': dailyConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)
