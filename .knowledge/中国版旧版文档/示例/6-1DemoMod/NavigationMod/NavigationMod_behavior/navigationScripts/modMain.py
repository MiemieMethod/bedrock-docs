# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "NavigationMod", version = "1.0")
class NavigationMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		serverApi.RegisterSystem("NavigationMod", "NavigationServer", "navigationScripts.NavigationServerSystem.NavigationServerSystem")
