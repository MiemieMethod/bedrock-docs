# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import neteaseDungeonScript.ui.uiMgr as uiMgr
import neteaseDungeonScript.ui.uiDef as uiDef

class DungeonClientSys(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mUIMgr = uiMgr.UIMgr()
		self.ListenForEvent(dungeonConsts.ModNameSpace, dungeonConsts.LobbyServerSystemName,
							dungeonConsts.DungeonFullMessageEvent, self, self.OnShowDungeonFullMessage)
		self.ListenForEvent(extraClientApi.GetEngineNamespace(), extraClientApi.GetEngineSystemName(),
							dungeonConsts.UiInitFinished, self, self.OnUiInitFinished)

	def OnShowDungeonFullMessage(self, args):
		print 'OnShowDungeonFullMessage', args
		uidScreen = self.mUIMgr.GetUI(uiDef.UIDef.UIDungeon)
		uidScreen.Show(args['dungeonName'])

	def OnUiInitFinished(self, args):
		print 'OnUiInitFinished'
		self.mUIMgr.Init()

	def GetUiMgr(self):
		return self.mUIMgr

	def Destroy(self):
		if self.mUIMgr:
			self.mUIMgr.Destroy()
