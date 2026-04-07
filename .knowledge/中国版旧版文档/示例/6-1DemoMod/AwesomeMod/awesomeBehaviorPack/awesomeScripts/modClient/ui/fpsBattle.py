# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from awesomeScripts.modClient import logger
from awesomeScripts.modCommon import modConfig
# 获取组件工厂，用来创建组件
compFactory = clientApi.GetEngineCompFactory()

# 所有的UI类需要继承自引擎的ScreenNode类
class FpsBattleScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 这个变量保存了控制视野范围的变量
        self.mOriginalFov = 1.0
        # 这个变量保存了是否显示瞄准界面
        self.mShowSight = False
        # 当前客户端的玩家Id
        self.mPlayerId = clientApi.GetLocalPlayerId()

        self.mButtonPanel = "/buttonPanel"
        self.mAimButton = self.mButtonPanel + "/aimButton"
        self.mShootButtonRight = self.mButtonPanel + "/shootButtonRight"
        self.mShootButtonLeft = self.mButtonPanel + "/shootButtonLeft"
        self.mChangeButton = self.mButtonPanel + "/changeButton"
        self.mAimPanel = "/aimPanel"
        self.mAimImage = self.mAimPanel + "/aimImage"
        self.mAimingImage = self.mAimPanel + "/aimingImage"

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        logger.info("===== FpsBattleScreen Create =====")
        self.AddTouchEventHandler(self.mAimButton, self.OnAimButtonTouch, {"isSwallow": True})
        self.AddTouchEventHandler(self.mShootButtonRight, self.OnShootButtonTouch, {"isSwallow": True})
        self.AddTouchEventHandler(self.mShootButtonLeft, self.OnShootButtonTouch, {"isSwallow": True})
        self.AddTouchEventHandler(self.mChangeButton, self.OnChangeButtonTouch, {"isSwallow": True})

    # 界面的一些初始化操作
    def Init(self):
        # 隐藏原生的中心图标
        self.SetCrossHair(False)
        # 隐藏瞄准界面
        self.SetVisible(self.mAimingImage, False)
        # 获取原始情况下的视野范围大小
        cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
        self.mOriginalFov = cameraComp.GetFov()

    # 绑定了瞄准按钮的 Down 点击事件
    def OnAimButtonTouch(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        # 按钮事件
        touchEvent = args["TouchEvent"]
        # 点击坐标
        touchPos = args["TouchPosX"], args["TouchPosY"]
        # 触控在按钮范围内弹起时
        if touchEvent == touchEventEnum.TouchUp:
            logger.info("============= touch up  =========")
        # 按钮按下时
        elif touchEvent == touchEventEnum.TouchDown:
            self.Aim()
            logger.info("============= touch down  =========")
        # 触控在按钮范围外弹起时
        elif touchEvent == touchEventEnum.TouchCancel:
            logger.info("============= touch cancel  =========")
        # 按下后触控移动时
        elif touchEvent == touchEventEnum.TouchMove:
            logger.info("============= touch move  =========")

    # 绑定了射击按钮的 Up 点击事件
    def OnShootButtonTouch(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]
        if touchEvent == touchEventEnum.TouchUp:
            self.Shoot()

    # 绑定了换子弹的按钮事件，但是没有写逻辑
    def OnChangeButtonTouch(self, args):
        logger.info("============= touch change button  =========")

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        pass

    # 瞄准按钮的逻辑
    def Aim(self):
        # 如果当前是开镜状态，关闭开镜UI并恢复视野范围，并显示角色
        if self.mShowSight:
            self.mShowSight = False
            self.SetVisible(self.mAimImage, True)
            self.SetVisible(self.mAimingImage, False)
            cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
            cameraComp.SetFov(self.mOriginalFov)
            modelComp = compFactory.CreateModel(self.mPlayerId)
            modelId = modelComp.GetModelId()
            modelComp.ShowModel(modelId)
        # 如果当前是不开镜状态，那么就开镜并调整视野范围，并隐藏角色
        else:
            self.mShowSight = True
            self.SetVisible(self.mAimImage, False)
            self.SetVisible(self.mAimingImage, True)
            cameraComp = compFactory.CreateCamera(clientApi.GetLevelId())
            cameraComp.SetFov(self.mOriginalFov + modConfig.SightFieldOfView)
            modelComp = compFactory.CreateModel(self.mPlayerId)
            modelId = modelComp.GetModelId()
            modelComp.HideModel(modelId)

    # 射击按钮的逻辑
    def Shoot(self):
        clientSystem = clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName)
        clientSystem.UpdateShoot()
