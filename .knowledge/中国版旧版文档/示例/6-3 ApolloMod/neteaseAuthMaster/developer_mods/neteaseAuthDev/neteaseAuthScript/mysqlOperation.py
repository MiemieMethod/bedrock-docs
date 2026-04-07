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
	
	def QueryAllPlayerGroup(self, cb = None):
		'''
		从数据库查找所有玩家的分组
		'''
		sql = 'SELECT uid,auth_group FROM neteasePlayerAuth'
		params = ()
		mysqlPool.AsyncQueryWithOrderKey('player', sql, params, cb)
	
	def QueryPlayerGroup(self, uid, cb = None):
		'''
		从数据库查找特定玩家的分组
		'''
		sql = 'SELECT auth_group FROM neteasePlayerAuth WHERE uid=%s'
		params = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(uid, sql, params, cb)
	
	def InsertPlayerGroup(self, uid, authData, cb = None):
		'''
		新增一个玩家分组至数据库
		'''
		sql = 'INSERT INTO neteasePlayerAuth (uid, auth_group) VALUES (%s, %s)'
		params = (uid, authData['authGroup'])
		mysqlPool.AsyncExecuteWithOrderKey(uid, sql, params, cb)
	
	def SavePlayerGroupByUid(self, uid, authData, cb = None):
		'''
		改变一个玩家分组至数据库
		'''
		sql = 'UPDATE neteasePlayerAuth SET auth_group=%s WHERE uid=%s'
		params = (authData['authGroup'], uid)
		mysqlPool.AsyncExecuteWithOrderKey(uid, sql, params, cb)
	
	def Destroy(self):
		mysqlPool.Finish()