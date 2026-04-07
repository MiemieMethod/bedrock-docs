# -*- coding: utf-8 -*-

from common.mod import Mod
from awesomeScripts.modCommon import modConfig

@Mod.Binding(name=modConfig.ServiceSystemName, version="0.1")
class ServiceMod(object):
	def __init__(self):
		pass

	@Mod.InitService()
	def initService(self):
		'''
		加载service mod入口
		'''
		print '===========================ServiceMod initService==============================='
		# 注册service的system
		import server.extraServiceApi as serviceApi
		self.server = serviceApi.RegisterSystem(modConfig.Minecraft, modConfig.ServiceSystemName, modConfig.ServiceServerSystemClsPath)

	@Mod.DestroyService()
	def destroyService(self):
		'''
		退出游戏时注销mod
		'''
		print '===========================ServiceMod destroyService==============================='