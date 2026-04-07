# -*- coding: utf-8 -*-
#
from common.mod import Mod
import server.extraServerApi as serverApi
import chestConsts as chestConsts

@Mod.Binding(name=chestConsts.ModNameSpace, version=chestConsts.ModVersion)
class ChestServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_ChestServer!==============================='
		self.server = serverApi.RegisterSystem(chestConsts.ModNameSpace, chestConsts.ServerSystemName, chestConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='