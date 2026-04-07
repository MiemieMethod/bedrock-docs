# -*- coding: utf-8 -*-

class RecipeManagerBase(object):
    """配方管理基类"""
    def __init__(self):
        super(RecipeManagerBase, self).__init__()
        self.mRecipes = {}
        # 燃料列表，每个燃料可以提供的燃烧时间在这里配置，key: str物品名称, value: int燃烧时间单位秒
        self.mFuelList = {}

    def GetFurnaceResult(self, inputItem):
        """根据原料及配方获取生成物，开发者可在子类中根据自身理解实现"""
        pass

    def GetBurnDuration(self, fuelItem):
        """根据燃料从燃料列表获取燃料燃烧时间，开发者可在子类中根据自身理解实现"""
        pass

    def IsFuelItem(self, item):
        """判断item是否为燃料"""
        return item in self.mFuelList