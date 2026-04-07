# -*- coding: utf-8 -*-
#
import logout
import apolloCommon.mongoPool as mongoPool
import neteaseUniqueIdScript.uniqueIdConsts as uniqueIdConsts
import neteaseUniqueIdScript.uniqueIdMgrBase as uniqueIdMgrBase
#---------------------------------------------------------------------------------
# 服务初始化时，从数据库查询过去已经用掉的唯一ID的记录
def QueryHistroyByMongo(collection):
	cur = collection.find({})
	if cur:
		records = []
		for record in cur:
			records.append(record)
		return records
	else:
		return None

# 插入一条新的记录，某个keyword首次申请ID时调用
def InsertHistroyByMongo(collection, _dict):
	ret = collection.insert_one(_dict)
	return ret

# 更新某个keyword已有记录中，max_id和plus
# db_maxid更新成功，等价于申请可用ID成功
def UpdateHistroyByMongo(collection, _id, _dict):
	ret = collection.replace_one({"_id": _id}, _dict)
	return ret
#---------------------------------------------------------------------------------
class CUniqueIdMgr(uniqueIdMgrBase.CUniqueIdMgr):
	def __init__(self, system, moduleName):
		super(CUniqueIdMgr, self).__init__(system, moduleName)
		# 初始化时需要查询历史记录
		self.QueryHistroyByMongo()
		logout.info("CREATE_SERVICE_SUCCESS module_name=%s use Mongo" % moduleName)
		
	def Destroy(self):
		super(CUniqueIdMgr, self).Destroy()
	
	# 从数据库查询过去已经用掉的唯一ID的记录
	def QueryHistroyByMongo(self):
		callback = lambda records:self.QueryHistroyByMongoCallback(records)
		mongoPool.AsyncExecuteWithOrderKey(uniqueIdConsts.TableUniqueId,
										   QueryHistroyByMongo,
										   "uniqueId",
										   callback,
										   )

	# service启动时查询历史唯一ID的返回
	def QueryHistroyByMongoCallback(self, records):
		if records is None:
			logout.error("UniqueIdServiceSystem QueryHistroyByMongo fail")
			return
		# 每条记录对应一个keyword
		# size是每次向数据库申请新的ID时的数量
		# db_maxid是已经用掉的ID的最大值，新的可用ID将从db_maxid+1开始
		for record in records:
			keyword = record["_id"]
			plusSize = record.get("plus", uniqueIdConsts.DefaultPlusSize)
			dbMaxId = record.get("max_id", 0)
			self.UpdateMemoryCache(keyword, plusSize, dbMaxId)
		self.mModuleReady = True
	#------------------------------------------------------------------------------
	# 插入一条新的keyword记录
	def InsertKeyword(self, keyword, requireNum):
		# 根据单次申请的ID数量，确定size
		size = max(requireNum*10, uniqueIdConsts.DefaultPlusSize)
		# 首次插入记录，同时完成第一次数据库ID申请
		# 假如插入成功，那么可用ID就是从1到size（默认0已经用掉了）
		_dict = {
			"_id": keyword,
			"plus": size,
			"max_id": size,
		}
		callback = lambda ret:self.InsertHistroyByMongoCallback(keyword, _dict, ret)
		mongoPool.AsyncExecuteWithOrderKey(uniqueIdConsts.TableUniqueId,
										   InsertHistroyByMongo,
										   "uniqueId_%s"%keyword,
										   callback,
										   _dict)
	
	# 插入记录的返回
	def InsertHistroyByMongoCallback(self, keyword, _dict, ret):
		# 插入失败，调用失败返回
		# 此时所有在排队的ID申请都会收到失败的返回
		if (not ret) or (not ret.inserted_id):
			self.OnMakeUniqueIdFailed(keyword, uniqueIdConsts.CodeAskNewMongoFail)
			return
		# 插入成功，更新内存缓存中的数据
		# 此时已经用掉的ID最大值是0，可用的ID最大值就是size
		self.UpdateMemoryCache(keyword, _dict["plus"], _dict["max_id"], 0)
		self.OnMakeUniqueIdSuccess(keyword)
	
	# 当前内存缓存中剩余可用的ID数量不够满足申请
	# 再次向数据库申请可用ID（即增加db_maxid的值）
	def RequireMoreKeyword(self, keyword, cacheData, requireNum):
		# 同样根据单次申请的ID数量，确定size
		size = max(requireNum*10, cacheData['plusSize'])
		# db_maxid增加到db_maxid+size，即申请新的size个可用ID
		# 假如插入成功，那么可用ID最小值不变，最大值增加到db_maxid+size
		_dict = {
			"_id": keyword,
			"plus": size,
			"max_id": cacheData['dbMaxId']+size,
		}
		callback = lambda ret:self.UpdateHistroyByMongoCallback(keyword, _dict, ret)
		mongoPool.AsyncExecuteWithOrderKey(uniqueIdConsts.TableUniqueId,
										   UpdateHistroyByMongo,
										   "uniqueId_%s"%keyword,
										   callback,
										   keyword, _dict)
	
	# 更新记录的返回
	def UpdateHistroyByMongoCallback(self, keyword, _dict, ret):
		# 更新记录成功，刷新内存缓存中的数据
		# 此时已经用掉的ID最大值不变，可用的ID最大值就是等于新记录的db_maxid
		if ret and (ret.modified_count == 1):
			self.UpdateMemoryCache(keyword, _dict['plus'], _dict['max_id'])
			self.OnMakeUniqueIdSuccess(keyword)
		# 更新记录失败
		# 同样所有在排队的ID申请都会收到失败的返回
		else:
			self.OnMakeUniqueIdFailed(keyword, uniqueIdConsts.CodeAskNewMongoFail)
	#------------------------------------------------------------------------------
	
	
	




