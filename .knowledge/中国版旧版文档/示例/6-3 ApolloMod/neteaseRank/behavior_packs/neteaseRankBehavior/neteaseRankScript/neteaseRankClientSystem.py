import rankConsts as rankConsts
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import neteaseRankScript.ui.uiMgr as uiMgr
import neteaseRankScript.ui.uiDef as uiDef
from rankDataManager import RankDataManager

class RankClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mUIMgr = uiMgr.UIMgr()
		self.mRankDataManager = RankDataManager(self)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ServerSystemName, "ShowUIFromServerEvent", self, self.OnShowUIFromServerEvent)
		self.ListenForEvent(rankConsts.ModNameSpace, rankConsts.ServerSystemName, "ModConfigResponseFromServerEvent", self, self.OnModConfigResponseFromServerEvent)
	
	def OnModConfigResponseFromServerEvent(self, modConfig):
		"""
		来自server的排行榜配置信息
		"""
		self.modConfig = modConfig
		rankCol = self.modConfig["rankCol"]
		for oneRankColConfig in rankCol:
			self.mRankDataManager.mRankColList.append(oneRankColConfig["colName"])
			self.mRankDataManager.mRankColTitleList.append(oneRankColConfig["title"])
		self.mRankDataManager.mRemarksContent = self.modConfig["remarks_content"]
		self.mRankDataManager.mRankName = self.modConfig["rank_name"]
		
	
	def OnUiInitFinished(self, args):
		"""
		client初始化完成，通知server
		"""
		self.mUIMgr.Init(self)
		
		data = self.CreateEventData()
		data["entityId"] = clientApi.GetLocalPlayerId()
		self.NotifyToServer("ClientUiInitFinished", data)
		
	def GetRankDataManager(self):
		return self.mRankDataManager
		
	def OnShowUIFromServerEvent(self, args):
		"""
		来自server的事件，显示排行榜界面
		"""
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIRankUI)
		if ui:
			ui.ShowRankPanel()