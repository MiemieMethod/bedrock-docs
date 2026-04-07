# -*- coding: utf-8 -*-
#
from common.mod import Mod
import guildConsts as guildConsts


@Mod.Binding(name=guildConsts.ModNameSpace, version=guildConsts.ModVersion)
class AuthMasterMod(object):
	def __init__(self):
		pass
	
	@Mod.InitMaster()
	def initMaster(self):
		print '===========================init_GuildMaster!==============================='
		import server.extraMasterApi as extraMasterApi
		self.server = extraMasterApi.RegisterSystem(guildConsts.ModNameSpace, guildConsts.MasterSystemName,
		                                            guildConsts.MaterSystemClsPath)
	
	@Mod.DestroyMaster()
	def destroyMaster(self):
		print 'destroy_master==============='