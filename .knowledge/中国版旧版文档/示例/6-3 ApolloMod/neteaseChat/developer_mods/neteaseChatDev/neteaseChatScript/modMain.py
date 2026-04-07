# -*- coding: utf-8 -*-

from common.mod import Mod
import chatConsts as chatConsts


@Mod.Binding(name=chatConsts.ModNameSpace, version=chatConsts.ModVersion)
class NeteaseChatServer(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseChat initServer==============================='
		import server.extraServerApi as serverApi
		self.mServerSystem = serverApi.RegisterSystem(chatConsts.ModNameSpace, chatConsts.ServerSystemName, chatConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print '===========================neteaseChat destroyServer==============================='