# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseUniqueIdScript.uniqueIdConsts import ModVersion, ModNameSpace, ServiceSystemName, ServiceSystemClsPath
import logout

def LoadJsonConfig():
	import neteaseUniqueIdScript.uniqueIdConsts as uniqueIdConsts
	import apolloCommon.commonNetgameApi as commonNetgameApi
	config = commonNetgameApi.GetModJsonConfig("neteaseUniqueIdScript")
	if not config:
		return
	for keyword in uniqueIdConsts.ConfigurableDefineList:
		logout.info("check %s" % keyword)
		if config.has_key(keyword):
			setattr(uniqueIdConsts, keyword, config[keyword])
			logout.info("change %s to %s" % (keyword, getattr(uniqueIdConsts, keyword)))
	uniqueIdConsts.ReloadErrorText()

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseUniqueIdService(object):
	def __init__(self):
		LoadJsonConfig()

	@Mod.InitService()
	def initService(self):
		print '===========================neteaseUniqueId initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(ModNameSpace, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseUniqueId destroyService==============================='