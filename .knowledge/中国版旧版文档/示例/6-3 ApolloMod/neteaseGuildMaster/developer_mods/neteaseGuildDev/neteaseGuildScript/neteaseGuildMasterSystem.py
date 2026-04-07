# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import json
import guildConsts as guildConsts

class GuildMasterSystem(MasterSystem):
	"""
	该mod的master类
	提供运营指令
	详见readme
	"""
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		print '====init GuildMasterSystem=====', namespace, systemName
		masterHttp.RegisterMasterHttp("/dismiss-guild", self, self.HttpDismissGuild)
		
	def HttpDismissGuild(self, clientId, requestBody):
		"""
		运营指令：强制解散指定公会
		"""
		eventData = json.loads(requestBody)
		guildId = eventData.get("guildId", -1)
		guildName = eventData.get("guildName", None)
		if guildName:
			guildName = guildName.encode("utf-8")
		if isinstance(guildId, int) == False:
			self.SendResponse(clientId, guildConsts.CodeParamError, guildConsts.ResponseText[guildConsts.CodeParamError])
			return
		if guildName != None and isinstance(guildName, str) == False:
			self.SendResponse(clientId, guildConsts.CodeParamError, guildConsts.ResponseText[guildConsts.CodeParamError])
			return
		# 逻辑实现，还是要丢给service，master只是中转请求
		def disMissCb(suc, args):
			if not suc:
				self.SendResponse(clientId, guildConsts.CodeOutOfTime, guildConsts.ResponseText[guildConsts.CodeOutOfTime])
				return
			else:
				self.SendResponse(clientId, args["code"], args["message"])
		data = {"guildId": guildId, "guildName": guildName}
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.DisMissGuildFromMasterEvent, data, disMissCb, 3)
	
	def SendResponse(self, clientId, code, message):
		response = {}
		response['code'] = code
		response['message'] = message
		response['entity'] = []
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)