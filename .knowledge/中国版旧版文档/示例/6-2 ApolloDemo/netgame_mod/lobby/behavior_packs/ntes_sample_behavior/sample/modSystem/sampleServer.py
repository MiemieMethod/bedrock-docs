# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import netgame_api
import serverlevel

from extradata.playerExtraData import PlayerData as PlayerData
import npcManager
import sample_config

class SampleServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.playerDic = {}
		self.frame_count = 0
		#
		if sample_config.IS_LOBBY_STYLE:
			netgame_api.set_city_mode(True)
			x, y, z = sample_config.BORN_POS
			serverlevel.set_auto_respawn(True, 30, 0, x, y, z)
			serverlevel.set_enable_limit_area(True, int(x), int(y), int(z), sample_config.LIMIT_AREA[0], sample_config.LIMIT_AREA[1])
			# 准备要初始化的npc
			self.npcMgr = npcManager.Manager(self)
			for keyname, extra_data in sample_config.PROP_NPCS.iteritems():
				self.npcMgr.register_npc(keyname, extra_data)
		else:
			self.npcMgr = None
		#
		print '--------Server Listen ---------->>>>>>>'
		self.DefineEvent('updatePlayerExtraData')
		self.ListenForEvent('Minecraft', 'SampleClient', 'PlayerJoin', self, self.OnPlayerJoin)	
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DelServerPlayerEvent', self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MobDieEvent', self, self.OnMobDie)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityLoadScriptEvent', self, self.OnPlayerExtraData)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerPlayerBornPosEvent', self, self.OnPlayerBornPosEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DamageEvent', self, self.OnNpcTouched)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterConnectStatusEvent', self, self.OnMasterConnectStatus)
		# 显示菜单
		self.DefineEvent('showMenuPanel')
		self.ListenForEvent('Minecraft', 'SampleClient', 'MenuChooseOk', self, self.OnMenuChooseOk)	
		# 广播
		self.DefineEvent('MasterAnnounceEvent')
		self.ListenForEvent("Minecraft", "ServerSys", 'AnnounceEvent', self, self.MasterAnnounceEvent)
		# 配对
		self.DefineEvent('StartMatchingEvent')
		self.DefineEvent('CancelMatchEvent')
		self.DefineEvent('MasterPlayerMatchingStatus')
		self.DefineEvent('MasterPlayerMatchingResult')
		self.ListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		self.ListenForEvent("idv", "masterMatch", 'PlayerMatchingResult', self, self.OnPlayerMatchingResult)
		self.ListenForEvent('Minecraft', 'SampleClient', 'PlayerMatchSucRec', self, self.OnPlayerMatchSucRec)	
		
	def Destroy(self):
		print '--------systemServer====destroy!!!!!~~~~~'
		self.UnListenForEvent('Minecraft', 'SampleClient', 'PlayerJoin', self, self.OnPlayerJoin)	
		self.UnListenForEvent('Minecraft', 'SampleClient', 'MenuChooseOk', self, self.OnMenuChooseOk)	
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DelServerPlayerEvent', self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MobDieEvent', self, self.OnMobDie)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityLoadScriptEvent', self, self.OnPlayerExtraData)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerPlayerBornPosEvent', self, self.OnPlayerBornPosEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DamageEvent', self, self.OnNpcTouched)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterConnectStatusEvent', self, self.OnMasterConnectStatus)
		#
		self.UnListenForEvent("Minecraft", "ServerSys", 'AnnounceEvent', self, self.MasterAnnounceEvent)
		self.UnListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		self.UnListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingResult)
		self.UnListenForEvent('Minecraft', 'SampleClient', 'PlayerMatchSucRec', self, self.OnPlayerMatchSucRec)	
		
	def Update(self):
		if self.npcMgr and self.npcMgr.waiting_create_npc():
			self.frame_count += 1
			if self.frame_count % 10 == 0:
				self.npcMgr.try_init_npc()
				
	def OnMasterConnectStatus(self, data):
		print "OnMasterConnectSuccess", data
		serverid = netgame_api.get_netgame_serverid()
		exist = netgame_api.check_master_exist()
		print "recent serverid=%d master exist=%d" % (serverid, exist)
	
	def OnPlayerJoin(self, data):
		print "OnPlayerJoin", data
		player_data = self.playerDic.get(data["id"], None)
		if not player_data:
			return
		self.updateExtraDataToPlayer(player_data)
	
	def updateExtraDataToPlayer(self, player_data):
		data = self.CreateEventData()
		data['id'] = player_data.pid
		data['exp'] = player_data.exp
		data['level'] = player_data.level
		# self.NotifyToClient(player_data.pid, 'updatePlayerExtraData', data)
		self.BroadcastToAllClient('updatePlayerExtraData', data)
		#
		comp = self.CreateComponent(player_data.pid, "Minecraft", "msg")
		comp.msg = "exp=%d level=%d" % (player_data.exp, player_data.level)
		self.NeedsUpdate(comp)
		
	def OnMobDie(self, data):
		mobId = data.get('id','-1')
		attackerId = data.get('attacker','-1')
		print "OnMobDie mobId=%s attackerId=%s" % (mobId, attackerId)
		player_data = self.playerDic.get(attackerId, None)
		if not player_data:
			return
		player_data.addExp(10)
		self.updateExtraDataToPlayer(player_data)
		print "player kill mob id=%s exp=%s level=%s" % (player_data.pid, player_data.exp, player_data.level)
		comp = self.GetComponent(player_data.pid, "Minecraft", "extraData")
		comp.extraData.exp = player_data.exp
		comp.extraData.level = player_data.level
		self.NeedsUpdate(comp)
		
	def OnAddServerPlayer(self, data):
		playerId = data.get('id','-1')
		print "OnAddServerPlayer playerId=%s" % playerId
		comp = self.GetComponent(playerId, "Minecraft", "extraData")
		if comp:
			print "GetComponent success"
			player_data = PlayerData(playerId, comp.extraData.exp, comp.extraData.level)
		else:
			print "GetComponent fail"
			comp = self.CreateComponent(playerId, "Minecraft", "extraData")
			player_data = PlayerData(playerId, 0, 1)
			comp.extraData.exp = player_data.exp
			comp.extraData.level = player_data.level
			self.NeedsUpdate(comp)
		player_data.netgame_uid = netgame_api.get_player_netgame_uid(playerId)
		player_data.netgame_nickname = netgame_api.get_player_netgame_nickname(playerId)
		self.playerDic[playerId] = player_data
	
	def OnDelServerPlayer(self, data):
		playerId = data.get('id','-1')
		print "OnDelServerPlayer playerId=%s" % playerId
		if self.playerDic.has_key(playerId):
			del self.playerDic[playerId]
			
	def find_player_by_netgame_uid(self, netgame_uid):
		for player_data in self.playerDic.itervalues():
			if player_data.netgame_uid == netgame_uid:
				return player_data
		return None
		
	def OnPlayerExtraData(self, data):
		print "=====OnPlayerExtraData", data
		playerId = data[0]
		comp = self.GetComponent(playerId, "Minecraft", "extraData")
		if not comp:
			print "GetComponent fail create new with exist data"
			comp = self.CreateComponent(playerId, "Minecraft", "extraData")
		print comp.extraData.exp
		print comp.extraData.level
		print "=====OnPlayerExtraData finish======"
		
	def OnPlayerBornPosEvent(self, data):
		print "======OnPlayerBornPosEvent", data
		if sample_config.IS_LOBBY_STYLE:
			data['posx'] = sample_config.BORN_POS[0]
			data['posy'] = sample_config.BORN_POS[1]
			data['posz'] = sample_config.BORN_POS[2]
			data['ret'] = True
		elif self.npcMgr is None:
			# 准备要初始化的npc
			self.npcMgr = npcManager.Manager(self)
			extra_data = {
				"pos" : (data['posx']+2, data['posy']-1, data['posz']+2)
			}
			self.npcMgr.register_npc("trans2lobby", extra_data)
	#---------------------------------------------------------------------------------
	def OnNpcTouched(self, args):
		print "=====================OnNpcTouched", args
		player_data = self.playerDic.get(args['srcId'], None)
		if not player_data:
			return
		npc_data = self.npcMgr.get_npc(args['entityId'])
		if not npc_data:
			return
		args["damage"] = 0
		if npc_data.speckey == "ranking":
			print "show ranking"
		else:
			print "show showMenuPanel"
			data = self.CreateEventData()
			data['menuKey'] = npc_data.speckey
			self.NotifyToClient(args['srcId'], 'showMenuPanel', data)
	
	def OnMenuChooseOk(self, args):
		print "OnMenuChooseOk", args
		if args['menuKey'] == 'trans2game':
			netgame_api.transfer_to_other_server(args['id'], 'game')
		elif args['menuKey'] == 'trans2lobby':
			netgame_api.transfer_to_other_server(args['id'], 'lobby')
		elif args['menuKey'] == 'match':
			is_start = args['start']
			self.send2master_matching(args["id"], is_start)
	#---------------------------------------------------------------------------------------
	# 来自master的广播事件
	def MasterAnnounceEvent(self, args):
		print "======MasterAnnounceEvent", args
		data = self.CreateEventData()
		data['message'] = args['message']
		self.BroadcastToAllClient('MasterAnnounceEvent', data)
	#---------------------------------------------------------------------------------------
	# 配对逻辑	
	def send2master_matching(self, playerId, is_start):
		player_data = self.playerDic.get(playerId, None)
		if not player_data:
			print "send2master_matching by not player"
			return
		netgame_uid = player_data.netgame_uid
		if not netgame_uid:
			print "send2master_matching fail netgame_uid=%s" % str(netgame_uid) 
			return
		data = self.CreateEventData()
		data["id"] = netgame_uid
		data["serverId"] = netgame_api.get_netgame_serverid()
		if is_start:
			self.NotifyToMaster("StartMatchingEvent", data)
		else:
			self.NotifyToMaster("CancelMatchEvent", data)
		print "send2master_matching done"
	
	# 来自master的配对事件
	def OnPlayerMatchingStatus(self, args):
		print "======OnPlayerMatchingStatus", args
		player_data = self.find_player_by_netgame_uid(args["id"])
		if not player_data:
			print "change matching status by no player"
			return
		data = self.CreateEventData()
		data['is_start'] = args['is_start']
		data['suc'] = args['suc']
		data['reason'] = args['reason']
		self.NotifyToClient(player_data.pid, 'MasterPlayerMatchingStatus', data)
	
	def OnPlayerMatchingResult(self, args):
		print "======OnPlayerMatchingResult", args
		player_data = self.find_player_by_netgame_uid(args["id"])
		if not player_data:
			print "receive matching result by no player"
			return
		data = self.CreateEventData()
		data['suc'] = args['suc']
		if data['suc']:
			data['serverid'] = args['serverid']
		else:
			data['serverid'] = 0
		data['reason'] = args['reason']
		self.NotifyToClient(player_data.pid, 'MasterPlayerMatchingResult', data)
	
	def OnPlayerMatchSucRec(self, args):
		print "=======OnPlayerMatchSucRec", args
		player_data = self.playerDic.get(args["id"], None)
		if not player_data:
			print "receive client match rec by not player"
			return
		netgame_api.transfer_to_other_server_by_id(args["id"], args["serverid"])
		
	
		
		
		