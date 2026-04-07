# -*- coding: utf-8 -*-
#
import mod.client.extraClientApi as clientApi
import modCommon.modConfig as modConfig
import mod.server.extraServerApi as serverApi
from mod.common.mod import Mod
from mod_log import logger


@Mod.Binding(name = modConfig.ModName, version = "1.0")
class CustomFurnaceMod(object):

    def __init__(self):
        logger.info("===== init CustomFurnace mod =====")

    @Mod.InitServer()
    def CustomFurnaceServerInit(self):
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)

    @Mod.InitClient()
    def CustomFurnaceClientInit(self):
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)

    @Mod.DestroyServer()
    def CustomFurnaceServerDestroy(self):
        pass

    @Mod.DestroyClient()
    def CustomFurnaceClientDestroy(self):
        pass
