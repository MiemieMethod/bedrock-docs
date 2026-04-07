# -*- coding:utf-8 -*-

import mod.client.extraClientApi as clientApi
from CustomFurnaceScripts.modCommon import modConfig

_clientModSystem = None


def GetModClientSystem():
    """
    获取客户端系统，全局一个单例。
    :return:
    :rtype: RPGBattleScripts.modClient.clientSystem.rpgBattleClientSystem.RPGBattleClientSystem
    """
    global _clientModSystem
    if not _clientModSystem:
        _clientModSystem = clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName)
    return _clientModSystem