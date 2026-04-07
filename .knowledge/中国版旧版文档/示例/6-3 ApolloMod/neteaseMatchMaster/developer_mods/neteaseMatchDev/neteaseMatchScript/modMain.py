# -*- coding: utf-8 -*-

from common.mod import Mod
import neteaseMatchScript.masterConsts as masterConsts
import server.extraMasterApi as extraMasterApi

@Mod.Binding(name=masterConsts.ModName, version=masterConsts.ModVersion)
class NeteaseMatchMaster(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initMaster(self):
		print '===========================NeteaseMatchMaster initMaster==============================='
		self.mServiceSystem = extraMasterApi.RegisterSystem(masterConsts.ModName, masterConsts.MasterSystemName,
					masterConsts.MasterSystemClsPath)

	@Mod.DestroyMaster()
	def destroyMaster(self):
		print '===========================NeteaseMatchMaster destroyMaster==============================='