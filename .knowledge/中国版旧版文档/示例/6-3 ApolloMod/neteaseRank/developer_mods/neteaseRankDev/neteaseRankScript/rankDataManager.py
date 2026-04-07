# -*- coding: utf-8 -*-
import time
import json
import apolloCommon.commonNetgameApi as commonNetgameApi
import apolloCommon.mysqlPool as mysqlPool
import logout
import rankConsts

class RankDataManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.mRankData = []
		self.system.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ServiceSystemName, "RefreshRankDataFromService", self, self.OnRefreshRankDataFromService)
	
	def Init(self):
		pass
	
	def OnRefreshRankDataFromService(self, args):
		"""
		收到service推送的排行榜刷新的事件，广播给当前所有的client
		"""
		rankData = args.get("rankData")
		self.mRankData = rankData
		self.system.BroadcastToAllClient("RefreshRankFromServerEvent", args)
		
	def GetRankData(self):
		return self.mRankData
	
	
		
	
			
	