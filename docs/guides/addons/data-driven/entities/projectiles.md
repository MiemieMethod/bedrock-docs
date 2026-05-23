# 弹射物

本文介绍`minecraft:projectile`行为包组件的全部字段，以及如何制作自定义弹射物实体。

/// warning | 注意
此组件的文档大部分来自对原版实体的反向工程分析，请以实际测试结果为准。
///

## 顶层字段

| 字段 | 类型 | 默认值 | 说明 |
|---|---|---|---|
| `anchor` | Integer | — | 锚点 |
| `angle_offset` | Decimal | 0 | 投掷角度偏移量 |
| `catch_fire` | Boolean | false | 命中时点燃被击中实体 |
| `crit_particle_on_hurt` | Boolean | false | 命中时产生暴击粒子 |
| `destroy_on_hurt` | Boolean | false | 被击中时销毁此弹射物 |
| `filter` | String | — | 该标识符的实体不会被此弹射物伤害 |
| `fire_affected_by_griefing` | Boolean | false | 火焰效果是否受生物破坏游戏规则影响 |
| `gravity` | Decimal | 0.05 | 下落重力，值越大下落越快 |
| `hit_ground_sound` | String | — | 命中地面时播放的音效 |
| `hit_sound` | String | — | 命中实体时播放的音效 |
| `homing` | Boolean | false | 是否追踪最近的目标 |
| `inertia` | Decimal | 0.99 | 每帧在空中保留的速度比例（1=无空气阻力） |
| `is_dangerous` | Boolean | false | 是否对玩家视为危险 |
| `knockback` | Boolean | true | 命中时是否击退实体 |
| `lightning` | Boolean | false | 命中时是否召唤闪电 |
| `liquid_inertia` | Decimal | 0.6 | 每帧在水中保留的速度比例 |
| `multiple_targets` | Boolean | true | 是否可以在一次飞行中命中多个实体 |
| `offset` | Vector | [0, 0.5, 0] | 相对实体锚点的生成偏移量 |
| `on_fire_time` | Decimal | 5 | 点燃目标的持续时间（秒） |
| `on_hit` | Object | — | 命中时的行为，见下文 |
| `particle` | String | iconcrack | 碰撞时产生的粒子 |
| `potion_effect` | Integer | -1 | 箭矢附带的状态效果ID（-1为无） |
| `power` | Decimal | 1.3 | 发射速度 |
| `reflect_on_hurt` | Boolean | false | 被击中时反弹 |
| `semi_random_diff_damage` | Boolean | false | 基于伤害和速度随机化伤害值 |
| `shoot_sound` | String | — | 发射时播放的音效 |
| `shoot_target` | Boolean | true | 是否朝发射者的目标方向射出 |
| `should_bounce` | Boolean | false | 命中时是否弹跳 |
| `splash_potion` | Boolean | false | 是否视为喷溅药水 |
| `splash_range` | Decimal | 4 | 喷溅效果半径（格） |
| `uncertainty_base` | Decimal | 0 | 基础精度。精度公式：`uncertaintyBase - difficultyLevel × uncertaintyMultiplier` |
| `uncertainty_multiplier` | Decimal | 0 | 难度对精度的影响系数 |
| `hit_water` | Boolean | false | 液体是否被视为固体<!-- md:flag edu --> |

## on_hit 行为

`on_hit`对象定义了弹射物命中时触发的一个或多个行为：

### arrow_effect

赋予目标箭矢效果（具体行为待明确）。

### teleport_owner

将发射者传送到命中位置。

### catch_fire

点燃目标（具体行为待明确）。

### ignite

点燃目标（具体行为待明确）。

### remove_on_hit

命中任何物体后销毁弹射物。

### douse_fire

熄灭目标身上的火焰（具体行为待明确）。

### impact_damage

命中时对目标造成伤害：

| 字段 | 类型 | 说明 |
|---|---|---|
| `damage` | Integer 或 [min, max] | 伤害值，可以是固定值或范围 |
| `knockback` | Boolean | 是否击退 |
| `catch_fire` | Boolean | 是否点燃目标 |
| `max_critical_damage` | Decimal | 最大暴击伤害 |
| `min_critical_damage` | Decimal | 最小暴击伤害 |
| `power_multiplier` | Decimal | 速度对伤害的乘数 |
| `semi_random_diff_damage` | Boolean | 基于伤害和速度随机化伤害值 |
| `channeling` | Boolean | 召唤闪电 |
| `filter` | String | 仅影响指定标识符的实体 |
| `destroy_on_hit` | Boolean | 命中后销毁弹射物 |

### definition_event

命中时触发指定事件：

| 字段 | 类型 | 说明 |
|---|---|---|
| `affect_projectile` | Boolean | 对弹射物本身触发事件 |
| `affect_shooter` | Boolean | 对发射者触发事件 |
| `affect_target` | Boolean | 对被命中实体触发事件 |
| `affect_splash_area` | Boolean | 对区域内所有实体触发事件 |
| `splash_area` | Decimal | 区域半径 |
| `event_trigger` | Object | 事件对象（含`event`、`target`、`filters`字段） |

### stick_in_ground

命中后插入地面：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shake_time` | Decimal | 插入后的震动时间 |

### spawn_aoe_cloud

命中后生成区域效果云：

| 字段 | 类型 | 说明 |
|---|---|---|
| `radius` | Decimal | 云的半径 |
| `radius_on_use` | Decimal | 每次施加效果后半径变化量 |
| `potion` | Integer | 药水效果ID（见下方药水ID表） |
| `particle` | String | 粒子发射器名称；`"dragonbreath"`允许玻璃瓶收集 |
| `duration` | Integer | 云存在时间（秒） |
| `color` | [r, g, b] | 粒子颜色 |
| `affect_owner` | Boolean | 是否对发射者施加效果 |
| `reapplication_delay` | Integer | 效果再次施加的间隔（刻） |

#### 药水ID表

| 药水 | 普通 | 延长 | 增强（II级） |
|---|---|---|---|
| 水瓶 | 0 | — | — |
| 粗制药水 | 1 | 2 | — |
| 浑浊药水 | 3 | — | — |
| 奇怪药水 | 4 | — | — |
| 夜视药水 | 5 | 6 | — |
| 隐身药水 | 7 | 8 | — |
| 跳跃药水 | 9 | 10 | 11 |
| 防火药水 | 12 | 13 | — |
| 迅捷药水 | 14 | 15 | 16 |
| 迟缓药水 | 17 | 18 | — |
| 水下呼吸药水 | 19 | 20 | — |
| 治疗药水 | 21 | — | 22 |
| 伤害药水 | 23 | — | 24 |
| 剧毒药水 | 25 | 26 | 27 |
| 再生药水 | 28 | 29 | 30 |
| 力量药水 | 31 | 32 | 33 |
| 虚弱药水 | 34 | 35 | — |
| 衰变药水 | 36 | — | — |
| 神龟药水 | 37 | 38 | 39 |
| 缓降药水 | 40 | 41 | — |
| 迟缓IV药水 | 42 | — | — |

### spawn_chance

命中时有概率生成实体：

| 字段 | 类型 | 说明 |
|---|---|---|
| `first_spawn_percent_chance` | Decimal | 第一次生成的概率 |
| `second_spawn_percent_chance` | Decimal | 第二次生成的概率 |
| `first_spawn_count` | Integer | 第一次生成的数量 |
| `second_spawn_count` | Integer | 第二次生成的数量 |
| `spawn_definition` | String | 要生成的实体标识符 |
| `spawn_baby` | Boolean | 是否生成幼年形态 |

### particle_on_hit

命中时生成粒子：

| 字段 | 类型 | 说明 |
|---|---|---|
| `particle_type` | String | 粒子发射器名称 |
| `num_particles` | Integer | 粒子数量 |
| `on_entity_hit` | Boolean | 命中实体时生成 |
| `on_other_hit` | Boolean | 命中其他物体时生成 |

### mob_effect

命中时对目标施加状态效果：

| 字段 | 类型 | 说明 |
|---|---|---|
| `effect` | String | 状态效果标识符 |
| `duration` | Integer | 效果持续时间（刻） |
| `durationeasy` | Integer | 简单难度下的持续时间（刻） |
| `durationnormal` | Integer | 普通难度下的持续时间（刻） |
| `durationhard` | Integer | 困难难度下的持续时间（刻） |
| `amplifier` | Integer | 效果等级 |
| `ambient` | Boolean | 是否为环境效果（粒子半透明） |
| `visible` | Boolean | 是否显示粒子 |

### grant_xp

命中时生成经验球（而非直接给予经验）：

| 字段 | 类型 | 说明 |
|---|---|---|
| `minXP` | Integer | 最小经验值 |
| `maxXP` | Integer | 最大经验值 |
| `xp` | Integer | 固定经验值（设置后忽略min/max） |

### freeze_on_hit

命中时冻结水（具体行为待明确）<!-- md:flag edu -->：

| 字段 | 类型 | 说明 |
|---|---|---|
| `shape` | String | `"sphere"`或`"cube"` |
| `snap_to_block` | Boolean | 对齐到方块 |
| `size` | Integer | 冻结范围大小 |

## 注意事项

创建自定义弹射物（如自定义箭矢、三叉戟变体或全新弹射物）时，建议设置合适的[运行时标识符](../../../refs/addon/runtime-identifier.md)，否则可能出现视觉异常、击退方向错误或可以徒手击杀箭矢等问题。
