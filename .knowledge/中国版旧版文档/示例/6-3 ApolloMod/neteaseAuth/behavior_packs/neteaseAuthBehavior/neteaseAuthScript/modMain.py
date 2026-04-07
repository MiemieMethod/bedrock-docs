 # -*- coding: utf-8 -*-

from common.mod import Mod
import authConsts as authConsts

@Mod.Binding(name = authConsts.ModNameSpace, version = authConsts.ModVersion)
class NeteaseAuthClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================NeteaseAuthClient initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(authConsts.ModNameSpace,
				authConsts.ClientSystemName, authConsts.ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================NeteaseAuthClient destroyClient==============================='