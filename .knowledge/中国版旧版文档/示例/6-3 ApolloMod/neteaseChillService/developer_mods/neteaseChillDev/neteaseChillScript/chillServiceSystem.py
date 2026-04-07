# -*- coding: utf-8 -*-

import service.serviceConf as serviceConf
import apolloCommon.mysqlPool as mysqlPool
import apolloCommon.redisPool as redisPool
import logout
import neteaseChillScript.chillConst as chillConst
import neteaseChillScript.timermanager as timermanager
import server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()


class ChillServiceSystem(ServiceSystem):
	"""
	该mod的service类
	逻辑在ChillMgr中
	"""
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		if not self.InitMysqlPool():
			return
		if not self.InitRedisPool():
			return
		if not self.InitChillCfg():
			return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（模块对应的是neteaseChill）
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(chillConst.ModName):
				mgr = self.CreateChillMgr(moduleName)
				self.mActionMgrs[moduleName] = mgr

	def CreateChillMgr(self, moduleName):
		from neteaseChillScript.chillMgr import ChillMgr
		return ChillMgr(self, moduleName)

	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		mysqlPool.Finish()
		redisPool.Finish()
		# ServiceSystem.Destroy(self)
		super(ChillServiceSystem, self).Destroy()

	def Update(self):
		timermanager.timerManager.tick()

	# 初始化mysql连接池
	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(20)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	def InitRedisPool(self):
		# try:
		# 	redisPool.InitDB(20)
		# except:
		# 	logout.error("Exception in InitRedisPool")
		# 	return False
		return True

	def InitChillCfg(self):
		# import apolloCommon.commonNetgameApi as commonNetgameApi
		# cfg = commonNetgameApi.GetModJsonConfig("neteaseChillScript")
		# if not cfg:
		# 	logout.error("nothing in InitChillCfg")
		# 	return False
		# raw = {}
		# import time
		# for reward in cfg[chillConst.CfgKeyRewards]:
		# 	departure = time.strptime(reward['date'], '%Y-%m-%d')
		# 	if departure.tm_wday:
		# 		# 这天不是周一
		# 		# 配置有误
		# 		logout.warning('配置段 {} 不生效因日期 {} 非周一'.format(reward, reward['date']))
		# 		continue
		# 	date = time.strftime('%Y-%m-%d', departure)
		# 	if date in raw:
		# 		logout.warning('配置段 {} 被配置段 {} 替换'.format(raw[date][-1], reward))
		# 	raw[date] = (time.mktime(departure), reward)
		# if not raw:
		# 	logout.warning('所有配置段均不生效')
		# 	return False
		# raw = raw.values()
		# raw.sort()
		# self.mRewards = raw
		return True

	def GetChillCfg(self):
		# return self.mRewards
		return
