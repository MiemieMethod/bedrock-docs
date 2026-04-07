# -*- coding: utf-8 -*-

from common.mod import Mod
import guildConsts as guildConsts


@Mod.Binding(name=guildConsts.ModNameSpace, version=guildConsts.ModVersion)
class NeteaseGuildService(object):
	def __init__(self):
		pass
	
	@Mod.InitService()
	def initService(self):
		print '===========================neteaseGuild initService==============================='
		import server.extraServiceApi as serviceApi
		self.mServiceSystem = serviceApi.RegisterSystem(guildConsts.ModNameSpace, guildConsts.ServiceSystemName, guildConsts.ServiceSystemClsPath)
	
	@Mod.DestroyService()
	def destroyService(self):
		print '===========================neteaseGuild destroyService==============================='