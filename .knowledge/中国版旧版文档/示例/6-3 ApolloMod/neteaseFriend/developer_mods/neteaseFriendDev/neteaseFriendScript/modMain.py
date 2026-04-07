# -*- coding: utf-8 -*-

from common.mod import Mod
import friendConsts as friendConsts


@Mod.Binding(name=friendConsts.ModNameSpace, version=friendConsts.ModVersion)
class NeteaseFriendServer(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseFriend initServer==============================='
		import server.extraServerApi as serverApi
		self.mServerSystem = serverApi.RegisterSystem(friendConsts.ModNameSpace, friendConsts.ServerSystemName, friendConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print '===========================neteaseFriend destroyServer==============================='