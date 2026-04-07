# -*- coding: utf-8 -*-
import apolloCommon.mysqlPool as mysqlPool
import logout
import lobbyGame.netgameApi as netgameApi

class MysqlOperation(object):
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		exist, host, user, password, database, port = netgameApi.GetMysqlConfig()
		if exist:
			mysqlPool.Init(host, port, user, password, database, 20)
		else:
			logout.error("[DATABASE_ERROR] mysql db not exist; server will not do right thing!")
		return exist
	
	def QueryPlayerData(self, player_id, uid, cb=None):
		sql = 'SELECT uid,nickname,login_time FROM playerCol WHERE uid=%s'
		params = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(uid,sql,params, cb)
	
	def InsertPlayerData(self, player_id, uid, player_data, cb=None):
		sql = 'INSERT INTO playerCol (uid, nickname,login_time) VALUES (%s, %s, %s)'
		params = (uid, player_data['nickname'],player_data['login_time'])
		mysqlPool.AsyncQueryWithOrderKey(uid,sql,params,cb)
	
	def SavePlayerByUid(self, uid, player_data, cb=None):
		sql = 'UPDATE playerCol SET nickname=%s,login_time=%s WHERE uid=%s'
		params = (player_data['nickname'],player_data['login_time'],uid)
		mysqlPool.AsyncQueryWithOrderKey(uid,sql, params, cb)
		
	def Destroy(self):
		mysqlPool.Finish()
		