# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "CustomRangedWeaponMod", version = "1.0")
class CustomRangedWeaponMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		print 'InitServer'
		serverApi.RegisterSystem("CustomRangedWeapon", "CustomRangedWeaponServer", "customRangedWeaponScripts.customRangedWeaponServer.CustomRangedWeaponServer")

	@Mod.InitClient()
	def init(self):
		print 'InitClient'
		clientApi.RegisterSystem("CustomRangedWeapon", "CustomRangedWeaponClient", "customRangedWeaponScripts.customRangedWeaponClient.CustomRangedWeaponClient")