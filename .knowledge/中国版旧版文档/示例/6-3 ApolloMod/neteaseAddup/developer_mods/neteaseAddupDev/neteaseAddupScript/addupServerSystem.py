# -*- coding: utf-8 -*-
import time

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from mod_log import engine_logger as logger
import apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as lobbyGameApi

from neteaseAddupScript.addupConsts import ModName, ClientSystemName, ClientEvent, ServerEvent, MasterSystemName, MasterEvent
import neteaseAddupScript.addupConsts as addupConsts
import neteaseAddupScript.dbApi as dbApi
import neteaseAddupScript.addupServerPlayer as addupServerPlayer

def CleanDict(_dict, exKey):
	if exKey in _dict:
		del _dict[exKey]
	for v in _dict.values():
		if type(v) == dict:
			CleanDict(v, exKey)

class AddupServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# 初始化数据库
		dbApi.Init()
		# 加载配置信息
		self.InitConfig()
		# 
		self.mFrame = 0
		self.mPlayerData = {}
		self.mUid2PlayerId = {}
		# 时间偏移，方便测试
		self.mOffsetTimestamp = 0
		self.mPassedAddupKeys = []
		self.mActiveAddupKey = None
		self.CheckActiveActivity()
		
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StoreBuySuccServerEvent", self, self.OnStoreBuySuc)
		self.ListenForEvent("neteaseShop", "neteaseShopDev", "ServerShipItemsEvent", self, self.OnQueryOrdersResult)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.ClientEnter, self, self.OnClientReady)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.GetAddupBonus, self, self.OnGetAddupBonus)
		self.ListenForEvent(ModName, ClientSystemName, ClientEvent.OpenNeteaseShop, self, self.OnOpenNeteaseShop)
		self.ListenForEvent(ModName, MasterSystemName, MasterEvent.GetAddupCharge, self, self.OnGetAddupCharge)
		self.ListenForEvent(ModName, MasterSystemName, MasterEvent.SetAddupCharge, self, self.OnSetAddupCharge)
		self.ListenForEvent(ModName, MasterSystemName, MasterEvent.SetAddupBonusState, self, self.OnSetAddupBonusState)
		

	def Destroy(self):
		dbApi.Destroy()
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent", self, self.OnServerChat)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent", self, self.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StoreBuySuccServerEvent", self, self.OnStoreBuySuc)
		self.UnListenForEvent("neteaseShop", "neteaseShopDev", "ServerShipItemsEvent", self, self.OnQueryOrdersResult)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.ClientEnter, self, self.OnClientReady)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.GetAddupBonus, self, self.OnGetAddupBonus)
		self.UnListenForEvent(ModName, ClientSystemName, ClientEvent.OpenNeteaseShop, self, self.OnOpenNeteaseShop)
		self.UnListenForEvent(ModName, MasterSystemName, MasterEvent.GetAddupCharge, self, self.OnGetAddupCharge)
		self.UnListenForEvent(ModName, MasterSystemName, MasterEvent.SetAddupCharge, self, self.OnSetAddupCharge)
		self.UnListenForEvent(ModName, MasterSystemName, MasterEvent.SetAddupBonusState, self, self.OnSetAddupBonusState)

	def InitConfig(self):
		cfg = commonNetgameApi.GetModJsonConfig("neteaseAddupScript")
		if not cfg:
			return False
		exKey = "_comment"
		addupConsts.AllActivityData = dbApi.UnicodeConvert(cfg["activityData"])
		CleanDict(addupConsts.AllActivityData, exKey)
		addupConsts.ActivityExpireTime = cfg["activityExpireTime"]
		#
		addupConsts.Item2ProcessMap = {}
		for data in dbApi.UnicodeConvert(cfg["itemPriceData"]):
			item_id = data["item_id"]
			plusProcess = data["plusProcess"]
			addupConsts.Item2ProcessMap[item_id] = plusProcess
		return True

	def Update(self):
		self.mFrame += 1
		if self.mFrame % 30 == 0:
			for player in self.mPlayerData.itervalues():
				if not player.IsDirty():
					continue
				self.DoSavePlayer(player, isLeave=False)
		if self.mFrame % 60 == 0:
			changed = self.CheckActiveActivity()
			if changed:
				self.SendActiveAddup()

	def GetPlayerByUid(self, uid):
		playerId = self.mUid2PlayerId.get(uid, None)
		if not playerId:
			return None
		return self.mPlayerData.get(playerId, None)

	def GetNow(self):
		return int(time.time()) + self.mOffsetTimestamp
	
	def GetActiveAddup(self):
		if not self.mActiveAddupKey:
			return None
		return addupConsts.AllActivityData.get(self.mActiveAddupKey, None)
	
	def CheckActiveActivity(self):
		oldActiveAddupKey = self.mActiveAddupKey
		self.mPassedAddupKeys = []
		self.mActiveAddupKey = None
		#
		now = self.GetNow()
		for actKey, config in addupConsts.AllActivityData.iteritems():
			if now < config["startTp"]:
				continue
			if now >= config["endTp"]:
				self.mPassedAddupKeys.append(actKey)
				continue
			if not self.mActiveAddupKey is None:
				logger.error("two or more addup in one time; one is {}, other is {}".format(self.mActiveAddupKey, actKey))
				continue
			self.mActiveAddupKey = actKey
		if oldActiveAddupKey == self.mActiveAddupKey:
			return False
		else:
			return True
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnServerChat(self, args):
		playerId = args["playerId"]
		messages = args['message'].split()
		command = messages[0]
		params = messages[1:]
		# 以下是调试用的测试代码
		"""
		if command == "additem":
			identifier = params[0]
			auxValue = int(params[1])
			count = int(params[2])
			self.DoAddItem(playerId, identifier, auxValue, count)
		elif command == "time":
			year, month, day, hour = int(params[0]), int(params[1]), int(params[2]), int(params[3])
			timestamp = int(time.mktime([year, month, day, hour, 0, 0, 0, 0, 0]))
			self.mOffsetTimestamp = timestamp - int(time.time())
			print "now is {}".format(time.strftime("%Y-%m-%d %H:%m:%S", time.localtime(self.GetNow())))
		elif command == "openui":
			self.OpenBonusUI(playerId)
		elif command == "pay":
			import random
			data = {
				"uid": 2147585444,
				"entities": [],
			}
			for i in xrange(5):
				one = {
					"item_id": random.choice([90027446413343740, 90027446413343741]),
					"item_num": random.choice([1,2,3]),
					"orderid": random.choice(["1", "2", "3"]),
					"cmd": "test",
					"buy_time": self.GetNow(),
					"group" : 1
        		}
				data["entities"].append(one)
			self.OnQueryOrdersResult(data)
		elif command == "getaddup":
			resulit = self.GetAddupPayDiamonds(2147585444, self.mActiveAddupKey)
			print "GetAddupPayDiamonds", resulit
		"""

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
	
	def GetEmptySlotList(self, playerId):
		slotList = []
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for slot in xrange(36):
			item = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot)
			if not item:
				slotList.append(slot)
		return slotList
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnStoreBuySuc(self, args):
		playerId = args["playerId"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		self.StartQueryPlayerOrders(player.mUid, False)
	
	def OnAddServerPlayer(self, args):
		# print "OnAddServerPlayer", args
		playerId = args["id"]
		uid = args["uid"]
		player = addupServerPlayer.Player(playerId, uid)
		self.mPlayerData[playerId] = player
		self.mUid2PlayerId[uid] = playerId
		dbApi.QueryPlayerData(uid, lambda addupInfo:self.OnQueryPlayerCallback(playerId, addupInfo))
	
	def OnQueryPlayerCallback(self, playerId, addupInfo):
		# print "OnQueryPlayerCallback", playerId, addupInfo
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		# 没有加载到数据，认为是第一次登录
		if addupInfo is None:
			player.OnCreateByNew()
		else:
			player.OnQueryCallback(addupInfo)
		# 用邮件发送已经过期的活动的尚未领取的奖励
		self.CheckAndMailPassedBonus(player)
		# 每次登录完成后，查询一下订单状态
		self.StartQueryPlayerOrders(player.mUid, True)
		# 如果此时客户端已经登录完成，那么需要发送serverReady
		self.CheckAndSendReady(player)

	def CheckAndMailPassedBonus(self, player):
		mailSystem = serverApi.GetSystem("neteaseAnnounce", "neteaseAnnounceDev")
		if not mailSystem:
			return
		now = self.GetNow()
		for addupKey in self.mPassedAddupKeys:
			addupConfig = addupConsts.AllActivityData.get(addupKey, None)
			if not addupConfig:
				continue
			addupInfo = player.GetAddupInfoByKey(addupKey)
			if not addupInfo:
				continue
			# 已经超过限制时间了，不再检查是否需要补发奖励，并且清理掉存储信息
			if now - addupConfig["endTp"] >= addupConsts.ActivityExpireTime:
				player.CleanAddupInfoByKey(addupKey)
				continue
			process = addupInfo.get("process", 0)
			bonusList = addupInfo.get("bonusList", [])
			for bonusKey, bonusConfig in addupConfig.get("quests", {}).iteritems():
				if process < bonusConfig["process"]:
					continue
				if bonusKey in bonusList:
					continue
				rewardList = []
				for singleReward in bonusConfig.get("reward", []):
					rewardList.append(singleReward["item"])
				player.SetAlreadyGetBonus(addupInfo, bonusKey)
				title = "{}补发奖励".format(addupConfig["title"])
				content = "补发尚未领取的消费{}钻石的奖励".format(bonusConfig["process"])
				mailSystem.SendMailToUser([player.mUid,], title, content, rewardList)
			player.SaveAddupInfoByKey(addupKey, addupInfo)

	def OnDelServerPlayer(self, args):
		# print "OnDelServerPlayer", args
		playerId = args["id"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		del self.mPlayerData[playerId]
		if player.mUid in self.mUid2PlayerId:
			del self.mUid2PlayerId[player.mUid]
		# 如果query数据库都没有完成，就不需要存档了
		if not player.DataReady():
			return
		if player.IsDirty():
			self.DoSavePlayer(player, isLeave=True)
	
	def DoSavePlayer(self, player, isLeave=False):
		# print "DoSavePlayer", isLeave
		needInsert = player.NeedInsert()
		playerId, uid, addupInfo = player.GetSaveData()
		if needInsert:
			dbApi.InsertPlayerData(uid, addupInfo, lambda suc:self.OnSaveByInsertCallback(playerId, uid, addupInfo, isLeave, suc))
		else:
			dbApi.UpdatePlayerData(uid, addupInfo, lambda suc:self.OnSaveByUpdateCallback(playerId, uid, addupInfo, isLeave, suc))
		player.SetSaved()
	
	def OnSaveByInsertCallback(self, playerId, uid, addupInfo, isLeave, suc):
		if isLeave:
			if not suc:
				logger.error("OnSaveByInsertCallback fail uid={} info={}".format(uid, addupInfo))
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
	def OpenBonusUI(self, playerId):
		# print "OpenBonusUI", playerId
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		self.NotifyToClient(playerId, ServerEvent.OpenBonusUI, {})

	def GetAddupPayDiamonds(self, uid, addupKey):
		player = self.GetPlayerByUid(uid)
		if not player:
			return None
		addupConfig = addupConsts.AllActivityData.get(addupKey, None)
		if addupConfig is None:
			return None
		addupInfo = player.GetAddupInfoByKey(addupKey)
		paydiamonds = addupInfo.get("process", 0)
		return paydiamonds

	def StartQueryPlayerOrders(self, uid, isLogin):
		shopSystem = serverApi.GetSystem("neteaseShop", "neteaseShopDev")
		shopSystem.StartShipProcess(uid)
	
	def OnQueryOrdersResult(self, data):
		# print "OnQueryOrdersResult", data
		uid = data["uid"]
		orderList = data["entities"]
		if not orderList:
			return
		player = self.GetPlayerByUid(uid)
		if not player:
			return
		# 当前没有累积消费活动
		if not self.mActiveAddupKey:
			return
		changed = player.UpdateByOrders(self.mActiveAddupKey, self.GetActiveAddup(), orderList)
		if changed:
			self.SyncAddupInfo(player)
	#------------------------------------------------------------------------------------------------------------------------------------
	def OnGetAddupBonus(self, data):
		playerId, addupKey, bonuskey = data["playerId"], data["addupKey"], data["bonuskey"]
		player = self.mPlayerData.get(playerId, None)
		if not player:	# 已经离线的玩家的请求就不需要回应了
			return
		suc, reason = self.TryGetAddupBonus(playerId, player, addupKey, bonuskey)
		if not suc:
			self.SendActionResponse(playerId, reason)
		eventData = {
			"suc": suc,
			"reason": reason,
			"addupKey": self.mActiveAddupKey,
			"addupInfo": player.mAddupInfo,
		}
		self.NotifyToClient(playerId, ServerEvent.GetAddupBonusRet, eventData)
	
	def TryGetAddupBonus(self, playerId, player, addupKey, bonusKey):
		if addupKey != self.mActiveAddupKey:
			return False, "活动已经过期了，无法领取奖励"
		addupConfig = addupConsts.AllActivityData.get(addupKey, None)
		if not addupConfig:
			return False, "目标活动不存在，无法领取奖励"
		bonusConfig = addupConfig.get("quests", {}).get(bonusKey, None)
		if not bonusConfig:
			return False, "目标奖励不存在，无法领取奖励"
		addupInfo = player.GetAddupInfoByKey(addupKey)
		if player.IsAlreadyGetBonus(addupInfo, bonusKey):
			return False, "目标奖励已经领取过了，无法再次领取"
		if not player.IsReachProcess(addupInfo, bonusConfig["process"]):
			return False, "领取目标奖励的消费钻石数尚未达到，无法领取奖励"
		rewardList = bonusConfig.get("reward", [])
		freeSlotList = self.GetEmptySlotList(playerId)
		if len(freeSlotList) < len(rewardList):
			return False, "领取目标奖励需要背包中存在{}个空格，背包中剩余的空格不足".format(len(rewardList))
		#
		player.SetAlreadyGetBonus(addupInfo, bonusKey)
		player.SaveAddupInfoByKey(addupKey, addupInfo)
		comp = self.CreateComponent(playerId, 'Minecraft', 'item')
		for singleReward in rewardList:
			slot = self.GetEmptySlot(playerId)
			if slot is None:
				continue
			comp.SpawnItemToPlayerInv(singleReward["item"], playerId, slot)
		return True, ""
	
	def OnClientReady(self, data):
		# print "OnClientReady", data
		playerId = data["playerId"]
		player = self.mPlayerData.get(playerId, None)
		if not player:
			return
		player.SetClientReady()
		self.CheckAndSendReady(player)

	def OnOpenNeteaseShop(self, data):
		playerId = data["playerId"]
		lobbyGameApi.NotifyClientToOpenShopUi(playerId)
	#------------------------------------------------------------------------------------------------------------------------------------
	def CheckAndSendReady(self, player):
		if not player.mClientReady or not player.mDbLoaded:
			return
		eventData = {
			"uid": player.mUid,
			"addupKey": self.mActiveAddupKey,
			"AllActivityData": addupConsts.AllActivityData,
			"addupInfo": player.mAddupInfo,
		}
		self.NotifyToClient(player.mPlayerId, ServerEvent.ServerReady, eventData)
	
	def SyncAddupInfo(self, player):
		eventData = {
			"addupKey": self.mActiveAddupKey,
			"addupInfo": player.mAddupInfo,
		}
		self.NotifyToClient(player.mPlayerId, ServerEvent.SyncAddupInfo, eventData)
	
	def SendActiveAddup(self):
		eventData = {
			"addupKey": self.mActiveAddupKey,
			"passedKeys": self.mPassedAddupKeys,
		}
		self.BroadcastToAllClient(ServerEvent.UpdateActiveAddup, eventData)
	
	def SendActionResponse(self, playerId, message):
		message = '§a%s' % message
		alertSystem = serverApi.GetSystem("neteaseAlert", "neteaseAlertDev")
		if alertSystem:
			alertSystem.Alert(playerId, message, 2, 0.5, 0.8)
		else:
			comp = self.CreateComponent(playerId, 'Minecraft', 'command')
			comp.SetCommand('tellraw @s {"rawtext": [{"text": "%s"}]}' % message, playerId)
	# -----------------------------------------------------------------------------------------------------------------------------------
	def OnGetAddupCharge(self, data):
		# print "OnGetAddupCharge", data
		clientId, uid, addupKey = data["clientId"], data["uid"], data["addupKey"]
		player = self.GetPlayerByUid(uid)
		if not player:
			self.ResponseFailToMaster(clientId, "查询失败，目标uid的玩家已经离线了")
			return
		addupConfig = addupConsts.AllActivityData.get(addupKey, None)
		if addupConfig is None:
			self.ResponseFailToMaster(clientId, "查询失败，关键字【{}】对应的累积活动不存在".format(addupKey))
			return
		addupInfo = player.GetAddupInfoByKey(addupKey)
		payDiamonds = addupInfo.get("process", 0)
		alreadyGetBonusKeys = addupInfo.get("bonusList", [])
		data = {
			"uid": uid,
			"online": True,
			"payDiamonds": payDiamonds,
			"alreadyGetBonusKeys": alreadyGetBonusKeys,
		}
		self.ResponseToMaster(clientId, data)

	def OnSetAddupCharge(self, data):
		# print "OnSetAddupCharge", data
		clientId, uid, addupKey, payDiamonds = data["clientId"], data["uid"], data["addupKey"], data["payDiamonds"]
		player = self.GetPlayerByUid(uid)
		if not player:
			self.ResponseFailToMaster(clientId, "设置累积消费活动消费进度失败，目标uid的玩家已经离线了")
			return
		if addupKey is None:
			addupKey = self.mActiveAddupKey
		addupConfig = addupConsts.AllActivityData.get(addupKey, None)
		if addupConfig is None:
			self.ResponseFailToMaster(clientId, "设置累积消费活动消费进度失败，关键字【{}】对应的累积消费活动不存在".format(addupKey))
			return
		addupInfo = player.GetAddupInfoByKey(addupKey)
		player.ChangeAddupProcess(addupInfo, payDiamonds)
		player.SaveAddupInfoByKey(addupKey, addupInfo)
		#
		payDiamonds = addupInfo.get("process", 0)
		alreadyGetBonusKeys = addupInfo.get("bonusList", [])
		data = {
			"uid": uid,
			"payDiamonds": payDiamonds,
			"alreadyGetBonusKeys": alreadyGetBonusKeys,
		}
		self.ResponseToMaster(clientId, data)
		self.SyncAddupInfo(player)

	def OnSetAddupBonusState(self, data):
		# print "OnSetAddupBonusState", data
		clientId, uid, addupKey, bonusKey, alreadyGet = data["clientId"], data["uid"], data["addupKey"], data["bonusKey"], data["alreadyGet"]
		player = self.GetPlayerByUid(uid)
		if not player:
			self.ResponseFailToMaster(clientId, "设置玩家的奖励领取状态失败，目标uid的玩家已经离线了")
			return
		if addupKey is None:
			addupKey = self.mActiveAddupKey
		addupConfig = addupConsts.AllActivityData.get(addupKey, None)
		if addupConfig is None:
			self.ResponseFailToMaster(clientId, "设置玩家的奖励领取状态失败，关键字【{}】对应的累积消费活动不存在".format(addupKey))
			return
		if bonusKey not in addupConfig["quests"]:
			self.ResponseFailToMaster(clientId, "设置玩家的奖励领取状态失败，奖励关键字【{}】对应的消费阶段不存在".format(bonusKey))
			return
		addupInfo = player.GetAddupInfoByKey(addupKey)
		player.ChangeAddupBonusState(addupInfo, bonusKey, alreadyGet)
		player.SaveAddupInfoByKey(addupKey, addupInfo)
		#
		payDiamonds = addupInfo.get("process", 0)
		alreadyGetBonusKeys = addupInfo.get("bonusList", [])
		data = {
			"uid": uid,
			"payDiamonds": payDiamonds,
			"alreadyGetBonusKeys": alreadyGetBonusKeys,
		}
		self.ResponseToMaster(clientId, data)
		self.SyncAddupInfo(player)

	def ResponseToMaster(self, clientId, entity):
		eventData = {
			"clientId": clientId,
			"suc": True,
			"message": "",
			"entity": entity,
		}
		self.NotifyToMaster(ServerEvent.HttpResponse, eventData)
	
	def ResponseFailToMaster(self, clientId, message):
		eventData = {
			"clientId": clientId,
			"suc": False,
			"message": message,
			"entity": None,
		}
		self.NotifyToMaster(ServerEvent.HttpResponse, eventData)
		