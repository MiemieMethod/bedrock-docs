---
title: 投射物
category: 文档
mentions:
    - SirLich
    - stirante
    - retr0cube
    - SmokeyStack
    - Luthorius
    - ThomasOrs
description: 投射物组件文档。
---

## 概述

本页旨在记录`minecraft:projectile`实体行为组件中可使用的所有不同字段。

:::warning
_免责声明：本组件主要基于游戏中发现的投射物或通过逆向工程游戏进行文档记录。_
_此信息最后测试于 **1.18.2** 版本。_
:::

| 名称                       | 类型                 | 默认值        | 描述                                                                                                                                       |
|----------------------------|----------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| anchor                     | Integer              |               |                                                                                                                                            |
| angle_offset               | Decimal              | 0             | 决定投射物抛出时的角度                                                                                                                        |
| catch_fire                 | Boolean              | false         | 如果为 true，命中的实体将被点燃                                                                                                                |
| crit_particle_on_hurt      | Boolean              | false         | 如果为 true，投射物在命中时会产生暴击粒子效果                                                                                                   |
| destroy_on_hurt            | Boolean              | false         | 如果为 true，此实体在被命中时将被销毁                                                                                                           |
| filter                     | String               |               | 此处定义的实体定义将无法被投射物伤害                                                                                                           |
| fire_affected_by_griefing  | Boolean              | false         | 如果为 true，投射物是否导致的火焰受 mob griefing 游戏规则的影响                                                                             |
| gravity                    | Decimal              | 0.05          | 抛出时施加于该实体的重力。值越大，实体下落速度越快                                                                                              |
| hit_ground_sound           | String               |               | 投射物碰到地面时播放的声音                                                                                                                    |
| hit_sound                  | String               |               | 投射物命中实体时播放的声音                                                                                                                    |
| homing                     | Boolean              | false         | 如果为 true，投射物会朝最近的实体自动追踪。**在 1.18.2 版本中不起作用**                                                                         |
| inertia                    | Decimal              | 0.99          | 投射物在空中飞行时每帧保持的速度比例                                                                                                           |
| is_dangerous               | Boolean              | false         | 如果为 true，投射物将被视为对玩家危险的                                                                                                         |
| knockback                  | Boolean              | true          | 如果为 true，投射物将对命中的实体造成击退效果                                                                                                   |
| lightning                  | Boolean              | false         | 如果为 true，命中的实体将被雷电击中                                                                                                             |
| liquid_inertia             | Decimal              | 0.6           | 投射物在水中飞行时每帧保持的速度比例                                                                                                           |
| multiple_targets           | Boolean              | true          | 如果为 true，投射物在一次飞行中可以命中多个实体                                                                                                   |
| offset                     | Vector [a, b, c]     | [0, 0.5, 0]   | 投射物生成时相对于实体锚点的偏移量                                                                                                             |
| on_fire_time               | Decimal              | 5             | 被命中的实体将处于燃烧状态的时间（秒）                                                                                                         |
| on_hit                     | Object               |               | 投射物命中时的行为。更多信息见 [下面](#on_hit)                                                                                                |
| particle                   | String               | iconcrack     | 碰撞时使用的粒子                                                                                                                              |
| potion_effect              | Integer              | -1            | 定义箭矢命中实体时将应用的效果                                                                                                                  |
| power                      | Decimal              | 1.3           | 决定投射物的速度                                                                                                                              |
| reflect_on_hurt            | Boolean              | false         | 如果为 true，该实体在被命中时将被反射                                                                                                         |
| semi_random_diff_damage    | Boolean              | false         | 如果为 true，伤害将根据伤害和速度进行随机化                                                                                                     |
| shoot_sound                | String               |               | 投射物被发射时播放的声音                                                                                                                      |
| shoot_target               | Boolean              | true          | 如果为 true，投射物将朝发射实体的目标发射                                                                                                      |
| should_bounce              | Boolean              | false         | 如果为 true，投射物在命中时会弹跳                                                                                                              |
| splash_potion              | Boolean              | false         | 如果为 true，投射物将被视为抛射药水                                                                                                            |
| splash_range               | Decimal              | 4             | '溅射'效果的半径（区块数）                                                                                                                       |
| stop_on_hurt               | Boolean              |               |                                                                                                                                            |
| uncertainty_base           | Decimal              | 0             | 基础精确度。精确度由公式 uncertaintyBase - difficultyLevel \* uncertaintyMultiplier 决定                                                        |
| uncertainty_multiplier     | Decimal              | 0             | 决定难度如何影响精确度。精确度由公式 uncertaintyBase - difficultyLevel \* uncertaintyMultiplier 决定                                              |
| hit_water                  | Boolean              | false         | 如果为 true，液体区块将被视为固体。**需要启用“教育版”开关**                                                                                      |

## on_hit

此对象包含投射物命中某物时可以执行的所有行为。

### arrow_effect

_具体行为未知_

### teleport_owner

将射手传送到命中位置。

### catch_fire

_具体行为未知_

将目标点燃

### ignite

_具体行为未知_

将目标点燃

### remove_on_hit

投射物在命中时被移除。

### douse_fire

_具体行为未知_

### impact_damage

在命中时造成伤害。

| 名称                          | 类型                             | 描述                                                                                                                           |
|-------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| damage                        | Integer/Integer Array [min, max] | 命中时对实体造成的伤害                                                                                                        |
| semi_random_diff_damage       | Boolean                          |                                                                                                                                 |
| max_critical_damage           | Decimal                          |                                                                                                                                 |
| min_critical_damage           | Decimal                          |                                                                                                                                 |
| power_multiplier              | Decimal                          |                                                                                                                                 |
| channeling                    | Boolean                          |                                                                                                                                 |
| set_last_hurt_requires_damage | Boolean                          |                                                                                                                                 |
| destroy_on_hit_requires_damage| Boolean                          |                                                                                                                                 |
| filter                        | String                           | 影响的实体。比其他地方使用的过滤器更基础，因为它不能 "测试" 除标识符之外的任何东西                                                                 |
| destroy_on_hit                | Boolean                          |                                                                                                                                 |
| knockback                     | Boolean                          |                                                                                                                                 |
| catch_fire                    | Boolean                          | 决定目标是否会被火焰吞没                                                                                                      |

### definition_event

在命中时调用一个事件。

| 名称               | 类型    | 描述                                         |
|--------------------|---------|----------------------------------------------|
| affect_projectile  | Boolean | 事件将针对投射物实体触发                      |
| affect_shooter     | Boolean | 事件将针对射手实体触发                        |
| affect_target      | Boolean | 事件将针对被击中的实体触发                    |
| affect_splash_area | Boolean | 事件将针对区域内的所有实体触发                |
| splash_area        | Decimal | 实体区域                                      |
| event_trigger      | Object  | 要触发的事件。结构见下文。                     |

| 名称   | 类型   | 描述                                     |
|--------|--------|------------------------------------------|
| event  | String | 要触发的事件                            |
| target | String | 事件的目标                                |
| filters| Object | 触发事件所需的条件                         |

### stick_in_ground

将投射物固定在地面上。

| 名称        | 类型    | 描述    |
|-------------|---------|---------|
| shake_time  | Decimal |         |

### spawn_aoe_cloud

生成一个具有药水效果的范围效果云。

| 名称                | 类型                    | 描述                                                                                                                                                                      |
|---------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| radius              | Decimal                 | 云的半径                                                                                                                                                                  |
| radius_on_use       | Decimal                 |                                                                                                                                                                          |
| potion              | Integer                 | 持续药水 ID                                                                                                                                                              |
| particle            | String                  | [原版粒子](../particles/vanilla-particles.md) 云的发射器。只接受原版粒子。**dragonbreath** 允许使用瓶子获得龙息                                                                  |
| duration            | Integer                 | 云的持续时间（秒）                                                                                                                                                         |
| color               | Integer array [r, g, b] | 粒子的颜色                                                                                                                                                                 |
| affect_owner        | Boolean                 | 药水效果是否影响射手。不适用于玩家                                                                                                                                         |
| reapplication_delay | Integer                 | 药水效果应用之间的延迟（tick）                                                                                                                                             |

#### 药水 ID

| 药水                      | 常规 | 扩展 | 增强（II级） |
|---------------------------|-----|------|---------------|
| Water Bottle              | 0   |      |               |
| Mundane Potion            | 1   | 2    |               |
| Thick Potion              | 3   |      |               |
| Awkward Potion            | 4   |      |               |
| Potion of Night Vision    | 5   | 6    |               |
| Potion of Invisibility    | 7   | 8    |               |
| Potion of Leaping         | 9   | 10   | 11            |
| Potion of Fire Resistance | 12  | 13   |               |
| Potion of Swiftness       | 14  | 15   | 16            |
| Potion of Slowness        | 17  | 18   |               |
| Potion of Water Breathing | 19  | 20   |               |
| Potion of Healing         | 21  |      | 22            |
| Potion of Harming         | 23  |      | 24            |
| Potion of Poison          | 25  | 26   | 27            |
| Potion of Regeneration    | 28  | 29   | 30            |
| Potion of Strength        | 31  | 32   | 33            |
| Potion of Weakness        | 34  | 35   |               |
| Potion of Decay           | 36  |      |               |
| Potion of Turtle Master   | 37  | 38   | 39            |
| Potion of Slow Falling    | 40  | 41   |               |
| Potion of Slowness IV     | 42  |      |               |
| Potion of Crashing        | 43+ |      |               |

### spawn_chance

在命中时生成一个实体。

| 名称                        | 类型    | 描述                                 |
|-----------------------------|---------|--------------------------------------|
| first_spawn_percent_chance  | Decimal |                                      |
| second_spawn_percent_chance | Decimal |                                      |
| first_spawn_count           | Integer |                                      |
| second_spawn_count          | Integer |                                      |
| spawn_definition            | String  | 要生成的实体的 ID                     |
| spawn_baby                  | Boolean | 生成的实体是否为幼体                 |

### particle_on_hit

在命中时生成粒子。

| 名称          | 类型    | 描述                                              |
|---------------|---------|---------------------------------------------------|
| particle_type | String  | 要使用的 [原版粒子](../particles/vanilla-particles.md) |
| num_particles | Integer | 粒子数量                                          |
| on_entity_hit | Boolean | 是否应在实体命中时生成粒子                      |
| on_other_hit  | Boolean | 是否应在其他命中时生成粒子                      |


### mob_effect

为目标应用一个生物效果。

| 名称            | 类型    | 描述                                 |
|-----------------|---------|--------------------------------------|
| effect          | String  | 效果                                 |
| duration        | Integer | 效果持续时间                         |
| durationeasy    | Integer | 简单难度下的效果持续时间             |
| durationnormal  | Integer | 普通难度下的效果持续时间             |
| durationhard    | Integer | 困难难度下的效果持续时间             |
| amplifier       | Integer | 效果增强级数                           |
| ambient         | Boolean |                                      |
| visible         | Boolean |                                      |

### grant_xp

尽管名称如此，这实际上会生成一定数量的经验球，价值为指定数量。

| 名称  | 类型    | 描述                                                                                      |
|-------|---------|-----------------------------------------------------------------------------------------|
| minXP | Integer | 要给予的最小经验值                                                                         |
| maxXP | Integer | 要给予的最大经验值                                                                         |
| xp    | Integer | 要给予的固定经验值。当设置时，将使用此值代替 min 和 max 值。                               |

### freeze_on_hit

_具体行为未知_

_需要启用 Education Edition 开关。_
在命中时冻结水。

| 名称          | 类型    | 描述                   |
|---------------|---------|-----------------------|
| shape         | String  | "sphere" 或 "cube"     |
| snap_to_block | Boolean |                       |
| size          | Integer | 冻结效果的大小         |

### hurt_owner

_具体行为未知。目前会导致 Minecraft 崩溃，可能是因为参数错误。_

| 名称          | 类型    | 描述 |
|---------------|---------|------|
| owner_damage  | Integer |      |
| knockback     | Boolean |      |
| ignite        | Boolean |      |

### thrown_potion_effect

_具体行为未知。目前会导致 Minecraft 崩溃，可能是因为它只对抛射药水有效。_

## 附加信息
在创建自定义投射物（例如箭矢或三叉戟变体，或完全自定义的投射物）时，您可能需要考虑定义一个 [runtime identifier](../entities/runtime-identifier.md)，以确保其按预期运作。如果不这样做，可能会导致不期望的行为，从奇怪的视觉效果到不正确的击退方向，以及用徒手就能杀死的箭矢。