# -*- coding: utf-8 -*-
import apolloCommon.mysqlPool as mysqlPool
import logout

class MysqlOperation(object):
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_Auth fail when init mysql")
			return False
		return True
	
	def CheckOrderHistory(self, uid, orders, callback = None):
		'''
		从数据库查找历史订单信息
		'''
		sql = 'SELECT * FROM neteaseOrderHistory WHERE uid=%s AND _id in %s'
		params = (uid,orders,)
		mysqlPool.AsyncQueryWithOrderKey(uid, sql, params, callback)
		
	def InsertOrder(self, odersDict, callback = None):
		'''
		插入一条订单信息至数据库
		'''
		sql = 'INSERT INTO neteaseOrderHistory (uid, _id, item_id, buy_time, item_num) VALUES (%s, %s, %s, %s, %s)'
		params = (odersDict["uid"],odersDict['_id'], odersDict['item_id'], odersDict['buy_time'], odersDict['item_num'])
		mysqlPool.AsyncQueryWithOrderKey(odersDict["uid"], sql, params, callback)
		
	def Destroy(self):
		mysqlPool.Finish()