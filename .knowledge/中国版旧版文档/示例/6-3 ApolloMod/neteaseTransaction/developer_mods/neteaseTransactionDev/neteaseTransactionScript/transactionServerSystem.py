# -*- coding: utf-8 -*-

import apolloCommon.commonNetgameApi as commonNetgameApi
import lobbyGame.netgameApi as netgameApi
import apolloCommon.mysqlPool as mysqlPool
import logout
import server.extraServerApi as serverApi
import time
import neteaseTransactionScript.transactionServerConsts as transactionConsts

ServerSystem = serverApi.GetServerSystemCls()
minecraftEnum = serverApi.GetMinecraftEnum()

# player data 用于存储交易信息
# {
# 	playerUid: {
# 		"lastUpdate": "20201111", # 上次更新交易次数的日期
# 		"remainTimes": 3, # 剩余交易次数
# 		"isTrading": False, # 是否正在交易
# 		"tradePartner": partnerUid, # 交易对象的playerUid
# 		"isLocked": False, # 是否锁定交易
# 		"isConfirmed": False, # 是否确定交易
# 		"currencyNum": 2000, # 持有的货币数量
# 		"tradeInfo": { # 交易面板锁定的内容
# 			"item": {
# 				"itemName": "minecraft:wool",
# 				"auxValue": 2,
# 			},
# 			"itemSlot": 0,
# 			"itemNum": 1,
# 			"currencyNum": 50
# 		}
# 	}
# }

class TransactionServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		self.ListenEvents()
		self.mPlayerData = {}
		self.Init()

	def Init(self):
		config = commonNetgameApi.GetModJsonConfig('neteaseTransactionScript')
		self.mDefaultTransactionTimes = int(config.get("TRANSACTION_TIMES_PER_DAY", 3))
		self.mCurrency = config.get("CURRENCY", "MCB")
		self.mCurrencyTexture = config.get("CURRENCY_TEXTURE", "textures/ui/netease_transaction/currency2")
		self.InitMysqlPool()

	def Destroy(self):
		self.UnListenEvents()
		mysqlPool.Finish()

	def ListenEvents(self):
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnClientEnterEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
							self, self.OnClientLeaveEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent",
							self, self.OnPlayerDieEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DimensionChangeServerEvent",
							self, self.OnClientCloseTransactionEvent)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.RequestTransactionClientEvent,
							self, self.OnClientRequestTransactionEvent)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.ConfirmRequestEvent,
							self, self.OnClientConfirmRequest)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.LockTransactionEvent,
							self, self.OnClientLockTransactionEvent)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.ConfirmTransactionEvent,
							self, self.OnClientConfirmTransactionEvent)
		self.ListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.CloseTransactionEvent,
							self, self.OnClientCloseTransactionEvent)
		self.ListenForEvent("neteaseTrade", "neteaseTradeDev", 'PlayerDoughsUpdateEvent',
		                    self, self.OnSomeoneUpdateDoughs)

	def UnListenEvents(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
							self, self.OnClientEnterEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
							self, self.OnClientLeaveEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "PlayerDieEvent",
							self, self.OnPlayerDieEvent)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DimensionChangeServerEvent",
							self, self.OnClientCloseTransactionEvent)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.RequestTransactionClientEvent,
							self, self.OnClientRequestTransactionEvent)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.ConfirmRequestEvent,
							self, self.OnClientConfirmRequest)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.LockTransactionEvent,
							self, self.OnClientLockTransactionEvent)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.ConfirmTransactionEvent,
							self, self.OnClientConfirmTransactionEvent)
		self.UnListenForEvent(transactionConsts.ModName, transactionConsts.ClientSystemName, transactionConsts.CloseTransactionEvent,
							self, self.OnClientCloseTransactionEvent)
	# ------------------------------------------------------------------------------------------
	# 事件相关处理
	def OnClientEnterEvent(self, args):
		logout.info("OnClientEnter ", str(args))
		playerUid = args.get("uid", -1)
		if playerUid == -1:
			logout.warning("Client Enter Warning [-1]")
			return
		if playerUid in self.mPlayerData:
			logout.warning("playerUid already in server!!!")
		logout.info("player [{0}] enter game.".format(playerUid))
		sql = "SELECT lastUpdate, remainTimes FROM {} ".format(transactionConsts.TableUserTransactionInfo)
		sql += "WHERE uid = %s"
		params = (playerUid, )
		callback = lambda records:self.QueryPlayerInfoCallBack(records, playerUid)
		mysqlPool.AsyncQueryWithOrderKey('playerLogin', sql, params, callback)

	def OnClientLeaveEvent(self, args):
		logout.info("OnClientLeave ", str(args))
		playerUid = args.get("uid", -1)
		if playerUid == -1:
			logout.warning("Client leave Warning [-1]")
			return
		args["playerId"] = args.get("id", -1)
		self.OnClientCloseTransactionEvent(args)
		if playerUid in self.mPlayerData:
			lastUpdate = self.mPlayerData[playerUid]["lastUpdate"]
			remainTimes = self.mPlayerData[playerUid]["remainTimes"]
			sql = "INSERT INTO {} (uid, lastUpdate, remainTimes)".format(transactionConsts.TableUserTransactionInfo)
			sql += "VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE lastUpdate=%s, remainTimes=%s"
			params = (playerUid, lastUpdate, remainTimes, lastUpdate, remainTimes)
			mysqlPool.AsyncExecuteWithOrderKey('playerLogout', sql, params, None)
			del self.mPlayerData[playerUid]
		else:
			logout.warning("Client leave Warning!!!PlayerData not exist this player")

	def OnPlayerDieEvent(self, args):
		args["playerId"] = args["id"]
		self.OnClientCloseTransactionEvent(args)

	def OnClientRequestTransactionEvent(self, args):
		# 玩家发起交易时触发该事件，判断是否满足交易条件并分别通知交易双方
		playerId = args.get("playerId")
		playerUid = args.get("playerUid")
		partnerId = args.get("partnerId")
		partnerUid = args.get("partnerUid")

		if not partnerUid:
			if not partnerId:
				logout.warning("Request Transaction Warning!!!No Partner!!!")
				return
			else:
				partnerUid = netgameApi.GetPlayerUid(partnerId)

		if not partnerId:
			partnerId = netgameApi.GetPlayerIdByUid(partnerUid)

		if partnerUid not in self.mPlayerData:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "交易双方不在相同服务器，无法交易" })
			return

		if not playerUid:
			if not playerId:
				logout.warning("Request Transaction Warning!!!No Player!!!")
				return
			else:
				playerUid = netgameApi.GetPlayerUid(playerId)

		if playerUid == partnerUid:
			logout.warning("Can't Transact with yourself!!!")
			return

		self.CheckRemainTimes(playerUid, partnerUid)
		playerData = self.mPlayerData[playerUid]
		playerRemainTimes = playerData["remainTimes"]
		if playerRemainTimes == 0:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "你的今日交易次数已用光，无法交易" })
			return
		partnerData = self.mPlayerData[partnerUid]
		if partnerData["isTrading"]:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "对方正在交易中" })
			return
		if playerData["isTrading"]:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "不能同时发起两个交易" })
			return
		partnerRemainTimes = partnerData["remainTimes"]
		if partnerRemainTimes == 0:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "对方的今日交易次数已用光，无法交易" })
			return

		playerItemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		partnerItemComp = self.CreateComponent(partnerId, 'Minecraft', 'item')
		playerBag = playerItemComp.GetPlayerAllItems(minecraftEnum.ItemPosType.INVENTORY)
		if None not in playerBag:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "你的背包空间不够，无法交易" })
			return
		partnerBag = partnerItemComp.GetPlayerAllItems(minecraftEnum.ItemPosType.INVENTORY)
		if None not in partnerBag:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "对方的背包空间不够，无法交易" })
			return

		self.mPlayerData[playerUid]["isTrading"] = True
		self.mPlayerData[partnerUid]["isTrading"] = True
		self.mPlayerData[playerUid]["tradePartner"] = partnerUid
		self.mPlayerData[partnerUid]["tradePartner"] = playerUid
		self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "面对面交易申请发送成功" })
		playerNickName = netgameApi.GetPlayerNickname(playerId)
		eventData = {
			"nickName": playerNickName,
			"fromPlayerId": playerId,
			"toPlayerId": partnerId
		}
		self.NotifyToClient(partnerId, transactionConsts.RequestTransactionServerEvent, eventData)

	def OnClientConfirmRequest(self, args):
		# 玩家点击同意交易或拒绝交易后触发该事件
		playerId = args.get("fromPlayerId")
		partnerId = args.get("toPlayerId")
		if not partnerId or not partnerId:
			logout.warning("Confirm Request failed! wrong playerId or partnerId")
			return
		playerUid = netgameApi.GetPlayerUid(playerId)
		partnerUid = netgameApi.GetPlayerUid(partnerId)
		isConfirmed = args.get("isConfirmed")
		playerNickName = netgameApi.GetPlayerNickname(playerId)
		partnerNickName = netgameApi.GetPlayerNickname(partnerId)
		if not isConfirmed:
			# 玩家拒绝交易
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "{}拒绝与你面对面交易".format(partnerNickName) })
			self.mPlayerData[playerUid]["isTrading"] = False
			self.mPlayerData[partnerUid]["isTrading"] = False
			return
		itemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
		playerEventData = self.CreateEventData()
		playerEventData["currency"] = self.mPlayerData[playerUid]["currencyNum"]
		playerEventData["currencyIcon"] = self.mCurrencyTexture
		playerEventData["remainTimes"] = self.mPlayerData[playerUid]["remainTimes"]
		playerEventData["bagInfo"] = itemComp.GetPlayerAllItems(minecraftEnum.ItemPosType.INVENTORY, True)
		playerEventData["partnerName"] = partnerNickName
		playerEventData["playerName"] = playerNickName
		canTransaction = False
		for i in xrange(36):
			if playerEventData["bagInfo"][i] == None:
				canTransaction = True
				break
		if not canTransaction:
			self.NotifyToClient(partnerId, transactionConsts.ShowTipsEvent, { "tips": "对方的背包空间不够，无法交易" })
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "你的背包空间不够，无法交易" })
			self.mPlayerData[playerUid]["isTrading"] = False
			self.mPlayerData[partnerUid]["isTrading"] = False
			return
		itemComp = self.CreateComponent(partnerId, 'Minecraft', 'item')
		partnerEventData = self.CreateEventData()
		partnerEventData["currency"] = self.mPlayerData[partnerUid]["currencyNum"]
		partnerEventData["currencyIcon"] = self.mCurrencyTexture
		partnerEventData["remainTimes"] = self.mPlayerData[partnerUid]["remainTimes"]
		partnerEventData["bagInfo"] = itemComp.GetPlayerAllItems(minecraftEnum.ItemPosType.INVENTORY, True)
		partnerEventData["playerName"] = partnerNickName
		partnerEventData["partnerName"] = playerNickName
		canTransaction = False
		for i in xrange(36):
			if partnerEventData["bagInfo"][i] == None:
				canTransaction = True
				break
		if not canTransaction:
			self.NotifyToClient(playerId, transactionConsts.ShowTipsEvent, { "tips": "对方的背包空间不够，无法交易" })
			self.NotifyToClient(partnerId, transactionConsts.ShowTipsEvent, { "tips": "你的背包空间不够，无法交易" })
			self.mPlayerData[playerUid]["isTrading"] = False
			self.mPlayerData[partnerUid]["isTrading"] = False
			return
		self.NotifyToClient(playerId, transactionConsts.InitiateTransactionEvent, playerEventData)
		self.NotifyToClient(partnerId, transactionConsts.InitiateTransactionEvent, partnerEventData)

	def OnClientLockTransactionEvent(self, args):
		# 客户端点击锁定后更新playerData，并通知partner更新锁定UI
		logout.info("OnClientLockTransactionEvent ", str(args))
		playerId = args.get("playerId", "-1")
		tradeInfo = args.get("tradeInfo", {})
		isLocked = args.get("isLocked", False)
		if playerId == "-1":
			logout.warning("Client LockTransaction Warning [-1]")
			return
		playerUid = netgameApi.GetPlayerUid(playerId)
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			playerData["isLocked"] = isLocked
			if not isLocked:
				playerData["isConfirmed"] = False
				partnerUid = playerData["tradePartner"]
				self.mPlayerData[partnerUid]["isConfirmed"] = False
				self.mPlayerData[partnerUid]["isLocked"] = False
			playerData["tradeInfo"] = tradeInfo
			partnerUid = playerData["tradePartner"]
			partnerId = netgameApi.GetPlayerIdByUid(partnerUid)
			self.NotifyToClient(partnerId, transactionConsts.PartnerLockEvent, args)
		else:
			logout.warning("Client Lock Warning!!!PlayerData not exist this player")

	def OnClientConfirmTransactionEvent(self, args):
		# 客户端点击确定交易后更新playerData，并通知partner更新确认UI
		# 如果partner已确认直接更新双方背包并通知交易成功
		logout.info("OnClientConfirmTransactionEvent ", str(args))
		playerId = args.get("playerId", "-1")
		if playerId == "-1":
			logout.warning("Client ConfirmTransaction Warning [-1]")
			return
		playerUid = netgameApi.GetPlayerUid(playerId)
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			playerData["isConfirmed"] = True
			partnerUid = playerData["tradePartner"]
			partnerId = netgameApi.GetPlayerIdByUid(partnerUid)
			partnerData = self.mPlayerData[partnerUid]
			if partnerData["isConfirmed"]:
				# 如果对方已经确认，直接交换双方物品及货币，并通知双方交易成功
				# 先更新双方背包的物品
				playerItemComp = self.CreateComponent(playerId, 'Minecraft', 'item')
				partnerItemComp = self.CreateComponent(partnerId, 'Minecraft', 'item')
				playerItem = playerData["tradeInfo"].get("item")
				if playerItem:
					slot = playerData["tradeInfo"].get("itemSlot", 0)
					itemNum = playerData["tradeInfo"].get("itemNum", 0)
					itemCnt = playerItem.get("count", 0)
					playerItemComp.SetInvItemNum(slot, itemCnt - itemNum)
					playerItem["count"] = itemNum
					partnerItemComp.SpawnItemToPlayerInv(playerItem, partnerId)
				partnerItem = partnerData["tradeInfo"].get("item")
				if partnerItem:
					slot = partnerData["tradeInfo"].get("itemSlot", 0)
					itemNum = partnerData["tradeInfo"].get("itemNum", 0)
					itemCnt = partnerItem.get("count", 0)
					partnerItemComp.SetInvItemNum(slot, itemCnt - itemNum)
					partnerItem["count"] = itemNum
					playerItemComp.SpawnItemToPlayerInv(partnerItem, playerId)
				playerTradeCurrency = playerData["tradeInfo"].get("currencyNum", 0)
				partnerTradeCurrency = partnerData["tradeInfo"].get("currencyNum", 0)
				playerData["currencyNum"] += partnerTradeCurrency - playerTradeCurrency
				partnerData["currencyNum"] += playerTradeCurrency - partnerTradeCurrency
				#这里接入了经济插件，由经济插件进行货币管理，这里负责更新货币
				tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
				if tradeSystem:
					tradeSystem.UpdatePlayerDoughs(playerUid, { self.mCurrency: partnerTradeCurrency - playerTradeCurrency })
					tradeSystem.UpdatePlayerDoughs(partnerUid, { self.mCurrency: playerTradeCurrency - partnerTradeCurrency })
				# 交易成功先减少当日交易次数，并修改交易状态
				playerData["remainTimes"] -= 1
				partnerData["remainTimes"] -= 1
				playerData["isTrading"] = False
				partnerData["isTrading"] = False
				playerData["isConfirmed"] = False
				partnerData["isConfirmed"] = False
				# 通知双方交易成功
				self.NotifyToClient(partnerId, transactionConsts.TransactionCompleteEvent, None)
				self.NotifyToClient(playerId, transactionConsts.TransactionCompleteEvent, None)
				logout.info("transaction completed")
			else:
				self.NotifyToClient(partnerId, transactionConsts.PartnerConfirmEvent, args)
		else:
			logout.warning("Client Confirmed Warning!!!PlayerData not exist this player")

	def OnClientCloseTransactionEvent(self, args):
		# 如果客户端点击关闭按钮需要同时关闭交易双方的界面
		logout.info("OnClientCloseTransactionEvent ", str(args))
		playerUid = args.get("uid", -1)
		playerId = args.get("playerId", "-1")
		if playerId == "-1":
			logout.warning("Client CloseTransaction Warning [-1]")
			return
		if playerUid == -1:
			playerUid = netgameApi.GetPlayerUid(playerId)
		if playerUid in self.mPlayerData:
			playerData = self.mPlayerData[playerUid]
			if playerData["isTrading"]:
				partnerUid = playerData["tradePartner"]
				partnerId = netgameApi.GetPlayerIdByUid(partnerUid)
				self.mPlayerData[playerUid]["isTrading"] = False
				self.mPlayerData[partnerUid]["isTrading"] = False
				self.mPlayerData[playerUid]["isConfirmed"] = False
				self.mPlayerData[partnerUid]["isConfirmed"] = False
				self.NotifyToClient(partnerId, transactionConsts.CancelTransactionEvent, { "tips": "对方已取消交易" })
				self.NotifyToClient(playerId, transactionConsts.CancelTransactionEvent, { "tips": "你已取消交易" })

	# ------------------------------------------------------------------------------------------
	def QueryPlayerInfoCallBack(self, records, uid):
		logout.info("QueryPlayerInfoCallBack: ", uid)
		today = time.strftime("%Y%m%d")
		if records is None or len(records) < 1:
			lastUpdate = today
			remainTimes = self.mDefaultTransactionTimes
		else:
			lastUpdate = records[0][0]
			remainTimes = records[0][1]
		if lastUpdate != today:
			lastUpdate = today
			remainTimes = self.mDefaultTransactionTimes
		# 这里接入了经济插件，并从中获取货币数量
		tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
		if tradeSystem:
			tradeSystem.QueryPlayerDoughs(uid, lambda suc, data: self.QueryCurrencyCallBack(uid, 0, suc, data))
		remainCurrency = 0
		playerData = {
			"lastUpdate": "20201111", # 上次更新交易次数的日期
			"remainTimes": remainTimes,
			"isTrading": False,
			"tradePartner": None,
			"isLocked": False,
			"isConfirmed": False,
			"currencyNum": remainCurrency,
			"tradeInfo": {
				"item": None,
				"itemSlot": 0,
				"itemNum": 0,
				"currencyNum": 0
			}
		}
		self.mPlayerData[uid] = playerData

	def CheckRemainTimes(self, playerUid, partnerUid):
		today = time.strftime("%Y%m%d")
		if self.mPlayerData[playerUid]["lastUpdate"] != today:
			self.mPlayerData[playerUid]["lastUpdate"] = today
			self.mPlayerData[playerUid]["remainTimes"] = self.mDefaultTransactionTimes
		if self.mPlayerData[partnerUid]["lastUpdate"] != today:
			self.mPlayerData[partnerUid]["lastUpdate"] = today
			self.mPlayerData[partnerUid]["remainTimes"] = self.mDefaultTransactionTimes

	def QueryCurrencyCallBack(self, uid, retryCnt, success, data):
		'''
		注意：依赖经济插件，登陆后可能不能及时获取currency，若获取失败需要重试，重试20次
		'''
		if (not success or data['code'] != 1) and retryCnt >= 20:
			logout.error('QueryCurrencyCallBack fail.exceed retry count. uid: {}'.format(uid))
			return
		delay = 1 if retryCnt == 1 else 2
		retryCnt += 1
		def _QueryTimer(uid):
			tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
			tradeSystem.QueryPlayerDoughs(uid, lambda suc, data: self.QueryCurrencyCallBack(uid, retryCnt, suc, data))
		if not success:
			commonNetgameApi.AddTimer(delay, _QueryTimer, uid)
			logout.warning('QueryCurrencyCallBack timeout. data: {}'.format(data))
		else:
			if data['code'] == 1: #请求成功
				remainCurrency = data['entity'][self.mCurrency]
				self.mPlayerData[uid]['currencyNum'] = remainCurrency
			else:
				commonNetgameApi.AddTimer(delay, _QueryTimer, uid)
				logout.warning('QueryCurrencyCallBack fail. data: {}'.format(data))

	def OnSomeoneUpdateDoughs(self, args):
		uid = args['uid']
		if uid not in self.mPlayerData:
			return
		tradeSystem = serverApi.GetSystem("neteaseTrade", "neteaseTradeDev")
		if tradeSystem:
			tradeSystem.QueryPlayerDoughs(uid, lambda suc, data: self.QueryCurrencyCallBack(uid, 0, suc, data))

	#-------------------------------------------  API  ----------------------------------------------
	def RequestTransaction(self, fromPlayerId, toPlayerId):
		"""
		发起交易，fromPlayerId为发起玩家的id，toPlayerId为目标玩家的id
		params: fromPlayerId str 发起交易玩家的id
		params: toPlayerId str 交易目标玩家的id
		"""
		args = {
			"playerId": fromPlayerId,
			"partnerId": toPlayerId
		}
		self.OnClientRequestTransactionEvent(args)

	def QueryPlayerRemainTransactionTimes(self, playerUid):
		"""
		查询玩家今日剩余交易次数
		params: fromPlayerId str 发起交易玩家的id
		return: int 返回今日剩余交易次数，如果为负数表示无限制，如果玩家不存在返回None
		"""
		if playerUid in self.mPlayerData:
			today = time.strftime("%Y%m%d")
			if self.mPlayerData[playerUid]["lastUpdate"] != today:
				self.mPlayerData[playerUid]["lastUpdate"] = today
				self.mPlayerData[playerUid]["remainTimes"] = self.mDefaultTransactionTimes
			return self.mPlayerData[playerUid]["remainTimes"]
		else:
			return None
	#------------------------------------------------------------------------------------------------
	# 初始化mysql连接池
	def InitMysqlPool(self):
		# 尝试初始化mysql连接池，失败则打印ERROR日志并返回False
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_transaction_server fail when init mysql")
			return False
		return True
