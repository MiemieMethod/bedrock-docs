# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseAnnounceScript.announceConsts import ModVersion, ModNameSpace, MasterSystemName, MasterSystemClsPath

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseAnnounceMaster(object):
	def __init__(self):
		pass

	@Mod.InitMaster()
	def initService(self):
		print '===========================neteaseAnnounce initMaster==============================='
		import server.extraMasterApi as extraMasterApi
		self.mServiceSystem = extraMasterApi.RegisterSystem(ModNameSpace, MasterSystemName, MasterSystemClsPath)

	@Mod.DestroyMaster()
	def destroyService(self):
		print '===========================neteaseAnnounce destroyMaster==============================='