# -*- coding: utf-8 -*-

from CustomFurnaceScripts.modServer.serverManager.furnaceMgrGas import FurnaceManagerGas

class FurnaceManagerFactory(object):
    """熔炉管理工厂类，根据方块名称创建不同的熔炉管理类"""
    @classmethod
    def GetFurnaceManager(cls, blockName):
        if blockName == "customblocks:custom_furnace":
            return FurnaceManagerGas()