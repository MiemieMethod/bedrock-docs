# -*- coding: utf-8 -*-
#
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
import guildConsts as guildConsts
from guildMgrGac import GuildMgrGac
from UIMgr import UIMgr

class GuildClientSystem(ClientSystem):
	"""
	该mod的大厅服客户端类
	"""
	def __init__(self,namespace, systemName):
		ClientSystem.__init__(self, namespace, systemName)
		print namespace, systemName, "====init===="
		self.mGuildMgrGac = GuildMgrGac()  # 管理类
		self.mUIMgr = UIMgr()
		
		# self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		#                     guildConsts.AddPlayerFromServerToClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnAddPlayer)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.DelPlayerFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnDelPlayer)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.SyncGuildAttrsFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnSyncGuildAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.SyncPlayerAttrsFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnSyncPlayerAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.ShowTipsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnShowTips)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.ShowCreateGuildUIFromServerEvent,
		                    self.mGuildMgrGac, self.mGuildMgrGac.OnShowCreateGuildUIFromServer)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.ShowUIFromClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnShowUI)
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
		                    guildConsts.UiInitFinishedEvent, self, self.OnUiInitFinished)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.LoginResponseEvent, self,
		                    self.OnLoginResponse)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.UnShowUIFromServerEvent,
		                    self, self.OnUnShowUIFromServer)
		
	def OnUnShowUIFromServer(self, args):
		self.mUIMgr.UnShowAllUI()
		
	def OnUiInitFinished(self, args):
		print "OnUiInitFinished", args
		self.mUIMgr.InitAllUI()
		#向server拉取玩家的数据
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
		# self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		#                     guildConsts.AddPlayerFromServerToClientEvent, self.mGuildMgrGac,
		#                     self.mGuildMgrGac.OnAddPlayer)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.DelPlayerFromServerEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnDelPlayer)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.SyncGuildAttrsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnSyncGuildAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                    guildConsts.SyncPlayerAttrsFromServerEvent, self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnSyncPlayerAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.ShowTipsFromServerEvent,
		                    self.mGuildMgrGac,
		                    self.mGuildMgrGac.OnShowTips)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.ShowUIFromClientEvent, self.mGuildMgrGac, self.mGuildMgrGac.OnShowUI)
		self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(),
		                     guildConsts.UiInitFinishedEvent, self.mUIMgr, self.mUIMgr.InitAllUI)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.LoginResponseEvent,self,
		                    self.OnLoginResponse)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServerSystemName, guildConsts.UnShowUIFromServerEvent,
		                    self, self.OnUnShowUIFromServer)
		
		
		