# -*- coding: utf-8 -*-
from common.mod import Mod
import server.extraServerApi as serverApi
import guildConsts as guildConsts


@Mod.Binding(name=guildConsts.ModNameSpace, version=guildConsts.ModVersion)
class GuildServerMod(object):
	def __init__(self):
		pass
	
	@Mod.InitServer()
	def initServer(self):
		print '===========================init_GuildServer!==============================='
		self.server = serverApi.RegisterSystem(guildConsts.ModNameSpace, guildConsts.ServerSystemName,
		                                       guildConsts.ServerSystemClsPath)
	
	@Mod.DestroyServer()
	def destroyServer(self):
		print 'destroy_server==============='