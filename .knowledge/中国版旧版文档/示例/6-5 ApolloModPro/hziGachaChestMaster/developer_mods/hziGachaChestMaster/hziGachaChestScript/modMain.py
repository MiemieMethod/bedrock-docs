# -*- coding: utf-8 -*-
# @Author : uni_kevin(可乐)

from mod.common.mod import Mod
import mod.server.extraMasterApi as extraMasterApi

@Mod.Binding(name='HziGachaChest', version='1.0.0')
class HziGachaChest(object):

    @Mod.InitMaster()
    def ServerInit(self):
        extraMasterApi.RegisterSystem('HziGachaChest', 'HziGachaChestMaster', 'hziGachaChestScript.hziGachaChestMaster.HziGachaChestMaster')

    @Mod.DestroyMaster()
    def ServerDestroy(self):
        pass