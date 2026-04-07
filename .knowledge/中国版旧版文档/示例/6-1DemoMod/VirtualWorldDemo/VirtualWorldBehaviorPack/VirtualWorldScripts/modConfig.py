# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
# Mod Version
ModType = "VirtualWorld"
ModName = "{}Mod".format(ModType)
ModVersion = "0.0.1"

# Server System
ServerSystemName = "{}ServerSystem".format(ModType)
ServerSystemClsPath = "{}Scripts.{}ServerSystem.{}ServerSystem".format(ModType, ModType, ModType)

engineSpace = serverApi.GetEngineNamespace()
engineName = serverApi.GetEngineSystemName()


# Client System
ClientSystemName = "{}ClientSystem".format(ModType)
ClientSystemClsPath = "{}Scripts.{}ClientSystem.{}ClientSystem".format(ModType, ModType, ModType)

# Engine
Minecraft = "Minecraft"