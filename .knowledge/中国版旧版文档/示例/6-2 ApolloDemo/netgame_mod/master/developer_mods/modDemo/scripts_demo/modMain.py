# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from master.masterConf import netgameConf
import netease_server.mysqlpool as mysqlpool
import netease_server.redispool as redispool
MasterSystem = masterApi.GetMasterSystemCls()
from netease_server.async_task_pool import asyncTaskPool
'''
master mod。
部署：按照公共配置创建mysql Database，然后执行mysql.sql，创建表格并插入测试数据。
功能：包含登录顶号、gm指令、排行榜、房间匹配等。
	房间匹配只支持申请匹配、取消匹配等功能。
mysql和redis线程池初始化和释放都在这里进行，注意，多次释放会导致错误。
'''

@Mod.Binding(name="demo",version="0.1")
class demoMod(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initMaster(self):
		print 'initServer ######################################initServer###############'
		#异步任务线程池，大小为30。
		asyncTaskPool.set_pool_size(30)
		#netgameConf以dict记录公共配置netgame_common.json内容。
		redisConf = netgameConf['redis']
		#初始化redis线程池，大小为30。redis和mysql线程池都是以asyncTaskPool为基础实现的。
		redispool.init(redisConf['host'], redisConf['port'], redisConf['password'], 30)
		mysqlConf = netgameConf['mysql']
		#初始化mysql线程池，大小为30.redis和mysql线程池都是以asyncTaskPool为基础实现的。
		mysqlpool.init(mysqlConf['host'], mysqlConf['port'], mysqlConf['user'], mysqlConf['password']
		               ,mysqlConf['database'], 30)
		#注册system
		self.asyncTaskSys = masterApi.RegisterSystem("Minecraft", "asyncTask", "scripts_demo.asyncTaskSysServer.AsyncTaskSysServer")
		self.serverHandlerSys = masterApi.RegisterSystem("Minecraft", "ServerSys", "scripts_demo.serverHandlerSys.ServerHandlerSys")
		self.rankSys = masterApi.RegisterSystem("idv", "RankSys", "scripts_demo.syncRankSystem.SyncRankSystem")
		self.matchSys = masterApi.RegisterSystem("idv", "masterMatch", "scripts_demo.matchSystem.MatchSystem")

	#会在所有system Destroy之后执行。确保是最后执行的。
	@Mod.DestroyMaster()
	def destroyMaster(self):
		print '######################################destroyMod################'
		#清理资源。
		redispool.finish()
		mysqlpool.finish()
		asyncTaskPool.finish(None)