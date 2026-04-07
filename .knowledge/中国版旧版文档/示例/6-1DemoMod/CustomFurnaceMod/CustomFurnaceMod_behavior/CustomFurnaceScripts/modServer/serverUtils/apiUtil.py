# -*- coding:utf-8 -*-

import mod.server.extraServerApi as serverApi
from CustomFurnaceScripts.modCommon import modConfig

_serverModSystem = None


def GetServerModSystem():
    """
    获取服务端系统，全局一个单例。
    :return:
    :rtype: RPGBattleScripts.modServer.serverSystem.rpgBattleServerSystem.RPGBattleServerSystem
    """
    global _serverModSystem
    if not _serverModSystem:
        _serverModSystem = serverApi.GetSystem(modConfig.ModName, modConfig.ServerSystemName)
    return _serverModSystem