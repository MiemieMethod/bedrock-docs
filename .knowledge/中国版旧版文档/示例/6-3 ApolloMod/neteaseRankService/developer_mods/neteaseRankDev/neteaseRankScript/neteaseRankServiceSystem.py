# -*- coding:utf-8 -*-
import rankConsts as rankConsts
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
from rankDataManager import RankDataManager
import logout
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import service.netgameApi as netServiceApi

class RankServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		
		self.mConnectedSid = {}
		self.mRankDataManager = RankDataManager(self)
		self.Init()
		self.RegisterRpcMethod(rankConsts.ModNameSpace, "CommitRankDataFromServerEvent", self.OnCommitRankDataFromServerEvent)
		#self.RegisterRpcMethod(rankConsts.ModNameSpace, "GetRankDataFromServerEvent", self.OnGetRankDataFromServerEvent)
		self.RegisterRpcMethod(rankConsts.ModNameSpace, "DeleteRankDataFromMasterEvent", self.OnDeleteRankDataFromMasterEvent)
		self.RegisterRpcMethod(rankConsts.ModNameSpace, "CommitRankDataFromMasterEvent", self.OnCommitRankDataFromMasterEvent)
		self.RegisterRpcMethod(rankConsts.ModNameSpace, "ServerReadyEvent", self.OnServerReadyEvent)
		self.ListenForEvent(serviceApi.GetEngineNamespace(),serviceApi.GetEngineSystemName(),"ServerDisconnectEvent",self,self.OnServerDisconnectEvent)
	
	def Init(self):
		self.modConfig = commonNetgameApi.GetModJsonConfig('neteaseRankScript')
		self.mRankDataManager.Init()
		#self.mRankType = self.modConfig.get("rank_type")
	
	def OnServerReadyEvent(self, serverId, callbackId, args):
		"""
		部署了排行榜插件的server会向service注册自己的serverId，用于广播一些信息的时候定位哪些server需要广播
		"""
		serverType = args.get("serverType")
		if serverId not in self.mConnectedSid:
			self.mConnectedSid[serverId] = serverType
		print "OnServerReadyEvent", self.mConnectedSid
			
	def OnServerDisconnectEvent(self, args):
		"""
		server与service的连接断开时，需要更新缓存中的需要广播的server列表
		"""
		serverId = args.get("serverId")
		if serverId in self.mConnectedSid.keys():
			self.mConnectedSid.pop(serverId)
		print "OnServerDisconnectEvent", self.mConnectedSid
	
	def OnDeleteRankDataFromMasterEvent(self, serverId, callbackId, args):
		"""
		处理来自master的运营指令：【删除一条指定排名的排行榜记录】
		"""
		index = args.get("index")
		self.OnDelOneRankData(index)
		self.SendResponseToMaster(serverId, callbackId, 0, "成功")
		
	def OnCommitRankDataFromMasterEvent(self, serverId, callbackId, args):
		"""
		处理来自master的运营指令：【新增一条排行榜记录】
		"""
		oneRankData = args.get("oneRankData")
		fromId = args.get("fromId")
		serverType = args.get("serverType")
		self.mRankDataManager.OutInsertRankData(oneRankData, serverType, fromId)
		self.SendResponseToMaster(serverId, callbackId, 0, "成功")
		
	def SendResponseToMaster(self, serverId, callbackId, code, message):
		'''
		返回消息给master
		'''
		print "SendResponseToMaster", serverId, callbackId, code
		response = {}
		response['code'] = code
		response['message'] = message
		self.ResponseToServer(serverId, callbackId, response)
		
	def OnCommitRankDataFromServerEvent(self, serverId, callbackId, args):
		"""
		来自server的请求：【新增一条排行榜记录】
		"""
		commonConfig = netServiceApi.GetCommonConfig()
		serverType = ""
		for conf in commonConfig.get("serverlist", []):
			sid = conf.get('serverid')
			if sid == serverId:
				serverType = conf.get("type")

		oneRankData = args.get("oneRankData")
		fromId = args.get("fromId")
		#isCover = args.get("isCover", True)
		self.mRankDataManager.OutInsertRankData(oneRankData, serverType, fromId)
		
	def OnDelOneRankData(self, rank):
		"""
		删除一条指定排名的排行榜记录
		"""
		return self.mRankDataManager.DeleteRankData(rank)

	def OnCleareRankData(self):
		"""
		清空排行榜全部记录
		"""
		return self.mRankDataManager.ClearRankData()
	
	def OnRankAward(self, maxIndex):
		"""
		开始排行榜结算，最多结算到前maxIndex名
		"""
		self.mRankDataManager.realRankAward(maxIndex)
		
	def OnGetRankData(self):
		"""
		获取当前排行榜的排名信息
		"""
		return self.mRankDataManager.realGetRankData()