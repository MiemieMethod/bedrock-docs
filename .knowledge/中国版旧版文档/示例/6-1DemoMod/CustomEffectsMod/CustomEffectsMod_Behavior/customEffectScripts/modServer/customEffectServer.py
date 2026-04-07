# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
from customEffectScripts.modCommon import modConfig
from customEffectScripts import logger

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class CustomEffectServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomEffectServerSystem, self).__init__(namespace, name)

        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddEffectServerEvent,
                            self, self.OnEffectAdded)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.RemoveEffectServerEvent,
                            self, self.OnEffectRemoved)

    def UnListenEvent(self):
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddEffectServerEvent,
                              self, self.OnEffectAdded)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.RemoveEffectServerEvent,
                              self, self.OnEffectRemoved)

    def OnEffectAdded(self, args):
        logger.info("AddEffectServerEvent")
        entityId = args["entityId"]
        effectName = args["effectName"]
        if effectName == "custom_effect:weightless":
            # 如果增加的状态是我们自定义的失重状态，在这里实现对应的效果逻辑
            logger.info("SetGravity -0.03")
            comp = compFactory.CreateGravity(entityId)
            comp.SetGravity(-0.03)

    def OnEffectRemoved(self, args):
        logger.info("RemoveEffectServerEvent")
        entityId = args["entityId"]
        effectName = args["effectName"]
        if effectName == "custom_effect:weightless":
            # 如果移除的状态是我们自定义的失重状态，在这里移除对应的效果逻辑
            logger.info("SetGravity 0")
            comp = compFactory.CreateGravity(entityId)
            comp.SetGravity(0)

    def Destroy(self):
        self.UnListenEvent()