# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import json
import logout
import neteaseAnnounceScript.announceConsts as announceConsts

class AnnounceMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self,namespace,systemName)
		# 登录弹窗
		masterHttp.RegisterMasterHttp(announceConsts.LoginPopupRequest.New,
									  self, self.HttpLoginPopupNew)
		masterHttp.RegisterMasterHttp(announceConsts.LoginPopupRequest.Del,
									  self, self.HttpLoginPopupDel)
		masterHttp.RegisterMasterHttp(announceConsts.LoginPopupRequest.View,
									  self, self.HttpLoginPopupView)
		masterHttp.RegisterMasterHttp(announceConsts.LoginPopupRequest.Clean,
									  self, self.HttpLoginPopupClean)
		# 浮窗公告
		masterHttp.RegisterMasterHttp(announceConsts.FloatingWindowRequest.New,
									  self, self.HttpFloatWinNew)
		masterHttp.RegisterMasterHttp(announceConsts.FloatingWindowRequest.Del,
									  self, self.HttpFloatWinDel)
		masterHttp.RegisterMasterHttp(announceConsts.FloatingWindowRequest.View,
									  self, self.HttpFloatWinView)
		masterHttp.RegisterMasterHttp(announceConsts.FloatingWindowRequest.Clean,
									  self, self.HttpFloatWinClean)
		# 邮件
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.SendToSingle,
									  self, self.HttpMailSendToSingle)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.SendToMany,
									  self, self.HttpMailSendToMany)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.SendToGroup,
									  self, self.HttpMailSendToGroup)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.DelFixMail,
									  self, self.HttpMailDelFix)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.CleanMail,
									  self, self.HttpMailClean)
		# 调试用GM指令
		masterHttp.RegisterMasterHttp(announceConsts.LoginPopupRequest.AskNew,
									  self, self.HttpLoginPopupAskNew)
		masterHttp.RegisterMasterHttp(announceConsts.FloatingWindowRequest.AskNew,
									  self, self.HttpFloatWinAskNew)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.RegUser,
									  self, self.HttpMailRegUser)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.GetMailList,
									  self, self.HttpMailGetList)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.SetRead,
									  self, self.HttpMailSetRead)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.GetBonus,
									  self, self.HttpMailGetBonus)
		masterHttp.RegisterMasterHttp(announceConsts.MailRequest.ReleaseLock,
									  self, self.HttpMailReleaseLock)

	def Destroy(self):
		MasterSystem.Destroy(self)
	# ------------------------------------------------------------------------------------------
	def SendSingleResponse(self, clientId, message="", entity=None):
		response = {}
		response['code'] = announceConsts.CodeSuc
		response['message'] = message
		response['entity'] = entity
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def SendMultiResponse(self, clientId, message="", entities=[]):
		response = {}
		response['code'] = announceConsts.CodeSuc
		response['message'] = message
		response['entities'] = entities
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def SendFailResponse(self, clientId, code, message=None):
		response = {}
		response['code'] = code
		if message is None:
			response['message'] = announceConsts.ErrorText.get(code, "")
		else:
			response['message'] = message
		response['entity'] = None
		response['entities'] = []
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)

	def CommonRequestToServiceCallback(self, suc, args, clientId, codeTimeout):
		if not suc:
			self.SendFailResponse(clientId, codeTimeout)
			return
		code = args["code"]
		if code == announceConsts.CodeSuc:
			self.SendSingleResponse(clientId, args["message"], args["entity"])
		else:
			self.SendFailResponse(clientId, code, args["message"])
	#------------------------------------------------------------------------------------------------
	# 登录弹窗相关请求
	def HttpLoginPopupNew(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeLoginServiceTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.LoginPopupEvent.New,
							  eventData,
							  callback)

	def HttpLoginPopupDel(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeLoginDelTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.LoginPopupEvent.Del,
							  eventData,
							  callback)

	def HttpLoginPopupView(self, clientId, requestBody):
		eventData = {}
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeLoginViewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.LoginPopupEvent.View,
							  eventData,
							  callback)

	def HttpLoginPopupClean(self, clientId, requestBody):
		eventData = {}
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeLoginCleanTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.LoginPopupEvent.Clean,
							  eventData,
							  callback)

	def HttpLoginPopupAskNew(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeLoginAskNewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.LoginPopupEvent.AskNew,
							  eventData,
							  callback)
	#------------------------------------------------------------------------------------------------
	def HttpFloatWinNew(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeFloatingServiceTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.FloatingWindowEvent.New,
							  eventData,
							  callback)

	def HttpFloatWinDel(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeFloatingDelTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.FloatingWindowEvent.Del,
							  eventData,
							  callback)

	def HttpFloatWinView(self, clientId, requestBody):
		eventData = {}
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeFloatingViewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.FloatingWindowEvent.View,
							  eventData,
							  callback)

	def HttpFloatWinClean(self, clientId, requestBody):
		eventData = {}
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeFloatingCleanTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.FloatingWindowEvent.Clean,
							  eventData,
							  callback)

	def HttpFloatWinAskNew(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeFloatingAskNewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.FloatingWindowEvent.AskNew,
							  eventData,
							  callback)
	# ------------------------------------------------------------------------------------------------
	def HttpMailSendToSingle(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args:self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailNewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.SendToSingle,
							  eventData,
							  callback)

	def HttpMailSendToMany(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc, args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailNewTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.SendToMany,
							  eventData,
							  callback)

	def HttpMailSendToGroup(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailGroupTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.SendToGroup,
							  eventData,
							  callback)

	def HttpMailDelFix(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailDelTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.DelFixMail,
							  eventData,
							  callback)

	def HttpMailClean(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailCleanTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.CleanMail,
							  eventData,
							  callback)

	def HttpMailRegUser(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailRegTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.RegUser,
							  eventData,
							  callback)

	def HttpMailGetList(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailListTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.GetMailList,
							  eventData,
							  callback)

	def HttpMailSetRead(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailReadTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.SetRead,
							  eventData,
							  callback)

	def HttpMailGetBonus(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailBonusTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.GetBonus,
							  eventData,
							  callback)

	def HttpMailReleaseLock(self, clientId, requestBody):
		eventData = json.loads(requestBody)
		callback = lambda suc,args: self.CommonRequestToServiceCallback(suc, args, clientId, announceConsts.CodeMailReleaseLockTimeout)
		self.RequestToService(announceConsts.ModNameSpace,
							  announceConsts.MailEvent.ReleaseLock,
							  eventData,
							  callback)