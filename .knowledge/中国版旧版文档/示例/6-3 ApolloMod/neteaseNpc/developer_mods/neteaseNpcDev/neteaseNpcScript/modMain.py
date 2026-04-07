# -*- coding: utf-8 -*-
#

from common.mod import Mod
import server.extraServerApi as serverApi

@Mod.Binding(name = "neteaseNpcDev", version = "1.0.4")
class NpcServerMod(object):
	def __init__(self):
		pass
		
	@Mod.InitServer()
	def InitServer(self):
		print '===========================init_NpcServer!==============================='
		self.server = serverApi.RegisterSystem("neteaseNpc", "npcServer", "neteaseNpcScript.neteaseNpcSystem.NpcServerSystem")

	@Mod.DestroyServer()
	def DestroyServer(self):
		print 'destroy_server==============='