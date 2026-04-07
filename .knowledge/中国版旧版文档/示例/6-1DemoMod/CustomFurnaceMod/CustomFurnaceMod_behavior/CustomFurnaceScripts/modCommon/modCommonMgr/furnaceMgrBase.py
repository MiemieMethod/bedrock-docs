# -*- coding:utf-8 -*-
from CustomFurnaceScripts.modCommon.modCommonMgr.recipeMgrBase import RecipeManagerBase
from CustomFurnaceScripts.modCommon import modConfig
from mod_log import logger

class FurnaceManagerBase(object):
    def __init__(self):
        super(FurnaceManagerBase, self).__init__()
        self.mLitTime = 0
        self.mLitDuration = 0
        self.mCookingProgress = 0
        self.mBurnInterval = modConfig.BURN_INTERVAL * 20
        self.mItems = [None, None, None]
        self.mRecipeMgr = RecipeManagerBase()
        self.mBlockName = ""

    def UpdateBlockData(self, itemList):
        self.mItems = itemList

    def UpdateSlotData(self, slotName, item):
        """更新自定义熔炉各个槽位中的物品，如果原料槽发生变化烧炼时间归零"""
        slot = self.GetSlot(slotName)
        if slot == -1:
            logger.error("UpdateSlotData Error!!!")
        self.mItems[slot] = item
        if slot > 1:
            self.mCookingProgress = 0

    def Tick(self):
        # 如果有需要更新的UI或者数据时shouldRefresh为True
        shouldRefresh = False
        lastLit = self.IsLit()
        if self.IsLit():
            self.mLitTime -= 1
        # 可烧炼且燃烧时间为0时尝试消耗燃料获取燃烧时间
        if self.mLitTime == 0 and self.CanBurn():
            if self.mItems[1]:
                self.mLitTime = self.mRecipeMgr.GetBurnDuration(self.mItems[1].get("itemName"))
                self.mLitDuration = self.mLitTime
                if self.IsLit():
                    self.mItems[1]["count"] -= 1
                    if self.mItems[1]["count"] == 0:
                        self.mItems[1] = None
                    shouldRefresh = True
        # 燃烧中并且可烧炼增加烧炼进度
        if self.IsCooking():
            self.mCookingProgress += 1
            if self.mCookingProgress == self.mBurnInterval:
                self.mCookingProgress = 0
                self.Burn()
                shouldRefresh = True
        else:
            if self.mCookingProgress > 0:
                shouldRefresh = True
                self.mCookingProgress = 0
        if lastLit != self.IsLit():
            shouldRefresh = True
        return shouldRefresh

    def GetSlot(self, slotName):
        """根据槽名获取熔炉槽num"""
        if isinstance(slotName, str):
            if not slotName.startswith(modConfig.FURNACE_SLOT_PREFIX):
                return -1
            return int(slotName[len(modConfig.FURNACE_SLOT_PREFIX):])
        return -1

    def IsLit(self):
        """判断自定义熔炉是否处于燃烧状态"""
        return self.mLitTime > 0

    def IsCooking(self):
        return self.IsLit() and self.CanBurn()

    def GetLitDuration(self):
        return self.mLitDuration

    def CanBurn(self):
        """判断是否能够烧炼，烧炼逻辑需要覆写此函数"""
        return False

    def Burn(self):
        """烧炼过程，消耗原料生成烧炼物，通过子类覆写实现"""
        pass

    def GetBlockItems(self):
        return self.mItems

    def CanSet(self, slot, item):
        """判断目标槽位的item是否可放置，通过子类覆写实现"""
        return True

    def GetBlockName(self):
        return self.mBlockName