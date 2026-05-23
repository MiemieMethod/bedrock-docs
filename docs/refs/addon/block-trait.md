# 方块萃取

本页列出行为包方块定义中`minecraft:block.description.traits`对象可用的主要方块萃取、可启用状态和附加字段。方块萃取用于使自定义方块复用由引擎维护的放置方向、放置位置或连接关系状态；相关概念说明见[方块萃取](../../docs/general/block-trait.md)。

## 位置

| 字段 | 类型 | 描述 |
| --- | --- | --- |
| `minecraft:block.description.traits` | 对象 | 方块萃取集合。每个键为一个萃取标识符，值为该萃取的配置对象。 |
| `enabled_states` | 字符串数组 | 启用该萃取维护的一个或多个方块状态。不同萃取允许的状态不同。 |

## `minecraft:placement_direction`

`minecraft:placement_direction`记录玩家放置方块时面对的方向。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled_states` | 字符串数组 | 未设置 | 可启用`minecraft:cardinal_direction`、`minecraft:facing_direction`或`minecraft:corner_and_cardinal_direction`。 |
| `y_rotation_offset` | 数值 | `0.0` | 将记录的水平朝向逆时针偏移指定角度。可用值为`0.0`、`90.0`、`180.0`和`270.0`。 |
| `blocks_to_corner_with` | 数组 | 同名方块 | 与`minecraft:corner_and_cardinal_direction`配合，用于指定可共同形成角部状态的方块匹配对象。官方示例使用`tags`条件。 |

| 启用状态 | 可查询状态 | 取值 |
| --- | --- | --- |
| `minecraft:cardinal_direction` | `minecraft:cardinal_direction` | `north`、`south`、`east`、`west` |
| `minecraft:facing_direction` | `minecraft:facing_direction` | `north`、`south`、`east`、`west`、`up`、`down` |
| `minecraft:corner_and_cardinal_direction` | `minecraft:cardinal_direction` | `north`、`south`、`east`、`west` |
| `minecraft:corner_and_cardinal_direction` | `minecraft:corner` | `inner_left`、`inner_right`、`outer_left`、`outer_right`、`none` |

## `minecraft:placement_position`

`minecraft:placement_position`记录方块相对于其他方块被放置的位置。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled_states` | 字符串数组 | 未设置 | 可启用`minecraft:block_face`或`minecraft:vertical_half`。 |

| 启用状态 | 可查询状态 | 取值与语义 |
| --- | --- | --- |
| `minecraft:block_face` | `minecraft:block_face` | `north`、`south`、`east`、`west`、`up`、`down`。表示该方块被放置在相邻方块的哪一个面上。 |
| `minecraft:vertical_half` | `minecraft:vertical_half` | `bottom`或`top`。表示该方块位于相邻方块的下半或上半。点击方块底面，或点击水平侧面的上半区域时，通常会得到`top`。 |

/// note | 半砖行为
`minecraft:vertical_half`只复用上半和下半放置状态。它不会自动实现两个半砖合并为双半砖的原版行为。
///

## `minecraft:connection`

`minecraft:connection`记录方块与水平相邻方块之间的连接关系。

/// warning | 实验性要求
`minecraft:connection`要求`format_version`不低于`1.21.130`，并且目前需要启用“Upcoming Creator Features”实验性开关。
///

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `enabled_states` | 字符串数组 | 未设置 | 目前唯一有效值为`minecraft:cardinal_connections`。 |

| 启用状态 | 可查询状态 | 类型 | 语义 |
| --- | --- | --- | --- |
| `minecraft:cardinal_connections` | `minecraft:connection_north` | 布尔值 | 方块是否向北连接。 |
| `minecraft:cardinal_connections` | `minecraft:connection_south` | 布尔值 | 方块是否向南连接。 |
| `minecraft:cardinal_connections` | `minecraft:connection_east` | 布尔值 | 方块是否向东连接。 |
| `minecraft:cardinal_connections` | `minecraft:connection_west` | 布尔值 | 方块是否向西连接。 |

连接状态会在该方块或相邻方块改变、移动时更新。方块是否根据这些状态改变模型、碰撞箱或其他组件，仍然需要通过`permutations`条件自行配置。
