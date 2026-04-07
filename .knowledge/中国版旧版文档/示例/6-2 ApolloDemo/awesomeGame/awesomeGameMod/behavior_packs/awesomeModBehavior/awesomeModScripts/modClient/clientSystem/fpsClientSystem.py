# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from awesomeModScripts.modCommon import modConfig
# 用来打印规范的log
from mod_log import logger

class FpsClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        # 保存ui界面节点
        self.mFpsBattleUINode = None
        # 拼接ShootComponent的Key
        self.mShootKey = modConfig.AwesomeModName + ":" + modConfig.ClientShootComponent
        # 获取客户端本地玩家的playerId
        self.mPlayerId = clientApi.GetLocalPlayerId()
        # 用于保存在击中后需要释放的实体
        self.mHitDestroyIdList = {}

    def ListenEvent(self):
        '''
        监听引擎和服务端脚本的事件
        '''
        #UI初始化框架完成，此时可以创建UI
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        #监听服务器自定义事件，处理玩家射击逻辑
        self.ListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        #监听服务器自定义事件，处理子弹飞行逻辑
        self.ListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        #监听服务器自定义事件，处理子弹碰撞逻辑
        self.ListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    def UnListenEvent(self):
        '''
        取消监听引擎和服务端脚本事件
        '''
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.UnListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.UnListenForEvent(modConfig.AwesomeModName, modConfig.FpsServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    def OnUIInitFinished(self, args):
        '''
        监听引擎初始化完成事件，在这个事件后创建我们的战斗UI
        '''
        logger.info("OnUIInitFinished : %s", args)
        # API详细说明参见 MC开发者文档（http://mc.163.com/mcstudio/mc-dev/）
        clientApi.RegisterUI(modConfig.AwesomeModName, modConfig.FpsBattleUIName, modConfig.FpsBattleUIPyClsPath, modConfig.FpsBattleUIScreenDef)
        # API详细说明参见 MC开发者文档（http://mc.163.com/mcstudio/mc-dev/）
        clientApi.CreateUI(modConfig.AwesomeModName, modConfig.FpsBattleUIName, {"isHud" : 1})
        self.mFpsBattleUINode = clientApi.GetUI(modConfig.AwesomeModName, modConfig.FpsBattleUIName)
        if self.mFpsBattleUINode:
            self.mFpsBattleUINode.Init()
        else:
            logger.error("create ui %s failed!" % modConfig.FpsBattleUIScreenDef)
        logger.info("change model datiangou")
        # 客户端换上模型大天狗并循环播放动作大天狗跑步
        modelComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    def OnPlayShootAnim(self, data):
        """
        监听来自服务端的事件，客户端在这里开始播放服务端通知的相应的射击动作
        """
        entityId = data.get("entityId", "-1")
        anim = data.get("anim", "")
        isLoop = data.get("isLoop", False)
        modelComp = self.GetComponent(entityId, modConfig.Minecraft, modConfig.ModelCompClient)
        if not modelComp:
            logger.warning("do not have model comp!")
            return
        modelComp.aniName = anim
        modelComp.isLoop = isLoop
        self.NeedsUpdate(modelComp)
        # 添加客户端触发的定时器，非重复，延迟1.2s执行
        comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
        comp.AddTimer(1.2, self.DelayPlayAnimRun)

    def DelayPlayAnimRun(self):
        '''
        在播放完大天狗风袭动作之后，播放大天狗跑步动作，延迟的帧数是风袭动作的播放帧数
        '''
        logger.info("Delay play run anim")
        modelComp = self.GetComponent(self.mPlayerId, modConfig.Minecraft, modConfig.ModelCompClient)
        modelComp.modelName = modConfig.DatiangouModel
        modelComp.aniName = modConfig.DatiangouRunAnim
        modelComp.isLoop = True
        self.NeedsUpdate(modelComp)

    def OnBulletFlyFrame(self, data):
        '''
        在子弹开始飞的时候，给子弹绑定上特效
        '''
        logger.info("OnBulletFlyFrame: %s" , data)
        bindId = data.get("bindId", "-1")
        # 同服务端的解释，tempEntity保存来自各个Component的数据
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompClient)
        typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_SFX
        pathComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PathComponent)
        pathComp.path = modConfig.BulletFlyFrameSfx
        # 创建真正的特效SFX实体绑定在子弹上
        frameEntityId = self.CreateEntity(tempEntity)
        entityBindComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniBindComponent)
        entityBindComp.bindEntityId = bindId
        entityBindComp.offset = (-1, 0, 0)
        entityBindComp.rot = (0, 0, 0)
        self.NeedsUpdate(entityBindComp)
        playerPosComp = self.GetComponent(self.mPlayerId, modConfig.Minecraft, modConfig.PosComponent)
        transComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniTransComponent)
        transComp.pos = playerPosComp.pos
        self.NeedsUpdate(transComp)
        ctrlComp = self.CreateComponent(frameEntityId, modConfig.Minecraft, modConfig.FrameAniCtrlComponent)
        ctrlComp.open = True
        ctrlComp.loop = True
        ctrlComp.faceCamera = True
        self.NeedsUpdate(ctrlComp)
        # 将特效实体Id保存在self.mHitDestroyIdList中，后续更新中会清除
        bindList = self.mHitDestroyIdList.setdefault(bindId, [])
        bindList.append(frameEntityId)

    def OnBulletHit(self, data):
        '''
        当子弹射中后，服务端通知客户端并返回一些数据后
        '''
        logger.info("OnBulletHit %s", data)
        bulletId = data.get("bulletId", "-1")
        targetId = data.get("targetId", "-1")
        hitFace = data.get("hitFace", -1)
        pos = data.get("pos", (0, 0, 0))
        pos = tuple(pos)
        # 添加播放声音的Component
        audioComp = self.CreateComponent(self.mPlayerId, modConfig.Minecraft, modConfig.AudioComponent)
        audioComp.name = modConfig.BulletHitSound
        audioComp.pos = pos
        audioComp.volume = 1.0
        audioComp.pitch = 1.0
        audioComp.needPlay = True
        self.NeedsUpdate(audioComp)
        # 添加击中后在原地产生的爆炸粒子特效
        tempEntity = self.CreateTempEntity()
        typeComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ScriptTypeCompClient)
        typeComp.type = clientApi.GetMinecraftEnum().EntityConst.TYPE_PARTICLE
        pathComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.PathComponent)
        pathComp.path = modConfig.BulletHitEffect
        transComp = self.CreateComponent(tempEntity.mId, modConfig.Minecraft, modConfig.ParticleTransComponent)
        transComp.pos = pos
        particleEntityId = self.CreateEntity(tempEntity)
        ctrlComp = self.CreateComponent(particleEntityId, modConfig.Minecraft, modConfig.ParticleControlComponent)
        ctrlComp.open = True
        self.NeedsUpdate(ctrlComp)
        # 爆炸的粒子特效延迟销毁
        comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
        comp.AddTimer(1.0, self.CloseParticleControl, ctrlComp)
        # 在每次射中后删除绑定在子弹上的特效
        destroyList = self.mHitDestroyIdList.get(bulletId, None)
        if destroyList:
            for entityId in destroyList:
                self.DestroyEntity(entityId)

    def CloseParticleControl(self, ctrlComp):
        ctrlComp.open = False
        self.NeedsUpdate(ctrlComp)

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        self.UpdateShoot()

    # 更新自定义的ClientShootComponent，提交ClientShootComponent更新操作的是fpsBattle.py UI类中
    # Component需要经过System更新后才能生效，自定义的Component需要自己写相应的更新函数
    # 引擎的Component则在NeedsUpdate之后，由引擎来更新
    def UpdateShoot(self):
        needUpdateEntities = self.GetNeedUpdate().get(self.mShootKey, {})
        for entityId in needUpdateEntities:
            comp = self.GetComponent(entityId, modConfig.AwesomeModName, modConfig.ClientShootComponent)
            if comp and comp.shoot:
                shootData = self.CreateEventData()
                shootData["id"] = self.mPlayerId
                print "NotifyToServer Shoot",shootData
                # 向服务端发送事件，玩家为playerId的人发送了射击事件
                self.NotifyToServer(modConfig.ShootEvent, shootData)
                # 发送后将Component置为不需要更新
                comp.shoot = False

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== Fps Client System Destroy =====")
        self.UnListenEvent()