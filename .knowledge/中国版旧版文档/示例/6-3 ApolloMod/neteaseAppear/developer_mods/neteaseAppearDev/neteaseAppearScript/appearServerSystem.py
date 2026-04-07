# -*- coding: utf-8 -*-

import time
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import lobbyGame.netgameApi as lobbyGameApi
import apolloCommon.commonNetgameApi as commonNetgameApi
from mod_log import engine_logger as logger


from neteaseAppearScript.appearConst import ModName, ClientSystemName, ClientEvent, ServerEvent
import neteaseAppearScript.appearConst as appearConst
import neteaseAppearScript.dbApi as dbApi
import neteaseAppearScript.appearServerPlayer as appearServerPlayer

def CleanDict(_dict, exKey):
	if exKey in _dict:
		del _dict[exKey]
	for v in _dict.values():
		if type(v) == dict:
			CleanDict(v, exKey)

class AppearServerSystem(ServerSystem):
	"""
	"""
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# 初始化数据库
		dbApi.Init()
		# 加载配置信息
		self.InitConfig()
		#
		self.mFrame = 0
		self.mPlayerData = {}
		self.mNeedRemoveList = set()

		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "EntityStopRidingEvent", self, self.OnEntityStopRiding)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent", self, self.OnPlayerDieEvent)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.ClientEnter, self, self.OnClientReady)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.BuyAppear, self, self.OnBuyAppear)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.ChangeUseAppear, self, self.OnChangeUseAppear)
		self.ListenForEvent('neteaseTrade', 'neteaseTradeDev', 'PlayerDoughsUpdateEvent', self, self.OnUpdateMoney)

	def Destroy(self):
		dbApi.Destroy()
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "EntityStopRidingEvent", self, self.OnEntityStopRiding)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent", self, self.OnPlayerDieEvent)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.ClientEnter, self, self.OnClientReady)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.BuyAppear, self, self.OnBuyAppear)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.ChangeUseAppear, self, self.OnChangeUseAppear)
		self.UnListenForEvent('neteaseTrade', 'neteaseTradeDev', 'PlayerDoughsUpdateEvent', self, self.OnUpdateMoney)

	def InitConfig(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseAppearScript")
		if not cfg:
			return False
		exKey = "_comment"
		appearConst.PropModels.update(cfg["propModels"])
		CleanDict(appearConst.PropModels, exKey)
		appearConst.PropEffects.update(cfg["propEffects"])
		CleanDict(appearConst.PropEffects, exKey)
		appearConst.PropAppears.update(cfg["propAppears"])
		CleanDict(appearConst.PropAppears, exKey)
		appearConst.FreeAppears.extend(cfg["freeAppears"])
		appearConst.DefaultBody = cfg["defaultBody"]
		appearConst.EmptyAppearData.update(cfg["emptyAppearData"])
		CleanDict(appearConst.EmptyAppearData, exKey)
		appearConst.AllAppearTypes = []
		for appearConf in appearConst.PropAppears.itervalues():
			appearType = appearConf.get("type", None)
			if appearType is None:
				continue
			if appearType in appearConst.AllAppearTypes:
				continue
			appearConst.AllAppearTypes.append(appearType)
		

		return True

	def Update(self):
		self.mFrame += 1
		if self.mFrame % 30 == 0:
			for player in self.mPlayerData.itervalues():
				if not player.IsDirty():
					continue
				self.DoSavePlayer(player, isLeave=False)
			if self.mNeedRemoveList:
				for entityId in self.mNeedRemoveList:
					self.DestroyEntity(entityId)
				self.mNeedRemoveList = set()
	
	def SetEntityToRemove(self, entityId):
		self.mNeedRemoveList.add(entityId)
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
		elif command == "ride":
			if params[0] == "start":
				mountId = self.DoStartRide(playerId)
				if mountId:
					self.OnStartRidingSuccess(playerId, mountId)
			else:
				self.DoStopRide(playerId)
		elif command == "appear":
			if len(params) == 1:
				suc, code = self.TryChangeUseAppear(playerId, params[0], None)
			else:
				suc, code = self.TryChangeUseAppear(playerId, params[0], params[1])
			print "TryChangeUseAppear", suc, appearConst.FMT[code]
		elif command == "shop":
			self.OpenShopUI(playerId)
		elif command == "money":
			player = self.mPlayerData.get(playerId, None)
			if not player:
				return
			tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
			if not tradeSystem:
				return
			data = {
				"RMB": 100,
			}
			tradeSystem.UpdatePlayerDoughs(player.mUid, data)
		elif command == "judge":
			eventData = {
				"appearType": params[0],
				"style": params[1],
				"x": params[2],
				"y": params[3],
				"z": params[4],
			}
			self.NotifyToClient(playerId, ServerEvent.JudgePosAndRot, eventData)

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
		print "OnAddServerPlayer", args
		playerId = args["id"]
		uid = args["uid"]
		player = appearServerPlayer.PlayerAppear(playerId, uid)
		self.mPlayerData[playerId] = player
		dbApi.QueryPlayerAppearData(uid, lambda appearInfo:self.OnQueryPlayerCallback(playerId, appearInfo))
	
	def OnQueryPlayerCallback(self, playerId, appearInfo):
		print "OnQueryPlayerCallback", playerId, appearInfo
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		# 没有加载到数据，认为是第一次登录
		if appearInfo:
			player.OnQueryCallback(appearInfo)
		else:
			player.OnCreateByNew()
		# 如果此时客户端已经登录完成，那么需要发送serverReady
		self.CheckAndSendReady(player)

	def OnDelServerPlayer(self, args):
		print "OnDelServerPlayer", args
		playerId = args["id"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		del self.mPlayerData[playerId]
		# 如果query数据库都没有完成，就不需要存档了
		if not player.DataReady():
			return
		if player.IsDirty():
			self.DoSavePlayer(player, isLeave=True)
	
	def OnPlayerDieEvent(self, args):
		playerId = args["id"]
		# 死亡时，强制下坐骑
		self.OnRealStopRiding(playerId)
		# 通知客户端，清理特效缓存
		eventData = {
			"playerId":playerId,
		}
		self.BroadcastEvent(ServerEvent.PlayerDie, eventData)
	
	def DoSavePlayer(self, player, isLeave=False):
		print "DoSavePlayer", isLeave
		needInsert = player.NeedInsert()
		playerId, uid, appearInfo = player.GetSaveData()
		if needInsert:
			dbApi.InsertPlayerAppearData(uid, appearInfo, lambda suc:self.OnSaveByInsertCallback(playerId, uid, appearInfo, isLeave, suc))
		else:
			dbApi.UpdatePlayerAppearData(uid, appearInfo, lambda suc:self.OnSaveByUpdateCallback(playerId, uid, appearInfo, isLeave, suc))
		player.SetSaved()
	
	def OnSaveByInsertCallback(self, playerId, uid, appearInfo, isLeave, suc):
		if isLeave:
			if not suc:
				logger.error("OnSaveByInsertCallback fail uid={} info={}".format(uid, appearInfo))
			return
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		if suc:	# 存档成功，设置标识位，下次触发存档就不会使用Insert方式了
			player.SetNotNeedInsert()
		else:	# 存档失败，设置为dirty，下次会再次触发存档
			player.SetDirty()

	def OnSaveByUpdateCallback(self, playerId, uid, appearInfo, isLeave, suc):
		if isLeave:
			if not suc:
				logger.error("OnSaveByUpdateCallback fail uid={} info={}".format(uid, appearInfo))
			return
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		if not suc:	# 存档失败，设置为dirty，下次会再次触发存档
			player.SetDirty()
	#------------------------------------------------------------------------------------------------------------------------------------
	def OpenShopUI(self, playerId):
		print "OpenShopUI", playerId
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		if not player.mMoneyData is None:
			self.SendOpenShopUI(playerId, player.mMoneyData)
			return
		tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
		if tradeSystem:
			def queryMoneyCallback(suc, data):
				if suc and data["code"] == 1:
					moneyData = data.get("entity", {})
					player.CacheMoneyData(moneyData)
				else:
					moneyData = {}
				self.SendOpenShopUI(playerId, moneyData)
			tradeSystem.QueryPlayerDoughs(player.mUid, queryMoneyCallback)
		else:
			self.SendOpenShopUI(playerId, {})

	def SendOpenShopUI(self, playerId, moneyData):
		print "SendOpenShopUI", playerId, moneyData
		eventData = {
			"moneyData": moneyData,
		}
		self.NotifyToClient(playerId, ServerEvent.ShowShop, eventData)
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnUpdateMoney(self, data):
		uid, moneyType, moneyValue = data["uid"], data["k"], data["dt"]
		for playerId, playerData in self.mPlayerData.iteritems():
			if playerData.mUid == uid:
				playerData.ChangeMoneydata(moneyType, moneyValue)
				eventData = {
					"moneyData": playerData.mMoneyData,
				}
				self.NotifyToClient(playerId, ServerEvent.SyncMoney, eventData)
				break

	def SendActionResponse(self, playerId, message):
		message = '§a%s' % message
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, message, 2, 0.5, 0.8)
		else:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % message, playerId)

	def OnClientReady(self, data):
		print "OnClientReady", data
		playerId = data["playerId"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		player.SetClientReady()
		self.CheckAndSendReady(player)

	def CheckAndSendReady(self, player):
		if not player.mClientReady or not player.mDbLoaded:
			return
		eventData = {
			"uid": player.mUid,
			"PropModels": appearConst.PropModels,
			"PropEffects": appearConst.PropEffects,
			"PropAppears": appearConst.PropAppears,
			"FreeAppears": appearConst.FreeAppears,
			"AllAppearTypes": appearConst.AllAppearTypes,
			"EmptyAppearData": appearConst.EmptyAppearData,
		}
		self.NotifyToClient(player.mPlayerId, ServerEvent.ServerReady, eventData)
		# 刚刚上线，默认清理坐骑骑乘状态
		rideComp = serverApi.CreateComponent(player.mPlayerId, "Minecraft", "ride")
		if rideComp.IsEntityRiding():
			rideComp.StopEntityRiding()
		player.SetUseMount(None)
		# 发送外观的解锁状态给新登录的player
		eventData = {
			"appearInfo": player.mAppearInfo,
		}
		self.NotifyToClient(player.mPlayerId, ServerEvent.SyncAppearInfo, eventData)
		# 群发当前的外观给所有client
		self.DoBroadcastUseAppear(player)
		# 发送其他所有玩家的外观给当前新登录的player
		for otherPlayerId, otherPlayer in self.mPlayerData.iteritems():
			if otherPlayerId == player.mPlayerId:
				continue
			self.NotifyToClient(player.mPlayerId, ServerEvent.UpdateUseAppear, otherPlayer.GetUseAppearData())
	
	def OnBuyAppear(self, data):
		playerId, appearKey = data["playerId"], data["appearKey"]
		suc, code = self.TryBuyAppear(playerId, appearKey)
		eventData = {
			"suc": suc,
			"code": code,
			"message": appearConst.FMT[code],
		}
		self.NotifyToClient(playerId, ServerEvent.BuyAppearRet, eventData)
		if not suc:
			self.SendActionResponse(playerId, eventData["message"])
	
	def TryBuyAppear(self, playerId, appearKey):
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return False, appearConst.CodePlayerAlreadyLeave
		if not appearKey:
			return False, appearConst.CodeBuyNotExistAppear
		appearConfig = appearConst.PropAppears.get(appearKey, None)
		if not appearConfig:
			return False, appearConst.CodeBuyNotExistAppear
		if player.AppearUnlocked(appearKey):
			return False, appearConst.CodeBuyUnlocked
		tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
		if not tradeSystem:
			return False, appearConst.CodeBuyWithoutTrade
		moneyType, moneyValue = appearConfig["cost"]["type"], appearConfig["cost"]["num"]
		if not player.CheckMoneyEnough(moneyType, moneyValue):
			return False, appearConst.CodeBuyLackMoney
		data = {
			moneyType: -moneyValue,
		}
		tradeSystem.UpdatePlayerDoughs(player.mUid, data)
		player.OnBuyAppearSuccess(appearKey)
		eventData = {
			"appearInfo": player.mAppearInfo,
		}
		self.NotifyToClient(player.mPlayerId, ServerEvent.SyncAppearInfo, eventData)
		return True, appearConst.CodeSuc

	def OnChangeUseAppear(self, data):
		playerId, appearType, appearKey = data["playerId"], data["appearType"], data["appearKey"]
		suc, code = self.TryChangeUseAppear(playerId, appearType, appearKey)
		eventData = {
			"suc": suc,
			"code": code,
			"message": appearConst.FMT[code],
		}
		self.NotifyToClient(playerId, ServerEvent.ChangeUseAppearRet, eventData)
		if not suc:
			self.SendActionResponse(playerId, eventData["message"])

	def TryChangeUseAppear(self, playerId, appearType, appearKey):
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return False, appearConst.CodePlayerAlreadyLeave
		if appearKey:
			appearConfig = appearConst.PropAppears.get(appearKey, None)
			if not appearConfig:
				return False, appearConst.CodeAppearNotExist
			if appearType != appearConfig.get("type", "empty"):
				return False, appearConst.CodeAppearWithWrongType
			if not player.AppearUnlocked(appearKey):
				return False, appearConst.CodeAppearNotUnloked
		if player.AppearAlreadyUsed(appearType, appearKey):
			return False, appearConst.CodeAlreadyUse
		if appearType == appearConst.AppearType.Mount:	# 坐骑类的处理比较特殊
			oldMount = player.GetUseMount()
			player.DoChangeUseAppear(appearType, appearKey)
			# 假如有使用坐骑，并且当前没有召唤坐骑，那么直接召唤一匹
			mount = player.GetUseMount()
			if oldMount: # 切换外观前使用了坐骑
				if not mount:	# 切换外观后，没有使用坐骑，那么触发停止骑乘逻辑
					self.DoStopRide(playerId)
				else:	# 否则仅仅是修改坐骑外观
					self.BroadcastToAllClient(ServerEvent.UpdateUseAppear, player.GetUseAppearData())
			else:	# 切换外观前没有坐骑
				if mount:	# 切换外观后有了坐骑，那么触发开始骑乘逻辑
					mountId = self.DoStartRide(playerId)
					if not mountId:
						player.SetUseMount(None)
						return False, appearConst.CodeCreateHorseFail
					else:
						self.OnStartRidingSuccess(playerId, mountId)
		else:
			player.DoChangeUseAppear(appearType, appearKey)
			self.BroadcastToAllClient(ServerEvent.UpdateUseAppear, player.GetUseAppearData())
		return True, appearConst.CodeSuc
	#------------------------------------------------------------------------------------------------------------------------------------
	def DoStartRide(self, playerId):
		# print "DoStartRide", playerId
		rideComp = serverApi.CreateComponent(playerId, "Minecraft", "ride")
		if rideComp.IsEntityRiding():
			return None
		posComp = serverApi.CreateComponent(playerId, "Minecraft", "pos")
		pos = posComp.GetPos()
		dimComp = serverApi.CreateComponent(playerId, "Minecraft", "dimension")
		dim = dimComp.GetEntityDimensionId()
		horseId = self.CreateEngineEntityByTypeStr("minecraft:horse", pos, (0, 0), dim)
		# print "DoStartRide summon horse", playerId, horseId
		if not horseId:
			return None
		suc = rideComp.SetEntityRide(playerId, horseId)
		if not suc:
			self.SetEntityToRemove(horseId)
			return None
		suc = rideComp.SetControl(horseId, True)
		if not suc:
			self.SetEntityToRemove(horseId)
			return None
		suc = rideComp.SetPlayerRideEntity(playerId, horseId)
		if not suc:
			self.SetEntityToRemove(horseId)
			return None
		return horseId
	
	def OnStartRidingSuccess(self, playerId, mountId):
		print "OnStartRidingSuccess", playerId, mountId
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		player.SaveMountId(mountId)
		self.DoBroadcastUseAppear(player)
	
	def DoStopRide(self, playerId):
		print "DoStopRide", playerId
		rideComp = serverApi.CreateComponent(playerId, "Minecraft", "ride")
		if rideComp.IsEntityRiding():
			rideComp.StopEntityRiding()
		self.OnRealStopRiding(playerId)
		
	def OnEntityStopRiding(self, args):
		playerId = args["id"]
		print "OnEntityStopRiding", playerId
		self.OnRealStopRiding(playerId)
	
	def OnRealStopRiding(self, playerId):
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		if not player.mMountId:
			return
		self.SetEntityToRemove(player.mMountId)
		player.StopRideing()
		self.DoBroadcastUseAppear(player)
	#------------------------------------------------------------------------------------------------------------------------------------
	def DoBroadcastUseAppear(self, player):
		self.BroadcastToAllClient(ServerEvent.UpdateUseAppear, player.GetUseAppearData())
		
		




