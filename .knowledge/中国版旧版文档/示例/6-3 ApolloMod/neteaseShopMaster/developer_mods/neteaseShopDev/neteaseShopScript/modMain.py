# -*- coding: utf-8 -*-

from common.mod import Mod
import shopConsts as shopConsts

@Mod.Binding(name = shopConsts.ModNameSpace, version = shopConsts.ModVersion)
class NeteaseShopMaster(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initMaster(self):
		print '===========================neteaseShop initMaster==============================='
		import server.extraMasterApi as extraMasterApi
		self.mServiceSystem = extraMasterApi.RegisterSystem(shopConsts.ModNameSpace, shopConsts.MasterSystemName, shopConsts.MasterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyMaster(self):
		print '===========================neteaseShop destroyMaster==============================='