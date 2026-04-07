# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "CustomCropMod", version = "1.0")
class CustomCropMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		serverApi.RegisterSystem("CustomCrop", "CustomCropServer", "customCropScripts.customCropServer.CustomCropServer")

	@Mod.InitClient()
	def init(self):
		clientApi.RegisterSystem("CustomCrop", "CustomCropClient", "customCropScripts.customCropClient.CustomCropClient")