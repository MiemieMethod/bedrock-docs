# Mod SDK更新信息

**2021.06.24：版本号（v1.23 BE1.16.201）**

详见<a href="/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/更新信息/1.23.html" target="_blank" rel="noopener noreferrer">新版开发者文档</a>

**2021.04.08：版本号（v1.22 BE1.16.10）**

详见<a href="/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/更新信息/1.22.html" target="_blank" rel="noopener noreferrer">新版开发者文档</a>

**2021.1.28：版本号（v1.21 BE1.16.10）**

详见<a href="/dev/mcmanual/mc-dev/mcdocs/1-ModAPI/更新信息/1.21.html" target="_blank" rel="noopener noreferrer">新版开发者文档</a>

**2020.11.26：版本号（v1.20 BE1.14.30）**

- 版本重大更新

1. 组件现在由组件工厂创建。详见[GetEngineCompFactory](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#getenginecompfactory)。
2. [ModSDK库](02-Python脚本开发/0-脚本开发入门.html#安装mod-sdk库)支持组件接口的补全。
3. 增加创建UI界面的方式[PushScreen](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#PushScreen)，该方式不再像[CreateUI](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#CreateUI)挂接在Hub界面上，而是一个独立的界面，通过此方式创建的界面更加灵活，引擎会做好隐藏显示等功能。
4. 支持在界面上显示[小地图](60-UI/5-UIAPI文档.html#MiniMapBaseScreen)，该功能为[实验性功能](../2-ModSDK模组开发/10-实验性功能.md)，具体示例请参考[CustomMapMod](../4-DEMO示例/示例简介.html#custommapmod)。
5. [NeteasePaperDoll](60-UI/4-UI说明文档.html#neteasepaperdoll)现在支持特效渲染，示例详见[GetNeteasePaperDollModelId](60-UI/5-UIAPI文档.html#GetNeteasePaperDollModelId)。

- 新增

1. 新增[AddEntityTickEventWhiteList](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.md#AddEntityTickEventWhiteList)，添加实体tick事件白名单<!--by czh-->

1. 新增[GetEngineCompFactory](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.md#GetEngineCompFactory)，获取组件的工厂，服务端引擎组件通过该工厂创建<!--by czh-->

1. 新增[GetEngineCompFactory](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#GetEngineCompFactory)，获取组件的工厂，客户端引擎组件通过该工厂创建<!--by czh-->

1. 新增[GetMiniMapScreenNodeCls](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#GetMiniMapScreenNodeCls)，获取小地图ScreenNode基类<!--by gzhuabo-->

1. 新增[HideArmorGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#HideArmorGui)，隐藏hud界面的护甲值显示<!--by sutao-->

1. 新增[PopScreen](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#PopScreen)，使用堆栈管理的方式关闭UI<!--by gzhuabo-->

1. 新增[PushScreen](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#PushScreen)，使用堆栈管理的方式创建UI<!--by gzhuabo-->

1. 新增[EntityTickServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#EntityTickServerEvent)，实体tick事件<!--by czh-->

1. 新增[ExtinguishFireServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ExtinguishFireServerEvent)，玩家扑灭火焰事件<!--by czh-->

1. 新增[ItemUseAfterServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ItemUseAfterServerEvent)，使用物品之后的服务端事件<!--by jishaobin-->

1. 新增[ItemUseOnAfterServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ItemUseOnAfterServerEvent)，对方块使用物品之后的服务端事件<!--by jishaobin-->

1. 新增[StartDestroyBlockServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#StartDestroyBlockServerEvent)，玩家开始挖方块的事件<!--by czh-->

1. 新增[ExtinguishFireClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ExtinguishFireClientEvent)，玩家扑灭火焰事件<!--by czh-->

1. 新增[HoldBeforeClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#HoldBeforeClientEvent)，玩家长按屏幕事件<!--by czh-->

1. 新增[LeftClickBeforeClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#LeftClickBeforeClientEvent)，鼠标左键点击事件，代替OnClickInGame事件<!--by czh-->

1. 新增[LeftClickReleaseClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#LeftClickReleaseClientEvent)，鼠标左键松开事件<!--by czh-->

1. 新增[RightClickBeforeClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#RightClickBeforeClientEvent)，鼠标右键点击事件，代替OnClickInGame事件<!--by czh-->

1. 新增[RightClickReleaseClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#RightClickReleaseClientEvent)，鼠标右键松开事件<!--by czh-->

1. 新增[StartDestroyBlockClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#StartDestroyBlockClientEvent)，玩家开始挖方块的事件<!--by czh-->

1. 新增[TapBeforeClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#TapBeforeClientEvent)，玩家短按屏幕事件<!--by czh-->

1. 新增[TapOrHoldReleaseClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#TapOrHoldReleaseClientEvent)，玩家点击屏幕松手事件<!--by czh-->

1. 新增[GetTopBlockHeight](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetTopBlockHeight)，获取某一位置最高的非空气方块的高度（服务端接口）<!--by czh-->

1. 新增[PlayerDestoryBlock](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#PlayerDestoryBlock)，增加使用手上工具破坏方块接口<!--by jishaobin-->

1. 新增[GetChunkMaxPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetChunkMaxPos)，获取某区块最大点的坐标<!--by liaoyi-->

1. 新增[GetChunkMinPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetChunkMinPos)，获取某区块最小点的坐标<!--by liaoyi-->

1. 新增[GetChunkMobNum](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetChunkMobNum)，获取某区块中的生物数量（不包括玩家）<!--by liaoyi-->

1. 新增[GetChunkPosFromBlockPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetChunkPosFromBlockPos)，服务端通过方块坐标获得该方块所在区块坐标<!--by liaoyi-->

1. 新增[IsChunkGenerated](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#IsChunkGenerated)，获取某个区块是否生成过。<!--by czh-->

1. 新增[GetContainerItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetContainerItem)，获取容器中物品，支持常加载区块<!--by jishaobin-->

1. 新增[GetEnderChestItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetEnderChestItem)，获取末影箱中物品<!--by jishaobin-->

1. 新增[GetSelectSlotId](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetSelectSlotId)，获取玩家当前选中槽位<!--by gzhuabo-->

1. 新增[GetUserDataInEvent](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetUserDataInEvent)，可以用物品相关服务端事件的参数中获取userData<!--by czh-->

1. 新增[GetRecipesByResult](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetRecipesByResult)，通过输出物品查询配方所需要的输入材料<!--by sutao-->

1. 新增[GetBlockPoweredState](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetBlockPoweredState)，获取某个坐标方块的充能状态<!--by gzhuabo-->

1. 新增[GetTopBlockHeight](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetTopBlockHeight)，获取某一位置最高的非空气方块的高度（客户端接口）<!--by czh-->

1. 新增[GetChunkPosFromBlockPos](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetChunkPosFromBlockPos)，客户端通过方块坐标获得该方块所在区块坐标<!--by liaoyi-->

1. 新增[GetUserDataInEvent](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetUserDataInEvent)，可以用物品相关客户端事件的参数中获取userData<!--by czh-->

1. 新增[BindModelSfx](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#BindModelSfx)，绑定序列帧动画到骨骼模型上<!--by gzhuabo-->

1. 新增[BindModelToModel](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#BindModelToModel)，在骨骼模型上挂接其他骨骼模型<!--by gzhuabo-->

1. 新增[UnBindModelToModel](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#UnBindModelToModel)，取消骨骼模型上挂接的某个骨骼模型<!--by gzhuabo-->

1. 新增[Create](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#Create)，创建特效粒子<!--by gzhuabo-->

1. 新增[GetMolangValue](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetMolangValue)，获取实体molang变量的值<!--by gzhuabo-->

1. 新增[GetRecipesByResult](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetRecipesByResult)，通过输出物品查询配方所需要的输入材料<!--by sutao-->

1. 新增[CreateTextBoardInWorld](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#CreateTextBoardInWorld)，创建文字面板, 不绑定实体的话使用世界坐标，绑定对象的话会跟随实体<!--by sutao-->

1. 新增[RemoveTextBoard](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#RemoveTextBoard)，删除文字面板<!--by sutao-->

1. 新增[SetBoardBackgroundColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardBackgroundColor)，修改文字面板的背景颜色<!--by sutao-->

1. 新增[SetBoardBindEntity](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardBindEntity)，设置文字面板绑定的实体对象<!--by sutao-->

1. 新增[SetBoardDepthTest](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardDepthTest)，设置文字面板是否开启深度测试<!--by sutao-->

1. 新增[SetBoardFaceCamera](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardFaceCamera)，设置文字面板的朝向<!--by sutao-->

1. 新增[SetBoardPos](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardPos)，修改文字面板的位置<!--by sutao-->

1. 新增[SetBoardRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardRot)，修改文字面板的旋转角度<!--by sutao-->

1. 新增[SetBoardScale](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardScale)，缩放文字面板的大小<!--by sutao-->

1. 新增[SetBoardTextColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#SetBoardTextColor)，修改文字面板的字体颜色<!--by sutao-->

1. 新增[GetNeteasePaperDollModelId](60-UI/5-UIAPI文档.md#GetNeteasePaperDollModelId)，获取NeteasePaperDoll渲染的骨骼模型Id<!--by gzhuabo-->

1. 新增[AddEntityMarker](60-UI/5-UIAPI文档.md#AddEntityMarker)，增加实体位置标记<!--by gzhuabo-->

1. 新增[AddStaticMarker](60-UI/5-UIAPI文档.md#AddStaticMarker)，增加地图上静态位置的标记<!--by gzhuabo-->

1. 新增[RemoveEntityMarker](60-UI/5-UIAPI文档.md#RemoveEntityMarker)，删除实体位置标记<!--by gzhuabo-->

1. 新增[RemoveStaticMarker](60-UI/5-UIAPI文档.md#RemoveStaticMarker)，删除静态位置标记<!--by gzhuabo-->

- 调整

1. [物品信息字典](02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典)中的customTips属性现在支持自定义格式

1. 调整[StartNavTo](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.md#StartNavTo)，优化寻路序列帧表现，新增了几个控制寻路序列帧表现的参数<!--by liaoyi-->

1. 调整[ActorAcquiredItemServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ActorAcquiredItemServerEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ActorUseItemServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ActorUseItemServerEvent)，修改触发时机描述。物品相关参数改为物品信息字典。<!--by jishaobin/czh-->

1. 调整[DamageEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#DamageEvent)，新增“伤害吸收生命值”参数<!--by jishaobin-->

1. 调整[DelServerPlayerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#DelServerPlayerEvent)，新增触发时机描述<!--by jishaobin-->

1. 调整[EntityRemoveEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#EntityRemoveEvent)，增加触发时机描述<!--by jishaobin-->

1. 调整[ItemReleaseUsingServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ItemReleaseUsingServerEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[OnCarriedNewItemChangedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#OnCarriedNewItemChangedServerEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[PlayerEatFoodServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#PlayerEatFoodServerEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[PlayerInteractServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#PlayerInteractServerEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ServerItemTryUseEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ServerItemTryUseEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ServerItemUseOnEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ServerItemUseOnEvent)，修改触发时机描述。物品相关参数改为物品信息字典。<!--by jishaobin-->

1. 调整[ServerPlayerTryTouchEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#ServerPlayerTryTouchEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ActorAcquiredItemClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ActorAcquiredItemClientEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ActorUseItemClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ActorUseItemClientEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[ClientItemTryUseEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ClientItemTryUseEvent)，物品相关参数改为物品信息字段<!--by czh-->

1. 调整[ClientItemUseOnEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ClientItemUseOnEvent)，物品相关参数改为物品信息字段<!--by czh-->

1. 调整[ItemReleaseUsingClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#ItemReleaseUsingClientEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[OnCarriedNewItemChangedClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#OnCarriedNewItemChangedClientEvent)，物品相关参数改为物品信息字典<!--by czh-->

1. 调整[StartUsingItemClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#StartUsingItemClientEvent)，物品相关参数改为物品信息字段<!--by czh-->

1. 调整[StopUsingItemClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.md#StopUsingItemClientEvent)，物品相关参数改为物品信息字段<!--by czh-->

1. 调整[GetAttrMaxValue](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetAttrMaxValue)，新增ABSORPTION(伤害吸收生命值)类型支持<!--by jishaobin-->

1. 调整[GetAttrValue](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetAttrValue)，新增ABSORPTION(伤害吸收生命值)类型支持<!--by jishaobin-->

1. 调整[SetAttrMaxValue](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetAttrMaxValue)，新增类型说明<!--by jishaobin-->

1. 调整[SetAttrValue](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetAttrValue)，新增类型说明<!--by jishaobin-->

1. 调整[PlaySystemSound](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#PlaySystemSound)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可在对应维度的常加载区块播放游戏音效<!--by liaoyi-->

1. 调整[CheckBlockToPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#CheckBlockToPos)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可判断对应维度的常加载区块内位置之间是否有方块<!--by liaoyi-->

1. 调整[GetBlockLightLevel](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetBlockLightLevel)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可获取对应维度的常加载区块内光照等级<!--by liaoyi-->

1. 调整[GetBlockNew](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetBlockNew)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可在对应维度的常加载区块获取方块<!--by liaoyi-->

1. 调整[SetBlockNew](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetBlockNew)，增加参数dimensionId，默认为-1，传入非负值时不依赖playerId，可在对应维度的常加载区块设置方块<!--by liaoyi-->

1. 调整[SpawnResources](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SpawnResources)，新增dimensionId，默认为-1，传入非负值时用于控制产生方块掉落的维度，可在对应维度的常加载区块产生掉落<!--by liaoyi-->

1. 调整[GetBlockStates](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetBlockStates)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可获取对应维度的常加载区块内方块状态<!--by liaoyi-->

1. 调整[SetBlockStates](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetBlockStates)，增加参数dimensionId，默认为-1，传入非负值时不依赖playerId，可设置对应维度的常加载区块内方块状态<!--by liaoyi-->

1. 调整[GetChestBoxSize](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetChestBoxSize)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可获取对应维度的常加载区块内箱子容量<!--by liaoyi-->

1. 调整[SetChestBoxItemNum](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetChestBoxItemNum)，增加参数dimensionId，默认为-1，传入非负值时不依赖playerId，可在对应维度的常加载区块设置箱子内物品数量<!--by liaoyi-->

1. 调整[GetEntitiesInSquareArea](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetEntitiesInSquareArea)，新增dimensionId参数，默认为-1，传入非负值时不依赖entityId，可获取对应维度的常加载区块内的实体列表<!--by liaoyi-->

1. 调整[PlaceStructure](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#PlaceStructure)，增加参数dimensionId，默认为-1，传入非负值时不依赖playerId，可在对应维度的常加载区块放置结构<!--by liaoyi-->

1. 调整[GetItemBasicInfo](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetItemBasicInfo)，返回信息新增挖掘相关属性tierDict<!--by jishaobin-->

1. 调整[SpawnItemToChestBlock](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SpawnItemToChestBlock)，增加参数dimensionId，默认为-1，传入非负值时不依赖playerId，可生成物品到对应维度的常加载区块内的箱子<!--by liaoyi-->

1. 调整[SetFootPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetFootPos)，修改行为与使用tp命令一致<!--by jishaobin-->

1. 调整[SetPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#SetPos)，修改行为与使用tp命令一致<!--by jishaobin-->

1. 调整[GetStrength](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.md#GetStrength)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId，可获取对应维度的常加载区块内红石信号强度<!--by liaoyi-->

1. 调整[GetBlock](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetBlock)，支持CreateBlockInfo时传入levelId，可获取到已加载区块中的方块信息<!--by liaoyi-->

1. 调整[GetEntityInArea](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetEntityInArea)，支持传入entityId为None，此时exceptEntity无作用，可获取到区域范围内已加载的实体列表<!--by liaoyi-->

1. 调整[GetItemBasicInfo](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.md#GetItemBasicInfo)，返回信息新增挖掘相关属性tierDict<!--by jishaobin-->

1. 增加了特殊情况下控件的路径变化说明，详见[UI说明文档](60-UI/4-UI说明文档.md#特殊情况下的根节点路径变化) <!--by panlei-->

1. 增加了图片控件[序列帧](60-UI/4-UI说明文档.md#序列帧)相关说明 <!--by panlei-->

1. [富文本](60-UI/4-UI说明文档.md#如何使用富文本)现在支持文本字体大小、缩放倍率、字体颜色设置<!--by panlei-->

**2020.09.24：版本号（v1.19  BE1.14.30）**

- 版本重大更新

1. 新增NeteasePaperDoll控件支持在UI上渲染生物模型，包括玩家与其他生物,既可以是生物类型,也可以是具体的生物实例。生物模型既可以是原版模型，也可以是骨骼模型。详情请查阅[RenderPaperDoll](60-UI/5-UIAPI文档.html#RenderPaperDoll))
2. 允许动态修改玩家的渲染，包括渲染几何体，渲染动画以及动画控制器，渲染贴图等。详情请查阅组件[actorRender](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#actorRender)相关的接口

- 新增

1. 自定义方块添加[netease:may_place_on](03-自定义游戏内容/05-自定义方块/1-JSON组件.html#netease-may-place-on)组件
2. 新增[GetEntityLimit](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#GetEntityLimit)，获取当前level最大实体数量<!--by lidi-->
3. 新增[GetPlayerList](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#GetPlayerList)，获取获取level中所有玩家的id列表<!--by lidi-->
4. 新增[SetEntityLimit](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#SetEntityLimit)，设置以玩家为中心，6个chunk范围内的最大实体数量<!--by lidi-->
5. 新增[StartRecordEvent](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartRecordEvent)，开始启动服务端与客户端之间的脚本事件收发包统计<!--by xltang-->
6. 新增[StartRecordPacket](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartRecordPacket)，开始启动服务端与客户端之间的引擎收发包统计<!--by xltang-->
7. 新增[StopRecordEvent](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopRecordEvent)，停止服务端与客户端之间的脚本事件收发包统计并输出结果<!--by xltang-->
8. 新增[StopRecordPacket](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopRecordPacket)，停止服务端与客户端之间的引擎收发包统计并输出结果<!--by xltang-->
9. 新增[HideAirSupplyGUI](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideAirSupplyGUI)，隐藏hud界面的氧气条显示<!--by why117-->
10. 新增[HideExpGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideExpGui)，新增隐藏经验条接口<!--by why117-->
11. 新增[HideMoveGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideMoveGui)，新增隐藏移动按钮<!--by lidi-->
12. 新增[ChangeLevelUpCostServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ChangeLevelUpCostServerEvent)，获取玩家下一个等级升级经验事件，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次<!--by xltang-->
13. 新增[ChunkAcquireDiscardedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ChunkAcquireDiscardedServerEvent)，在监听白名单内的服务端区块即将被卸载事件<!--by liaoyi-->
14. 新增[ChunkLoadedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ChunkLoadedServerEvent)，在监听白名单内的服务端区块加载完成事件<!--by liaoyi-->
15. 新增[EntityDieLoottableServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#EntityDieLoottableServerEvent)，生物死亡掉落物品事件<!--by lidi-->
16. 新增[EntityPlaceBlockAfterServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#EntityPlaceBlockAfterServerEvent)，生物成功放置方块后触发<!--by czh-->
17. 新增[GameTypeChangedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#GameTypeChangedServerEvent)，个人游戏模式发生变化事件<!--by gzhuabo-->
18. 新增[OnContainerFillLoottableServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnContainerFillLoottableServerEvent)，随机奖励箱填充事件<!--by lidi-->
19. 新增[SpawnProjectileServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#SpawnProjectileServerEvent)，抛射物生成事件<!--by czh-->
20. 新增[WillAddEffectServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#WillAddEffectServerEvent)，实体即将获得状态效果<!--by xltang-->
21. 新增[ChunkAcquireDiscardedClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#ChunkAcquireDiscardedClientEvent)，在监听白名单内的客户端区块即将被卸载事件<!--by liaoyi-->
22. 新增[ChunkLoadedClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#ChunkLoadedClientEvent)，在监听白名单内的客户端区块加载完成事件<!--by liaoyi-->
23. 新增[GameTypeChangedClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#GameTypeChangedClientEvent)，个人游戏模式发生变化事件<!--by gzhuabo-->
24. 新增[GetEntityByCoordReleaseClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#GetEntityByCoordReleaseClientEvent)，点击屏幕后松开事件<!--by czh-->
25. 新增[OnCommandOutputClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#OnCommandOutputClientEvent)，增加命令及命令组件有返回值时事件<!--by lidi-->
26. 新增[GetFootPos](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetFootPos)，获取实体脚底的位置<!--by liaoyi-->
27. 新增[GetHoldTimeThresholdInMs](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetHoldTimeThresholdInMs)，获取长按判定时间<!--by czh-->
28. 新增[SetHoldTimeThreshold](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetHoldTimeThreshold)，设置长按判定时间<!--by czh-->
29. 新增[GetCameraAnchor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetCameraAnchor)，获取相机锚点<!--by jishaobin-->
30. 新增[SetCameraAnchor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetCameraAnchor)，设置相机锚点<!--by jishaobin-->
31. 新增[SetFadeDistance](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetFadeDistance)，设置序列帧开始自动调整透明度的距离<!--by liaoyi-->
32. 新增[SetMixColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetMixColor)，增加设置序列帧混合颜色的方法<!--by sutao-->
33. 新增[SetUsePointFiltering](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetUsePointFiltering)，设置序列帧是否使用点滤波<!--by liaoyi-->
34. 新增[SetFadeDistance](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SetFadeDistance)，设置粒子开始自动调整透明度的距离<!--by liaoyi-->
35. 新增[SimulateTouchWithMouse](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#SimulateTouchWithMouse)，新增模拟使用鼠标控制UI（PC的F11快捷键）<!--by gzhuabo-->
36. 新增[BindModelToEntity](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#BindModelToEntity)，给替换骨骼模型的实体的骨骼上挂接其他骨骼模型<!--by czh-->
37. 新增[GetAllBindModelToEntity](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetAllBindModelToEntity)，获取实体上挂接的骨骼模型<!--by czh-->
38. 新增[UnBindModelToEntity](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#UnBindModelToEntity)，取消实体上挂接的某个骨骼模型<!--by czh-->
39. 新增[AddPlayerAnimation](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerAnimation)，增加玩家渲染动画<!--by gzhuabo-->
40. 新增[AddPlayerAnimationController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerAnimationController)，增加玩家渲染动画控制器<!--by gzhuabo-->
41. 新增[AddPlayerGeometry](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerGeometry)，增加玩家渲染几何体<!--by gzhuabo-->
42. 新增[AddPlayerTexture](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerTexture)，增加玩家渲染贴图<!--by gzhuabo-->
43. 新增[RemovePlayerAnimationController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemovePlayerAnimationController)，移除玩家渲染动画控制器<!--by gzhuabo-->
44. 新增[RemovePlayerGeometry](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemovePlayerGeometry)，删除玩家渲染几何体<!--by gzhuabo-->
45. 新增[AddChunkPosWhiteList](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddChunkPosWhiteList)，为客户端区块加载完成、准备卸载事件添加监听<!--by liaoyi-->
46. 新增[RemoveChunkPosWhiteList](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemoveChunkPosWhiteList)，为客户端区块加载完成、准备卸载事件移除监听<!--by liaoyi-->
47. 新增[AddBlockItemListenForUseEvent](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddBlockItemListenForUseEvent)，增加原版方块对ClientBlockUseEvent事件的脚本层监听<!--by gzhuabo-->
48. 新增[ClearAllListenForBlockUseEventItems](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#ClearAllListenForBlockUseEventItems)，清空原版方块白名单列表对ClientBlockUseEvent事件的脚本层监听<!--by gzhuabo-->
49. 新增[RemoveBlockItemListenForUseEvent](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemoveBlockItemListenForUseEvent)，移除原版方块对ClientBlockUseEvent事件的脚本层监听<!--by gzhuabo-->
50. 新增[CleanBlockTileEntityCustomData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#CleanBlockTileEntityCustomData)，清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。<!--by xltang-->
51. 新增[GetBlockTileEntityCustomData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockTileEntityCustomData)，读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据<!--by xltang-->
52. 新增[GetBlockTileEntityWholeCustomData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockTileEntityWholeCustomData)，读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。<!--by xltang-->
53. 新增[GetChestPairedPosition](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetChestPairedPosition)，获取与箱子A合并成一个大箱子的箱子B的坐标<!--by xltang-->
54. 新增[SetBlockTileEntityCustomData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetBlockTileEntityCustomData)，设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。<!--by xltang-->
55. 新增[SetRecoverTotalAirSupplyTime](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetRecoverTotalAirSupplyTime)，设置恢复最大氧气量的时间<!--by why117-->
56. 新增[AddChunkPosWhiteList](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#AddChunkPosWhiteList)，为服务端区块加载完成、准备卸载事件添加监听<!--by liaoyi-->
57. 新增[RemoveChunkPosWhiteList](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#RemoveChunkPosWhiteList)，为服务端区块加载完成、准备卸载事件移除监听<!--by liaoyi-->
58. 新增[SetCanActorSetOnFireByLightning](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetCanActorSetOnFireByLightning)，禁止/允许闪电点燃实体<!--by xltang-->
59. 新增[SetCanBlockSetOnFireByLightning](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetCanBlockSetOnFireByLightning)，禁止/允许闪电点燃方块<!--by xltang-->
60. 新增[UpgradeMapDimensionVersion](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#UpgradeMapDimensionVersion)，提升指定地图维度的版本号，版本号不符的维度，地图存档信息将被废弃<!--by xltang-->
61. 新增[ClearPlayerOffHand](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ClearPlayerOffHand)，清除玩家左手物品<!--by xltang-->
62. 新增[GetCustomName](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetCustomName)，获取物品的自定义名称，与铁砧修改的名称一致<!--by czh-->
63. 新增[GetDroppedItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetDroppedItem)，新增获取掉落在世界的指定entityid的物品信息<!--by why117-->
64. 新增[GetEntityItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEntityItem)，支持获取生物身上的物品<!--by lidi-->
65. 新增[GetPlayerAllItems](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetPlayerAllItems)，获取制定槽位的批量物品信息<!--by why117-->
66. 新增[SetCustomName](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetCustomName)，设置物品的自定义名称<!--by czh-->
67. 新增[SetEntityItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetEntityItem)，支持设置生物身上的物品<!--by lidi-->
68. 新增[SetPlayerAllItems](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetPlayerAllItems)，设置玩家制定槽位物品信息<!--by xltang-->
69. 新增[GetFootPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetFootPos)，获取实体脚底的位置<!--by liaoyi-->
70. 新增[SetFootPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetFootPos)，设置实体脚所在的位置<!--by liaoyi-->
71. 新增[ClearDefinedLevelUpCost](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ClearDefinedLevelUpCost)，清理自定义的升级经验，清理后才有会再次回调ChangeLevelUpCostServerEvent事件并再次设置新的升级经验值。<!--by xltang-->
72. 新增[IsSwiming](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#IsSwiming)，获取玩家是否处于游泳状态<!--by xltang-->
73. 新增[LocateNeteaseFeature](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#LocateNeteaseFeature)，定位由网易自定义特征放置的结构<!--by liaoyi-->
74. 新增[LocateStructureFeature](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#LocateStructureFeature)，定位原版的部分结构<!--by liaoyi-->
75. 新增[ChangePlayerFlyState](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ChangePlayerFlyState)，改变玩家的飞行状态<!--by gzhuabo-->
76. 新增[GetBlockAuxValueFromStates](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockAuxValueFromStates)，根据方块名称和[方块状态](02-Python脚本开发/99-ModAPI/0-名词解释.html#方块状态)获取方块附加值AuxValue<!--by gzhuabo-->
77. 新增[GetEditText](60-UI/5-UIAPI文档.html#GetEditText)，获取edit_box输入框的文本信息<!--by lidi-->
78. 新增[GetRichTextItem](60-UI/5-UIAPI文档.html#GetRichTextItem)，返回一个富文本控件实例<!--by panlei-->
79. 新增[GetScrollViewPos](60-UI/5-UIAPI文档.html#GetScrollViewPos)，支持获得当前scroll_view最上方内容的位置<!--by panlei-->
80. 新增[RenderPaperDoll](60-UI/5-UIAPI文档.html#RenderPaperDoll)，渲染生物模型<!--by gzhuabo-->
81. 新增[SetAlpha](60-UI/5-UIAPI文档.html#SetAlpha)，设置控件透明度<!--by lidi-->
82. 新增[SetEditText](60-UI/5-UIAPI文档.html#SetEditText)，设置edit_box输入框的文本信息<!--by lidi-->
83. 新增[SetScrollViewPercentValue](60-UI/5-UIAPI文档.html#SetScrollViewPercentValue)，支持设置当前scroll_view内容的百分比位置<!--by panlei-->
84. 新增[SetScrollViewPos](60-UI/5-UIAPI文档.html#SetScrollViewPos)，支持设置当前scroll_view内容的位置<!--by panlei-->
85. 新增[SetSpriteUV](60-UI/5-UIAPI文档.html#SetSpriteUV)，设置UI图片控件的uv<!--by czh-->
86. 新增[SetSpriteUVSize](60-UI/5-UIAPI文档.html#SetSpriteUVSize)，设置UI图片控件的uv大小<!--by czh-->
87. 新增[SetToggleState](60-UI/5-UIAPI文档.html#SetToggleState)，设置Toggle开关控件的值<!--by sutao-->
88. 新增[ImmuneDamage](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ImmuneDamage)，设置实体是否免疫伤害<!--by gzhuabo-->

- 调整

1. [自定义音乐](03-自定义游戏内容/09-自定义音乐.html)中，*sound_definitions.json*内的stream字段可以设置为true了
2. 调整[HideSlotBarGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideSlotBarGui)，增加hideslotbar使用说明。隐藏后点击相应位置不会响应<!--by wanghaoyu-->
3. 调整[DestroyEntity](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#DestroyEntity)，增加销毁实体返回值<!--by gzhuabo-->
4. 调整[OnCarriedNewItemChangedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnCarriedNewItemChangedServerEvent)，新增关键字oldItemDict、newItemDict<!--by xltang-->
5. 调整[OnNewArmorExchangeServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnNewArmorExchangeServerEvent)，新增关键字oldArmorDict、newArmorDict<!--by xltang-->
6. 调整[OnOffhandItemChangedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#OnOffhandItemChangedServerEvent)，新增关键字oldItemDict、newItemDict<!--by xltang-->
7. 调整[ClientPlayerInventoryOpenEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#ClientPlayerInventoryOpenEvent)，新增cancel参数<!--by why117-->
8. 调整[GetCurrentAirSupply](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetCurrentAirSupply)，新增备注说明<!--by why117-->
9. 调整[GetMaxAirSupply](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetMaxAirSupply)，新增备注说明<!--by why117-->
10. 调整[SetCurrentAirSupply](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetCurrentAirSupply)，新增备注说明<!--by why117-->
11. 调整[SetMaxAirSupply](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetMaxAirSupply)，新增备注说明<!--by why117-->
12. 调整[SetGameRulesInfoServer](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetGameRulesInfoServer)，增加返回值<!--by gzhuabo-->
13. 调整[SetHurtByEntity](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetHurtByEntity)，新增参数knocked，可设置是否产生击退<!--by xltang-->
14. 调整[GetEquItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEquItemDurability)，新增支持获取生物装备槽位中盔甲的耐久值<!--by lidi-->
15. 调整[GetEquItemEnchant](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEquItemEnchant)，新增支持获取生物装备槽位中盔甲的附魔<!--by lidi-->
16. 调整[SetEquItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetEquItemDurability)，新增支持设置生物装备槽位中盔甲的耐久值<!--by lidi-->
17. 调整[AddBlockItemListenForUseEvent](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#AddBlockItemListenForUseEvent)，去掉增加原版方块监听ServerBlockUseEvent事件时同步到客户端的功能<!--by gzhuabo-->
18. 调整[ClearAllListenForBlockUseEventItems](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ClearAllListenForBlockUseEventItems)，去掉清空原版方块监听ServerBlockUseEvent事件时同步到客户端的功能<!--by gzhuabo-->
19. 调整[RemoveBlockItemListenForUseEvent](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#RemoveBlockItemListenForUseEvent)，去掉移除原版方块监听ServerBlockUseEvent事件时同步到客户端的功能<!--by gzhuabo-->
20. 调整[GetBiomeName](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBiomeName)，添加维度参数，并支持获取未加载区块的群系，不再需要使用playerId创建comp<!--by czh-->



**2020.08.27：版本号（v1.18  BE1.14.30）**

- 新增

1. 移除了“TestUIMod”示例，请参考“UIDemoMod”

* 调整

1. 完善[自定义农作物](03-自定义游戏内容/05-自定义方块/3-特殊方块/3-自定义农作物方块.md)文档，细化了自定义农作物的过程说明
2. 整理[portalGateDemo](../4-DEMO示例/示例简介.md#portalGateDemo)示例，优化代码的可读性



**2020.08.18：版本号（v1.18  BE1.14.30）**

* 新增

1. 新增自定义音乐功能，详见[自定义音乐](03-自定义游戏内容/09-自定义音乐.md)文档以及 customAudio组件（2020.08.18维护后生效）



**2020.08.07：版本号（v1.18  BE1.14.30）**

* 新增

1. 新增[Disable](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#Disable)，禁用官方伙伴功能<!--by gzhuabo-->
2. 新增[Enable](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#Enable)，开启官方伙伴功能<!--by gzhuabo-->



**2020.07.10：版本号（v1.18  BE1.14.30）**

* 新增

1. 新增支持自定义红石，新增内容详见[4-自定义红石方块](03-自定义游戏内容/05-自定义方块/3-特殊方块/4-自定义红石方块.md)<!--by gzhuabo-->
2. 新增自定义传送门示例（portalGateDemo），使用portal组件，DimensionChangeFinishServerEvent与extraData组件实现类似原版地狱传送门，可以搭建传送门并在自定义维度之间传送的功能<!--by gzhuabo and why117-->
3. 新增UIDemoMod相关说明，新增内容详见[4-UI说明文档](60-UI/4-UI说明文档.md) <!--by panlei-->

* **调整**

1. 自定义方块模型文档根据MCStudio功能进行优化，现在可以使用BlockBench的自由模型进行编辑，并使用MCStudio导入到addon了
2. 完善自定义熔炉，新增内容详见[自定义熔炉demo](03-自定义游戏内容/05-自定义方块/a-自定义熔炉.html)<!--by  ld-->
3. 模型制作文档优化，内容详见[模型和动作](http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/81-资源制作/1-模型和动作)<!--by gzhuabo-->
4. 完善自定义生物demo，使用queryVariable和actorRender组件实现动态改变生物的材质，内容详见[自定义基础生物](03-自定义游戏内容/06-自定义生物/01-自定义基础生物.md)与自定义生物示例demo<!--by gzhuabo-->
5. 去掉armorSlot组件的描述。请使用item组件的GetPlayerItem以及SpawnItemToPlayerInv代替

**2020.06.11：版本号（v1.18beta  BE1.14.30）**

* **新增**

1. 支持开关控件，详见《UI说明文档》 <!--by hyk-->
2. 支持类弓箭效果自定义，详见文档[自定义蓄力物品](03-自定义游戏内容/03-自定义物品/5-自定义蓄力物品.md)<!--by gzhuabo-->
3. 支持自定义抛射物，详见文档[自定义远程武器](03-自定义游戏内容/07-自定义远程武器.html)<!--by gzhuabo-->
4. 新增[GetUseEventTuple](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#GetUseEventTuple),获取当前是否设置开启事件支持tuple元组<!--by hongshubin-->
5. 新增[SetUseEventTuple](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#SetUseEventTuple),设置开启事件支持tuple元组<!--by hongshubin-->
6. 新增[StartMultiProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartMultiProfile),开始启动服务端与客户端双端脚本性能分析<!--by hongshubin-->
7. 新增[StartProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StartProfile),开始启动服务端脚本性能分析<!--by hongshubin-->
8. 新增[StopMultiProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopMultiProfile),停止双端脚本性能分析并生成火焰图<!--by hongshubin-->
9. 新增[StopProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#StopProfile),停止服务端脚本性能分析并生成火焰图<!--by hongshubin-->
10. 新增[GetUseEventTuple](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#GetUseEventTuple),获取当前是否设置开启事件支持tuple元组<!--by hongshubin-->
11. 新增[HideHealthGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideHealthGui),隐藏hud界面的血量显示<!--by czh-->
12. 新增[HideHungerGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#HideHungerGui),隐藏hud界面的饥饿值显示<!--by czh-->
13. 新增[SetUseEventTuple](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#SetUseEventTuple),设置开启事件支持tuple元组<!--by hongshubin-->
14. 新增[StartMultiProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#StartMultiProfile),开始启动服务端与客户端双端脚本性能分析<!--by hongshubin-->
15. 新增[StartProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#StartProfile),开始启动客户端脚本性能分析<!--by hongshubin-->
16. 新增[StopMultiProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#StopMultiProfile),停止双端脚本性能分析并生成火焰图<!--by hongshubin-->
17. 新增[StopProfile](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#StopProfile),停止客户端端脚本性能分析并生成火焰图<!--by hongshubin-->
18. 新增[GetPlatform](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#GetPlatform),获取脚本运行的平台<!--by gzhuabo-->
19. 新增[UnListenAllEvents](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#UnListenAllEvents),反注册监听某个系统抛出的所有事件，即不再监听。<!--by gzhuabo-->
20. 新增[ActorHurtServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ActorHurtServerEvent),生物受伤事件<!--by gzhuabo-->
21. 新增[BlockRemoveServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#BlockRemoveServerEvent),自定义方块被移除时触发<!--by gzhuabo-->
22. 新增[BlockStrengthChangedServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#BlockStrengthChangedServerEvent),自定义机械元件方块红石信号量发生变化事件<!--by gzhuabo-->
23. 新增[ChestBlockTryPairWithServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ChestBlockTryPairWithServerEvent),两个并排的小箱子方块组合为一个大箱子事件<!--by xltang-->
24. 新增[DimensionChangeFinishServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#DimensionChangeFinishServerEvent),新增玩家改变维度事件<!--by why117-->
25. 新增[ItemReleaseUsingServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#ItemReleaseUsingServerEvent),释放正在使用的物品事件<!--by gzhuabo-->
26. 新增[PlayerDropItemServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#PlayerDropItemServerEvent),新增玩家丢弃物品事件<!--by why117-->
27. 新增[AddEntityClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#AddEntityClientEvent),新增actor实体加入玩家区块范围触发的AOI事件<!--by why117-->
28. 新增[AddPlayerAOIClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#AddPlayerAOIClientEvent),增加客户端玩家进入区块的AOI事件<!--by why117-->
29. 新增[GridComponentSizeChangedClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#GridComponentSizeChangedClientEvent),新增grid控件size大小发生变化触发的事件<!--by why117-->
30. 新增[ItemReleaseUsingClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#ItemReleaseUsingClientEvent),释放正在使用的物品事件<!--by gzhuabo-->
31. 新增[RemoveEntityClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#RemoveEntityClientEvent),新增actor实体离开玩家区块范围触发的AOI事件<!--by why117-->
32. 新增[RemovePlayerAOIClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#RemovePlayerAOIClientEvent),增加客户端玩家离开区块的AOI事件<!--by why117-->
33. 新增[CreateSFXTextBoard](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#CreateSFXTextBoard),新增跟随实体的文字面板<!--by why117-->
34. 新增[GetBodyRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetBodyRot),获取实体的身体角度，默认角度为头部角度<!--by guoxun-->
35. 新增[GetItemEffectName](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetItemEffectName),获取物品的状态描述<!--by gzhuabo-->
36. 新增[GetItemFormattedHoverText](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetItemFormattedHoverText),获取物品格式化hover文本<!--by gzhuabo-->
37. 新增[GetItemHoverName](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetItemHoverName),获取物品的Hover名称<!--by gzhuabo-->
38. 新增[GetMotion](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetMotion),增加获取生物瞬时移动方向向量接口<!--by gzhuabo-->
39. 新增[GetAmbientBrightness](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetAmbientBrightness),获取环境光亮度<!--by hongshubin-->
40. 新增[GetMoonRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetMoonRot),获取月亮角度<!--by hongshubin-->
41. 新增[GetSkyColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetSkyColor),获取天空颜色<!--by hongshubin-->
42. 新增[GetSkyTextures](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetSkyTextures),获取当前维度天空盒贴图<!--by hongshubin-->
43. 新增[GetStarBrightness](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetStarBrightness),获取星星亮度<!--by hongshubin-->
44. 新增[GetSunRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetSunRot),获取太阳角度<!--by hongshubin-->
45. 新增[GetUseAmbientBrightness](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseAmbientBrightness),判断是否在mod设置了环境光亮度<!--by hongshubin-->
46. 新增[GetUseMoonRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseMoonRot),判断是否在mod设置了月亮角度<!--by hongshubin-->
47. 新增[GetUseSkyColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseSkyColor),判断是否在mod设置了天空颜色<!--by hongshubin-->
48. 新增[GetUseStarBrightness](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseStarBrightness),判断是否在mod设置了星星亮度<!--by hongshubin-->
49. 新增[GetUseSunRot](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseSunRot),判断是否在mod设置了太阳角度<!--by hongshubin-->
50. 新增[AddActorRenderController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddActorRenderController),增加生物渲染控制器<!--by gzhuabo-->
51. 新增[AddActorRenderMaterial](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddActorRenderMaterial),增加生物渲染材质<!--by gzhuabo-->
52. 新增[AddPlayerRenderController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerRenderController),增加玩家渲染控制器<!--by gzhuabo-->
53. 新增[AddPlayerRenderMaterial](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#AddPlayerRenderMaterial),增加玩家渲染材质<!--by gzhuabo-->
54. 新增[RebuildActorRender](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RebuildActorRender),重建生物渲染控制器<!--by gzhuabo-->
55. 新增[RebuildPlayerRender](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RebuildPlayerRender),重建玩家渲染控制器<!--by gzhuabo-->
56. 新增[RemoveActorRenderController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemoveActorRenderController),删除生物渲染控制器<!--by gzhuabo-->
57. 新增[RemovePlayerRenderController](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#RemovePlayerRenderController),删除玩家渲染控制器<!--by gzhuabo-->
58. 新增[GetFogColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetFogColor),获取当前雾效颜色<!--by hongshubin-->
59. 新增[GetFogLength](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetFogLength),获取雾效范围<!--by hongshubin-->
60. 新增[GetUseFogColor](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseFogColor),判断当前是否开启设置雾效颜色<!--by hongshubin-->
61. 新增[GetUseFogLength](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetUseFogLength),判断当前是否开启设置雾效范围<!--by hongshubin-->
62. 新增[getUid](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#getUid),客户端获取本机玩家uid<!--by why117-->
63. 新增[isGliding](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isGliding),获取玩家是否鞘翅飞行<!--by gzhuabo-->
64. 新增[isInLava](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isInLava),获取玩家是否在岩浆中<!--by gzhuabo-->
65. 新增[isInWater](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isInWater),获取玩家是否在水中<!--by gzhuabo-->
66. 新增[isMoving](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isMoving),获取玩家是否在行走<!--by gzhuabo-->
67. 新增[isOnGround](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isOnGround),获取玩家是否触地<!--by gzhuabo-->
68. 新增[isRiding](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isRiding),获取玩家是否在骑乘<!--by gzhuabo-->
69. 新增[isSneaking](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isSneaking),获取玩家是否在潜行<!--by gzhuabo-->
70. 新增[isSprinting](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isSprinting),获取玩家是否在疾跑<!--by gzhuabo-->
71. 新增[isSwimming](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#isSwimming),获取玩家是否在游泳<!--by gzhuabo-->
72. 新增[setMoving](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setMoving),设置本地玩家行走<!--by gzhuabo-->
73. 新增[setSneaking](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setSneaking),设置玩家是否潜行<!--by gzhuabo-->
74. 新增[setSprinting](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setSprinting),设置玩家是否疾跑<!--by gzhuabo-->
75. 新增[Get](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#Get)，获取实体计算节点的值<!--by gzhuabo-->
76. 新增[Register](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#Register)，注册实体计算节点<!--by gzhuabo-->
77. 新增[Set](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#Set)，设置实体计算节点的值<!--by gzhuabo-->
78. 新增[UnRegister](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#UnRegister)，反注册实体计算节点<!--by gzhuabo-->
79. 新增[IsEntityOnFire](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#IsEntityOnFire),获取实体是否着火<!--by gzhuabo-->
80. 新增[SetEntityOnFire](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetEntityOnFire),设置实体是否着火<!--by gzhuabo-->
81. 新增[GetBlockEntityData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockEntityData),获取方块（包括自定义方块）的数据<!--by gzhuabo-->
82. 新增[SpawnResources](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SpawnResources),产生方块随机掉落<!--by gzhuabo-->
83. 新增[CleanExtraData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#CleanExtraData),清理指定key的实体数据/全局数据，数据存放到leveldb。<!--by xltang-->
84. 新增[GetWholeExtraData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetWholeExtraData),获取完整的实体数据/全局数据字典，数据存放到leveldb。<!--by xltang-->
85. 新增[ForbidLiquidFlow](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ForbidLiquidFlow),禁止/允许地图中的流体流动<!--by xltang-->
86. 新增[LookupItemByName](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#LookupItemByName),判定指定identifier的物品是否存在<!--by xltang-->
87. 新增[OpenCityProtect](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#OpenCityProtect),开启城市保护，包括禁止破坏方块，禁止对方块使用物品，禁止怪物攻击玩家，禁止玩家之间互相攻击，禁止日夜切换，禁止天气变化，禁止怪物群落刷新<!--by xltang-->
88. 新增[SetGameDifficulty](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetGameDifficulty),设置游戏难度<!--by liaoyi-->
89. 新增[ClearPlayerOffHand](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ClearPlayerOffHand),清除玩家左手物品<!--by xltang-->
90. 新增[GetDroppedItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetDroppedItem),新增获取玩家丢弃在世界的物品的entityId的接口<!--by why117-->
91. 新增[GetEquItemEnchant](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetEquItemEnchant),新增获取装备槽位中盔甲的附魔<!--by why117-->
92. 新增[GetItemBasicInfo](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetItemBasicInfo),新增获取物品的基础信息<!--by why117-->
93. 新增[SpawnItemToArmor](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SpawnItemToArmor),添加物品到玩家装备位<!--by xltang-->
94. 新增[SetRiderRideEntity](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetRiderRideEntity),新增实体骑乘生物接口<!--by why117-->
95. 新增[ChangeSelectSlot](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#ChangeSelectSlot),设置玩家当前选中快捷栏物品的index<!--by xltang-->
96. 新增[IsSneaking](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#IsSneaking),获取玩家是否处于潜行状态<!--by xltang-->
97. 新增[CanPlayerFly](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#CanPlayerFly)，获取玩家是否有飞行的能力<!--by gzhuabo-->
98. 新增[CreateProjectileEntity](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#CreateProjectileEntity)，创建抛射物（直接发射）<!--by gzhuabo-->

99. 新增[GetBlockStates](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockStates)，获取方块状态<!--by gzhuabo-->

100. 新增[GetBlockStatesFromAuxValue](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetBlockStatesFromAuxValue)，根据方块名称和方块附加值AuxValue获取方块状态<!--by gzhuabo-->

101. 新增[SetBlockStates](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetBlockStates)，设置方块状态<!--by gzhuabo-->

102. 新增[GetStrength](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetStrength)，获取某个坐标的红石信号强度<!--by gzhuabo-->

103. 新增[GetMotion](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetMotion)，获取生物的瞬时移动方向向量<!--by gzhuabo-->

104. 新增[SetMotion](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetMotion)，设置生物瞬时移动方向向量<!--by gzhuabo-->

105. 新增[SpawnLootTable](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SpawnLootTable)，生成生物一次随机掉落<!--by gzhuabo-->

106. 新增[SpawnLootTableWithActor](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SpawnLootTableWithActor)，使用生物Id生成一次随机掉落<!--by gzhuabo-->

107. 新增[DetectStructure](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#DetectStructure)，检测自定义门的结构<!--by gzhuabo-->
108. 新增[GetText](60-UI/5-UIAPI文档.html#GetText),获取Label的文本信息<!--by liaoyi-->
109. 新增[SetSpriteColor](60-UI/5-UIAPI文档.html#SetSpriteColor),设置图片颜色<!--by lioneldy-->
110. 新增[SetUiModelScale](60-UI/5-UIAPI文档.html#SetUiModelScale),支持单独设置PaperDoll控件模型的缩放比例<!--by guoxun-->

- 调整

1. 调整[AddEntityServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#AddEntityServerEvent),当实体为物品实体时增加参数itemName和auxValue<!--by gzhuabo-->
2. 调整[DamageEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#DamageEvent),参数击退及点燃支持修改<!--by guoxun-->
3. 调整[EntityStopRidingEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#EntityStopRidingEvent),支持取消实体下马功能<!--by gzhuabo-->
4. 调整[EntityStopRidingEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#EntityStopRidingEvent),支持取消下马操作<!--by gzhuabo-->
5. 调整[GetItemBasicInfo](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#GetItemBasicInfo),itemdict增加耐久值参数<!--by why117-->
6. 调整[SetBlockNew](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#SetBlockNew),增加参数oldBlockHandling，默认为替换replace<!--by gzhuabo-->
7. 调整[GetPlayerItem](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#GetPlayerItem)，增加获取userData的参数，默认不获取<!--by gzhuabo-->
7. 调整[AddTouchEventHandler](60-UI/5-UIAPI文档.html#AddTouchEventHandler),新增TouchMoveIn/TouchMoveOut事件<!--by gzhuabo-->
8. 调整[SetUiItem](60-UI/5-UIAPI文档.html#SetUiItem),新增支持显示附魔效果及各种附带userData的物品（如灾厄旗帜、纺织过的各种旗帜）<!--by lioneldy-->
9. 调整[SetUiModel](60-UI/5-UIAPI文档.html#SetUiModel),新增默认动作名称以及是否循环播放参数<!--by gzhuabo-->



**2020.05.12：版本号（v1.17 BE1.13.3）**

<!--toVer: 2020.02.20-->

- 新增

1. 新增文档[骨骼模型的使用](81-资源制作/1-模型和动作/04-骨骼模型的使用.html)文档，说明了如何添加第一人称骨骼模型。<!--by yqc-->



**2020.04.29：版本号（v1.17 BE1.13.3）**

<!--toVer: 2020.02.20-->

- 新增

1. 新增[IsEntityRiding](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#isentityriding)、[GetEntityRider](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getentityrider)、[StopEntityRiding](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#stopentityriding)接口，用于判定生物的骑乘状态 <!--by  xltang-->
2. 新增[PistonActionServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#pistonactionserverevent)事件，活塞影响方块的事件 <!--by  xltang-->
3. 新增[WillTeleportToServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#willteleporttoserverevent)事件，实体即将传送事件 <!--by  xltang-->
4. 新增[StartRidingServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#startridingserverevent)事件，实体骑乘事件 <!--by  xltang-->
5. 新增[StartRidingClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#startridingclientevent)事件，实体骑乘事件 <!--by  xltang-->
6. 新增[PlayerInteractServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#playerinteractserverevent)事件，玩家和实体交互事件 <!--by  xltang-->
7. 新增[MobGriefingBlockServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#mobgriefingblockserverevent)事件，生物与方块交互事件 <!--by  xltang-->
8. 新增[StepOnBlockServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#steponblockserverevent)事件，生物脚踩压力板、踩红石矿、踩拌线钩事件 <!--by  xltang-->
9. 新增[StepOnBlockClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#steponblockclientevent)事件，生物踩红石矿事件 <!--by  xltang-->
10. 新增[ActuallyHurtServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#actuallyhurtserverevent)事件，返回实体受的真实伤害 <!--by  czh-->
11. 新增[自定义熔炉demo](03-自定义游戏内容/05-自定义方块/a-自定义熔炉.html)，复刻原版熔炉部分功能，开发者可根据其进行修改实现自己的自定义熔炉。后续版本会陆续完善<!--by  ld-->
12. 新增文档[名词解释](02-Python脚本开发/99-ModAPI/0-名词解释.html)，阐述常见的组件和事件的类型含义。
14. 新增文档[自定义维度文档](03-自定义游戏内容/07-自定义维度/0-自定义维度及相关内容总览.md)，介绍mod中引入自定义维度的步骤<!--by  why-->
15. 新增文档[自定义基础生物](03-自定义游戏内容/06-自定义生物/01-自定义基础生物.md)，介绍mod中自定义生物的步骤<!--by  gzhuabo-->
16. 新增文档[原版模型制作指南](81-资源制作/1-模型和动作/01-原版模型制作指南.md)，介绍如何制作原版模型制作的指南<!--by  gzhuabo-->
- 调整

1. 文档结构调整与优化：
   * “Mod入门简介”移到“Mod开发简介”，并拆分为三个文档
   * “从零开始创建UI”文档移到UI - [从零开始创建UI界面](60-UI/2-从零开始创建UI.html)，并进行优化。将UI编辑器的使用流程融合进UI界面的教程中，通过图片+文字描述的形式，引导开发者制作一个简单实用的fps战斗界面。
   * “从零开始创造Mod”文档移到Python脚本开发 - [脚本开发入门](02-Python脚本开发/0-脚本开发入门.html)，并进行优化
   * “MOD SDK文档”移到Python脚本开发 - ModAPI
   * "自定义生物文档"，"自定义物品"，"自定义方块"，"自定义配方"，"自定义状态效果"移到“自定义游戏内容”板块
   * "自定义生物群系"移到自定义游戏内容 - 自定义维度，并拆分为群系地貌，生物生成，自定义特征三个文档
   * “Minecraft枚举值文档”移到参考资源 - [Minecraft枚举值文档](99-参考资料/0-Minecraft枚举值文档.html)
   * "UI说明文档“，”UI API文档“移到”UI“板块，并进行优化。增加了部分可用控件及其相关介绍，同时针对每个控件，附上了UI编辑器中的控件截图、操作方法和实际效果，更好的帮助开发者使用UI编辑器。
   * ”联机大厅商品Mod文档“，”竞技模式组件SDK 文档“移到”联机大厅开发“板块
2. 示例mod优化：
   * TutorialMod，AwesomeMod调整为组件的接口化形式
   * TestUIMod，AwesomeMod的按钮绑定改为使用AddTouchEventHandler
   * AwesomeMod中的coroutineMgr改为使用game组件的AddTimer接口
   * 调整了CustomBlocksMod，CustomCropMod中import的模块，修复无法通过机审的问题
3. 移除GetCompData的相关内容 <!--by  czh-->
4. [CreateEngineItemEntity](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#createengineitementity)参数改为itemDict
5. [GetEngineType](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#enginetype)接口的示例提供如何判断一个实体是否是Mob、是否是弹射物的示例代码 <!--by  gx-->

**2020.03.16：版本号（v1.17  BE1.13.3）**

<!--toVer: 2020.02.20-->

- 新增

1. 支持自定义配方Json配置耐久度参数，详见[自定义配方](03-自定义游戏内容/04-自定义配方.html#支持耐久度配置的配方)<!--by  ld-->
2. 新增自定义状态效果，详见[自定义状态效果](03-自定义游戏内容/08-自定义状态效果.html)<!--by  ld-->
3. 新增自定义状态效果新增、移除、查询接口及新增、删除、更新事件，详见[effect组件](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#effect)及[AddEffectServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#addeffectserverevent)、[RefreshEffectServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#refresheffectserverevent)、[RemoveEffectServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#removeeffectserverevent)事件<!--by  ld-->
4. 新增[自定义方块实体](03-自定义游戏内容/05-自定义方块/4-自定义方块实体.html)，支持为自定义方块配置自定义方块实体，可向其中存储、读取数据。<!--by  liaoyi -->
5. 新增[自定义方块模型](03-自定义游戏内容/05-自定义方块/5-自定义方块模型.html)<!--by  czh-->
6. 新增自定义维度设置，防止不同的Mod的维度冲突的方案，[详见](03-自定义游戏内容/07-自定义维度/1-自定义维度.html)<!--by  why-->
7. 新增[自定义物品分页](03-自定义游戏内容/03-自定义物品/9-自定义物品分页.html)，用于扩展物品分页<!--by  guoxun-->
8. 新增支持设置Mod加载依赖关系，详见[netease_require](80-其它基础游戏配置.html#netease-require)<!--by  hongshubin-->
9. 新增对UI绑定实体的支持，可在创建时将UI绑定到某个实体上，绑定后UI会随实体移动，详见[创建UI界面](60-UI/4-UI说明文档.html#创建ui界面)。UI API文档还提供了[判断实体是否能与UI绑定](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#CheckCanBindUI)、[修改绑定的实体](60-UI/5-UIAPI文档.html#changebindentityid)、[获取绑定的实体id](60-UI/5-UIAPI文档.html#GetBindEntityId)、[修改UI与绑定实体间偏移量](60-UI/5-UIAPI文档.html#changebindoffset)、[获取UI与绑定实体间偏移量](60-UI/5-UIAPI文档.html#GetBindOffset)、[设置UI是否可以动态缩放](60-UI/5-UIAPI文档.html#changebindautoscale)、[获取UI是否可以动态缩放](60-UI/5-UIAPI文档.html#GetBindAutoScale)的接口<!--by  liaoyi-->
10. 新增[SetLayer](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setlayer-layer)接口，设置粒子和序列帧特效的渲染层级 <!--by  hongshubin-->
11. 新增[ResetAttackTarget](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#resetattacktarget)与[ResetHurtBy](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#resethurtby)取消标记攻击对象和取消标记攻击自己的对象接口 <!--by  hongshubin-->
12. 新增[SetDefaultGameType](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setdefaultgametype-gametype)设置默认游戏模式接口<!--by  ld-->
13. 新增[SetPlayerGameType](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setplayergametype-gametype)设置玩家个人游戏模式接口<!--by  ld-->
14. 新增[CheckBlockToPos](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#checkblocktopos-frompos-topos)判断位置之间是否有方块接口<!--by  ld-->
15. 新增[GetEngineActor](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#getengineactor)获取当前地图所有实体信息接口<!--by  ld-->
16. 新增[GetEntityScale](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getentityscale)获取实体缩放比例接口<!--by  ld-->
17. 新增[OnLocalPlayerStopLoading](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#onlocalplayerstoploading)事件<!--by  ld-->
18. 新增[服务端](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#getdirfromrot)与[客户端](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#getdirfromrot)的GetDirFromRot接口，可用于根据旋转角度获取朝向 <!--by  liaoyi-->
19. 新增[GetAnimLength](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#getanimlength-aniname)接口，用于获取动画长度 <!--by  liaoyi-->
20. 新增[LockPerspective](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#lockperspective-persp)接口，用于锁定玩家视角 <!--by  liaoyi-->
21. 新增[SetBrightness](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setbrightness-brightness)接口，用于设置实体的亮度 <!--by  liaoyi-->
22. 新增[OpenNeteaseStoreGui](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/2-客户端ExtraAPI接口.html#openneteasestoregui)接口，用于打开购买商品界面 <!--by  liaoyi-->
23. 新增[SetModelOffset](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setmodeloffset-offset)接口，用于设置骨骼模型偏移量 <!--by  liaoyi-->
24. 新增[IsInServer](02-Python脚本开发/99-ModAPI/1-ExtraAPI接口/1-服务端ExtraAPI接口.html#isinserver)接口，用于判断当前游戏是否跑在服务器环境下 <!--by  liaoyi-->
25. 新增[SetDisableGravityInLiquid](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setdisablegravityinliquid-isdisable)接口，用于关闭实体在水或岩浆中的重力 <!--by  liaoyi-->
26. 新增[SetPickUpArea](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setpickuparea-area)接口，用于设置玩家拾取物品范围 <!--by  liaoyi-->
27. 新增[LockInputVector](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#lockinputvector-inputvector)和[UnlockInputVector](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#unlockinputvector)接口，用于锁定或解锁本地玩家的移动轮盘输入 <!--by  liaoyi-->
28. 新增[GetUIProfile](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#getuiprofile)接口，用于获取玩家的ui风格<!--by  czh-->
29. 新增[PlayerTryDestroyBlockClientEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#playertrydestroyblockclientevent)事件，用于某些方块配合同名server事件使用<!--by  czh-->
30. 新增[PlayerEatFoodServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#playereatfoodserverevent)事件，用于玩家吃完食物时触发<!--by  why-->
31. 新增[SetPlayerRideEntity](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setplayerrideentity-playerid-rideentityid)接口，设置玩家骑乘某个生物<!--by  why-->
32. 新增[SetUiEntity](60-UI/5-UIAPI文档.html#setuientity)接口，设置原版生物模型在Paperdoll控件中显示<!--by  hyk-->
33. 新增[SetSpriteClipRatio](60-UI/5-UIAPI文档.html#setspriteclipratio)接口，设置图片的裁剪区域比例<!--by  hyk-->
34. 新增[服务端SetPopupNotice](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setpopupnotice-message-subtitle)、[客户端SetPopupNotice](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setpopupnotice-message-subtitle)、[服务端SetTipMessage](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#settipmessage-message)接口、[客户端SetTipMessage](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#settipmessage-message)、[服务端SetOnePopupNotice](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setonepopupnotice-playerid-message-subtitle)、[服务端SetOneTipMessage](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setonetipmessage-playerid-message)，支持显示tip和popup两种类型的通知<!--by  hongshubin-->
35. 新增[GetTopBlockData](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#gettopblockdata-pos)接口，获取纵向最顶层方块信息<!--by  hongshubin-->
36. 新增支持设置序列帧动画每帧之间的大小插值，详见[序列帧配置文件解析](81-资源制作/2-特效/序列帧配置文件解析.html)<!--by  hongshubin-->
37. 新增支持设置序列帧动画随机播放，详见[序列帧配置文件解析](81-资源制作/2-特效/序列帧配置文件解析.html)<!--by  hongshubin-->
38. 新增[SetSkyTextures](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setskytextures-texturelist)与[ResetSkyTextures](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#resetskytextures)接口，支持动态设置天空盒贴图<!--by  hongshubin-->

- 调整

1. 移除ExplosionHurtEvent事件与ServerExplosionBlockEvent事件，并删去相关文档。新增整合了前两个事件信息的[ExplosionServerEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#explosionserverevent)事件 <!--by  liaoyi-->
2. 事件系统现在支持优先级，详见[ListenForEvent](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#listenforevent)<!--by  czh-->
3. [CreateEngineTextboard](02-Python脚本开发/99-ModAPI/5-实体创建/2-客户端表现实体创建.html#创建文字面板)加入敏感词过滤的建议<!--by  czh-->
4. GetPlayerDimensionId调整为[GetEntityDimensionId](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getentitydimensionid)，支持获取所有实体的维度信息<!--by  czh-->
5. [ServerItemUseOnEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#serveritemuseonevent)和[ServerBlockUseEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#serverblockuseevent)事件完善说明<!--by why-->
6. [GetPlayerExp](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getplayerexp-ispercent)接口增加ispercent参数设置是否获取百分比还是绝对值经验<!--by why-->
7. 2020.01.21更改中的SetInvItemDamage、GetInvItemDamage、SetEquItemDamage、GetEquItemDamage更改为[SetInvItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setinvitemdurability-slotpos-damage)、[GetInvItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getinvitemdurability-slotpos)、[SetEquItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#setequitemdurability-slotpos-damage)、[GetEquItemDurability](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getequitemdurability-slotpos)<!--by why-->
5. [ServerItemTryUseEvent](02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#serveritemtryuseevent)、 [ClientItemTryUseEvent](02-Python脚本开发/99-ModAPI/3-事件/3-客户端事件.html#clientitemtryuseevent)增加cancel<!--by  hb-->
6. [SetSize](60-UI/5-UIAPI文档.html#setsize)接口调整为添加resizeChildren参数，支持调整控件尺寸时一并调整其子控件尺寸<!--by  hyk-->
7. CreateEngineItem调整为[CreateEngineItemEntity](02-Python脚本开发/99-ModAPI/2-系统相关/2-系统相关API.html#createengineitementity)，支持返回生成item的entity Id<!--by  hongshubin-->

- 修复

1. 输入框中输入文字后，点输入框外的按钮，第一次点击失效修复  <!--by  syy-->
2. 补充《ModAPI文档》中客户端表现、服务端实体创建部分缺失的函数名称<!-- by  liaoyi -->
3. 统一《ModAPI文档》中示例的代码风格<!-- by  liaoyi-->
4. [GetBiomeName](02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#getbiomename-pos)接口在区块未加载时由返回ocean修复为返回空字符串<!-- by  czh-->
5. [SetCamerabindActorId](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setcamerabindactorid-targetid)绑定对象死亡或者离开chunk时闪退问题修复<!--by  hongshubin-->
6. 帧动画始终遮挡粒子特效的效果问题修复，详见[粒子](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setlayer-layer)和[序列帧](02-Python脚本开发/99-ModAPI/4-组件/3-客户端组件.html#setlayer-layer-2)的SetLayer接口<!--by  hongshubin-->
7. 修复在自定义维度，玩家如果卡在一个地下密闭的地形里，退出游戏重进，会被传送到地面上<!-- by  hb-->
8. 修复自定义物品超过115断言报错<!-- by  hb-->
9. [SetCrossHair](60-UI/5-UIAPI文档.html#setcrosshair)接口visible参数说明修复<!-- by  hyk-->
10. 修复grid控件如果dimensions行数较多，则排在后面的grid单元的控件路径会有异常<!-- by why-->

**2020.01.21更改：版本号（v1.17 BE1.13.3）**

<!-- toVer:2020.01.21 -->

- 新增

1. 新增SetModelPerspectiveEffect设置透视效果接口，详见《3-1Mod SDK文档》 <!-- by ld -->
2. 新增SetSpeedFovLock加速奔跑时锁定相机视口接口，详见《3-1Mod SDK文档》 <!-- by ld -->
3. 新增碰撞生物相关事件及碰撞生物检测相关接口，详见《3-1Mod SDK文档》 <!-- by ld -->
4. 新增SetEntityPushable接口，详见《3-1Mod SDK文档》 <!-- by ld -->
5. 新增BindEntityToEntity、ResetBindEntity绑定实体接口，详见《3-1Mod SDK文档》 <!-- by ld -->
6. 新增SetModelOffeset设置模型偏移接口，详见《3-1Mod SDK文档》 <!-- by ld -->
7. 新增GetScreenViewInfo获取屏幕视口接口，详见《3-1Mod SDK文档》 <!-- by ld -->
8. 新增NotifyOneMessage通知消息接口，详见《3-1Mod SDK文档》 <!-- by ld -->
9. 新增SetEntityScale设置实体缩放大小接口，详见《3-1Mod SDK文档》 <!-- by ld -->
10. 新增GetModelName获取模型名称接口，详见《3-1Mod SDK文档》 <!-- by ld -->
11. 新增注册、反注册感应区域接口，有生物进出时会有消息通知，详见《3-1Mod SDK文档》 <!-- by ld -->
12. 新增禁止跳跃、移动、推动等接口，详见《3-1Mod SDK文档》 <!-- by ld -->
13. 新增检测chunk是否加载完成接口，详见《3-1Mod SDK文档》 <!-- by ld -->
14. 新增SetPersistence设置实体是否存盘接口，详见《3-1Mod SDK文档》 <!-- by ld -->
15. attr组件支持设置水中移速，详见《3-1Mod SDK文档》 <!-- by ld -->
16. blockinfo组件新增接口获取纵向高度上雨雪可达的最顶层实体方块信息，详见《3-1Mod SDK文档》
17. 新增ItemRenderer控件，详见《3-4 UI说明文档》的ItemRenderer <!-- by syy -->
18. 新增SetUiItem接口设置ItemRenderer的显示，详见《3-5 UI API文档》 <!-- by syy -->
19. 新增GetDirFromRot根据旋转角度获取朝向接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
20. 新增GetAnimLength获取动画长度接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
21. 新增LockPerspectiveGetAnimLength锁定玩家视角模式接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
22. 新增SetBrightness设置实体的亮度接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
23. 新增IsInServer判断是否跑在服务器环境下接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
24. 新增SetDisableGravityInLiquid关闭实体在液体（水/岩浆）中的重力接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
25. 新增SetPickUpArea设置玩家拾取物品范围接口，详见《3-1Mod SDK文档》 <!-- by liaoyi -->
26. TextNotifyComponet组件增加与SetLeftCornerNotify接口添加 <!-- by why -->
27. ExpComponentServer组件增加AddPlayerExperience接口 <!-- by why -->
28. GameComponentServer组件增加与SetGameRulesInfoServer，GetGameRulesInfoServer接口增加 <!-- by why -->
29. 新增EntityDefinitionsEventServerEvent事件 <!-- by why -->
30. 新增SetEntityOpacity设置实体不透明度接口，详见《3-1Mod SDK文档》 <!-- by drx -->
31. 新增HidePlayerName设置隐藏玩家名字接口，详见《3-1Mod SDK文档》 <!-- by drx -->
32. 新增BeginSprinting设置玩家为冲刺状态接口，详见《3-1Mod SDK文档》 <!-- by drx -->
33. 新增EndSprinting设置停止玩家冲刺状态接口，详见《3-1Mod SDK文档》 <!-- by drx -->
34. 新增SetPlayerPrefixAndSuffixName设置玩家头顶名字显示（待测试） <!-- by why -->
35. 新增GetModelName获取实体模型名称（待测试） <!-- by why -->
36. 新增SetAlwaysShowName设置enityName常驻在头顶显示（待测试） <!-- by why -->
37. gamecompserver和gamecompclitent新增AddOnceTimer、AddRepeatedTimer、CancelTimer函数（待测试） <!-- by why -->
38. 新增SetInvItemDamage、GetInvItemDamage、SetEquItemDamage、GetEquItemDamage函数（待测试） <!-- by why -->
39. 新增PlayerEatFoodServerEvent事件，玩家吃食物时触发 <!-- by why -->
40. 新增EnableKeepInventory设置某个玩家死亡不掉落物品接口，详见《3-1Mod SDK文档》 <!-- by hb -->
41. AudioCustomComponent 组件新增接口 DisableOriginMusic ，PlayGlobalCustomMusic ，PlayCustomMusic ，StopCustomMusic ，StopCustomMusicById ，SetCustomMusicLoop，SetCustomMusicLoopById <!-- by gx -->
42. 新增 OnMusicStopClientEvent 事件 <!-- by gx -->
43. 新增支持自定义农作物，详见《3-10 自定义方块》 <!-- by hb -->

- 修复

无

- 调整

1. PlayerTouchNewModItemEvent事件移除 <!-- by why -->
2. ServerPlayerTryTouchEvent事件增加extraId\customtips参数 <!-- by why -->
3. SpawnItemToPlayerInv接口增加是否掉落到附近参数和设置到临近槽位 <!-- by why -->
4. ExplosionHurtEvent增加爆炸位置参数 <!-- by why -->
5. SpawnItemToPlayerInv事件增加isDrop参数 <!-- by why -->
6. DamageEvent事件增加projectId参数 <!-- by why -->

**2019.11.22更改：版本号（v1.16 BE1.13.1） <!-- by syy -->**

toVer:2019.11.7

1. 新增服务端与客户端modAttr组件,支持AOI的脚本层属性同步,详见组件说明
2. 微软自定义生物可自行设定是否为实验性的，详见《3-2 自定义生物文档》中关于is_experimental的说明
3. 自定义生物群系新增对自定义特征的支持，通过json配置Feature Rules与Feature，可用于在地形生成时自动放置由结构方块导出的结构。可通过服务端组件neteaseStructureFeatureWhiteList管理结构白名单，白名单内结构在放置时会触发PlaceNeteaseStructureFeatureEvent服务端事件，支持取消放置。详见《3-8 自定义生物群系》
4. PlayerAttackEntityEvent事件新增支持设置击退效果是否生效，详见《3-1 Mod SDK文档》相关事件
5. 新增服务端biome组件及相关接口，详见《3-1 Mod SDK文档》服务端组件biome
6. 由于已支持更强大的json配置配方，RegisterRecipe(rcp)接口从《3-1 Mod SDK文档》中删除
7. 修复《3-4 UI说明文档》中九宫格相关UI拼写错误，buttom改为bottom
8. "自定义spawn_rules"、"生物生成规则说明文档"并入《3-8 自定义生物群系》" ，并剔除重复部分
9. "我的世界基岩版饥饿度机制说明"并入《3-1 Mod SDK文档》中相应的接口说明中
10. "配置文件说明文档"名字修改为"其它基础游戏配置"
11. 新增自定义物品设置物品名字说明，详见《3-9 自定义物品》自定义物品名字部分
12. CreateEngineEntity和CreateEngineEntityByTypeStr增加isNpc参数，详见《3-1Mod SDK文档》 <!-- by syy -->
13. controlAi组件SetBlockControlAi接口，修复部分生物失效bug <!-- by syy -->
14. button增加触控事件吞噬功能。详见《3-5 UI API文档》，AddTouchEventHandler中args参数及备注中args的说明 <!-- by syy -->
15. 《3-2 自定义生物文档》中删除网易自定义生物。由于微软的自定义生物已经覆盖了网易自定义生物功能，建议使用微软自定义生物。 <!-- by syy -->
16. 自定义生物蛋支持发射器。
17. 增加自定义盔甲功能，详见自定义物品文档中的盔甲内容
18. "自定义生物群系"的json格式升级到微软1.13版本。"群系开发模板"移动至demo的behavior/tools目录，并添加"版本升级工具"提供给基于2019.10.24版本开发的开发者。详见《3-8 自定义生物群系》
19. 自定义方块增加"netease:solid"及"netease:pathable"两个component，详见《3-10 自定义方块》

**2019.11.11 更改：版本号（v1.16 BE1.12.0）**

toVer:2019.10.24

1. 新增"获取指定位置所属的生物群系信息"接口，详见《3-1Mod SDK文档》生物群系组件
2. 新增更多客户端model相关接口及细化文档，详见客户端组件 model
3. 新增更多客户端game相关接口，详见客户端组件 game
4. 新增更多客户端textboard相关接口，详见客户端组件 textboard
5. 新增客户端blockInfo组件及相关接口
6. 新增服务端scale组件及相关接口
7. 新增更多服务端 action相关接口，详见客户端组件 action
8. 自定义方块新增对自定义刷怪笼方块的支持，可生成原生生物、微软自定义生物及网易自定义生物，详见《3-10 自定义方块》
9. 自定义方块新增对自定义传送门方块的支持，可配置贴图、目标维度、粒子特效，详见《3-10 自定义方块》
10. 新增自定义武器/工具功能，详见自定义物品文档
11. 新增自定义生物蛋功能，详见自定义物品文档

**2019.10.24 更改：版本号（v1.16 BE1.12.0）**

toVer:2019.10.24

1. 添加"自定义生物群系"文档，支持自定义维度下的生物群系的自定义
2. 添加"自定义方块"文档，支持json配置的自定义方块，并支持"MOD SDK文档"中"方块"分类的事件及组件。
3. 添加"自定义物品"文档，支持json配置的自定义物品，并支持"MOD SDK文档"中"物品"分类的事件及组件。去除了"MOD SDK文档"中旧版自定义物品的相关内容
4. 新增自定义盔甲功能，详见自定义物品文档
5. camera组件添加GetChosen接口，支持获取选中的方块
6. button支持多点触控，需要使用AddTouchEventHandler注册
7. 修改PlayerAttackEntityEvent事件支持取消
8. 新增AddEntityServerEvent服务端事件
9. 新增饥饿值调整相关接口，详见服务端组件player相关接口
10. 新增进入和离开维度事件DimensionChagneClientEvent、DimensionChagneServerEvent
11. 新增禁止物品使用配置文件和动态管理禁止物品，详见ModSdk文档客户端组件itembanned组件以及《3-14 配置文件说明文档》
12. 新增支持Addon自定义配方，详见《3-12 自定义配方》
13. 新增服务端组件bloackUseEventWhiteList管理对NewModBlockUseEvent事件进行监听
14. 新增更多camera相关接口，详见客户端组件camera
15. 特效绑定参数文档说明细化
16. 新增ActorUseItemServerEvent、ActorUseItemClientEvent事件：玩家使用物品（该事件不提供取消接口）
17. 新增客户端actorCollidable组件：控制玩家是否可碰撞
18. 新增Addon支持spawn_rules自定义，详见《3-11 自定义spawn_rules》
19. 新增 ActorAcquiredItemServerEvent、ActorAcquiredItemClientEvent 事件：玩家获得物品
20. 新增可禁止游戏中藤曼蔓延，详见服务端组件game DisableVineBlockSpread
21. 支持对原版方块白名单监听方块使用事件（ClientNewModBlockUseEvent和NewModBlockUseEvent），并且支持取消使用功能，白名单管理详见服务端组件blockUseEventWhiteList
22. 新增CanSee视野判断接口
23. 新增DamageEvent的可配置参数knock，选择是否击退被攻击者（其他不变）

**2019.9.11 更改：版本号（v1.15 BE1.12.0）**

toVer: 2019.8.22

1. button绑定回调函数方式修改；并且回调增加move和cancel事件；详见《UI API文档》AddTouchEventHandler
2. armorslot组件增加修改装备槽位接口
3. PlayerTouchNewModItemEvent事件兼容新版物品
4. 新增OnArmorExchangeServerEvent事件：装备穿上/脱下
5. 新增ClientPlayerInventoryOpenEvent事件：客户端打开和关闭背包事件
6. 新增ClientChestOpenEvent事件：客户端打开和关闭箱子事件
7. tame组件支持实体被玩家驯服
8. 新增ServerPlayerGetExperienceOrbEvent事件：玩家拾起经验球事件
9. item组件支持自定义物品添加到快捷栏或者背包固定槽位
10. component接口化改版
11. 增加mod加载失败时异常信息的输出
12. 支持微软自定义生物，详见《3-2 自定义生物文档》
13. 支持根据特效编辑器配置好的序列帧属性生成序列帧，见"创建特效编辑器编辑的序列帧特效"
14. 支持根据特效编辑器配置好的绑定信息创建特效，见"创建模型特效"
15. Mod SDK文档增加 OnKeyPressInGame的键码描述、伤害增加伤害来源cause
16. 新增客户端组件：actorRender组件。详见ModSdk文档客户端组件实体部分的actorRender组件
17. 新增客户端组件：skyRender组件。详见ModSdk文档客户端组件界面部分的skyRender组件
18. 新增客户端组件：fog组件。详见ModSdk文档客户端组件界面部分的fog组件
19. command组件支持指定玩家功能，command组件调用setCommand时第二个参数可以选择传入玩家ID

**2019.7.31 更改：版本号（v1.15 BE1.11.4）**

1. 新增服务器组件：gravity组件,设置实体重力。详见ModSdk文档服务端gravity组件

2. 新增设置世界levelGravity，详见ModSdk文档服务器game组件

3. 服务器moveto组件移到生物分类。并添加寻路距离及回调的说明

4. 新增服务器组件chunkSource，可用于区块的长加载。

5. 新增OnItemSlotButtonClickedEvent事件，事件参数详见文档。

6. 新增entityEvent组件和tame组件，详见mod sdk服务器组件部分。

**2019.7.8 更改：版本号（v1.14 BE1.11.4）**

1. 新增设置游戏gamerule功能，包括作弊选项。详见ModSdk文档服务器game组件的gameRulesInfo

2. 新增设置生物nameTag功能。详见ModSdk文档服务器name组件

3. 新增交换背包物品的槽位功能。详见ModSdk文档服务器item组件

4. 新增设置背包物品数量功能。详见ModSdk文档服务器item组件

5. 新增blockChest组件，支持获取、设置箱子内物品。详见ModSdk文档blockChest组件

6. 新增breath组件，支持获取、设置玩家氧气相关信息。详见ModSdk文档breath组件

7. 新增设置物品tips功能，详见ModSdk文档服务器item组件的customTips

8. 新增关闭生物实例AI的功能，详见ModSdk文档服务器controlAi组件

9. 新增导航（寻路提示）功能，详见ModSdk文档clientApi的GetNavPath及StartNavTo

10. 新增《从零开始创造MOD》文档，Mod示例内增加tutorialMod的demo

11. 优化《Mod入门简介》中的MOD 开发指引，优化文档中对AwesomeMod entities的描述

12. 优化AwesomeMod。增加代码注释，修复按钮弹起后显示问题

**2019.5.22 更改：版本号（1.13）**

1. 新增OnClientPlayerStartMove事件：客户端玩家开始移动事件

2. 新增OnClientPlayerStopMove事件：客户端玩家移动结束事件

3. 新增OnModItemUseClientEvent事件：使用自定义物品，客户端事件

4. 新增OnModItemUseOnClientEvent事件：对方块使用自定义物品，客户端事件

5. 新增OnModItemUseServerEvent事件：使用自定义物品，服务端事件

6. 新增OnModItemUseOnServerEvent事件：对方块使用自定义物品，服务端事件

7. 新增offHand，carried，inventory客户端组件，详见文档相应组件描述

8. 新增offHand，carried，inventory服务端组件，详见文档相应组件描述

9. operation组件新增moveLock 属性，详见文档描述

10. 新增ApproachEntityClientEvent，LeaveEntityClientEvent客户端事件。玩家靠近、远离生物事件

11. 新增导航相关api

**2019.4.16更改：版本号（1.13）**

1. get_player_inventory_slot添加extraId，去除不会覆盖原有值的描述

**2019.3.16更改：版本号（1.12）**

1. 优化《自定义物品、配方.md》里的说明

2. 新增查询背包指定位置的物品，详见inventory组件

3. 新增屏蔽玩家与容器交互功能，详见服务器game组件

4. 新增禁止玩家丢弃物品功能，详见服务器game组件

5. 内存优化

6. 新增接口控件ProjectileCritHitEvent事件是否开启，详见ProjectileCritHitEvent

7. 加大exdata数据存储量

8. 新增DestroyBlockEvent事件

9. 新增方块组合生成生物事件，详见ServerPreBlockPatternEvent

10. ModBlockUseEvent增加点击方块坐标

**2019.3.5更改：版本号（1.11）**

1. 新增dimension功能，详见dimsnsion组件和createEntity接口
2. 新增锁饥饿度功能，详见服务器game组件 3.新加《mod开发时遇到BUG可能的原因》文档

**2019.1.29更改：版本号（1.11）**

1. data/manifest增加版本信息，version
2. 规范文档更新 3.增加mod开发辅助工具

**2019.1.10更改：版本号（1.11）**

1. UI功能完善，增加UI生命周期函数，layer层级、响应问题优化，详见UI文档
2. UI接口增加namespace参数，详见UI文档
3. modDemo规范化，详见DeveloperDemoMod
4. 屏幕分辨率获取接口，详见game组件
5. 更新客户端组件：operation新增inair属性。修复按着移动键屏蔽move会一直移动的bug
6. 自定义item：相关组件新增extraId字段
7. Carried组件：新增获取是否附魔
8. 新增服务端组件：action组件，设置攻击目标对象，实现仇恨效果

**2018.12.15更改：版本号（1.11）**

1. 更新服务端事件: ServerMobSpawnEvent生成怪物的事件可以控制是否生成。

2. 更新服务端组件: ride组件可以设置是不是可以骑乘，驯服者骑乘，骑乘位置是哪里，骑乘控制以及骑乘的保存。

3. 新增服务端组件：collisionBox组件，设置物体包围盒

4. 增加服务端事件：DamageEvent

5. 更新客户端组件：model增加动画播放速度设置，获取当前播放动画名字。

6. 更新客户端组件：game可以设置不渲染本地玩家。

**2018.12.10更改： 版本号（1.11）**

1. 更新服务器组件：Pos组件当生物不存在时返回none
2. 新增服务器事件：替换模型后，走路动作、攻击动作、跳跃动作起始事件与终止事件
3. 更新服务器组件：attr组件增加moveDir变量获取生物移动方向
4. 更新服务器组件：model组件支持使用平台皮肤和更换骨骼贴图
5. 更新客户端组件：actorMotion组件支持客户端移动Player
6. 更新客户端组件：model增加原版自定义皮肤功能
7. 更新客户端组件：operation操作锁定功能
8. 更新UI文档：GetInputVector获取游戏中玩家输入移动的向量
9. 更新UI文档：HideHudGUI隐藏游戏中的UI界面
10. Bug修复：textboard第一人称渲染问题

**2018.10.10更改：**

1.UI node可以设置点击UI时是否响应下层游戏（挥手攻击方块等），设置为False时点击UI不会响应到，True则可以。 2.修复PC端在点击F11后，点击UI界面时，捕捉不到entity的问题，现在可以像鼠标一样点击获取entity。 3.bug修复：health组件获取血量不正确的bug 4.新增设置单个实体血条是否显示功能，详见文档health组件 5.新增设置单个实体名字是否显示功能，详见文档name组件 6.新增设置名字是否透视功能，详见文档game组件 7.新增摄像机锁定及解锁功能，详见文档camera组件 8.新增获取准星选中的实体功能，详见文档camera组件 9.新增设置玩家视角功能，详见文档playerView组件 10.新增伤害功能，详见文档hurt组件

**2018.9.17更改：**

1. 自定义物品的id改为了用str字符串形式，从而避免多mod加载中有冲突；兼容以前mod的形式，但不兼容以前mod的存档。新的自定义物品接口参数可以看文档，新例子也添加到RoboCraft，。对应地，之前接口中设置或获取modValue的component或者event，都会附加一个modExtendValue作为真正的自定义扩展id值。建议开发者以后编码按照新接口，避免旧接口弃用时存在问题。

2. 增加服务器组件：指令组件

3. 服务器事件：玩家攻击事件增加修改伤害值

4. 增加服务器组件：attr组件，提供设置血量、速度和伤害值

5. 新增锁定摄像机功能，详见Camera组件

6. 新增骑乘事件，详见modApi文档EntityStartRidingEvent、EntityStopRidingEvent

7. 修复特效资源缺失导致的程序崩溃

8. 修复pos组件获取位置不正确的问题

9. 所有生物支持骨骼模型

10. 服务器组件：game组件，增加获取区域内实体

11. 客户端组件：帧动画绑定骨骼组件，增加rot和offset实现特效旋转和偏移

12. 客户端组件：粒子绑定骨骼组件，增加rot和offset

13. 服务器组件：game组件，增加通知栏消息

14. bug修复：加载模型时皮肤仍存在的bug

15. bug修复：复活事件重复通知的bug

16. bug修复：第三人称血条、特效渲染位置错乱修复

17. 新增自定义Block的多面向支持。如使用此功能，需要完整定义blocks.json, terrain_texture.json。详细内容参考文档，使用可以参考例子。

18. MOD版本管理。MOD版本管理采取向下兼容，即新的游戏引擎版本，可以兼容新引擎开发的MOD和旧引擎开发的MOD，旧引擎则不能使用新引擎开发的MOD。后续在开发者平台上传MOD时会有MOD引擎版本选择，开发者根据文档中的引擎版本号选择即可。开发者想更新MOD脚本内容（修BUG等等），只需要在MOD的manifest.json中的header的version字段进行版本升级([0, 0, 1] --> [0, 0 ,2])，然后重新上传到开发者平台即可完成更新操作。

19. 设置自定义装备属性，可以设置装备的耐损度和防御值。设置依然是在自定义armor的时候指定；设定后，在该mod期间，属性不会变化。

20. 增加对装备栏进行操作的接口。主要是armorSlotComp，详见文档和示例。

**2018.7.25 更新内容**

1. OnScriptTickClient、OnScriptTickServer部分机器超过30帧修复
2. 骨骼绑定特效失败时崩溃修复
3. 上下半身动作播放功能，详见api文档model组件
4. system的update()中设置needsUpdate失效修复
5. walkEnd事件延迟问题修复
6. 绑定特效没绑定成功时，特效设置为不显示
7. 特效有机率残留bug修复
8. exDataComp数据失效修复
9. 性能优化
10. 增加复活事件
11. 自定义物品联机显示错误问题修复
12. UI按钮增加cancel事件
13. BlockInfo的Component增加 placeBlock 的接口，用于同帧内更新一个或多个block；之前的blockId、auxData、pos暂时保留用于兼容接口，已弃用，建议不使用。

**2018.6.25 更新内容**

1. 增加了drop itemEntity的示例，详见testFpsSystem.py#OnHitResult
2. 增加了实体变种数据值组件，可以获取实体变种的auxValue，目前支持药水的变种数据值，详见文档。
3. 修改了物品使用事件回调的监听事件： ModItemReleaseUseServerEvent改为ModItemUseServerEvent； ModItemReleaseUseClientEvent改为ModItemUseClientEvent。
4. 子弹伤害hook，ProjectileDoHitEffectEvent事件中， 参数cancel设置为True时，碰撞伤害无效
5. 增加受击cd设置功能，详见api文档中的game组件
6. 增加是显示血条功能，详见api文档中的game组件
7. 性能优化
8. 新增服务器model组件，客户端model组件的模型同步及存盘功能移植到服务器组件
9. 粒子特效使用贴图原色支持,详见特效规范Particle Json
10. 特效需要切换镜头才能看到bug维护
11. 第一人称特效挂接位置不在相应的骨骼上bug维护
12. 特效挂到第一人称骨骼上，第三人称没此骨骼的时候会crash bug维护。当前版本请尽量保证第一人称和第三人称骨骼名称统一，不然可能出现位置错乱问题。
13. 修复联机模式下，调用设置玩家血条颜色时崩溃问题
14. 更新了Addon加载相关信息，更新了Python加载的具体要求和实例，更新了所用到的目录信息，具体内容参见Addon加载.docx

**2018.6.13 更新内容**

1. 骨骼模型播放动画isLoop为False时播放失败修复
2. 准星图在开枪时能够放大缩小样例，详见fpsBattle.py#OnClickShoot
3. 按钮up down事件不准确bug修复
4. 客户端rot组件，详见API文档
5. 特效绑定第一人称模型时，特效不显示问题修复
6. scriptTick事件更改。客户端OnScriptTickClient，服务器OnScriptTickServer, 详见API文档
7. Scoreboard UI样例，详见fpsBattle.py #TestScoreBoard
8. 客户端新增UiInitFinished事件，创建UI时机使用这个, 详见API文档，样例testFpsSystem.py#**init**
9. button长按、短按实现样例, 详见fpsBattle.py#OnClickShoot
10. 特效文档，详见Particle Json.docx
11. 补充了骨骼模型组件使用文档
12. 服务端engineType组件更改，可以获取entity的类型；增加了客户端engineType。详见文档。
13. 子弹碰撞事件ProjectileDoHitEffectEvent修改：如果碰撞到Block，给出精确整型的BlockPos，击中面，可用BlockPos信息和blockInfo组件获取Block的id。详见文档和mod样例。
14. 增加客户端的右手物品更换事件，物品修改或物品性质改变时会通知，数量改变不会通知。
15. 新增UI文档，详见UI文档
16. 射子弹时，骨骼模型播放射击动作样例，详见testFpsSystem.py#PlayAni
17. 开镜及镜头缩放样例，详见fpsBattle.py#OnClickAim
18. Mod样例增加物品栏信息获取、物品消耗等操作，详见testFpsSystem.py#Shoot
