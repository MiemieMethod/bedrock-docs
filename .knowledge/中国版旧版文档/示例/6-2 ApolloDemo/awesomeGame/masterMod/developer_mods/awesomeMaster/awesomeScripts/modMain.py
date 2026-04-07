# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from mod_log import logger
from awesomeScripts.modCommon import modConfig

@Mod.Binding(name=modConfig.MasterModName,version="0.1")
class masterMod(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initMaster(self):
		'''
		加载master mod入口
		'''
		logger.info('===========================init_masterMod!===============================')
		self.server = masterApi.RegisterSystem(modConfig.Minecraft, modConfig.MasterSystemName, modConfig.MasterServerSystemClsPath)

	@Mod.DestroyMaster()
	def destroyMaster(self):
		'''
		退出游戏时注销mod
		'''
		print '######################################destroy masterMod################'