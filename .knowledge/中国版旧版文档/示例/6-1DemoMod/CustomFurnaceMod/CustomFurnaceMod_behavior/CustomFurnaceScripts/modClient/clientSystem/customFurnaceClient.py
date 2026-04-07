# -*- coding: utf-8 -*-
from CustomFurnaceScripts.modClient.clientSystem.customContainerClientSystem import CustomContainerClientSystem
from CustomFurnaceScripts.modCommon import modConfig


class CustomFurnaceClientSystem(CustomContainerClientSystem):
    def __init__(self, namespace, name):
        super(CustomFurnaceClientSystem, self).__init__(namespace, name)

    # 监听引擎和服务端脚本事件
    def ListenEvent(self):
        super(CustomFurnaceClientSystem, self).ListenEvent()

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        super(CustomFurnaceClientSystem, self).UnListenEvent()

    # 在清除该system的时候调用取消监听事件
    def Destroy(self):
        self.UnListenEvent()
