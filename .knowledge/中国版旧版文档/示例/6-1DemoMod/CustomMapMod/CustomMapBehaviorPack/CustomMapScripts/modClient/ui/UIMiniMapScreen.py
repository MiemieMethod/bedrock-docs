# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi
MiniMapBaseScreen = clientApi.GetMiniMapScreenNodeCls()

class UIMiniMapScreen(MiniMapBaseScreen):
    def __init__(self, namespace, name, param):
        MiniMapBaseScreen.__init__(self, namespace, name, param)
