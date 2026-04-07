# -*- coding:utf-8 -*-
import friendConsts as friendConsts
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import apolloCommon.mysqlPool as mysqlPool
import neteaseFriendScript.friendManager as friendManager
import neteaseFriendScript.playerManager as playerManager
import neteaseFriendScript.chatManager as chatManager
import neteaseFriendScript.friendCommon.friendDbManager as friendDbManager
import neteaseFriendScript.friendCommon.playerDbManager as playerDbManager
import neteaseFriendScript.friendCommon.chatRecordDbManager as chatRecordDbManager
import logout
import apolloCommon.commonNetgameApi as commonNetgameApi
#import neteaseFriendScript.friendCommon.httpApi as httpApi
import time
import timer
import Queue
import json

class FriendServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		
		
		self.InitMysqlDb()
		
		self.mFriendManager = friendManager.FriendManager(self)
		self.mChatManager = chatManager.ChatManager(self)
		self.mPlayerManager = playerManager.PlayerManager(self)
		
		self.mFriendDbManager = friendDbManager.FriendDbManager()
		self.mPlayerDbManager = playerDbManager.PlayerDbManager()
		self.mChatRecordDbManager = chatRecordDbManager.ChatDbManager()
		#self.mHttpApi = httpApi.HttpApi()

		self.Init()
		
		# self.RegisterRpcMethod(friendConsts.ModNameSpace, "testADD", self.OntestADD)
		# self.RegisterRpcMethod(friendConsts.ModNameSpace, "testDEL", self.OntestDEL)
		# self.RegisterRpcMethod(friendConsts.ModNameSpace, "testBLACK", self.OntestBLACK)
		# self.RegisterRpcMethod(friendConsts.ModNameSpace, "testCHAT", self.OntestCHAT)
		self.RegisterRpcMethod(friendConsts.ModNameSpace, "testChangeHead", self.testChangeHead)
		
	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseFriendScript')
		self.mFriendManager.Init(self.modConfig)
		self.mChatRecordDbManager.RECORD_MAX_NUM = self.modConfig.get("RECORD_MAX_NUM")
		self.mChatManager.RECORD_MAX_LENGTH = self.modConfig.get("RECORD_MAX_LENGTH")
	
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_Friend fail when init mysql")
			return False
		return True


	def Destroy(self):
		mysqlPool.Finish()
	
	#=====================对外接口==========================================	
	def OnDEL(self, args, callback):
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		self.mFriendManager.OutDelFriend(selfUid, friendUid, callback)
			
	def OnBLACK(self, args, callback):
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		self.mFriendManager.OutAddBlack(selfUid, friendUid, callback)
		
	def OnIsFriend(self, args, callback):
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		self.mFriendManager.OutIsFriend(selfUid, friendUid, callback)
		
	def OnCHAT(self, args, callback):
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		args["fromUid"] = selfUid
		args["toUid"] = friendUid
		message = args.get("message")
		self.mChatManager.OutChat(selfUid, friendUid, message, callback)
		
	def OnADD(self, args, callback):
		selfUid = args.get("selfUid")
		friendUid = args.get("friendUid")
		self.mFriendManager.OutAddFriend(selfUid, friendUid, callback)
	
	def testChangeHead(self, serverId, callbackId, args):
		playerDict = {}
		playerDict["selfUid"] = args.get("selfUid")
		playerDict["head_image"] = "textures/ui/netease_friend/icon10@3x"
		def tttttt(args):
			print args
		#self.OnChangeHead(playerDict, tttttt)
		
		
	def OnChangeHead(self, playerDict, callback):
		playerDict["uid"] = playerDict.get("selfUid")
		self.mPlayerManager.OnChangeHeadImage(playerDict, callback)
		
	def OnGetFriends(self, args, callback):
		selfUid = args.get("selfUid")
		self.mFriendManager.OutGetFriends(selfUid, callback)
	
	
		
	
		
	
	