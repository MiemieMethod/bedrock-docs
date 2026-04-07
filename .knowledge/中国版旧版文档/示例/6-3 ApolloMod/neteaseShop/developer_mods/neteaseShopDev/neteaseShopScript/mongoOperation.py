# -*- coding: utf-8 -*-
import apolloCommon.mongoPool as mongoPool
import logout
import lobbyGame.netgameApi as netgameApi
# -----------------------------------------------------------------------------------
ORDER_HISOTRY_COL = "order_history"
def insert_order(collection, base):
	ret = collection.insert(base)
	return ret

def query_orders(collection, uid, orders):
	datas = collection.find({"uid":uid, "_id":{"$in":orders}})
	return datas

def query_items(collection, uid, item_id):
	datas = collection.find({"uid": uid, "item_id": item_id})
	return datas

class MongoOperation(object):
	
	def InitMongoDb(self):
		exist, host, user, password, database, port = netgameApi.GetMongoConfig()
		if exist:
			mongoPool.Init(host, port, user, password, database, 20)
		else:
			logout.error("[DATABASE_ERROR] mongo db not exist!")
		return exist

	def CheckItem(self, uid, item_id, callback = None):
		'''
		从数据库查找历史订单信息
		'''
		mongoPool.AsyncExecute(ORDER_HISOTRY_COL, query_items, callback, uid, item_id)
	
	def CheckOrderHistory(self, uid, orders, callback = None):
		'''
		从数据库查找历史订单信息
		'''
		mongoPool.AsyncExecute(ORDER_HISOTRY_COL, query_orders, callback, uid, orders)
	
	def InsertOrder(self, odersDict, callback = None):
		'''
		插入一条订单信息至数据库
		'''
		mongoPool.AsyncExecute(ORDER_HISOTRY_COL, insert_order, callback, odersDict)
	
	def Destroy(self):
		mongoPool.Finish()