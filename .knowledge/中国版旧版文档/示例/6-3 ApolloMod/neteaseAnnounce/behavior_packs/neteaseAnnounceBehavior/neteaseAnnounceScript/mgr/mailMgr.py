# -*- coding: utf-8 -*-
import time
import client.extraClientApi as extraClientApi
from neteaseAnnounceScript.announceConsts import ModNameSpace, ServerSystemName, ServiceSystemName
from neteaseAnnounceScript.announceConsts import MailEvent, MailQueryOnce
import neteaseAnnounceScript.apiUtil as apiUtil
import neteaseAnnounceScript.announceConsts as announceConsts

class MailMgr(object):
	def __init__(self):
		super(MailMgr, self).__init__()
		self.mMailDeleted = []
		self.mMailList = []
		self.mMailDict = {}
		self.mMailCount = 0
		self.mMailArriveCallbackIndex = 0
		self.mMailArriveCallbackList = {}

	def Init(self):
		self.mSystem = apiUtil.GetClientModSystem()
		self.mSystem.ListenForEvent(ModNameSpace, ServerSystemName, MailEvent.GetMailList,
									self, self.OnGetMailList)
		self.mSystem.ListenForEvent(ModNameSpace, ServerSystemName, MailEvent.SetRead,
									self, self.OnSetRead)
		self.mSystem.ListenForEvent(ModNameSpace, ServerSystemName, MailEvent.GetBonus,
									self, self.OnGetBonus)
		self.mSystem.ListenForEvent(ModNameSpace, ServerSystemName, MailEvent.DelFixMail,
									self, self.OnDelFixMail)
		self.mSystem.ListenForEvent(ModNameSpace, ServiceSystemName, MailEvent.NewMailArrive,
									self, self.OnNewMailArrive)
		self.mSystem.ListenForEvent("NeteasePush", "NeteasePush", MailEvent.NewMailArrive,
									self, self.OnNewMailArrive)

	def Destroy(self):
		self.mSystem.UnListenForEvent(ModNameSpace, ServerSystemName, MailEvent.GetMailList,
									self, self.OnGetMailList)
		self.mSystem.UnListenForEvent(ModNameSpace, ServerSystemName, MailEvent.SetRead,
									self, self.OnSetRead)
		self.mSystem.UnListenForEvent(ModNameSpace, ServerSystemName, MailEvent.GetBonus,
									self, self.OnGetBonus)
		self.mSystem.UnListenForEvent(ModNameSpace, ServerSystemName, MailEvent.DelFixMail,
									self, self.OnDelFixMail)
		self.mSystem.UnListenForEvent(ModNameSpace, ServiceSystemName, MailEvent.NewMailArrive,
									self, self.OnNewMailArrive)
		self.mSystem.UnListenForEvent("NeteasePush", "NeteasePush", MailEvent.NewMailArrive,
									self, self.OnNewMailArrive)
		self.mSystem = None
	#------------------------------------------------------------------------------------
	def InspectExpiredMails(self):
		now = int(time.time())
		needDelMailIds = []
		for mailId in self.mMailList:
			mail = self.mMailDict.get(mailId, None)
			if not mail:
				continue
			if mail["expire"] <= now:
				needDelMailIds.append(mailId)
		if needDelMailIds:
			for mailId in needDelMailIds:
				self.mMailList.remove(mailId)
				self.mMailDeleted.append(mailId)
			self.mMailCount -= len(needDelMailIds)
			return True
		return False

	def GetMail(self, mailId):
		if mailId in self.mMailDeleted:
			return None
		return self.mMailDict.get(mailId, None)

	def GetMailByIndex(self, index):
		if index >= len(self.mMailList):
			return None
		mailId = self.mMailList[index]
		return self.mMailDict.get(mailId, None)

	def GetMailOverview(self):
		return self.mMailCount, self.mMailList, self.mMailDict
	#------------------------------------------------------------------------------------
	def SendGetMailList(self, mailId=0):
		data = {
			"playerId": extraClientApi.GetLocalPlayerId(),
			"mailId": mailId,
		}
		self.mSystem.NotifyToServer(MailEvent.GetMailList, data)
	#------------------------------------------------------------------------------------
	def SendSetRead(self, mailId):
		data = {
			"playerId": extraClientApi.GetLocalPlayerId(),
			"mailIds": [mailId,],
		}
		self.mSystem.NotifyToServer(MailEvent.SetRead, data)

	def SendDelFix(self, mailId):
		data = {
			"playerId": extraClientApi.GetLocalPlayerId(),
			"mailIds": [mailId, ],
		}
		self.mSystem.NotifyToServer(MailEvent.DelFixMail, data)

	def SendGetBonus(self, mailId):
		mail = self.mMailDict.get(mailId, None)
		if not mail:
			return
		data = {
			"playerId": extraClientApi.GetLocalPlayerId(),
			"mailIds": [mailId, ],
			"itemList": mail["itemList"],
		}
		self.mSystem.NotifyToServer(MailEvent.GetBonus, data)

	def OnGetMailList(self, data):
		if data["code"] != announceConsts.CodeSuc:
			print "OnGetMailList ERROR message =", data["message"]
			return
		count = data["entity"].get("number", None)
		if count is not None:
			self.mMailCount = count
		newMailIdList = []
		mails = data["entity"].get("mails", [])
		if mails:
			for mail in mails:
				_id = mail["_id"]
				self.mMailDict[_id] = mail
				if _id not in self.mMailList and _id not in self.mMailDeleted:
					newMailIdList.append(_id)
					self.mMailList.append(_id)
			newMailIdList.sort()
			self.mMailList.sort()
			self.mMailList.reverse()
		if len(newMailIdList) >= MailQueryOnce:	# 拉到了上限，就继续拉
			self.SendGetMailList(newMailIdList[0])
		apiUtil.GetMailUI().DoDrawAll()

	def OnSetRead(self, data):
		if data["code"] != announceConsts.CodeSuc:
			print "OnSetRead ERROR message =", data["message"]
			return
		mailIds = data["entity"].get("mailIds", [])
		if mailIds:
			for mailId in mailIds:
				mail = self.mMailDict.get(mailId, None)
				if not mail:
					continue
				mail["hasRead"] = 1
		apiUtil.GetMailUI().DoRefreshMailContent()

	def OnGetBonus(self, data):
		if data["code"] != announceConsts.CodeSuc:
			print "OnGetBonus ERROR message =", data["message"]
			return
		mailIds = data["entity"].get("mailIds", [])
		if mailIds:
			for mailId in mailIds:
				mail = self.mMailDict.get(mailId, None)
				if not mail:
					continue
				mail["getBonus"] = 1
		apiUtil.GetMailUI().DoRefreshMailContent()

	def OnDelFixMail(self, data):
		if data["code"] != announceConsts.CodeSuc:
			print "OnGetBonus ERROR message =", data["message"]
			return
		mailIds = data["entity"].get("mailIds", [])
		if mailIds:
			for mailId in mailIds:
				if mailId not in self.mMailDeleted:
					self.mMailDeleted.append(mailId)
				if mailId in self.mMailList:
					self.mMailList.remove(mailId)
					self.mMailCount -= 1
		apiUtil.GetMailUI().DoDrawAll()
					
	def OnNewMailArrive(self, data):
		self.SendGetMailList()
		for cbFunc in self.mMailArriveCallbackList.itervalues():
			cbFunc()
	
	def RegisterMailArriveCallback(self, cbFunc):
		if not cbFunc:
			return None
		if not callable(cbFunc):
			return None
		index = self.mMailArriveCallbackIndex
		self.mMailArriveCallbackIndex += 1
		self.mMailArriveCallbackList[index] = cbFunc
		return index

	def UnRegisterMailArriveCallback(self, index):
		if not self.mMailArriveCallbackList.has_key(index):
			return False
		del self.mMailArriveCallbackList[index]
		return True
	#------------------------------------------------------------------------------------


