# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import logout
import neteaseFriendScript.friendCommon.friendData as friendData
import neteaseFriendScript.friendCommon.playerData as playerData
import neteaseFriendScript.friendCommon.chatRecordData as chatRecordData
import client.extraClientApi as clientApi
import apiUtil
import neteaseFriendScript.ui.uiDef as uiDef


class FriendManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.FRIENDS_MAX_NUM = 200
		self.TEMP_MAX_NUM = 200
		
		self.mFriendData = 	friendData.CFriendData()
		self.mFriendState = {}
		self.mSearchFriendUid = []
		self.mAroundFriendUid = []
		self.isInit = False
		
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'FriendStateResponseEvent', self, self.OnFriendStateResponseEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'ServerFriendsResponseEvent', self, self.OnServerFriendsResponseEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'FriendsRequestFromServerEvent', self, self.OnFriendsRequestFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'FriendsListFromServerEvent', self, self.OnFriendsListFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'TempListFromServerEvent', self, self.OnTempListFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'RNFriendsListFromServerEvent', self, self.OnRNFriendsListFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'FriendsUnReadFromServerEvent', self, self.OnFriendsUnReadFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'FriendsBlackFromServerEvent', self, self.OnFriendsBlackFromServerEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'SearchFriendResultEvent', self, self.OnSearchFriendResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'SearchFriendAroundResultEvent', self, self.OnSearchFriendAroundResultEvent)
		
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'DeleteBlackListResultEvent', self, self.OnDeleteBlackListResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'DelFriendResultEvent', self, self.OnDelFriendResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'AddBlackListResultEvent', self, self.OnAddBlackListResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'AddFriendResultEvent', self, self.OnAddFriendResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'AcceptFriendResultEvent', self, self.OnAcceptFriendResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'AddTempResultEvent', self, self.OnAddTempResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'RefuseFriendResultEvent', self, self.OnRefuseFriendResultEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServerSystemName, 'NewRequestFromServerEvent', self, self.OnNewRequestFromServerEvent)
		
		#self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, 'LocalReadChatEvent', self, self.OnLocalReadChatEvent)
		
		
	def Init(self):
		if not self.isInit:
			self.updateFriends()
			self.isInit = True
			
	def OnNewRequestFromServerEvent(self, args):
		self.system.BroadcastEvent('NewChatOrApplyEvent', {"fromUid": args["auid"], "type": "request"})
			
	def updateFriends(self):
		print "updateFriends"
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		self.system.NotifyToServer("ClientFriendsRequestEvent", data)
		
	def OnDeleteBlackListResultEvent(self, args):
		#TODO
		print "OnDeleteBlackListResultEvent", args
		self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
		if args.get("errCode") == friendConsts.CodeSuc:
			self.system.mChatManager.mChatData.DelChatRecord(args.get("friendUid"))
	
	def OnDelFriendResultEvent(self, args):
		print "OnDelFriendResultEvent", args
		self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
		if args.get("errCode") == friendConsts.CodeSuc:
			self.system.mChatManager.mChatData.DelChatRecord(args.get("friendUid"))
			
	
	def OnAddBlackListResultEvent(self, args):
		print "OnAddBlackListResultEvent", args
		friendUid = args.get("friendUid")
		friendData = self.system.mPlayerManager.getPlayerData(friendUid)
		if friendData is not None:
			nickname = friendData.GetPlayerData().get("nickname", "")
			if args.get("errCode") == friendConsts.CodeSuc:
				self.system.ShowConfirmPop("提示", "已成功将【%s】加入黑名单，对方将无法向你发送消息和添加好友" % nickname)
			else:
				self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
	
	def OnAddFriendResultEvent(self, args):
		print "OnAddFriendResultEvent", args
		if args.get("needShow", False):
			if args.get("errCode") == friendConsts.CodeSuc:
				self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
			elif args.get("errCode") == friendConsts.HisFriendsMax:
				inviteUi = self.system.mUIMgr.GetUI(uiDef.UIDef.UIFriendInvite)
				inviteUi.SaveInProcessHint("对方好友已满", args.get("friendUid"), "PageNearList")
				inviteUi.SaveInProcessHint("对方好友已满", args.get("friendUid"), "PageFindList")
				self.system.BroadcastEvent('LocalUpdatePlayerData', {"uid": args.get("friendUid")})
			else:
				inviteUi = self.system.mUIMgr.GetUI(uiDef.UIDef.UIFriendInvite)
				inviteUi.SaveInProcessHint("无法加为好友", args.get("friendUid"), "PageNearList")
				inviteUi.SaveInProcessHint("无法加为好友", args.get("friendUid"), "PageFindList")
				self.system.BroadcastEvent('LocalUpdatePlayerData', {"uid": args.get("friendUid")})
	
	def OnAcceptFriendResultEvent(self, args):
		print "OnAcceptFriendResultEvent", args
		if args.get("needShow", False):
			self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
			
	def OnAddTempResultEvent(self, args):
		print "OnAddTempResultEvent", args
		if args.get("needShow", False):
			self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
	
	def OnRefuseFriendResultEvent(self, args):
		print "OnRefuseFriendResultEvent", args
		self.system.ShowConfirmPop("提示", friendConsts.ResponseText[args.get("errCode")])
	
	def OnSearchFriendResultEvent(self, args):
		print "OnSearchFriendResultEvent", args
		if args.has_key("uid"):
			self.mSearchFriendUid = [args.get("uid")]
		else:
			self.mSearchFriendUid = []
			self.system.ShowConfirmPop("提示", "你搜索的玩家不存在！")
		self.system.BroadcastEvent('LocalSearchFriendChangeEvent', {"mSearchFriendUid": self.mSearchFriendUid})
		
	def OnSearchFriendAroundResultEvent(self, args):
		aroundPlayerUids = args.get("aroundPlayerUids")
		self.mAroundFriendUid = aroundPlayerUids
		self.system.BroadcastEvent('LocalSearchAroundChangeEvent', {"mAroundFriendUid":self.mAroundFriendUid})
		
	def OnFriendsUnReadFromServerEvent(self, args):
		friendUnReadList = args.get("friendUnReadList")
		self.mFriendData.SetUnReadFriend(friendUnReadList)
		for unReadUid in friendUnReadList:
			self.system.mChatManager.SetChatNew(unReadUid,True)
		self.system.BroadcastEvent('LocalFriendUnReadChangeEvent', {})
		
	
	def OnFriendsRequestFromServerEvent(self, args):
		print 'OnFriendsRequestFromServerEvent', args
		friendRequests = args.get("friendsRequest")
		self.mFriendData.SetRequest(friendRequests)
		if args.get("needFreshClient", True) == True:
			self.system.BroadcastEvent('LocalFriendRequestChangeEvent', {})
		
	def OnFriendsListFromServerEvent(self, args):
		print 'OnFriendsListFromServerEvent', args
		friendUids = args.get("friendUids")
		self.mFriendData.SetFriends(friendUids)
		self.system.BroadcastEvent('LocalFriendListChangeEvent', {})
		# if self.system.mChatManager.mChatData.mChatRecords is not None:
		# 	for hasChatUid in self.system.mChatManager.mChatData.mChatRecords.keys():
		# 		if hasChatUid not in friendUids:
		# 			self.system.mChatManager.mChatData.DelChatRecord(hasChatUid)
		for hasNewChatUid in self.system.mChatManager.mIsAnyChatNew.keys():
			if hasNewChatUid not in friendUids:
				self.system.mChatManager.mIsAnyChatNew.pop(hasNewChatUid)
		# 请求查看好友是否在线
		requestStateUids = [uid for uid in friendUids if uid not in self.mFriendState]
		self.requestFriendsState(requestStateUids)
		
	def OnTempListFromServerEvent(self, args):
		print 'OnTempListFromServerEvent', args
		tempList = args.get("tempList")
		self.mFriendData.SetTempFriend(tempList)
		self.system.BroadcastEvent('LocalTempListChangeEvent', {})
		# if self.system.mChatManager.mChatData.mChatRecords is not None:
		# 	for hasChatUid in self.system.mChatManager.mChatData.mChatRecords.keys():
		# 		if hasChatUid not in tempList:
		# 			self.system.mChatManager.mChatData.DelChatRecord(hasChatUid)
		for hasNewChatUid in self.system.mChatManager.mIsAnyChatNew.keys():
			if hasNewChatUid not in tempList:
				self.system.mChatManager.mIsAnyChatNew.pop(hasNewChatUid)
		# 请求查看好友是否在线
		requestStateUids = [uid for uid in tempList if uid not in self.mFriendState]
		self.requestFriendsState(requestStateUids)
		
		
	def	OnRNFriendsListFromServerEvent(self, args):
		print 'OnRNFriendsListFromServerEvent', args
		RNfriendUids = args.get("RNfriendUids")
		self.mFriendData.SetRNFriend(set(RNfriendUids))
		self.system.BroadcastEvent('LocalRNFriendListChangeEvent', {})
		# 请求查看好友是否在线
		requestStateUids = [uid for uid in RNfriendUids if uid not in self.mFriendState]
		self.requestFriendsState(requestStateUids)
		
	def OnFriendsBlackFromServerEvent(self, args):
		print "OnFriendsBlackFromServerEvent", args
		friendBlackUids = args.get("friendBlackUids")
		self.mFriendData.SetBlackList(friendBlackUids)
		self.system.BroadcastEvent('LocalBlackListChangeEvent', {})
		# # 请求查看好友是否在线
		# requestStateUids = [uid for uid in friendBlackUids if uid not in self.mFriendState]
		# self.requestFriendsState(requestStateUids)
	
	def OnServerFriendsResponseEvent(self, args):
		print 'OnServerFriendsResponseEvent', args
		RNFriendUids = set(args.get("RNFriends"))
		friendUids = args.get("friendUids")
		friendRequests = args.get("friendRequests")
		friendBlackUids = args.get("friendBlackUids")
		friendUnReadList = args.get("friendUnReadList")
		tempList = args.get("tempList")
		self.mFriendData.SetRNFriend(RNFriendUids)
		self.mFriendData.SetFriends(friendUids)
		self.mFriendData.SetRequest(friendRequests)
		self.mFriendData.SetBlackList(friendBlackUids)
		self.mFriendData.SetUnReadFriend(friendUnReadList)
		self.mFriendData.SetTempFriend(tempList)
		if friendUnReadList:
			for unReadUid in friendUnReadList:
				self.system.mChatManager.SetChatNew(unReadUid, True)
			self.system.BroadcastEvent('LocalIsAnyChatNewChange', {})
		self.mFriendData.SetUnReadFriend([])
		#请求查看好友是否在线
		if friendUids is None:
			friendUids = []
		if friendBlackUids is None:
			friendBlackUids = []
		requestStateUids = [uid for uid in friendUids + friendBlackUids if uid not in self.mFriendState]
		self.requestFriendsState(requestStateUids)
		for tempUid in tempList:
			self.system.mChatManager.TryGetRecord(tempUid, True)
		
	def requestFriendsState(self, uids):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['uids'] = uids
		self.system.NotifyToServer("ClientFriendStateRequestEvent", data)
		
	# def requestFriendLastChatTime(self, uids):
	# 	data = self.system.CreateEventData()
	# 	data["entityId"] = clientApi.GetLocalPlayerId()
	# 	data['uids'] = uids
	# 	self.system.NotifyToServer("ClientLastChatTimeRequestEvent", data)
		
	def OnFriendStateResponseEvent(self, args):
		print "FriendStateResponseEvent", args
		for uid, state in args['friendState'].iteritems():
			self.mFriendState[uid] = state
		self.system.BroadcastEvent("ClientFriendStateChangeEvent", self.mFriendState)
			
	def addFriend(self, friendUid, message):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		data['message'] = message
		self.system.NotifyToServer(friendConsts.AddFriendFromClientEvent, data)
		
	def acceptFriend(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer(friendConsts.AcceptFriendFromClientEvent, data)
		
	def refuseFriend(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer(friendConsts.RefuseFriendFromClientEvent, data)
		
	def deleteFriend(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer(friendConsts.DeleteFriendFromClientEvent, data)
		
	def addBlack(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer(friendConsts.AddBlackFromClientEvent, data)
		
	def delBlack(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer(friendConsts.DeleteBlackFromClientEvent, data)
		
	def delTemp(self, friendUid):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['friendUid'] = friendUid
		self.system.NotifyToServer("DeleteTempFromClientEvent", data)
		
	def searchFriend(self, searchTxt):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		data['searchTxt'] = searchTxt
		self.system.NotifyToServer(friendConsts.SearchFriendFromClientEvent, data)
		
	def searchNear(self):
		data = self.system.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		self.system.NotifyToServer(friendConsts.SearchFriendAroundFromClientEvent, data)
		
		
		
		