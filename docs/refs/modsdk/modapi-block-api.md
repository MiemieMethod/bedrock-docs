# 方块与世界接口<!-- md:flag china -->

本页列出中国版模组SDK中与方块读写、方块状态与附加值、方块实体数据、容器、红石、记分板、生物生成及配方相关的接口。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK体系，与国际版`@minecraft/server`脚本API无关。方块坐标以`tuple(int,int,int)`整数三元组表示，维度ID为整数（0=主世界、1=下界、2=末地）。
///

## 端与组件

| 组件 | 创建方法 | 服务端 | 客户端 | 说明 |
| --- | --- | :---: | :---: | --- |
| `BlockInfoCompServer`/`BlockInfoCompClient` | `CreateBlockInfo(levelId/playerId)` | ✔ | ✔ | 方块信息读写（坐标查询、碰撞盒、破坏时间等） |
| `BlockStateComponentServer` | `CreateBlockState(levelId)` | ✔ | — | 方块状态与附加值转换 |
| `ItemCompServer` | `CreateItem(playerId)` | ✔ | — | 容器物品读写（含酿造台） |
| `ChestContainerCompServer` | `CreateChestBlock(levelId)` | ✔ | — | 箱子容器操作 |
| `GameComponentServer`/`GameComponentClient` | `CreateGame(levelId)` | ✔ | ✔ | 记分板管理 |
| `RecipeCompServer` | `CreateRecipe(levelId)` | ✔ | — | 配方注册与查询 |

## 方块信息读写

通过`GetEngineCompFactory().CreateBlockInfo(levelId)`（服务端）或`CreateBlockInfo(levelId)`（客户端）获取方块信息组件。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetBlock(pos)` | 客户端 | `pos:tuple(int,int,int)` | `tuple(str,int)` | 获取当前维度指定坐标的方块`(标识符,附加值)`。未加载的区块返回`None`。 |
| `GetBlockNew(pos,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`dimensionId:int` | `dict` | 获取指定维度坐标的方块信息字典（含`name`、`aux`字段）。需该区块已加载。 |
| `SetBlock(pos,blockDict,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`blockDict:dict`（含`name`和`aux`字段）、`dimensionId:int` | `bool` | 在指定维度坐标放置方块，支持带附加值。 |
| `SetBlockNew(pos,blockDict,showParticles,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`blockDict:dict`、`showParticles:bool`、`dimensionId:int` | `bool` | 放置方块并可选显示破坏/放置粒子效果。 |
| `DestroyBlock(pos,dimensionId,playerId)` | 服务端 | `pos:tuple(int,int,int)`、`dimensionId:int`、`playerId:str`或`None` | `bool` | 摧毁指定坐标方块并产生掉落物，`playerId`决定掉落率计算参照玩家。 |
| `GetTopBlockHeight(pos,dimensionId)` | 服务端 | `pos:tuple(int,int)` (x,z)、`dimensionId:int` | `int` | 获取指定XZ坐标上最高的非空气方块的Y坐标。 |
| `GetBlockClip(pos)` | 客户端 | `pos:tuple(int,int,int)` | `dict` | 获取当前维度指定位置方块的碰撞盒（clip AABB）字典。 |
| `GetBlockCollision(pos,dimensionId)` | 服务端/客户端 | `pos:tuple(int,int,int)`、`dimensionId:int`（服务端）/ 无（客户端） | `dict` | 获取方块当前碰撞盒（collision AABB）字典。碰撞盒随相邻方块变化而变化。 |
| `GetDestroyTotalTime(blockName,itemName,miningArgs)` | 服务端/客户端 | `blockName:str`、`itemName:str`或`None`、`miningArgs:dict`或`None` | `float` | 计算使用指定工具破坏指定方块所需时间（秒）；`miningArgs`包含`haste`、`conduit_power`、`mining_fatigue`、`mining_efficiency`键。 |

```python
import mod.server.extraServerApi as serverApi

comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 获取主世界 (0,64,0) 处的方块
blockDict = comp.GetBlockNew((0, 64, 0), 0)
print(blockDict)  # {'name': 'minecraft:grass', 'aux': 0}

# 在指定位置放置石头
comp.SetBlock((0, 64, 0), {'name': 'minecraft:stone', 'aux': 0}, 0)
```

## 方块状态与附加值

通过`GetEngineCompFactory().CreateBlockState(levelId)`获取`BlockStateComponentServer`（仅服务端）。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetBlockStates(pos,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`dimensionId:int` | `dict`或`None` | 获取指定位置方块的全部方块状态字典，键为状态名，值为状态值。 |
| `SetBlockStates(pos,states,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`states:dict`、`dimensionId:int` | `bool` | 批量设置指定位置方块的方块状态。 |
| `GetBlockAuxValueFromStates(blockName,states)` | 服务端 | `blockName:str`、`states:dict` | `int` | 通过方块名和方块状态字典计算对应的附加值。 |
| `GetBlockStatesFromAuxValue(blockName,auxValue)` | 服务端 | `blockName:str`、`auxValue:int` | `dict` | 通过方块名和附加值反查方块状态字典。 |

```python
import mod.server.extraServerApi as serverApi

blockStateComp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)

# 获取某位置台阶方块的状态
states = blockStateComp.GetBlockStates((10, 65, 10), 0)
# 例：{'stone_slab_type': 'smooth_stone', 'top_slot_bit': False}

# 将台阶设置为顶部台阶
blockStateComp.SetBlockStates((10, 65, 10), {'top_slot_bit': True}, 0)

# 通过方块状态计算附加值
aux = blockStateComp.GetBlockAuxValueFromStates("minecraft:stone_slab", {'stone_slab_type': 'brick'})
```

## 方块实体数据

方块实体数据（`TileEntity`自定义数据）存储在`BlockInfoCompServer`上。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetBlockEntityData(pos,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`dimensionId:int` | `dict`或`None` | 获取指定位置方块实体的全部自定义数据字典。 |
| `SetBlockEntityData(pos,dataDict,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`dataDict:dict`、`dimensionId:int` | `bool` | 设置指定位置方块实体的自定义数据。 |
| `CleanBlockTileEntityCustomData(pos,dimensionId)` | 服务端 | `pos:tuple(int,int,int)`、`dimensionId:int` | `bool` | 清空指定位置方块实体绑定的全部自定义数据。 |
| `CreateFrameEffectForBlockEntity(pos,path,frameKeyName,effectPos)` | 客户端 | `pos:tuple(int,int,int)`、`path:str`、`frameKeyName:str`、`effectPos:tuple(float,float,float)` | `int`或`None` | 在自定义方块实体上创建序列帧特效，返回特效ID。`path`以`textures/`开头时不需扩展名，以`effects/`开头时需`.json`后缀。 |

## 微缩方块资源生成

旧版中国版资料还记录了一组面向**微缩方块**的资源导出接口。它们用于把世界中的一个已加载区域转换为微缩方块资源字符串，再由开发者自行保存为资源文件。

/// warning | 旧版资料存在命名差异
同一份旧版资料同时出现了`CreateMicroBlockResStr`与`CreateMicroBlockResJsonStr`两种写法。下表按资料能确认的参数语义整理，不对其历史命名差异作进一步外推。
///

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CreateMicroBlockResStr(...)`/`CreateMicroBlockResJsonStr(...)` | 服务端 | `identifier:str`、`start:tuple(int,int,int)`、`end:tuple(int,int,int)`、`colorMap:dict|None`、`isMerge:bool`、`icon:str` | `str` | 根据选区生成微缩方块资源JSON字符串。`identifier`不含`micro_block:`前缀；`colorMap`可覆盖特定方块颜色；`isMerge`用于合并同类方块降低复杂度；`icon`引用已注册到图集中的图标名。 |

旧版资料指出，这组接口只会导出选区中的方块数据，不会把实体数据一并导出；若选区包含未加载区域，则只能得到已加载部分的数据。对于朝向，`start`与`end`的先后顺序也会影响最终渲染方向。

## 容器

容器接口包含箱子和酿造台等。通过`CreateChestBlock(levelId)`获取`ChestContainerCompServer`，通过`CreateItem(playerId)`获取`ItemCompServer`。

| 接口 | 端 | 组件 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `GetChestBoxSize(playerId,pos,dimensionId)` | 服务端 | `CreateChestBlock(levelId)` | `playerId:None`（废弃）、`pos:tuple(int,int,int)`、`dimensionId:int` | `int` | 获取箱子容量槽位数；错误返回-1。 |
| `GetChestItem(slot,pos,dimensionId)` | 服务端 | `CreateChestBlock(levelId)` | `slot:int`、`pos:tuple(int,int,int)`、`dimensionId:int` | `dict`或`None` | 获取箱子指定槽位物品信息字典。 |
| `SetChestItem(slot,item,pos,dimensionId)` | 服务端 | `CreateChestBlock(levelId)` | `slot:int`、`item:dict`、`pos:tuple(int,int,int)`、`dimensionId:int` | `bool` | 设置箱子指定槽位的物品。 |
| `GetBrewingStandSlotItem(slot,pos,dimensionId)` | 服务端 | `CreateItem(playerId)` | `slot:int`（酿造台槽位枚举）、`pos:tuple(int,int,int)`、`dimensionId:int` | `dict`或`None` | 获取酿造台指定槽位的物品信息字典。 |
| `GetChestPairedPosition(pos,dimensionId)` | 服务端 | `CreateBlockInfo(levelId/playerId)` | `pos:tuple(int,int,int)`、`dimensionId:int` | `tuple(int,int,int)`或`None` | 获取大箱子中与指定半个箱子配对的另一半的坐标。 |

## 红石

通过`GetEngineCompFactory().CreateRedstone(pos,dimensionId)`获取红石组件（红石组件需传入方块坐标和维度创建）。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetStrength()` | 服务端 | 无 | `int` | 获取当前位置的红石信号强度（0–15）。 |
| `SetStrength(strength)` | 服务端 | `strength:int` | `bool` | 设置当前位置的红石信号强度，用于自定义红石源逻辑。 |

## 记分板

记分板接口位于`GameComponentServer`/`GameComponentClient`中，通过`CreateGame(levelId)`获取。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetAllScoreboardObjects()` | 服务端/客户端 | 无 | `list(dict)` | 获取全部记分项列表，每个字典包含`name`（记分项名称）和`displayName`（显示名称）字段。 |
| `GetAllPlayerScoreboardObjects(playerId)` | 服务端/客户端 | `playerId:str` | `list(dict)` | 获取指定玩家参与的全部记分项及其分值列表。 |
| `CreateScoreboardObjective(name,displayName)` | 服务端 | `name:str`、`displayName:str` | `bool` | 创建新记分项。 |
| `RemoveScoreboardObjective(name)` | 服务端 | `name:str` | `bool` | 删除指定记分项及其全部分值数据。 |
| `GetPlayerScoreByName(playerId,name)` | 服务端/客户端 | `playerId:str`、`name:str` | `int`或`None` | 获取指定玩家在指定记分项的分值。 |
| `SetPlayerScoreByName(playerId,name,score)` | 服务端 | `playerId:str`、`name:str`、`score:int` | `bool` | 设置指定玩家在指定记分项的分值。 |
| `AddPlayerScoreByName(playerId,name,score)` | 服务端 | `playerId:str`、`name:str`、`score:int` | `bool` | 为指定玩家在指定记分项增减分值，支持负值。 |

```python
import mod.server.extraServerApi as serverApi

gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)

# 创建记分项并初始化分值
gameComp.CreateScoreboardObjective("kills", "击杀数")
gameComp.SetPlayerScoreByName(playerId, "kills", 0)

# 记一次击杀
gameComp.AddPlayerScoreByName(playerId, "kills", 1)
kills = gameComp.GetPlayerScoreByName(playerId, "kills")
```

## 生物生成

生物生成规则管理接口位于服务端，通过`extraServerApi`的直接方法或`SpawnRuleComp`调用。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddSpawnRule(jsonStr)` | 服务端 | `jsonStr:str`（JSON字符串）| `bool` | 动态添加生物生成规则，相当于添加一条`spawn_rules`定义。 |
| `RemoveSpawnRule(identifier)` | 服务端 | `identifier:str` | `bool` | 移除指定标识符的生物生成规则。 |
| `SpawnMobInPos(entityType,pos,dimensionId)` | 服务端 | `entityType:str`、`pos:tuple(float,float,float)`、`dimensionId:int` | `str`或`None` | 在指定位置强制生成实体，绕过生成条件检查，返回`entityId`。 |

## 配方

通过`GetEngineCompFactory().CreateRecipe(levelId)`获取`RecipeCompServer`，仅服务端可用。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetRecipesByInput(inputDict)` | 服务端 | `inputDict:dict`（物品信息字典）| `list(dict)`或`None` | 获取以指定物品为原料的所有配方列表。 |
| `GetRecipesByResult(resultDict)` | 服务端 | `resultDict:dict`（物品信息字典）| `list(dict)`或`None` | 获取以指定物品为产出的所有配方列表。 |
| `GetRecipeResult(key)` | 服务端 | `key:str`（配方标识符）| `dict`或`None` | 获取指定配方的产出物品字典。 |
