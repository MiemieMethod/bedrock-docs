# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import mod.client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from mod_log import logger
from awesomeModScripts.modCommon import modConfig

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

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        logger.info("===== FpsBattleScreen Create =====")
        self.mButtonPanel = "/buttonPanel"
        self.mAimButton = self.mButtonPanel + "/aimButton"
        self.mShootButtonRight = self.mButtonPanel + "/shootButtonRight"
        self.mChangeButton = self.mButtonPanel + "/changeButton"
        self.mShootButtonLeft = self.mButtonPanel + "/shootButtonLeft"
        self.mAimPanel = "/aimPanel"
        self.mAimImage = self.mAimPanel + "/aimImage"
        self.mAimingImage = self.mAimPanel + "/aimingImage"

    # 界面的一些初始化操作
    def Init(self):
        # 隐藏原生的中心图标
        self.SetCrossHair(False)
        # 隐藏瞄准界面
        self.SetVisible(self.mAimingImage, False)
        # 获取原始情况下的视野范围大小
        cameraComp = clientApi.CreateComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
        self.mOriginalFov = cameraComp.fov
        clientApi.CreateComponent(self.mPlayerId, modConfig.AwesomeModName, modConfig.ClientShootComponent)

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        pass

    # 绑定这一块详细参考《UIAPI文档》
    # 绑定了瞄准按钮的Up事件
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnAimButtonClick(self, args):
        logger.info("OnAimButtonClick Up")
        self.Aim()
        return ViewRequest.Refresh | ViewRequest.Exit

    # 绑定了换子弹的按钮的Up和Down事件，但是没有写逻辑
    @ViewBinder.binding(ViewBinder.BF_ButtonClick)
    def OnChangeButtonClick(self, args):
        if args["ButtonState"]:
            logger.info("OnChangeButtonClick down")
            return ViewRequest.Refresh
        else:
            logger.info("OnChangeButtonClick up")
            return ViewRequest.Refresh | ViewRequest.Exit

    # 绑定了左边射击按钮的Up点击事件
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnShootButtonLeftClick(self, args):
        logger.info("OnShootButtonLeftClick Up")
        self.Shoot()
        return ViewRequest.Refresh | ViewRequest.Exit

    # 绑定了左边射击按钮的Cancel事件，没有写逻辑
    @ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name = "OnShootButtonLeftClick")
    def OnShootButtonLeftClickCancel(self, args):
        logger.info("OnShootButtonLeftClickCancel Cancel")

    # 绑定了右边边射击按钮的Up点击事件
    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def OnShootButtonRightClick(self, args):
        logger.info("OnShootButtonRightClick Up")
        self.Shoot()
        return ViewRequest.Refresh | ViewRequest.Exit

    # 绑定了右边射击按钮的Cancel事件，没有写逻辑
    @ViewBinder.binding(ViewBinder.BF_ButtonClickCancel, binding_name = "OnShootButtonRightClick")
    def OnShootButtonRightClickCancel(self, args):
        logger.info("OnShootButtonRightClickCancel Cancel")

    # 瞄准按钮的逻辑
    def Aim(self):
        # 如果当前是开镜状态，关闭开镜UI并恢复视野范围
        if self.mShowSight:
            self.mShowSight = False
            self.SetVisible(self.mAimImage, True)
            self.SetVisible(self.mAimingImage, False)
            cameraComp = clientApi.GetComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
            cameraComp.fov = self.mOriginalFov
            clientApi.NeedsUpdate(cameraComp)
        # 如果当前是不开镜状态，那么就开镜并调整视野范围
        else:
            self.mShowSight = True
            self.SetVisible(self.mAimImage, False)
            self.SetVisible(self.mAimingImage, True)
            cameraComp = clientApi.GetComponent(clientApi.GetLevelId(), modConfig.Minecraft, modConfig.CameraComponent)
            cameraComp.fov = self.mOriginalFov + modConfig.SightFieldOfView
            clientApi.NeedsUpdate(cameraComp)

    # 射击按钮的逻辑
    def Shoot(self):
        # 射击逻辑告诉fpsClientSystem这里有一个需要更新的ClientShootComponent
        shootComp = clientApi.GetComponent(self.mPlayerId, modConfig.AwesomeModName, modConfig.ClientShootComponent)
        shootComp.shoot = True
        clientApi.NeedsUpdate(shootComp)
