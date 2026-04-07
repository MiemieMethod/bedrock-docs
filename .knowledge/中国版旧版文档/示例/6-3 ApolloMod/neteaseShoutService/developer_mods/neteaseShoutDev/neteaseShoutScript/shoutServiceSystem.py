# -*- coding: utf-8 -*-

import service.serviceConf as serviceConf
import logout
import neteaseShoutScript.shoutConst as shoutConst
import neteaseShoutScript.timermanager as timermanager
import server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()


class ShoutServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		if not self.InitShoutCfg():
			return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（模块对应的是neteaseShout）
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(shoutConst.ModName):
				mgr = self.CreateShoutMgr(moduleName)
				self.mActionMgrs[moduleName] = mgr

	def CreateShoutMgr(self, moduleName):
		from neteaseShoutScript.shoutMgr import ShoutMgr
		return ShoutMgr(self, moduleName)

	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		super(ShoutServiceSystem, self).Destroy()

	def Update(self):
		timermanager.timerManager.tick()

	def InitShoutCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseShoutScript")
		if not cfg:
			logout.error("nothing in InitShoutCfg")
			return False
		self.mShoutInterval = cfg['interval']
		self.mContentWordCountLimit = cfg['wc']
		self.mPendingCountLimit = cfg['qsize']
		return True

	def GetShoutInterval(self):
		return self.mShoutInterval

	def GetContentWordCountLimit(self):
		return self.mContentWordCountLimit

	def GetPendingCountLimit(self):
		return self.mPendingCountLimit
