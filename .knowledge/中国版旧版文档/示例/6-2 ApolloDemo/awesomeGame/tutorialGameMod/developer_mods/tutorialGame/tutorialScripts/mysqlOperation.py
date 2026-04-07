# -*- coding: utf-8 -*-
import apolloCommon.mysqlPool as mysqlPool
import logout
import lobbyGame.netgameApi as netgameApi
import utils


class MysqlOperation(object):
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		exist, host, user, password, database, port = netgameApi.GetMysqlConfig()
		if exist:
			mysqlPool.Init(host, port, user, password, database, 20)
		else:
			logout.error("[DATABASE_ERROR] mysql db not exist; server will not do right thing!")
		return exist
		
	def AddDiamondSword(self, playerId):
		'''
		玩家钻石剑数量加1
		'''
		uid = netgameApi.GetPlayerUid(playerId)
		sql = 'SELECT DiamondSwordNum FROM tutorialmod WHERE uid=%s'
		params = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(
			 uid,
			sql,
			params,
			lambda data: self.AddOneDiamondSword(uid, data))
		
	def AddOneDiamondSword(self, uid, data):
		print "AddOneDiamondSword",data
		if data:
			delta = 1
			sql = 'UPDATE tutorialmod SET DiamondSwordNum=DiamondSwordNum+%s WHERE uid=%s'
			params = (delta,uid)
			mysqlPool.AsyncExecuteWithOrderKey(
				uid,
				sql,
				params,
				lambda ret:self.modifyRoleDataCb(uid, delta,ret))
		else:
			sql = 'INSERT INTO tutorialmod (uid, DiamondSwordNum) VALUES (%s, %s)'
			params = (uid, 1)
			mysqlPool.AsyncExecuteWithOrderKey(
				uid,
				sql,
				params,
				lambda ret: self.modifyRoleDataCb(uid, 1, ret))
			pass
	
	def modifyRoleDataCb(self,uid, delta, ret):
		if ret is None:
			logout.error("UPDATE ROLE DATA FOR [%d] FAIL dexp=%s" % (uid, delta))
			
	def Destroy(self):
		mysqlPool.Finish()
		