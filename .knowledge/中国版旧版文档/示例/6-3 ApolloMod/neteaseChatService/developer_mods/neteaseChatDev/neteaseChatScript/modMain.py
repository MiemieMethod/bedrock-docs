# -*- coding: utf-8 -*-

from common.mod import Mod
import chatConsts as chatConsts


@Mod.Binding(name=chatConsts.ModNameSpace, version=chatConsts.ModVersion)
class NeteaseChatService(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initService(self):
		print '===========================neteaseChat initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(chatConsts.ModNameSpace, chatConsts.ServiceSystemName, chatConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseChat destroyService==============================='