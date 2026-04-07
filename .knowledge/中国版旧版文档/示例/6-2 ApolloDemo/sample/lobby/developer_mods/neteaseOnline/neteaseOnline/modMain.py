# -*- coding: utf-8 -*-
#

from common.mod import Mod
import server.extraServerApi as serverApi
import logout

'''
开服工具必须Mod
使用redis维护玩家在整组服务器中的在线状态
'''

@Mod.Binding(name = "neteaseOnline", version = "0.1")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		logout.info('===========================init_online_mod!===============================')
		self.server = serverApi.RegisterSystem("Minecraft", "demoOnlineServer", "neteaseOnline.onlineServer.OnlineServer")

	@Mod.DestroyServer()
	def destroyServer(self):
		logout.info('destroy_server===============')
		
	@Mod.InitClient()
	def initClient(self):
		pass
		
	@Mod.DestroyClient()
	def destroyClient(self):
		pass
