# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
import neteaseFlyScript.flyClientConsts as flyConsts
import neteaseFlyScript.mgr.uiMgr as uiMgr
from neteaseFlyScript.ui.uiDef import UIDef

ClientSystem = extraClientApi.GetClientSystemCls()

class FlyClientSystem(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self,namespace,systemName)
		self.mUIMgr = uiMgr.UIMgr()
		# 引擎事件
		self.ListenEvents()

	def Destroy(self):
		if self.mUIMgr:
			self.mUIMgr.Destroy()
		# 引擎事件
		self.UnListenEvents()
		ClientSystem.Destroy(self)

	def ListenEvents(self):
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.SyncConfigEvent,
							self, self.OnSyncConfig)
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ChangeFlyStateEvent,
							self, self.OnFlyStateChange)
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ShowTipsEvent,
							self, self.OnShowTips)
		self.ListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ChangeFlyPermissionEvent,
							self, self.OnFlyEnableChange)

	def UnListenEvents(self):
		self.UnListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							"UiInitFinished", self, self.OnUiInitFinished)
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.SyncConfigEvent,
							self, self.OnSyncConfig)
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ChangeFlyStateEvent,
							self, self.OnFlyStateChange)
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ShowTipsEvent,
							self, self.OnShowTips)
		self.UnListenForEvent(flyConsts.ModNameSpace, flyConsts.ServerSystemName, flyConsts.ChangeFlyPermissionEvent,
							self, self.OnFlyEnableChange)

	# ------------------------------------------------------------------------------------------
	def OnUiInitFinished(self, args):
		print "OnUiInitFinished"
		self.NotifyToServer(flyConsts.ClientEnterEvent, {"playerId":extraClientApi.GetLocalPlayerId()})

	def OnFlyStateChange(self, args):
		print "ClientFlyStateChange"
		state = args.get("state", False)
		if self.GetFlyPluginUI():
			self.GetFlyPluginUI().ChangeFlyState(state)

	def OnFlyEnableChange(self, args):
		print "OnFlyEnableChange"
		flyEnable = args.get("flyEnable", False)
		if self.GetFlyPluginUI():
			self.GetFlyPluginUI().ChangeFlyEnable(flyEnable)

	def OnSyncConfig(self, args):
		print "OnSyncConfig", str(args)
		self.mUIMgr.Init()
		if self.GetFlyPluginUI():
			self.GetFlyPluginUI().SyncConfig(args)

	def OnShowTips(self, args):
		tips = args.get("tips", "")
		if len(tips) > 0:
			if self.GetFlyPluginUI():
				self.GetFlyPluginUI().ShowTips(tips)

	# ------------------------------------------------------------------------------------------
	def GetUiMgr(self):
		return self.mUIMgr

	def GetFlyPluginUI(self):
		return self.mUIMgr.GetUI(UIDef.UIFlyPlugin)