# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from uidemoScripts.modCommon import modConfig
# 用来打印规范格式的log
from uidemoScripts.modServer import logger
# 用来执行一些延迟函数
from uidemoScripts.modServer.serverManager.coroutineMgrGas import CoroutineMgr


class UIDemoServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        logger.info("===== Server Listen =====")
        self.ListenEvent()

    # 在类初始化的时候开始监听
    def ListenEvent(self):
        pass

    # 在Destroy中调用反注册一些事件
    def UnListenEvent(self):
        pass

    # ServerChatEvent的回调函数（响应函数）
    def OnServerChat(self, args):
        pass

    # ScriptTickServerEvent的回调函数，会在引擎tick的时候调用，1秒30帧（被调用30次）
    def OnTickServer(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    # 这个Update函数是基类的方法，同样会在引擎tick的时候被调用，1秒30帧（被调用30次）
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== UIDemo Server System Destroy =====")
        self.UnListenEvent()
