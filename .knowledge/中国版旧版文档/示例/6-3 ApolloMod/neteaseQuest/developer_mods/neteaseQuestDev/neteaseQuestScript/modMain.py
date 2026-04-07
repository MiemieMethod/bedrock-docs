# -*- coding: utf-8 -*-

from common.mod import Mod
import server.extraServerApi as serverApi
from modCommon import questConfig, dialogueConfig
from . import logger

'''
与一般的插件不同，任务插件包含了两个服务端system，需要分别初始化，类似于一个由两个互相强关联的插件组合而成的Mod。
其中QuestSystem没有对应的客户端system
'''

@Mod.Binding(name=questConfig.ModName, version=questConfig.ModVersion)
class QuestMod(object):
    def __init__(self):
        logger.info("==== init QuestMod ====")

    @Mod.InitServer()
    def QuestServerInit(self):
        logger.info("==== init QuestServer ====")
        serverApi.RegisterSystem(questConfig.ModName, questConfig.ServerSystemName, questConfig.ServerSystemClsPath)

    @Mod.DestroyServer()
    def QuestServerDestroy(self):
        logger.info("==== destroy QuestServer ====")


@Mod.Binding(name=dialogueConfig.ModName, version=dialogueConfig.ModVersion)
class DialogueMod(object):
    def __init__(self):
        logger.info("===== init DialogueMod =====")

    @Mod.InitServer()
    def DialogueServerInit(self):
        logger.info("===== init DialogueServer =====")
        serverApi.RegisterSystem(dialogueConfig.ModName, dialogueConfig.ServerSystemName, dialogueConfig.ServerSystemClsPath)

    @Mod.DestroyServer()
    def DialogueServerDestroy(self):
        logger.info("===== destroy DialogueServer =====")
