# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name = "TutorialMod", version = "0.0.1")
class CustomBiomesMod(object):

    def __init__(self):
        print "===== init CustomBiomesMod mod ====="

    @Mod.InitServer()
    def ServerInit(self):
        print "===== init CustomBiomesMod server ====="
        serverApi.RegisterSystem("CustomBiomesMod", "CustomBiomesServerSystem", "customBiomesScripts.customBiomesServerSystem.CustomBiomesServerSystem")

    @Mod.DestroyServer()
    def ServerDestroy(self):
        print "===== destroy CustomBiomesMod server ====="
    
    @Mod.InitClient()
    def ClientInit(self):
        print "===== init CustomBiomesMod client ====="
        clientApi.RegisterSystem("CustomBiomesMod", "CustomBiomesClientSystem", "customBiomesScripts.customBiomesClientSystem.CustomBiomesClientSystem")
    
    @Mod.DestroyClient()
    def ClientDestroy(self):
        print "===== destroy CustomBiomesMod client ====="
