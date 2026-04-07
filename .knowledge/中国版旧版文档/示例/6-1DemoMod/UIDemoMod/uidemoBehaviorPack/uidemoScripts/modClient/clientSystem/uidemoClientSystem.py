# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from uidemoScripts.modCommon import modConfig
# 用来打印规范的log
from uidemoScripts.modClient import logger
# 用来执行一些延迟函数，yield 负数为帧数，正数为秒数
from uidemoScripts.modClient.clientManager.coroutineMgrGac import CoroutineMgr


class UIDemoClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        # 保存ui界面节点
        self.mUIDemoNode = None

    # 监听引擎和服务端脚本的事件
    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)

    # 监听引擎初始化完成事件，在这个事件后创建我们的战斗UI
    def OnUIInitFinished(self, args):
        logger.info("OnUIInitFinished : %s", args)
        # 注册UI 详细解释参照《UI API》
        clientApi.RegisterUI(modConfig.ModName, modConfig.UIDemoUIName, modConfig.UIDemoUIPyClsPath, modConfig.UIDemoUIScreenDef)
        # 创建UI 详细解释参照《UI API》，下面是两种获得 uiNode 的方式
        self.mUIDemoNode = clientApi.CreateUI(modConfig.ModName, modConfig.UIDemoUIName, {"isHud": 1})
        self.mUIDemoNode = clientApi.GetUI(modConfig.ModName, modConfig.UIDemoUIName)
        if self.mUIDemoNode:
            def fun():
                self.mUIDemoNode.Init()
            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            ret=comp.AddTimer(1,fun)
        else:
            logger.error("create ui %s failed!" % modConfig.UIDemoUIScreenDef)

    # 监听引擎ScriptTickClientEvent事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== UIDemo Client System Destroy =====")
        self.UnListenEvent()