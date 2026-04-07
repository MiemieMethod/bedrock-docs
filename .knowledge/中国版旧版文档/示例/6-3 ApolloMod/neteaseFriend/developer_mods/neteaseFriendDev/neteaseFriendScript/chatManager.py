# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import server.extraServerApi as serverApi


class ChatManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		
		# 聊天
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, friendConsts.ChatFromClientEvent,
		                    self, self.OnChatFromClientEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, "ClientChatRecordRequestEvent", self, self.OnClientChatRecordRequestEvent)
		#self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ClientSystemName, "ClientLastChatTimeRequestEvent", self, self.OnClientLastChatTimeRequestEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.ChatResultFromServiceEvent, self, self.OnChatResultFromServiceEvent)
		self.system.ListenForEvent(friendConsts.ModNameSpace, friendConsts.ServiceSystemName,
		                    friendConsts.NewChatFromServiceEvent, self, self.OnNewChatFromServiceEvent)
	
	# 完整的一次私聊请求的处理流程：
	# 1、client向server发送私聊事件
	# 2、server接收到事件后，对事件参数进行检查后，把事件转发给service
	# 3、service接收到私聊事件后，对聊天消息的文本进行检查
	# 4、service判断私聊双方的好友相关的信息，是否已经从数据库中读取到内存缓存中了
	# 5、假如私聊双方的好友相关信息，尚未读取到内存缓存中，那么就先从数据库中读取对应信息到内存缓存中
	# 6、判断私聊双方是否存在于对方的黑名单之内
	# 7、向聊天记录数据库，插入一条新的聊天记录
	# 8、插入成功后，判定是否此两人的私聊记录是否已经读取到内存中了
	# 9、假如尚未读取，那么从聊天记录数据库，读取此两人的私聊记录到内存中
	# 10、把新的一条聊天记录，保存到内存缓存中
	# 11、向私聊发起者所在的server，发送私聊消息成功的事件，对应server接收到此事件后，转发给client -- 私聊发送方逻辑链完成
	# 12、从redis中读取私聊目标玩家的在线信息
	# 13、假如私聊目标玩家在线，那么向目标玩家所在的server，发送有人私聊你的事件，对应server接收到此事件后，转发给client -- 私聊接收方逻辑链完成情境一
	# 14、假如私聊目标玩家不在线，那么向数据库（以及内存缓存）插入有未读聊天消息的记录
	# 15、当私聊目标玩家上线后，会收到所有存在未读聊天消息的玩家列表，并逐一拉取对应的聊天记录 -- 私聊接收方逻辑链完成情境二
	def OnChatFromClientEvent(self, args):
		"""
		来自client的私聊请求，转发给service处理
		"""
		logout.info("OnChatFromClientEvent", args)
		playerId = args["entityId"]
		fromUid = netgameApi.GetPlayerUid(playerId)
		toUid = args.get("friendUid")
		if toUid is None:
			return
		message = args.get("message")
		data = {}
		data["fromUid"] = fromUid
		data["toUid"] = toUid
		data["message"] = message
		self.system.RequestToService(friendConsts.ModNameSpace, friendConsts.ChatFromServerEvent, data)
	
	def OnChatResultFromServiceEvent(self, args):
		"""
		来自service的，发送一条私聊消息事件的返回结果（包括成功和失败），
		1、假如成功，会更新server的聊天记录缓存后，
		2、无论是否成功，都会把发送私聊的结果转发给client
		"""
		logout.info("OnChatResultFromServiceEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		self.system.NotifyToClient(entityId, "ChatResultEvent", args)
		ret = args["result"]
		if ret:
			self.system.mChatRecordDbManager.InsertChatRecordInCache(args["neteaseId"], args["friendUid"], args["message"],
			                                                  args["chatIndex"])
	
	def OnNewChatFromServiceEvent(self, args):
		"""
		来自service的，被私聊的事件
		1、会更新server的聊天记录缓存
		2、把被私聊的事件，转发给对应的client
		"""
		logout.verbose("NewChatEvent", args)
		entityId = netgameApi.GetPlayerIdByUid(args["neteaseId"])
		self.system.NotifyToClient(entityId, "NewChatEvent", args)
		self.system.mChatRecordDbManager.InsertChatRecordInCache(args["friendUid"], args["neteaseId"], args["message"], args["chatIndex"])
		
	def OnClientChatRecordRequestEvent(self, args):
		"""
		来自client的，请求两个玩家之间的聊天历史记录的事件、
		1、直接从数据库（或本地内存缓存）中，读取聊天历史记录
		2、通知service，修改此两个玩家之间的聊天记录状态为【已读】
		"""
		logout.info("ClientChatRecordRequestEvent", args)
		playerId = args["entityId"]
		selfUid = netgameApi.GetPlayerUid(playerId)
		args["selfUid"] = selfUid
		friendUid = args.get("friendUid")
		self.system.mChatRecordDbManager.QueryChatRecord(selfUid, friendUid, lambda records: self.ClientChatRecordResponseEvent(
			args["entityId"], selfUid, friendUid, records), False)
		readUnread = args.get("readUnread", True)
		if readUnread:
			self.readUnReadMessage(selfUid, friendUid)
		
	def readUnReadMessage(self, uid, friendId):
		"""
		通知service，修改此两个玩家之间的聊天记录状态为【已读】
		"""
		data = self.system.CreateEventData()
		data["selfUid"] = uid
		data["friendUid"] = friendId
		self.system.RequestToService(friendConsts.ModNameSpace, "ReadMessageEvent", data)
	
	def ClientChatRecordResponseEvent(self, entityId, uid, friendId, records):
		"""
		从数据库（或本地内存缓存）中，获取聊天历史记录后，返回给client的函数
		"""
		logout.verbose("ClientChatRecordResponseEvent", entityId, uid, friendId, records)
		data = self.system.CreateEventData()
		data["neteaseId"] = uid
		data["friendUid"] = friendId
		data["records"] = records
		self.system.NotifyToClient(entityId, "ClientChatRecordResponseEvent", data)
		
		