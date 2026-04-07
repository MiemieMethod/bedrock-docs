# -*- coding: utf-8 -*-
import client.extraClientApi as extraClientApi
ClientSystem = extraClientApi.GetClientSystemCls()
import neteaseMapAttrsScript.util as util
from neteaseMapAttrsScript.mapAttrsConsts import ServerEvent, ClientEvent
from neteaseMapAttrsScript.textBoardMgr import TextBoardMgr

class MapAttrsClientSys(ClientSystem):
	def __init__(self, namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		util.SetSystem(self)
		util.ListenClientEngineEvent("UiInitFinished", self, self.OnUiInitFinished)
		util.ListenClientEngineEvent("DimensionChangeClientEvent", self, self.OnDimChange)
		util.ListenServerEvent(ServerEvent.LoginResponse, self, self.OnLoginResponse)
		self.mPlayerId = extraClientApi.GetLocalPlayerId()
		self.mPlayerDim = None
		self.mTextMgr = TextBoardMgr(self.mPlayerId, offset=50.0)

	def Destroy(self):
		if self.mTextMgr:
			self.mTextMgr.Destroy()
			self.mTextMgr = None
		util.Destroy()
	# -----------------------------------------------------------------------------------
	def OnUiInitFinished(self, data):
		print 'OnUiInitFinished', data
		requestData = {
			"playerId": self.mPlayerId,
		}
		util.NotifyToServer(ClientEvent.PlayerEnter, requestData)


	def OnDimChange(self, data):
		self.mPlayerDim = data["toDimensionId"]
		self.mTextMgr.OnDimChange(data)

	def OnLoginResponse(self, data):
		print 'OnLoginResponse', data
		self.mPlayerDim = data["dim"]
		self.mTextMgr.Init(data["configData"])
	# -----------------------------------------------------------------------------------
	def GetLocalPlayerDim(self):
		return self.mPlayerDim
