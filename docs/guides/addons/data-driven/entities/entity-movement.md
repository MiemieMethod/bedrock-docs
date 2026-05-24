# 实体移动

在Minecraft中，实体可以通过步行、游泳或飞行等方式在世界中移动。要让一个自定义实体能够移动，通常需要多个组件协同工作。阅读本文时，请记住你的实体至少需要：

1. **移动速度组件**——控制实体的移动快慢
2. **移动类型组件**——决定实体以哪种方式移动（步行、飞行等）
3. **导航组件**——让实体能够生成寻路路径
4. **AI意向组件**——决定实体何时、朝哪里移动

/// tip | 参考原版行为包
创建会移动的实体的最佳方式，是从原版行为包中找到一个类似的实体，将其组件复制到你的实体中作为起点。例如，幻翼、恶魂和鹦鹉都是飞行实体，但行为差异极大——选择与你目标最接近的那个作为模板。
///

## 移动速度

实体的第一个必要组件是速度组件，控制实体在世界中的移动快慢。

| 组件 | 说明 |
|---|---|
| `minecraft:movement` | 设置基本移动速度（必选） |
| `minecraft:underwater_movement` | 设置在水中的移动速度 |
| `minecraft:flying_speed` | 设置在空中的移动速度 |

`minecraft:movement`几乎是所有会移动实体的必选组件。其他两个按需添加——原版游泳实体（如海豚）会包含`underwater_movement`，部分飞行实体会包含`flying_speed`。

## 移动类型

实体还需要一个移动类型组件，它决定实体在硬编码层面**如何**移动。每个实体只能拥有一个移动类型组件。

| 组件 | 说明 |
|---|---|
| `minecraft:movement.basic` | 基础陆地移动 |
| `minecraft:movement.amphibious` | 两栖移动，可在水中游泳，也可在陆地行走 |
| `minecraft:movement.fly` | 飞行移动 |
| `minecraft:movement.hover` | 悬停移动 |
| `minecraft:movement.generic` | 通用移动，支持飞行、游泳、攀爬等 |
| `minecraft:movement.jump` | 跳跃移动，移动时间隔一定时间跳跃 |
| `minecraft:movement.skip` | 蛙跳式移动 |
| `minecraft:movement.sway` | 摇摆移动，给人游泳的感觉 |

一般来说，`basic`、`amphibious`和`fly`是最常用的三种。

## 移动修饰

以下组件不是必须的，但在特殊场合很有用：

| 组件 | 说明 |
|---|---|
| `minecraft:water_movement` | 设置实体在水中受到的摩擦力 |
| `minecraft:rail_movement` | 让实体只能在铁轨上移动 |
| `minecraft:friction_modifier` | 设置实体在陆地上受到的摩擦力 |

## 导航

导航组件告诉实体它**能够**走哪些路——能否穿越水域、能否爬墙、能否避开阳光等。组件的各个字段的配置往往比选择哪个组件更重要！

每个实体在同一时间只能有一个导航组件。

| 组件 | 说明 |
|---|---|
| `minecraft:navigation.walk` | 标准步行导航，可上下跳一格 |
| `minecraft:navigation.climb` | 支持攀爬竖直墙壁，如蜘蛛 |
| `minecraft:navigation.swim` | 包含水路的导航 |
| `minecraft:navigation.fly` | 飞行导航，类似鹦鹉 |
| `minecraft:navigation.float` | 在空中漂浮的导航，类似恶魂 |
| `minecraft:navigation.generic` | 通用导航，支持步行、游泳、飞行和攀爬 |

/// tip | 参考原版配置
导航组件的字段配置非常重要，强烈建议参考原版实体的导航组件来了解不同字段和值的用法。
///

## 导航能力扩展

除了导航组件本身，还有一些组件可以扩展实体的导航能力：

| 组件 | 说明 |
|---|---|
| `minecraft:can_climb` | 允许实体爬梯子 |
| `minecraft:can_fly` | 标记实体为飞行实体，寻路时不要求脚下有方块 |
| `minecraft:can_power_jump` | 允许实体像马一样蓄力跳跃 |
| `minecraft:floats_in_liquid` | 允许实体浮在液体方块上 |
| `minecraft:annotation.break_door` | 允许实体破门（还需在导航组件中开启此选项） |
| `minecraft:annotation.open_door` | 允许实体开门（同上） |
| `minecraft:jump.static` | 赋予实体跳跃能力 |
| `minecraft:jump.dynamic` | 动态跳跃，跳跃属性随速度修饰变化 |
| `minecraft:preferred_path` | 基于方块设置路径代价，影响实体的寻路偏好 |

## AI意向

导航组件告诉实体**如何**生成路径，但不决定**何时**或**朝哪里**生成路径。这是AI意向组件的职责。

AI意向的标识符以`behavior`开头，遵循优先级系统——**数值越小优先级越高**，优先级最高的意向会被优先执行。

通常你需要添加多个不同优先级的AI意向，它们组合在一起就能创造出真实自然的实体行为。以下是几个常用的移动类AI意向示例：

| 组件 | 说明 |
|---|---|
| `minecraft:behavior.random_stroll` | 随机游荡 |
| `minecraft:behavior.follow_owner` | 跟随主人 |
| `minecraft:behavior.move_to_water` | 移动到水边 |
| `minecraft:behavior.stroll_towards_village` | 朝村庄方向漫步 |

AI意向的完整列表可参阅官方实体组件参考。

## 指定目标寻路

在地图制作和附加包中，让实体前往指定地点是一个非常常见的需求。最可靠的方式是使用一个辅助实体作为路标——我们称之为**路标实体**。关于如何创建路标实体，可参考[虚拟实体](dummy-entities.md)教程。

### 原理

让实体对路标实体保持攻击意向，再将路标放到目标位置，实体就会自动寻路前往。

### 组件配置

以下配置让实体将`waypoint_1`族的实体视为攻击目标，并向其寻路。记得同时为实体添加移动和导航组件。

```json title="BP/entities/my_entity.json（components节选）"
"minecraft:behavior.nearest_attackable_target": {
    "priority": 0,
    "reselect_targets": true,
    "target_search_height": 1000,
    "within_radius": 1000,
    "must_see": false,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "waypoint_1"
            },
            "max_dist": 1000
        }
    ]
},
"minecraft:attack": {
    "damage": 0
},
"minecraft:behavior.melee_attack": {
    "priority": 0,
    "require_complete_path": true,
    "track_target": true
},
"minecraft:follow_range": {
    "value": 1000,
    "max": 1000
}
```

### 检测是否到达路标

使用`minecraft:target_nearby_sensor`可以检测实体是否已到达路标附近：

```json title="BP/entities/my_entity.json（components节选）"
"minecraft:target_nearby_sensor": {
    "inside_range": 2.0,
    "outside_range": 4.0,
    "must_see": true,
    "on_inside_range": {
        "event": "wiki:reached_waypoint"
    },
    "on_outside_range": {
        "event": "wiki:left_waypoint"
    }
}
```

## 其他技巧

通过命令触发实体的步行动画，同时控制实体移动方向：

```
/execute as @e[type=wiki:my_entity] at @s run tp @s ^^^0.1
```

这种方法可以让你精确控制实体的移动路线，同时使其看起来像在自然行走。