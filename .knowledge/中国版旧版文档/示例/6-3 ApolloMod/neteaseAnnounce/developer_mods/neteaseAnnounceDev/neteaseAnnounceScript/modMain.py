# -*- coding: utf-8 -*-

from common.mod import Mod
from neteaseAnnounceScript.announceConsts import ModVersion, ModNameSpace, ServerSystemName, ServerSystemClsPath

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
class NeteaseAnnounceServer(object):
	def __init__(self):
		LoadJsonConfig()

	@Mod.InitServer()
	def initServer(self):
		print '===========================neteaseAnnounce initServer==============================='
		import server.extraServerApi as extraServerApi
		self.mServerSystem = extraServerApi.RegisterSystem(ModNameSpace, ServerSystemName, ServerSystemClsPath)

	@Mod.DestroyServer()
	def destroyService(self):
		print '===========================neteaseAnnounce destroyServer==============================='