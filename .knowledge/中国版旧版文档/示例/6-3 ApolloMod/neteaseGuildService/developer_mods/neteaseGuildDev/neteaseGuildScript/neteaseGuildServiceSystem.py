# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
import service.serviceConf as serviceConf
ServiceSystem = serviceApi.GetServiceSystemCls()
from guildMgrGas import GuildMgrGas
from guildConsts import GuildAttrType
from guildConsts import PlayerAttrType
import guildConsts as guildConsts
from mysqlOperation import MysqlOperation
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import logout
from coroutineMgrGas import CoroutineMgr

class GuildServiceSystem(ServiceSystem):
	"""
	该mod的service类
	"""
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		self.mGuildMgrGas = GuildMgrGas()#管理类
		self.mMysqlMgr = MysqlOperation()#数据库
		self.mCoroutineMgr = CoroutineMgr()
		self.Init()
	
	def Init(self):
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.AddPlayerFromServerEvent,
		                       self.mGuildMgrGas.OnAddPlayerFromServer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.DelPlayerFromServerEvent,
		                       self.mGuildMgrGas.OnDelPlayerFromServer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.CreateGuildFromServerEvent,
		                       self.mGuildMgrGas.OnCreateGuildFromServer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.CreateGuildSuccessFromServerEvent,
		                       self.mGuildMgrGas.OnCreateGuildSuccessFromServer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.GetGuildBriefFromServerEvent,
		                       self.mGuildMgrGas.GetBriefGuildMes)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.JoinGuildFromServerEvent,
		                       self.mGuildMgrGas.OnApplication)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.AgreePlayerFromServerEvent,
		                       self.mGuildMgrGas.OnAgreePlayer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.AppointPlayerFromServerEvent,
		                       self.mGuildMgrGas.OnAppointPlayer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.KickPlayerFromServerEvent,
		                       self.mGuildMgrGas.OnKickPlayer)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.ExitGuildFromServerEvent,
		                       self.mGuildMgrGas.OnPlayerLeaveGuild)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.ReturnGuildMapFromServerEvent,
		                       self.mGuildMgrGas.OnReturnGuildMap)
		self.RegisterRpcMethod(guildConsts.ModNameSpace, guildConsts.DisMissGuildFromMasterEvent,
		                       self.mGuildMgrGas.OnDismissGuild)
		# self.ListenForEvent(serviceApi.GetEngineNamespace(), serviceApi.GetEngineSystemName(), guildConsts.LoadServerAddonScriptsAfter,
		#                        self.mGuildMgrGas, self.mGuildMgrGas.OnLoadServerAddonScriptsAfter)
		self.mMysqlMgr.InitMysqlDb()
		
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseGuildScript')
		self.mGuildMgrGas.SetParam(modConfig)
		
		self.mCoroutineMgr.DelayNoParamFunc(1, self.DelayInit)
	
	def DelayInit(self):
		logout.info("DelayInit")
		self.mGuildMgrGas.OnLoadServerAddonScriptsAfter()
		
	def GetMysqlMgr(self):
		return self.mMysqlMgr
	
	def Update(self):
		self.mGuildMgrGas.Tick()
		self.mCoroutineMgr.Tick()
		
	def Destroy(self):
		self.mGuildMgrGas.Destroy()
		self.mMysqlMgr.Destroy()
		
	def GetGuildUidsByGuilId(self, guildId):
		guildOne = self.mGuildMgrGas.mGuildDict.get(guildId, None)
		if guildOne is None:
			return {"code":guildConsts.CodeGuildNone, "message":"公会不存在！", "players":[]}
		return {"code":guildConsts.CodeSuc, "message":"成功！", "players":guildOne.GetAttr(GuildAttrType.PresidentPlayerDict).keys() + guildOne.GetAttr(GuildAttrType.ElderPlayerDict).keys() + guildOne.GetAttr(GuildAttrType.CommonPlayerDict).keys()}
	
	def GetPlayerAtGuild(self, playerUid):
		if self.mGuildMgrGas.mPlayerDict.has_key(playerUid) == False:
			return {"code":guildConsts.CodePlayerNone, "message":"玩家不存在！", "guildId":-1}
		playerAtGuild = self.mGuildMgrGas.mPlayerDict[playerUid].GetAttr(PlayerAttrType.GuildId)
		if playerAtGuild == -1:
			return {"code":guildConsts.CodePlayerNotInGuild, "message":"玩家不在任何公会！", "guildId":playerAtGuild}
		return {"code":guildConsts.CodeSuc, "message":"成功！", "guildId":playerAtGuild}