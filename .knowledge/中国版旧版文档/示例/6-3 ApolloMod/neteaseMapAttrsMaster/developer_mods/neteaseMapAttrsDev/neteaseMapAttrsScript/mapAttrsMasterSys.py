# -*- coding: utf-8 -*-
import json
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import neteaseMapAttrsScript.util as util
from neteaseMapAttrsScript.mapAttrsConsts import ServerEvent, MasterEvent
from neteaseMapAttrsScript.mapAttrsConsts import SuccessCode, FailCode

class MapAttrsMasterSys(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		util.SetSystem(self)
		masterHttp.RegisterMasterHttp("/mapAttrs/set-area-limit", self, self.OnChangeAreaLimit)
		util.ListenServerEvent(ServerEvent.HttpResponse, self, self.OnHttpResponse)

	def OnHttpResponse(self, args):
		res = self.makeResponse(args['code'], args['message'], args['entity'])
		masterHttp.SendHttpResponse(args['clientId'], res)

	def OnChangeAreaLimit(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		for key in ('type', 'minPos', 'maxPos'):
			if key not in eventData:
				res = self.makeFailResponse(FailCode, 'type, minPos, maxPos is required')
				masterHttp.SendHttpResponse(clientId, res)
				return
		serverId = self.GetServerIdByType(eventData['type'])
		if serverId is None:
			res = self.makeFailResponse(FailCode, 'server type %s is not exist'%eventData["type"])
			masterHttp.SendHttpResponse(clientId, res)
			return
		eventData['clientId'] = clientId
		self.NotifyToServerNode(serverId, MasterEvent.SetMapArea, eventData)

	def GetServerIdByType(self, typeKey):
		import master.netgameApi as netgameApi
		conf = netgameApi.GetCommonConfig()
		serverlist = conf['serverlist']
		for serverInfo in serverlist:
			if serverInfo['type'] == typeKey:
				return serverInfo['serverid']
		return None

	def Destroy(self):
		util.Destroy()
