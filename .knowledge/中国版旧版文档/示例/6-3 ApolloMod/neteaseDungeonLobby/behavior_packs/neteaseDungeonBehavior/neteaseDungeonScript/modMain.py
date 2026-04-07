# -*- coding: utf-8 -*-
#
from common.mod import Mod
import client.extraClientApi as extraClientApi
import neteaseDungeonScript.dungeonConsts as dungeonConsts

@Mod.Binding(name=dungeonConsts.ModNameSpace, version=dungeonConsts.ModVersion)
class DungeonClientMod(object):
	def __init__(self):
		pass
	
	@Mod.InitClient()
	def initClient(self):
		print '===========================init_DungeonClientMod!==============================='
		self.client = extraClientApi.RegisterSystem(dungeonConsts.ModNameSpace, dungeonConsts.LobbyClientSystemName,
											   dungeonConsts.ClientSystemClsPath)
	
	@Mod.DestroyClient()
	def destroyClient(self):
		print 'destroy_DungeonClientMod==============='