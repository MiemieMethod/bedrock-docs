# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
from awesomeScripts.modCommon import modConfig
# 用来打印规范的log
from awesomeScripts.modClient import logger
# 获取组件工厂，用来创建组件
compFactory = clientApi.GetEngineCompFactory()

class FpsClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        # 保存ui界面节点
        self.mFpsBattleUINode = None
        # 拼接ShootComponent的Key
        self.mShootKey = modConfig.ModName + ":" + modConfig.ClientShootComponent
        # 获取客户端本地玩家的playerId
        self.mPlayerId = clientApi.GetLocalPlayerId()
        # 用于保存在击中后需要释放的实体
        self.mHitDestroyIdList = {}

    # 监听引擎和服务端脚本的事件
    def ListenEvent(self):
        self.DefineEvent(modConfig.ShootEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.ListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.PlayShootAnimEvent, self, self.OnPlayShootAnim)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletFlyFrameEvent, self, self.OnBulletFlyFrame)
        self.UnListenForEvent(modConfig.ModName, modConfig.ServerSystemName, modConfig.BulletHitEvent, self, self.OnBulletHit)

    # 监听引擎初始化完成事件，在这个事件后创建我们的战斗UI
    def OnUIInitFinished(self, args):
        logger.info("OnUIInitFinished : %s", args)
        # 注册UI 详细解释参照《UI API》
        clientApi.RegisterUI(modConfig.ModName, modConfig.FpsBattleUIName, modConfig.FpsBattleUIPyClsPath, modConfig.FpsBattleUIScreenDef)
        # 创建UI 详细解释参照《UI API》，下面是两种获得 uiNode 的方式
        self.mFpsBattleUINode = clientApi.CreateUI(modConfig.ModName, modConfig.FpsBattleUIName, {"isHud": 1})
        self.mFpsBattleUINode = clientApi.GetUI(modConfig.ModName, modConfig.FpsBattleUIName)
        if self.mFpsBattleUINode:
            self.mFpsBattleUINode.Init()
        else:
            logger.error("create ui %s failed!" % modConfig.FpsBattleUIScreenDef)
        logger.info("change model datiangou")
        # 客户端换上模型大天狗并循环播放动作大天狗跑步
        modelComp = compFactory.CreateModel(self.mPlayerId)
        modelComp.SetModel(modConfig.DatiangouModel)
        modelComp.PlayAnim(modConfig.DatiangouRunAnim, True)

    # 监听引擎ScriptTickClientEvent事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        pass

    # 监听来自服务端的事件，客户端在这里开始播放服务端通知的相应的射击动作
    def OnPlayShootAnim(self, data):
        """
        Play shoot anim
        """
        entityId = data.get("entityId", "-1")
        anim = data.get("anim", "")
        isLoop = data.get("isLoop", False)
        modelComp = compFactory.CreateModel(entityId)
        if not modelComp:
            logger.warning("do not have model comp!")
            return
        modelComp.PlayAnim(anim, isLoop)
        # 延迟恢复播放大天狗跑步
        gameComp = compFactory.CreateGame(clientApi.GetLevelId())
        gameComp.AddTimer(modConfig.DatiangouFengxiAnimFrames/30.0, self.DelayPlayAnimRun)

    # 在播放完大天狗风袭动作之后，播放大天狗跑步动作，延迟的帧数是风袭动作的播放帧数
    def DelayPlayAnimRun(self):
        logger.info("Delay play run anim")
        modelComp = compFactory.CreateModel(self.mPlayerId)
        modelComp.PlayAnim(modConfig.DatiangouRunAnim, True)

    # 在子弹开始飞的时候，给子弹绑定上特效
    def OnBulletFlyFrame(self, data):
        logger.info("OnBulletFlyFrame: %s", data)
        bindId = data.get("bindId", "-1")

        # 创建真正的特效SFX实体绑定在子弹上
        frameEntityId = self.CreateEngineSfx(modConfig.BulletFlyFrameSfx)
        entityBindComp = compFactory.CreateFrameAniEntityBind(frameEntityId)
        entityBindComp.Bind(bindId, (0, 0, 0), (0, 0, 0))
        frameAniTransComp = compFactory.CreateFrameAniTrans(frameEntityId)
        playerPosComp = compFactory.CreatePos(self.mPlayerId)
        frameAniTransComp.SetPos(playerPosComp.GetPos())
        frameAniTransComp.SetRot((0, 0, 0))
        frameAniTransComp.SetScale((1, 1, 1))
        frameAniControlComp = compFactory.CreateFrameAniControl(frameEntityId)
        frameAniControlComp.SetLoop(True)
        frameAniControlComp.SetFaceCamera(True)
        frameAniControlComp.Play()

        # 将特效实体Id保存在self.mHitDestroyIdList中，后续更新中会清除
        bindList = self.mHitDestroyIdList.setdefault(bindId, [])
        bindList.append(frameEntityId)

    # 当子弹射中后，服务端通知客户端并返回一些数据后
    def OnBulletHit(self, data):
        logger.info("OnBulletHit %s", data)
        bulletId = data.get("bulletId", "-1")
        targetId = data.get("targetId", "-1")
        hitFace = data.get("hitFace", -1)
        pos = data.get("pos", (0, 0, 0))
        pos = tuple(pos)
        # 添加播放声音的Component
        audioComp = compFactory.CreateCustomAudio(self.mPlayerId)
        audioComp.Play(modConfig.BulletHitSound, pos, 1.0, 1.0)
        # 添加击中后在原地产生的爆炸粒子特效
        particleEntityId = self.CreateEngineParticle(modConfig.BulletHitEffect, pos)
        ctrlComp = compFactory.CreateParticleControl(particleEntityId)
        ctrlComp.Play()
        # 爆炸的粒子特效延迟销毁
        gameComp = compFactory.CreateGame(clientApi.GetLevelId())
         # 在延后modConfig.ParticleControlFrames这么多帧后开始执行销毁
        gameComp.AddTimer(modConfig.ParticleControlFrames/30.0, self.DelayCloseParticleControl, ctrlComp)
        # 在每次射中后删除绑定在子弹上的特效
        destroyList = self.mHitDestroyIdList.get(bulletId, None)
        if destroyList:
            for entityId in destroyList:
                self.DestroyEntity(entityId)
   
    def DelayCloseParticleControl(self, ctrlComp):
        ctrlComp.Stop()

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 发送射击事件
    def UpdateShoot(self):
        shootData = self.CreateEventData()
        shootData["id"] = self.mPlayerId
        # 向服务端发送事件，玩家为playerId的人发送了射击事件
        self.NotifyToServer(modConfig.ShootEvent, shootData)

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== Fps Client System Destroy =====")
        self.UnListenEvent()