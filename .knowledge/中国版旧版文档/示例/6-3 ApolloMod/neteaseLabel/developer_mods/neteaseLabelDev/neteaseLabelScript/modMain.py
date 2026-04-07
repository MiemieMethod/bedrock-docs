# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from neteaseLabelScript.labelConst import ModVersion, ModName, ServerSystemName, ServerSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseLabelServer(object):
	@Mod.InitServer()
	def LabelServerInit(self):
		print '==== neteaseLabel initServer ===='
		serverApi.RegisterSystem(ModName, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def LabelServerDestroy(self):
		print '==== neteaseLabel destroyServer ===='
