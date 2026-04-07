# -*- coding: utf-8 -*-

# 获取客户端引擎API模块
import mod.client.extraClientApi as clientApi
# 获取客户端system的基类ClientSystem
ClientSystem = clientApi.GetClientSystemCls()
import modConfig

CompFactory = clientApi.GetEngineCompFactory()

# 在modMain中注册的Client System类
class VirtualWorldClientSystem(ClientSystem):

    # 客户端System的初始化函数
    def __init__(self, namespace, systemName):
        # 首先初始化TutorialClientSystem的基类ClientSystem
        super(VirtualWorldClientSystem, self).__init__(namespace, systemName)
        print "==== ClientSystem Init ===="
        self.playerID = clientApi.GetLocalPlayerId()
        self.virtualWorldComp = CompFactory.CreateVirtualWorld(clientApi.GetLevelId())
        #是否存在虚拟世界
        self.IsExistVirtualWorld = False
        #当前模型组索引
        self.currentIndex = 1
        #模型组id字典
        self.modelIdDic = {}
        #可点击模型
        self.clickMId = None
        self.cameraSwitch = False
        self.ListenEvent()

    def ListenEvent(self):
      self.ListenForEvent(modConfig.ModName,modConfig.ServerSystemName,"CreateVirtualWorld",self,self.CreateVirtualWorld)
      self.ListenForEvent(modConfig.engineSpace,modConfig.engineName,"UiInitFinished",self,self.UiInitFinished)
      self.ListenForEvent(modConfig.engineSpace,modConfig.engineName,"GetEntityByCoordEvent",self,self.GetEntityByCoordEvent)
       
    def showLeftMsg(self, message, color):
        comp = CompFactory.CreateTextNotifyClient(self.playerID)
        comp.SetLeftCornerNotify("§" + color + "[client]" + message)

    def UiInitFinished(self, data):
        self.CreateWorld()
        self.showLeftMsg("聊天窗口指令：","a")
        self.showLeftMsg("关闭虚拟世界输入：关闭虚拟世界","b")
        self.showLeftMsg("创建虚拟世界输入：虚拟世界","b")
        self.showLeftMsg("增加模型组输入：增加模型","b")
        self.showLeftMsg("减少模型组输入：减少模型","b")

    def CreateVirtualWorld(self, data):
        state = data['state']
        if state == "create":
            self.showLeftMsg("创建虚拟世界","6")
            self.CreateWorld()
        elif state == "close":
            result = self.virtualWorldComp.VirtualWorldDestroy()
            #重置环境
            if result:
                self.IsExistVirtualWorld = False
                self.currentIndex = 1
                self.modelIdDic = {}
                self.showLeftMsg("关闭虚拟世界","6")
        elif state == "addObj":
            if not self.IsExistVirtualWorld:
                return
            self.currentIndex += 1
            initX = self.currentIndex * 2
            self.CreateObj(10, 1, initX)
            self.CreateObj(10, 0, initX)
            self.showLeftMsg("增加模型","6")
        elif state == "reduceObj":
            if self.currentIndex == 0:
                return
            for mid in self.modelIdDic[self.currentIndex]:
                self.virtualWorldComp.ModelRemove(mid)
            self.currentIndex -= 1
            self.showLeftMsg("减少模型","6")

    def CreateObj(self, count, orientation, initX):
        initPos = (-initX, 0, -6) if orientation else (initX, 0, -6)
        moveTime = 2
        for i in range(count):
            mid = self.virtualWorldComp.ModelCreateObject("datiangou", "run")
            if self.currentIndex in self.modelIdDic:
                self.modelIdDic[self.currentIndex].append(mid)
            else:
                self.modelIdDic[self.currentIndex] = [mid]
            xOffset = i % 2
            zOffset = i 
            self.virtualWorldComp.ModelMoveTo(mid, (initPos[0] - xOffset, initPos[1], initPos[2] - zOffset), moveTime, clientApi.GetMinecraftEnum().TimeEaseType.linear)
            if orientation:
                self.virtualWorldComp.ModelRotateTo(mid, (0, 45, 0), moveTime)
            else:
                self.virtualWorldComp.ModelRotateTo(mid, (0, -45, 0), moveTime)

    def CreateWorld(self):
        result = self.virtualWorldComp.VirtualWorldCreate()
        #判断是否创建成功
        if result:
            self.IsExistVirtualWorld = True
        else:
            self.showLeftMsg("Create false",'c')
            return
        #创建模型
        initX = self.currentIndex * 2
        self.CreateObj(10, 1, initX)
        self.CreateObj(10, 0, initX)
        #设置相机
        self.virtualWorldComp.CameraSetPos((0, 15, 5))
        self.virtualWorldComp.CameraLookAt((0, 0, -13), (0, 1, 0))
        #创建文字面板
        comp = clientApi.GetEngineCompFactory().CreateTextBoard(self.playerID)
        boardId = comp.CreateTextBoardInWorld("欢迎来到虚拟世界!",(0.5, 0.0, 1.0, 1.0),(1, 1, 1, 1),True)
        comp.SetBoardPos(boardId,(0, 8, -10))
        comp.SetBoardScale(boardId,(8, 8))
        self.virtualWorldComp.MoveToVirtualWorld(clientApi.GetMinecraftEnum().VirtualWorldObjectType.Textboard,boardId)
        #创建粒子
        particleEntityId = self.CreateEngineParticle("effects/burst.json", (-6.0, 7.0, -10.0))
        particleEntityId1 = self.CreateEngineParticle("effects/burst.json", (6.0, 7.0, -10.0))
        parComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
        parComp.Play()
        parComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId1)
        parComp.Play()
        self.virtualWorldComp.MoveToVirtualWorld(clientApi.GetMinecraftEnum().VirtualWorldObjectType.Particle, particleEntityId)
        self.virtualWorldComp.MoveToVirtualWorld(clientApi.GetMinecraftEnum().VirtualWorldObjectType.Particle, particleEntityId1)
        #创建地形
        mid = self.virtualWorldComp.ModelCreateObject("qd_shilaimu_0_0", "")
        self.virtualWorldComp.ModelSetPos(mid, (0, -2, -12))
        self.virtualWorldComp.ModelSetRot(mid, (0, 180, 0))
        self.virtualWorldComp.ModelSetScale(mid, (30.0, 2.0, 30.0))

        #创建可操控模型
        mid = self.virtualWorldComp.ModelCreateObject("datiangou", "fengxi")
        self.virtualWorldComp.ModelSetPos(mid, (10, 2, -12))
        self.virtualWorldComp.ModelSetRot(mid, (-35, 0, 0))
        self.virtualWorldComp.ModelSetScale(mid, (1.5, 1.5, 1.5))
        self.virtualWorldComp.ModelSetBoxCollider(mid, (2.0, 2.0, 2.0), (0.0, 0.0, 0.0))
        self.clickMId = mid
        comp = CompFactory.CreateTextBoard(self.playerID)
        boardId = comp.CreateTextBoardInWorld("点我",(0.5, 0.0, 0.5, 1.0),(0, 0, 1, 0.3),True)
        comp.SetBoardPos(boardId,(8.5, 8.0, -12.0))
        comp.SetBoardScale(boardId,(8, 5))
        self.virtualWorldComp.MoveToVirtualWorld(clientApi.GetMinecraftEnum().VirtualWorldObjectType.Textboard,boardId)

    def GetEntityByCoordEvent(self, data):
        currentId = self.virtualWorldComp.CameraGetClickModel()
        if currentId == self.clickMId:
            self.showLeftMsg("点击成功","6")
            self.cameraSwitch = not self.cameraSwitch
            if self.cameraSwitch:
                self.virtualWorldComp.CameraSetZoom(3.5)
                self.virtualWorldComp.CameraLookAt((9, 6, -12), (-0.25, 1, 0))
            else:
                self.virtualWorldComp.CameraSetZoom(1.0)
                self.virtualWorldComp.CameraLookAt((0, 0, -13), (0, 1, 0))
