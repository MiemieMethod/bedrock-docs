# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
from mod_log import logger
from CustomFurnaceScripts.modCommon import modConfig
from CustomFurnaceScripts.modServer.serverFactory.furnaceManagerFactory import FurnaceManagerFactory
from CustomFurnaceScripts.modServer.serverSystem.customContainerServerSystem import CustomContainerServerSystem
from CustomFurnaceScripts.modCommon.modCommonUtils import itemUtils

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class CustomFurnaceServerSystem(CustomContainerServerSystem):
    def __init__(self, namespace, name):
        super(CustomFurnaceServerSystem, self).__init__(namespace, name)
        # key: (x, y, z, dimension), value: furnaceManager
        self.mCustomFurnaceDict = {}
        # 初始化可以进行右键打开的容器列表
        self.mCustomContainer = modConfig.CUSTOM_CONTAINER_LIST

    def ListenEvent(self):
        super(CustomFurnaceServerSystem, self).ListenEvent()
        # 监听服务端引擎事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerBlockEntityTickEvent,
                            self, self.OnBlockEntityTick)

    def UnListenEvent(self):
        super(CustomFurnaceServerSystem, self).UnListenEvent()
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerBlockEntityTickEvent,
                              self, self.OnBlockEntityTick)

    def GetCustomContainerItems(self, dimension, blockName, blockPos):
        # 覆写基类方法，获取自定义熔炉中blockEntityData中的数据
        items = {}
        blockEntityComp = compFactory.CreateBlockEntityData(self.mLevelId)
        blockEntityData = blockEntityComp.GetBlockEntityData(dimension, blockPos)
        if blockEntityData:
            for i in range(0, modConfig.FURNACE_SLOT_NUM_DICT.get(blockName, 0)):
                key = "{0}{1}".format(modConfig.FURNACE_SLOT_PREFIX, i)
                items[key] = blockEntityData[key]
        return items

    def ResetCustomContainer(self, dimension, blockName, blockPos):
        # 覆写基类方法，方块被摧毁时需要重置的数据在这里处理
        furnaceKey = (blockPos[0], blockPos[1], blockPos[2], dimension)
        if furnaceKey in self.mCustomFurnaceDict:
            del self.mCustomFurnaceDict[furnaceKey]

    def UpdateCustomContainer(self, playerId, blockPos, dimension):
        # 覆写基类方法，获取自定义熔炉状态，更新熔炉状态（此处不要更新熔炉内物品槽，会导致飞行动画错误）
        furnaceMgr = self.mCustomFurnaceDict.get((blockPos[0], blockPos[1], blockPos[2], dimension))
        if furnaceMgr:
            furnaceData = self.CreateEventData()
            furnaceData["blockName"] = furnaceMgr.GetBlockName()
            furnaceData["isLit"] = furnaceMgr.IsLit()
            furnaceData["litDuration"] = furnaceMgr.GetLitDuration()
            furnaceData["isCooking"] = furnaceMgr.IsCooking()
            self.NotifyToClient(playerId, modConfig.OnCustomContainerChangedEvent, furnaceData)

    def OnBlockEntityTick(self, args):
        # 避免频繁输出，易造成卡顿
        blockName = args["blockName"]
        blockPos = (args["posX"], args["posY"], args["posZ"])
        dimension = args["dimension"]
        blockKey = (args["posX"], args["posY"], args["posZ"], args["dimension"])
        # 在这里进行实现自定义熔炉的tick逻辑
        if blockName in modConfig.CUSTOM_CONTAINER_LIST:
            # 第一次tick的时候需要从blockEntity获取数据，之后只有数据更新才需要获取blockEntity进行更新
            furnaceMgr = self.mCustomFurnaceDict.get(blockKey)
            if not furnaceMgr:
                furnaceMgr = FurnaceManagerFactory.GetFurnaceManager(blockName)
                blockEntityComp = compFactory.CreateBlockEntityData(self.mLevelId)
                blockEntityData = blockEntityComp.GetBlockEntityData(args["dimension"], (args["posX"], args["posY"], args["posZ"]))
                furnaceItems = []
                for i in range(0, modConfig.FURNACE_SLOT_NUM_DICT.get(blockName, 0)):
                    key = "{0}{1}".format(modConfig.FURNACE_SLOT_PREFIX, i)
                    furnaceItems.append(blockEntityData[key])
                furnaceMgr.UpdateBlockData(furnaceItems)
                self.mCustomFurnaceDict[blockKey] = furnaceMgr
            # tick 当需要更新数据或UI时进入下面流程
            if furnaceMgr.Tick():
                # 更新blockEntity数据
                blockEntityComp = compFactory.CreateBlockEntityData(self.mLevelId)
                blockEntityData = blockEntityComp.GetBlockEntityData(args["dimension"], (args["posX"], args["posY"], args["posZ"]))
                blockItems = furnaceMgr.GetBlockItems()
                for i in range(0, modConfig.FURNACE_SLOT_NUM_DICT.get(blockName, 0)):
                    key = "{0}{1}".format(modConfig.FURNACE_SLOT_PREFIX, i)
                    blockEntityData[key] = blockItems[i]
                if not self.mCurOpenedBlock:
                    return
                # 如果当前ui界面打开则通知客户端更新UI
                for playerId, blockInfo in self.mCurOpenedBlock.items():
                    if blockPos in blockInfo.values() and dimension in blockInfo.values():
                        furnaceData = self.CreateEventData()
                        furnaceData[modConfig.CUSTOM_CONTAINER_BAG] = {}
                        for i in range(0, modConfig.FURNACE_SLOT_NUM_DICT.get(blockName, 0)):
                            key = "{0}{1}".format(modConfig.FURNACE_SLOT_PREFIX, i)
                            furnaceData[modConfig.CUSTOM_CONTAINER_BAG][key] = blockItems[i]
                        furnaceData["blockName"] = blockName
                        furnaceData["isLit"] = furnaceMgr.IsLit()
                        furnaceData["litDuration"] = furnaceMgr.GetLitDuration()
                        furnaceData["isCooking"] = furnaceMgr.IsCooking()
                        self.NotifyToClient(playerId, modConfig.OnCustomContainerChangedEvent, furnaceData)
                        break

    def OnCustomContainerItemSwap(self, playerId, fromSlot, fromItem, toSlot, toItem):
        # 因为熔炉槽位名是str，背包槽位名是int所以做如下判断
        if isinstance(fromSlot, str) and isinstance(toSlot, str):
            # 不允许熔炉内部槽物物品交换
            return False
        # 熔炉槽和背包槽之间的交换
        if isinstance(fromSlot, str) or isinstance(toSlot, str):
            itemComp = compFactory.CreateItem(playerId)
            blockEntityComp = compFactory.CreateBlockEntityData(self.mLevelId)
            blockInfo = self.GetBlockInfoByPlayerId(playerId)
            if not blockInfo:
                logger.error("Get opened block key error!")
                return False
            blockPos = blockInfo.get("blockPos")
            dimension = blockInfo.get("dimension")
            blockKey = (blockPos[0], blockPos[1], blockPos[2], dimension)
            blockEntityData = blockEntityComp.GetBlockEntityData(blockInfo.get("dimension"), blockInfo.get("blockPos"))
            furnaceMgr = self.mCustomFurnaceDict.get(blockKey)
            # 如果其中一个槽不可放置则返回
            if not furnaceMgr.CanSet(fromSlot, toItem) or not furnaceMgr.CanSet(toSlot, fromItem):
                return False
            # 从熔炉取出物品到背包
            if isinstance(toSlot, int):
                if furnaceMgr.GetSlot(fromSlot) == 0:
                    # 从生成槽取出物品时，只能在目标槽位为空时才可以取出
                    if toItem and not itemUtils.IsSameItem(fromItem, toItem):
                        return False
                furnaceMgr.UpdateSlotData(fromSlot, toItem)
                blockEntityData[fromSlot] = toItem
                itemComp.SpawnItemToPlayerInv(fromItem, playerId, toSlot)
            # 从背包放置物品到熔炉
            else:
                furnaceMgr.UpdateSlotData(toSlot, fromItem)
                blockEntityData[toSlot] = fromItem
                if toItem:
                    itemComp.SpawnItemToPlayerInv(toItem, playerId, fromSlot)
                else:
                    itemComp.SetInvItemNum(fromSlot, 0)
        return True

    def OnCustomContainerItemDrop(self, playerId, slot):
        blockEntityComp = compFactory.CreateBlockEntityData(self.mLevelId)
        blockInfo = self.GetBlockInfoByPlayerId(playerId)
        if not blockInfo:
            logger.error("Get opened block key error!")
            return False
        blockPos = blockInfo.get("blockPos")
        dimension = blockInfo.get("dimension")
        blockKey = (blockPos[0], blockPos[1], blockPos[2], dimension)
        blockEntityData = blockEntityComp.GetBlockEntityData(blockInfo.get("dimension"), blockInfo.get("blockPos"))
        furnaceMgr = self.mCustomFurnaceDict.get(blockKey)
        furnaceMgr.UpdateSlotData(slot, None)
        blockEntityData[slot] = None
        return True