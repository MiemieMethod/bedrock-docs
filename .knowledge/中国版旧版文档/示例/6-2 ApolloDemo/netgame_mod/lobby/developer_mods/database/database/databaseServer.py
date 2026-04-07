# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import netgame_api
import workerpool

import callplayerdata

class DatabaseServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		print '--------DatabaseServer====start!!!!!~~~~~'
		# 创建多线程模块，设置最多同时3个线程
		self.work_pool = workerpool.fork_new_pool(3)
		# 设置使用数据库存储引擎玩家原始存档，关键字前缀为netgame，每15秒触发定时存档
		netgame_api.set_use_database_save(True, "netgame", 15)
		# 读取公共配置中填写的redis连接参数和mysql连接参数配置
		callplayerdata.read_redis_config()
		callplayerdata.read_mysql_config()
		# 注册事件
		# 【服务器即将关闭】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		# 【玩家登陆，需要从数据库读取玩家存档】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'queryPlayerDataEvent', self, self.OnQueryPlayerData)
		# 【玩家离线/被踢，需要把玩家存档存储到数据库】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'savePlayerDataEvent', self, self.OnSavePlayerData)
		# 【服务器关机，需要把当前还在线的玩家的存档存储到数据库】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'savePlayerDataOnShutDownEvent', self, self.OnShutDownSavePlayerData)
	
	def Destroy(self):
		print '--------DatabaseServer====destroy!!!!!~~~~~'
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerWillShutDownEvent', self, self.OnServerWillShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'queryPlayerDataEvent', self, self.OnQueryPlayerData)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'savePlayerDataEvent', self, self.OnSavePlayerData)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'savePlayerDataOnShutDownEvent', self, self.OnShutDownSavePlayerData)
	
	# 服务器即将关闭的消息
	# 需要让所有的异步线程函数都执行完毕
	# 并且返回所有数据库的回调
	def OnServerWillShutDown(self, data):
		print "------------------OnServerWillShutDown"
		if self.work_pool:
			self.work_pool.finish(timeout=5.0)
			self.work_pool = None

	# 服务器逻辑帧，需要调用多线程模块的逻辑帧
	def Update(self):
		# print '--------DatabaseServer====Update!!!!!~~~~~'
		if self.work_pool:
			self.work_pool.schedule()
		
	# 玩家登陆，需要从数据库读取玩家存档
	def OnQueryPlayerData(self, data):
		print "============OnQueryPlayerData", data
		# 使用自己设置的前缀+玩家key的形式生成存档的key
		# 支持不同的游戏模式使用不同的存档
		# 相同的游戏模式但是进程不同的情况下存档又是统一的
		redis_key = data["dbName"] + "_" + data["playerKey"]
		print "redis_key =", redis_key
		# emit_order(key, func, callback, *args)
		# key：string -- 多线程执行中相同key的函数将会按照调用emit的顺序依序执行
		# func：function -- 需要在子线程运行的函数
		# callback：function -- 子线程函数执行完毕后的回调函数
		# *args：params -- func函数的参数
		# 备注：回调函数的参数，强制设置为func函数的返回值
		self.work_pool.emit_order(
			data["playerKey"], 
			# callplayerdata.mysql_query_playerdata,
			callplayerdata.redis_query_playerdata, 
			self.QueryPlayerDataCallback, 
			int(data["idx"]), redis_key)
	
	# 数据库查询的回调函数，因为调用了C++提供的函数，所以只能在python主线程中执行
	def QueryPlayerDataCallback(self, idx, suc, data):
		print "QueryPlayerDataCallback", suc
		netgame_api.query_player_data_result(idx, suc, data)
		
	# 玩家离线/被踢，需要把玩家存档存储到数据库
	def OnSavePlayerData(self, data):
		print "============OnSavePlayerData"
		# 使用自己设置的前缀+玩家key的形式生成存档的key
		redis_key = data["dbname"] + "_" + data["playerKey"]
		print "redis_key =", redis_key, len(data["playerData"])
		self.work_pool.emit_order(
			data["playerKey"], 
			# callplayerdata.mysql_save_playerdata,
			callplayerdata.redis_save_playerdata, 
			self.SavePlayerDataCallback, 
			int(data["idx"]), redis_key, data["playerData"])
		
	# 存档结果返回给引擎层
	def SavePlayerDataCallback(self, idx, suc):
		print "SavePlayerDataCallback", suc
		netgame_api.save_player_data_result(idx, suc)
	
	# 服务器关机，需要把当前还在线的玩家的存档存储到数据库
	# 在这个时间节点，其实多线程模块已经调用过finish和自我销毁了
	# 这个事件之后引擎会顺序执行走到关机逻辑
	# 所以只能使用同步调用的方式存档数据
	def OnShutDownSavePlayerData(self, data):
		print "============OnShutDownSavePlayerData"
		redis_key = data["dbname"] + "_" + data["playerKey"]
		print "redis_key =", redis_key, len(data["playerData"])
		# idx, suc = callplayerdata.mysql_save_playerdata(int(data["idx"]), redis_key, data["playerData"])
		idx, suc = callplayerdata.redis_save_playerdata(int(data["idx"]), redis_key, data["playerData"])
		netgame_api.save_player_data_result(idx, suc)
		print "============OnShutDownSavePlayerData fin"
		
		
		
		
		