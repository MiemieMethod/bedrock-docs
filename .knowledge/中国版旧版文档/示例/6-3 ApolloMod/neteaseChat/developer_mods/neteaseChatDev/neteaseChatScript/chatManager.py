# -*- coding:utf-8 -*-
import chatConsts as chatConsts
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import server.extraServerApi as serverApi
import apolloCommon.mysqlPool as mysqlPool
import time

class ChatManager(object):
	def __init__(self, system, channel):
		import weakref
		self.system = weakref.proxy(system)
		self.mChatChannel = channel
		self.mChatRecords = []
		self.mScreenUids = {}
		self.mDirty = False
		#self.mRepeatedTellClientNewChatTimer = timer.TimerManager.addRepeatTimer(1.5, self.RepeatedTellClientNewChat)
		
	# def RepeatedTellClientNewChat(self):
	# 	if self.mDirty == True:
	# 		self.TellClientNewChat(chatDict)
		
	def InsertChatMes(self, chatDict):
		print "ServerInsertChatMes", chatDict
		playerUid = chatDict["playerUid"]
		# if self.mChatRecords.has_key(playerUid) == False:
		# 	self.mChatRecords[playerUid] = []
		self.mChatRecords.append(chatDict)
		self.TellClientNewChat(chatDict)
		
	def TellClientNewChat(self, chatDict):
		self.system.BroadcastToAllClient("newChatFromServerEvent", chatDict)
		print "newChatFromServerEvent", chatDict
		
	def QueryScreenUid(self, playerId, uid, callback = None):
		if self.mScreenUids.has_key(uid):
			callback(self.mChatChannel, self.mScreenUids[uid])
			self.system.NotifyToClient(playerId, "TellCilentScreenUidsEvent", {"channel": self.mChatChannel, "screenUids": self.mScreenUids[uid]})
			return
		sql = "SELECT * FROM neteaseChatScreen WHERE uid = %s AND channel = %s"
		sqlparam = (uid, self.mChatChannel, )
		def ServerQueryScreenCb(args):
			logout.verbose("query ServerQueryScreenCb uid=%s" % uid)
			suids = []
			if args is None:
				logout.error("query ServerQueryScreenCb FOR [%d] FAIL" % uid)
			else:
				for data in args:
					if data is not None:
						suid = data[1]
						suids.append(suid)
				self.mScreenUids[uid] = suids
				self.system.NotifyToClient(playerId, "TellCilentScreenUidsEvent", {"chatChannel":self.mChatChannel, "screenUids":suids})
			#logout.info("ServiceInsertFriendShip test test", self.getFriendData(uid).GetFriends())
			if callback is not None:
				callback(self.mChatChannel, suids)

		mysqlPool.AsyncQueryWithOrderKey(str([uid]), sql, sqlparam, lambda args: ServerQueryScreenCb(args))
