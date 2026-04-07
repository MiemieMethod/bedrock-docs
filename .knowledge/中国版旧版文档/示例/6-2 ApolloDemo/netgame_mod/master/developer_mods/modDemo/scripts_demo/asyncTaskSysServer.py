# -*- coding: utf-8 -*-
from netease_server.async_task_pool import asyncTaskPool
import server.system.serverSystem as modSysServer
''' 
异步任务的tick。
'''
class AsyncTaskSysServer(modSysServer.ServerSystem):
	def __init__(self, namespace, name):
		modSysServer.ServerSystem.__init__(self, namespace, name)
	#每帧都会执行。
	def Update(self):
		import netease_server.mysqlpool as mysqlpool
		import netease_server.redispool as redispool
		asyncTaskPool.schedule()
		redispool.tick()
		mysqlpool.tick()

	def Destroy(self):
		print 'Destroy #########yyyyyyyyyyyyyyyyyyyyyyyyyyy#######AsyncTaskSysServer################'
		modSysServer.ServerSystem.Destroy(self)