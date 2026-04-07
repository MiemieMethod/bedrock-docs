# -*- coding: utf-8 -*-
#
import logout
import apolloCommon.mysqlPool as mysqlPool
import neteaseUniqueIdScript.uniqueIdConsts as uniqueIdConsts
import neteaseUniqueIdScript.uniqueIdMgrBase as uniqueIdMgrBase
#---------------------------------------------------------------------------------
class CUniqueIdMgr(uniqueIdMgrBase.CUniqueIdMgr):
	def __init__(self, system, moduleName):
		super(CUniqueIdMgr, self).__init__(system, moduleName)
		# 初始化时需要查询历史记录
		self.QueryHistroyByMysql()
		logout.info("CREATE_SERVICE_SUCCESS module_name=%s use Mysql" % moduleName)
		
	def Destroy(self):
		super(CUniqueIdMgr, self).Destroy()
	
	# 从数据库查询过去已经用掉的唯一ID的记录
	def QueryHistroyByMysql(self):
		sql = 'SELECT keyword, max_id, plus FROM %s' % uniqueIdConsts.TableUniqueId
		params = ()
		callback = lambda records:self.QueryHistroyByMysqlCallback(records)
		mysqlPool.AsyncQueryWithOrderKey("uniqueId", sql, params, callback)

	# service启动时查询历史唯一ID的返回
	def QueryHistroyByMysqlCallback(self, records):
		# 查询语句执行失败时records为None
		if records is None:
			logout.error("UniqueIdServiceSystem QueryHistroyByMysql fail")
			return
		# 每条记录对应一个keyword
		# size是每次向数据库申请新的ID时的数量
		# db_maxid是已经用掉的ID的最大值，新的可用ID将从db_maxid+1开始
		for record in records:
			keyword = record[0]
			dbMaxId = record[1]
			plusSize = record[2]
			self.UpdateMemoryCache(keyword, plusSize, dbMaxId)
		self.mModuleReady = True
	#------------------------------------------------------------------------------
	# 插入一条新的keyword记录
	def InsertKeyword(self, keyword, requireNum):
		# 根据单次申请的ID数量，确定size
		size = max(requireNum*10, uniqueIdConsts.DefaultPlusSize)
		# 首次插入记录，同时完成第一次数据库ID申请
		# 假如插入成功，那么可用ID就是从1到size（默认0已经用掉了）
		sql = "INSERT INTO %s (keyword, max_id, plus)" % uniqueIdConsts.TableUniqueId
		sql += "VALUES (%s, %s, %s)"
		params = (keyword, size, size)
		callback = lambda suc:self.InsertHistroyByMysqlCallback(keyword, size, size, suc)
		mysqlPool.AsyncExecuteWithOrderKey("uniqueId_%s"%keyword, sql, params, callback)
	
	# 插入记录的返回
	def InsertHistroyByMysqlCallback(self, keyword, size, dbMaxId, suc):
		# 插入失败，调用失败返回
		# 此时所有在排队的ID申请都会收到失败的返回
		if not suc:
			self.OnMakeUniqueIdFailed(keyword, uniqueIdConsts.CodeAskNewMysqlFail)
			return
		# 插入成功，更新内存缓存中的数据
		# 此时已经用掉的ID最大值是0，可用的ID最大值就是size
		self.UpdateMemoryCache(keyword, size, dbMaxId, 0)
		self.OnMakeUniqueIdSuccess(keyword)
	
	# 当前内存缓存中剩余可用的ID数量不够满足申请
	# 再次向数据库申请可用ID（即增加db_maxid的值）
	def RequireMoreKeyword(self, keyword, cacheData, requireNum):
		# 同样根据单次申请的ID数量，确定size
		size = max(requireNum*10, cacheData['plusSize'])
		# db_maxid增加到db_maxid+size，即申请新的size个可用ID
		# 假如插入成功，那么可用ID最小值不变，最大值增加到db_maxid+size
		dbMaxId = cacheData['dbMaxId']+size
		sql = "UPDATE %s SET " % uniqueIdConsts.TableUniqueId
		sql += "plus=%s, max_id=%s WHERE keyword=%s"
		params = (size, dbMaxId, keyword)
		callback = lambda suc:self.UpdateHistroyByMysqlCallback(keyword, size, dbMaxId, suc)
		mysqlPool.AsyncExecuteWithOrderKey("uniqueId_%s"%keyword, sql, params, callback)
	
	# 更新记录的返回
	def UpdateHistroyByMysqlCallback(self, keyword, size, dbMaxId, suc):
		# 更新记录失败
		# 同样所有在排队的ID申请都会收到失败的返回
		if not suc:
			self.OnMakeUniqueIdFailed(keyword, uniqueIdConsts.CodeAskNewMysqlFail)
			return
		# 更新记录成功，刷新内存缓存中的数据
		# 此时已经用掉的ID最大值不变，可用的ID最大值就是等于新记录的db_maxid
		self.UpdateMemoryCache(keyword, size, dbMaxId)
		self.OnMakeUniqueIdSuccess(keyword)
	#------------------------------------------------------------------------------
	
	
	




