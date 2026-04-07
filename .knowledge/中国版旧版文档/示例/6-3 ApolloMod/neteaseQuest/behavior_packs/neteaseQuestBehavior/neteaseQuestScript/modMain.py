# -*- coding: utf-8 -*-

from common.mod import Mod
import client.extraClientApi as clientApi
from modCommon import dialogueConfig as modConfig
from . import logger


@Mod.Binding(name=modConfig.ModName, version=modConfig.ModVersion)
class DialogueMod(object):
    def __init__(self):
        logger.info("===== init DialogueMod =====")

    @Mod.InitClient()
    def DialogueClientInit(self):
        logger.info("===== init DialogueClient =====")
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)

    @Mod.DestroyClient()
    def DialogueClientDestroy(self):
        logger.info("===== destroy DialogueClient =====")
