# -*- coding:utf-8 -*-
import rankConsts as rankConsts
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

import logout
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
from rankDataManager import RankDataManager

class RankServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		
		self.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ClientSystemName, 'ClientUiInitFinished', self, self.OnClientUiInitFinished)
		self.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ServiceSystemName, 'SendMailFromServiceEvent', self, self.OnSendMailFromServiceEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServiceConnectEvent', self, self.OnServiceConnectEvent)
		self.mRankDataManager = RankDataManager(self)
		self.Init()
		
	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseRankScript')
		self.mRankDataManager.Init()
	
	def OnServiceConnectEvent(self, args):
		"""
		成功连接到service后，延时0.5秒向service发送信息标识本server部署了排行榜插件（用于service广播）
		"""
		def doServerReady():
			serverType = commonNetgameApi.GetServerType()
			self.RequestToService(rankConsts.ModNameSpace, "ServerReadyEvent", {"serverType": serverType})
		import apolloCommon.commonNetgameApi as commonNetgameApi
		commonNetgameApi.AddTimer(0.5, doServerReady)
		
	def OnClientUiInitFinished(self, args):
		"""
		client初始化完成，发送第一条消息给server，此时server需要发送排行信息与排行配置信息给client
		"""
		playerId = args.get("entityId")
		rankData = self.mRankDataManager.GetRankData()
		dict = {"rankData": rankData}
		print "RefreshRankFromServerEvent", dict
		self.NotifyToClient(playerId, "RefreshRankFromServerEvent", dict)
		self.NotifyToClient(playerId, "ModConfigResponseFromServerEvent", self.modConfig)
		
	def OnSendMailFromServiceEvent(self, args):
		"""
		service驱动的发送邮件事件，并不承担排行榜相关的具体逻辑
		"""
		mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
		print "OnSendMailFromServiceEvent", args, mailSystem
		if mailSystem:
			uid = args.get("uid")
			mail_titile = args.get("mail_titile")
			mail_content = args.get("mail_content")
			award_content = args.get("award_content")
			award_num = args.get("award_num")
			itemDict = {
				'itemName': award_content,
				'count': award_num,
				'auxValue':  0,
			}
			print "SendMailToUser", [uid], mail_titile, mail_content, [itemDict, ]
			mailSystem.SendMailToUser([uid], mail_titile, mail_content, [itemDict, ], 86400, "开发组")
	
	def OnServerChat(self, args):
		playerId = args['playerId']
		playerUid = netgameApi.GetPlayerUid(playerId)
		line = args["message"].split(" ")
		command = line[0]
		dict = {}
		self.NotifyToClient(playerId, "ShowUIFromServerEvent", {})
		import random
		# if command == "1":
		#	a = ["gmy", "yfg", "txl", "lrl"]
		#	self.OutCommitRankData(random.randint(1,10), [a[random.randint(0,4)], random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)])

	def OpenRankUI(self, uid):
		"""
		通知指定uid的client，打开排行榜界面
		"""
		playerId = netgameApi.GetPlayerIdByUid(uid)
		if not playerId:
			print 'can not get playerId by uid: %s' % uid
			return
		self.NotifyToClient(playerId, "ShowUIFromServerEvent", {})
		
	def OutCommitRankData(self, fromId, oneRankData):
		"""
		向排行榜提交一条数据（转发给service处理）
		"""
		dict = {}
		dict["oneRankData"] = oneRankData
		dict["fromId"] = fromId
		self.RequestToService(rankConsts.ModNameSpace, "CommitRankDataFromServerEvent", dict)