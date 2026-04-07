# -*- coding: utf-8 -*-
from common.mod import Mod
import server.extraServerApi as serverApi
import shopConsts as shopConsts

@Mod.Binding(name = shopConsts.ModNameSpace, version = shopConsts.ModVersion)
class ShopServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_ShopServer!==============================='
		self.server = serverApi.RegisterSystem(shopConsts.ModNameSpace, shopConsts.ServerSystemName, shopConsts.ServerSystemClsPath)
		#这个是system做示例用
		#serverApi.RegisterSystem(shopConsts.ModNameSpace, shopConsts.TestServerSystemName, shopConsts.TestServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='