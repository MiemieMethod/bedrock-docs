# -*- coding:utf-8 -*-
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import apolloCommon.mysqlPool as mysqlPool
import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import feedbackConsts
from feedbackManager import FeedbackManager

class FeedbackServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		self.mFeedbackManager = FeedbackManager(self)
		self.Init()
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChatEvent)
		self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ClientSystemName, 'ClientUiInitFinished', self, self.OnClientUiInitFinished)
		self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ClientSystemName, 'ShowTipsFromClientEvent', self, self.OnShowTipsFromClientEvent)
		#self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ClientSystemName, 'CommitFeedbackFromClientEvent', self, self.OnCommitFeedbackFromClientEvent)

	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseFeedbackScript')
		self.mFeedbackManager.Init()
		
	def OnShowTipsFromClientEvent(self, args):
		feedbackConsts.ShowAlert(args["playerId"], args["message"])
		
	# def OnCommitFeedbackFromClientEvent(self, args):
	# 	self.mFeedbackManager.OnCommitFeedbackFromClientEvent(args)

	def OnServerChatEvent(self, args):
		print "OnServerChatEvent1233", args
		playerId = args.get("playerId")
		message = args["message"]
		# import lobbyGame.netgameApi as lobbyGameApi
		# import json
		# transData = {'bornPos': [112,64,154], 'dim': 1}
		# lobbyGameApi.TransferToOtherServer(playerId, "game", json.dumps(transData))
		#self.mFeedbackManager.OnCommitFeedbackFromClientEvent({"message":message, "playerId":playerId, "tags":["故事背景", "模型", "场景"]})
		#self.NotifyToClient(playerId, "ShowUIFromServerEvent", {})
		
	def OnClientUiInitFinished(self, args):
		playerId = args.get("entityId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		nickName = netgameApi.GetPlayerNickname(playerId)
		self.NotifyToClient(playerId, "ModConfigResponseFromServerEvent", self.modConfig)
		self.NotifyToClient(playerId, "NotifyAllFeedbackTagsFromSeverEvent", {"feedbackTags": self.mFeedbackManager.GetAllFeedbackTags()})
		# for key, chatManager in self.mChatManagers.iteritems():
		# 	chatManager.QueryScreenUid(playerId, playerUid)
	
	def ServerGetFeedbackByCond(self, args, cb):
		self.mFeedbackManager.GetFeedbackByCond(args, cb)
	
		
		
		



		
		
	