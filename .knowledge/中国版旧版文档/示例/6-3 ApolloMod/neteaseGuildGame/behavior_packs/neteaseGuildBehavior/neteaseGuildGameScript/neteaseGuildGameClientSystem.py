# -*- coding: utf-8 -*-
#
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import guildConsts as guildConsts
from guildMgrGac import GuildMgrGac
from UIMgr import UIMgr

class GuildGameClientSystem(ClientSystem):
	"""
	该mod游戏服的客户端类
	"""
	def __init__(self,namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print namespace, systemName, "====init===="
		self.mGuildMgrGac = GuildMgrGac()  # 管理类
		self.mUIMgr = UIMgr()
		
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.AddPlayerFromServerToClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnAddPlayer)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.DelPlayerFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnDelPlayer)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.SyncGuildAttrsFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnSyncGuildAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.SyncPlayerAttrsFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnSyncPlayerAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName, guildConsts.ShowTipsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnShowTips)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.ShowUIFromClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnShowUI)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
		                    guildConsts.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName, guildConsts.LoginResponseEvent,
		                    self, self.OnLoginResponse)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName, guildConsts.UnShowUIFromServerEvent,
		                    self, self.OnUnShowUIFromServer)
		
	def OnUnShowUIFromServer(self, args):
		self.mUIMgr.UnShowAllUI()
	
	def OnUiInitFinished(self, args):
		self.mUIMgr.InitAllUI()
		# 向server拉取玩家的数据
		playerId = clientApi.GetLocalPlayerId()
		loginData = {}
		loginData['playerId'] = playerId
		self.NotifyToServer(guildConsts.LoginRequestEvent, loginData)
	
	def OnLoginResponse(self, args):
		self.mGuildMgrGac.OnAddPlayer(args)
		
	def GetUIMgr(self):
		return self.mUIMgr
	
	def GetGuildMgrGac(self):
		return self.mGuildMgrGac
	
	def Destroy(self):
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName, guildConsts.LoginResponseEvent,
		                    self, self.OnLoginResponse)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.AddPlayerFromServerToClientEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnAddPlayer)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.DelPlayerFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnDelPlayer)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.SyncGuildAttrsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnSyncGuildAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.SyncPlayerAttrsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnSyncPlayerAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName,
		                    guildConsts.ShowTipsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnShowTips)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.ShowUIFromClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnShowUI)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
		                    guildConsts.UiInitFinishedEvent, self.mUIMgr, self.mUIMgr.InitAllUI)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameServerSystemName, guildConsts.UnShowUIFromServerEvent,
		                    self, self.OnUnShowUIFromServer)
		
		
		
		