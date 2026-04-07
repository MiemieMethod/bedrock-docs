# -*- coding: utf-8 -*-

# 获取引擎服务端API的模块
import mod.server.extraServerApi as serverApi
# 获取引擎服务端System的基类，System都要继承于ServerSystem来调用相关函数
ServerSystem = serverApi.GetServerSystemCls()
import modConfig

CompFactory = serverApi.GetEngineCompFactory()

# 在modMain中注册的Server System类
class VirtualWorldServerSystem(ServerSystem):

    # ServerSystem的初始化函数
    def __init__(self, namespace, systemName):
        # 首先调用父类的初始化函数
        super(VirtualWorldServerSystem, self).__init__(namespace, systemName)
        print "===== ServerSystem init ====="
        # 初始时调用监听函数监听事件
        self.ListenEvent()

    # 监听函数，用于定义和监听函数。函数名称除了强调的其他都是自取的，这个函数也是。
    def ListenEvent(self):
        self.ListenForEvent(modConfig.engineSpace, modConfig.engineName, 'ServerChatEvent', self, self.ServerChatEvent)
       
    def showMsg(self, message, color, entityId):
        comp = CompFactory.CreateGame(entityId)
        comp.SetNotifyMsg(message, "§" + color)   
  
    def ServerChatEvent(self, args):
        tempData = self.CreateEventData()
        if args["message"] == "虚拟世界":
            tempData["state"] = "create"
        elif args["message"] == "关闭虚拟世界":
            tempData["state"] = "close"
        elif args["message"] == "增加模型":
            tempData["state"] = "addObj"
        elif args["message"] == "减少模型":
            tempData["state"] = "reduceObj"
        else:
            return
        self.BroadcastToAllClient("CreateVirtualWorld",tempData)
            


