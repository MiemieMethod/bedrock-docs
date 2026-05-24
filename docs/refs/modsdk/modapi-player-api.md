# 玩家接口<!-- md:flag china -->

本页列出中国版模组SDK中专属于玩家（`Player`）的接口，包括经验与等级、饥饿与食物、玩家特有行为、运动器、摄像机控制及渲染接口。适用于所有玩家但不专属于玩家的实体属性（生命值、速度等）请参见[实体接口](modapi-entity-api.md)中的同名接口。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK体系，与国际版`@minecraft/server`脚本API无关。玩家标识符（`playerId`）为字符串类型，在服务端与客户端语义相同，但客户端仅可访问当前本地玩家。
///

## 端与组件

| 组件 | 创建方法 | 服务端 | 客户端 | 说明 |
| --- | --- | :---: | :---: | --- |
| `ExpComponentServer` | `CreateExp(playerId)` | ✔ | — | 经验值读写 |
| `LevelComponentServer`/客户端 | `CreateLv(playerId)` | ✔ | — | 玩家等级读写 |
| `GameComponentServer`/`GameComponentClient` | `CreateGame(levelId)` | ✔ | ✔ | 游戏模式、饥饿、护甲值等玩家状态（客户端需传`playerId`参数） |
| `PlayerCompServer` | `CreatePlayer(playerId)` | ✔ | — | 玩家特有行为（附魔种子、消耗度等） |
| `ActorMotionComponentServer` | `CreateActorMotion(playerId)` | ✔ | — | 玩家运动器（与实体运动器共用组件，使用`Player`专属接口） |
| `CameraCompClient` | `CreateCamera(playerId)` | — | ✔ | 摄像机控制 |
| `AttrCompServer`/`AttrCompClient` | `CreateAttr(playerId)` | ✔ | ✔ | 玩家属性，与实体属性接口相同，见[实体接口](modapi-entity-api.md) |

## 经验与等级

通过`GetEngineCompFactory().CreateExp(playerId)`获取`ExpComponentServer`，`CreateLv(playerId)`获取等级组件。

| 接口 | 端 | 组件 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `AddPlayerExperience(exp)` | 服务端 | `CreateExp(playerId)` | `exp:int` | `bool` | 为玩家增加指定数量的经验值，支持负值以扣减经验。 |
| `GetPlayerExp(isPercent)` | 服务端/客户端 | `CreateExp(playerId)` / `CreateGame(levelId)` | `isPercent:bool` | `float` | 获取玩家当前等级下的经验值；`isPercent=True`时返回百分比（0.0–1.0），`isPercent=False`时返回绝对经验值。 |
| `AddPlayerLevel(level)` | 服务端 | `CreateLv(playerId)` | `level:int` | `bool` | 为玩家增加指定等级数，支持负值以扣减等级。 |
| `GetPlayerLevel()` | 服务端/客户端 | `CreateLv(playerId)` / `CreateGame(levelId)` | 无 | `int` | 获取玩家当前等级。 |
| `GetPlayerCurLevelExp(playerId)` | 客户端 | `CreateGame(levelId)` | `playerId:str` | `int` | 获取玩家升至下一等级所需要的总经验值。 |

```python
import mod.server.extraServerApi as serverApi

# 为玩家添加100经验值
expComp = serverApi.GetEngineCompFactory().CreateExp(playerId)
expComp.AddPlayerExperience(100)

# 获取玩家当前等级
lvComp = serverApi.GetEngineCompFactory().CreateLv(playerId)
level = lvComp.GetPlayerLevel()
```

## 饥饿、消耗度与护甲

| 接口 | 端 | 组件 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `GetArmorValue(playerId)` | 客户端 | `CreateGame(levelId)` | `playerId:str` | `int` | 获取玩家当前护甲值（综合装备防御量与接口附加量）。 |
| `GetPlayerCurrentExhaustionValue()` | 服务端 | `CreatePlayer(playerId)` | 无 | `float` | 获取玩家当前食物消耗度（`foodExhaustionLevel`），详见饥饿机制。 |
| `GetEnchantmentSeed()` | 服务端 | `CreatePlayer(playerId)` | 无 | `int` | 获取玩家附魔种子，决定附魔台上该玩家看到的可附魔选项。 |

## 游戏模式与基本行为

通过`GetEngineCompFactory().CreateGame(levelId)`获取`GameComponentServer`/`GameComponentClient`，以下接口需在服务端调用。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `SetPlayerGameType(gameType)` | 服务端 | `gameType:int`（游戏模式枚举） | `bool` | 设置玩家游戏模式，值见`GameType`枚举（0=生存，1=创造，2=冒险）。注意：组件以`levelId`创建但需传`playerId`创建后调用或使用`PlayerCompServer`。 |
| `SetCanFly(isAble)` | 服务端 | `isAble:bool` | `bool` | 设置玩家是否可以飞行（不受游戏模式限制）。 |
| `IsFlying()` | 服务端/客户端 | 无 | `bool` | 获取玩家当前是否处于飞行状态。 |
| `SetMoveLock(lock)` | 服务端 | `lock:bool` | `bool` | 锁定/解锁玩家移动输入，锁定后玩家无法通过操作移动。 |
| `SetLookLock(lock)` | 服务端 | `lock:bool` | `bool` | 锁定/解锁玩家视角旋转输入。 |

## 玩家运动器

玩家运动器与实体运动器使用同一组件（`ActorMotionComponentServer`），但提供了针对玩家优化的专属接口，支持同时在服务端和客户端同步运行。接口签名与实体运动器类似，详见[实体接口 · 运动器](modapi-entity-api.md#运动器)。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddPlayerAroundEntityMotion(eID,angularVelocity,axis,lockDir,stopRad,radius)` | 服务端 | `eID:str`、`angularVelocity:float`（弧度/秒）、`axis:tuple(float,float,float)`、`lockDir:bool`、`stopRad:float`、`radius:float` | `int` | 为玩家添加绕实体圆周运动器，运动同步在客户端和服务端执行。返回运动器ID。 |
| `AddPlayerAroundPointMotion(center,angularVelocity,axis,lockDir,stopRad)` | 服务端 | `center:tuple(float,float,float)`、`angularVelocity:float`、`axis:tuple(float,float,float)`、`lockDir:bool`、`stopRad:float` | `int` | 为玩家添加绕固定点圆周运动器。返回运动器ID。 |
| `AddPlayerTrackMotion(targetPos,durationTime,startSpeed,endSpeed,isAsync,isLoop,lockDir)` | 服务端 | `targetPos:tuple`、`durationTime:float`、`startSpeed:float`、`endSpeed:float`、`isAsync:bool`、`isLoop:bool`、`lockDir:bool` | `int` | 为玩家添加路径跟踪运动器。返回运动器ID。 |
| `StartPlayerMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 启动指定玩家运动器。 |
| `StopPlayerMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 停止指定玩家运动器。 |
| `RemovePlayerMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 移除并销毁指定玩家运动器。 |

/// note | 玩家运动器与输入控制
玩家运动器不屏蔽玩家的手动移动输入。若需完全接管玩家位置，建议配合`SetMoveLock(True)`使用，或调用`DepartCamera`分离摄像机与玩家，以便精确控制玩家朝向。
///

## 摄像机

通过`GetEngineCompFactory().CreateCamera(playerId)`获取`CameraCompClient`，所有摄像机接口仅在客户端可用，通常由服务端通过事件通知客户端执行。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetCameraFov()` | 客户端 | 无 | `float` | 获取摄像机当前视野角（FOV），单位角度。 |
| `SetCameraFov(fov)` | 客户端 | `fov:float` | `bool` | 设置摄像机视野角；设置为0恢复默认值。 |
| `GetCameraPos()` | 客户端 | 无 | `tuple(float,float,float)` | 获取摄像机当前世界坐标。 |
| `SetCameraPos(pos)` | 客户端 | `pos:tuple(float,float,float)` | `bool` | 设置摄像机位置，需先调用`DepartCamera`分离摄像机。 |
| `GetCameraRot()` | 客户端 | 无 | `tuple(float,float)` | 获取摄像机旋转角，格式为`(俯仰角,偏航角)`。 |
| `SetCameraRot(rot)` | 客户端 | `rot:tuple(float,float)` | `bool` | 设置摄像机旋转角。 |
| `DepartCamera(rot,pos)` | 客户端 | `rot:tuple(float,float)`、`pos:tuple(float,float,float)` | `bool` | 将摄像机从玩家分离，使用独立位置和旋转，此后可自由控制摄像机。 |
| `CancelDepartCamera()` | 客户端 | 无 | `bool` | 取消摄像机分离，恢复随玩家移动。 |
| `SetCameraMotionParams(params)` | 客户端 | `params:dict` | `bool` | 设置摄像机插值运动参数，实现平滑过渡效果。 |

```python
import mod.client.extraClientApi as clientApi

playerId = clientApi.GetLocalPlayerId()
cameraComp = clientApi.GetEngineCompFactory().CreateCamera(playerId)

# 分离摄像机并将其移至玩家头顶正上方俯视
currentRot = cameraComp.GetCameraRot()
currentPos = cameraComp.GetCameraPos()
cameraComp.DepartCamera((90, currentRot[1]), (currentPos[0], currentPos[1] + 20, currentPos[2]))

# 完成后恢复
# cameraComp.CancelDepartCamera()
```

## 收集在线数据

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CollectOnlineClientData(playerIds)` | 服务端 | `playerIds:list(str)` | 无 | 向客户端请求在线玩家的客户端数据（如设备信息、输入模式等），数据通过`ClientDataLoadEvent`事件异步返回。 |