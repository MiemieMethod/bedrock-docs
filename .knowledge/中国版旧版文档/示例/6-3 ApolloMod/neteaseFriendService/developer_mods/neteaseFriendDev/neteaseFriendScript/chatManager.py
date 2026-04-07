# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import apiUtil
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


class ChatManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.RECORD_MAX_LENGTH = 30
		
		self.system.RegisterRpcMethod(friendConsts.ModNameSpace, friendConsts.ChatFromServerEvent, self.OnChatFromServerEvent)
	
	# =======聊天
	def OnChatFromServerEvent(self, serverId, callbackId, args):
		"""
		来自server的一个玩家向另一个玩家私聊的请求，处理逻辑第一阶段
		1、接收到私聊事件后，对聊天消息的文本进行检查
		2、判断私聊双方的好友相关的信息，是否已经从数据库中读取到内存缓存中了
		3、私聊双方的好友相关信息，尚未读取到内存缓存中，那么就先从数据库中读取对应信息
		4、读取数据库并更新内存缓存之后，调用【OnRealChat】继续处理
		"""
		logout.info("OnChatFromServerEvent", args)
		fromUid = args.get("fromUid")
		toUid = args.get("toUid")
		message = args.get("message")
		currentTime = time.time()
		args["chatTime"] = currentTime
		if apiUtil.GetTextViewLength(message) <= self.RECORD_MAX_LENGTH:
			self.system.mFriendDbManager.PrepareFriendData([fromUid, toUid], lambda args: self.OnRealChat(args),
                                               {"fromUid": fromUid, "toUid": toUid, "message": message, "currentTime":currentTime, "serverId":serverId, "chatTime":currentTime})
		else:
			self.ChatResult(serverId, fromUid, toUid, False, message, currentTime, "消息长度超过限制")
			
	def OnRealChat(self, args):
		"""
		来自server的一个玩家向另一个玩家私聊的请求，处理逻辑第二阶段
		1、判断私聊双方是否存在于对方的黑名单之内
		2、向聊天记录数据库，插入新的聊天记录，并更新内存中的聊天记录缓存
		3、完成后，调用【OnChatCb】继续处理
		"""
		fromUid = args.get("fromUid")
		toUid = args.get("toUid")
		message = args.get("message")
		serverId = args.get("serverId")
		currentTime = time.time()
		sData = self.system.mFriendDbManager.getFriendData(fromUid)
		fData = self.system.mFriendDbManager.getFriendData(toUid)
		if sData is not None:
			if sData.GetBlackList() is not None and toUid in sData.GetBlackList():
				self.ChatResult(serverId, fromUid, toUid, False, message, currentTime, "不能给黑名单玩家发消息")
				return
		if fData is not None:
			if fData.GetBlackList() is not None and fromUid in fData.GetBlackList():
				self.ChatResult(serverId, fromUid, toUid, False, message, currentTime, "该玩家将你拉黑")
				return
				
			
		self.system.mChatRecordDbManager.InsertChatRecord(fromUid, toUid, message, currentTime, lambda ret: self.OnChatCb(ret, serverId, args))
			
	def OnChatCb(self, ret, serverId, args):
		"""
		来自server的一个玩家向另一个玩家私聊的请求，处理逻辑第三阶段
		1、向私聊发起者所在的server，发送私聊消息成功的事件
		2、从redis中读取私聊目标玩家的在线信息
		3、假如私聊目标玩家在线，那么向目标玩家所在的server，发送有人私聊你的事件
		4、假如私聊目标玩家不在线，那么向数据库（以及内存缓存）插入有未读聊天消息的记录
		"""
		logout.info("OnChatCb", ret, args)
		fromUid = args.get("fromUid")
		toUid = args.get("toUid")
		message = args.get("message")
		chatTime = args.get("chatTime")
		self.ChatResult(serverId, fromUid, toUid, ret, message, chatTime)
		if ret is not None:
			def GetOnlineCb(args):
				friendLobby = args.get("serverId")
				if friendLobby:
					self.NotifyNewChat(friendLobby, toUid, fromUid, message, chatTime, ret)
				else:
					self.system.mFriendManager.addUnreadMessageFriend(toUid, fromUid)
			
			commonNetgameApi.GetOnlineServerInfoOfPlayer(toUid, GetOnlineCb)
	
	def ChatResult(self, lobbyId, uid, friendId, ret, message, chatTime, reason = ""):
		"""
		向位于指定server的指定uid的玩家，发送私聊的结果的事件
		"""
		data = self.system.CreateEventData()
		data["neteaseId"] = uid
		data["friendUid"] = friendId
		if ret is not None:
			data["result"] = True
			data["chatIndex"] = ret
		else:
			data["result"] = False
			data["reason"] = reason
		data["message"] = message
		data["chatTime"] = chatTime
		self.system.NotifyToServerNode(lobbyId, friendConsts.ChatResultFromServiceEvent, data)
	
	def NotifyNewChat(self, lobbyId, uid, friendId, message, chatTime, ret):
		"""
		向位于指定server的指定uid的玩家，发送有人向他私聊的事件
		"""
		data = self.system.CreateEventData()
		data["neteaseId"] = uid
		data["friendUid"] = friendId
		data["message"] = message
		data["chatTime"] = chatTime
		data["chatIndex"] = ret
		self.system.NotifyToServerNode(lobbyId, friendConsts.NewChatFromServiceEvent, data)


	def OutChat(self, selfUid, friendUid, message, callback):
		"""
		直接从service端驱动的，实现两个玩家之间一次私聊的函数，整体处理逻辑与【OnChatFromServerEvent】一致
		"""
		if selfUid <= 0 or friendUid <= 0:
			callback({"code": friendConsts.CodeFailed, "message": "uid不合法"})
			return
		self.system.mFriendDbManager.PrepareFriendData([selfUid, friendUid], lambda args: self.outRealChat(args, callback),
		                                               {"selfUid": selfUid, "friendUid": friendUid, "message":message})
	
	def outRealChat(self, args, callback):
		fromUid = args.get("selfUid")
		toUid = args.get("friendUid")
		message = args.get("message")
		currentTime = time.time()
		sData = self.system.mFriendDbManager.getFriendData(fromUid)
		fData = self.system.mFriendDbManager.getFriendData(toUid)
		
		if sData is not None:
			if sData.GetFriends() is None or toUid not in sData.GetFriends():
				callback({"code":friendConsts.CodeFailed, "message":"不是好友不能发消息"})
				return
			if sData.GetBlackList() is not None and toUid in sData.GetBlackList():
				callback({"code": friendConsts.CodeFailed, "message": "不能给黑名单玩家发消息"})
				return
		else:
			callback({"code": friendConsts.CodeFailed, "message": "不是好友不能发消息"})
			return
		if fData is not None:
			if fData.GetBlackList() is not None and fromUid in fData.GetBlackList():
				callback({"code": friendConsts.CodeFailed, "message": "该玩家将你拉黑"})
				return
		
		if apiUtil.GetTextViewLength(message) <= self.RECORD_MAX_LENGTH:
			self.system.mChatRecordDbManager.InsertChatRecord(fromUid, toUid, message, currentTime,
			                                                  lambda ret: self.outChatCb(ret, fromUid, toUid, message,
			                                                                             currentTime))
			callback({"code": friendConsts.CodeSuc, "message": "成功"})
		else:
			callback({"code": 102, "message": "消息长度超过限制"})
			return
	
	def outChatCb(self, ret, fromUid, toUid, message, currentTime):
		if ret is not None:
			def GetOnlineCb1(args):
				logout.info("GetOnlineCb1", args)
				friendLobby = args.get("serverId")
				if friendLobby:
					self.NotifyNewChat(friendLobby, toUid, fromUid, message, currentTime, ret)
				else:
					self.system.mFriendManager.addUnreadMessageFriend(toUid, fromUid)

			commonNetgameApi.GetOnlineServerInfoOfPlayer(toUid, GetOnlineCb1)

			def GetOnlineCb2(args):
				logout.info("GetOnlineCb2", args)
				serverId = args.get("serverId")
				if serverId:
					self.ChatResult(serverId, fromUid, toUid, ret, message, currentTime)
			commonNetgameApi.GetOnlineServerInfoOfPlayer(fromUid, GetOnlineCb2)