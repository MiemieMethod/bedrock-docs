# -*- coding: utf-8 -*-

from common.mod import Mod
import chatConsts as chatConsts


@Mod.Binding(name=chatConsts.ModNameSpace, version=chatConsts.ModVersion)
class NeteaseChatClient(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseChat initClient==============================='
		import client.extraClientApi as clientApi
		self.mClentSystem = clientApi.RegisterSystem(chatConsts.ModNameSpace, chatConsts.ClientSystemName, chatConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseChat destroyClient==============================='