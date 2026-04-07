# -*- coding: utf-8 -*-

import time
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import lobbyGame.netgameApi as lobbyGameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
from mod_log import engine_logger as logger

from neteaseRoundScript.roundConst import ModName, ClientSampleSystemName, SampleClientEvent, SampleServerEvent, ServerBattleSystemName
import neteaseRoundScript.roundConst as roundConst
from neteaseRoundScript.roundServerPlayer import ServerPlayer

class RoundSampleServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# 加载配置信息
		self.InitConfig()
		#
		self.mPlayerData = {}

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DamageEvent", self, self.OnDamageEvent)
		self.ListenForEvent(ModName, ClientSampleSystemName, SampleClientEvent.ClientEnter, self, self.OnClientReady)
		
	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DamageEvent", self, self.OnDamageEvent)
		self.UnListenForEvent(ModName, ClientSampleSystemName, SampleClientEvent.ClientEnter, self, self.OnClientReady)

	def InitConfig(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseRoundScript")
		if not cfg:
			return False
		exKey = "_comment"
		# 角色、技能、持续效果、演出的配置，每个identifier都对应独立的配置文件
		for keyword, configBase in roundConst.ConfigAllTypeMap.iteritems():
			configDict = cfg.get(keyword, {})
			roundConst.CleanDict(configDict, exKey)
			for identifier, jsonFile in configDict.iteritems():
				jsonConfig = commonNetgameApi.GetModJsonConfigByName("neteaseRoundScript", jsonFile)
				if not jsonConfig:
					logger.error("cannot load config file type={} identifier={} file={}".format(keyword, identifier, jsonFile))
					continue
				if jsonConfig["identifier"] != identifier:
					logger.error("config file {} identifier is not same".format(jsonFile))
					continue
				roundConst.CleanDict(jsonConfig, exKey)
				configBase[identifier] = roundConst.UnicodeConvert(jsonConfig)
		return True

	def Update(self):
		pass
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnServerChat(self, args):
		playerId = args["playerId"]
		messages = args['message'].split()
		command = messages[0]
		params = messages[1:]
		if command == "additem":
			identifier = params[0]
			auxValue = int(params[1])
			count = int(params[2])
			self.DoAddItem(playerId, identifier, auxValue, count)

	def DoAddItem(self, playerId, identifier, auxValue, count):
		slot = self.GetEmptySlot(playerId)
		if slot is None:
			return
		itemDict = {
			'itemName': identifier,
    		'count': count,
			'enchantData': [],
			'auxValue': auxValue,
			'customTips': '',
			'extraId': '',
			'userData': {},
		}
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		comp.SpawnItemToPlayerInv(itemDict, playerId, slot)
	
	def GetEmptySlot(self, playerId):
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for slot in xrange(36):
			item = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				return slot
		return None
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnAddServerPlayer(self, args):
		# print "OnAddServerPlayer", args
		playerId = args["id"]
		uid = args["uid"]
		self.mPlayerData[playerId] = ServerPlayer(playerId, uid)

	def OnDelServerPlayer(self, args):
		# print "OnDelServerPlayer", args
		playerId = args["id"]
		playerData = self.mPlayerData.get(playerId, None)
		if not playerData:
			return
		del self.mPlayerData[playerId]
		battleSystem = serverApi.GetSystem(ModName, ServerBattleSystemName)
		battleSystem.OnPlayerLeave(playerId)
	
	def OnDamageEvent(self, args):
		args["damage"] = 0
		args["knock"] = False
		args["ignite"] = False
		srcId = args["srcId"]
		srcPlayer = self.mPlayerData.get(srcId, None)
		targetId = args["entityId"]
		targetPlayer = self.mPlayerData.get(targetId, None)
		if srcPlayer and targetPlayer:
			self.DoStartPVP(srcPlayer, targetPlayer)
		elif srcPlayer:
			self.DoStartPVE(srcPlayer, targetId)
			self.DestroyEntity(targetId)
		elif targetPlayer:
			self.DoStartPVE(targetPlayer, srcId)
			self.DestroyEntity(srcId)
	#------------------------------------------------------------------------------------------------------------------------------------
	def DoStartPVP(self, srcPlayer, tarPlayer):
		print "DoStartPVP", srcPlayer, tarPlayer
		# 修正客户端登录和准备工作尚未完全前就触发战斗最终导致出现trace的问题
		if (not srcPlayer.mClientReady) or (not tarPlayer.mClientReady):
			print "DoStartPVP fail srcPlayer or tarPlayer client not ready"
			return
		battleSystem = serverApi.GetSystem(ModName, ServerBattleSystemName)
		battle = battleSystem.GetBattleByPlayerId(srcPlayer.mPlayerId)
		if battle:
			print "DoStartPVP fail srcPlayer is already in battle"
			return
		battle = battleSystem.GetBattleByPlayerId(tarPlayer.mPlayerId)
		if battle:
			print "DoStartPVP fail tarPlayer is already in battle"
			return
		battleSystem.CreatePVPBattle(srcPlayer, tarPlayer)
	
	def DoStartPVE(self, srcPlayer, entityId):
		print "DoStartPVE", srcPlayer, entityId
		if entityId in (-1, "-1"):
			return
		# 修正客户端登录和准备工作尚未完全前就触发战斗最终导致出现trace的问题
		if (not srcPlayer.mClientReady):
			print "DoStartPVE fail srcPlayer client is not ready"
			return
		battleSystem = serverApi.GetSystem(ModName, ServerBattleSystemName)
		battle = battleSystem.GetBattleByPlayerId(srcPlayer.mPlayerId)
		if battle:
			print "DoStartPVE fail srcPlayer is already in battle"
			return
		battleSystem.CreatePVEBattle(srcPlayer, entityId)
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnClientReady(self, data):
		print "OnClientReady", data
		playerId = data["playerId"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		player.SetClientReady()
		self.NotifyToClient(playerId, SampleServerEvent.ServerReady, {"uid": player.mUid})
		for keyword, configDict in roundConst.ConfigAllTypeMap.iteritems():
			for identifier, config in configDict.iteritems():
				eventData = {
					"keyword": keyword,
					"identifier": identifier,
					"config": config,
				}
				self.NotifyToClient(playerId, SampleServerEvent.SyncConfig, eventData)
	#------------------------------------------------------------------------------------------------------------------------------------
		




