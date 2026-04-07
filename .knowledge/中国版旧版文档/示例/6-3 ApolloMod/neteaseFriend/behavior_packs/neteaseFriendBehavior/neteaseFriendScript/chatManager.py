# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import apiUtil
import logout
import neteaseFriendScript.friendCommon.friendData as friendData
import neteaseFriendScript.friendCommon.playerData as playerData
import neteaseFriendScript.friendCommon.chatRecordData as chatRecordData
import client.extraClientApi as clientApi
import neteaseFriendScript.ui.uiDef as uiDef


class ChatManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.RECORD_MAX_NUM = 200
		self.RECORD_MAX_LENGTH = 30
		
		self.mChatData = chatRecordData.ChatData()
		self.mIsAnyChatNew = {}
		self.mLastChatTime = {}
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'ChatResultEvent', self,
		                           self.OnChatResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'NewChatEvent', self,
		                           self.OnNewChatEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName,
		                           'ClientChatRecordResponseEvent', self, self.OnClientChatRecordResponseEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, 'LocalReadChatEvent', self,
		                           self.OnLocalReadChatEvent)
	
	def OnLocalReadChatEvent(self, args):
		if args.get("mSelectFriendUid") is None:
			return
		self.mIsAnyChatNew[args.get("mSelectFriendUid")] = False
		self.system.BroadcastEvent('LocalIsAnyChatNewChange', {'mSelectFriendUid': args.get("mSelectFriendUid")})
	
	def SetChatNew(self, uid, unRead):
		self.mIsAnyChatNew[uid] = unRead
		if unRead == True:
			self.system.BroadcastEvent('NewChatOrApplyEvent', {"fromUid": uid, "type": "chat"})
			#print "NewChatOrApplyEvent", {"fromUid": uid, "type": "chat"}
	
	def ChatRecordToDict(self, chatIndex, fromUid, toUid, message, chatTime):
		dict = {}
		dict["chatIndex"] = chatIndex
		dict["fromUid"] = fromUid
		dict["toUid"] = toUid
		dict["message"] = message
		dict["chatTime"] = chatTime
		return dict
	
	def clientChat(self, friendUid, message):
		print "clientChat", friendUid
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data["friendUid"] = friendUid
		data["message"] = message
		if apiUtil.GetTextViewLength(message) <= self.RECORD_MAX_LENGTH:
			self.system.NotifyToServer(friendConsts.ChatFromClientEvent, data)
		else:
			self.system.mUIMgr.GetUI(uiDef.UIDef.UIFriendList).ShowTalkWarning("消息长度超过限制")
	
	def OnChatResultEvent(self, args):
		selfUid = args["neteaseId"]
		friendUid = args["friendUid"]
		chatIndex = args["chatIndex"]
		message = args["message"]
		chatTime = args["chatTime"]
		result = args["result"]
		if result:
			tempRecord = self.ChatRecordToDict(chatIndex, selfUid, friendUid, message, chatTime)
			# self.mChatData.InsertChatRecord(friendUid, tempRecord)
			if self.RealInsertChat(friendUid, tempRecord) == True:
				print "OnChatResultEvent", self.mChatData.GetChatRecord(friendUid)
				self.mLastChatTime[args['friendUid']] = tempRecord["chatTime"]
				self.system.BroadcastEvent('LocalChatRecordData', {'friendUid': args['friendUid']})
				self.system.BroadcastEvent("ClientTempChatTimeChangeEvent", self.mLastChatTime)
		else:
			self.system.mUIMgr.GetUI(uiDef.UIDef.UIFriendList).ShowTalkWarning(args.get("reason"))
	
	def RealInsertChat(self, friendUid, tempRecord):
		if self.mChatData.GetChatRecord(friendUid) is not None:
			self.mChatData.InsertChatRecord(friendUid, tempRecord)
			if len(self.mChatData.GetChatRecord(friendUid)) > self.RECORD_MAX_NUM:
				self.mChatData.PopChatRecord(friendUid)
			return True
		else:
			# 没初始化，就往服务器拉数据
			self.TryGetRecord(friendUid)
			return False
	
	def OnNewChatEvent(self, args):
		selfUid = args["neteaseId"]
		friendUid = args["friendUid"]
		chatIndex = args["chatIndex"]
		message = args["message"]
		chatTime = args["chatTime"]
		tempRecord = self.ChatRecordToDict(chatIndex, friendUid, selfUid, message, chatTime)
		self.system.BroadcastEvent('NewChatOrApplyEvent', {"fromUid": friendUid, "type": "chat"})
		#print "NewChatOrApplyEvent", {"fromUid": friendUid, "type": "chat"}
		# self.mChatData.InsertChatRecord(friendUid, tempRecord)
		if self.RealInsertChat(friendUid, tempRecord) == True:
			#print "OnNewChatEvent2", self.mChatData.GetChatRecord(friendUid)
			self.system.BroadcastEvent('LocalChatRecordData', {'friendUid': args['friendUid']})
			self.mLastChatTime[args['friendUid']] = tempRecord["chatTime"]
			self.system.BroadcastEvent("ClientTempChatTimeChangeEvent", self.mLastChatTime)
		# 小红点
		mSelectFriendUid = self.system.mUIMgr.GetUI(uiDef.UIDef.UIFriendList).mSelectFriendUid
		#print "mSelectFriendUid ttst", mSelectFriendUid
		if self.system.mFriendManager.mFriendData.GetFriends() is not None and friendUid not in self.system.mFriendManager.mFriendData.GetFriends():
			if mSelectFriendUid is None or mSelectFriendUid != friendUid:
				self.system.BroadcastEvent('LocalIsAnyChatNewChange',
				                           {'mSelectFriendUid': args.get("mSelectFriendUid")})
				if self.system.mFriendManager.mFriendData.GetTempFriends() is not None and friendUid in self.system.mFriendManager.mFriendData.GetTempFriends():
					return
				else:
					self.SetChatNew(friendUid, True)
	
	# self.system.BroadcastEvent('NewChatOrApplyEvent', {"fromUid": friendUid, "type": "chat"})
	
	def OnClientChatRecordResponseEvent(self, args):
		print "OnClientChatRecordResponseEvent", args
		tempChatRecord = []
		uid1 = args['neteaseId']
		uid2 = args['friendUid']
		if uid1 > uid2:
			uid1, uid2 = uid2, uid1
		for data in args["records"]:
			if data['isSend']:
				fromUid = uid1
				toId = uid2
			else:
				fromUid = uid2
				toId = uid1
			chatIndex = data["chatIndex"]
			message = data["message"]
			chatTime = data["chatTime"]
			tempRecord = self.ChatRecordToDict(chatIndex, fromUid, toId, message, chatTime)
			tempChatRecord.append(tempRecord)
		if len(tempChatRecord) > 0:
			tempChatRecord.sort(self.CmpChatTime)
		self.mChatData.SetChatRecord(args['friendUid'], tempChatRecord)
		self.system.BroadcastEvent('LocalChatRecordData', {'friendUid': args['friendUid']})
		if len(tempChatRecord) > 0:
			self.mLastChatTime[args['friendUid']] = tempChatRecord[-1]["chatTime"]
			self.system.BroadcastEvent("ClientTempChatTimeChangeEvent", self.mLastChatTime)
	
	def CmpChatTime(self, a, b):
		return cmp(a["chatTime"], b["chatTime"])
	
	def TryGetRecord(self, uid, readUnread=True):
		if self.mChatData.GetChatRecord(uid) is not None:
			return self.mChatData.GetChatRecord(uid)
		self.RequestRecordToServer(uid, readUnread)
		return []
	
	def RequestRecordToServer(self, friendUid, readUnread=True):
		print "getRecord", friendUid
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data["friendUid"] = friendUid
		data["readUnread"] = readUnread
		self.system.NotifyToServer("ClientChatRecordRequestEvent", data)
