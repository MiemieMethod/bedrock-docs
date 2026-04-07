# -*- coding: utf-8 -*-
import hmac
import hashlib
import json
import serverhttp
import logout

class HttpApi(object):
	def __init__(self):
		super(HttpApi, self).__init__()
		self.mGasServerGameKey = ''

	def SetGameKey(self, key):
		self.mGasServerGameKey = key
		
	def _genPostSign(self, url, reqStr):
		'''
		生成签名
		'''
		str2sign = 'POST%s%s' % (url, reqStr)
		sign = hmac.new(self.mGasServerGameKey, str2sign, digestmod=hashlib.sha256)
		return sign.hexdigest()
	
	def PostRequest(self, url, baseUrl, reqDict, callback):
		'''
		post请求
		'''
		reqStr = json.dumps(reqDict)
		headerDict = {}
		headerDict['Content-Type'] = 'application/json'
		headerDict['Netease-Server-Sign'] = self._genPostSign(baseUrl, reqStr)
		logout.info('PostRequest.url:%s, req:%s ,gamekey:%s' % (url, reqStr, self.mGasServerGameKey))
		serverhttp.HttpPool().Request('POST', url, headerDict, reqStr, callback)
	
	def GetRNFriends(self, uid, callback):
		import apolloCommon.launcherApi as launcherApi
		launcherApi.GetUserFriend(uid, callback)
	