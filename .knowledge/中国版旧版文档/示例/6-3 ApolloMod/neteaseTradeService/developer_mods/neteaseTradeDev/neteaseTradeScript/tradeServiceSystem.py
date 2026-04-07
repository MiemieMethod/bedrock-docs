# -*- coding: utf-8 -*-

import service.serviceConf as serviceConf
import apolloCommon.mysqlPool as mysqlPool
# import apolloCommon.mongoPool as mongoPool
import logout
import neteaseTradeScript.tradeConst as tradeConst
import neteaseTradeScript.timermanager as timermanager
import server.extraServiceApi as serviceApi

ServiceSystem = serviceApi.GetServiceSystemCls()


class TradeServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		if not self.InitMysqlPool():
			return
		if not self.InitTradeCfg():
			return
		# service进程虽然是逻辑单点，但并不是只能启动一个进程
		# 公共service模块支持在任意一个service进程中初始化
		# 是否提供服务，在代码中读取service的模块配置来处理
		# 假如没有读取到对应的配置key（模块对应的是neteaseTrade）
		# 则说明唯一ID模块没有部署在当前的service进程中，那么就不需要初始化服务逻辑了
		self.mActionMgrs = {}
		for moduleName in serviceConf.get_module_names():
			if moduleName.startswith(tradeConst.ModName):
				mgr = self.CreateTradeMgr(moduleName)
				self.mActionMgrs[moduleName] = mgr

	def CreateTradeMgr(self, moduleName):
		from neteaseTradeScript.tradeMgr import TradeMgr
		return TradeMgr(self, moduleName)

	# service的关闭
	# 需要调用数据库连接池的finish函数
	def Destroy(self):
		for mgr in self.mActionMgrs.itervalues():
			mgr.Destroy()
		self.mActionMgrs.clear()
		mysqlPool.Finish()
		# mongoPool.Finish()
		# ServiceSystem.Destroy(self)
		super(TradeServiceSystem, self).Destroy()

	def Update(self):
		timermanager.timerManager.tick()

	# 初始化mysql连接池
	def InitMysqlPool(self):
		try:
			mysqlPool.InitDB(44)
		except:
			logout.error("Exception in InitMysqlPool")
			return False
		return True

	# def InitMongoPool(self):
	# 	try:
	# 		mongoPool.InitDB(44)
	# 	except:
	# 		logout.error("Exception in InitMongoPool")
	# 		return False
	# 	return True

	def InitTradeCfg(self):
		import apolloCommon.commonNetgameApi as commonNetgameApi
		cfg = commonNetgameApi.GetModJsonConfig("neteaseTradeScript")
		if not cfg:
			logout.error("nothing in InitTradeCfg")
			return False
		self.mDoughs = {dough['dough_id']: dough for dough in cfg[tradeConst.CfgKeyDoughs]}
		self.mGroceries = {grocery['grocery_id']: grocery for grocery in cfg[tradeConst.CfgKeyGroceries]}
		self.mSales = cfg[tradeConst.CfgKeySales]
		self.mSaleRules = {
			'merchcount': self.mSales['merch_count_limit'],
			'currencyoptions': [[k, self.mDoughs[k]['dough_icon'], self.mDoughs[k]['dough_desc']] for k in self.mSales['sale_doughs']],
			'timelimit': self.mSales['sale_time_limit'],
			'unitlimit': self.mSales['unit_price_limit'],
			'hourlyfee': self.mSales['hourly_fee'],
			'feetype': self.mDoughs[self.mSales['fee_dough']]['dough_icon'],
		}
		return True

	def GetTradeCfg(self):
		return self.mDoughs, self.mGroceries

	def GetSaleCfg(self):
		return self.mSales

	def GetSaleRules(self):
		return self.mSaleRules
