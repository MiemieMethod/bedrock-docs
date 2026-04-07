# -*- coding: utf-8 -*-
import apolloCommon.mysqlPool as mysqlPool
import logout
from guildConsts import PlayerAttrType
from guildConsts import GuildAttrType

playerSqlStr = {
	PlayerAttrType.Name : 'name',
	PlayerAttrType.GuildId : 'guild_id',
	PlayerAttrType.Duty : 'duty',
	PlayerAttrType.Activity : 'activity',
	PlayerAttrType.Level : 'player_level',
	PlayerAttrType.LastLoginTime : 'last_login_time'
}
guildSqlStr = {
	GuildAttrType.Name: 'name',
	GuildAttrType.MapId: 'map_id',
	GuildAttrType.MaxNum: 'max_num',
	GuildAttrType.Activity: 'activity',
	GuildAttrType.UnActivityDay: 'un_active_day'
}

class MysqlOperation(object):
	def InitMysqlDb(self):
		# 创建Mysql线程池，这里封装了Mysql的连接建立，多线程执行的功能
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_Guild fail when init mysql")
			return False
		return True
	
	def InsertPlayer(self, playerDict, callback = None):
		'''
		新增玩家数据
		'''
		sql = 'INSERT INTO neteaseGuildPlayerCol (uid, name, guild_id, duty, activity, player_level, last_login_time) VALUES (%s, %s, %s, %s, %s, %s, %s)'
		params = (playerDict.get(PlayerAttrType.Uid), playerDict.get(PlayerAttrType.Name), playerDict.get(PlayerAttrType.GuildId),
		          playerDict.get(PlayerAttrType.Duty), playerDict.get(PlayerAttrType.Activity), playerDict.get(PlayerAttrType.Level),
		          playerDict.get(PlayerAttrType.LastLoginTime))
		mysqlPool.AsyncQueryWithOrderKey(playerDict.get(PlayerAttrType.Uid), sql, params, callback)
		
	def InsertGuild(self, guildDict, callback = None):
		'''
		新增公会数据
		'''
		sql = 'INSERT INTO neteaseGuildCol (guild_id, name, map_id, max_num, activity, un_active_day) VALUES (%s, %s, %s, %s, %s, %s)'
		params = (guildDict.get(GuildAttrType.GuildId), guildDict.get(GuildAttrType.Name), guildDict.get(GuildAttrType.MapId),
		          guildDict.get(GuildAttrType.MaxNum), guildDict.get(GuildAttrType.Activity), guildDict.get(GuildAttrType.UnActivityDay))
		mysqlPool.AsyncQueryWithOrderKey(guildDict.get(PlayerAttrType.Uid), sql, params, callback)
		
	def DeletePlayer(self, uid, callback = None):
		'''
		删除玩家
		'''
		sql = 'DELETE FROM neteaseGuildPlayerCol WHERE uid = %s'
		params = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(uid, sql, params, callback)
		
	def DeleteGuild(self, guildId, callback = None):
		'''
		删除公会
		'''
		sql = 'DELETE FROM neteaseGuildCol WHERE guild_id = %s'
		params = (guildId,)
		mysqlPool.AsyncQueryWithOrderKey(guildId, sql, params, callback)
		
	def CheckPlayerByUid(self, uid, callback = None):
		'''
		通过uid查找玩家
		'''
		sql = 'SELECT uid,name,guild_id,duty,activity,player_level,last_login_time FROM neteaseGuildPlayerCol WHERE uid = %s'
		params = (uid,)
		mysqlPool.AsyncQueryWithOrderKey(uid, sql, params, callback)
		
	def CheckPlayerByGuildId(self, guildId, callback = None):
		'''
		通过公会id查找玩家
		'''
		sql = 'SELECT uid,name,guild_id,duty,activity,player_level,last_login_time FROM neteaseGuildPlayerCol WHERE guild_id = %s'
		params = (guildId,)
		mysqlPool.AsyncQueryWithOrderKey(guildId, sql, params, callback)
		
	def CheckAllPlayer(self, callback = None):
		'''
		查找所有玩家
		'''
		sql = 'SELECT uid,name,guild_id,duty,activity,player_level,last_login_time FROM neteaseGuildPlayerCol'
		params = ()
		mysqlPool.AsyncQueryWithOrderKey('', sql, params, callback)
		
	def CheckGuildByGuildId(self, guildId, callback = None):
		'''
		通过公会id查找公会
		'''
		sql = 'SELECT guild_id, name, map_id, max_num, activity, un_active_day FROM neteaseGuildCol WHERE guild_id = %s'
		params = (guildId,)
		mysqlPool.AsyncQueryWithOrderKey(guildId, sql, params, callback)
		
	def CheckAllGuild(self, callback = None):
		'''
		查找所有公会
		'''
		sql = 'SELECT guild_id, name, map_id, max_num, activity, un_active_day FROM neteaseGuildCol'
		params = ()
		mysqlPool.AsyncQueryWithOrderKey('', sql, params, callback)
		
	def SavePlayerByUid(self, playerDict, callback = None):
		'''
		保存玩家数据
		'''
		sql = 'INSERT INTO neteaseGuildPlayerCol (uid, name, guild_id, duty, activity, player_level, last_login_time) VALUES (%s, %s, %s, %s, %s, %s, %s) ' \
		      'ON DUPLICATE KEY UPDATE name=%s, guild_id=%s, duty=%s, activity=%s, player_level=%s, last_login_time=%s'
		params = (playerDict.get(PlayerAttrType.Uid), playerDict.get(PlayerAttrType.Name), playerDict.get(PlayerAttrType.GuildId),
		          playerDict.get(PlayerAttrType.Duty), playerDict.get(PlayerAttrType.Activity), playerDict.get(PlayerAttrType.Level),
		          playerDict.get(PlayerAttrType.LastLoginTime),
		          #如果存在
		          playerDict.get(PlayerAttrType.Name), playerDict.get(PlayerAttrType.GuildId),
		          playerDict.get(PlayerAttrType.Duty), playerDict.get(PlayerAttrType.Activity), playerDict.get(PlayerAttrType.Level),
		          playerDict.get(PlayerAttrType.LastLoginTime)
		          )
		mysqlPool.AsyncQueryWithOrderKey(playerDict.get(PlayerAttrType.Uid), sql, params, callback)
		
	def SavePlayerPartByUid(self, playerDict, callback = None):
		if playerDict.has_key(PlayerAttrType.Uid) == False and len(playerDict) <= 1:
			return
		sql = ''
		sqlHead = 'UPDATE neteaseGuildPlayerCol SET '
		sqlEnd = ' WHERE uid=%s'
		sql = sql + sqlHead
		paramsList = []
		attrList = []
		for attrType, attrValue in playerDict.items():
			if attrType != PlayerAttrType.Uid:
				attrList.append(playerSqlStr[attrType] + "=%s")
				#sql += playerSqlStr[attrType] + "=%s, "
				paramsList.append(attrValue)
		sql = sql + ','.join(attrList)
		paramsList.append(playerDict.get(PlayerAttrType.Uid))
		params = tuple(paramsList)
		sql = sql + sqlEnd
		mysqlPool.AsyncQueryWithOrderKey(playerDict.get(PlayerAttrType.Uid), sql, params, callback)
		
	def SaveGuildPartByGuildId(self, guildDict, callback = None):
		if guildDict.has_key(GuildAttrType.GuildId) == False and len(guildDict) <= 1:
			return
		sql = ''
		sqlHead = 'UPDATE neteaseGuildCol SET '
		sqlEnd = ' WHERE guild_id=%s'
		sql = sql + sqlHead
		paramsList = []
		attrList = []
		for attrType, attrValue in guildDict.items():
			if attrType != GuildAttrType.GuildId:
				attrList.append(guildSqlStr[attrType] + "=%s")
				#sql += guildSqlStr[attrType] + "=%s, "
				paramsList.append(attrValue)
		sql = sql + ','.join(attrList)
		paramsList.append(guildDict.get(GuildAttrType.GuildId))
		params = tuple(paramsList)
		sql = sql + sqlEnd
		mysqlPool.AsyncQueryWithOrderKey(guildDict.get(GuildAttrType.GuildId), sql, params, callback)
		
	def SaveGuildByGuildId(self, guildDict, callback = None):
		'''
		保存公会数据
		'''
		sql = 'INSERT INTO neteaseGuildCol (guild_id, name, map_id, max_num, activity, un_active_day) VALUES (%s, %s, %s, %s, %s, %s) ' \
		      'ON DUPLICATE KEY UPDATE name=%s,map_id=%s,max_num=%s,activity=%s,un_active_day=%s'
		params = (guildDict.get(GuildAttrType.GuildId), guildDict.get(GuildAttrType.Name), guildDict.get(GuildAttrType.MapId),
		          guildDict.get(GuildAttrType.MaxNum), guildDict.get(GuildAttrType.Activity), guildDict.get(GuildAttrType.UnActivityDay),
		          # 如果存在
		          guildDict.get(GuildAttrType.Name), guildDict.get(GuildAttrType.MapId),
		          guildDict.get(GuildAttrType.MaxNum), guildDict.get(GuildAttrType.Activity), guildDict.get(GuildAttrType.UnActivityDay)
		          )
		mysqlPool.AsyncQueryWithOrderKey(guildDict.get(GuildAttrType.GuildId), sql, params, callback)
		
	def SaveGuildApplication(self, applicationDict, callback = None):
		'''
		新增申请队列的数据
		'''
		sql = 'INSERT INTO neteaseGuildApplication (guild_id, uid, application_time) VALUES (%s, %s, %s)'
		params = (applicationDict.get('guildId'), applicationDict.get('uid'), applicationDict.get('applicationTime'))
		mysqlPool.AsyncQueryWithOrderKey(applicationDict.get('guildId'), sql, params, callback)
		
	def DeleteGuildApplication(self, guildId, uid, callback = None):
		'''
		删除申请队列的数据
		'''
		sql = 'DELETE FROM neteaseGuildApplication WHERE guild_id=%s AND uid=%s'
		params = (guildId, uid)
		mysqlPool.AsyncQueryWithOrderKey(uid, sql, params, callback)
		
	def CheckApplicationByGuildId(self, guildId, callback = None):
		'''
		查询申请队列的数据
		'''
		sql = 'SELECT guild_id, uid, application_time FROM neteaseGuildApplication WHERE guild_id=%s'
		params = (guildId,)
		mysqlPool.AsyncQueryWithOrderKey(guildId, sql, params, callback)
		
	def Destroy(self):
		mysqlPool.Finish()
		