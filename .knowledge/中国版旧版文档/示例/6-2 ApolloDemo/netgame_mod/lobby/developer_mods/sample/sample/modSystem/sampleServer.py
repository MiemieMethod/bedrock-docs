# -*- coding: utf-8 -*-
#
import time

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
		# 玩家脚本内数据对象的字典
		self.playerDic = {}
		# 逻辑帧数，主要是为了限制一些轮询操作的频率
		self.frame_count = 0
		# 排行榜的缓存和最后一次获取排行榜的时间戳
		self.ranking_cache = None
		self.ranking_cache_time = 0
		# 初始化主城的一些设置
		if sample_config.IS_LOBBY_STYLE:
			# 设置主城模式，包括不许改变地形，不变换天气日夜等
			netgame_api.set_city_mode(True)
			# 开启自动重生逻辑，Y左边低于一定程度会自动拉回出生点
			x, y, z = sample_config.BORN_POS
			serverlevel.set_auto_respawn(True, 30, 0, x, y, z)
			# 设置地图最大区域
			serverlevel.set_enable_limit_area(True, int(x), int(y), int(z), sample_config.LIMIT_AREA[0], sample_config.LIMIT_AREA[1])
			# 准备要初始化的npc
			self.npcMgr = npcManager.Manager(self)
			for keyname, extra_data in sample_config.PROP_NPCS.iteritems():
				self.npcMgr.register_npc(keyname, extra_data)
		else:
			self.npcMgr = None
		#
		print '--------Server Listen ---------->>>>>>>'
		# 【自定义事件，向客户端发送自定义玩家属性信息】
		self.DefineEvent('updatePlayerExtraData')
		# 【响应客户端自定义事件，客户端玩家加载成功】
		self.ListenForEvent('Minecraft', 'SampleClient', 'PlayerJoin', self, self.OnPlayerJoin)	
		# 【新玩家登陆服务器成功】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'AddServerPlayerEvent', self, self.OnAddServerPlayer)
		# 【玩家离线】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DelServerPlayerEvent', self, self.OnDelServerPlayer)
		# 【怪物死亡】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MobDieEvent', self, self.OnMobDie)
		# 【由组件提供的额外数据加载】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'EntityLoadScriptEvent', self, self.OnPlayerExtraData)
		# 【玩家即将上线，设定玩家出生位置】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerPlayerBornPosEvent', self, self.OnPlayerBornPosEvent)
		# 处理master连接事件
		# 排行榜
		# 【自定义事件，向客户端发送显示排行榜】
		self.DefineEvent('showRanking')
		# 【自定义事件，向Master请求排行榜数据信息】
		self.DefineEvent('RankingRequestEvent')
		# 【Mod脚本加载完成】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', self, self.OnLoadModSuccess)
		# 【与Master的连接状态产生变化】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterConnectStatusEvent', self, self.OnMasterConnectStatus)
		# 【响应Master的更新排行榜信息的事件】
		self.ListenForEvent("idv", "RankSys", 'RankingResponseEvent', self, self.OnRankingResponse)
		# 显示菜单
		# 【自定义事件，显示预定义菜单】
		self.DefineEvent('showMenuPanel')
		# 【NPC被敲击事件】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'DamageEvent', self, self.OnNpcTouched)
		# 【响应来自客户端的菜单选择结果事件】
		self.ListenForEvent('Minecraft', 'SampleClient', 'MenuChooseOk', self, self.OnMenuChooseOk)	
		# 广播
		self.DefineEvent('MasterAnnounceEvent')
		self.ListenForEvent("Minecraft", "ServerSys", 'AnnounceEvent', self, self.MasterAnnounceEvent)
		# 配对
		# 【自定义事件，向Master发送开始配对】
		self.DefineEvent('StartMatchingEvent')
		# 【自定义事件，向Master发送结束配对】
		self.DefineEvent('CancelMatchEvent')
		# 【自定义事件，向客户端发送配对状态变化的返回信息】
		self.DefineEvent('MasterPlayerMatchingStatus')
		# 【自定义事件，向客户端发送配对最终结果的信息】
		self.DefineEvent('MasterPlayerMatchingResult')
		# 【响应来自Master的玩家配对状态变化的消息】
		self.ListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		# 【响应来自Master的玩家配对最终结果的消息】
		self.ListenForEvent("idv", "masterMatch", 'PlayerMatchingResult', self, self.OnPlayerMatchingResult)
		# 【响应来自客户端的，已经接受配对结果的消息】
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
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter', self, self.OnLoadModSuccess)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterConnectStatusEvent', self, self.OnMasterConnectStatus)
		#
		self.UnListenForEvent("Minecraft", "ServerSys", 'AnnounceEvent', self, self.MasterAnnounceEvent)
		self.UnListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingStatus)
		self.UnListenForEvent("idv", "masterMatch", 'PlayerMatchingStatus', self, self.OnPlayerMatchingResult)
		self.UnListenForEvent('Minecraft', 'SampleClient', 'PlayerMatchSucRec', self, self.OnPlayerMatchSucRec)	
		self.UnListenForEvent("idv", "RankSys", 'RankingResponseEvent', self, self.OnRankingResponse)
	
	# 脚本逻辑帧
	def Update(self):
		self.frame_count += 1
		# 假如有预定的NPC尚未生成，则每10帧检查一次，看看是否满足生成条件
		if self.npcMgr and self.npcMgr.waiting_create_npc():
			if self.frame_count % 10 == 0:
				self.npcMgr.try_init_npc()
		# 第一次获取排行榜数据后
		# 每20帧检查一次，假如缓存时间超过1分钟
		# 就重新获取一次
		if self.frame_count % 20 == 0 and self.ranking_cache_time > 0:
			pass_time = int(time.time()) - self.ranking_cache_time
			if pass_time > 60:
				self.do_call_ranking_from_master()
	#---------------------------------------------------------------------------------------------
	# 处理master连接
	# 排行榜逻辑示例
	# 由于master连接成功的时间点可能在Mod加载完成之前
	# 所以在Mod加载成功时，需要判断一下Master是否已经连接成功了
	# 假如已经和Master建立连接，则需要执行与Master连接成功相同的逻辑
	def OnLoadModSuccess(self, args):
		print "OnLoadModSuccess", args
		exist = netgame_api.check_master_exist()
		if exist:
			self.do_call_ranking_from_master()
	
	# 与Master成功建立连接，请求排行榜数据
	def OnMasterConnectStatus(self, args):
		print "OnMasterConnectStatus", args
		serverid = netgame_api.get_netgame_serverid()
		exist = netgame_api.check_master_exist()
		print "recent serverid=%d master exist=%d" % (serverid, exist)
		if args['isConnect']:
			self.do_call_ranking_from_master()
	
	# 请求排行榜数据
	def do_call_ranking_from_master(self):
		# 记录当前时间为最后一次请求时间
		self.ranking_cache_time = int(time.time())
		data = self.CreateEventData()
		data["serverId"] = netgame_api.get_netgame_serverid()
		# 向Master发送自定义事件，用于请求排行榜数据
		self.NotifyToMaster("RankingRequestEvent", data)
		print "====================do_call_ranking_from_master"
	
	# Master回应排行榜数据事件的响应函数
	# 缓存排行榜数据
	def OnRankingResponse(self, args):
		print "OnRankingResponse", args
		if not args['players']:
			self.ranking_cache = []
		else:
			self.ranking_cache = args['players']
	#---------------------------------------------------------------------------------------------
	# 自定义数据
	# 客户端成功登陆事件的响应函数
	# 向客户端发送额外数据
	def OnPlayerJoin(self, data):
		print "OnPlayerJoin", data
		player_data = self.playerDic.get(data["id"], None)
		if not player_data:
			return
		self.updateExtraDataToPlayer(player_data)
	
	# 向客户端发送额外数据
	# 目前只有独立的等级和经验
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
	
	# 响应服务器事件，在脚本层缓存通过组件获取的额外数据--角色经验+等级
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
	
	# 响应服务器事件，每杀死一个怪物获得经验值
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
	#---------------------------------------------------------------------------------------------
	# 响应玩家登陆成功的服务器事件
	# 在脚本层生成玩家数据对象
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
		# 缓存玩家对应的netease uid和昵称
		player_data.netgame_uid = netgame_api.get_player_netgame_uid(playerId)
		player_data.netgame_nickname = netgame_api.get_player_netgame_nickname(playerId)
		self.playerDic[playerId] = player_data
		print "OnAddServerPlayer fin uid=%s nickname=%s" % (player_data.netgame_uid, player_data.netgame_nickname)
	
	# 响应玩家离线的服务器事件
	# 在脚本层删除对应的玩家数据对象
	def OnDelServerPlayer(self, data):
		playerId = data.get('id','-1')
		print "OnDelServerPlayer playerId=%s" % playerId
		if self.playerDic.has_key(playerId):
			del self.playerDic[playerId]
	
	# 通过netease uid获取对应的脚本层玩家数据对象
	def find_player_by_netgame_uid(self, netgame_uid):
		for player_data in self.playerDic.itervalues():
			if player_data.netgame_uid == netgame_uid:
				return player_data
		return None
	#---------------------------------------------------------------------------------------------
	# 修改初始的出生点
	def OnPlayerBornPosEvent(self, data):
		print "======OnPlayerBornPosEvent", data
		if sample_config.IS_LOBBY_STYLE:
			data['posx'] = sample_config.BORN_POS[0]
			data['posy'] = sample_config.BORN_POS[1]
			data['posz'] = sample_config.BORN_POS[2]
			# 设置ret为True，上面的修改才会生效
			data['ret'] = True
	#---------------------------------------------------------------------------------
	# 功能NPC
	# 响应敲击NPC的事件
	# 如果玩家敲击了指定的功能NPC
	# 则根据NPC预设数据，显示跳转菜单、配对菜单、或排行榜弹出界面
	def OnNpcTouched(self, args):
		print "=====================OnNpcTouched", args
		player_data = self.playerDic.get(args['srcId'], None)
		if not player_data:
			return
		npc_data = self.npcMgr.get_npc(args['entityId'])
		if not npc_data:
			print "no npc_data"
			return
		args["damage"] = 0
		if npc_data.speckey == "ranking":
			print "show showRanking"
			data = self.CreateEventData()
			if self.ranking_cache:
				data['exist'] = 1
				data['cache'] = self.ranking_cache
			else:
				data['exist'] = 0
			self.NotifyToClient(args['srcId'], 'showRanking', data)
		else:
			print "show showMenuPanel"
			data = self.CreateEventData()
			data['menuKey'] = npc_data.speckey
			self.NotifyToClient(args['srcId'], 'showMenuPanel', data)
	
	# 响应客户端自定义事件
	# 根据弹出菜单的不同，有不同的反应
	def OnMenuChooseOk(self, args):
		print "OnMenuChooseOk", args
		if args['menuKey'] == 'trans2game':
			netgame_api.transfer_to_other_server(args['id'], 'game')
		elif args['menuKey'] == 'trans2lobby':
			netgame_api.transfer_to_other_server(args['id'], 'lobby')
		elif args['menuKey'] == 'trans2fps':
			netgame_api.transfer_to_other_server(args['id'], 'fps')
		elif args['menuKey'] == 'match':
			is_start = args['start']
			self.send2master_matching(args["id"], is_start)
	#---------------------------------------------------------------------------------------
	# 响应来自master的广播事件
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
			data["nickname"] = player_data.netgame_nickname
			self.NotifyToMaster("StartMatchingEvent", data)
		else:
			self.NotifyToMaster("CancelMatchEvent", data)
		print "send2master_matching done"
	
	# 来自master的配对状态事件
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
	
	# 来自Master的配对结果事件
	def OnPlayerMatchingResult(self, args):
		print "======OnPlayerMatchingResult", args
		player_data = self.find_player_by_netgame_uid(args["id"])
		if not player_data:
			print "receive matching result by no player"
			return
		data = self.CreateEventData()
		data['suc'] = args['suc']
		if data['suc']:
			data['serverid'] = args['serverId']
		else:
			data['serverid'] = 0
		data['reason'] = args['reason']
		self.NotifyToClient(player_data.pid, 'MasterPlayerMatchingResult', data)
	
	# 配对成功后，客户端确认收到配对成功消息
	# 自动跳转向指定ID的服务器进程
	def OnPlayerMatchSucRec(self, args):
		print "=======OnPlayerMatchSucRec", args
		player_data = self.playerDic.get(args["id"], None)
		if not player_data:
			print "receive client match rec by not player"
			return
		netgame_api.transfer_to_other_server_by_id(args["id"], args["serverid"])
		print "OnPlayerMatchSucRec done"
		print "==================begin trans2idv"
		
	
		
		
		