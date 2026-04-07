# -*- coding: utf-8 -*-
import apolloCommon.mongoPool as mongoPool
import logout
# -----------------------------------------------------------------------------------
ORDER_HISOTRY_COL = "order_history"
def insert_order(collection, base):
	ret = collection.insert(base)
	return ret

def query_orders(collection, uid, orders):
	datas = collection.find({"uid":uid, "_id":{"$in":orders}})
	return datas

class MongoOperation(object):
	
	def InitMongoDb(self):
		try:
			mongoPool.InitDB(20)
		except:
			logout.error("start_Auth fail when init mongo")
			return False
		return True
	
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