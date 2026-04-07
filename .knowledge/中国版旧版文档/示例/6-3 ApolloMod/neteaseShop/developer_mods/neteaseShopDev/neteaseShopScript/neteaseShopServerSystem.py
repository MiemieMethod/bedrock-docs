# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

from shopManager import ShopManager
from shopProcess import ShopProccess
import logout
import lobbyGame.netgameApi as netgameApi
from mongoOperation import MongoOperation
from mysqlOperation import MysqlOperation
import netgame.apolloCommon.commonNetgameApi as commonNetgameApi
import json

class DbType(object):
	#使用的数据库种类
	Mongo = 1
	Mysql = 2

class ShopServerSystem(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print '--------ShopServer====start!!!!!~~~~~'
		self.mGameId = 0
		self.mIsTestServer = False
		
		self.mShopManager = ShopManager()
		self.mShopProccess = ShopProccess()
		
		self.mongoMgr = MongoOperation()
		self.mysqlMgr = MysqlOperation()
		self.dbType = 0
		self.Init()
		
	def Init(self):
		modConfig = commonNetgameApi.GetModJsonConfig('neteaseShopScript')
		commonConfig = netgameApi.GetCommonConfig()
		# 使用公共配置中的game_id和game_key配置信息初始化
		gameId = commonConfig.get("game_id", 0)
		gameKey = commonConfig.get("game_key", "")
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
		# env = commonConfig.get("env", None)
		# if env and env == "obt":
		#	self.mIsTestServer = False
		# else:
		#	self.mIsTestServer = True
		print "mGameId ",self.mGameId," mIsTestServer ",self.mIsTestServer
		# 是否自动驱动订单查询
		# True：插件会主动驱动订单查询，无需主动调用API【StartShipProcess】
		# False：插件不会主动查询订单，需要外部逻辑调用API【StartShipProcess】驱动订单查询
		auto_detect = modConfig.get("auto_detect", False)
		self.mShopProccess.InitConfig(auto_detect)
		#
		if self.mysqlMgr.InitMysqlDb() == True:
			self.dbType = DbType.Mysql
		elif self.mongoMgr.InitMongoDb() == True:
			self.dbType = DbType.Mongo
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
		                    self.mShopProccess, self.mShopProccess.OnAddServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
		                    self.mShopProccess, self.mShopProccess.OnDelServerPlayer)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StoreBuySuccServerEvent", 
							self.mShopProccess, self.mShopProccess.OnStoreBuySucc)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ClientLoadAddonsFinishServerEvent", 
							self.mShopProccess, self.mShopProccess.OnClientLoadAddonsFinish)
		
	def StartShipProcess(self, uid):
		'''
		开始发货流程
		'''
		self.mShopProccess.OnCheckPlayerOrder(uid)
		
	def ShipOrderSuccess(self, args):
		'''
		发货成功
		'''
		self.mShopProccess.OnShipOrderSuccess(args)


	def CheckItem(self, args):
		'''
		查看某个商品是否买过
		'''
		self.mShopProccess.OnCheckItem(args)
	
	def Destroy(self):
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent",
		                    self.mShopProccess, self.mShopProccess.OnAddServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "DelServerPlayerEvent",
		                    self.mShopProccess, self.mShopProccess.OnDelServerPlayer)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StoreBuySuccServerEvent", 
							self.mShopProccess, self.mShopProccess.OnStoreBuySucc)
		if self.mShopProccess:
			self.mShopProccess.Destroy()
			self.mShopProccess = None
		if self.dbType == DbType.Mongo:
			self.mongoMgr.Destroy()
		elif self.dbType == DbType.Mysql:
			self.mysqlMgr.Destroy()