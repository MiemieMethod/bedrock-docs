# -*- coding: utf-8 -*-
# 这个文件保存了MOD中使用的一些变量

# Mod Version
ModName = "CustomFurnaceMod"
ModVersion = "0.0.1"

# Server System
ServerSystemName = "CustomFurnaceServerSystem"
ServerSystemClsPath = "CustomFurnaceScripts.modServer.serverSystem.customFurnaceServer.CustomFurnaceServerSystem"

# Client System
ClientSystemName = "CustomFurnaceClientSystem"
ClientSystemClsPath = "CustomFurnaceScripts.modClient.clientSystem.customFurnaceClient.CustomFurnaceClientSystem"

# Engine
Minecraft = "Minecraft"
# ————————————————————————————————————————————————————————————————————————————————————————————————————
# Server Event 服务端事件
## Engine 服务端引擎事件
ServerBlockEntityTickEvent = "ServerBlockEntityTickEvent"
ServerBlockUseEvent = "ServerBlockUseEvent"
ServerItemUseOnEvent = "ServerItemUseOnEvent"
ServerPlayerTryDestroyBlockEvent = "ServerPlayerTryDestroyBlockEvent"
ActorAcquiredItemServerEvent = "ActorAcquiredItemServerEvent"
PlayerDieEvent = "PlayerDieEvent"

##Custom 服务端自定义事件
OpenCustomContainerEvent = "OpenCustomContainerEvent"
OnCustomContainerChangedEvent = "OnCustomContainerChangedEvent"
OnUIShouldCloseServerEvent = "OnUIShouldCloseServerEvent"
OnBagChangedEvent = "OnBagChangedEvent"
OnItemSwapServerEvent = "OnItemSwapServerEvent"
OnItemDropServerEvent = "OnItemDropServerEvent"

# DisplayJumpingTextFromServerEvent = 'DisplayJumpingTextFromServerEvent'
# Client Event 客户端事件
## Engine 客户端引擎事件
UiInitFinishedEvent = 'UiInitFinished'

##Custom 客户端自定义事件
CloseCustomFurnaceEvent = "CloseCustomFurnaceEvent"
OnItemSwapClientEvent = "OnItemSwapClientEvent"
OnItemDropClientEvent = "OnItemDropClientEvent"

# ————————————————————————————————————————————————————————————————————————————————————————————————————
# Server Component 服务端组件
## 服务端实体组件

# Client ComponFurnaceent 客户端组件
## 客户端实体组件

# ————————————————————————————————————————————————————————————————————————————————————————————————————
# UI相关定义
CustomFurnaceUIName = 'customFurnaceUI'
CustomFurnaceUIClassPath = 'CustomFurnaceScripts.modClient.ui.customFurnaceUI.CustomFurnaceUIScreen'
CustomFurnaceUIScreenDef = 'customFurnaceUI.main'
# ————————————————————————————————————————————————————————————————————————————————————————————————————

INV_SLOT_NUM = 36
MAX_STACK_SIZE = 64
# 燃烧时间间隔，单位秒，可配置
BURN_INTERVAL = 5
# 飞行动画时间间隔，单位帧，可配置
FLY_ANIMATION_DURATION = 5
# 背包分类
INVENTORY_BAG = 1
CUSTOM_CONTAINER_BAG = 2
# 自定义熔炉槽前缀
FURNACE_SLOT_PREFIX = "furnaceSlot"
# 自定义容器列表
CUSTOM_CONTAINER_LIST = ["customblocks:custom_furnace"]
# 自定义熔炉槽数量，key为方块名,value为槽数
FURNACE_SLOT_NUM_DICT = {"customblocks:custom_furnace": 3}
# 自定义熔炉UI相关绑定信息, key为上面的自定义方块名，value为uiData
# uiName: UI的json文件名
# uiClassPath: UI的ScreenNode管理类
# uiScreenDef: UI的根节点
UI_DEFS = {
    "customblocks:custom_furnace" : {
        "uiName": "customFurnaceUI",
        "uiClassPath": "CustomFurnaceScripts.modClient.ui.customFurnaceUI.CustomFurnaceUIScreen",
        "uiScreenDef": "customFurnaceUI.main"
    }
}
# 双击间隔帧数，该间隔内的两次点击算双击事件
DOUBLE_CLICK_INTERVAL = 4