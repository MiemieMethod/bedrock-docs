# -*- coding:utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import neteaseChatScript.chatManager as chatManager
import logout
import apolloCommon.commonNetgameApi as commonNetgameApi
import chatConsts
#import neteaseChatScript.ChatCommon.httpApi as httpApi
import time
import timer
import Queue
import json
import service.netgameApi as netServiceApi

class ChatServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		self.mChatManagers = {}
		self.RegisterRpcMethod(chatConsts.ModNameSpace, "ChatFromServerEvent", self.OnChatFromServerEvent)
		self.ListenForEvent(serviceApi.GetEngineNamespace(),serviceApi.GetEngineSystemName(),"NetGameCommonConfChangeEvent", self, self.OnNetGameCommonConfChangeEvent)
		#self.mChatManager = chatManager.ChatManager(self)
		self.mCommonConfig = None
		self.Init()
	
	def GetCommonConfig(self):
		return self.mCommonConfig
		
	def OnNetGameCommonConfChangeEvent(self, args):
		serverIds = set()
		ccfg = netServiceApi.GetCommonConfig()
		print "OnNetGameCommonConfChangeEvent", ccfg
		for conf in ccfg.get("serverlist", []):
			if conf.get("app_type") in ("game", "lobby"):
				serverid = int(conf.get('serverid'))#用serverid来区分频道
				serverIds.add(serverid)
				if self.mChatManagers.has_key(serverid) == False:
					self.mChatManagers[serverid] = chatManager.ChatManager(self, serverid)
		if self.mChatManagers.has_key(chatConsts.ALL_SERVER_CHANNEL) == False:
			self.mChatManagers[chatConsts.ALL_SERVER_CHANNEL] = chatManager.ChatManager(self, chatConsts.ALL_SERVER_CHANNEL)

		self.mCommonConfig = serverIds

	def OnChatFromServerEvent(self, serverId, callbackId, args):
		chatChannel = args["chatChannel"]
		print "OnChatFromServerEvent", self.mChatManagers.keys()
		if self.mChatManagers.has_key(chatChannel):
			self.mChatManagers[chatChannel].InsertChatMes(args)

		
	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseChatScript')
		commonConf = netServiceApi.GetCommonConfig()
		serverIds = set()
		for conf in commonConf['serverlist']:
			if conf['app_type'] in ("game", "lobby"):
				serverId = int(conf['serverid'])
				serverIds.add(serverId)
				self.mChatManagers[serverId] = chatManager.ChatManager(self, serverId)
		self.mChatManagers[chatConsts.ALL_SERVER_CHANNEL] = chatManager.ChatManager(self, chatConsts.ALL_SERVER_CHANNEL)
		self.mCommonConfig = serverIds
	
	
	#=====================对外接口==========================================
	
	
		
	
		
	
	