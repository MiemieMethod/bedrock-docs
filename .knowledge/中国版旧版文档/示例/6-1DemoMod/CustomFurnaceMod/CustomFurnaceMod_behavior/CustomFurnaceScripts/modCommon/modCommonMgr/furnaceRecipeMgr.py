# -*- coding: utf-8 -*-

from CustomFurnaceScripts.modCommon.modCommonMgr.recipeMgrBase import RecipeManagerBase

class FurnaceRecipeManager(RecipeManagerBase):
    # 配方在这里配置
    # 这里举例的是单个烧炼槽生成单个生成物的例子，开发者可以根据自己理解进行修改成多对一或多对多配方
    # 注:最大堆叠数maxStackSize如果超过物品的实际最大堆叠数，原料和燃料会继续消耗但生成物取回背包时以实际最大生成数生成
    def __init__(self):
        self.mRecipes = {
            "minecraft:apple": {"itemName": "minecraft:iron_sword", "auxValue": 0, "maxStackSize": 1}
        }
        # 燃料列表，每个燃料可以提供的燃烧时间在这里配置，key: str物品名称, value: int燃烧时间单位秒
        self.mFuelList = {"minecraft:planks": 10}

    def GetFurnaceResult(self, inputItem):
        """根据原料及配方获取生成物，开发者可在子类中根据自身理解实现"""
        return self.mRecipes.get(inputItem)

    def GetBurnDuration(self, fuelItem):
        """根据燃料从燃料列表获取燃料燃烧时间
        @param fuelItem 燃料名称
        @return int 燃料对应的燃烧时间（单位刻1s = 20刻），如果不可燃烧返回0
        """
        return self.mFuelList.get(fuelItem, 0) * 20

    def IsFuelItem(self, fuelItem):
        """判断item是否为燃料"""
        return fuelItem in self.mFuelList