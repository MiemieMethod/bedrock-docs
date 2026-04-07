# -*- coding: utf-8 -*-

from mod_log import logger
from CustomFurnaceScripts.modCommon import modConfig
from CustomFurnaceScripts.modClient.ui.customContainerUIBase import CustomContainerUIScreenBase


class CustomFurnaceUIScreen(CustomContainerUIScreenBase):

    def __init__(self, namespace, name, param):
        super(CustomFurnaceUIScreen, self).__init__(namespace, name, param)
        self.mFireMaskPath = self.mRightPanelPath + "/fire/fireMask"
        self.mArrowMaskPath = self.mRightPanelPath + "/arrow/arrowMask"
        # 管理燃烧状态相关数据
        self.mIsLit = False
        self.mIsCooking = False
        self.mLitProgress = 0
        self.mLitDuration = 0
        self.mBurnProgress = 0

    def Update(self):
        # 执行父类方法
        super(CustomFurnaceUIScreen, self).Update()
        # 更新燃烧动画
        if not self.mIsLit:
            self.mLitProgress = 0
            self.SetSpriteClipRatio(self.mFireMaskPath, 1)
        else:
            # 更新火焰进度
            self.mLitProgress += 1
            fireRatio = (self.mLitProgress * 2.0) / (self.mLitDuration * 3.0)
            self.SetSpriteClipRatio(self.mFireMaskPath, fireRatio)
            if fireRatio == 1:
                self.mLitProgress = 0
        if not self.mIsCooking:
            self.mBurnProgress = 0
            self.SetSpriteClipRatio(self.mArrowMaskPath, 1)
        else:
            # 更新箭头进度
            self.mBurnProgress += 1
            arrowRatio = self.mBurnProgress / (modConfig.BURN_INTERVAL * 30.0)
            self.SetSpriteClipRatio(self.mArrowMaskPath, 1.0 - arrowRatio)
            if arrowRatio == 1:
                self.mBurnProgress = 0

    def InitCustomContainerUI(self, args):
        items = args[modConfig.CUSTOM_CONTAINER_BAG]
        for slotName, itemDict in items.items():
            slotPath = "{0}/{1}".format(self.mRightPanelPath, slotName)
            self.mBagInfo[slotPath] = {"slot": slotName, "item": itemDict}
            self.mSlotToPath[slotName] = slotPath
            self.SetSlotUI(slotPath, itemDict)
        # 初始化燃烧进度
        self.SetSpriteClipRatio(self.mFireMaskPath, 1)
        self.SetSpriteClipRatio(self.mArrowMaskPath, 1)

    def UpdateCustomContainerUI(self, args):
        for key, value in args.items():
            # 更新燃烧状态
            if key == "isLit":
                self.mIsLit = value
            # 更新燃料数据
            elif key == "litDuration":
                if value != self.mLitDuration:
                    self.mLitDuration = args["litDuration"]
                    self.mLitProgress = 0
            elif key == "isCooking":
                self.mIsCooking = value
            # 更新熔炉槽物品信息
            elif key == modConfig.CUSTOM_CONTAINER_BAG:
                for itemSlot, itemDict in value.items():
                    slotPath = "{0}/{1}".format(self.mRightPanelPath, itemSlot)
                    self.mBagInfo[slotPath] = {"slot": itemSlot, "item": itemDict}
                    self.SetSlotUI(slotPath, itemDict)