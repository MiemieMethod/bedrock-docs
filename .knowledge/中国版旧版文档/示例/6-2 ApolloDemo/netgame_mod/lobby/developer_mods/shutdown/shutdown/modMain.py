# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi

'''
开服工具必须Mod
响应Master发送的优雅关机、强制关机、强制更新公告配置指令
用于服务器的滚动更新
'''


@Mod.Binding(name = "SHUTDOWN", version = "0.1")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_shutdown_mod!==============================='
		self.server = serverApi.RegisterSystem("Minecraft", "demoShutdownServer", "shutdown.shutdownServer.ShutDownServer")

	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='
		
	@Mod.InitClient()
	def initClient(self):
		pass
		
	@Mod.DestroyClient()
	def destroyClient(self):
		pass
