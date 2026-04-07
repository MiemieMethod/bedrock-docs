# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi

@Mod.Binding(name='HziGachaChest', version='1.0.0')
class HziGachaChest(object):

    @Mod.InitClient()
    def ClientInit(self):
        clientApi.RegisterSystem('HziGachaChest', 'HziGachaChestBeh', 'hziGachaChestScript.hziGachaChestBeh.HziGachaChestBeh')

    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass