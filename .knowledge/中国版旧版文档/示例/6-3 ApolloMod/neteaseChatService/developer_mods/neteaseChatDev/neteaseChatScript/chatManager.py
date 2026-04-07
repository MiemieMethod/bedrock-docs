# -*- coding:utf-8 -*-
import chatConsts as chatConsts
import logout
import apolloCommon.commonNetgameApi as commonNetgameApi
import time
import timer
import Queue
import json

class ChatManager(object):
	def __init__(self, system, channel):
		import weakref
		self.system = weakref.proxy(system)
		self.mChatChannel = channel
		self.mChatRecords = []
		
	def InsertChatMes(self, args):
		print "serviceInsertChatMes", args
		playerUid = args["playerUid"]
		chatDict = self.GenChatDict(args)
		# if self.mChatRecords.has_key(playerUid) == False:
		# 	self.mChatRecords[playerUid] = []
		self.mChatRecords.append(chatDict)
		self.TellServerNewChat(chatDict)
		
	def GenChatDict(self, args):
		chatDict = {
			"playerUid": args["playerUid"],
			"nickName": args["nickName"],
			"playerLevel": args["playerLevel"],
			"chatType": args["chatType"],
			"mes": args["mes"],
			"infoDict": args.get("infoDict", {}),
			"chatChannel": args["chatChannel"],
			"chatTime": time.time()#用于客户端排序
		}
		return chatDict
	
	def TellServerNewChat(self, chatDict):
		if self.mChatChannel != chatConsts.ALL_SERVER_CHANNEL:
			self.system.NotifyToServerNode(self.mChatChannel, "newChatFromServiceEvent", chatDict)
		else:
			serverlist = self.system.GetCommonConfig()
			for serverid in serverlist:
				self.system.NotifyToServerNode(serverid, "newChatFromServiceEvent", chatDict)
	
		
	