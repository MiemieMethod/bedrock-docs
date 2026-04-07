# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from awesomeScripts.modCommon import modConfig
# 用来打印规范格式的log
from awesomeScripts.modServer import logger
# 获取组件工厂，用来创建组件
compFactory = serverApi.GetEngineCompFactory()

class FpsServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        logger.info("===== Server Listen =====")
        self.ListenEvent()

    # 在类初始化的时候开始监听
    def ListenEvent(self):
        # 服务端脚本自定义了3个事件，用于通知所有的监听了这个事件的客户端
        # PlayShootAnimEvent 用于通知客户端在射击时播放玩家的骨骼动画
        # BulletFlyFrameEvent 用于通知客户端在设计时给子弹绑定特效
        # BulletHitEvent 用于通知客户端子弹击中了目标并返回给客户端一些击中信息
        self.DefineEvent(modConfig.PlayShootAnimEvent)
        self.DefineEvent(modConfig.BulletFlyFrameEvent)
        self.DefineEvent(modConfig.BulletHitEvent)
        # 服务器端脚本监听了引擎的4个事件，分别为 ServerChatEvent / ScriptTickServerEvent / AddServerPlayerEvent / ProjectileDoHitEffectEvent
        # 具体每个事件的详细事件data可以参考《MODSDK文档》
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent, self, self.OnServerChat)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ScriptTickServerEvent, self, self.OnTickServer)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddServerPlayerEvent, self, self.OnPlayerAdd)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ProjectileDoHitEffectEvent, self, self.OnProjectileHit)
        # 服务端脚本监听了客户端自定义的事件 ShootEvent
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShootEvent, self, self.OnShoot)

    # 在Destroy中调用反注册一些事件
    def UnListenEvent(self):
        # 取消自定义的3个事件
        self.UnDefineEvent(modConfig.PlayShootAnimEvent)
        self.UnDefineEvent(modConfig.BulletFlyFrameEvent)
        self.UnDefineEvent(modConfig.BulletHitEvent)
        # 取消监听4个系统事件
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerChatEvent, self, self.OnServerChat)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ScriptTickServerEvent, self, self.OnTickServer)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.AddServerPlayerEvent, self, self.OnPlayerAdd)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ProjectileDoHitEffectEvent, self, self.OnProjectileHit)
        # 取消监听客户端事件
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.ShootEvent, self, self.OnShoot)

    # ServerChatEvent的回调函数（响应函数）
    def OnServerChat(self, args):
        logger.info("ServerChatMessage : %s", args)
        # 这里使用了§这个符号来修改输入消息的用户名和信息
        # 具体参考https://minecraft-zh.gamepedia.com/index.php?title=%E6%A0%B7%E5%BC%8F%E4%BB%A3%E7%A0%81&variant=zh
        args["username"] = "§l§e Hugo"
        args["message"] = "§l§e HelloWorld!"

    # ScriptTickServerEvent的回调函数，会在引擎tick的时候调用，1秒30帧（被调用30次）
    def OnTickServer(self):
        """
        Driven by event, One tick way
        """
        pass

    # 这个Update函数是基类的方法，同样会在引擎tick的时候被调用，1秒30帧（被调用30次）
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 客户端ShootEvent的回调，在客户端射击的时候被调用 关于参数问题参考《MODSDK文档》
    def OnShoot(self, data):
        playerId = data.get("id", "-1")
        logger.info("OnShoot playerId: %s" % playerId)
        # 下面这些内容都可以在《MODSDK文档中找到》

        # 获取到玩家的位置pos和转向rot信息
        posComp = compFactory.CreatePos(playerId)
        rotComp = compFactory.CreateRot(playerId)
        pos = posComp.GetPos()
        rot = rotComp.GetRot()
        direct = serverApi.GetDirFromRot(rot)
        power = modConfig.BulletPower
        gravity = modConfig.BulletGravity
        # 使用弓箭类型来创建抛射物子弹
        bulletId = self.CreateEngineBullet(playerId, serverApi.GetMinecraftEnum().EntityType.Arrow, pos, direct, power, gravity)

        # 创建事件数据 data 并赋值，注意事件数据不支持 tuple
        # 广播BulletFlyFrameEvent子弹飞行这个事件通知客户端让客户端给子弹绑上特效
        frameInfo = self.CreateEventData()
        frameInfo["bindId"] = bulletId
        self.BroadcastToAllClient(modConfig.BulletFlyFrameEvent, frameInfo)

        # 广播PlayShootAnimEvent事件，通知客户端播放发射的玩家骨骼动作大天狗风袭
        animInfo = self.CreateEventData()
        animInfo["entityId"] = playerId
        animInfo["anim"] = modConfig.DatiangouFengxiAnim
        animInfo["isLoop"] = False
        self.BroadcastToAllClient(modConfig.PlayShootAnimEvent, animInfo)

    # AddServerPlayerEvent的回调函数，在服务器端加入玩家的时候被调用
    def OnPlayerAdd(self, data):
        logger.info("OnPlayerAdd : %s", data)
        playerId = data.get("id", "-1")
        if playerId == "-1":
            return
        # 将加入进服务器的玩家的模型换成大天狗
        modelComp = compFactory.CreateModel(playerId)
        modelComp.SetModel(modConfig.DatiangouModel)
        logger.info("TEST === enter set model ===")

    # ProjectileDoHitEffectEvent的回调事件，在抛射物击中的时候被调用，相关参数请参考《MODSDK文档》
    def OnProjectileHit(self, data):
        logger.info("OnProjectileHit : %s", data)
        bulletId = data.get("id", "-1")
        targetType = data.get("hitTargetType", "")
        targetId = data.get("targetId", "")
        hitFace = data.get("hitFace", -1)
        x = data.get("x", 0.0)
        y = data.get("y", 0.0)
        z = data.get("z", 0.0)
        blockPosX = data.get("blockPosX", 0)
        blockPosY = data.get("blockPosY", 0)
        blockPosZ = data.get("blockPosZ", 0)
        # 将子弹射中事件广播给客户端
        hitInfo = self.CreateEventData()
        hitInfo["bulletId"] = bulletId
        hitInfo["pos"] = (x, y, z)
        hitInfo["targetId"] = targetId
        hitInfo["targetType"] = targetType
        hitInfo["hitFace"] = hitFace
        self.BroadcastToAllClient(modConfig.BulletHitEvent, hitInfo)
        # 在子弹射中后将子弹实体清除掉
        self.DestroyEntity(bulletId)

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== Fps Server System Destroy =====")
        self.UnListenEvent()
