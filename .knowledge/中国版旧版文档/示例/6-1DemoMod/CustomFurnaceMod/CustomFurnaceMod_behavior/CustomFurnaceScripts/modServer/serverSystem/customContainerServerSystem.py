# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
from mod_log import logger
from CustomFurnaceScripts.modCommon import modConfig
from CustomFurnaceScripts.modServer.serverFactory.furnaceManagerFactory import FurnaceManagerFactory
from CustomFurnaceScripts.modCommon.modCommonUtils import itemUtils

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()

class CustomContainerServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomContainerServerSystem, self).__init__(namespace, name)
        serverApi.SetUseEventTuple()
        self.ListenEvent()
        self.mLevelId = serverApi.GetLevelId()
        # key: playerId, value: blockInfo
        self.mCurOpenedBlock = {}
        # 存储所有自定义容器的name，在子类初始化
        self.mCustomContainer = []

    def ListenEvent(self):
        # 定义服务端自定义事件
        self.DefineEvent(modConfig.OpenCustomContainerEvent)
        self.DefineEvent(modConfig.OnItemSwapServerEvent)
        self.DefineEvent(modConfig.OnItemDropServerEvent)
        self.DefineEvent(modConfig.OnBagChangedEvent)
        self.DefineEvent(modConfig.OnUIShouldCloseServerEvent)
        self.DefineEvent(modConfig.OnCustomContainerChangedEvent)
        # 监听服务端引擎事件
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerBlockUseEvent,
                            self, self.ServerBlockUseEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerItemUseOnEvent,
                            self, self.ServerItemUseOnEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerPlayerTryDestroyBlockEvent,
                            self, self.OnPlayerTryDestroyBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ActorAcquiredItemServerEvent,
                            self, self.OnActorAcquiredItemSeverEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.PlayerDieEvent,
                            self, self.OnPlayerDieServerEvent)
        # 监听客户端自定义事件
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.CloseCustomFurnaceEvent, self, self.CloseCustomContainer)
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.OnItemSwapClientEvent, self, self.OnItemSwap)
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.OnItemDropClientEvent, self, self.OnItemDrop)

    def UnListenEvent(self):
        self.UnDefineEvent(modConfig.OpenCustomContainerEvent)
        self.UnDefineEvent(modConfig.OnItemSwapServerEvent)
        self.UnDefineEvent(modConfig.OnItemDropServerEvent)
        self.UnDefineEvent(modConfig.OnBagChangedEvent)
        self.UnDefineEvent(modConfig.OnUIShouldCloseServerEvent)
        self.UnDefineEvent(modConfig.OnCustomContainerChangedEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerBlockUseEvent,
                            self, self.ServerBlockUseEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerItemUseOnEvent,
                            self, self.ServerItemUseOnEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ServerPlayerTryDestroyBlockEvent,
                            self, self.OnPlayerTryDestroyBlockServerEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.ActorAcquiredItemServerEvent,
                            self, self.OnActorAcquiredItemSeverEvent)
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), modConfig.PlayerDieEvent,
                            self, self.OnPlayerDieServerEvent)
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.CloseCustomFurnaceEvent, self, self.CloseCustomContainer)
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.OnItemSwapClientEvent, self, self.OnItemSwap)
        self.UnListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.OnItemDropClientEvent, self, self.OnItemDrop)

    def CloseCustomContainer(self, args):
        playerId = args["playerId"]
        del self.mCurOpenedBlock[playerId]

    def ServerBlockUseEvent(self, args):
        blockName = args['blockName']
        blockPos = (args['x'], args['y'], args['z'])
        playerId = args['playerId']
        dimensionComp = compFactory.CreateDimension(playerId)
        dimension = dimensionComp.GetPlayerDimensionId()
        # 因为每帧都会tick到，所以加个判断UI已打开就不走后面逻辑
        if blockName in self.mCustomContainer and not self.mCurOpenedBlock.get(playerId):
            self.mCurOpenedBlock[playerId] = {"blockName": blockName, "blockPos": blockPos, "dimension": dimension}
            eventData = self.CreateEventData()
            eventData["blockName"] = blockName
            eventData["blockPos"] = blockPos
            eventData["dimension"] = dimension
            eventData[modConfig.CUSTOM_CONTAINER_BAG] = self.GetCustomContainerItems(dimension, blockName, blockPos)
            self.NotifyToClient(playerId, modConfig.OpenCustomContainerEvent, eventData)
            # 更新熔炉UI，需要确认当前燃烧进度
            self.UpdateCustomContainer(playerId, blockPos, dimension)
            # 初始化UI的时候Grid未创建无法获取对应路径，延迟0.1秒等Grid创建完毕再更新显示数据
            gameComp = compFactory.CreateGame(serverApi.GetLevelId())
            gameComp.AddTimer(0.1, self.UpdateBagUI, playerId, blockName)

    def UpdateBagUI(self, playerId, blockName):
        itemComp = compFactory.CreateItem(playerId)
        eventData = self.CreateEventData()
        eventData["blockName"] = blockName
        eventData[modConfig.INVENTORY_BAG] = {}
        for i in xrange(modConfig.INV_SLOT_NUM):
            eventData[modConfig.INVENTORY_BAG][i] = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, i, True)
        self.NotifyToClient(playerId, modConfig.OnBagChangedEvent, eventData)

    def GetCustomContainerItems(self, dimension, blockName, blockPos):
        """
        @description 获取自定义容器中的所有物品，该数据保存在blockEntityData中
        @param dimension int 自定义容器所在维度
        @param blockName str 自定义容器的方块名，即identifier
        @param blockPos tuple 自定义容器的位置信息，格式为(x, y, z)
        @return dict 返回dict，key为槽位名，value为itemDict
        """
        pass

    def ResetCustomContainer(self, dimension, blockName, blockPos):
        """
        @description 方块被摧毁时需要重置的数据在这里处理
        @param dimension int 自定义容器所在维度
        @param blockName str 自定义容器的方块名，即identifier
        @param blockPos tuple 自定义容器的位置信息，格式为(x, y, z)
        @return dict 返回dict，key为槽位名，value为itemDict
        """
        pass

    def UpdateCustomContainer(self, playerId, blockPos, dimension):
        """
        @description 自定义容器内容发生变化或者打开的时候会调用，可在该函数中实现其他初始化，比如通知客户端初始化容器状态。切记不要在该函数中更新自定义容器槽内物品的数据，可能会导致飞行动画异常
        @param playerId str 打开容器的玩家id，用于通知
        @param blockPos tuple 自定义容器的位置信息，格式为(x, y, z)
        @param dimension int 自定义容器所在维度
        """
        pass

    def ServerItemUseOnEvent(self, args):
        # 如果对自定义熔炉使用物品时拦截物品使用，防止打开自定义熔炉操作的时候误操作放置物品
        playerId = args["entityId"]
        x = args["x"]
        y = args["y"]
        z = args["z"]
        blockComp = compFactory.CreateBlockInfo(playerId)
        blockDict = blockComp.GetBlockNew((x, y, z))
        if blockDict["name"] in self.mCustomContainer:
            args["ret"] = True

    def OnPlayerTryDestroyBlockServerEvent(self, args):
        # 如果破坏自定义熔炉，且熔炉内有物品需要掉落
        blockName = args["fullName"]
        if blockName in modConfig.CUSTOM_CONTAINER_LIST:
            logger.info("Destroy Custom Furnace Block")
            blockPos = (args["x"], args["y"], args["z"])
            playerId = args['playerId']
            dimensionComp = compFactory.CreateDimension(playerId)
            dimension = dimensionComp.GetPlayerDimensionId()
            containerDict = self.GetCustomContainerItems(dimension, blockName, blockPos)
            if not isinstance(containerDict, dict):
                logger.info("Block has no item to drop")
                return
            itemComp = compFactory.CreateItem(self.mLevelId)
            for _, item in containerDict.items():
                if item:
                    res = itemComp.SpawnItemToLevel(item, dimension, blockPos)
                    if not res:
                        logger.error("Spawn Item Error: {0}".format(item))
            self.ResetCustomContainer(dimension, blockName, blockPos)
            # 如果当前该方块的ui被打开需要关闭
            for openedPlayerId, blockInfo in self.mCurOpenedBlock.items():
                if blockPos in blockInfo.values() and dimension in blockInfo.values():
                    eventData = self.CreateEventData()
                    eventData["blockName"] = blockName
                    self.NotifyToClient(openedPlayerId, modConfig.OnUIShouldCloseServerEvent, eventData)
                    break

    def OnActorAcquiredItemSeverEvent(self, args):
        playerId = args["actor"]
        blockInfo = self.GetBlockInfoByPlayerId(playerId)
        if blockInfo:
            blockName = blockInfo.get("blockName")
            self.UpdateBagUI(playerId, blockName)

    def OnPlayerDieServerEvent(self, args):
        playerId = args["id"]
        blockInfo = self.GetBlockInfoByPlayerId(playerId)
        if blockInfo:
            blockName = blockInfo.get("blockName")
            eventData = self.CreateEventData()
            eventData["blockName"] = blockName
            self.NotifyToClient(playerId, modConfig.OnUIShouldCloseServerEvent, eventData)
        del self.mCurOpenedBlock[playerId]

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        pass

    def OnItemSwap(self, args):
        fromSlot = args["fromSlot"]
        toSlot = args["toSlot"]
        fromItem = args["fromItem"]
        toItem = args["toItem"]
        takePercent = args["takePercent"]
        playerId = args["playerId"]
        logger.info("Try swap [{0}] to [{1}]".format(fromSlot, toSlot))
        itemComp = compFactory.CreateItem(playerId)
        # 如果交换的物品是背包里面的，从服务端获取数量做校验
        if isinstance(toSlot, int):
            toItem = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, toSlot, True)
        if isinstance(fromSlot, int):
            fromItem = itemComp.GetPlayerItem(minecraftEnum.ItemPosType.INVENTORY, fromSlot, True)
        if itemUtils.IsSameItem(fromItem, toItem):
            # 两个槽物品相同时处理堆叠
            basicInfo = itemComp.GetItemBasicInfo(toItem.get("itemName"), toItem.get("auxValue"))
            if not basicInfo:
                return
            maxStackSize = basicInfo.get("maxStackSize")
            takeNum = int(fromItem.get("count") * takePercent)
            fromNum = fromItem.get("count")
            toNum = toItem.get("count")
            if not takeNum and not toNum:
                logger.error("OnItemSwap Error!!!")
                return
            if toNum == maxStackSize:
                return
            if toNum + takeNum >= maxStackSize:
                fromNum -= maxStackSize - toNum
                toNum = maxStackSize
            else:
                toNum += takeNum
                fromNum -= takeNum
            fromItem["count"] = toNum
            toItem["count"] = fromNum
            if fromNum == 0:
                toItem = None
            if isinstance(fromSlot, int):
                itemComp.SetInvItemNum(fromSlot, toNum)
            if isinstance(toSlot, int):
                itemComp.SetInvItemNum(toSlot, fromNum)
        if takePercent < 1 and not toItem:
            # 处理分堆
            toNum = int(fromItem.get("count") * takePercent)
            fromNum = int(fromItem.get("count")) - toNum
            fromItem["count"] = toNum
            import copy
            toItem = copy.deepcopy(fromItem)
            toItem["count"] = fromNum
            if isinstance(toSlot, int):
                itemComp.SpawnItemToPlayerInv(toItem, playerId, toSlot)
            if isinstance(fromSlot, int):
                itemComp.SpawnItemToPlayerInv(fromItem, playerId, fromSlot)
        # 自定义容器和背包之间的交换
        if isinstance(fromSlot, str) or isinstance(toSlot, str):
            # 如果交换失败直接返回
            if not self.OnCustomContainerItemSwap(playerId, fromSlot, fromItem, toSlot, toItem):
                return
            self.UpdateCustomContainer(playerId, args["blockPos"], args["dimension"])
        # 背包内部交换
        else:
            itemComp.SetInvItemExchange(fromSlot, toSlot)
        args["fromItem"] = fromItem
        args["toItem"] = toItem
        self.NotifyToClient(playerId, modConfig.OnItemSwapServerEvent, args)

    def OnItemDrop(self, args):
        item = args["item"]
        slot = args["slot"]
        playerId = args["playerId"]
        logger.info("Try drop item in slot[{0}]".format(slot))
        # 丢弃背包物品
        itemComp = compFactory.CreateItem(playerId)
        if isinstance(slot, str):
            if not self.OnCustomContainerItemDrop(playerId, slot):
                return
        else:
            itemComp.SetInvItemNum(slot, 0)
        dimension = args["dimension"]
        pos = args["blockPos"]
        itemComp.SpawnItemToLevel(item, dimension, pos)
        self.NotifyToClient(playerId, modConfig.OnItemDropServerEvent, args)

    def GetBlockInfoByPlayerId(self, playerId):
        return self.mCurOpenedBlock.get(playerId)

    def OnCustomContainerItemSwap(self, playerId, fromSlot, fromItem, toSlot, toItem):
        """
        @description 当交换的物品涉及自定义容器时调用，需在子类实现，返回True表示允许交换，返回False禁止交换，交换成功时需要更新对应容器方块的blockEntityData
        @param playerId 玩家Id
        @param fromSlot 第一次点击的槽位
        @param fromItem 第一次点击槽位的itemDict
        @param toSlot 第二次点击的槽位
        @param toItem 第二次点击槽位的itemDict
        @return bool True表示交换成功，False表示禁止交换"""
        return False

    def OnCustomContainerItemDrop(self, playerId, slot):
        """
        @description 当丢弃物品涉及自定义容器时调用，需在子类实现，返回True表示允许丢弃，返回False禁止丢弃，丢弃成功时需要更新对应容器方块的blockEntityData
        @param playerId 玩家Id
        @param slot 需要丢弃物品所在的槽位
        @return bool True表示丢弃成功并更新blockEntityData，False表示禁止丢弃
        """
        return False

    # 在清除该system的时候调用取消监听事件
    def Destroy(self):
        self.UnListenEvent()