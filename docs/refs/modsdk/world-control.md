# 世界控制接口<!-- md:flag china -->

本页列出中国版模组SDK中与世界时间、天气、游戏规则、消息和指令相关的常用运行时接口。这些接口属于中国版Python模组SDK，通常通过`mod.server.extraServerApi`或`mod.client.extraClientApi`创建组件后调用；它们不是国际版`@minecraft/server`脚本API的一部分。

/// warning | 与国际版脚本API分开使用
本页接口使用中国版组件体系，例如`CreateTime`、`CreateWeather`、`CreateGame`、`CreateMsg`和`CreateCommand`。不要将这些接口写入国际版行为包的JavaScript脚本，也不要将国际版脚本API的对象模型套用于本页接口。
///

## 端与组件

| 领域 | 组件创建方式 | 典型组件类 | 可用端 |
| --- | --- | --- | --- |
| 时间 | `GetEngineCompFactory().CreateTime(levelId)` | `TimeComponentServer`、`TimeComponentClient` | 服务端、客户端 |
| 维度局部时间 | `GetEngineCompFactory().CreateDimension(levelId)` | `DimensionCompServer`、`DimensionCompClient` | 服务端、客户端部分接口 |
| 天气 | `GetEngineCompFactory().CreateWeather(levelId)` | `WeatherComponentServer` | 服务端 |
| 游戏规则与世界行为 | `GetEngineCompFactory().CreateGame(levelId)` | `GameComponentServer`、`GameComponentClient` | 服务端、客户端部分接口 |
| 消息 | `GetEngineCompFactory().CreateMsg(levelId)`或`CreateGame(...)` | `MsgComponentServer`、`GameComponentServer`、`GameComponentClient` | 服务端、客户端部分接口 |
| 指令 | `GetEngineCompFactory().CreateCommand(levelId)` | `CommandCompServer` | 服务端 |

## 时间

世界时间接口分为全局时间和维度局部时间。时间值以游戏刻计量，1秒为20刻，1个游戏日为24000刻。局部时间规则启用后，指定维度可以拥有独立于全局世界时间的时间值和昼夜更替规则。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetTime()` | 服务端、客户端 | 无 | `int` | 获取当前世界全局时间。关闭昼夜更替后，当前世界时间会暂停。 |
| `SetTime(time)` | 服务端 | `time:int` | `bool` | 设置当前世界全局时间。 |
| `SetTimeOfDay(timeOfDay)` | 服务端 | `timeOfDay:int` | `bool` | 设置当前全局时间在一个游戏日内的位置。若目标时间早于当前日内时间，会跳至次日对应时间。 |
| `GetUseLocalTime(dimension)` | 服务端 | `dimension:int` | `bool` | 获取维度是否启用局部时间规则。 |
| `SetUseLocalTime(dimension,value)` | 服务端 | `dimension:int`、`value:bool` | `bool` | 为主世界或自定义维度启用局部时间规则。建议在游戏启动时统一调用。 |
| `GetLocalTime(dimension)` | 服务端 | `dimension:int` | `int` | 获取指定维度时间；若未启用局部时间规则，则返回全局时间。 |
| `GetLocalTime()` | 客户端 | 无 | `int` | 获取客户端当前维度时间；若未启用局部时间规则，则返回全局时间。 |
| `SetLocalTime(dimension,time)` | 服务端 | `dimension:int`、`time:int` | `bool` | 设置已启用局部时间规则的维度时间。 |
| `SetLocalTimeOfDay(dimension,timeOfDay)` | 服务端 | `dimension:int`、`timeOfDay:int` | `bool` | 设置局部维度在一个游戏日内的位置。 |
| `GetLocalDoDayNightCycle(dimension)` | 服务端 | `dimension:int` | `bool` | 获取局部维度是否打开昼夜更替；若未启用局部时间规则，则返回全局昼夜更替规则。 |
| `SetLocalDoDayNightCycle(dimension,value)` | 服务端 | `dimension:int`、`value:bool` | `bool` | 设置已启用局部时间规则的维度是否进行昼夜更替。 |

/// note | 局部时间规则的限制
原版`time`指令、`gamerule dodaylightcycle`、`daylock`及相关设置不会作用于局部维度。原版下界与末地不受时间规则影响，始终没有正常昼夜更替。
///

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
dimensionComp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
dimensionComp.SetUseLocalTime(3, True)
dimensionComp.SetLocalTimeOfDay(3, 6000)
dimensionComp.SetLocalDoDayNightCycle(3, False)
```

## 天气

天气接口同样分为全局天气和维度局部天气。局部天气启用后，指定维度可以拥有独立的下雨强度、下雨持续时间、打雷强度、打雷持续时间和天气循环规则。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `IsRaining()` | 服务端 | 无 | `bool` | 获取全局天气是否下雨。 |
| `IsThunder()` | 服务端 | 无 | `bool` | 获取全局天气是否打雷。 |
| `SetRaining(level,time)` | 服务端 | `level:float`、`time:int` | `bool` | 设置全局下雨强度和持续时间。`level`范围为0至1，`time`以刻计量。 |
| `SetThunder(level,time)` | 服务端 | `level:float`、`time:int` | `bool` | 设置全局打雷强度和持续时间。`level`范围为0至1，`time`以刻计量。 |
| `GetDimensionUseLocalWeather(dimension)` | 服务端 | `dimension:int` | `bool` | 获取维度是否启用局部天气规则。 |
| `SetDimensionUseLocalWeather(dimension,value)` | 服务端 | `dimension:int`、`value:bool` | `bool` | 为主世界或自定义维度启用局部天气规则。 |
| `GetDimensionLocalWeatherInfo(dimension)` | 服务端 | `dimension:int` | `dict` | 获取局部维度天气信息，包括下雨、打雷和天气循环相关数据。 |
| `SetDimensionLocalRain(dimension,rainLevel,rainTime)` | 服务端 | `dimension:int`、`rainLevel:float`、`rainTime:int` | `bool` | 设置局部维度下雨强度和持续时间。 |
| `SetDimensionLocalThunder(dimension,thunderLevel,thunderTime)` | 服务端 | `dimension:int`、`thunderLevel:float`、`thunderTime:int` | `bool` | 设置局部维度打雷强度和持续时间。 |
| `SetDimensionLocalDoWeatherCycle(dimension,value)` | 服务端 | `dimension:int`、`value:bool` | `bool` | 设置局部维度是否开启天气循环。 |

/// note | 局部天气规则的限制
原版`weather`指令以及`SetRaining`、`SetThunder`不会影响已启用局部天气规则的维度。原版下界与末地没有天气系统，因此天气规则对这两个维度无效。
///

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
weatherComp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
weatherComp.SetDimensionUseLocalWeather(0, True)
weatherComp.SetDimensionLocalRain(0, 0.5, 1200)
weatherComp.SetDimensionLocalDoWeatherCycle(0, True)
```

## 游戏规则和世界行为

`GameComponentServer`提供的接口既包含原版游戏规则的读取与写入，也包含中国版额外的世界行为开关。部分接口只在Apollo网络服环境可用。

### 游戏规则、难度和模式

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetGameRulesInfoServer()` | 服务端 | 无 | `dict` | 获取游戏规则字典。 |
| `SetGameRulesInfoServer(gameRuleDict)` | 服务端 | `gameRuleDict:dict` | `bool` | 设置游戏规则字典。`option_info`和`cheat_info`下的每个规则项均可选。 |
| `IsLockGameRulesInfo()` | 服务端 | 无 | `bool` | 获取当前世界游戏规则是否被锁定。 |
| `LockGameRulesInfo(lock)` | 服务端 | `lock:bool` | `bool` | 锁定或解锁本次游戏中的游戏规则修改。 |
| `GetGameDiffculty()` | 服务端 | 无 | `int` | 获取游戏难度，枚举值为和平、简单、普通、困难对应0至3。 |
| `SetGameDifficulty(difficulty)` | 服务端 | `difficulty:int` | `bool` | 设置游戏难度。若难度已锁定或处于极限模式，可能失败。 |
| `IsLockDifficulty()` | 服务端 | 无 | `bool` | 获取当前世界游戏难度是否被锁定。 |
| `LockDifficulty(lock)` | 服务端 | `lock:bool` | `bool` | 锁定或解锁本次游戏中的难度修改。 |
| `GetGameType()` | 服务端 | 无 | `int` | 获取默认游戏模式，生存、创造、冒险对应0至2。 |
| `SetDefaultGameType(gameType)` | 服务端 | `gameType:int` | `bool` | 设置默认游戏模式。极限模式不可修改默认游戏模式。 |
| `IsLockGameType()` | 服务端 | 无 | `bool` | 获取当前世界游戏类型是否被锁定。 |
| `LockGameType(lock)` | 服务端 | `lock:bool` | `bool` | 锁定或解锁本次游戏中的默认游戏类型和个人游戏类型修改。 |

`SetGameRulesInfoServer`使用的字典分为`option_info`和`cheat_info`两组。常见字段如下：

| 组 | 字段 | 类型 | 说明 |
| --- | --- | --- | --- |
| `option_info` | `pvp` | `bool` | 玩家间伤害。 |
| `option_info` | `show_coordinates` | `bool` | 显示坐标。 |
| `option_info` | `fire_spreads` | `bool` | 火焰蔓延。 |
| `option_info` | `tnt_explodes` | `bool` | TNT爆炸。 |
| `option_info` | `mob_loot` | `bool` | 生物战利品。 |
| `option_info` | `natural_regeneration` | `bool` | 自然生命恢复。 |
| `option_info` | `respawn_block_explosion` | `bool` | 重生点方块爆炸。 |
| `option_info` | `respawn_radius` | `int` | 重生半径，当前支持0至128。 |
| `option_info` | `tile_drops` | `bool` | 方块掉落。 |
| `option_info` | `immediate_respawn` | `bool` | 立即重生。 |
| `cheat_info` | `enable` | `bool` | 激活作弊。 |
| `cheat_info` | `always_day` | `bool` | 终为白日。 |
| `cheat_info` | `mob_griefing` | `bool` | 生物破坏。 |
| `cheat_info` | `keep_inventory` | `bool` | 保留物品栏。 |
| `cheat_info` | `weather_cycle` | `bool` | 天气更替。 |
| `cheat_info` | `mob_spawn` | `bool` | 生物生成。 |
| `cheat_info` | `entities_drop_loot` | `bool` | 实体掉落战利品。 |
| `cheat_info` | `daylight_cycle` | `bool` | 开启昼夜更替。 |
| `cheat_info` | `command_blocks_enabled` | `bool` | 启用命令方块。 |
| `cheat_info` | `random_tick_speed` | `int` | 随机刻速度。 |

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
gameComp.SetGameRulesInfoServer({
    "cheat_info": {
        "enable": True,
        "always_day": True
    }
})
```

### 世界行为开关

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetSeed()` | 服务端 | 无 | `int` | 获取存档种子。 |
| `GetLevelGravity()` | 服务端 | 无 | `float` | 获取世界重力因子。 |
| `SetLevelGravity(data)` | 服务端 | `data:float` | `bool` | 设置世界重力因子。实体也可通过实体重力组件单独设置重力因子。 |
| `SetHurtCD(cdTime)` | 服务端 | `cdTime:int` | `bool` | 设置全局受击间隔，单位为刻。 |
| `ForbidLiquidFlow(forbid)` | 服务端 | `forbid:bool` | `bool` | 禁止或允许地图中的流体流动。重新允许后，既有流体通常需要方块更新才会继续流动。 |
| `DisableVineBlockSpread(disable)` | 服务端 | `disable:bool` | 无 | 设置是否禁用藤蔓蔓延生长。 |
| `SetCanActorSetOnFireByLightning(enable)` | 服务端 | `enable:bool` | `bool` | 设置闪电是否可以点燃实体。 |
| `SetCanBlockSetOnFireByLightning(enable)` | 服务端 | `enable:bool` | `bool` | 设置闪电是否可以点燃方块。只有普通及以上难度且开启火焰蔓延时，闪电才会点燃方块。 |
| `SetDisableContainers(isDisable)` | 服务端 | `isDisable:bool` | `bool` | 禁止或允许打开所有容器界面，包括玩家背包、容器方块界面和部分实体交互界面。 |
| `SetDisableDropItem(isDisable)` | 服务端 | `isDisable:bool` | `bool` | 设置是否禁止丢弃物品。创造模式下物品仍可丢弃。 |
| `SetDisableGravityInLiquid(isDisable)` | 服务端 | `isDisable:bool` | `bool` | 设置是否屏蔽所有实体在液体中的重力。 |
| `SetDisableHunger(isDisable)` | 服务端 | `isDisable:bool` | `bool` | 设置是否屏蔽饥饿度。隐藏饥饿度界面应使用客户端接口。 |
| `GetPistonMaxInteractionCount()` | 服务端、客户端 | 无 | `int` | 获取活塞或黏性活塞最多推动的方块数量。 |
| `SetPistonMaxInteractionCount(value)` | 服务端 | `value:int` | `bool` | 设置活塞或黏性活塞最多推动的方块数量，范围为1至1024；该设置不存档。 |

### 禁用物品

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddBannedItem(itemName)` | 服务端 | `itemName:str` | `bool` | 增加禁用物品。`itemName`格式为`namespace:name:auxvalue`，附加值可省略为0或使用`*`匹配任意附加值。 |
| `RemoveBannedItem(itemName)` | 服务端 | `itemName:str` | `bool` | 移除禁用物品。 |
| `ClearBannedItems()` | 服务端 | 无 | `bool` | 清空禁用物品。 |
| `GetBannedItemList()` | 服务端 | 无 | `list(str)`或`None` | 获取禁用物品列表。 |

### Apollo专用世界保护

以下接口仅Apollo可用，不应视为普通中国版单机或联机大厅模组的通用能力。

| 接口 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `AddBlockProtectField(dimensionId,startPos,endPos)` | `dimensionId:int`、`startPos:tuple(int,int,int)`、`endPos:tuple(int,int,int)` | `int` | 添加玩家或实体无法破坏方块的区域，成功时返回区域唯一ID，失败时返回`-1`。 |
| `RemoveBlockProtectField(field)` | `field:int` | `bool` | 取消一个方块保护区域。 |
| `CleanBlockProtectField()` | 无 | `bool` | 取消全部方块保护区域。 |
| `OpenCityProtect()` | 无 | `bool` | 开启城市保护，包含禁止破坏方块、禁止对方块使用物品、禁止怪物攻击玩家、禁止玩家互相攻击、禁止日夜切换、禁止天气变化和禁止怪物群落刷新。 |
| `IsDisableCommandMinecart()` | 无 | `bool` | 获取当前是否禁止命令方块矿车运行内置逻辑指令。 |
| `SetDisableCommandMinecart(isDisable)` | `isDisable:bool` | `bool` | 设置是否禁止命令方块矿车运行内置逻辑指令。 |

## 消息

消息接口可以向聊天栏、左上角通知区域、物品栏上方提示区域和弹出提示区域输出文本。服务端接口通常影响指定玩家或所有玩家，客户端接口通常只影响本地玩家。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `NotifyOneMessage(playerId,msg,color)` | 服务端 | `playerId:str`、`msg:str`、`color:str` | 无 | 给指定玩家发送聊天框消息。`color`可使用格式化代码字符串，默认白色。 |
| `SendMsg(name,msg)` | 服务端 | `name:str`、`msg:str` | `bool` | 模拟指定玩家向所有人发送聊天栏消息。若玩家名不存在，会随机选择一个玩家发出消息。 |
| `SendMsgToPlayer(fromEntityId,toEntityId,msg)` | 服务端 | `fromEntityId:str`、`toEntityId:str`、`msg:str` | 无 | 模拟一个玩家给另一个玩家发送聊天栏消息。 |
| `SetNotifyMsg(msg,color)` | 服务端 | `msg:str`、`color:str` | `bool` | 设置消息通知，颜色可由`GenerateColor`生成。 |
| `SetLeftCornerNotify(textMsg)` | 客户端 | `textMsg:str` | `bool` | 设置左上角通知信息。 |
| `SetTipMessage(message)` | 服务端、客户端 | `message:str` | `bool` | 服务端在所有玩家物品栏上方显示tip类型通知；客户端在本地玩家显示该通知。 |
| `SetOneTipMessage(playerId,message)` | 服务端 | `playerId:str`、`message:str` | `bool` | 在指定玩家物品栏上方显示tip类型通知。 |
| `SetPopupNotice(message,subtitle)` | 服务端、客户端 | `message:str`、`subtitle:str` | `bool` | 服务端在所有玩家物品栏上方显示popup类型通知；客户端在本地玩家显示该通知。 |
| `SetOnePopupNotice(playerId,message,subtitle)` | 服务端 | `playerId:str`、`message:str`、`subtitle:str` | `bool` | 在指定玩家物品栏上方显示popup类型通知。 |
| `SetPopupState(state)` | 客户端 | `state:int` | `bool` | 设置popup消息栏状态。`0`为原版开启，`1`为关闭，`2`为使用接口设置的物品字典中`customTips`第一行作为弹出信息。 |

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
gameComp.SetTipMessage(serverApi.GenerateColor("RED") + "警告")
gameComp.SetPopupNotice("消息通知", "消息子标题")
```

## 指令

指令接口只在服务端可用。`SetCommand`用于从脚本执行游戏内指令，权限等级接口用于读取或设置与服务器配置相对应的默认权限。

| 接口 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `SetCommand(cmdStr,entityId=None,showOutput=False)` | `cmdStr:str`、`entityId:str`、`showOutput:bool` | `bool` | 执行游戏内指令。若不指定`entityId`，会随机选择玩家。`showOutput`为`True`时，成功输出会进入聊天窗口并触发命令输出事件。 |
| `GetCommandPermissionLevel()` | 无 | `int` | 获取使用`/op`命令时OP的权限等级，对应`server.properties`中的`op-permission-level`。 |
| `SetCommandPermissionLevel(opLevel)` | `opLevel:int` | `bool` | 设置后续获取OP身份的玩家权限等级，不修改已经获取OP的玩家；建议在游戏初始化时调用。 |
| `GetDefaultPlayerPermissionLevel()` | 无 | `int` | 获取新玩家加入时的默认权限身份，对应`server.properties`中的`default-player-permission-level`。 |
| `SetDefaultPlayerPermissionLevel(opLevel)` | `opLevel:int` | `bool` | 设置后续新加入玩家的默认权限身份，不修改已经加入过游戏的玩家；建议在游戏初始化时调用。 |

权限等级含义如下：

| 配置 | 值 | 含义 |
| --- | --- | --- |
| `op-permission-level` | `1` | OP可以绕过重生点保护。 |
| `op-permission-level` | `2` | OP可以使用所有单人游戏作弊命令。 |
| `op-permission-level` | `3` | OP可以使用大多数多人游戏中独有的命令。 |
| `op-permission-level` | `4` | OP可以使用所有命令。 |
| `default-player-permission-level` | `0` | 访客。 |
| `default-player-permission-level` | `1` | 成员。 |
| `default-player-permission-level` | `2` | 操作员。 |
| `default-player-permission-level` | `3` | 自定义。 |

```python
import mod.server.extraServerApi as serverApi

levelId = serverApi.GetLevelId()
commandComp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
commandComp.SetCommand("/tp @p 100 5 100")
commandComp.SetCommandPermissionLevel(4)
```