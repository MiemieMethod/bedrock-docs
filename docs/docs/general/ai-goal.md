# AI意向

**AI意向（AI Goal）**是Minecraft基岩版中驱动生物实体自主行为的系统。每个AI意向定义了生物在满足特定条件时应执行的一种行为模式，多个AI意向基于优先级共同构成生物的行为决策逻辑。

## 概述

基岩版的生物AI基于优先级驱动的意向系统。每个生物实体可以拥有多个AI意向组件，每个组件对应一种行为（如行走、攻击、进食、逃跑等），并被分配一个**优先级（Priority）**值。优先级值越小，该行为的优先级越高。

在每个游戏刻中，引擎会评估所有可执行的AI意向，选择满足条件且优先级最高的行为来执行。当更高优先级的行为条件满足时，低优先级的行为会被中断。

## 行为组件

AI意向通过行为包中实体定义文件的组件来配置。行为组件的标识符通常以`minecraft:behavior.`为前缀，每个组件代表一种AI意向。

### 常见行为组件

以下按功能分类列举部分重要的AI意向组件：

#### 移动行为

| 组件 | 功能 |
|------|------|
| `minecraft:behavior.random_stroll` | 随机漫步 |
| `minecraft:behavior.float` | 在水中上浮 |
| `minecraft:behavior.look_at_player` | 注视玩家 |
| `minecraft:behavior.random_look_around` | 随机环顾 |
| `minecraft:behavior.move_to_water` | 移向水源 |
| `minecraft:behavior.move_to_land` | 移向陆地 |
| `minecraft:behavior.go_home` | 返回家中 |
| `minecraft:behavior.follow_parent` | 跟随父母 |

#### 攻击行为

| 组件 | 功能 |
|------|------|
| `minecraft:behavior.melee_attack` | 近战攻击 |
| `minecraft:behavior.ranged_attack` | 远程攻击 |
| `minecraft:behavior.hurt_by_target` | 反击伤害来源 |
| `minecraft:behavior.nearest_attackable_target` | 寻找最近的可攻击目标 |

#### 交互行为

| 组件 | 功能 |
|------|------|
| `minecraft:behavior.breed` | 繁殖 |
| `minecraft:behavior.tempt` | 被食物引诱 |
| `minecraft:behavior.beg` | 乞食 |
| `minecraft:behavior.trade_with_player` | 与玩家交易 |

#### 特殊行为

| 组件 | 功能 |
|------|------|
| `minecraft:behavior.panic` | 受伤后惊慌逃跑 |
| `minecraft:behavior.flee_sun` | 逃离阳光 |
| `minecraft:behavior.avoid_mob_type` | 回避特定类型的生物 |
| `minecraft:behavior.door_interact` | 开关门 |
| `minecraft:behavior.sleep` | 在床上睡觉 |

## 优先级

每个行为组件的`priority`字段决定了其执行优先级。一般来说，生存相关的行为（如逃跑、攻击）设置为较小的数值（高优先级），而休闲行为（如随机漫步、环顾）设置为较大的数值（低优先级）。

```json title="优先级示例"
{
  "minecraft:behavior.panic": { "priority": 1, "speed_multiplier": 1.25 },
  "minecraft:behavior.breed": { "priority": 3, "speed_multiplier": 1.0 },
  "minecraft:behavior.random_stroll": { "priority": 6, "speed_multiplier": 0.8 },
  "minecraft:behavior.look_at_player": { "priority": 7 }
}
```

## 导航

AI意向在执行移动相关行为时依赖**导航（Navigation）**组件来规划路径。不同类型的导航组件适用于不同的运动方式：

- `minecraft:navigation.walk`：步行导航，适用于陆地生物。
- `minecraft:navigation.fly`：飞行导航，适用于飞行生物。
- `minecraft:navigation.swim`：游泳导航，适用于水生生物。
- `minecraft:navigation.float`：漂浮导航，适用于在水面漂浮的生物。
- `minecraft:navigation.climb`：攀爬导航，适用于可以攀爬的生物。
- `minecraft:navigation.hover`：悬浮导航，适用于悬浮在空中的生物。

导航组件控制着寻路的细节参数，如是否可以开门、是否可以穿越水面、是否可以破坏方块等。