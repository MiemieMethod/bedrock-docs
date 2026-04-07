# -*- coding: utf-8 -*-
import lobbyGame.netgameApi as netgameApi
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import time
import json
import logout
import shopConsts as shopConsts


SHIP_WAIT_STEP = (0, 1, 1, 1, 2, 2, 3, 3, 4)

class DbType(object):
	#使用的数据库种类
	Mongo = 1
	Mysql = 2

class ShopProccess(object):
	def __init__(self):
		super(ShopProccess, self).__init__()
		self.mAutoDetectOrder = False
		self.mPlayerToUid = {}
		self.mPlayerData = {}
		self.mNeedShipPlayers = set()
		self.mReplenishShipTimer = commonNetgameApi.AddRepeatedTimer(0.5, self.DoReplenishShip)
	
	def Destroy(self):
		if self.mReplenishShipTimer:
			commonNetgameApi.CancelTimer(self.mReplenishShipTimer)
			self.mShipPlayerTimer = None
	
	def DoReplenishShip(self):
		now = time.time()
		for uid in self.mNeedShipPlayers:
			data = self.mPlayerData.get(uid, None)
			if data is None:
				continue
			if data["shipStep"] >= len(SHIP_WAIT_STEP):
				continue
			timestamp = SHIP_WAIT_STEP[data["shipStep"]]
			if now - data["lastShipTime"] >= timestamp:
				logout.info("do ShipPlayer now={} shipStep={} lastShipTime={}".format(now, data["shipStep"], data["lastShipTime"]))
				data["shipStep"] += 1
				data["lastShipTime"] = now
				self.ShipPlayer(uid)
	
	def InitConfig(self, auto_detect):
		self.mAutoDetectOrder = auto_detect

	def OnClientLoadAddonsFinish(self, args):
		if not self.mAutoDetectOrder:
			return
		playerId = args["playerId"]
		uid = self.mPlayerToUid.get(playerId, None)
		if not uid:
			return
		self.OnCheckPlayerOrder(uid)

	def OnStoreBuySucc(self, args):
		if not self.mAutoDetectOrder:
			return
		playerId = args["playerId"]
		uid = self.mPlayerToUid.get(playerId, None)
		if not uid:
			return
		self.OnCheckPlayerOrder(uid)

	def GetInitPlayerData(self, playerId, uid):
		return {
			"playerId": playerId,
			"uid": uid,
			"finOrders": [],
			"shipStep": 0,
			"lastShipTime": 0,
		}
	
	def OnAddServerPlayer(self, args):
		'''
		玩家登陆，加入在线队列
		'''
		playerId = args.get('id', '-1')
		uid = netgameApi.GetPlayerUid(playerId)
		self.mPlayerToUid[playerId] = uid
		self.mPlayerData[uid] = self.GetInitPlayerData(playerId, uid)
	
	def OnDelServerPlayer(self, args):
		'''
		玩家离开，从在线队列移除
		'''
		playerId = args.get('id', '-1')
		uid = self.mPlayerToUid.get(playerId, None)
		if not uid is None:
			del self.mPlayerToUid[playerId]
		if uid in self.mPlayerData:
			del self.mPlayerData[uid]
		self.mNeedShipPlayers.discard(uid)
	
	def OnCheckPlayerOrder(self, uid):
		'''
		把玩家的uid插入轮询队列里
		'''
		# 玩家必须在线
		data = self.mPlayerData.get(uid, None)
		if not data:
			return False
		self.mNeedShipPlayers.add(uid)
		data["shipStep"] = 0
		return True

	def ShipPlayer(self, uid):
		'''
		查询订单，并发货
		'''
		shopServerSystem = shopConsts.GetServerModSystem()
		def getOrderListCb(code, responseStr, time):
			logout.info("getOrderListCb Post Response.code:{} response={} time={}".format(code, responseStr, time))
			# 离线了就不返回事件了
			playerData = self.mPlayerData.get(uid, None)
			if not playerData:
				return
			try:
				response = json.loads(responseStr)
			except:
				logout.error("ShipPlayer, cannot load json!")
				self.ShipItems(uid, None, -1, "404 error")
				return
			if 200 != code or 0 != response['code']:
				logout.error('Response error!')
				self.ShipItems(uid, None,response['code'],response['message'])
				return
			entities = response['entities']
			if not entities:
				# self.ShipItems(uid, None, response['code'], response['message'])
				return
			orders = []
			# 得到订单列表
			# 过滤掉已经声明发货完毕的订单
			for entity in entities:
				orderId = int(entity['orderid'])
				if orderId in playerData["finOrders"]:
					continue
				orders.append(orderId)
			logout.info('ship list is', orders)
			# 假如所有订单都已经发货了，那么不返回
			# 针对本地记录中已经发货的订单，再次调用发货成功的链接
			if not orders:
				self.RetryFinOrders(uid, entities, playerData["finOrders"])
				# self.ShipItems(uid, None, response['code'], response['message'])
				return
			# 从数据库查询已发货的订单
			if shopServerSystem.dbType == DbType.Mongo:
				shopServerSystem.mongoMgr.CheckOrderHistory(uid, orders, lambda records: self._doShipItems(uid, entities, records))
			elif shopServerSystem.dbType == DbType.Mysql:
				shopServerSystem.mysqlMgr.CheckOrderHistory(uid, orders, lambda records: self._doShipItems(uid, entities, records))
		# 从gas链接查询订单信息
		logout.info('Try to get ship list from gas',uid)
		shopServerSystem.mShopManager.GetMcItemOrderList(uid, shopServerSystem.mGameId, shopServerSystem.mIsTestServer, getOrderListCb)
	
	def _doShipItems(self, uid, httpEntities, records):
		'''
		根据已发货的历史和从gas链接查询到的订单信息，执行发货
		'''
		# 离线了就不返回事件了
		playerData = self.mPlayerData.get(uid, None)
		if not playerData:
			# self.ShipItems(uid, None, -2, "player offLine")
			return
		if records is None:
			logout.error('records is None')
			self.ShipItems(uid, None, -1, "records is None")
			return
		existOrders = []
		if shopConsts.GetServerModSystem().dbType == DbType.Mysql:
			for record in records:
				# record[1]代表mysql查找得到的第二个值，代表"_id"字段
				existOrders.append(int(record[1]))
		elif shopConsts.GetServerModSystem().dbType == DbType.Mongo:
			for record in records:
				existOrders.append(int(record["_id"]))
		# 缓存下来
		for orderId in existOrders:
			if orderId not in playerData["finOrders"]:
				playerData["finOrders"].append(orderId)
		# 还没发货的订单
		remainEntities = []
		for entity in httpEntities:
			orderId = int(entity['orderid'])
			if orderId in playerData["finOrders"]:
				continue
			remainEntities.append(entity)
		logout.info('remain list is', remainEntities)
		
		#对于数据库已记录的，同时HttpEntities也有的，则再次调用发货成功的链接（因为正常情况下数据库和HttpEntities是同步的，唯一可能就是调用ShipMcItemOrder时出错了）
		self.RetryFinOrders(uid, httpEntities, playerData["finOrders"])
		#
		self.ShipItems(uid, remainEntities, 0, "正常返回")

	def RetryFinOrders(self, uid, httpEntities, finOrders):
		retryOrders = []
		for entity in httpEntities:
			orderId = int(entity["orderid"])
			if orderId in finOrders:
				retryOrders.append(entity["orderid"])
		if not retryOrders:
			return
		def _shipOrderCb(code, responseStr, time):
			logout.info("_shipretryOrdersCb Post Response.code={} response={} time={}".format(code, responseStr, time))
		shopServerSystem = shopConsts.GetServerModSystem()
		shopServerSystem.mShopManager.ShipMcItemOrder(uid, shopServerSystem.mGameId, retryOrders, shopServerSystem.mIsTestServer, _shipOrderCb)
		
	def ShipItems(self, uid, entities = None,code = None, message = None):
		'''
		通知外部执行发货逻辑
		'''
		data = {"uid": uid, "entities": entities, "code": code, "message": message}
		shopConsts.GetServerModSystem().BroadcastEvent("ServerShipItemsEvent", data)
		
	def OnShipOrderSuccess(self,args):
		uid = args.get('uid', -1)
		remainEntities = args.get('entities', [])
		# 还在线的玩家，需要先更新本地缓存
		playerData = self.mPlayerData.get(uid, None)
		if playerData:
			for entity in remainEntities:
				orderId = int(entity["orderid"])
				if orderId not in playerData["finOrders"]:
					playerData["finOrders"].append(orderId)
		# 更新本地数据库
		shopServerSystem = shopConsts.GetServerModSystem()
		def _insertOrderCb(args):
			if args is None:
				logout.error('insert_order error!')
		for entity in remainEntities:
			logout.info("shipOneItem orderId={}".format(entity['orderid']))
			odersDict = {"uid": uid, "_id": entity['orderid'], "item_id": entity['item_id'],
			             "buy_time": entity['buy_time'], "item_num": entity['item_num']}
			if shopServerSystem.dbType == DbType.Mongo:
				shopServerSystem.mongoMgr.InsertOrder(odersDict, _insertOrderCb)
			elif shopServerSystem.dbType == DbType.Mysql:
				shopServerSystem.mysqlMgr.InsertOrder(odersDict, _insertOrderCb)
		# 调用发货成功的链接，通知平台发货成功
		def _shipOrderCb(code, responseStr, time):
			logout.info("_shipOrderCb Post Response.code={} response={} time={}".format(code, responseStr, time))
		checkOrders = [entity['orderid'] for entity in remainEntities]
		shopServerSystem.mShopManager.ShipMcItemOrder(uid, shopServerSystem.mGameId, checkOrders, shopServerSystem.mIsTestServer, _shipOrderCb)

	def OnCheckItem(self, args):
		uid = args.get('uid')
		item_id = args.get('item_id')
		shopServerSystem = shopConsts.GetServerModSystem()

		def BrocastReSult(uid ,item_id, records):
			existItemids= []
			if shopServerSystem.dbType == DbType.Mysql:
				for record in records:
					# record[1]代表mysql查找得到的第二个值，代表"_id"字段
					existItemids.append(record[2])
			elif shopServerSystem.dbType == DbType.Mongo:
				for record in records:
					existItemids.append(record["item_id"])
			has_buy = False
			if item_id in existItemids:
				has_buy = True
			data = {"uid": uid, "item_id": item_id, "has_buy": has_buy}
			shopServerSystem.BroadcastEvent("CheckItemResultEvent", data)
		if shopServerSystem.dbType == DbType.Mongo:
			shopServerSystem.mongoMgr.CheckItem(uid, item_id, lambda records: BrocastReSult(uid, item_id, records))
		elif shopServerSystem.dbType == DbType.Mysql:
			shopServerSystem.mysqlMgr.CheckItem(uid, item_id, lambda records: BrocastReSult(uid, item_id, records))
	