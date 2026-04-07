# -*- coding: utf-8 -*-
import server.extraMasterApi as extraMasterApi
MasterSystem = extraMasterApi.GetMasterSystemCls()
import master.masterHttp as masterHttp
import json
import logout
from shopManager import ShopManager
from mongoOperation import MongoOperation
from mysqlOperation import MysqlOperation
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi

class DbType(object):
	#使用的数据库种类
	Mongo = 1
	Mysql = 2

class ShopMasterSystem(MasterSystem):
	def __init__(self, namespace, systemName):
		MasterSystem.__init__(self, namespace, systemName)
		self.mGameId = 0
		self.mIsTestServer = False
		self.mGameKey = ""
		self.mShopManager = ShopManager()
		
		self.mongoMgr = MongoOperation()
		self.mysqlMgr = MysqlOperation()
		self.dbType = 0
		masterHttp.RegisterMasterHttp("/check-single-order", self, self.HttpCheckSingleOrder)
		masterHttp.RegisterMasterHttp("/check-orders-list", self, self.HttpCheckOrdersList)
		masterHttp.RegisterMasterHttp("/ship-orders-success", self, self.HttpShipOrderSuccess)
		self.Init()
	
	def Init(self):
		from master.masterConf import netgameConf
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseShopScript')
		# 使用公共配置中的game_id和game_key配置信息初始化
		gameId = netgameConf.get("game_id", 0)
		gameKey = netgameConf.get("game_key", "")
		if isinstance(gameKey, unicode):
			gameKey = gameKey.encode("utf-8")
		self.mGameId = gameId
		self.mShopManager.SetParam(gameKey)
		# 根据公共配置中的env配置来确定是否正式服
		# 审核通过之后商城插件无需通过再次修改来适用正式服
		reviewStage = commonNetgameApi.GetApolloReviewStage()
		if reviewStage == 2:
			self.mIsTestServer = False
		else:
			self.mIsTestServer = True
		# env = netgameConf.get("env", None)
		# if env and env == "obt":
		#	self.mIsTestServer = False
		# else:
		#	self.mIsTestServer = True
		print "mGameId ", self.mGameId, " mIsTestServer ", self.mIsTestServer
		if self.mysqlMgr.InitMysqlDb() == True:
			self.dbType = DbType.Mysql
		elif self.mongoMgr.InitMongoDb() == True:
			self.dbType = DbType.Mongo
		
	def HttpCheckSingleOrder(self, clientId, requestBody):
		'''
		查询一个订单信息
		'''
		eventData = json.loads(requestBody)
		if eventData.has_key('uid') == False or eventData.has_key('orderid') == False:
			self.SendResponse(clientId, 12, "参数错误")
			return
		uid = eventData.get('uid', -1)
		orderid = eventData.get('orderid', -1)
		self.GetMcItemOrderList(clientId, uid, orderid)
		
	def HttpCheckOrdersList(self, clientId, requestBody):
		'''
		查询订单信息列表
		'''
		eventData = json.loads(requestBody)
		if eventData.has_key('uid') == False:
			self.SendResponse(clientId, 12, "参数错误")
			return
		uid = eventData.get('uid', -1)
		self.GetMcItemOrderList(clientId,uid)
		
	def HttpShipOrderSuccess(self, clientId, requestBody):
		'''
		发货成功
		'''
		eventData = json.loads(requestBody)
		if eventData.has_key('orderid') == False or eventData.has_key('uid') == False:
			self.SendResponse(clientId, 12, "参数错误")
			return
		uid = eventData.get('uid', -1)
		orderid = eventData.get('orderid', -1)
		def _shipOrderCb(code, responseStr, time):
			print '_shipOrderCb Post Response.code', code, ' response:', responseStr, ' time:', time
			try:
				response = json.loads(responseStr)
			except:
				logout.warning("ShipPlayer, cannot load json!")
				self.SendResponse(clientId, 16, "请求链接出错")
				return
			self.SendResponse(clientId, response['code'], response["message"], None)
		checkOrders = []
		checkOrders.append(orderid)
		self.mShopManager.ShipMcItemOrder(uid, self.mGameId, checkOrders, self.mIsTestServer, _shipOrderCb)
		
	def GetMcItemOrderList(self, clientId, uid, checkOrderId = -1):
		'''
		获取订单列表
		'''
		
		def ResponseRemainItems(uid, httpEntities, records, orderid):
			'''
			根据已发货的历史和从gas链接查询到的订单信息
			'''
			if records is None:
				logout.error('records is None')
				return
			existOrders = []
			if self.dbType == DbType.Mysql:
				for record in records:
					# record[1]代表mysql查找得到的第二个值，代表"_id"字段
					existOrders.append(record[1])
			elif self.dbType == DbType.Mongo:
				for record in records:
					existOrders.append(record["_id"])
			# 还没发货的订单
			if orderid != -1:
				remainEntities = [entity for entity in httpEntities if int(entity['orderid']) not in existOrders and int(entity['orderid']) == int(orderid)]
			else:
				remainEntities = [entity for entity in httpEntities if int(entity['orderid']) not in existOrders]
			self.SendResponse(clientId, 0, "正常返回", remainEntities)

			# 对于数据库已记录的，同时HttpEntities也有的，则再次调用发货成功的链接（因为正常情况下数据库和HttpEntities是同步的，唯一可能就是调用ShipMcItemOrder时出错了）
			def _shipOrderCb(code, responseStr, time):
				print '_shipretryOrdersCb Post Response.code', code, ' response:', responseStr, ' time:', time
			retryOrders = [entity['orderid'] for entity in httpEntities if int(entity['orderid']) in existOrders]
			self.mShopManager.ShipMcItemOrder(uid, self.mGameId, retryOrders, self.mIsTestServer, _shipOrderCb)
		def getOrderListCb(code, responseStr, time):
			print 'getOrderListCb Post Response.code:', code, ' response:', responseStr, ' time:', time
			try:
				response = json.loads(responseStr)
			except:
				logout.warning("ShipPlayer, cannot load json!")
				self.SendResponse(clientId, 16, "请求链接出错")
				return
			if 200 != code or 0 != response['code']:
				logout.error('Response error!')
				self.SendResponse(clientId, response['code'], response["message"])
				return
			entities = response['entities']
			if not entities:
				self.SendResponse(clientId, response['code'], response["message"])
				return 
			orders = []
			# if orderid != -1:
			# 	# 如果传入了订单id，则匹配订单id
			# 	for entity in entities:
			# 		if entity["orderid"] == orderid:
			# 			orders.append(entity)
			# else:
			# 	#否则，所有订单一起返回
			# 	for entity in entities:
			# 		orders.append(entity)
			for entity in entities:
				orders.append(int(entity['orderid']))
			if self.dbType == DbType.Mongo:
				self.mongoMgr.CheckOrderHistory(uid, orders, lambda records: ResponseRemainItems(uid, entities, records, checkOrderId))
			elif self.dbType == DbType.Mysql:
				self.mysqlMgr.CheckOrderHistory(uid, orders, lambda records: ResponseRemainItems(uid, entities, records, checkOrderId))
			#self.SendResponse(clientId, response["code"], response["message"], returnEntities)
		self.mShopManager.GetMcItemOrderList(uid, self.mGameId, self.mIsTestServer, getOrderListCb)
		
	def SendResponse(self, clientId, code, message, entities = None):
		response = {}
		response['code'] = code
		response['message'] = message
		response['entity'] = entities
		response = json.dumps(response)
		masterHttp.SendHttpResponse(clientId, response)
		