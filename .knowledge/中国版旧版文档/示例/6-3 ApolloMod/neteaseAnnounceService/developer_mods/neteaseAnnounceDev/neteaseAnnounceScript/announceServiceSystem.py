# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import service.serviceConf as serviceConf
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import logout
import neteaseAnnounceScript.announceConsts as announceConsts
import neteaseAnnounceScript.timermanager as timermanager

class AnnounceServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self,namespace,systemName)
		suc = self.InitMysqlPool()
		if not suc:
			return
		suc = self.initRedisPool()
		if not suc:
			return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（公告模块对应的是netease_announce），
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(announceConsts.ModNameSpace):
				mgr = self.CreateAnnounceMgr(moduleName)
			else:
				continue
			self.mActionMgrs[moduleName] = mgr

	def CreateAnnounceMgr(self, moduleName):
		import neteaseAnnounceScript.announceMgr as announceMgr
		return announceMgr.AnnounceMgr(self, moduleName)
	
	def OutSendMailToMany(self, touids, title, content, itemList=[], expire=None, srcName=""):
		mgr = self.mActionMgrs[announceConsts.ModNameSpace]
		eventData = {
			"touids": touids,
			"title": title,
			"content": content,
			"itemList": itemList,
			"expire": expire,
			"srcName": srcName,
		}
		mgr.OutDoMailSendToUser(touids, eventData)

	def OutSendMailToGroup(self, title, content, itemList=[], effectTime=None, expire=None, srcName=""):
		mgr = self.mActionMgrs[announceConsts.ModNameSpace]
		mgr.OutSendMailToGroup(title, content, itemList, effectTime, expire, srcName)

	def Update(self):
		timermanager.timerManager.tick()
	
	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		mysqlPool.Finish()
		redisPool.Finish()
		ServiceSystem.Destroy(self)
	#------------------------------------------------------------------------------------------------
	# 初始化mysql连接池
	def InitMysqlPool(self):
		# 尝试初始化mysql连接池，失败则打印ERROR日志并返回False
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("start_announce_service fail when init mysql")
			return False
		return True

	def initRedisPool(self):
		try:
			redisPool.InitDB(20)
		except:
			logout.error("start_announce_service fail when init redis")
			return False
		return True
	#------------------------------------------------------------------------------------------------
		