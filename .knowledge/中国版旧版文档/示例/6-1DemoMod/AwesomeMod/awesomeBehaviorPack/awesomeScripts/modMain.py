# -*- coding: utf-8 -*-

# 关于MOD开发的基本内容可以先参考TutorialMod
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi
# 变量的值尽量写在一个config文件中，这里我们写在了modConfig中
# 这样的好处是，对于字符串变量我们不会打错减少BUG
# DeBug的时候或者修改变量的时候，不用修改每一个使用的地方，只需要修改config文件
from awesomeScripts.modCommon import modConfig
# 这个logger的定义是写在同级目录__init__.py中的
from awesomeScripts import logger

@Mod.Binding(name=modConfig.ModName, version=modConfig.ModVersion)
class HugoFpsMod(object):

    def __init__(self):
        logger.info("===== init hugo fps mod =====")

    @Mod.InitServer()
    def HugoFpsServerInit(self):
        logger.info("===== init hugo fps server =====")
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)

    @Mod.DestroyServer()
    def HugoFpsServerDestroy(self):
        logger.info("===== destroy hugo fps server =====")
    
    @Mod.InitClient()
    def HugoFpsClientInit(self):
        logger.info("===== init hugo fps client =====")
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)
    
    @Mod.DestroyClient()
    def HugoFpsClientDestroy(self):
        logger.info("===== destroy hugo fps client =====")
