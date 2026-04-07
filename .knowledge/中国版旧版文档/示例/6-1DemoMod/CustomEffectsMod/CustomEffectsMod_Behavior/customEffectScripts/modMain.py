# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
import modCommon.modConfig as modConfig
from customEffectScripts import logger

@Mod.Binding(name = modConfig.ModName, version = "1.0")
class CustomEffectMod(object):

    def __init__(self):
        logger.info("===== init CustomEffect mod =====")

    @Mod.InitServer()
    def CustomEffectServerInit(self):
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)

    @Mod.InitClient()
    def CustomEffectClientInit(self):
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)

    @Mod.DestroyServer()
    def CustomEffectServerDestroy(self):
        pass

    @Mod.DestroyClient()
    def CustomEffectClientDestroy(self):
        pass