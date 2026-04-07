# -*- coding: utf-8 -*-

import master.masterHttp as masterHttp
import logout
import neteaseShoutScript.shoutConst as shoutConst
import json
import server.extraMasterApi as masterApi

MasterSystem = masterApi.GetMasterSystemCls()


def post_json_loads(p_object):
	if isinstance(p_object, dict):
		return {post_json_loads(key): post_json_loads(value) for key, value in p_object.iteritems()}
	elif isinstance(p_object, list):
		return [post_json_loads(item) for item in p_object]
	elif isinstance(p_object, unicode):
		return p_object.encode('utf-8')
	else:
		return p_object


json_loads = lambda s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kwargs: post_json_loads(json.loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kwargs))


class ShoutMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)

		masterHttp.RegisterMasterHttp(shoutConst.ShoutRequestMapping.Notice, self, self.OnNoticeReq)

	def Destroy(self):
		# MasterSystem.Destroy(self)
		super(ShoutMasterSystem, self).Destroy()

	def ShoutMasterRender(self, clientId, respData):
		responseBody = json.dumps({
			'code': respData['code'],
			'message': respData.get('message', ''),
			'entity': respData.get('entity', {})
		})
		masterHttp.SendHttpResponse(clientId, responseBody)

	def OnNoticeReq(self, clientId, requestBody):
		reqData = json_loads(requestBody)
		print 'OnNoticeReq', reqData
		reqData['admin'] = 1
		self.RequestToService(
			shoutConst.ModName,
			shoutConst.PlayerAiringEvent,
			reqData,
			lambda rtn, data: self.ShoutMasterRender(clientId, data if rtn else {
				'code': shoutConst.RespCodeTimeout,
				'message': '请求超时'
			})
		)
