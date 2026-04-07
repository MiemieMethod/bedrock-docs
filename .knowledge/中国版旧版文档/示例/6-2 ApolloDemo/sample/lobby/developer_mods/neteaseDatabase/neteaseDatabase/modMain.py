# -*- coding: utf-8 -*-
#

from common.mod import Mod
import server.extraServerApi as serverApi
import logout

'''
通过python访问redis或mysql数据库的示例
使用数据库存取引擎玩家原始存档的示例
使用异步线程模块驱动异步IO逻辑的示例

使用此示例mod后，玩家存档不再存储在本地，而是远程数据库
适用于同类但是不同进程的服务器，共享同一份玩家存档（比如说背包物品）
'''


@Mod.Binding(name = "neteaseDatabase", version = "0.1")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		logout.info('===========================init_database_mod!===============================')
		self.server = serverApi.RegisterSystem("Minecraft", "demoDatabaseServer", "neteaseDatabase.databaseServer.DatabaseServer")

	@Mod.DestroyServer()
	def destroyServer(self):
		logout.info('destroy_server===============')
		
	@Mod.InitClient()
	def initClient(self):
		pass
		
	@Mod.DestroyClient()
	def destroyClient(self):
		pass
