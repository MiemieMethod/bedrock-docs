# -*- coding: utf-8 -*-
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
import service.serviceConf as serviceConf
import logout
import neteaseDungeonScript.dungeonConsts as dungeonConsts
import neteaseDungeonScript.dungeon as dungeon

class DungeonServiceSystem(ServiceSystem):
	def __init__(self, namespace, systemName):
		ServiceSystem.__init__(self, namespace, systemName)
		self.mDungeonMgr = dungeon.DungeonManager(self)

	def Destroy(self):
		self.mDungeonMgr.Destroy()