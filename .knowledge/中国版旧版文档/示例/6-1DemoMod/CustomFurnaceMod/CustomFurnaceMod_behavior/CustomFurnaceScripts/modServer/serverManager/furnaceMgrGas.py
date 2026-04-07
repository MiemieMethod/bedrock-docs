# -*- coding:utf-8 -*-
from CustomFurnaceScripts.modCommon.modCommonMgr.furnaceRecipeMgr import FurnaceRecipeManager
from CustomFurnaceScripts.modCommon import modConfig
from CustomFurnaceScripts.modCommon.modCommonMgr.furnaceMgrBase import FurnaceManagerBase
from CustomFurnaceScripts.modCommon.modCommonUtils import itemUtils


class FurnaceManagerGas(FurnaceManagerBase):
    """继承自FurnaceManagerBase基类，在这里可以覆写CanBurn函数和Burn函数来实现不同烧炼逻辑"""
    def __init__(self):
        super(FurnaceManagerGas, self).__init__()
        self.mRecipeMgr = FurnaceRecipeManager()
        self.mBlockName = "customblocks:custom_furnace"

    def CanBurn(self):
        """判断是否能够烧炼，只有当生成槽没物品或者生成物跟生成槽物品一致且生成槽物品小于最大堆叠数才返回True"""
        if not self.mItems[2]:
            return False
        resultItem = self.mRecipeMgr.GetFurnaceResult(self.mItems[2].get("itemName"))
        # 配方中没有匹配的生成物返回False
        if not resultItem:
            return False
        # 生成槽为空返回True
        if not self.mItems[0]:
            return True
        # 生成物与生成槽中物品不是同一个物品返回False
        if not itemUtils.IsSameItem(self.mItems[0], resultItem):
            return False
        # 生成槽中物品与生成物一致且堆叠数小于最大堆叠数返回True，最大堆叠数在配方中配置，默认为64
        if self.mItems[0].get("count") < resultItem.get("maxStackSize", modConfig.MAX_STACK_SIZE):
            return True
        return False

    def Burn(self):
        """烧炼过程，消耗原料生成烧炼物"""
        if not self.CanBurn():
            return
        resultItem = self.mRecipeMgr.GetFurnaceResult(self.mItems[2].get("itemName"))
        if not self.mItems[0]:
            self.mItems[0] = resultItem
            self.mItems[0]["count"] = 1
        else:
            self.mItems[0]["count"] += 1
        self.mItems[2]["count"] -= 1
        if self.mItems[2]["count"] == 0:
            self.mItems[2] = None

    def CanSet(self, slotName, item):
        slot = self.GetSlot(slotName)
        # 如果为背包槽允许放置
        if slot == -1:
            return True
        # 如果为生成槽禁止放置
        if slot == 0:
            if item:
                return False
            return True
        # 如果为燃料槽需是燃料才可以放置
        if slot == 1:
            if item and not self.mRecipeMgr.IsFuelItem(item["itemName"]):
                return False
            return True
        # 如果为原料槽可放置
        if slot > 1:
            return True
        return False
