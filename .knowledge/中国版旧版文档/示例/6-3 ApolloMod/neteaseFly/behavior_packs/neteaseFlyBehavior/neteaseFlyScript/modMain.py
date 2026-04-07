 # -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseFlyScript.flyClientConsts import (ClientSystemClsPath,
                                              ClientSystemName, ModNameSpace,
                                              ModVersion)


@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseFlyClient(object):
	def __init__(self):
		pass

	@Mod.InitClient()
	def initClient(self):
		print '===========================neteaseFly initClient==============================='
		import client.extraClientApi as extraClientApi
		self.mClientSystem = extraClientApi.RegisterSystem(ModNameSpace, ClientSystemName, ClientSystemClsPath)

	@Mod.DestroyClient()
	def destroyClient(self):
		print '===========================neteaseFly destroyClient==============================='
