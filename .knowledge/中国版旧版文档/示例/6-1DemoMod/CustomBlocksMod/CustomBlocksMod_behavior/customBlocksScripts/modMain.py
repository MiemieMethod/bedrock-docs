# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "CustomBlocksMod", version = "1.0")
class CustomBlocksMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		serverApi.RegisterSystem("CustomBlocks", "CustomBlocksServer", "customBlocksScripts.customBlocksServer.CustomBlocksServer")

	@Mod.InitClient()
	def init(self):
		clientApi.RegisterSystem("CustomBlocks", "CustomBlocksClient", "customBlocksScripts.customBlocksClient.CustomBlocksClient")