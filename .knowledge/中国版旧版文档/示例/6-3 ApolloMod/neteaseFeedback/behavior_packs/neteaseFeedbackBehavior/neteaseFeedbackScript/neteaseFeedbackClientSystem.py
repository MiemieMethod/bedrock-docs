# -*- coding: utf-8 -*-
import feedbackConsts as feedbackConsts
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import neteaseFeedbackScript.ui.uiMgr as uiMgr
import neteaseFeedbackScript.ui.uiDef as uiDef

class FeedbackClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print namespace, systemName, "====init===="
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ServerSystemName, "ModConfigResponseFromServerEvent", self, self.OnModConfigResponseFromServerEvent)
		self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ServerSystemName, "NotifyAllFeedbackTagsFromSeverEvent", self, self.OnNotifyAllFeedbackTagsFromSeverEvent)
		self.ListenForEvent(feedbackConsts.ModNameSpace, feedbackConsts.ServerSystemName, "ShowUIFromServerEvent", self, self.OnShowUIFromServerEvent)
		self.mUIMgr = uiMgr.UIMgr()
		self.mLocalPlayerId = clientApi.GetLocalPlayerId()
		
	def OnUiInitFinished(self, args):
		self.mUIMgr.Init(self)
		data = self.CreateEventData()
		data["entityId"] = self.mLocalPlayerId
		self.NotifyToServer("ClientUiInitFinished", data)

	def Destroy(self):
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUiInitFinished)
		if self.mUIMgr:
			self.mUIMgr.Destroy()

	def OnModConfigResponseFromServerEvent(self, modConfig):
		self.modConfig = modConfig
		
	def OnNotifyAllFeedbackTagsFromSeverEvent(self, args):
		self.mFeedbackTags = args["feedbackTags"]
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFeedbackMain)
		ui.InitFeedbackTags(self.mFeedbackTags)
	
	def OnShowUIFromServerEvent(self, args):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFeedbackMain)
		if ui:
			ui.Show(True)
			
	def ShowFeedbackMainUI(self, args):
		ui = self.mUIMgr.GetUI(uiDef.UIDef.UIFeedbackMain)
		if ui:
			ui.Show(args["isShow"])

	# -------------------------------------------------------------------------------------
	def GetUiMgr(self):
		return self.mUIMgr
