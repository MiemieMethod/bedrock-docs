# -*- coding: utf-8 -*-

from common.mod import Mod
import friendConsts as friendConsts


@Mod.Binding(name=friendConsts.ModNameSpace, version=friendConsts.ModVersion)
class NeteaseFriendClient(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseFriend initClient==============================='
		import client.extraClientApi as clientApi
		self.mClentSystem = clientApi.RegisterSystem(friendConsts.ModNameSpace, friendConsts.ClientSystemName, friendConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseFriend destroyClient==============================='