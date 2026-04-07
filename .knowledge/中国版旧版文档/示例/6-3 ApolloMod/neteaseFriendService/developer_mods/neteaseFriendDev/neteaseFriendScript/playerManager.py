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


class PlayerManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		
		# =====
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.AddPlayerFromServerEvent,
		                       self.OnAddPlayerFromServer)
		# self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.DelPlayerFromServerEvent,
		#                        self.OnDelPlayerFromServer)
	
	# 玩家登陆
	def OnAddPlayerFromServer(self, serverId, callbackId, args):
		"""
		server发送的玩家登录事件，假如此玩家是首次登录游戏，那么会在玩家基本信息数据库中插入一位新玩家的信息
		"""
		logout.info("OnAddPlayerFromServer", args)
		uid = args.get("uid")
		username = args.get("nickName")
		head_image = "textures/ui/netease_friend/img01@3x"  # TODO 默认头像框
		
		def OnQueryPlayerDataCb(playerData):
			if playerData is None:
				#不存在
				playerDict = {}
				playerDict["uid"] = uid
				playerDict["username"] = username
				playerDict["head_image"] = head_image
				self.system.mPlayerDbManager.InSertPlayerData(playerDict, None)
			data = self.system.CreateEventData()
			data['selfUid'] = uid
			data['changeUid'] = uid
			self.system.NotifyToServerNode(serverId, friendConsts.UpdatePlayerDataFromServiceEvent, data)
		
		self.system.mPlayerDbManager.QueryPlayerData(uid, True, OnQueryPlayerDataCb)
		
	def OnChangeHeadImage(self, playerDict, callback):
		"""
		修改指定uid的玩家的头像信息，第一阶段
		1、检查uid的合法性
		2、修改数据库中指定uid玩家的头像信息，成功后修改内存缓存中的头像信息
		3、通知主动修改头像的server，修改头像信息成功
		4、拉取指定uid的玩家的好友信息，并传递给【OnChangeImageQueryFriendShip】函数
		"""
		logout.info("OnChangeHeadImage", playerDict)
		uid = playerDict.get("uid")
		if uid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		def OnChangeImageCb(args):
			logout.info("OnChangeImageCb", args)
			if args is not None:
				#commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, lambda args:self.TellServerChangePlayerData(args, uid))
				self.system.mFriendDbManager.ServiceQueryFriendShip([uid], self.OnChangeImageQueryFriendShip, {"selfUid": uid})
				callback({"code": friendConsts.CodeSuc, "message": "成功"})
			else:
				callback({"code": friendConsts.CodeFailed, "message": "失败"})
		self.system.mPlayerDbManager.ChangePlayerHeadImage(playerDict, OnChangeImageCb)
		
	def OnChangeImageQueryFriendShip(self, args):
		"""
		修改指定uid的玩家的头像信息，第二阶段
		1、遍历玩家的全部好友，并依次从redis中获取对应玩家所在的服务器信息
		2、将返回的信息，传递给【TellServerChangePlayerData】函数
		"""
		selfUid = args.get("selfUid")
		sData = self.system.mFriendDbManager.getFriendData(selfUid)
		if sData is None:
			friendUids = []
		else:
			friendUids = sData.GetFriends()
		if friendUids:
			commonNetgameApi.GetOnlineServerInfoOfMultiPlayers(friendUids + [selfUid], lambda args:self.TellServerChangePlayerData(args, selfUid))
	
		# commonNetgameApi.GetOnlineServerInfoOfPlayer(uid, lambda args:self.TellServerChangePlayerData(args, uid))
		
	def TellServerChangePlayerData(self, args, changeUid):
		"""
		修改指定uid的玩家的头像信息，第三阶段
		1、给所有在线的好友对应的server，推送指定uid的玩家的头像改变的事件
		"""
		logout.info("TellServerChangePlayerData", args)
		for data in args:
			serverId = data.get("serverId")
			if serverId is None:
				continue
			reDict = {}
			reDict["selfUid"] = data.get("uid")
			reDict["changeUid"] = changeUid
			reDict["needChangeClient"] = True
			self.system.NotifyToServerNode(serverId, friendConsts.UpdatePlayerDataFromServiceEvent, reDict)
		
	# self.mPlayerDbManager.QueryPlayerData(uid, True, OnQueryPlayerDataCb)
	
	# def NotifyFriendUpdateState(self, friendUids, args):
	# 	uid, state = args
	#
	# 	def GetPlayersOnlineCb(args):
	# 		# 登陆了就告诉所有好友
	# 		for info in args:
	# 			data = self.system.CreateEventData()
	# 			data['changeUid'] = uid
	# 			data['state'] = state
	# 			serverId = info.get("serverId")
	# 			friendUid = info.get("uid")
	# 			data['selfUid'] = friendUid
	# 			if serverId:
	# 				self.doNotifyFriendUpdateState(serverId, data)
	#
	# 	commonNetgameApi.GetOnlineServerInfoOfMultiPlayers(friendUids, GetPlayersOnlineCb)
	
	def doNotifyFriendUpdateState(self, serverId, data):
		self.system.NotifyToServerNode(serverId, friendConsts.FriendStateResponseFromServiceEvent, data)
	
	# 玩家退出
	def OnDelPlayerFromServer(self, serverId, callbackId, args):
		uid = args.get("uid")
		#self.system.mFriendDbManager.PrepareFriendData([uid],
		
		# def OnQueryPlayerDataCb(playerData):
		# 	self.system.mPlayerDbManager.getPlayerCaches(uid).SetOnline(True)
		# 	args = uid, False  # 离线
		# 	self.system.mFriendDbManager.ServerGetFriendShip(uid, True, lambda friendUids, args:self.NotifyFriendUpdateState(friendUids, args), args)
		#
		# self.system.mPlayerDbManager.QueryPlayerData(uid, True, OnQueryPlayerDataCb)
		# data = self.system.CreateEventData()
		# data['changeUid'] = uid
		# data['state'] = False
		# data['selfUid'] = uid
		# self.system.NotifyToServerNode(serverId, friendConsts.UpdatePlayerDataFromServiceEvent, data)
