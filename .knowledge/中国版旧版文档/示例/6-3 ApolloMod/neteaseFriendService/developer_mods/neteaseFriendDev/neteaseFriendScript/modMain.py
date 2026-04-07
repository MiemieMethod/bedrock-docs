# -*- coding: utf-8 -*-

from common.mod import Mod
import friendConsts as friendConsts


@Mod.Binding(name=friendConsts.ModNameSpace, version=friendConsts.ModVersion)
class NeteaseFriendService(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initService(self):
		print '===========================neteaseFriend initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(friendConsts.ModNameSpace, friendConsts.ServiceSystemName, friendConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseFriend destroyService==============================='