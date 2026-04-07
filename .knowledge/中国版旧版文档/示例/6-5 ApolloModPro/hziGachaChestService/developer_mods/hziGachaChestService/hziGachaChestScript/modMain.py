# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

from mod.common.mod import Mod
import mod.server.extraServiceApi as serviceApi

@Mod.Binding(name='HziGachaChest', version='1.0.0')
class HziGachaChest(object):

    @Mod.InitService()
    def ServerInit(self):
        serviceApi.RegisterSystem('HziGachaChest', 'HziGachaChestService', 'hziGachaChestScript.hziGachaChestService.HziGachaChestService')

    @Mod.DestroyService()
    def ServerDestroy(self):
        pass