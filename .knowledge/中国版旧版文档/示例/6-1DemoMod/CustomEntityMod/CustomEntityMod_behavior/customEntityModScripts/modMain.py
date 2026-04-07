# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = 'customEntityMod', version = "1.0")
class MyMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		testServer = serverApi.RegisterSystem('customEntityMod', 'customEntityServerSystem', "customEntityModScripts.customEntityServerSystem.CustomEntityServerSystem")

	@Mod.InitClient()
	def initClient(self):
		testClient = clientApi.RegisterSystem('customEntityMod', 'customEntityClientSystem', "customEntityModScripts.customEntityClientSystem.CustomEntityClientSystem")