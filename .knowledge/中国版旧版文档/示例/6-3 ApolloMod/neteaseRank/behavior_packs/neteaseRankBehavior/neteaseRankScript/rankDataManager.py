# -*- coding: utf-8 -*-
import time
import json
import logout
import rankConsts
import neteaseRankScript.ui.uiDef as uiDef

class RankDataManager(object):
	def __init__(self, system):
		import weakref
		self.system = weakref.proxy(system)
		self.mRankData = []
		self.mRankColList = []
		self.mRankColTitleList = []
		self.mRemarksContent = ""
		self.mRankName = ""
		self.system.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ServerSystemName, "RefreshRankFromServerEvent", self, self.OnRefreshRankDataFromServer)
	
	def Init(self):
		pass
	
	def OnRefreshRankDataFromServer(self, args):
		"""
		来自server的排行榜刷新事件，界面如果处于显示状态，需要刷新界面
		"""
		rankData = args.get("rankData")
		self.mRankData = rankData
		ui = self.system.mUIMgr.GetUI(uiDef.UIDef.UIRankUI)
		if ui and ui.mIsShow == True:
			ui.ShowRankPanel()
	
	def GetRankData(self):
		return self.mRankData
	
	def GetRankColList(self):
		return self.mRankColList
	
	def GetRemarksContent(self):
		return self.mRemarksContent
	
	def GetRankName(self):
		return self.mRankName
	
	def GetRankColTitleList(self):
		return self.mRankColTitleList
	
	
		
	
			
	