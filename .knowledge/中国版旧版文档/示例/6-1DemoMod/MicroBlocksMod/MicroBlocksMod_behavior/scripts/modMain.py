# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "MicroBlocksMod", version = "1.0")
class CustomBlocksMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		serverApi.RegisterSystem("MicroBlocks", "MicroBlocksServer", "scripts.microBlocksServer.MicroBlocksServer")

	@Mod.InitClient()
	def init(self):
		clientApi.RegisterSystem("MicroBlocks", "MicroBlocksClient", "scripts.microBlocksClient.MicroBlocksClient")