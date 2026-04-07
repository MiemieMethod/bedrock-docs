# -*- coding: utf-8 -*-
#
import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
import netgame_api
import logout

class ShutDownServer(ServerSystem):
	def __init__(self, namespace, systemName):
		ServerSystem.__init__(self, namespace, systemName)
		# 脚本内标识
		self.frame_count = 0
		self.on_grace_shutdown = False
		self.on_force_shutdown = False
		logout.info('--------ShutDownServer====start!!!!!~~~~~')
		# 注册事件
		# 【接收到Master的优雅关机指令】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterGraceShutDownEvent', self, self.OnGraceShutDown)
		# 【接收到Master的强制关机指令】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterForceShutDownEvent', self, self.OnForceShutDown)
		# 【接收到Master的公共配置更新指令，并已经从网络获取了最新的公共配置】
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ReloadCommonConfigEvent', self, self.OnReloadCommonConfig)
		
	def Destroy(self):
		logout.info('--------ShutDownServer====destroy!!!!!~~~~~')
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterGraceShutDownEvent', self, self.OnGraceShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterForceShutDownEvent', self, self.OnForceShutDown)
		self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ReloadCommonConfigEvent', self, self.OnReloadCommonConfig)
	
	# 脚本逻辑帧
	def Update(self):
		# 假如进入到优雅关机状态
		if self.on_grace_shutdown:
			self.frame_count += 1
			if self.frame_count % 10 == 0:
				# 获取当前在线玩家数量--进入优雅关机状态后，Master不会分配新玩家到此服务器进程
				num = netgame_api.get_online_player_num()
				# 假如玩家已经都离线了，则告知引擎脚本层关机准备已经完成
				if num <= 0:
					netgame_api.set_graceful_shutdown_ok()
	
	# 接收到Master的优雅关机指令
	def OnGraceShutDown(self, data):
		logout.info("===================OnGraceShutDown")
		self.on_grace_shutdown = True
	
	# 接收到Master的强制关机指令
	def OnForceShutDown(self, data):
		logout.info("===================OnForceShutDown")
		self.on_force_shutdown = True
		# 最简单的逻辑，直接告知引擎脚本层关机准备已经完成
		netgame_api.set_shutdown_ok()
	
	# 接收到Master的公共配置更新指令
	# 此时引擎层已经从网络获取了最新的公共配置
	# 脚本可以通过相关的接口函数获取最新的配置信息。比如说数据库连接参数
	def OnReloadCommonConfig(self, data):
		logout.info("===================OnReloadCommonConfig")
		num = netgame_api.get_online_player_num()
		logout.info("player num=%s" % num)
		
		
		
		