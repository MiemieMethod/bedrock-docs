---
title: 实体移动
category: 教程
mentions:
    - SirLich
    - sermah
    - MedicalJewel105
    - TheDoctor15
description: 学习如何制作一个合适的实体移动行为。
---

在Minecraft中，实体能够通过行走、游泳或飞行在世界中移动。为了实现这些行为，你的实体通常需要相当多的行为组件，分解为各种类型。

在阅读本教程时，请记住你的实体至少需要：

-   [设置实体移动速度的组件。](#movement-speed)
-   [设置实体移动方式（行走、飞行等）的组件。](#movement-type)
-   [设置实体导航能力，以便其能生成路径的组件。](#navigation-abilities)
-   [设置实体何时/在哪里移动（AI目标）的组件。](#ai)

:::tip
创建一个移动实体的最佳方式是从原版行为包中选择一个相似的实体，并将其组件复制到你的实体中。

例如，幻翼骷髅（Phantom）、喷火骷髅（Ghast）或鹦鹉（Parrot）都是飞行实体，但它们的游戏内行为非常不同！使用最接近的实体作为模板。
:::

## 移动速度

你的实体首先需要一个速度组件。这个组件设置了实体在世界中移动的速度。

| 组件名称                                                                                  | 备注                                 |
|-----------------------------------------------------------------------------------------|--------------------------------------|
| [minecraft:movement](../entities/vanilla-usage-components.md#movement)                       | 设置移动速度（必需）                 |
| [minecraft:underwater_movement](../entities/vanilla-usage-components.md#underwater-movement) | 设置水中的移动速度。                 |
| [minecraft:flying_speed](../entities/vanilla-usage-components.md#flying-speed)               | 设置空中的速度。                     |

你应该始终包含 `minecraft:movement`。根据需要添加其他两个组件。

所有原版“游泳”实体如海豚（Dolphin）都包含 `underwater_movement`。只有一些飞行实体拥有 `flying_speed`。尚不清楚原因。

## 移动类型

你的实体还需要一个移动类型。移动类型为实体如何在世界中移动设置硬编码的行为。

你的实体中只能包含一种移动类型。选择最符合你需求的组件。通常使用 `basic`、`amphibious` 和 `fly` 是不错的选择。

| 组件名称                                                                                                 | 备注                                                                                             |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [minecraft:movement.amphibious](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.amphibious) | 此移动控制允许实体在水中游泳并在陆地上行走。                                                   |
| [minecraft:movement.basic](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.basic)           | 此组件增强了实体的移动。                                                                         |
| [minecraft:movement.fly](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.fly)               | 此移动控制使实体能够飞行。                                                                       |
| [minecraft:movement.generic](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.generic)       | 此移动控制允许实体飞行、游泳、攀爬等。                                                           |
| [minecraft:movement.hover](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.hover)           | 此移动控制使实体能够悬停。                                                                       |
| [minecraft:movement.jump](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.jump)             | 移动控制使实体在移动时以指定的延迟跳跃。                                                         |
| [minecraft:movement.skip](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.skip)             | 此移动控制使实体在移动时跳跃。                                                                     |
| [minecraft:movement.sway](https://bedrock.dev/docs/stable/Entities#minecraft%3Amovement.sway)             | 此移动控制使实体左右摇摆，给人一种在游泳的印象。                                                   |

## 移动修改器

移动修改器提供了关于实体如何在世界中移动的额外信息。这些组件对于普通实体不是必需的，但你应该了解它们。

| 组件名称                                                                                             | 备注                                             |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [minecraft:water_movement](https://bedrock.dev/docs/stable/Entities#minecraft%3Awater_movement)       | 设置实体在水中遇到的摩擦力。                       |
| [minecraft:rail_movement](https://bedrock.dev/docs/stable/Entities#minecraft%3Arail_movement)         | 设置实体可以在轨道上移动（仅限）。                 |
| [minecraft:friction_modifier](https://bedrock.dev/docs/stable/Entities#minecraft%3Afriction_modifier) | 设置实体在陆地上遇到的摩擦力。                     |

## 导航

接下来，实体需要一个导航组件。导航组件有很多字段，比如实体是否可以开门或躲避阳光。如何设置这些字段通常比选择哪个导航组件更重要！

导航组件之所以有这么多，是因为每个组件都提供了略微不同的硬编码行为。选择名字/描述最符合你实体导航需求的导航组件。

任何时候只能有一个导航组件。

:::tip
此组件非常重要。你应该查看原版示例，以获取使用哪些字段和数值的灵感。
:::

| 组件名称                                                                                               | 备注                                                                                                                    |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| [minecraft:navigation.climb](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.climb)     | 允许实体生成包括垂直墙壁在内的路径，如原版蜘蛛。                                                                    |
| [minecraft:navigation.float](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.float)     | 允许实体通过在空中飞行生成路径，如普通喷火骷髅。                                                                    |
| [minecraft:navigation.generic](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.generic) | 允许实体通过步行、游泳、飞行和攀爬，以及上下跳跃来生成路径。                                                           |
| [minecraft:navigation.fly](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.fly)         | 允许实体在空中生成路径，如原版鹦鹉。                                                                                  |
| [minecraft:navigation.swim](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.swim)       | 允许实体生成包含水域的路径。                                                                                            |
| [minecraft:navigation.walk](https://bedrock.dev/docs/stable/Entities#minecraft%3Anavigation.walk)       | 允许实体通过步行和上下跳跃生成路径，如普通怪物。                                                                        |

## 导航能力

除了移动和导航组件外，还有许多附加组件来增强实体在世界中的移动能力。

| 组件名称                                                                                                     | 备注                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [minecraft:annotation.break_door](https://bedrock.dev/docs/stable/Entities#minecraft%3Aannotation.break_door) | 允许实体破坏门。导航组件中也必须启用此功能。                                                                                |
| [minecraft:annotation.open_door](https://bedrock.dev/docs/stable/Entities#minecraft%3Aannotation.open_door)   | 允许实体开门。导航组件中也必须启用此功能。                                                                                   |
| [minecraft:buoyant](https://bedrock.dev/docs/stable/Entities#minecraft%3Abuoyant)                             | 指定实体可以漂浮的液体。                                                                                                        |
| [minecraft:can_climb](https://bedrock.dev/docs/stable/Entities#minecraft%3Acan_climb)                         | 允许实体攀爬梯子。                                                                                                              |
| [minecraft:can_fly](https://bedrock.dev/docs/stable/Entities#minecraft%3Acan_fly)                             | 标记实体为可以飞行。寻路器不会限于需要有实体下方的固体块的路径。                                                             |
| [minecraft:can_power_jump](https://bedrock.dev/docs/stable/Entities#minecraft%3Acan_power_jump)               | 允许实体像原版马一样进行动力跳跃。                                                                                              |
| [minecraft:floats_in_liquid](https://bedrock.dev/docs/stable/Entities#minecraft%3Afloats_in_liquid)           | 设置实体可以在液体方块中漂浮。                                                                                                  |
| [minecraft:jump.dynamic](https://bedrock.dev/docs/stable/Entities#minecraft%3Ajump.dynamic)                   | 定义动态类型的跳跃控制，根据实体的速度修改器改变跳跃属性。                                                                    |
| [minecraft:jump.static](https://bedrock.dev/docs/stable/Entities#minecraft%3Ajump.static)                     | 赋予实体跳跃的能力。                                                                                                            |

还有像 `minecraft:preferred_path` 这样的组件，会根据基于方块的路径成本来修改导航。

## AI 目标

导航组件告诉实体如何生成路径，但它并未说明何时或在哪里生成路径。这就是AI组件的作用。

AI目标以 `behavior` 为前缀，并遵循优先级系统来选择运行哪个行为。较低的优先级会优先被选中。

通常，你应该添加相当多的AI组件，具有不同的优先级。层叠在一起，这些将为你的实体创造出逼真的移动和行为。和往常一样，原版实体提供了一个很好的模板，说明应添加哪些组件，以及使用哪些属性/优先级。

生成路径的AI组件太多，无法在本文档中一一列出。以下是一些示例：

| 组件名称                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|
| [minecraft:behavior.random_stroll](https://bedrock.dev/docs/stable/Entities#minecraft%3Abehavior.random_stroll)                   |
| [minecraft:behavior.follow_owner](https://bedrock.dev/docs/stable/Entities#minecraft%3Abehavior.follow_owner)                     |
| [minecraft:behavior.move_to_water](https://bedrock.dev/docs/stable/Entities#minecraft%3Abehavior.move_to_water)                   |
| [minecraft:behavior.stroll_towards_village](https://bedrock.dev/docs/stable/Entities#minecraft%3Abehavior.stroll_towards_village) |

欲获取完整列表，请访问 [bedrock.dev](https://bedrock.dev/docs/stable/Entities#AI%20Goals)。

### 路径查找

让实体前往特定地点是市场内容中最常见的需求之一。
实现路径查找的最佳方式是使用第二个实体，第一个实体会被其吸引。我将这个次要实体称为 **标记**。如果你不清楚如何创建标记，请访问 [虚拟实体](../entities/dummy-entities.md) 页面。

#### 思路

我们将要实现的路径查找方法其实相当简单：让我们的实体对标记实体具有攻击性，然后简单地将标记实体放置在我们希望实体前往的位置。困难之处在于知道要添加哪些组件以实现非常远程的路径查找。

#### 组件

这些组件可以根据需要进行编辑，以创建良好的路径查找。确保将 `nearest_attackable_target` 指向你的标记实体。这需要一个 `family_type`，所以你应该在标记上设置一个。

别忘了添加一些基本的移动和导航组件，以便你的实体能够移动。

<CodeHeader></CodeHeader>

```json
"minecraft:behavior.nearest_attackable_target": {
    "priority": 0,
    "reselect_targets": true,
    "target_search_height": 1000,
    "within_radius": 1000,
    "must_see": false,
    "entity_types": [
        {
            "filters": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "waypoint_1"
                }
            ],
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

#### 检测到达标记点

你可以使用 `minecraft:target_nearby_sensor` 来检测何时到达标记实体：

<CodeHeader></CodeHeader>

```json
"minecraft:target_nearby_sensor": {
    "inside_range": 2.0,
    "outside_range": 4.0,
    "must_see": true,
    "on_inside_range": {
        "event": "reached_waypoint"
    },
    "on_outside_range": {
        "event": "not_reached_waypoint"
    }
}
```

## 其他

:::tip
你可以通过命令触发实体的行走动画。
`/execute as @e[type=...] at @s run tp @s ^^^0.1`
这种方式你可以控制实体的移动方向，使其看起来自然。
:::