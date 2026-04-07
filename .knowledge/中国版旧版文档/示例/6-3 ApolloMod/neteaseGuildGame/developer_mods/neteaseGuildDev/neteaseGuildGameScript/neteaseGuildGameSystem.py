# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import guildConsts as guildConsts
from guildConsts import PlayerAttrType, GuildAttrType
import lobbyGame.netgameApi as netgameApi
import logout
from coroutineMgrGas import CoroutineMgr
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
from guildMgrGas import GuildMgrGas
import json

class GuildGameSystem(ServerSystem):
	"""
	该mod的游戏服服务端类
	"""

	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		
		self.mCoroutineMgr = CoroutineMgr()
		self.mGuildMgrGas = GuildMgrGas()  # 管理类
		
		self.mUidToPlayerId = {} #记录在线玩家的uid:playerId
		self.mPlayerTempArgs = {}  # 记录临时数据，因为addserverevent发给客户端可能收不到，所以只能先存着等客户端准备好再取
		self.Init()
		
		self.mGuildMembersDict = {}
		self.mPlayerAtGuildDict = {}
		
	def Init(self):
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseGuildGameScript')
		self.mGuildConsumeDiamond = modConfig.get('GuildConsumeDiamond', 1)
		
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncGuildAttrsFromServiceEvent,
		                    self, self.OnSyncGuildAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncPlayerAttrsFromServiceEvent,
		                    self, self.OnSyncPlayerAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.ShowTipsFromServiceEvent,
		                    self, self.OnShowTips)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.AgreePlayerFromClientEvent,
		                    self, self.OnAgreePlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.AppointPlayerFromClientEvent,
		                    self, self.OnAppointPlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.KickPlayerFromClientEvent,
		                    self, self.OnKickPlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.ExitGuildFromClientEvent,
		                    self, self.ExitGuildFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName, guildConsts.ReturnLobbyFromClientEvent,
		                    self, self.OnReturnLobbyFromClient)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "ServerChatEvent", self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerRespawnEvent", self, self.OnPlayerRespawn)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerDieEvent", self, self.OnPlayerDie)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName, guildConsts.LoginRequestEvent, self,
		                    self.OnLoginRequest)
		
	def Update(self):
		self.mCoroutineMgr.Tick()
	
	def Destroy(self):
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncGuildAttrsFromServiceEvent,
		                    self, self.OnSyncGuildAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncPlayerAttrsFromServiceEvent,
		                    self, self.OnSyncPlayerAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.ShowTipsFromServiceEvent,
		                    self, self.OnShowTips)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.AgreePlayerFromClientEvent,
		                    self, self.OnAgreePlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.AppointPlayerFromClientEvent,
		                    self, self.OnAppointPlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.KickPlayerFromClientEvent,
		                    self, self.OnKickPlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.ExitGuildFromClientEvent,
		                    self, self.ExitGuildFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName,
		                    guildConsts.ReturnLobbyFromClientEvent,
		                    self, self.OnReturnLobbyFromClient)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerRespawnEvent", self, self.OnPlayerRespawn)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "ServerChatEvent", self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerDieEvent", self, self.OnPlayerDie)
		
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.GameClientSystemName, guildConsts.LoginRequestEvent,
		                    self, self.OnLoginRequest)
	
	# 监听ServerChatEvent的回调函数
	def OnServerChat(self, args):
		"""
		重载基础聊天逻辑，仅广播给同公会的玩家
		"""
		playerId = args.get("playerId")
		#args['cancel'] = True
		#获取game领地内同公会玩家
		playerUidGuildList = self.mGuildMgrGas.GetSameGuildPlayers(playerId)
		playerIdGuildList = [self.mUidToPlayerId[uid] for uid in playerUidGuildList]
		# #广播给自己的玩家
		# msgComp = self.CreateComponent(playerId, "Minecraft", "msg")
		# for playerUid in playerGuildList:
		# 	sendPlayerId = self.mUidToPlayerId.get(playerUid, None)
		# 	if sendPlayerId == None:
		# 		continue
		# 	msgComp.SendMsgToPlayer(playerId, sendPlayerId, args['message'])
		args["bChatById"] = True
		args["toPlayerIds"] = playerIdGuildList
		
	def OnShowTips(self, args):
		"""
		中转来自service的弹出提示的事件给客户端
		"""
		playerUid = args.get('uid')
		playerId = self.mUidToPlayerId.get(playerUid)
		logout.info("OnShowTips", args)
		self.NotifyToClient(playerId, guildConsts.ShowTipsFromServerEvent, args)
		if args['code'] in (guildConsts.CodeKick, guildConsts.CodeGuildDisMiss):
			#data = {}
			#data['bornPos'] = [1400, 68, 50]
			self.mCoroutineMgr.StartCoroutine(self.DelayeTransfer(playerId, 3))
			
	def DelayeTransfer(self, playerId, delayFrame = 0):
		"""
		延时一定时间后，把玩家踢回lobby
		"""
		yield -1 * delayFrame
		#netgameApi.TransferToOtherServer(playerId, "lobby", json.dumps(args))
		self.ReturnLobby(playerId)
	
		
	def OnAgreePlayerFromClient(self, args):
		"""
		中转来自client的同意玩家的加入公会的事件给service
		"""
		logout.info("OnAgreePlayerFromClient", args)
		playerId = args.get('operatorPlayerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['operatorUid'] = playerUid
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.AgreePlayerFromServerEvent, args)
		
	def OnAppointPlayerFromClient(self, args):
		"""
		中转来自client的调整玩家公会职务的事件给service
		"""
		logout.info("OnAppointPlayerFromClient", args)
		playerId = args.get('operatorPlayerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['operatorUid'] = playerUid
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.AppointPlayerFromServerEvent, args)
		
	def OnKickPlayerFromClient(self, args):
		"""
		中转来自client的把玩家踢出公会的事件给service
		"""
		logout.info("OnKickPlayerFromClient", args)
		playerId = args.get('operatorPlayerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['operatorUid'] = playerUid
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.KickPlayerFromServerEvent, args)
		
	def ExitGuildFromClient(self, args):
		"""
		中转来自client的主动退出公会的事件给service
		"""
		logout.info("ExitGuildFromClient", args)
		playerId = args.get('playerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['uid'] = playerUid
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.ExitGuildFromServerEvent, args)
		
	def OnReturnLobbyFromClient(self, args):
		"""
		返回公会驻地（lobby）
		"""
		playerId = args.get('playerId')
		self.ReturnLobby(playerId)
		
	def ReturnLobby(self, playerId):
		data = {}
		#data['bornPos'] = guildConsts.DEFAULT_LOBBY_BORN_POS
		netgameApi.TransferToOtherServer(playerId, "lobby", json.dumps(data))
	
	def OnAddServerPlayer(self, args):
		'''
		玩家登陆的监听函数
		'''
		logout.info("OnAddServerPlayer", args)
		playerId = args.get('id', '-1')
		playerUid = netgameApi.GetPlayerUid(playerId)
		self.mUidToPlayerId[playerUid] = playerId
		#名字
		nickName = netgameApi.GetPlayerNickname(playerId)
		#等级
		levelComp = self.CreateComponent(playerId, "Minecraft", "lv")
		playerLevel = levelComp.GetPlayerLevel()
		args['uid'] = playerUid
		args['nickName'] = nickName
		args['playerLevel'] = playerLevel
		transferParamStr = args.get('transferParam', None)
		if transferParamStr:
			transferParam = json.loads(transferParamStr)
			bornPos = transferParam.get('bornPos', None)
			if bornPos:
				posComp = self.CreateComponent(playerId, "Minecraft", "pos")
				posComp.SetPos(tuple(bornPos))
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.AddPlayerFromServerEvent, args)
		print 'AddPlayerFromServerToClientEvent', playerId
		self.mGuildMgrGas.OnAddPlayer(args)
		self.mPlayerTempArgs[playerUid] = args
		
		# self.mCoroutineMgr.StartCoroutine(self.DelayNotifyToClient(playerId, guildConsts.AddPlayerFromServerToClientEvent, args, 1))
	def OnPlayerRespawn(self, args):
		"""
		复活后强制移动到公会驻地
		"""
		playerId = args.get("id")
		playerUid = netgameApi.GetPlayerUid(playerId)
		playerArgs = self.mPlayerTempArgs.get(playerUid)
		transferParamStr = playerArgs.get('transferParam', None)
		if transferParamStr:
			transferParam = json.loads(transferParamStr)
			bornPos = transferParam.get('bornPos', None)
			if bornPos:
				posComp = self.CreateComponent(playerId, "Minecraft", "pos")
				posComp.SetPos(tuple(bornPos))
		
	def OnPlayerDie(self, args):
		"""
		死亡时强制关闭全部公会界面
		"""
		playerId = args.get('id')
		# 取消公会UI显示
		self.NotifyToClient(playerId, guildConsts.UnShowUIFromServerEvent, args)
	
	def OnLoginRequest(self, args):
		"""
		客户端通知服务端，初始化完成
		"""
		playerId = args.get("playerId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		playerArgs = self.mPlayerTempArgs.get(playerUid)
		self.NotifyToClient(playerId, guildConsts.LoginResponseEvent, playerArgs)
		
	def OnDelServerPlayer(self, args):
		'''
		玩家离线的监听函数
		'''
		playerId = args.get('id', '-1')
		playerUid = netgameApi.GetPlayerUid(playerId)
		if self.mUidToPlayerId.has_key(playerUid):
			self.mUidToPlayerId.pop(playerUid)
			# 名字
			nickName = netgameApi.GetPlayerNickname(playerId)
			# 等级
			levelComp = self.CreateComponent(playerId, "Minecraft", "lv")
			playerLevel = levelComp.GetPlayerLevel()
			args['uid'] = playerUid
			args['nickName'] = nickName
			args['playerLevel'] = playerLevel
			self.RequestToService(guildConsts.ModNameSpace, guildConsts.DelPlayerFromServerEvent, args)
			self.mGuildMgrGas.OnDelPlayer(args)
			self.NotifyToClient(playerId, guildConsts.DelPlayerFromServerEvent, args)
	
	def OnSyncGuildAttrs(self, args):
		"""
		来自service的更新公会信息的事件，需要更新本地缓存并同步给client
		"""
		playerUid = args.get('uid', None)
		playerId = self.mUidToPlayerId.get(playerUid)
		if playerId:
			self.NotifyToClient(playerId, guildConsts.SyncGuildAttrsFromServerEvent, args)
		
		guildId = args.get(GuildAttrType.GuildId, None)
		if guildId != -1:
			if self.mGuildMembersDict.has_key(guildId) == False:
				self.mGuildMembersDict[guildId] = {}
			PresidentPlayerDict = args.get(GuildAttrType.PresidentPlayerDict)
			if PresidentPlayerDict:
				self.mGuildMembersDict[guildId][GuildAttrType.PresidentPlayerDict] = PresidentPlayerDict
			ElderPlayerDict = args.get(GuildAttrType.ElderPlayerDict)
			if ElderPlayerDict:
				self.mGuildMembersDict[guildId][GuildAttrType.ElderPlayerDict] = ElderPlayerDict
			CommonPlayerDict = args.get(GuildAttrType.CommonPlayerDict)
			if CommonPlayerDict:
				self.mGuildMembersDict[guildId][GuildAttrType.CommonPlayerDict] = CommonPlayerDict
			
			PresidentPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.PresidentPlayerDict,
			                                                                  {}).keys()
			ElderPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.ElderPlayerDict, {}).keys()
			CommonPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.CommonPlayerDict, {}).keys()
			if PresidentPlayerDict or ElderPlayerDict or CommonPlayerDict:
				self.BroadcastEvent("PlayerGuildMembersChangeEvent", {"uid": playerUid,
				                                                             "guildMembers": PresidentPlayerList + ElderPlayerList + CommonPlayerList})
	
	def OnSyncPlayerAttrs(self, attrsToSync):
		"""
		来自service的更新公会成员信息的事件，需要更新本地缓存并同步给client
		"""
		playerUid = attrsToSync.get(PlayerAttrType.Uid, None)
		guildId = attrsToSync.get(PlayerAttrType.GuildId)
		if playerUid:
			playerId = self.mUidToPlayerId.get(playerUid)
			attrsToSync['playerId'] = playerId
			self.NotifyToClient(playerId, guildConsts.SyncPlayerAttrsFromServerEvent, attrsToSync)
			
			if guildId is not None:
				self.mPlayerAtGuildDict[playerUid] = guildId
				PresidentPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.PresidentPlayerDict,
				                                                                  {}).keys()
				ElderPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.ElderPlayerDict, {}).keys()
				CommonPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.CommonPlayerDict,
				                                                               {}).keys()
				self.BroadcastEvent("PlayerGuildMembersChangeEvent", {"uid": playerUid,
				                                                             "guildMembers": PresidentPlayerList + ElderPlayerList + CommonPlayerList})
		
	