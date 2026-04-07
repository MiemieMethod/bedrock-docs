# -*- coding: utf-8 -*-
import apolloCommon.commonNetgameApi as commonNetgameApi
import neteaseResidenceScript.playerGas as playerGas
import neteaseResidenceScript.util as util
import neteaseResidenceScript.dbApi as dbApi
from neteaseResidenceScript.residenceConsts import DimensionIdOverWorld
import lobbyGame.netgameApi as lobbyGameApi
import neteaseResidenceScript.residenceConsts as residenceConsts

class PlayerMgr(object):
	"""
	玩家管理器
	"""
	def __init__(self):
		self.mServerType = commonNetgameApi.GetServerType()
		util.ListenEngineEvent('ServerItemUseOnEvent', self, self.OnServerItemUseOn)
		util.ListenEngineEvent('ServerPlayerTryDestroyBlockEvent', self, self.OnServerPlayerTryDestroyBlock)
		util.ListenEngineEvent('ServerBlockUseEvent', self, self.OnServerBlockUse)
		util.ListenEngineEvent('DamageEvent', self, self.OnDamage)
		# 领地外的爆炸是否可破坏方块，源头来自非领地所有者的爆炸（包括生物），无法影响领地
		util.ListenEngineEvent('ServerExplosionBlockEvent', self, self.OnExplosionBlock)
		# 是否可影响物理方块，主要影响玩家脚踩压力板、踩红石矿、踩拌线钩三种行为。如果配置为否，非领地所有者这三种行为不会生效
		util.ListenEngineEvent('StepOnBlockServerEvent', self, self.OnStepOnBlock)
		# 非领地所有者（包括非玩家的生物）是否可使方块变化，包括踩踏耕地、破门而入、捡起方块、破坏方块等
		util.ListenEngineEvent('MobGriefingBlockServerEvent', self, self.OnMobGriefingBlock)
		# 投掷物是否在领地内生效，用于防止玩家在领地外投掷喷溅药水/鸡蛋/弓箭/三叉戟等到领地内，影响领地内的生物
		util.ListenEngineEvent('ProjectileDoHitEffectEvent', self, self.OnProjectileDoHitEffect)
		# 可交互实体列表
		util.ListenEngineEvent('PlayerInteractServerEvent', self, self.OnPlayerInteract)
		# 是否可骑乘坐骑, 假如被骑乘的坐骑不在可交互实体列表中，那么就算开放了骑乘功能，也是无法骑乘的
		util.ListenEngineEvent('StartRidingServerEvent', self, self.OnStartRiding)
		# 是否可进入领地
		util.ListenEngineEvent('WillTeleportToServerEvent', self, self.OnWillTeleportTo)
		# 活塞是否可影响领地内方块
		util.ListenEngineEvent('PistonActionServerEvent', self, self.OnPistonAction)
		#
		self.mPlayerMap = {}
		self.mId2Uid = {}
		self.mFrame = 0
		self.mTickPlayers = []
		self.mTickLength = 0
		
		self.mPlayerCaches = {}
	
	def QueryPlayerDataUserName(self, userName, useCache, callback):
		"""
		根据昵称查询玩家个人信息
		"""
		if useCache:
			for uid, playerName in self.mPlayerCaches.iteritems():
				if playerName == userName:
					callback({"playerUid":uid})
					return
		def QueryPlayerDataCb(args, callback):
			exist = False
			uid = ""
			for data in args:
				if data:
					uid = data[0]
					playerName = data[1]
					exist = True
					if self.mPlayerCaches.has_key(uid) == False:
						self.mPlayerCaches[uid] = playerName
			if exist:
				callback({"playerUid":uid})
			else:
				callback(None)
		dbApi.QueryPlayerDataByUserName(userName,  lambda args: QueryPlayerDataCb(args, callback))
		
	# 逻辑帧
	# 分时驱动当前在线玩家的逻辑帧，每个玩家每秒一次，尽量平均分布到每个逻辑帧中
	def OnScriptTickServer(self):
		self.mFrame += 1
		if self.mFrame % 30 == 0:
			self.mTickPlayers = self.mPlayerMap.keys()
			self.mTickLength = (len(self.mTickPlayers) + 29) // 30
			if self.mTickLength < 2:
				self.mTickLength = 2
		for i in xrange(self.mTickLength):
			if not self.mTickPlayers:
				break
			uid = self.mTickPlayers.pop(0)
			player = self.mPlayerMap.get(uid, None)
			if player:
				player.CheckMove()

	def AddPlayer(self, playerId, uid):
		"""
		玩家上线
		"""
		player = playerGas.PlayerGas(playerId, uid)
		self.mId2Uid[playerId] = uid
		self.mPlayerMap[uid] = player
		dbApi.QueryPlayerResidence(uid, lambda records:self.QueryPlayerResidenceCallback(playerId, uid, records))
		dbApi.QueryPlayerResidenceAuthority(uid, self.mServerType, lambda records:self.QueryPlayerResidenceAuthorityCallback(uid, records))
		if uid != residenceConsts.SERVER_PLAYER_UID:
			userName = lobbyGameApi.GetPlayerNickname(playerId)
		else:
			userName = residenceConsts.SERVER_PLAYER_NICKNAME
		playerData = {"uid":uid, "username":userName}
		def InSertPlayerDataCB(args):
			if args:
				self.mPlayerCaches[uid] = userName
		dbApi.InSertPlayerData(playerData, lambda args:InSertPlayerDataCB(args))
		
	def SlowAddPlayer(self, playerId, uid):
		"""
		查询未读提示
		"""
		dbApi.QueryTransferUnread(uid, lambda args: self.QueryTransferUnreadCb(playerId, args))
		dbApi.QueryApplicationUnread(uid, lambda args: self.QueryApplicatorUnreadCb(playerId, args))
		
	def QueryApplicatorUnreadCb(self, playerId, args):
		unReadDataDict = {}
		for unReadData in args:
			if unReadData is not None:
				resId = unReadData[1]
				applicatorUid = unReadData[2]
				if unReadDataDict.has_key(resId) == False:
					unReadDataDict[resId] = []
				unReadDataDict[resId].append(applicatorUid)
		util.residenceSystem.NotifyToClient(playerId, "UpdateApplicatorUnreadFromServerEvent", {"unRead": unReadDataDict})
		
	def QueryTransferUnreadCb(self, playerId, args):
		unReadDataList = []
		for unReadData in args:
			if unReadData is not None:
				resId = unReadData[1]
				unReadDataList.append(resId)
		util.residenceSystem.NotifyToClient(playerId, "UpdateTransferUnreadFromServerEvent", {"unRead":unReadDataList})
				

	def QueryPlayerResidenceCallback(self, playerId, uid, records):
		player = self.mPlayerMap.get(uid, None)
		if not player:
			return
		player.CacheResData(records)
		if player.mResDataQueryed and player.mClientKnock:
			util.GetResidenceSystem().SendLoginResponse(player)
		
		resApplication = {}
		resAuthority = {}
		for oneResData in records:
			if oneResData:
				resId = oneResData[0]
				mResApplication = util.residenceSystem.GetResidenceMgr().mResApplication
				mResAuthority = util.residenceSystem.GetResidenceMgr().mResAuthority
				if mResApplication.has_key(resId) == True:
					resApplication[resId] = mResApplication[resId]
				if mResAuthority.has_key(resId) == True:
					resAuthority[resId] = mResAuthority[resId]
		if resApplication:
			util.residenceSystem.NotifyToClient(playerId, "UpdateApplicationFromServerEvent", resApplication)
		if resAuthority:
			util.residenceSystem.NotifyToClient(playerId, "UpdateAuthorityFromServerEvent", resAuthority)
				

	def QueryPlayerResidenceAuthorityCallback(self, uid, records):
		player = self.mPlayerMap.get(uid, None)
		if not player:
			return
		player.CacheAuthorityData(records)
		if player.mResDataQueryed and player.mClientKnock:
			util.GetResidenceSystem().SendLoginResponse(player)

	def GetPlayerById(self, playerId):
		if playerId not in self.mId2Uid:
			return None
		uid = self.mId2Uid[playerId]
		return self.mPlayerMap[uid]

	def GetPlayerByUid(self, uid):
		return self.mPlayerMap.get(uid, None)

	def DelPlayer(self, playerId):
		uid = self.mId2Uid.get(playerId, None)
		if uid:
			del self.mId2Uid[playerId]
			del self.mPlayerMap[uid]

	def FindResidenceOnlineOwners(self, resId):
		result = []
		for player in self.mPlayerMap.itervalues():
			if player.IsResidenceOwner(resId):
				result.append(player.mUid)
		return result

	def CleanOwnerAndAuthorityByDeleteResidence(self, resIdList):
		for player in self.mPlayerMap.itervalues():
			player.CleanOwnerAndAuthorityByDeleteResidence(resIdList)

	def GetAllPlayerIdList(self):
		idList = []
		for player in self.mPlayerMap.itervalues():
			idList.append(player.mPlayerId)
		return idList
	# ---------------------------------------------------------------------------------------------
	# 指定玩家在当前位置是否行为受限，返回是否受限，或具体权限信息
	# 非领地玩家行为不受限
	# 玩家是领地所有者，行为不受限
	# 玩家是领地外部人员，根据具体情况返回配置的结果，最终使用mod.json保底
	def GetLimitAndAuthorityByResidence(self, entityId, dim, pos, aukey):
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, pos)
		if not resInfoList:		# 非领地玩家行为不受限
			return False, None
		player = self.GetPlayerById(entityId)
		if not player:		# 非玩家或者不在线的玩家，默认受限
			return True, None
		topLevelResId = resInfoList[-1]["id"]
		if player.IsResidenceOwner(topLevelResId):		# 玩家是领地所有者，行为不受限
			return False, None
		# 对于领地外部人员的限制，部分权限需要考虑玩家个体限制，部分权限不需要考虑
		auValue = self.GetAuthorityMutex(aukey, resInfoList, player)
		return None, auValue

	def GetAuthorityMutex(self, aukey, resInfoList, player):
		usePlayer = residenceConsts.AuthorityForPlayer.get(aukey, False)
		if usePlayer:
			auValue = self.GetAuthorityWithPlayer(aukey, resInfoList, player)
		else:
			auValue = self.GetAuthorityWithoutPlayer(aukey, resInfoList)
		return auValue

	def GetAuthorityWithPlayer(self, aukey, resInfoList, player):
		for resInfo in resInfoList:
			# 如果玩家独立配置了领地权限
			# 那么玩家自身的权限配置拥有最高的优先级
			ret = player.FindPlayerAuthority(aukey, resInfo["id"])
			if not ret is None:
				return ret
			# 否则查看子领地权限
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return ret
		# 最终保底还是返回mod.json的默认值
		return util.GetModConfByField(aukey)

	def GetAuthorityWithoutPlayer(self, aukey, resInfoList):
		for resInfo in resInfoList:
			ret = resInfo["authority"].get(aukey, None)
			if not ret is None:
				return ret
		# 最终保底还是返回mod.json的默认值
		return util.GetModConfByField(aukey)
	# --------------------------------------------------------------------------------------------
	def DoShowHintToPlayer(self, playerId, aukey, itemOrBlockName="", auxValue=0):
		player = self.GetPlayerById(playerId)
		if not player:
			return
		if aukey == "place_on_block_items_limit":
			hint = "当前领地禁止对方块使用该物品"
		elif aukey == "can_destroy_block_limit":
			hint = "当前领地禁止破坏此类型方块"
		elif aukey == "cannot_interact_block_list":
			hint = "当前领地禁止和该方块交互"
		elif aukey == "can_block_be_stepon":
			if itemOrBlockName == "minecraft:farmland":
				hint = "当前领地禁止踩踏耕地"
			else:
				hint = "当前领地禁止影响物理方块"
		elif aukey == "can_block_be_mobgriefing":
			if itemOrBlockName == "minecraft:farmland":
				hint = "当前领地禁止踩踏耕地"
			else:
				return
		elif aukey == "can_attack_player":
			hint = "当前领地禁止攻击其它玩家"
		elif aukey == "can_attack_mob":
			hint = "当前领地禁止攻击生物"
		elif aukey == "can_projectile_take_effect":
			hint = "当前领地投掷物无法生效"
		elif aukey == "can_interact_entity_list":
			hint = "当前领地无法和该对象交互"
		elif aukey == "can_ride":
			hint = "当前领地禁止骑乘坐骑"
		elif aukey == "can_other_player_enter":
			hint = "当前领地禁止进入"
		else:
			return
		if not player.CheckCanHint(aukey):
			return
		print "DoShowHintToPlayer playerId=%s" % playerId, hint
		util.NotifyOneMessage(playerId, hint)

	def RefreshAllPlayerResidence(self):
		for player in self.mPlayerMap.itervalues():
			player.RefreshResidence()

	def OnServerItemUseOn(self, data):
		'''
		检查可对方块使用物品列表
		'''
		# print "OnServerItemUseOn", data['x'], data['y'], data['z']
		playerId = data['entityId']
		dim = util.GetEntityDimensionId(playerId)
		placePos = (data['x'], data['y'], data['z'])
		#util.residenceSystem.GetResidenceMgr().mResAuthority
		beLimit, limitItems = self.GetLimitAndAuthorityByResidence(playerId, dim, placePos, "place_on_block_items_limit")
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, placePos)
		if not resInfoList:  # 非领地玩家行为不受限
			return
		player = self.GetPlayerById(playerId)
		if not player:  # 非玩家或者不在线的玩家，默认受限
			return
		topLevelResId = resInfoList[-1]["id"]
		playerUid = self.mId2Uid[playerId]
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["ret"] = True
			return
		if util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(playerUid, {}).get("authority", {}).get("PlacedBlock", True) == False:
			data["ret"] = True
			return
		# 需要看具体权限的外部玩家
		useItem = '%s:%s' % (data['itemName'], data['auxValue'])
		if useItem not in limitItems:
			data["ret"] = True
			self.DoShowHintToPlayer(playerId, "place_on_block_items_limit", data['itemName'], data['auxValue'])
		
		
	def OnServerPlayerTryDestroyBlock(self, data):
		'''
		检查方块是否可以破坏
		'''
		# print 'OnServerPlayerTryDestroyBlock test', data
		playerId = data['playerId']
		dim = util.GetEntityDimensionId(playerId)
		blockPos = (data['x'], data['y'], data['z'])
		beLimit, canDestroyItems = self.GetLimitAndAuthorityByResidence(playerId, dim, blockPos, "can_destroy_block_limit")
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, blockPos)
		if not resInfoList:  # 非领地玩家行为不受限
			return
		player = self.GetPlayerById(playerId)
		if not player:  # 非玩家或者不在线的玩家，默认受限
			return
		topLevelResId = resInfoList[-1]["id"]
		playerUid = self.mId2Uid[playerId]
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		if util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(playerUid, {}).get("authority", {}).get("PlacedBlock", False) == False:
			data["cancel"] = True
			self.DoShowHintToPlayer(playerId, "can_destroy_block_limit")
			return
		# 需要看具体权限的外部玩家
		blockItem = '%s:%s' % (data['fullName'], data['auxData'])
		if blockItem not in canDestroyItems:
			data['cancel'] = True
			self.DoShowHintToPlayer(playerId, "can_destroy_block_limit", data['fullName'], data['auxData'])

	def OnServerBlockUse(self, data):
		'''
		不同领地内方块进行交互
		'''
		playerId = data['playerId']
		dim = util.GetEntityDimensionId(playerId)
		blockPos = (data['x'], data['y'], data['z'])
		beLimit, notInteractItems = self.GetLimitAndAuthorityByResidence(playerId, dim, blockPos, "cannot_interact_block_list")
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, blockPos)
		print "useDoorAuth1",resInfoList
		if not resInfoList:  # 非领地玩家行为不受限
			return
		player = self.GetPlayerById(playerId)
		if not player:  # 非玩家或者不在线的玩家，默认受限
			return
		topLevelResId = resInfoList[-1]["id"]
		playerUid = self.mId2Uid[playerId]
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		if util.GetResidenceGasMgr().mResAuthority.get(topLevelResId, {}).get(playerUid, {}).get("authority", {}).get("UseDoor", False) == True:
			data["cancel"] = False
			#self.DoShowHintToPlayer(playerId, "cannot_interact_block_list")
			return
		# 需要看具体权限的外部玩家
		blockItem = '%s:%s' % (data['blockName'], data['aux'])
		blockItemAll = '%s:%s' % (data['blockName'], "*")
		#print "notInteractItems", notInteractItems
		print "useDoorAuth2", notInteractItems
		if blockItem in notInteractItems or blockItemAll in notInteractItems:
			data["cancel"] = True
			self.DoShowHintToPlayer(playerId, "cannot_interact_block_list", data['blockName'], data['aux'])

	def OnStepOnBlock(self, data):
		'''
		脚踩压力板、踩红石矿、踩拌线钩
		'''
		# print "OnStepOnBlock", data
		entityId = data["entityId"]
		dim = util.GetEntityDimensionId(entityId)
		blockPos = (data['blockX'], data['blockY'], data['blockZ'])
		beLimit, canBlockBeStepon = self.GetLimitAndAuthorityByResidence(entityId, dim, blockPos, "can_block_be_stepon")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		if not canBlockBeStepon:
			data["cancel"] = True
			self.DoShowHintToPlayer(entityId, "can_block_be_stepon", data['blockName'])

	def OnMobGriefingBlock(self, data):
		'''
		踩踏耕地
		'''
		print "OnMobGriefingBlock", data
		entityId = data["entityId"]
		dim = util.GetEntityDimensionId(entityId)
		blockPos = (data['blockX'], data['blockY'], data['blockZ'])
		beLimit, canBlockBeMobgriefing = self.GetLimitAndAuthorityByResidence(entityId, dim, blockPos, "can_block_be_mobgriefing")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		if not canBlockBeMobgriefing:
			data["cancel"] = True
			self.DoShowHintToPlayer(entityId, "can_block_be_mobgriefing", data['blockName'])

	def OnExplosionBlock(self, data):
		"""
		爆炸破坏方块
		"""
		# print "OnExplosionBlock", data
		entityId = data["entityId"]
		dim = util.GetEntityDimensionId(entityId)
		for idx, blockInfo in enumerate(data["data"]):
			x, y, z, cancel = blockInfo
			blockPos = (x, y, z)
			beLimit, canBlockBeExploded = self.GetLimitAndAuthorityByResidence(entityId, dim, blockPos, "can_block_be_exploded")
			# 不受限的玩家
			if beLimit == False:
				continue
			# 强制受限的玩家
			if beLimit == True:
				data["data"][idx][3] = True
				continue
			# 需要看具体权限的外部玩家
			if not canBlockBeExploded:
				data["data"][idx][3] = True

	def OnProjectileDoHitEffect(self, data):
		"""
		投掷物命中
		"""
		# print "OnProjectileDoHitEffect", data
		entityId = data["srcId"]
		dim = util.GetEntityDimensionId(entityId)
		hitPos = (data["x"], data["y"], data["z"])
		beLimit, canProjectileTakeEffect = self.GetLimitAndAuthorityByResidence(entityId, dim, hitPos, "can_projectile_take_effect")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		if not canProjectileTakeEffect:
			data["cancel"] = True
			self.DoShowHintToPlayer(entityId, "can_projectile_take_effect")

	def OnDamage(self, data):
		"""
		判定领地内伤害是否生效
		"""
		entityId = data["entityId"]
		dim = util.GetEntityDimensionId(entityId)
		# 无法获取到位置，认为是非领地，维持原始逻辑
		targetPos = util.GetEntityPos(entityId)
		if not targetPos:
			return
		# 非领地区域，维持原始逻辑
		resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, targetPos)
		if not resInfoList:
			return
		topLevelResId = resInfoList[-1]["id"]
		srcId = data["srcId"]
		actor = self.GetPlayerById(srcId)
		target = self.GetPlayerById(entityId)
		if target:		# 对象是玩家
			auKey = "can_attack_player"
		else:
			auKey = "can_attack_mob"
		if not actor:	# 攻击者不是玩家，默认受限
			data["damage"] = 0
			data["knock"] = False
			return
		if actor.IsResidenceOwner(topLevelResId):  # 玩家是领地所有者，行为不受限
			return
		# 需要看具体权限的外部玩家
		auValue = self.GetAuthorityMutex(auKey, resInfoList, actor)
		if not auValue:
			data["damage"] = 0
			data["knock"] = False
			self.DoShowHintToPlayer(srcId, auKey)

	def OnPlayerInteract(self, data):
		"""
		玩家与实体交互
		"""
		# print "OnPlayerInteract", data
		playerId = data["playerId"]
		dim = util.GetEntityDimensionId(playerId)
		targetPos = util.GetEntityPos(data["victimId"])
		# 无法获取到位置，认为是非领地，维持原始逻辑
		if not targetPos:
			return
		beLimit, canInteractEntityList = self.GetLimitAndAuthorityByResidence(playerId, dim, targetPos, "can_interact_entity_list")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		entityName = util.GetEntityIdentifier(data["victimId"])
		if entityName not in canInteractEntityList:
			data["cancel"] = True
			self.DoShowHintToPlayer(playerId, "can_interact_entity_list")

	def OnStartRiding(self, data):
		"""
		玩家上坐骑
		"""
		# print "OnStartRiding", data
		actorId = data["actorId"]
		dim = util.GetEntityDimensionId(actorId)
		targetPos = util.GetEntityPos(data["victimId"])
		# 无法获取到位置，认为是非领地，维持原始逻辑
		if not targetPos:
			return
		beLimit, canRide = self.GetLimitAndAuthorityByResidence(actorId, dim, targetPos, "can_ride")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		if not canRide:
			data["cancel"] = True
			self.DoShowHintToPlayer(actorId, "can_ride")

	def OnWillTeleportTo(self, data):
		"""
		即将传送
		"""
		# print "OnWillTeleportTo", data
		# 领地逻辑仅仅对主世界生效
		entityId = data["entityId"]
		dim = data["toDimensionId"]
		targetPos = (data["toX"], data["toY"], data["toZ"])
		beLimit, canOtherPlayerTeleport = self.GetLimitAndAuthorityByResidence(entityId, dim, targetPos, "can_other_player_teleport")
		# 不受限的玩家
		if beLimit == False:
			return
		# 强制受限的玩家
		if beLimit == True:
			data["cancel"] = True
			return
		# 需要看具体权限的外部玩家
		if not canOtherPlayerTeleport:
			data["cancel"] = True
			self.DoShowHintToPlayer(entityId, "can_other_player_teleport")

	def OnPistonAction(self, data):
		"""
		活塞推送方块
		"""
		# print "OnPistonAction", data
		dim = data["dimensionId"]
		for blockPos in data.get("blockList", []):
			resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, blockPos)
			if not resInfoList:  # 非领地行为不受限
				continue
			canPistonEffectInto = self.GetAuthorityWithoutPlayer("can_piston_effect_into", resInfoList)
			if not canPistonEffectInto:
				data["cancel"] = True
				return
		for blockPos in data.get("breakBlockList", []):
			resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, blockPos)
			if not resInfoList:  # 非领地行为不受限
				continue
			canPistonEffectInto = self.GetAuthorityWithoutPlayer("can_piston_effect_into", resInfoList)
			if not canPistonEffectInto:
				data["cancel"] = True
				return
		for entityId in data.get("entityList", []):
			pos = util.GetEntityPos(entityId)
			if not pos:
				continue
			resInfoList = util.GetResidenceGasMgr().FindResidenceByPos(dim, pos)
			if not resInfoList:  # 非领地行为不受限
				continue
			canPistonEffectInto = self.GetAuthorityWithoutPlayer("can_piston_effect_into", resInfoList)
			if not canPistonEffectInto:
				data["cancel"] = True
				return

	def Destroy(self):
		pass