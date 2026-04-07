# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseAnnounceScript.announceConsts import ModVersion, ModNameSpace, ServiceSystemName, ServiceSystemClsPath

def LoadJsonConfig():
	import apolloCommon.commonNetgameApi as commonNetgameApi
	config = commonNetgameApi.GetModJsonConfig("neteaseAnnounceScript")
	if not config:
		return
	import neteaseAnnounceScript.announceConsts as announceConsts
	for keyword in announceConsts.ConfigurableDefineList:
		print "check %s" % keyword
		if config.has_key(keyword):
			setattr(announceConsts, keyword, config[keyword])
			print "change %s to %s" % (keyword, getattr(announceConsts, keyword))
	announceConsts.ReloadErrorText()

@Mod.Binding(name=ModNameSpace, version=ModVersion)
class NeteaseAnnounceService(object):
	def __init__(self):
		LoadJsonConfig()

	@Mod.InitService()
	def initService(self):
		print '===========================neteaseAnnounce initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(ModNameSpace, ServiceSystemName, ServiceSystemClsPath)

	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseAnnounce destroyService==============================='