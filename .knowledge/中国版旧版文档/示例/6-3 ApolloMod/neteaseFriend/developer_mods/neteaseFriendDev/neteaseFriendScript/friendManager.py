# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import server.extraServerApi as serverApi
import timer
import json


class FriendManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		
		# 加好友
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.AddFriendFromClientEvent, self, self.OnAddFriendFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.AddFriendResultFromServiceEvent, self, self.OnAddFriendResultFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName, friendConsts.AddFriendNotifyFromServiceEvent, self, self.OnAddFriendNotifyFromServiceEvent)
		
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName, "AddTempFriendResultFromServiceEvent", self, self.OnAddTempFriendResultFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName, "AddTempFriendNotifyFromServiceEvent", self, self.OnAddTempFriendNotifyFromServiceEvent)
		
		# 接受好友
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.AcceptFriendFromClientEvent, self, self.OnAcceptFriendFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.AcceptFriendResultFromServiceEvent, self,
		                    self.OnAcceptFriendResultFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.AcceptFriendNotifyFromServiceEvent, self,
		                    self.OnAcceptFriendNotifyFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                           friendConsts.RNFriendsUpdateFromServiceEvent, self,
		                           self.OnRNFriendsUpdateFromServiceEvent)
		
		# 拒绝好友
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.RefuseFriendFromClientEvent, self, self.OnRefuseFriendFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.RefuseFriendResultFromServiceEvent, self,
		                    self.OnRefuseFriendResultFromServiceEvent)
		
		# 刪除好友
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.DeleteFriendFromClientEvent, self, self.OnDeleteFriendFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.DeleteFriendResultFromServiceEvent, self,
		                    self.OnDeleteFriendResultFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.DeleteFriendNotifyFromServiceEvent, self,
		                    self.OnDeleteFriendNotifyFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, "DeleteTempFromClientEvent", self, self.OnDeleteTempFromClientEvent)
		
		# 刪除黑名单
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, friendConsts.DeleteBlackFromClientEvent, self, self.OnDeleteBlackFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.DeleteBlackListResultFromServiceEvent, self,
		                    self.OnDeleteBlackListResultFromServiceEvent)
		
		# 加入黑名单
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.AddBlackFromClientEvent, self, self.OnAddBlackFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.AddBlackListResultFromServiceEvent, self,
		                    self.OnAddBlackListResultFromServiceEvent)
		
		# 查找好友
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.SearchFriendFromClientEvent, self, self.OnSearchFriendFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                    friendConsts.SearchFriendAroundFromClientEvent, self,
		                    self.OnSearchFriendAroundFromClientEvent)
		
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName,
		                           "ClientFriendsRequestEvent", self, self.OnClientFriendsRequestEvent)
		
		self.mNeedSyncRNFriendsUids = []
		self.mSyncRNFriendsTimer = timer.TimerManager.addRepeatTimer(1, self.PollSyncRN)  # 1S 轮询一次,
		
	# =========同步RN好友
	def PollSyncRN(self):
		"""
		定时向RN请求一部分在线玩家的好友信息，并与本地数据同步
		"""
		if len(self.mNeedSyncRNFriendsUids) <= 0:
			return
		needSyncUid = self.mNeedSyncRNFriendsUids[0]
		del self.mNeedSyncRNFriendsUids[0]
		self.system.mHttpApi.GetRNFriends(needSyncUid, lambda reponse: self.GetRNFriendsCb(needSyncUid, reponse))
		
	def GetRNFriendsCb(self, needSyncUid, response):
		"""
		向RN请求在线玩家的好友信息后，发送给service，实现本地数据同步
		"""
		logout.info("GetRNFriendsCb, uid %s, response:%s" % (needSyncUid, response))
		if 0 != response['code']:
			logout.error('GetRNFriends Response error!uid:%s, response:%s'% (needSyncUid, response))
			return
		entity = response['entity']
		if not entity:
			return
		entity["needSyncUid"] = needSyncUid
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.SyncRNFriendFromServerEvent, entity)
		
		
	def OnClientFriendsRequestEvent(self, args):
		"""
		client发送的，获取面向指定uid的加好友申请的事件
		1、假如此uid的玩家的好友信息内存缓存不存在，则会从数据库读取
		2、完成后驱动【doNotifyFriendUpdate】打包发送玩家的好友相关信息（包括但不限于好友列表，黑名单等）给client
		"""
		logout.info("OnClientFriendsRequestEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		self.system.mFriendDbManager.ServerPrePareData(selfUid, lambda a,args: self.doNotifyFriendUpdate(selfUid, args), args)
		
	def doNotifyFriendUpdate(self, selfUid, args):
		"""
		打包发送指定uid的玩家的好友相关信息（包括但不限于好友列表，黑名单等）给client
		"""
		logout.verbose("doNotifyFriendUpdate: ", " args: ", args)
		entityId = args.get("entityId")
		data = self.system.CreateEventData()
		friendData = self.system.mFriendDbManager.getFriendData(selfUid)
		data['RNFriends'] = list(friendData.GetRNFriend())
		data['friendUids'] = friendData.GetFriends()
		data['friendRequests'] = friendData.GetFriendRequests()
		data['friendBlackUids'] = friendData.GetBlackList()
		data['friendUnReadList'] = friendData.GetUnReadFriendList()
		data['tempList'] = friendData.GetTempFriends()
		self.system.NotifyToClient(entityId, "ServerFriendsResponseEvent", data)
		
	def RealCreateTempChat(self, args, callback = None):
		"""
		创建临时好友关系，并开始聊天
		"""
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		def DoCallBack(data):
			if callback is not None:
				callback(data)
		if selfUid == friendUid:
			#TODO 返回不能给自己创建临时聊天
			DoCallBack({"suc":False, "reason":"你不能给自己创建临时聊天！"})
			return
		if friendUid is None:
			#TODO 返回好友不存在
			DoCallBack({"suc": False, "reason": "好友不存在"})
			return
		def CreateTempChatFromServerCb(suc, data):
			if not suc:
				DoCallBack({"suc":False, "reason":"请求超时！"})
				return
			DoCallBack(data)
			if data.get("suc") == True:
				entityId = netgameApi.GetPlayerIdByUid(selfUid)
				openTemp = data.get("openTemp", True)
				self.system.NotifyToClient(entityId, "OpenFriendList", {"uid":friendUid, "openTemp":openTemp})
		self.system.RequestToService(friendConsts.ModNameSpace, "CreateTempChatFromServer", args, CreateTempChatFromServerCb, 5)
	
	# 加好友==========
	def OnAddFriendFromClientEvent(self, args):
		logout.info("OnAddFriendFromClientEvent", args)
		self.ServerDoAddFriend(args)
		
	def ServerDoAddFriend(self, args):
		"""
		来自client的发送加好友申请的事件，转发给service处理
		"""
		if args.has_key("entityId"):
			playerId = args["entityId"]
			selfUid = netgameApi.GetPlayerUid(playerId)
			args["selfUid"] = selfUid
		else:
			selfUid = args["selfUid"]
		#selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		message = args.get("message")
		if selfUid == friendUid:
			self.notifyAddFriendResult(args["entityId"], None, False, False, friendConsts.FriendIsYou, True)
			return
		if friendUid is None:
			self.notifyAddFriendResult(args["entityId"], None, False, False, friendConsts.FriendNone, True)
			return
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.AddFriendFromServerEvent, args)
	
	def notifyAddFriendResult(self, entityId, friendId, isSuc, needRefresh, errCode, needShow = False):
		'''
		通知客户端申请好友的结果
		'''
		logout.info('notifyAddFriendResult', isSuc, errCode)
		data = self.system.CreateEventData()
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['needShow'] = needShow
		self.system.NotifyToClient(entityId, "AddFriendResultEvent", data)
	
	def OnAddFriendResultFromServiceEvent(self, args):
		'''
		申请好友
		'''
		logout.info("OnAddFriendResultFromServiceEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		logout.info("OnAddFriendResultFromServiceEvent1", entityId)
		logout.info("OnAddFriendResultFromServiceEvent2", args["showTip"])
		if args.get("showTip", False) == True:
			logout.info("OnAddFriendResultFromServiceEvent3", args.get("showTip", False))
			self.notifyAddFriendResult(entityId, args["friendUid"], args['isSuc'], args['needRefresh'], args['errCode'], True)
	
	def OnAddFriendNotifyFromServiceEvent(self, args):
		'''
		收到申请好友的请求
		'''
		logout.info("OnAddFriendNotifyFromServiceEvent", args)
		uid = args.get("uid")
		entityId = netgameApi.GetPlayerIdByUid(uid)
		#auid = args.get("auid")
		self.system.NotifyToClient(entityId, "NewRequestFromServerEvent", args)
		self.notifyFriendRequestUpdate(entityId, uid, False)
	
	def notifyFriendRequestUpdate(self, entityId, uid, useCache, needFreshClient = True):
		if entityId is None or uid is None:
			return
		args = entityId, uid
		
		def doNotifyFriendRequestUpdate(friendRequest, args):
			entityId, uid = args
			data = self.system.CreateEventData()
			data["friendsRequest"] = friendRequest
			data["needFreshClient"] = needFreshClient
			self.system.NotifyToClient(entityId, "FriendsRequestFromServerEvent", data)
		
		self.system.mFriendDbManager.ServerGetFriendRequest(uid, useCache, lambda friendRequest, args:doNotifyFriendRequestUpdate(friendRequest, args), args)
	
	# 接受好友========
	def OnAcceptFriendFromClientEvent(self, args):
		"""
		来自client的同意某人的加好友申请的事件，转发给service处理
		"""
		logout.info("OnAcceptFriendFromClientEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		#selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		if selfUid == friendUid:
			self.notifyAcceptFriendResult(args["entityId"], None, False, False, friendConsts.FriendIsYou)
			return
		if friendUid is None:
			self.notifyAcceptFriendResult(args["entityId"], None, False, False, friendConsts.FriendNone)
			return
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.AcceptFriendFromServerEvent, args)
	
	def OnAcceptFriendResultFromServiceEvent(self, args):
		'''
		来自service的，好友关系成立的事件
		'''
		logout.info("OnAcceptFriendResultFromServiceEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		if args.get("showTip", False) == True:
			self.notifyAcceptFriendResult(entityId, args["friendUid"], args['isSuc'], args['needRefresh'], args['errCode'], True)
		if args['needRefresh']:
			self.notifyFriendListUpdate(entityId, args["neteaseId"], False)
			self.notifyFriendRequestUpdate(entityId, args["neteaseId"], False, False)
			
	def OnRNFriendsUpdateFromServiceEvent(self, args):
		"""
		来自service的，同步RN好友信息完成的事件
		server需要更新自己本地缓存后，发送玩家好友相关信息更新的事件给client
		"""
		logout.info("OnRNFriendsUpdateFromServiceEvent", args)
		uid = args.get("uid")
		entityId = netgameApi.GetPlayerIdByUid(uid)
		self.notifyRnFriendListUpdate(entityId, uid, False)
	
	def notifyRnFriendListUpdate(self, entityId, uid, useCache, callback=None):
		if entityId is None or uid is None:
			return
		args = entityId, uid
		
		def doNotifyFriendListUpdate(friendList, args):
			entityId, uid = args
			data = self.system.CreateEventData()
			data["RNfriendUids"] = list(friendList)
			logout.info("RNFriendsListFromServerEvent", data)
			self.system.NotifyToClient(entityId, "RNFriendsListFromServerEvent", data)
			if callback is not None:
				callback()
		
		self.system.mFriendDbManager.ServerGetRNFriendShip(uid, lambda friendList, args: doNotifyFriendListUpdate(friendList,
		                                                                                                   args), args)
	
	def OnAcceptFriendNotifyFromServiceEvent(self, args):
		"""
		来自service的，同意加好友申请的事件
		1、通过重新读取数据库信息的方式强制更新内存缓存，
		2、发送玩家好友相关信息更新的事件给client
		"""
		logout.info("OnAcceptFriendNotifyFromServiceEvent", args)
		uid = args.get("uid")
		entityId = netgameApi.GetPlayerIdByUid(uid)
		self.notifyFriendListUpdate(entityId, uid, False)
		
	def OnAddTempFriendNotifyFromServiceEvent(self, args):
		"""
		来自service的，新增临时好友关系的事件
		1、通过重新读取数据库信息的方式强制更新内存缓存，
		2、发送玩家临时好友信息更新的事件给client
		"""
		logout.info("OnAcceptFriendNotifyFromServiceEvent", args)
		uid = args.get("uid")
		entityId = netgameApi.GetPlayerIdByUid(uid)
		self.notifyTempListUpdate(entityId, uid, False)
		
	def OnAddTempFriendResultFromServiceEvent(self, args):
		"""
		来自service的，发送新建临时好友关系的结果事件
		"""
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		if args.get("showTip", False) == True:
			self.notifyAcceptFriendResult(entityId, args["friendUid"], args['isSuc'], args['needRefresh'], args['errCode'], True)
		def afterNotifyTempList():
			self.system.NotifyToClient(entityId, "OpenFriendList", {"uid": args["friendUid"], "openTemp": args.get("openTemp", True)})
		if args['needRefresh']:
			self.notifyTempListUpdate(entityId, args["neteaseId"], False, afterNotifyTempList)
	
	def notifyAcceptFriendResult(self, entityId, friendId, isSuc, needRefresh, errCode, needShow = False):
		'''
		通知客户端接受好友的结果
		'''
		logout.info('notifyAcceptFriendResult', isSuc, errCode)
		data = self.system.CreateEventData()
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['needShow'] = needShow
		self.system.NotifyToClient(entityId, "AcceptFriendResultEvent", data)
		
	def notifyAddTempResult(self, entityId, friendId, isSuc, needRefresh, errCode, needShow = False):
		'''
		通知客户端接受好友的结果
		'''
		logout.info('notifyAddTempResult', isSuc, errCode)
		data = self.system.CreateEventData()
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		data['needShow'] = needShow
		self.system.NotifyToClient(entityId, "AddTempResultEvent", data)
	
	def notifyTempListUpdate(self, entityId, uid, useCache, callback=None):
		"""
		1、useCache=False，通过重新读取数据库信息的方式强制更新内存缓存中的临时好友信息
		2、useCache=True，优先从内存缓存中，次优先从数据库中，读取玩家临时好友信息
		3、发送玩家临时好友信息更新的事件给client
		"""
		if entityId is None or uid is None:
			return
		args = entityId, uid
		
		def doNotifyTempListUpdate(tempList, args):
			entityId, uid = args
			data = self.system.CreateEventData()
			data["tempList"] = tempList
			data["uid"] = uid
			self.system.NotifyToClient(entityId, "TempListFromServerEvent", data)
			#self.system.BroadcastEvent("FriendsListChangeEvent", data)
			if callback is not None:
				callback()
		
		self.system.mFriendDbManager.ServerGetTemp(uid, useCache, lambda tempList, args: doNotifyTempListUpdate(tempList, args), args)
	
	def notifyFriendListUpdate(self, entityId, uid, useCache, callback=None):
		"""
		1、useCache=False，通过重新读取数据库信息的方式强制更新内存缓存中的好友列表信息
		2、useCache=True，优先从内存缓存中，次优先从数据库中，读取玩家好友列表信息
		3、发送玩家好友列表信息更新的事件给client
		"""
		if entityId is None or uid is None:
			return
		args = entityId, uid
		
		def doNotifyFriendListUpdate(friendList, args):
			entityId, uid = args
			data = self.system.CreateEventData()
			data["friendUids"] = friendList
			data["uid"] = uid
			self.system.NotifyToClient(entityId, "FriendsListFromServerEvent", data)
			#self.system.BroadcastEvent("FriendsListChangeEvent", data)
			if callback is not None:
				callback()
		
		self.system.mFriendDbManager.ServerGetFriendShip(uid, useCache, lambda friendList, args:doNotifyFriendListUpdate(friendList, args), args)
	
	# 拒绝好友
	def OnRefuseFriendFromClientEvent(self, args):
		"""
		来自client的，拒绝某个玩家发来的加好友申请的事件，转发给service处理
		"""
		logout.info("OnRefuseFriendFromClientEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		#selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.RefuseFriendFromServerEvent, args)
	
	def OnRefuseFriendResultFromServiceEvent(self, args):
		"""
		来自service的，拒绝某个玩家发来的加好友申请的结果事件，驱动更新面向对应uid玩家的好友申请
		"""
		logout.info("OnRefuseFriendResultFromServiceEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		uid = args["neteaseId"]
		if args.get("showTip", False) == True:
			self.system.NotifyToClient(entityId, 'RefuseFriendResultEvent', args)
		self.notifyFriendRequestUpdate(entityId, uid, False, False)
	
	# 删除好友
	def OnDeleteFriendFromClientEvent(self, args):
		"""
		来自client的，从好友列表中删除指定uid玩家的事件
		"""
		logout.info("OnDeleteFriendFromClientEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		#selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		if selfUid == friendUid:
			self.notifyDelFriendResult(args["entityId"], None, False, False, "你不能删除自己！")
			return
		if friendUid is None:
			self.notifyDelFriendResult(args["entityId"], None, False, False, "目标好友不存在！")
			return
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.DeleteFriendFromServerEvent, args)
	
	def OnDeleteFriendResultFromServiceEvent(self, args):
		'''
		接受好友
		'''
		logout.info("OnDeleteFriendResultFromServiceEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		if args.get("showTip", False) == True:
			self.notifyDelFriendResult(entityId, args["friendUid"], args['isSuc'], args['needRefresh'], args['errCode'])
		if args['needRefresh']:
			self.notifyFriendListUpdate(entityId, args["neteaseId"], False)
			self.notifyFriendRequestUpdate(entityId, args["neteaseId"], False)
	
	def OnDeleteFriendNotifyFromServiceEvent(self, args):
		"""
		来自service的，删除好友结果的事件
		"""
		logout.info("OnDeleteFriendNotifyFromServiceEvent", args)
		uid = args.get("uid")
		entityId = netgameApi.GetPlayerIdByUid(uid)
		self.notifyFriendListUpdate(entityId, uid, False)
	
	def notifyDelFriendResult(self, entityId, friendId, isSuc, needRefresh, errCode):
		'''
		通知客户端删除好友的结果
		'''
		logout.info('notifyDelFriendResult', isSuc, errCode)
		data = self.system.CreateEventData()
		data['friendUid'] = friendId
		data['isSuc'] = isSuc
		data['needRefresh'] = needRefresh
		data['errCode'] = errCode
		self.system.NotifyToClient(entityId, "DelFriendResultEvent", data)
	
	# 移除黑名单
	def OnDeleteBlackFromClientEvent(self, args):
		"""
		来自client的，把某人从指定uid玩家的黑名单中移除的处理，转发给service处理
		"""
		logout.info("OnDeleteBlackFromClientEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		friendUid = args.get("friendUid")
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.DeleteBlackFromServerEvent, args)
		
	def OnDeleteTempFromClientEvent(self, args):
		"""
		来自client的，把某人从指定uid玩家的临时好友中移除的处理，转发给service处理
		"""
		logout.info("OnDeleteTempFromClientEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		friendUid = args.get("friendUid")
		self.system.RequestToService(friendConsts.ModNameSpace, "DeleteTempFromServerEvent", args)
	
	def OnDeleteBlackListResultFromServiceEvent(self, args):
		"""
		来自service的，从黑名单中移除指定uid玩家的结果事件
		"""
		logout.info("OnDeleteBlackListResultFromServiceEvent", args)
		uid = args["neteaseId"]
		entityId = netgameApi.GetPlayerIdByUid(uid)
		if args.get("showTip", False) == True:
			self.system.NotifyToClient(entityId, "DeleteBlackListResultEvent", args)
		self.notifyFriendBlackUpdate(entityId, uid, False)
	
	def notifyFriendBlackUpdate(self, entityId, uid, useCache):
		"""
		1、useCache=False，通过重新读取数据库信息的方式强制更新内存缓存中的黑名单信息
		2、useCache=True，优先从内存缓存中，次优先从数据库中，读取玩家黑名单信息
		3、发送玩家黑名单列表信息更新的事件给client
		"""
		# if entityId is None or uid is None:
		# 	return
		args = entityId, uid
		logout.info("notifyFriendBlackUpdate", entityId, uid, useCache)
		def doNotifyFriendBlackUpdate(friendBlack, args):
			entityId, uid = args
			data = self.system.CreateEventData()
			data["friendBlackUids"] = friendBlack
			logout.info("FriendsBlackFromServerEvent11111", entityId, uid, data)
			self.system.NotifyToClient(entityId, "FriendsBlackFromServerEvent", data)
		
		self.system.mFriendDbManager.ServerGetFriendBlack(uid, useCache, lambda friendList, args:doNotifyFriendBlackUpdate(friendList, args), args)
	
	# 加入黑名单
	def OnAddBlackFromClientEvent(self, args):
		logout.info("OnAddBlackFromClientEvent", args)
		self.ServerDoAddBlack(args)
		
	def ServerDoAddBlack(self, args):
		"""
		来自client的，把指定uid的玩家，加入自己的黑名单列表的请求，转发给service户理
		"""
		if args.has_key("entityId"):
			playerId = args["entityId"]
			selfUid = netgameApi.GetPlayerUid(playerId)
			args["selfUid"] = selfUid
		else:
			selfUid = args["selfUid"]
		friendUid = args.get("friendUid")
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.AddBlackFromServerEvent, args)
	
	def OnAddBlackListResultFromServiceEvent(self, args):
		"""
		来自service的，把指定uid的玩家啊，加入自己黑名单中的事件
		"""
		logout.info("OnAddBlackListResultFromServiceEvent", args)
		uid = args["neteaseId"]
		entityId = netgameApi.GetPlayerIdByUid(uid)
		if args.get("showTip", False) == True:
			self.system.NotifyToClient(entityId, "AddBlackListResultEvent", args)
		self.notifyFriendBlackUpdate(entityId, uid, False)
		self.notifyFriendListUpdate(entityId, uid, False)
	
	def OnSearchFriendFromClientEvent(self, args):
		"""
		来自client的，搜索指定uid或者指定昵称的的玩家的请求，转发给service
		"""
		logout.info("OnSearchFriendFromClientEvent", args)
		#userName = args.get("nickname")
		searchTxt = args.get("searchTxt")
		entityId = args.get("entityId")
		#entityId = netgameApi.GetPlayerIdByUid(args["selfUid"])
		if searchTxt == "" or searchTxt is None:
			return
		def OnSearchFriendCb(playerData, args):
			logout.info("OnSearchFriendCb", playerData)
			self.system.NotifyToClient(entityId, "SearchFriendResultEvent", playerData)
		self.system.mPlayerDbManager.GetPlayerDataByUserName(searchTxt, OnSearchFriendCb, args)
	
	def OnSearchFriendAroundFromClientEvent(self, args):
		"""
		来自client的，查找附近玩家的请求
		"""
		logout.info("OnSearchFriendAroundFromClientEvent", args)
		entityId = args.get("entityId")
		playerUid = netgameApi.GetPlayerUid(entityId)
		self.notifyFriendListUpdate(entityId, playerUid, True, self.RealSearchFriendAround(args))
	
	def RealSearchFriendAround(self, args):
		"""
		查找附近的玩家，并发送给client
		"""
		entityId = args.get("entityId")
		comp = serverApi.CreateComponent(entityId, "Minecraft", "game")
		aroundPlayerIds = comp.GetEntitiesAroundByType(entityId, 5, 319)
		logout.info("aroundPlayerIds", aroundPlayerIds)
		aroundPlayerUids = []
		for aroundPlayerId in aroundPlayerIds:
			if aroundPlayerId == entityId:
				continue
			aroundPlayerUid = netgameApi.GetPlayerUid(aroundPlayerId)
			aroundPlayerUids.append(aroundPlayerUid)
			
			#self.system.mPlayerDbManager.QueryPlayerData(aroundPlayerUid, True, OnSearchFriendAroundCb)
		self.system.NotifyToClient(entityId, "SearchFriendAroundResultEvent", {"aroundPlayerUids": aroundPlayerUids})