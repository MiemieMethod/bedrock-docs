# -*- coding: utf-8 -*-

import neteaseSquadScript.squadConst as squadConst
import client.extraClientApi as clientApi
import neteaseSquadScript.ui.uiMgr as uiMgr
import neteaseSquadScript.ui.uiDef as uiDef

ClientSystem = clientApi.GetClientSystemCls()


class SquadClientSystem(ClientSystem):
	@property
	def EnableUI(self):
		return self.mEnableUI

	@EnableUI.setter
	def EnableUI(self, flag):
		self.mEnableUI = flag
		if self.EnableUI:
			if self.mSquadApplyUINode:
				self.mSquadApplyUINode.activate()
			if self.mSquadReplyUINode:
				self.mSquadReplyUINode.activate()
			if self.mSquadClsBtnUINode:
				self.mSquadClsBtnUINode.activate()
			if self.mSquadMainUINode:
				self.mSquadMainUINode.activate()
		else:
			if self.mSquadApplyUINode:
				self.mSquadApplyUINode.deactivate()
			if self.mSquadReplyUINode:
				self.mSquadReplyUINode.deactivate()
			if self.mSquadClsBtnUINode:
				self.mSquadClsBtnUINode.deactivate()
			if self.mSquadMainUINode:
				self.mSquadMainUINode.deactivate()

	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		self.mPlayerId = clientApi.GetLocalPlayerId()
		self.mSquadUINode = None
		self.mInputUINode = None
		self.mEnableUI = False
		
		self.mSquadApplyUINode = None
		self.mSquadAlertUINode = None
		self.mSquadReplyUINode = None
		self.mSquadClsBtnUINode = None
		self.mSquadMainUINode = None
		
		self.mUIMgr = uiMgr.UIMgr()

		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), squadConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerUpdateEvent, self, self.OnSquadPlayerUpdate)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerRecruitEvent, self, self.OnSquadPlayerRecruit)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SetupSquadEvent, self, self.OnSetupSquad)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.DissolveSquadEvent, self, self.OnDissolveSquad)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerLeaveEvent, self, self.OnSquadPlayerLeave)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplyListEvent, self, self.OnSquadApplyList)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadRecruitListEvent, self, self.OnSquadRecruitList)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplicantsClearEvent, self, self.OnSquadApplicantsClear)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadInvitePlayerEvent, self, self.OnSquadInvitePlayer)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.AssembleEvent, self, self.OnAssemble)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadAppendPlayerEvent, self, self.OnSquadAppendPlayer)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadRecruitmentApplyEvent, self, self.OnSquadRecruitmentApply)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplicationNoticeEvent, self, self.OnSquadApplicationNotice)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerDisconnectEvent, self, self.OnSquadPlayerDisconnect)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerReconnectEvent, self, self.OnSquadPlayerReconnect)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.JoinSquadEvent, self, self.OnJoinSquad)
		self.ListenForEvent(squadConst.ModName, squadConst.ServerSystemName, 'EnableUI', self, self.OnEnableUI)

	def Destroy(self):
		self.mSquadUINode = None
		self.mInputUINode = None
		
		self.mSquadApplyUINode = None
		self.mSquadAlertUINode = None
		self.mSquadReplyUINode = None
		self.mSquadClsBtnUINode = None
		self.mSquadMainUINode = None
		
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), squadConst.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerUpdateEvent, self, self.OnSquadPlayerUpdate)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerRecruitEvent, self, self.OnSquadPlayerRecruit)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SetupSquadEvent, self, self.OnSetupSquad)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.DissolveSquadEvent, self, self.OnDissolveSquad)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerLeaveEvent, self, self.OnSquadPlayerLeave)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplyListEvent, self, self.OnSquadApplyList)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadRecruitListEvent, self, self.OnSquadRecruitList)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplicantsClearEvent, self, self.OnSquadApplicantsClear)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadInvitePlayerEvent, self, self.OnSquadInvitePlayer)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.AssembleEvent, self, self.OnAssemble)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadAppendPlayerEvent, self, self.OnSquadAppendPlayer)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadRecruitmentApplyEvent, self, self.OnSquadRecruitmentApply)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadApplicationNoticeEvent, self, self.OnSquadApplicationNotice)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerDisconnectEvent, self, self.OnSquadPlayerDisconnect)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.SquadPlayerReconnectEvent, self, self.OnSquadPlayerReconnect)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, squadConst.JoinSquadEvent, self, self.OnJoinSquad)
		self.UnListenForEvent(squadConst.ModName, squadConst.ServerSystemName, 'EnableUI', self, self.OnEnableUI)
		if self.mUIMgr:
			self.mUIMgr.Destroy()

	def OnEnableUI(self, data):
		self.EnableUI = data['flag']

	def OnUiInitFinished(self, *args):
		self.NotifyToServer(squadConst.SquadPlayerCheckEvent, {
			'playerId': self.mPlayerId
		})
		# # 注册UI 详细解释参照《UI API》
		# clientApi.RegisterUI(squadConst.ModName, squadConst.squadUIName, squadConst.squadUIClsPath, squadConst.squadUIScreenDef)
		# # 创建UI 详细解释参照《UI API》
		# clientApi.CreateUI(squadConst.ModName, squadConst.squadUIName, {"isHud": 1})
		# self.mSquadUINode = clientApi.GetUI(squadConst.ModName, squadConst.squadUIName)
		# if self.mSquadUINode:
		# 	self.mSquadUINode.InitScreen()
		# else:
		# 	print '==== %s ====' % 'create UI: %s failed' % squadConst.squadUIScreenDef
		# # 注册UI 详细解释参照《UI API》
		# clientApi.RegisterUI(squadConst.ModName, 'inputUI', "neteaseSquadScript.inputUI.InputScreen", 'inputUI.main')
		# # 创建UI 详细解释参照《UI API》
		# self.mInputUINode = clientApi.CreateUI(squadConst.ModName, 'inputUI', {"isHud": 1})
		# if self.mInputUINode:
		# 	self.mInputUINode.InitScreen()
		
		self.mUIMgr.Init(self)
		self.mSquadApplyUINode = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadApply)
		self.mSquadAlertUINode = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadAlert)
		self.mSquadReplyUINode = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadReply)
		self.mSquadClsBtnUINode = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadClsBtn)
		self.mSquadMainUINode = clientApi.GetUI(squadConst.ModName, uiDef.UIDef.UISquadMain)

	def OnSquadPlayerUpdate(self, data):
		print 'OnSquadPlayerUpdate', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.dispose(data)
		# if self.mSquadApplyUINode:
		# 	self.mSquadApplyUINode.dispose(data)
		self.OnDispose(data)

	def OnSquadPlayerRecruit(self, data):
		print 'OnSquadPlayerRecruit', data

	def OnSetupSquad(self, data):
		print 'OnSetupSquad', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.dispose(data)
		self.OnDispose(data)

	def OnDissolveSquad(self, data):
		print 'OnDissolveSquad', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.dispose(data)
		self.OnDispose(data)

	def OnSquadPlayerLeave(self, data):
		print 'OnSquadPlayerLeave', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.dispose(data)
		self.OnDispose(data)

	def OnSquadApplyList(self, data):
		print 'OnSquadApplyList', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.display_reply_board(data)
		if self.mSquadReplyUINode:
			self.mSquadReplyUINode.display_reply_board(data)

	def OnSquadRecruitList(self, data):
		print 'OnSquadRecruitList', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.display_apply_board(data)
		if self.mSquadApplyUINode:
			self.mSquadApplyUINode.display_apply_board(data)

	def OnSquadApplicantsClear(self, data):
		print 'OnSquadRecruitList', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.clear_reply_board()
		if self.mSquadReplyUINode:
			self.mSquadReplyUINode.clear_reply_board()

	def OnSquadInvitePlayer(self, data):
		print 'OnSquadInvitePlayer', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.invite(data)
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.invite(data)

	def OnAssemble(self, data):
		print 'OnAssemble', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.assemble(data)
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.assemble(data)

	def OnSquadAppendPlayer(self, data):
		print 'OnSquadAppendPlayer', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.update_reply_board(data)
		if self.mSquadReplyUINode:
			self.mSquadReplyUINode.update_reply_board(data)

	def OnSquadRecruitmentApply(self, data):
		print 'OnSquadRecruitmentApply', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.update_apply_board(data)
		if self.mSquadApplyUINode:
			self.mSquadApplyUINode.update_apply_board(data)

	def OnSquadApplicationNotice(self, data):
		print 'OnSquadApplicationNotice', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.notice(data)
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.notice(data)

	def OnSquadPlayerDisconnect(self, data):
		print 'OnSquadPlayerDisconnect', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.gray(data['entity'])
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.gray(data['entity'])
			
	def OnSquadPlayerReconnect(self, data):
		print 'OnSquadPlayerReconnect', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.recover(data['entity'])
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.recover(data['entity'])

	def OnJoinSquad(self, data):
		print 'OnJoinSquad', data
		# if self.mSquadUINode:
		# 	self.mSquadUINode.dispose(data)
		self.OnDispose(data)
			
	def OnDispose(self, data):
		if self.mSquadApplyUINode:
			self.mSquadApplyUINode.dispose(data)
		if self.mSquadReplyUINode:
			self.mSquadReplyUINode.dispose(data)
		if self.mSquadClsBtnUINode:
			self.mSquadClsBtnUINode.dispose(data)
		if self.mSquadMainUINode:
			self.mSquadMainUINode.dispose(data)
