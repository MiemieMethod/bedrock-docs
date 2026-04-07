# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseFlyScript.flyServerConsts import (ModNameSpace, ModVersion,
                                              ServerSystemClsPath,
                                              ServerSystemName)


@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseFlyServer(object):
	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseFly initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(ModNameSpace, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================neteaseFly destroyServer==============================='
