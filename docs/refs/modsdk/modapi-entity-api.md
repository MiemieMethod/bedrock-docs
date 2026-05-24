# 实体接口<!-- md:flag china -->

本页列出中国版模组SDK中与实体（生物及非生物实体）读写、控制相关的全部接口，涵盖属性、位置、旋转、缩放、类型、名称、物品栏、状态效果、行为与AI意向、运动器、维度传送及实体生命周期管理。接口域总览入口见[中国版ModAPI接口域索引](modapi-interface-index.md)。

/// warning | 与国际版脚本API分开使用
本页接口属于中国版Python模组SDK体系，与国际版`@minecraft/server`脚本API无关。实体标识符（`entityId`）为字符串类型，在服务端和客户端之间不能直接互换，客户端只能操作当前维度中已加载的实体。
///

## 端与组件

以下为本页涉及的全部组件，以及对应的创建方法与可用端。

| 组件 | 创建方法 | 服务端 | 客户端 | 说明 |
| --- | --- | :---: | :---: | --- |
| `AttrCompServer`/`AttrCompClient` | `CreateAttr(entityId)` | ✔ | ✔ | 实体属性（生命、速度、护甲等） |
| `PosCompServer`/`PosCompClient` | `CreatePos(entityId)` | ✔ | ✔ | 实体坐标位置 |
| `RotCompServer`/`RotCompClient` | `CreateRot(entityId)` | ✔ | ✔ | 实体视角旋转 |
| `RotCompClient`（Body） | `CreateRot(entityId)` | — | ✔ | 实体身体朝向 |
| `ScaleCompServer`/`ScaleCompClient` | `CreateScale(entityId)` | ✔ | ✔ | 实体缩放比例 |
| `EngineTypeCompServer`/`EngineTypeCompClient` | `CreateEngineType(entityId)` | ✔ | ✔ | 实体类型标识符 |
| `NameCompServer`/`NameCompClient` | `CreateName(entityId)` | ✔ | ✔ | 实体名称 |
| `BreathCompServer`/`GameCompClient` | `CreateBreath(entityId)` | ✔ | ✔ | 实体氧气储备 |
| `EntityEventComponentServer` | `CreateEntityEvent(entityId)` | ✔ | — | 实体定义事件与组件组 |
| `ActorMotionComponentServer` | `CreateActorMotion(entityId)` | ✔ | — | 实体运动器 |
| `EffectComponentServer`/`EffectComponentClient` | `CreateEffect(entityId)` | ✔ | ✔ | 实体状态效果 |
| `ItemCompServer`/`ItemCompClient` | `CreateItem(entityId)` | ✔ | ✔ | 实体物品栏 |

## 特性与属性

通过`GetEngineCompFactory().CreateAttr(entityId)`获取`AttrCompServer`或`AttrCompClient`。特性类型通过`GetMinecraftEnum().AttrType`枚举指定。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetAttrValue(attrType)` | 服务端/客户端 | `attrType:int` | `float` | 获取实体当前属性值。若实体不存在该属性，返回-1。注意`damage`、`knockback_resistance`、`jump_strength`只能通过服务端准确获取。 |
| `SetAttrValue(attrType,value)` | 服务端 | `attrType:int`、`value:float` | `bool` | 设置实体当前属性值。 |
| `GetAttrMaxValue(attrType)` | 服务端/客户端 | `attrType:int` | `float` | 获取实体属性最大值。 |
| `SetAttrMaxValue(attrType,value)` | 服务端 | `attrType:int`、`value:float` | `bool` | 设置实体属性最大值。 |
| `GetAllComponentsName()` | 服务端 | 无 | `list` | 获取该实体当前已附加的全部组件名列表，用于调试实体定义状态。 |

```python
import mod.server.extraServerApi as serverApi

comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
attrType = serverApi.GetMinecraftEnum().AttrType
# 将实体当前生命值设置为最大值
maxHp = comp.GetAttrMaxValue(attrType.HEALTH)
comp.SetAttrValue(attrType.HEALTH, maxHp)
```

## 位置与变换

| 接口 | 端 | 组件 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `GetPos()` | 服务端/客户端 | `CreatePos(entityId)` | 无 | `tuple(float,float,float)`或`None` | 获取实体渲染中心坐标（通常为脚底上方约1.62格，玩家为眼睛位置下方）。 |
| `SetPos(pos)` | 服务端 | `CreatePos(entityId)` | `pos:tuple(float,float,float)` | `bool` | 传送实体至指定坐标。 |
| `GetFootPos()` | 服务端/客户端 | `CreatePos(entityId)` | 无 | `tuple(float,float,float)`或`None` | 获取实体脚底坐标。 |
| `SetFootPos(pos)` | 服务端 | `CreatePos(entityId)` | `pos:tuple(float,float,float)` | `bool` | 传送实体脚底至指定坐标，适合精确地面放置。 |
| `GetRot()` | 服务端/客户端 | `CreateRot(entityId)` | 无 | `tuple(float,float)` | 获取实体视角旋转角，格式为`(俯仰角,偏航角)`，单位角度。 |
| `SetRot(rot)` | 服务端 | `CreateRot(entityId)` | `rot:tuple(float,float)` | `bool` | 设置实体视角旋转角，格式为`(俯仰角,偏航角)`。 |
| `GetBodyRot()` | 客户端 | `CreateRot(entityId)` | 无 | `float` | 获取实体身体绕竖直方向的旋转角（偏航角），单位角度；无身体时返回0。 |
| `GetScale()` | 服务端/客户端 | `CreateScale(entityId)` | 无 | `float` | 获取实体当前缩放比例。 |
| `SetScale(scale)` | 服务端 | `CreateScale(entityId)` | `scale:float` | `bool` | 设置实体缩放比例，影响碰撞箱和视觉大小。 |
| `GetMotion()` | 服务端/客户端 | `CreateActorMotion(entityId)` | 无 | `tuple(float,float,float)` | 获取实体当前速度向量。 |
| `SetMotion(motion)` | 服务端 | `CreateActorMotion(entityId)` | `motion:tuple(float,float,float)` | `bool` | 直接设置实体速度向量，用于施加冲击。 |

## 类型与名称

| 接口 | 端 | 组件 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- | --- |
| `GetEngineTypeStr()` | 服务端/客户端 | `CreateEngineType(entityId)` | 无 | `str` | 获取实体的类型标识符字符串，如`minecraft:zombie`。 |
| `IsEntityAlive(entityId)` | 服务端/客户端 | `CreateEngineType(entityId)` | `entityId:str` | `bool` | 判断该实体是否仍然存活（未被销毁）。 |
| `GetName()` | 服务端/客户端 | `CreateName(entityId)` | 无 | `str` | 获取实体的显示名称。 |
| `SetName(name)` | 服务端 | `CreateName(entityId)` | `name:str` | `bool` | 设置实体的显示名称。 |
| `GetCurrentAirSupply()` | 服务端/客户端 | `CreateBreath(entityId)` / `CreateGame(levelId)` | 无 | `int` | 获取实体当前氧气储备值（单位为逻辑帧，即1秒=20帧）。 |
| `SetCurrentAirSupply(value)` | 服务端 | `CreateBreath(entityId)` | `value:int` | `bool` | 设置实体当前氧气储备值。 |

## 行为与AI意向

通过`GetEngineCompFactory().CreateEntityEvent(entityId)`获取`EntityEventComponentServer`，可动态修改实体的定义文件组件与组件组。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddActorComponent(componentName,componentValue)` | 服务端 | `componentName:str`、`componentValue:dict` | `bool` | 向实体添加指定AI组件，并设置其初始值，等效于在定义文件中添加组件。 |
| `RemoveActorComponent(componentName)` | 服务端 | `componentName:str` | `bool` | 从实体移除指定AI组件。 |
| `AddActorComponentGroup(groupName)` | 服务端 | `groupName:str` | `bool` | 激活实体定义文件中的指定组件组。 |
| `RemoveActorComponentGroup(groupName)` | 服务端 | `groupName:str` | `bool` | 停用实体定义文件中的指定组件组。 |
| `TriggerCustomEvent(eventName)` | 服务端 | `eventName:str` | `bool` | 触发实体定义文件中的自定义事件，可在事件中嵌套`add_component_group`等操作。 |

## 运动器

运动器允许程序化控制实体运动轨迹，通过`GetEngineCompFactory().CreateActorMotion(entityId)`获取`ActorMotionComponentServer`。运动器创建后需调用`StartEntityMotion`激活，可叠加多个。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddEntityAroundEntityMotion(eID,angularVelocity,axis,lockDir,stopRad,radius)` | 服务端 | `eID:str`、`angularVelocity:float`（弧度/秒）、`axis:tuple(float,float,float)`、`lockDir:bool`、`stopRad:float`、`radius:float` | `int` | 为实体添加绕另一实体做圆周运动的运动器，返回运动器ID；失败返回-1。`stopRad`为0时永续。`radius`为-1时使用当前距离为半径。 |
| `AddEntityAroundPointMotion(center,angularVelocity,axis,lockDir,stopRad)` | 服务端 | `center:tuple(float,float,float)`、`angularVelocity:float`、`axis:tuple(float,float,float)`、`lockDir:bool`、`stopRad:float` | `int` | 为实体添加绕固定点做圆周运动的运动器，返回运动器ID。 |
| `AddEntityLinearMotion(targetPos,durationTime,isAsync,isLoop,lockDir,stopWhenHurt)` | 服务端 | `targetPos:tuple(float,float,float)`、`durationTime:float`、`isAsync:bool`、`isLoop:bool`、`lockDir:bool`、`stopWhenHurt:bool` | `int` | 为实体添加线性（直线）运动器，返回运动器ID。 |
| `StartEntityMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 启动指定运动器。 |
| `StopEntityMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 停止指定运动器。 |
| `RemoveEntityMotion(motionId)` | 服务端 | `motionId:int` | `bool` | 移除并销毁指定运动器。 |

```python
import mod.server.extraServerApi as serverApi

motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
# 使实体绕原点（0,64,0）做圆周运动，角速度1.0弧度/秒
mId = motionComp.AddEntityAroundPointMotion((0, 64, 0), 1.0, (0, 1, 0), True, 0)
motionComp.StartEntityMotion(mId)
```

## 物品栏

通过`GetEngineCompFactory().CreateItem(entityId)`获取`ItemCompServer`或`ItemCompClient`。物品信息以字典（物品信息字典）形式传递。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetEntityItem(slotType,slot,getUserData)` | 服务端/客户端 | `slotType:int`（槽位类型枚举）、`slot:int`（槽位索引）、`getUserData:bool`（是否获取userData，服务端参数） | `dict`或`None` | 获取实体指定槽位的物品信息字典。 |
| `SetEntityItem(slotType,slot,item)` | 服务端 | `slotType:int`、`slot:int`、`item:dict` | `bool` | 设置实体指定槽位的物品。 |
| `SpawnItemToLevel(itemDict,dimensionId,pos)` | 服务端 | `itemDict:dict`、`dimensionId:int`、`pos:tuple(float,float,float)` | `bool` | 在指定位置生成物品掉落物实体。 |

## 状态效果

通过`GetEngineCompFactory().CreateEffect(entityId)`获取`EffectComponentServer`或`EffectComponentClient`。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `AddEffectToEntity(effectName,duration,amplifier,showParticles)` | 服务端 | `effectName:str`、`duration:float`（秒）、`amplifier:int`（0为第一级）、`showParticles:bool` | `bool` | 为实体添加状态效果；若已存在同名效果，按等级/剩余时间规则决定是否覆盖。 |
| `RemoveEffectFromEntity(effectName)` | 服务端 | `effectName:str` | `bool` | 移除实体的指定状态效果。 |
| `GetAllEffects()` | 服务端/客户端 | 无 | `list(dict)`或`None` | 获取实体当前全部状态效果信息列表，字段包含`effectName`、`duration`（int，秒）、`duration_f`（float，秒）、`amplifier`。 |
| `GetEffectOnEntityByName(effectName)` | 服务端/客户端 | `effectName:str` | `dict`或`None` | 获取实体指定名称状态效果的信息字典；不存在时返回`None`。 |

## 维度传送

通过`GetEngineCompFactory().CreateAttr(entityId)`（旧版）或专属维度组件（视版本而定）执行维度传送。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `ChangeEntityDimension(dimensionId,pos)` | 服务端 | `dimensionId:int`、`pos:tuple(float,float,float)` | `bool` | 将实体传送到指定维度的指定坐标，`dimensionId`为0（主世界）、1（下界）、2（末地）或自定义维度ID。 |

## 世界实体管理

以下方法为`ServerSystem`或`ClientSystem`实例方法，不通过组件工厂调用。

| 接口 | 端 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `CreateEngineEntityByTypeStr(engineTypeStr,pos,rot,dimensionId,isNpc,isGlobal)` | 服务端 | `engineTypeStr:str`、`pos:tuple(float,float,float)`、`rot:tuple(float,float)`、`dimensionId:int`、`isNpc:bool`、`isGlobal:bool` | `str`或`None` | 通过类型字符串在指定维度的指定位置生成实体，返回`entityId`。`isNpc`为`True`时生成NPC，`isGlobal`为`True`时实体全局常加载。 |
| `CreateEngineEntityByNBT(nbtDict,pos,rot,dimensionId,isNpc,isGlobal)` | 服务端 | `nbtDict:dict`、`pos:tuple(float,float,float)`、`rot:tuple(float,float)`、`dimensionId:int`、`isNpc:bool`、`isGlobal:bool` | `str`或`None` | 通过NBT字典在指定位置生成实体，可携带完整NBT数据（如自定义名称、装备等）。 |
| `CreateEngineItemEntity(itemDict,dimensionId,pos)` | 服务端 | `itemDict:dict`、`dimensionId:int`、`pos:tuple(float,float,float)` | `str`或`None` | 在指定位置生成物品掉落物实体，返回该物品实体的`entityId`。 |
| `CreateClientEntityByTypeStr(engineTypeStr,pos)` | 客户端 | `engineTypeStr:str`、`pos:tuple(float,float,float)` | `str`或`None` | 创建客户端本地实体（仅当前客户端可见，不同步服务端），返回`entityId`。 |
| `DestroyEntity(entityId)` | 服务端/客户端 | `entityId:str` | `bool` | 销毁指定实体（服务端销毁同步全局；客户端销毁仅移除客户端本地实体或粒子/特效实体）。 |

```python
import mod.server.extraServerApi as serverApi

class MyServerSystem(serverApi.GetServerSystemCls()):
    def SummonZombie(self, pos, dimensionId=0):
        entityId = self.CreateEngineEntityByTypeStr(
            "minecraft:zombie",
            pos,
            (0, 0),   # 俯仰角, 偏航角
            dimensionId,
            False,    # 不是NPC
            False     # 非常加载
        )
        return entityId

    def DropItem(self, itemDict, pos, dimensionId=0):
        return self.CreateEngineItemEntity(itemDict, dimensionId, pos)
```