# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi
import logout
from awesomeScripts.modCommon import modConfig

'''
网络游戏进阶 demo mod：从mysql或mongo读取的玩家信息
'''

@Mod.Binding(name = modConfig.LobbyServerModName, version = "0.1")
class LobbyMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def initServer(self):
		#加载mod入口
		logout.info('===========================init_LobbyMod_mod!===============================')
		self.server = serverApi.RegisterSystem(modConfig.Minecraft, modConfig.LobbyServerSystemName, modConfig.LobbyServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyServer(self):
		#退出游戏时注销mod
		logout.info('destroy_server===============')