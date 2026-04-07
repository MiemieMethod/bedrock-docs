# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraMasterApi as masterApi
from neteaseLabelScript.labelConst import ModVersion, ModName, MasterSystemName, MasterSystemClsPath


@Mod.Binding(name=ModName, version=ModVersion)
class NeteaseLabelMaster(object):
	@Mod.InitMaster()
	def LabelMasterInit(self):
		print '==== neteaseLabel initMaster ===='
		masterApi.RegisterSystem(ModName, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def LabelMasterDestroy(self):
		print '==== neteaseLabel destroyMaster ===='
