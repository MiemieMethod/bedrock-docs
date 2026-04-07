# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import netgame_api
import logout
import netease_server.redispool as redispool

import sqlDealOnline

class OnlineServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print '--------OnlineServer====start!!!!!~~~~~'
		# 创建redis连接池，设置最多同时30个线程
		suc, host, port, pwd = netgame_api.get_redis_config()
		if suc:
			redispool.init(host, port, pwd, 30)
		else:
			logout.error("[DATABASE_ERROR] redis db not exist; server will not do right thing!")
		# 注册事件
		# 【服务器即将关闭】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		# 【玩家上线，需要在redis记录在线标识】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerGetPlayerLockEvent', self, self.OnGetPlayerLock)
		# 【玩家离线/被踢，需要清理redis中的在线标识】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerReleasePlayerLockEvent', self, self.OnReleasePlayerLock)
		# 【服务器关机，需要清理当前在线玩家的在线标识】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerReleasePlayerLockOnShutDownEvent', self, self.OnShutDownReleasePlayerLock)
	
	def Destroy(self):
		print '--------OnlineServer====destroy!!!!!~~~~~'
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerGetPlayerLockEvent', self, self.OnGetPlayerLock)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerReleasePlayerLockEvent', self, self.OnReleasePlayerLock)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerReleasePlayerLockOnShutDownEvent', self, self.OnShutDownReleasePlayerLock)
	
	# 服务器即将关闭的消息
	# 需要让所有的异步线程函数都执行完毕
	# 并且返回所有数据库的回调
	def OnServerWillShutDown(self, data):
		print "------------------OnServerWillShutDown"
		redispool.finish()
		
	# 服务器逻辑帧，需要调用多线程模块的逻辑帧
	def Update(self):
		# print '--------DatabaseServer====Update!!!!!~~~~~'
		redispool.tick()
	
	# 玩家上线，需要在redis记录在线标识
	# 写数据库失败，则玩家无法登陆
	def OnGetPlayerLock(self, data):
		print "============OnGetPlayerLock", data
		redispool.async_func_with_key(
			sqlDealOnline.redis_get_player_lock,
			data["uid"],
			self.GetPlayerLockCallback,
			int(data["idx"]), int(data["uid"]), int(data["serverid"]), int(data["proxyid"]))
			
	# 回调函数，因为调用了C++提供的函数，所以只能在python主线程中执行
	def GetPlayerLockCallback(self, args):
		print "============GetPlayerLockCallback", args
		idx, uid, suc = args
		netgame_api.get_player_lock_result(idx, suc)
		
	# 玩家离线/被踢，需要清理redis中的在线标识
	# 可以异步执行和返回
	def OnReleasePlayerLock(self, data):
		print "============OnReleasePlayerLock", data
		# async_func_with_key(func, key, callback, *args)
		# func：function -- 需要在子线程运行的函数
		# key：string -- 多线程执行中相同key的函数将会按照调用emit的顺序依序执行
		# callback：function -- 子线程函数执行完毕后的回调函数
		# *args：params -- func函数的参数
		# 备注：回调函数的参数，强制设置为只有一个，func函数可以以tuple或dict的形式返回复数的值
		redispool.async_func_with_key(
			sqlDealOnline.redis_release_player_lock,
			data["uid"],
			self.ReleasePlayerLockCallback,
			int(data["idx"]), int(data["uid"]))
		print "=======relase fin"
	
	# 回调函数，因为调用了C++提供的函数，所以只能在python主线程中执行
	def ReleasePlayerLockCallback(self, args):
		print "============ReleasePlayerLockCallback", args
		idx, uid, suc = args
		netgame_api.release_player_lock_result(idx, suc)
	
	# 服务器关机，需要清理当前在线玩家的在线标识
	# 在这个时间节点，其实多线程模块已经调用过finish和自我销毁了
	# 这个事件之后引擎会顺序执行走到关机逻辑
	# 所以只能使用同步调用的方式存档数据
	def OnShutDownReleasePlayerLock(self, data):
		print "============OnShutDownReleasePlayerLock", data
		redispool.async_func_with_key(
			sqlDealOnline.redis_release_player_lock,
			data["uid"],
			self.ReleasePlayerLockCallback,
			int(data["idx"]), int(data["uid"]))
		redispool.finish()
		print "============OnShutDownReleasePlayerLock finish"
		
		
		
		