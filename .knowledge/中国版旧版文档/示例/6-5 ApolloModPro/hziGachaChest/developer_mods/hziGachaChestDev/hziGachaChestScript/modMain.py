# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi

@Mod.Binding(name='HziGachaChest', version='1.0.0')
class HziGachaChest(object):

    @Mod.InitServer()
    def ServerInit(self):
        serverApi.RegisterSystem('HziGachaChest', 'HziGachaChestDev', 'hziGachaChestScript.hziGachaChestDev.HziGachaChestDev')

    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass