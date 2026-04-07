# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import neteaseFriendScript.friendCommon.friendData as friendData
#import neteaseFriendScript.friendCommon.httpApi as httpApi
import logout
import apolloCommon.commonNetgameApi as commonNetgameApi
import time
import timer
import Queue
import json

class FriendManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.FRIENDS_MAX_NUM = 0
		self.TEMP_MAX_NUM = 0
		
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.AddFriendFromServerEvent, self.OnAddFriendFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, "CreateTempChatFromServer", self.OnCreateTempChatFromServer)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, "DeleteTempFromServerEvent", self.OnDeleteTempFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.AcceptFriendFromServerEvent,
		                       self.OnAcceptFriendFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.RefuseFriendFromServerEvent,
		                       self.OnRefuseFriendFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.DeleteFriendFromServerEvent,
		                       self.OnDeleteFriendFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.AddBlackFromServerEvent,
		                       self.OnAddBlackFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.DeleteBlackFromServerEvent,
		                       self.OnDeleteBlackFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.SyncRNFriendFromServerEvent,
		                              self.OnSyncRNFriendFromServerEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, "ReadMessageEvent",
		                              self.OnReadMessageEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, "RequestFriendListsEvent",
		                              self.OnRequestFriendListsEvent)
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.DelPlayerFromServerEvent,
		                              self.OnDelPlayerFromServer)

	def Init(self, modConfig):
		logout.info("FriendManager, init", modConfig)
		self.FRIENDS_MAX_NUM = modConfig.get("FRIENDS_MAX_NUM")
		self.TEMP_MAX_NUM = modConfig.get("TEMP_MAX_NUM")
	
	def OnDelPlayerFromServer(self, serverId, callbackId, args):
		"""
		玩家离线事件，清理全部的临时好友信息
		"""
		logout.info("OnDelPlayerFromServer", args)
		uid = args.get("uid")
		self.system.mFriendDbManager.PrepareFriendData([uid], lambda args: self.realDelAllTemp(serverId, args),args)
		
	def realDelAllTemp(self, serverId, args):
		"""
		清理临时好友信息
		"""
		selfUid = args.get("uid")
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		print "realDelAllTemp", args
		if sData is None:
			return
		selfTempFriends = sData.GetTempFriends()
		print "selfTempFriends", selfTempFriends
		if selfTempFriends is None or len(selfTempFriends) <= 0:
			return
		for oneTempFriendUid in selfTempFriends:
			fData = self.system.mFriendDbManager.getFriendData(oneTempFriendUid)
			#先删，不管fData有没有
			if fData is not None:
				fData.DelTempFriend(selfUid)
			sData.DelTempFriend(oneTempFriendUid)
			self.system.mFriendDbManager.ServiceDelTemp(selfUid, oneTempFriendUid)
			self.system.mFriendDbManager.ServiceDelTemp(oneTempFriendUid, selfUid, self.notifyDelTempFromService(oneTempFriendUid, selfUid))
			#如果内存没有最好，有才删一下
			if fData is None or fData.GetTempFriends() is None or len(fData.GetTempFriends()) <= 0:
				continue
	
	def notifyDelTempFromService(self, selfUid, tempFriendUid):
		def GetOnlineCb(args):
			# 申请了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				self.system.NotifyToServerNode(serverId, "AddTempFriendNotifyFromServiceEvent", args)
			else:
				logout.info("notifyAddFriendRequest, player offline", args['uid'])
		commonNetgameApi.GetOnlineServerInfoOfPlayer(selfUid, GetOnlineCb)
		
	def OnRequestFriendListsEvent(self, serverId, callbackId, args):
		"""
		来自server，请求指定uid玩家的好友列表
		1、假如玩家好友信息没有在内存缓存中，需要先从数据库从读取好友相关信息，并保存在内存缓存中
		2、返回玩家好友列表信息给对应server
		"""
		uid = args.get("uid")
		def SerciceQueryPlayerDataCb():
			friendUidLists = self.system.mFriendDbManager.getFriendData(uid).GetFriends()
			self.system.ResponseToServer(serverId, callbackId, {"uid":uid, "friendUidLists":friendUidLists})
		self.system.mPlayerDbManager.SerciceQueryPlayerData([uid], SerciceQueryPlayerDataCb)
		
	
	def OnSyncRNFriendFromServerEvent(self, serverId, callbackId, args):
		"""
		来自server，同步指定uid玩家的RN好友信息，第一阶段
		1、假如玩家好友信息没有在内存缓存中，需要先从数据库从读取好友相关信息，并保存在内存缓存中
		2、假如玩家其他好友相关信息（黑名单、好友申请、RN好友同步记录）没有在内存缓存中，需要先从数据库从读取这些信息，并保存在内存缓存中
		3、传递参数到【RealSyncRNFriend】函数
		"""
		logout.info("OnSyncRNFriendFromServerEvent", args)
		needSyncUid = args.get("needSyncUid")
		friendUids = args.get("friend_uids")
		def SerciceQueryPlayerDataCb():
			self.system.mFriendDbManager.SyncRNPrepareFriendData([needSyncUid] + friendUids, self.RealSyncRNFriend,
			                                        {"friend_uids": friendUids, "needSyncUid": needSyncUid})
		
		self.system.mPlayerDbManager.SerciceQueryPlayerData([needSyncUid] + friendUids, SerciceQueryPlayerDataCb)
	
	def RealSyncRNFriend(self, args):
		"""
		来自server，同步指定uid玩家的RN好友信息，第二阶段
		1、对比当前本地已有好友列表和RN好友列表，diff出需要增量加为好友的uid列表
		2、遍历增量uid列表，尝试自动生成好友关系，并通知对应目标玩家（假如在线）
		3、推送通知非RN好友，更新【是否为RN好友】的标识状态，并通知对应目标玩家（假如在线）
		"""
		friendUids = args.get("friend_uids")
		needSyncUid = args.get("needSyncUid")
		sData = self.system.mFriendDbManager.getFriendData(needSyncUid)
		if sData is not None:
			sData.ClearRNFriend()
			alreadyFriends = sData.GetFriends()
			alreadySyncFriends = sData.GetHasSyncUids()
			if alreadyFriends is None:
				alreadyFriends = []
			if alreadySyncFriends is None:
				alreadySyncFriends = []
		else:
			alreadyFriends = []
			alreadySyncFriends = []
		def GetOnlineCb(args):
			serverId = args.get("serverId")
			RNFriendUids = set()
			for friendUid in friendUids:
				if friendUid in alreadySyncFriends:
					continue
				canContinue,suc = self.doSyncRnFriend(serverId, needSyncUid, friendUid)
				logout.info("doSyncRnFriend_after", needSyncUid, friendUid, canContinue, suc)
				if canContinue == False:
					break
				if suc == True:
					RNFriendUids.add(friendUid)
			notRNFriendUids = set(alreadyFriends) - set(friendUids)
			if len(notRNFriendUids) > 0:
				self.system.mFriendDbManager.ServiceUpdateFriendShip(needSyncUid, list(notRNFriendUids), False, lambda :self.notyfyUpdateFriendShip(serverId,needSyncUid, notRNFriendUids))
		commonNetgameApi.GetOnlineServerInfoOfPlayer(needSyncUid, GetOnlineCb)
		
	def notyfyUpdateFriendShip(self, lobbyId,needSyncUid, notRNFriendUids):
		"""
		推送通知非RN好友，更新【是否为RN好友】的标识状态，并通知对应目标玩家（假如在线）
		"""
		logout.info("notyfyUpdateFriendShip", list(notRNFriendUids))
		def GetOnlineCb(args):
			logout.info("GetOnlineCbnotyfyUpdateFriendShip", args)
			for data in args:
				serverId = data.get("serverId")
				if serverId is not None:
					self.system.NotifyToServerNode(serverId, friendConsts.RNFriendsUpdateFromServiceEvent, {"uid":data.get("uid")})
		self.system.NotifyToServerNode(lobbyId, friendConsts.RNFriendsUpdateFromServiceEvent, {"uid":needSyncUid})
		commonNetgameApi.GetOnlineServerInfoOfMultiPlayers(list(notRNFriendUids), GetOnlineCb)
		
	
	def doSyncRnFriend(self, lobbyId, selfUid, friendUid):
		"""
		尝试自动生成好友关系，并通知对应目标玩家（假如在线）
		"""
		logout.info("doSyncRnFriend", selfUid, friendUid)
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		logout.info("doSyncRnFriend2", sData, fData)
		
		fPlayerData = self.system.mPlayerDbManager.getPlayerCaches(friendUid)
		#这个人没来过这个游戏
		if fPlayerData is None:
			return True,False
		
		if sData is not None:
			# if sData.GetFriends() is not None and friendUid in sData.GetFriends():
			# 	return True,False
			logout.info("doSyncRnFriend7", sData.GetFriends())
			if sData.GetFriends() is not None and len(sData.GetFriends()) >= self.FRIENDS_MAX_NUM and friendUid not in sData.GetFriends():
				return False,False  # 达到最大了，不同步了
			if sData.GetBlackList() is not None and friendUid in sData.GetBlackList():
				return True,False
		else:
			logout.info("doSyncRnFriend3")
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
		if fData is not None:
			if fData.GetBlackList() is not None and selfUid in fData.GetBlackList():
				return True,False
			if fData.GetFriends() is not None and len(fData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				return True,False
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.AddRNFriend(selfUid)
		else:
			logout.info("doSyncRnFriend4")
			fData = friendData.CFriendData()
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.AddRNFriend(selfUid)
			fData.AddHasSyncUids(selfUid)
		# 互相都是好友
		sData.AddFriend(friendUid)
		sData.AddRNFriend(friendUid)
		sData.AddHasSyncUids(friendUid)
		self.system.mFriendDbManager.mFriends[friendUid] = fData
		logout.info("doSyncRnFriend5", self.system.mFriendDbManager.mFriends[friendUid])
		self.system.mFriendDbManager.mFriends[selfUid] = sData
		
		self.system.mFriendDbManager.ServiceDeleteFriendRequest(selfUid, friendUid,
		                                                        lambda: self.afterRNAddFriendDelRequest(selfUid,
		                                                                                              friendUid,
		                                                                                              lobbyId))
		
		return True,True
	
	def afterRNAddFriendDelRequest(self, selfUid, friendUid, lobbyId):
		"""
		基于RN的好友关系，自动生成新的好友关系后，清理对应的尚未处理好友申请信息
		"""
		self.system.mFriendDbManager.ServiceInsertFriendShip(selfUid, friendUid, True,
		                                                     lambda: self.notifyAcceptFriendResult(lobbyId, selfUid,
		                                                                                           friendUid, True,
		                                                                                           True, friendConsts.CodeSuc))
		self.system.mFriendDbManager.ServiceInsertFriendShip(friendUid, selfUid, True, lambda: self.notifyAcceptFriend(friendUid, selfUid))
		
		self.system.mFriendDbManager.ServiceInsertHasSyncFriendShip(selfUid, friendUid)
		self.system.mFriendDbManager.ServiceInsertHasSyncFriendShip(friendUid, selfUid)
	
	# 标识两个玩家之间的聊天记录为已读
	def OnReadMessageEvent(self, serverId, callbackId, args):
		"""
		标识selfUid已读和friendUid之间的聊天记录，第一阶段：从数据库加载selfUid的好友相关信息到内存缓存
		"""
		logout.info("OnAddFriendFromServerEvent", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid], lambda args: self.realReadMessage(serverId, args), args)
		
	def realReadMessage(self, lobbyId, args):
		"""
		标识selfUid已读和friendUid之间的聊天记录，第二阶段：修改内存缓存中的聊天记录已读状态，然后修改数据库中聊天记录的已读状态
		"""
		logout.info("realReadMessage", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		if sData and sData.GetUnReadFriendList() and selfUid in sData.GetUnReadFriendList():
			sData.DelUnReadFriendList(friendUid)
		self.system.mFriendDbManager.ServiceDelUnread(selfUid, friendUid, lambda: None)
		#self.notifyAddFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.CodeSuc)
	
	def addUnreadMessageFriend(self, selfUid, friendUid):
		"""
		标识selfUid未读和friendUid之间的聊天记录，第一阶段：从数据库加载selfUid的好友相关信息到内存缓存
		"""
		args = selfUid, friendUid
		self.system.mFriendDbManager.PrepareFriendData([selfUid], lambda args: self.realAddUnRead(args), args)
		
	def realAddUnRead(self, args):
		"""
		标识selfUid未读和friendUid之间的聊天记录，第二阶段：修改内存缓存中的聊天记录已读状态，然后修改数据库中聊天记录的已读状态
		"""
		selfUid, friendUid = args
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		if sData :
			sData.AddUnReadFriendList(friendUid)
		self.system.mFriendDbManager.ServiceInsertUnread(selfUid, friendUid, lambda: None)
		
	# ========申请好友逻辑
	def OnAddFriendFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid向friendUid发出加好友申请，第一阶段：从数据库加载selfUid和friendUid的好友相关信息到内存缓存
		'''
		logout.info("OnAddFriendFromServerEvent", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid],
		                                        lambda args: self.realAddFriend(serverId, args), args)
		
	def OnCreateTempChatFromServer(self, serverId, callbackId, args):
		'''
		selfUid发出的，加friendUid为临时好友的请求，第一阶段：从数据库加载selfUid和friendUid的好友相关信息到内存缓存
		'''
		logout.info("OnCreateTempChatFromServer", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid],
		                                               lambda args: self.realCreateTemp(serverId, callbackId, args), args)
		
	def OnDeleteTempFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid发出的，把friendUid从临时好友中删除的请求，第一阶段：从数据库加载selfUid和friendUid的好友相关信息到内存缓存
		'''
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args: self.realDelTemp(serverId, args), args)
		
	def realDelTemp(self, serverId, args):
		'''
		selfUid发出的，把friendUid从临时好友中删除的请求，第二阶段：修改内存缓存中临时好友信息，然后修改数据库中临时好友信息，再然后通知双方
		'''
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		fData.DelTempFriend(selfUid)
		sData.DelTempFriend(friendUid)
		self.system.mFriendDbManager.ServiceDelTemp(selfUid, friendUid, lambda: self.notifyAddTempFriend(selfUid, friendUid))
		self.system.mFriendDbManager.ServiceDelTemp(friendUid, selfUid, lambda: self.notifyAddTempFriend(friendUid, selfUid))

	def realCreateTemp(self, lobbyId, callbackId, args):
		'''
		selfUid发出的，加friendUid为临时好友的请求，第二阶段：修改内存缓存中临时好友信息，然后修改数据库中临时好友信息，再然后通知双方结果（假如失败，仅给发起方返回失败原因）
		'''
		logout.info("realCreateTemp", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		if sData is not None:
			if sData.GetBlackList() is not None and friendUid in sData.GetBlackList():
				#你已拉黑该玩家，不能创建临时聊天
				self.notifyAddTempFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.FriendInYourBlack, True)
				self.system.ResponseToServer(lobbyId, callbackId, {{"suc":False, "reason":"你已经拉黑该玩家！"}})
				return
			if sData.GetTempFriends() is not None and friendUid in sData.GetTempFriends():
				#self.notifyAddTempFriendResult(lobbyId, selfUid, friendUid, True, True, friendConsts.AlreadyInTempFriends, True)
				#self.system.ResponseToServer(lobbyId, callbackId, {{"suc": False, "reason": "你已经添加该玩家为临时好友！"}})
				self.system.ResponseToServer(lobbyId, callbackId, {"suc": True, "reason": "创建临时聊天成功！"})
				return
			if sData.GetFriends() is not None and friendUid in sData.GetFriends():
				#self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.AlreadyFriend, True)
				self.system.ResponseToServer(lobbyId, callbackId, {"suc": True, "reason": "创建临时聊天成功！", "openTemp":False})
				return
		else:
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
			self.system.mFriendDbManager.mFriends[selfUid] = sData
		if fData is not None:
			if fData.GetBlackList() is not None and selfUid in fData.GetBlackList():
				# 该玩家已拉黑你
				self.notifyAddTempFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.YouInFriendBlack, True)
				self.system.ResponseToServer(lobbyId, callbackId, {{"suc": False, "reason": "该玩家已拉黑你！"}})
				return
		else:
			friend = friendData.CFriendData()
			friend.SetUid(friendUid)
			self.system.mFriendDbManager.mFriends[friendUid] = friend
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		if sData.GetTempFriends() is not None and len(sData.GetTempFriends()) >= self.system.mFriendManager.TEMP_MAX_NUM:
			#self.ChatResult(serverId, fromUid, toUid, False, message, currentTime, "你的临时聊天好友数量已经达到最大值")
			self.notifyAddTempFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.YourTempFriendsMax, True)
			self.system.ResponseToServer(lobbyId, callbackId, {{"suc": False, "reason": "你的临时聊天数量已达最大值！"}})
			return
		if fData.GetTempFriends() is not None and len(fData.GetTempFriends()) >= self.system.mFriendManager.TEMP_MAX_NUM:
			#self.ChatResult(serverId, fromUid, toUid, False, message, currentTime, "对方的临时聊天好友数量已经达到最大值")
			self.notifyAddTempFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.HisTempFriendsMax, True)
			self.system.ResponseToServer(lobbyId, callbackId, {{"suc": False, "reason": "他的临时聊天数量已达最大值！"}})
			return
		fData.AddTempFriend(selfUid)
		sData.AddTempFriend(friendUid)
		self.system.mFriendDbManager.ServiceInsertTempFriends(selfUid, friendUid, lambda: self.notifyAddTempFriendResult(lobbyId, selfUid,friendUid, True, True, friendConsts.CodeSuc, False, callbackId))
		self.system.mFriendDbManager.ServiceInsertTempFriends(friendUid, selfUid, lambda: self.notifyAddTempFriend(friendUid, selfUid))
	
	def realAddFriend(self, lobbyId, args):
		'''
		selfUid向friendUid发出加好友申请，第二阶段：修改内存缓存中好友关系信息，然后修改数据库中好友关系信息，再然后通知双方（失败仅通知发起方失败原因）
		'''
		logout.info("realAddFriend", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		message = args.get("message")
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		requestDict = self.system.mFriendDbManager.RequestToDict(friendUid, selfUid, message)
		#logout.info("=======11111111111==========", fData.GetFriends())
		#logout.info("=======22222222222==========", fData.GetFriendRequests())
		
		if sData is not None:
			logout.info("realAddFriend", sData.GetFriends(), self.FRIENDS_MAX_NUM)
			if sData.GetFriends() is not None and friendUid in sData.GetFriends():
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.AlreadyFriend, True)
				return
			if sData.GetFriends() is not None and len(sData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.YourFriendsMax, True)
				return
			if sData.GetBlackList() is not None and friendUid in sData.GetBlackList():
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.FriendInYourBlack, True)
				return
		if fData is not None:
			if fData.GetBlackList() is not None and selfUid in fData.GetBlackList():
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.YouInFriendBlack, True)
				return
			if fData.GetFriendRequests() is not None and selfUid in fData.GetFriendRequests():
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.AlreadyInRequest, True)
				return
			if fData.GetFriends() is not None and len(fData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				self.notifyAddFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.HisFriendsMax, True)
				return
			fData.SetUid(selfUid)
			fData.AddFriendRequest(requestDict)
		else:
			friend = friendData.CFriendData()
			friend.SetUid(friendUid)
			friend.AddFriendRequest(requestDict)
			self.system.mFriendDbManager.mFriends[friendUid] = friend
		
		self.system.mFriendDbManager.ServiceInsertFriendRequest(requestDict, lambda:self.notifyAddFriendRequest(requestDict))
		self.notifyAddFriendResult(lobbyId, selfUid, friendUid, True, False, friendConsts.CodeSuc, False)
	
	def notifyAddFriendRequest(self, request):
		"""
		推送通知成立好友关系的被动方：好友关系成立（仅成功）
		"""
		def GetOnlineCb(args):
			# 申请了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				self.system.NotifyToServerNode(serverId, friendConsts.AddFriendNotifyFromServiceEvent, request)
			else:
				logout.info("notifyAddFriendRequest, player offline", request['uid'])
		
		commonNetgameApi.GetOnlineServerInfoOfPlayer(request['uid'], GetOnlineCb)
	
	def notifyAddFriendResult(self, lobbyId, uid, friendId, isSuc, needRefresh, errCode, showTip = False):
		"""
		通知成立好友关系的主动方，操作的结果（成功/失败）
		"""
		logout.verbose('notifyAddFriendResult', isSuc, errCode, friendConsts.ResponseText[errCode])
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['showTip'] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.AddFriendResultFromServiceEvent, data)
		
	def notifyAddTempFriendResult(self, lobbyId, uid, friendId, isSuc, needRefresh, errCode, showTip = False, callbackId = None):
		"""
		通知成立临时好友关系的主动方，操作的结果（成功/失败）
		"""
		logout.verbose('notifyAddTempFriendResult', isSuc, errCode, friendConsts.ResponseText[errCode])
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['showTip'] = showTip
		data['openTemp'] = True
		# if callbackId:
		# 	self.system.ResponseToServer(lobbyId, callbackId, {"suc": True, "reason": "创建临时聊天成功！"})
		self.system.NotifyToServerNode(lobbyId, "AddTempFriendResultFromServiceEvent", data)
		
	def notifyAddTempFriend(self, uid, friendId):
		"""
		通知成立临时好友关系的被动方，临时好友关系成立（仅成功）
		"""
		def GetOnlineCb(args):
			# 接受了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				data = self.system.CreateEventData()
				data["uid"] = uid
				data["friendUid"] = friendId
				self.system.NotifyToServerNode(serverId, "AddTempFriendNotifyFromServiceEvent", data)
			else:
				logout.info("AddTempFriend, player offline", uid)
		commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, GetOnlineCb)
	
	# ========接受好友
	def OnAcceptFriendFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid同意friendUid发出的加好友申请，第一阶段：从数据库加载selfUid和friendUid的好友信息到内存缓存
		'''
		logout.info("OnAcceptFriendFromServerEvent", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid],
		                                        lambda args: self.realAcceptFriend(serverId, args), args)
	
	def realAcceptFriend(self, lobbyId, args):
		'''
		selfUid同意friendUid发出的加好友申请，第二阶段：
		1、通过各种判定之后，修改内存中好友关系信息（成立好友关系，删除加好友申请，删除临时好友关系）
		2、然后修改数据库中对应的信息
		3、再然后通知双方（失败是仅返回失败原因给主动发起方selfUid）
		'''
		logout.info("realAcceptFriend", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		
		if sData is not None:
			logout.info("realAcceptFriend", sData.GetFriends(), self.FRIENDS_MAX_NUM)
			if sData.GetFriends() is not None and friendUid in sData.GetFriends():
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.AlreadyFriend, True)
				return
			if sData.GetFriends() is not None and len(sData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.YourFriendsMax, True)
				return
			if sData.GetBlackList() is not None and friendUid in sData.GetBlackList():
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True,
				                              friendConsts.FriendInYourBlack, True)
				return
			if sData.GetFriendRequests() is not None and friendUid not in sData.GetFriendRequests():
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True,
				                              friendConsts.NotInRequest, True)
				return
		else:
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
			self.system.mFriendDbManager.mFriends[friendUid] = sData
		if fData is not None:
			if fData.GetBlackList() is not None and selfUid in fData.GetBlackList():
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True,
				                              friendConsts.YouInFriendBlack, True)
				return
			if fData.GetFriends() is not None and len(fData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid, False, True, friendConsts.HisFriendsMax, True)
				return
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.DelFriendRequest(selfUid)
			fData.DelTempFriend(selfUid)
		else:
			fData = friendData.CFriendData()
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.DelFriendRequest(selfUid)
			fData.DelTempFriend(selfUid)
			self.system.mFriendDbManager.mFriends[friendUid] = fData
		# 互相都是好友
		sData.AddFriend(friendUid)
		sData.DelFriendRequest(friendUid)
		sData.DelTempFriend(friendUid)
		self.system.mFriendDbManager.ServiceDelTemp(selfUid, friendUid, lambda: self.notifyAddTempFriend(selfUid, friendUid))
		self.system.mFriendDbManager.ServiceDelTemp(friendUid, selfUid, lambda: self.notifyAddTempFriend(friendUid, selfUid))
		
		self.system.mFriendDbManager.ServiceDeleteFriendRequest(selfUid, friendUid, lambda:self.afterAddFriendDelRequest(selfUid, friendUid, lobbyId))
		
	def afterAddFriendDelRequest(self, selfUid, friendUid, lobbyId):
		self.system.mFriendDbManager.ServiceInsertFriendShip(selfUid, friendUid, False,
		                                              lambda:self.notifyAcceptFriendResult(lobbyId, selfUid, friendUid,
		                                                                            True,
		                                                                            True, friendConsts.CodeSuc, False))
		self.system.mFriendDbManager.ServiceInsertFriendShip(friendUid, selfUid, False,
		                                              lambda:self.notifyAcceptFriend(friendUid, selfUid))
		self.system.BroadcastEvent("ServiceAcceptFriendBroadCastEvent", {"selfUid":selfUid, "friendUid":friendUid})
	
	def notifyAcceptFriend(self, uid, friendId):
		"""
		通知成立好友关系的被动方，好友关系成立（仅成功）
		"""
		def GetOnlineCb(args):
			# 接受了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				data = self.system.CreateEventData()
				data["uid"] = uid
				data["friendUid"] = friendId
				self.system.NotifyToServerNode(serverId, friendConsts.AcceptFriendNotifyFromServiceEvent, data)
			else:
				logout.info("notifyAcceptFriend, player offline", uid)
		
		commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, GetOnlineCb)
	
	def notifyAcceptFriendResult(self, lobbyId, uid, friendId, isSuc, needRefresh, errCode, showTip = False):
		"""
		通知建立好友关系的主动方，试图建立好友关系的结果（成功/失败）
		"""
		logout.verbose('notifyAcceptFriendResult', isSuc, errCode, friendConsts.ResponseText[errCode])
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['showTip'] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.AcceptFriendResultFromServiceEvent, data)
	
	def notifyCFriendResult(self, lobbyId, uid, friendId, isSuc, needRefresh, errCode):
		"""
		已废弃
		"""
		logout.verbose('notifyAcceptFriendResult', isSuc, errCode, friendConsts.ResponseText[errCode])
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		self.system.NotifyToServerNode(lobbyId, friendConsts.AcceptFriendResultFromServiceEvent, data)
	
	# ======拒绝好友
	def OnRefuseFriendFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid拒绝friendUid发出的加好友申请，第一阶段：从数据库加载selfUi的好友信息到内存缓存
		'''
		logout.info("OnRefuseFriendFromServerEvent", args)
		uid = args.get("selfUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([uid], lambda args: self.realRefuseFriend(serverId, args), args)
	
	def realRefuseFriend(self, lobbyId, args):
		'''
		selfUid拒绝friendUid发出的加好友申请，第二阶段：从内存中删除对应的加好友申请，然后修改数据库中对应的信息，再然后通知双方
		'''
		logout.info('realRefuseFriend', args)
		uid = args['selfUid']
		friendId = args['friendUid']
		sData = self.system.mFriendDbManager.getFriendData(uid)
		sData.DelFriendRequest(friendId)
		self.system.mFriendDbManager.ServiceDeleteFriendRequest(uid, friendId,
		                                                 lambda: self.notifyRefuseFriendRequest(lobbyId, uid, friendId,
		                                                                                uid, friendConsts.CodeSuc, True))
		
		self.system.BroadcastEvent("ServiceRefuseFriendBroadCastEvent", {"selfUid": args['selfUid'], "friendUid": args['friendUid']})
		
		def GetOnlineCb(args):
			# 删除了申请，给friend所在的lobby发送消息,但是好像不用？
			serverId = args.get("serverId")
			if serverId:
				self.notifyRefuseFriendRequest(serverId, friendId, friendId, uid)
			else:
				logout.info("realRefuseFriend, player offline", uid)
		
		commonNetgameApi.GetOnlineServerInfoOfPlayer(friendId, GetOnlineCb)
	
	# notify
	def notifyRefuseFriendRequest(self, lobbyId, uid, fromId, toId, errCode = 0, showTip = False):
		"""
		通知拒绝加好友申请的主动方，拒绝加好友申请的结果（成功/失败）
		"""
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['fromId'] = fromId
		data['toId'] = toId
		data['errCode'] = errCode
		data['showTip'] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.RefuseFriendResultFromServiceEvent, data)
	
	# =====删除好友
	def OnDeleteFriendFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid刪除与friendUid的好友关系，第一阶段：从数据库加载selfUid与friendUid的好友信息到内存缓存
		'''
		logout.info("OnDeleteFriendFromServerEvent", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid],
		                                        lambda args: self.realDeleteFriend(serverId, args), args)
	
	def realDeleteFriend(self, lobbyId, args):
		'''
		selfUid刪除与friendUid的好友关系，第二阶段：删除内存缓存中的好友关系，然后删除数据库中的好友关系，再然后通知双方
		'''
		logout.verbose('realRefuseFriendEvent', args)
		selfUid = args['selfUid']
		friendUid = args['friendUid']
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		sData.DelFriend(friendUid)
		fData.DelFriend(selfUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(selfUid, friendUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(friendUid, selfUid)
		self.system.mFriendDbManager.ServiceDeleteFriendShip(selfUid, friendUid,
		                                              lambda: self.notifyDeleteFriendResult(lobbyId, selfUid, friendUid,
		                                                                            True, True,
		                                                                            friendConsts.CodeSuc, True))
		self.system.mFriendDbManager.ServiceDeleteFriendShip(friendUid, selfUid,
		                                              lambda: self.notifyDeleteFriend(friendUid, selfUid))
	
	def notifyDeleteFriend(self, uid, friendId):
		"""
		通知删除好友关系的被动方，好友关系被解除（仅成功）
		"""
		def GetOnlineCb(args):
			# 删除了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				data = self.system.CreateEventData()
				data["uid"] = uid
				data["friendUid"] = friendId
				self.system.NotifyToServerNode(serverId, friendConsts.DeleteFriendNotifyFromServiceEvent, data)
			else:
				logout.info("notifyDeleteFriend, player offline", uid)
		
		commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, GetOnlineCb)
	
	def notifyDeleteFriendResult(self, lobbyId, uid, friendId, isSuc, needRefresh, errCode, showTip =False):
		"""
		通知删除好友关系的主动方，试图解除好友关系的结果（成功/失败）
		"""
		logout.verbose('notifyDeleteFriendResult', isSuc, errCode, friendConsts.ResponseText[errCode])
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['showTip'] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.DeleteFriendResultFromServiceEvent, data)
	
	# =====移出黑名单
	def OnDeleteBlackFromServerEvent(self, serverId, callbackId, args):
		'''
		selfUid把friendUid从黑名单中删除：第一阶段：从数据库中把selfUid的好友数据加载到内存缓存
		'''
		logout.info("OnDeleteBlackFromServerEvent", args)
		selfUid = args.get("selfUid")
		# 先把数据加载进内存
		self.system.mFriendDbManager.PrepareFriendData([selfUid], lambda args: self.realDeleteBlack(serverId, args), args)
	
	def realDeleteBlack(self, lobbyId, args):
		'''
		selfUid把friendUid从黑名单中删除：第二阶段：修改内存缓存中的黑名单信息，然后更新数据库中的黑名单信息，再然后通知selfUid操作结果
		'''
		logout.info('realDeleteBlack', args)
		selfUid = args['selfUid']
		friendUid = args['friendUid']
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		sData.DelBlackList(friendUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(selfUid, friendUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(friendUid, selfUid)
		self.system.mFriendDbManager.ServiceDeleteFriendBlack(selfUid, friendUid, lambda: self.notifyDeleteBlackListResult(lobbyId, selfUid, friendUid, True))
	
	def notifyDeleteBlackListResult(self, lobbyId, uid, friendId, showTip = False):
		"""
		通知删除黑名单的主动方，试图删除黑名单的结果（成功/失败）
		"""
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['errCode'] = friendConsts.CodeSuc
		data['showTip'] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.DeleteBlackListResultFromServiceEvent, data)
	
	# ====加入黑名单
	def OnAddBlackFromServerEvent(self, serverId, callbackId, args):
		"""
		selfUid把friendUid加入到自己的黑名单中，第一阶段：从数据库加载selfUid和friendUid的好友相关信息到内存缓存
		"""
		logout.verbose('OnAddBlackFromServerEvent', args)
		selfUid = args['selfUid']
		friendUid = args['friendUid']
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args: self.realAddBlack(serverId, args), args)
	
	def realAddBlack(self, lobbyId, args):
		"""
		selfUid把friendUid加入到自己的黑名单中，第二阶段：
		1、通过各种判定之后，修改内存中好友关系信息（加入黑名单，删除好友关系，删除临时好友关系）
		2、然后修改数据库中对应的信息
		3、再然后通知双方（失败是仅返回失败原因给主动发起方selfUid）
		"""
		logout.info("realAddBlack", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		
		if sData is not None:
			if sData.GetBlackList() is not None and len(sData.GetBlackList()) >= self.FRIENDS_MAX_NUM:
				self.notifyAddBlackListResult(lobbyId, selfUid, friendUid, False, friendConsts.YourFriendsMax, True)
				return
		else:
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
			self.system.mFriendDbManager.mFriends[selfUid] = sData
		if fData is None:
			fData = friendData.CFriendData()
			fData.SetUid(friendUid)
			self.system.mFriendDbManager.mFriends[friendUid] = fData
		if sData.GetFriends() is not None and friendUid in sData.GetFriends():
			sData.DelFriend(friendUid)
			fData.DelFriend(selfUid)
			self.system.mFriendDbManager.ServiceDeleteFriendShip(selfUid, friendUid, lambda: self.notifyDeleteFriendResult(lobbyId, selfUid, friendUid,
			                                                                            True, True, friendConsts.CodeSuc))
			self.system.mFriendDbManager.ServiceDeleteFriendShip(friendUid, selfUid, lambda: self.notifyDeleteFriend(friendUid, selfUid))
		fData.DelTempFriend(selfUid)
		sData.DelTempFriend(friendUid)
		self.system.mFriendDbManager.ServiceDelTemp(selfUid, friendUid, lambda: self.notifyAddTempFriend(selfUid, friendUid))
		self.system.mFriendDbManager.ServiceDelTemp(friendUid, selfUid, lambda: self.notifyAddTempFriend(friendUid, selfUid))
		sData.AddblackList(friendUid)
		
		self.system.mFriendDbManager.ServiceInsertFriendBlack(selfUid, friendUid, lambda: self.notifyAddBlackListResult(lobbyId, selfUid, friendUid, True, friendConsts.CodeSuc, True))
	
	def notifyAddBlackListResult(self, lobbyId, uid, friendId, isSuc, errCode, showTip = False):
		"""
		通知添加黑名单的主动方，试图添加黑名单的结果（成功/失败）
		"""
		if not lobbyId:
			return
		data = self.system.CreateEventData()
		data['neteaseId'] = uid
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data["errCode"] = errCode
		data["showTip"] = showTip
		self.system.NotifyToServerNode(lobbyId, friendConsts.AddBlackListResultFromServiceEvent, data)

	#===========================================提供的接口===========================================================
	#加好友
	def OutAddFriend(self, selfUid, friendUid, callback):
		"""
		由代码直接驱动，selfUid和friendUid建立好友关系， 第一阶段：从数据库加载selfUid和friendUid的好友信息到内存缓存
		"""
		if selfUid <= 0 or friendUid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args:self.outRealAddFriend(args, callback), {"selfUid":selfUid,"friendUid":friendUid})

	def outRealAddFriend(self, args, callback):
		"""
		由代码直接驱动，selfUid和friendUid建立好友关系， 第二阶段：
		1、通过各种判定后，修改内存中的好友关系以及相关伴随状态
		2、然后修改数据库中对应的信息
		3、调用参数中的回调函数，返回最终处理的结果（成功/失败）
		4、通知被影响到的双方，好友关系成立（仅成功）
		"""
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")

		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)

		if sData is not None:
			if sData.GetFriends() is not None and friendUid in sData.GetFriends():
				callback({"code":friendConsts.AlreadyFriend, "message":"已经是好友"})
				return
			if sData.GetFriends() is not None and len(sData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				callback({"code": friendConsts.YourFriendsMax, "message": "玩家数量达到上限"})
				return
			if sData.GetBlackList() is not None and friendUid in sData.GetBlackList():
				callback({"code": friendConsts.FriendInYourBlack, "message": "你已拉黑该玩家"})
				return
		else:
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
			self.system.mFriendDbManager.mFriends[selfUid] = sData
		if fData is not None:
			if fData.GetBlackList() is not None and selfUid in fData.GetBlackList():
				callback({"code": friendConsts.YouInFriendBlack, "message": "该玩家将你拉黑"})
				return
			if fData.GetFriends() is not None and len(fData.GetFriends()) >= self.FRIENDS_MAX_NUM:
				callback({"code": friendConsts.YouInFriendBlack, "message": "好友数量达到上限"})
				return
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.DelFriendRequest(selfUid)
		else:
			fData = friendData.CFriendData()
			fData.SetUid(friendUid)
			fData.AddFriend(selfUid)
			fData.DelFriendRequest(selfUid)
			self.system.mFriendDbManager.mFriends[friendUid] = fData
		# 互相都是好友
		sData.AddFriend(friendUid)
		sData.DelFriendRequest(friendUid)
		callback({"code": friendConsts.CodeSuc, "message": "成功"})
		self.system.mFriendDbManager.ServiceDeleteFriendRequest(selfUid, friendUid, lambda: self.outAfterAddFriendDelRequest(selfUid,friendUid))

	def outAfterAddFriendDelRequest(self, selfUid, friendUid):
		self.system.mFriendDbManager.ServiceInsertFriendShip(friendUid, selfUid, False, lambda: self.notifyAcceptFriend(friendUid, selfUid))
		self.system.mFriendDbManager.ServiceInsertFriendShip(selfUid, friendUid, False, lambda: self.notifyAcceptFriend(selfUid, friendUid))

	#删好友
	# =====删除好友
	def OutDelFriend(self, selfUid, friendUid, callback):
		"""
		由代码直接驱动，selfUid和friendUid解除好友关系， 第一阶段：从数据库加载selfUid和friendUid的好友信息到内存缓存
		"""
		# 先把数据加载进内存
		if selfUid <= 0 or friendUid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args:self.outRealDeleteFriend(args, callback), {"selfUid":selfUid,"friendUid":friendUid})

	def outRealDeleteFriend(self, args, callback):
		"""
		由代码直接驱动，selfUid和friendUid解除好友关系， 第二阶段：
		1、通过各种判定后，修改内存中的好友关系以及相关伴随状态
		2、然后修改数据库中对应的信息
		3、调用参数中的回调函数，返回最终处理的结果（成功/失败）
		4、通知被影响到的双方，好友关系解除（仅成功）
		"""
		logout.verbose('outRealDeleteFriend', args)
		selfUid = args['selfUid']
		friendUid = args['friendUid']
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)
		sData.DelFriend(friendUid)
		fData.DelFriend(selfUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(selfUid, friendUid)
		self.system.mChatRecordDbManager.DeleteChatRecord(friendUid, selfUid)
		self.system.mFriendDbManager.ServiceDeleteFriendShip(friendUid, selfUid, lambda: self.notifyDeleteFriend(friendUid, selfUid))
		self.system.mFriendDbManager.ServiceDeleteFriendShip(selfUid, friendUid, lambda: self.notifyDeleteFriend(selfUid, friendUid))
		redict = {}
		redict["code"] = friendConsts.CodeSuc
		redict["message"] = "成功！"
		callback(redict)

	#拉黑
	def OutAddBlack(self, selfUid, friendUid, callback):
		"""
		由代码直接驱动，selfUid把friendUid加入自己的黑名单列表中， 第一阶段：从数据库加载selfUid和friendUid的好友信息到内存缓存
		"""
		if selfUid <= 0 or friendUid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args:self.outRealAddBlack(args, callback), {"selfUid":selfUid,"friendUid":friendUid})

	def outRealAddBlack(self, args, callback):
		"""
		由代码直接驱动，selfUid把friendUid加入自己的黑名单列表中， 第二阶段：
		1、通过各种判定后，修改内存中的好友关系以及相关伴随状态
		2、然后修改数据库中对应的信息
		3、调用参数中的回调函数，返回最终处理的结果（成功/失败）
		4、通知被影响到的双方，selfUid把friendUid加入自己的黑名单列表中（仅成功）
		"""
		logout.info("outRealAddBlack", args)
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")

		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)

		if sData is not None:
			if sData.GetBlackList() is not None and len(sData.GetBlackList()) >= self.FRIENDS_MAX_NUM:
				callback({"code": friendConsts.YourFriendsMax, "message": "黑名单数量达到上限"})
				return
		else:
			sData = friendData.CFriendData()
			sData.SetUid(selfUid)
			self.system.mFriendDbManager.mFriends[selfUid] = sData
		if fData is None:
			fData = friendData.CFriendData()
			fData.SetUid(friendUid)
			self.system.mFriendDbManager.mFriends[friendUid] = fData
		if sData.GetFriends() is not None and friendUid in sData.GetFriends():
			sData.DelFriend(friendUid)
			fData.DelFriend(selfUid)
			self.system.mFriendDbManager.ServiceDeleteFriendShip(friendUid, selfUid,
																 lambda: self.notifyDeleteFriend(friendUid, selfUid))
			self.system.mFriendDbManager.ServiceDeleteFriendShip(selfUid, friendUid,
																 lambda: self.notifyDeleteFriend(selfUid, friendUid))
		sData.AddblackList(friendUid)
		callback({"code": friendConsts.CodeSuc, "message": "成功"})
		self.system.mFriendDbManager.ServiceInsertFriendBlack(selfUid, friendUid,
															  lambda: self.notifyAddBlack(selfUid, friendUid))
	def notifyAddBlack(self, selfUid, friendUid):
		"""
		通知被加入到黑名单中的被动方
		"""
		def GetOnlineCb(args):
			# 删除了好友，给friend所在的lobby发送消息
			serverId = args.get("serverId")
			if serverId:
				data = self.system.CreateEventData()
				data["neteaseId"] = selfUid
				data["friendUid"] = friendUid
				#self.system.NotifyToServerNode(serverId, friendConsts.AddBlackListRNotifyFromServiceEvent, data)
				data['isSuc'] = True
				data["errCode"] = friendConsts.CodeSuc
				data["showTip"] = False
				self.system.NotifyToServerNode(serverId, friendConsts.AddBlackListResultFromServiceEvent, data)
			else:
				logout.info("notifyAddBlack, player offline", selfUid)

		commonNetgameApi.GetOnlineServerInfoOfPlayer(selfUid, GetOnlineCb)

	#判断是否好友
	def OutIsFriend(self, selfUid, friendUid, callback):
		"""
		判断selfUid和friendUid双方是否是好友，第一阶段：从数据库加载selfUid和friendUid的好友信息到内存缓存
		"""
		if selfUid <= 0 or friendUid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args:self.realOutIsFriend(args, callback), {"selfUid":selfUid,"friendUid":friendUid})

	def realOutIsFriend(self, args, callback):
		"""
		判断selfUid和friendUid双方是否是好友，第二阶段：通过内存缓存数据判定后，通过参数中的回调函数返回结果
		"""
		logout.verbose('realOutIsFriend', args)
		selfUid = args['selfUid']
		friendUid = args['friendUid']
		
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		fData = self.system.mFriendDbManager.getFriendData(friendUid)

		if sData is not None:
			if sData.GetFriends() is not None and friendUid in sData.GetFriends():
				callback({"code": friendConsts.IsFriend, "message": "是好友"})
				return True
		callback({"code": friendConsts.IsNotFriend, "message": "不是好友"})
		return False
	
	#获取全部好友
	def OutGetFriends(self, selfUid, callback):
		"""
		获取selfUid的好友列表：
		1、从数据库加载selfUid的好友信息到内存缓存
		2、从内存缓存中获取好友列表信息，并通过参数中的回调函数返回结果
		"""
		if selfUid <= 0 :
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法", "friendsList":[]})
			return
		def QueryFriendsCB(reFriends, params):
			callback({"code": friendConsts.CodeSuc, "message": "成功", "friendsList":reFriends})
		self.system.mFriendDbManager.ServiceQueryFriendShipNew(selfUid, QueryFriendsCB, {"selfUid": selfUid})
		