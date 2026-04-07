# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import guildConsts as guildConsts
from guildConsts import PlayerAttrType, GuildAttrType
import lobbyGame.netgameApi as netgameApi
import logout
from coroutineMgrGas import CoroutineMgr
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import json

class GuildServerSystem(ServerSystem):
	"""
	该mod的大厅服服务端类
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		logout.info(namespace, systemName, "====init====")
		
		self.mCoroutineMgr = CoroutineMgr()
		
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName, guildConsts.SyncGuildAttrsFromServiceEvent,
		                    self, self.OnSyncGuildAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName, guildConsts.SyncPlayerAttrsFromServiceEvent,
		                    self, self.OnSyncPlayerAttrs)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName, guildConsts.GetGuildBriefFromServiceEvent,
		                    self, self.OnShowGuildBrief)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName, guildConsts.ShowTipsFromServiceEvent,
		                    self, self.OnShowTips)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                      guildConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.CreateGuildFromClientEvent,
		                    self, self.OnCreateGuild)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.JoinGuildFromClientEvent,
		                    self, self.OnJoinGuild)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.GetGuildBriefFromClientEvent,
		                    self, self.OnGetGuildBrief)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.AgreePlayerFromClientEvent,
		                    self, self.OnAgreePlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.AppointPlayerFromClientEvent,
		                    self, self.OnAppointPlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.KickPlayerFromClientEvent,
		                    self, self.OnKickPlayerFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.ExitGuildFromClientEvent,
		                    self, self.OnExitGuildFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.ReturnGuildMapFromClientEvent,
		                    self, self.OnReturnGuildMapFromClient)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.LoginRequestEvent, self,
		                    self.OnLoginRequest)
		self.ListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.ShowCreateGuildUIFromClientEvent, self,
		                    self.OnShowCreateGuildUIFromClient)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                      "ServerChatEvent", self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerRespawnEvent", self, self.OnPlayerRespawn)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerDieEvent", self, self.OnPlayerDie)
		
		self.mUidToPlayerId = {} #记录在线玩家的uid:playerId
		self.mPlayerTempArgs = {} #记录临时数据，因为addserverevent发给客户端可能收不到，所以只能先存着等客户端准备好再取
		self.Init()
		
		self.mGuildMembersDict = {}
		self.mPlayerAtGuildDict = {}
		
	def Init(self):
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseGuildScript')
		self.mGuildConsumeDiamond = modConfig.get('GuildConsumeDiamond', 1)
		
	def Destroy(self):
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncGuildAttrsFromServiceEvent,
		                    self, self.OnSyncGuildAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.SyncPlayerAttrsFromServiceEvent,
		                    self, self.OnSyncPlayerAttrs)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.GetGuildBriefFromServiceEvent,
		                    self, self.OnShowGuildBrief)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ServiceSystemName,
		                    guildConsts.ShowTipsFromServiceEvent,
		                    self, self.OnShowTips)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.AddServerPlayerEvent, self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    guildConsts.DelServerPlayerEvent, self, self.OnDelServerPlayer)
		
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.CreateGuildFromClientEvent,
		                    self, self.OnCreateGuild)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.JoinGuildFromClientEvent,
		                    self, self.OnJoinGuild)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.GetGuildBriefFromClientEvent,
		                    self, self.OnGetGuildBrief)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.AgreePlayerFromClientEvent,
		                    self, self.OnAgreePlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.AppointPlayerFromClientEvent,
		                    self, self.OnAppointPlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.KickPlayerFromClientEvent,
		                    self, self.OnKickPlayerFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.ExitGuildFromClientEvent,
		                    self, self.OnExitGuildFromClient)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName,
		                    guildConsts.ReturnGuildMapFromClientEvent,
		                    self, self.OnReturnGuildMapFromClient)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "ServerChatEvent", self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerRespawnEvent", self, self.OnPlayerRespawn)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
		                    "PlayerDieEvent", self, self.OnPlayerDie)
		self.UnListenForEvent(guildConsts.ModNameSpace, guildConsts.ClientSystemName, guildConsts.LoginRequestEvent, self,
		                    self.OnLoginRequest)
		
	def Update(self):
		self.mCoroutineMgr.Tick()
		
	# 监听ServerChatEvent的回调函数
	def OnServerChat(self, args):
		"""
		重载聊天逻辑，增加了获得钻石的巫师指令
		"""
		playerId = args.get("playerId")
		print "=====chat=====", playerId
		if args["message"] == "ad":
			itemDict = {
				'itemName': 'minecraft:diamond',
				'count': 64,
				'auxValue': 0,
			}
			comp = serverApi.CreateComponent(playerId, 'Minecraft', 'item')
			comp.SpawnItemToPlayerInv(itemDict, playerId, 0)
			comp.SpawnItemToPlayerInv(itemDict, playerId, 1)
	
	def OnShowCreateGuildUIFromClient(self, args):
		"""
		处理来自client的显示创建公会界面的请求，返回是否有足够的钻石来创建新公会
		"""
		playerId = args.get("playerId")
		enoughDiamond = True
		if guildConsts.GetPlayerDimondNum(playerId) < self.mGuildConsumeDiamond:
			enoughDiamond = False
		createGuildUIArgs = {"enoughDiamond" : enoughDiamond}
		self.NotifyToClient(playerId, guildConsts.ShowCreateGuildUIFromServerEvent, createGuildUIArgs)
	
	def OnShowGuildBrief(self, args):
		"""
		中转来自service的公会快照信息事件给client
		"""
		logout.info("OnShowGuildBrief", args)
		playerUid = args.get('uid')
		playerId = self.mUidToPlayerId.get(playerUid)
		guildBrief = args.get('guildBrief')
		self.NotifyToClient(playerId, guildConsts.GetGuildBriefFromServerEvent, guildBrief)
		
	def OnShowTips(self, args):
		"""
		中转来自service的显示提示信息的事件给client
		"""
		playerUid = args.get('uid')
		playerId = self.mUidToPlayerId.get(playerUid)
		logout.info("OnShowTips", args)
		self.NotifyToClient(playerId, guildConsts.ShowTipsFromServerEvent, args)
	
	def OnGetGuildBrief(self, args):
		"""
		中转来自client的获取可加入的公会快照的事件给service
		"""
		logout.info("OnGetGuildBrief", args)
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.GetGuildBriefFromServerEvent, args)
		
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
		
	def OnExitGuildFromClient(self, args):
		"""
		中转来自client的主动退出公会的事件给service
		"""
		logout.info("ExitGuildFromClient", args)
		playerId = args.get('playerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['uid'] = playerUid
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.ExitGuildFromServerEvent, args)
		
	def OnReturnGuildMapFromClient(self, args):
		"""
		中转来自client的返回公会驻地的事件给service
		"""
		logout.info("OnReturnGuildMapFromClient", args)
		playerId = args.get('playerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['uid'] = playerUid
		def ReturnMapCb(suc, args):
			if not suc:
				logout.info("OnReturnGuildMapFromClient", "创建请求超时")
				response = {'code': guildConsts.CodeOutOfTime,
				            'message': guildConsts.ResponseText[guildConsts.CodeOutOfTime]
				            }
				self.NotifyToClient(playerId, guildConsts.ShowTipsFromServerEvent, response)
				return
			serverType = args.get('serverType')
			data = {}
			data["bornPos"] = args.get("bornPos")
			netgameApi.TransferToOtherServer(playerId, serverType, json.dumps(data))
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.ReturnGuildMapFromServerEvent, args, ReturnMapCb, 3)
	
	def OnJoinGuild(self, args):
		"""
		中转来自client的加入公会请求的事件给service
		"""
		playerId = args.get('playerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['uid'] = playerUid
		logout.info("OnJoinGuild", args)
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.JoinGuildFromServerEvent, args)
	
	def OnCreateGuild(self, args):
		"""
		中转来自client的创建新公会的事件给service
		"""
		playerId = args.get('playerId')
		playerUid = netgameApi.GetPlayerUid(playerId)
		args['uid'] = playerUid
		logout.info("OnCreateGuild", args)
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.CreateGuildFromServerEvent, args, lambda suc, args:self.CreateGuildCb(playerId, suc, args))
		
	def CreateGuildCb(self, playerId, suc, args):
		if not suc:
			logout.info("CreateGuildCb", "创建请求超时")
			response = {'code': guildConsts.CodeOutOfTime,
			            'message': guildConsts.ResponseText[guildConsts.CodeOutOfTime]
			            }
			self.NotifyToClient(playerId, guildConsts.ShowTipsFromServerEvent, response)
			return
		elif args.get('suc') == False:
			logout.info("CreateGuildCb", "创建失败")
			# TODO 提示创建失败
		else:
			print "CreateGuildCb", guildConsts.GetServerModSystem()
			if guildConsts.GetPlayerDimondNum(playerId) < self.mGuildConsumeDiamond:
				response = {'code': guildConsts.CodeDiamondNotEnough,
				            'message': guildConsts.ResponseText[guildConsts.CodeDiamondNotEnough]
				            }
				self.NotifyToClient(playerId, guildConsts.ShowTipsFromServerEvent, response)
				return
			else:
				#TODO 扣除钻石
				guildConsts.ConsumeDiamond(playerId, self.mGuildConsumeDiamond)
				self.RequestToService(guildConsts.ModNameSpace, guildConsts.CreateGuildSuccessFromServerEvent, args)
	
	def OnAddServerPlayer(self, args):
		'''
		玩家登陆的监听函数
		'''
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
		args['guildConsumeDiamond'] = self.mGuildConsumeDiamond
		transferParamStr = args.get('transferParam', None)
		if transferParamStr:
			transferParam = json.loads(transferParamStr)
			bornPos = transferParam.get('bornPos', None)
			if bornPos:
				posComp = self.CreateComponent(playerId, "Minecraft", "pos")
				posComp.SetPos(tuple(bornPos))
		# else:
		# 	posComp = self.CreateComponent(playerId, "Minecraft", "pos")
		# 	posComp.SetPos(tuple(guildConsts.DEFAULT_LOBBY_BORN_POS))
		self.RequestToService(guildConsts.ModNameSpace, guildConsts.AddPlayerFromServerEvent, args)
		print 'AddPlayerFromServerToClientEvent', playerId
		#先存到内存上
		self.mPlayerTempArgs[playerUid] = args
		#self.mCoroutineMgr.StartCoroutine(self.DelayNotifyToClient(playerId, guildConsts.AddPlayerFromServerToClientEvent, args, 1))
		
	def OnLoginRequest(self, args):
		"""
		客户端通知服务端，初始化完成
		"""
		print "OnLoginRequest", args
		playerId = args.get("playerId")
		playerUid = netgameApi.GetPlayerUid(playerId)
		playerArgs = self.mPlayerTempArgs.get(playerUid)
		self.NotifyToClient(playerId, guildConsts.LoginResponseEvent, playerArgs)
	
	def OnPlayerDie(self, args):
		"""
		死亡时强制关闭全部公会界面
		"""
		playerId = args.get('id')
		# 取消公会UI显示
		self.NotifyToClient(playerId, guildConsts.UnShowUIFromServerEvent, args)
		
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
		# else:
		# 	posComp = self.CreateComponent(playerId, "Minecraft", "pos")
		# 	posComp.SetPos(tuple(guildConsts.DEFAULT_LOBBY_BORN_POS))
		
	# def DelayNotifyToClient(self, playerId, event, args, delayFrame = 0):
	# 	yield -1 * delayFrame
	# 	self.NotifyToClient(playerId, event, args)
		
	def OnDelServerPlayer(self, args):
		'''
		玩家离线的监听函数
		'''
		playerId = args.get('id', '-1')
		playerUid = args.get('uid', 0)
		if self.mUidToPlayerId.has_key(playerUid):
			self.mUidToPlayerId.pop(playerUid)
			args['uid'] = playerUid
			self.RequestToService(guildConsts.ModNameSpace, guildConsts.DelPlayerFromServerEvent, args)
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
			
			PresidentPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.PresidentPlayerDict,{}).keys()
			ElderPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.ElderPlayerDict, {}).keys()
			CommonPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.CommonPlayerDict, {}).keys()
			if PresidentPlayerDict or ElderPlayerDict or CommonPlayerDict:
				self.BroadcastEvent("PlayerGuildMembersChangeEvent", {"uid":playerUid, "guildMembers":PresidentPlayerList + ElderPlayerList + CommonPlayerList})
	
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
				PresidentPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.PresidentPlayerDict, {}).keys()
				ElderPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.ElderPlayerDict, {}).keys()
				CommonPlayerList = self.mGuildMembersDict.get(guildId, {}).get(GuildAttrType.CommonPlayerDict, {}).keys()
				self.BroadcastEvent("PlayerGuildMembersChangeEvent", {"uid":playerUid, "guildMembers":PresidentPlayerList + ElderPlayerList + CommonPlayerList})
		
	