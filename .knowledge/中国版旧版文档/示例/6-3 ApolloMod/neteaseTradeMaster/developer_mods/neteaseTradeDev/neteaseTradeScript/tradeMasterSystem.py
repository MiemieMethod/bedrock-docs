# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import logout
import neteaseTradeScript.tradeConst as tradeConst
import json
import server.extraMasterApi as masterApi

MasterSystem = masterApi.GetMasterSystemCls()


class TradeMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		masterHttp.RegisterMasterHttp(tradeConst.TradeRequestMapping.Query, self, self.OnQueryPlayerDoughsReq)
		masterHttp.RegisterMasterHttp(tradeConst.TradeRequestMapping.Update, self, self.OnUpdatePlayerDoughsReq)
		masterHttp.RegisterMasterHttp(tradeConst.TradeRequestMapping.Count, self, self.OnCountStallsReq)

	def Destroy(self):
		# MasterSystem.Destroy(self)
		super(TradeMasterSystem, self).Destroy()

	def TradeMasterRender(self, clientId, respData):
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnQueryPlayerDoughsReq(self, clientId, requestBody):
		reqData = json.loads(requestBody)
		print 'OnQueryPlayerDoughsReq', reqData
		if 'uid' not in reqData or not isinstance(reqData['uid'], int):
			return self.TradeMasterRender(clientId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': '参数 uid 有误',
			})
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.QueryPlayerDoughsEvent,
			reqData,
			lambda rtn, data: self.TradeMasterRender(clientId, data if rtn else {
				'code': tradeConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)

	def OnUpdatePlayerDoughsReq(self, clientId, requestBody):
		reqData = json.loads(requestBody)
		print 'OnUpdatePlayerDoughsReq', reqData
		if 'uid' not in reqData or not isinstance(reqData['uid'], int):
			return self.TradeMasterRender(clientId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': '参数 uid 有误',
			})
		if 'mod' not in reqData or not reqData['mod'] or not isinstance(reqData['mod'], dict):
			return self.TradeMasterRender(clientId, {
				'code': tradeConst.RespCodeInvalidParameter,
				'message': '参数 mod 有误',
			})
		self.RequestToService(
			tradeConst.ModName,
			tradeConst.UpdatePlayerDoughsEvent,
			reqData,
			lambda rtn, data: self.TradeMasterRender(clientId, data if rtn else {
				'code': tradeConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)

	def OnCountStallsReq(self, clientId, requestBody):
		print 'OnCountStallsReq', requestBody
		self.RequestToService(
			tradeConst.ModName,
			'CountStallsEvent',
			{},
			lambda rtn, data: self.TradeMasterRender(clientId, data if rtn else {
				'code': tradeConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)
