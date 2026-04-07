# -*- coding: utf-8 -*-
import hmac
import hashlib
import json
import serverhttp
import logout
import shopConsts as shopConsts

class ShopManager(object):
	def __init__(self):
		super(ShopManager,self).__init__()
		self.mGasServerGameKey = ''
		self.mTotalGetUrl = ""
		self.mTotalShipUrl = ""
	
	def SetParam(self, gameKey):
		'''
		设置配置信息
		'''
		
		self.mGasServerGameKey = gameKey
	
	def _genPostSign(self,url,reqStr):
		'''
		生成签名
		'''
		str2sign = 'POST%s%s' % (url, reqStr)
		sign = hmac.new(self.mGasServerGameKey, str2sign, digestmod=hashlib.sha256)
		return sign.hexdigest()
		
	def PostRequest(self,url,baseUrl,reqDict,callback):
		'''
		post请求
		'''
		reqStr = json.dumps(reqDict)
		headerDict = {}
		headerDict['Content-Type'] = 'application/json'
		headerDict['Netease-Server-Sign'] = self._genPostSign(baseUrl, reqStr)
		logout.info('PostRequest.url:%s, req:%s' % (url, reqStr))
		serverhttp.HttpPool().Request('POST', url, headerDict, reqStr, callback)
		
	def GetMcItemOrderList(self,uid,gameId,isTestServer,callback):
		'''
		获取订单列表
		'''
		reqdict = {}
		reqdict['uid'] = uid
		reqdict['gameid'] = gameId
		if isTestServer:
			self.mTotalGetUrl = shopConsts.testGasUrl + shopConsts.baseGetUrl
		else:
			self.mTotalGetUrl = shopConsts.obtGasUrl + shopConsts.baseGetUrl
		self.PostRequest(self.mTotalGetUrl, shopConsts.baseGetUrl, reqdict, callback)
		
	def ShipMcItemOrder(self,uid,gameId,orderidList,isTestServer,callback):
		'''
		通知发货成功
		'''
		reqdict = {}
		reqdict['uid'] = uid
		reqdict['gameid'] = gameId
		reqdict['orderid_list'] = orderidList
		if isTestServer:
			self.mTotalShipUrl = shopConsts.testGasUrl + shopConsts.baseShipUrl
		else:
			self.mTotalShipUrl = shopConsts.obtGasUrl + shopConsts.baseShipUrl
		self.PostRequest(self.mTotalShipUrl, shopConsts.baseShipUrl, reqdict, callback)