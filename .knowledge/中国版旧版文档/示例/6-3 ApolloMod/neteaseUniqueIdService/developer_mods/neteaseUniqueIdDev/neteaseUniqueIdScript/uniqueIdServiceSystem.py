# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import service.serviceConf as serviceConf
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.mongoPool as mongoPool
import logout
import neteaseUniqueIdScript.uniqueIdConsts as uniqueIdConsts


# 唯一ID模块的system
# 根据配置文件中数据库的配置，初始化数据库连接池（mongo or mysql）
# 根据数据库初始化的状态实例化实现具体功能的类
class UniqueIdServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		self.useDb = None
		# 尝试初始化数据库连接池
		if uniqueIdConsts.TryUseMysqlFirst:
			suc = self.InitMysql()
			if suc:
				self.useDb = "mysql"
			else:
				logout.error("UniqueIdServiceSystem init fail by no Mysql database support")
				return
		else:
			suc = self.InitMongo()
			if suc:
				self.useDb = "mongo"
			else:
				logout.error("UniqueIdServiceSystem init fail by no Mongo database support")
				return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（唯一ID模块对应的是neteaseUniqueId），
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.activeMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith("neteaseUniqueId"):
				# 成功初始化mongo连接池，则实例化mongo版
				if self.useDb == "mongo":
					self.activeMgrs[moduleName] = self.CreateMongoMgr(moduleName)
				# 成功初始化mysql连接池，则实例化mysql版
				elif self.useDb == "mysql":
					self.activeMgrs[moduleName] = self.CreateMysqlMgr(moduleName)
				# 否则打印ERROR日志
				else:
					logout.error("ServiceUniqueidSys init_fail no database usable")

	# 初始化mongo版
	def CreateMongoMgr(self, moduleName):
		import neteaseUniqueIdScript.uniqueIdMgrMongo as uniqueIdMgrMongo
		return uniqueIdMgrMongo.CUniqueIdMgr(self, moduleName)

	# 初始化mysql版
	def CreateMysqlMgr(self, moduleName):
		import neteaseUniqueIdScript.uniqueIdMgrMysql as uniqueIdMgrMysql
		return uniqueIdMgrMysql.CUniqueIdMgr(self, moduleName)

	# service的tick
	def Update(self):
		pass

	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		if self.useDb == "mongo":
			mongoPool.Finish()
		elif self.useDb == "mysql":
			mysqlPool.Finish()
		ServiceSystem.Destroy(self)
	# ------------------------------------------------------------------------------------------------
	# 初始化mongo连接池
	def InitMongo(self):
		try:
			mongoPool.InitDB(20)
		except:
			logout.warning("UniqueIdServiceSystem failed by init mongo database fail")
			return False
		return True

	def InitMysql(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.warning("UniqueIdServiceSystem failed by init mysql database fail")
			return False
		return True
# ------------------------------------------------------------------------------------------------

