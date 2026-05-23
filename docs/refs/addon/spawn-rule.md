# 生成规则

本页列出国际版行为包`spawn_rules/`目录中生成规则文件的主要结构、官方生成条件组件、字段默认值和已弃用项。生成规则用于控制实体的自然生成位置、数量、权重、群体规模和环境条件，不影响命令、刷怪蛋或脚本直接生成实体。

/// note | 资料来源范围
本页依据Microsoft Learn的`SpawnRulesReference`自动生成参考整理。该参考未对部分字段给出完整语义说明；这些字段仅按官方字段名、类型和默认值记录。
///

## 根对象

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `format_version` | 版本 | 未设置 | 生成规则文件使用的格式版本。 |
| `minecraft:spawn_rules` | 对象 | 未设置 | 单个生成规则定义。 |

## `minecraft:spawn_rules`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `description` | 对象 | 未设置 | 生成规则的标识信息和人口控制池。 |
| `conditions` | 对象数组 | `[]` | 一个或多个生成条件集合。每个元素定义一套独立的生成环境、数量和事件设置。 |

### `description`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 未设置 | 关联实体的赋命名空间标识符，例如`minecraft:zombie`。 |
| `population_control` | 字符串 | 未设置 | 人口控制池。该字段指定实体参与哪一类生成数量控制。 |

常见人口控制池包括`animal`、`water_animal`、`monster`和`cat`。其中`cat`池按照村庄内的猫数量进行限制，行为不同于普通人口控制池。

### `conditions`

| 组件 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `minecraft:biome_filter` | 过滤器对象、过滤器对象数组 | 未设置 | 限定实体可生成的生物群系。结构与实体过滤器相同。 |
| `minecraft:brightness_filter` | 对象 | 未设置 | 按生成位置亮度限制生成。 |
| `minecraft:delay_filter` | 对象 | 未设置 | 在生成条件满足后延迟实体生成。 |
| `minecraft:density_limit` | 对象 | 未设置 | 分别限制地表和地下生成的实体数量。 |
| `minecraft:difficulty_filter` | 对象 | 未设置 | 按世界困难度限制生成。 |
| `minecraft:disallow_spawns_in_bubble` | 对象 | 未设置 | 阻止实体在气泡柱内生成。 |
| `minecraft:distance_filter` | 对象 | 未设置 | 按与最近玩家的距离限制生成。 |
| `minecraft:height_filter` | 对象 | 未设置 | 按生成位置Y坐标限制生成。 |
| `minecraft:herd` | 对象、对象数组 | `[]` | 配置群体生成数量，以及群体生成过程中的实体事件。 |
| `minecraft:is_experimental` | 对象 | 未设置 | 将该生成条件标记为实验性；仅在对应实验开关启用时生效。<!-- md:flag experimental --> |
| `minecraft:is_persistent` | 对象 | 未设置 | 使生成出的实体不会自然消失，常用于村民等实体。 |
| `minecraft:mob_event_filter` | 对象 | 未设置 | 按世界级生物事件是否激活限制生成。 |
| `minecraft:permute_type` | 对象、对象数组 | `[]` | 按权重选择实际生成的实体置换。 |
| `minecraft:player_in_village_filter` | 对象 | 未设置 | 按玩家是否位于村庄范围附近限制生成。 |
| `minecraft:spawn_event` | 对象 | `{ "event": "" }` | 实体生成时触发指定实体事件，常用于初始化实体行为。 |
| `minecraft:spawns_above_block_filter` | 对象 | `{ "blocks": [], "distance": 1 }` | 按生成点上方的方块限制生成。该组件已弃用，见[已弃用组件](#已弃用组件)。 |
| `minecraft:spawns_lava` | 对象 | 未设置 | 表示实体可在熔岩中生成。 |
| `minecraft:spawns_on_block_filter` | 字符串、字符串数组、对象数组 | `[]` | 指定实体可生成在其上的方块。对象形式使用方块说明对象。 |
| `minecraft:spawns_on_block_prevented_filter` | 字符串数组 | `[]` | 指定实体不可生成在其上的方块。 |
| `minecraft:spawns_on_surface` | 对象 | 未设置 | 表示实体可在地表生成。 |
| `minecraft:spawns_underground` | 对象 | 未设置 | 表示实体可在地下生成。 |
| `minecraft:spawns_underwater` | 对象 | 未设置 | 表示实体可在水中生成。 |
| `minecraft:weight` | 对象 | 未设置 | 设置该生成条件相对于同一生物群系和生成池内其他条件的权重。 |
| `minecraft:world_age_filter` | 对象 | 未设置 | 按世界已存在时间限制生成，单位为刻。 |

<!-- md:sortable -->

## 组件字段

### `minecraft:biome_filter`

`minecraft:biome_filter`允许生成规则使用过滤器结构判断生物群系。过滤器可写为单个测试对象、测试数组、逻辑组合对象，或这些结构的组合。常用测试为`has_biome_tag`。过滤器的基本字段详见[实体过滤器](entity-filter.md)。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `test` | 字符串 | 未设置 | 过滤器测试名。 |
| `subject` | 字符串 | 未设置 | 测试主体。 |
| `operator` | 字符串 | 未设置 | 与`value`比较时使用的运算符。 |
| `value` | 整数 | 未设置 | 用于比较的值。官方自动表在此处列为整数；实际测试的值类型由具体测试决定。 |
| `domain` | 字符串 | 未设置 | 测试域。 |
| `all_of` | 对象数组 | 未设置 | 所有子过滤器均需通过。 |
| `any_of` | 对象数组 | 未设置 | 任一子过滤器通过即可。 |
| `none_of` | 对象数组 | 未设置 | 所有子过滤器均不得通过。 |

### `minecraft:brightness_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数 | `0` | 允许生成的最小亮度，最大值为`15`。 |
| `max` | 整数 | `15` | 允许生成的最大亮度，最大值为`15`。 |
| `adjust_for_weather` | 布尔值 | `false` | 是否按当前天气修正亮度。降雨和雷暴会降低亮度。 |

### `minecraft:delay_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `identifier` | 字符串 | 空字符串 | 延迟过滤器标识符。官方参考未给出进一步说明。 |
| `min` | 整数 | `0` | 延迟范围的最小值。 |
| `max` | 整数 | `0` | 延迟范围的最大值。 |
| `spawn_chance` | 整数 | `100` | 延迟完成后的生成机会。 |

### `minecraft:density_limit`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `surface` | 整数 | `-1` | 地表生成数量上限。`-1`表示不限制。 |
| `underground` | 整数 | `-1` | 地下生成数量上限。`-1`表示不限制。 |

### `minecraft:difficulty_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 字符串 | `peaceful` | 允许生成的最低困难度。 |
| `max` | 字符串 | `hard` | 允许生成的最高困难度。 |

`min`和`max`可使用下列值：

| 值 | 描述 |
| --- | --- |
| `peaceful` | 和平。 |
| `easy` | 简单。 |
| `normal` | 普通。 |
| `hard` | 困难。 |

### `minecraft:distance_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数 | `24` | 与最近玩家之间允许生成的最小距离。 |
| `max` | 整数 | `128` | 与最近玩家之间允许生成的最大距离。 |

### `minecraft:height_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数 | `24` | 允许生成的最小Y坐标。 |
| `max` | 整数 | `128` | 允许生成的最大Y坐标。 |

### `minecraft:herd`

`minecraft:herd`配置一次生成尝试中群体的数量范围。它还可以在群体生成过程中对前若干个实体或跳过若干个实体后的实体运行事件。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min_size` | 整数 | `1` | 该群体尝试生成的最小数量。 |
| `max_size` | 整数 | `1` | 该群体尝试生成的最大数量。 |
| `initial_event` | 字符串 | 空字符串 | 对群体中最先放置的若干实体运行的事件。 |
| `initial_event_count` | 整数 | `0` | `initial_event`运行次数。 |
| `event` | 字符串 | 空字符串 | 跳过指定数量后运行的事件。 |
| `event_skip_count` | 整数 | `0` | 运行`event`前跳过的群体数量。 |

### `minecraft:mob_event_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `event` | 字符串 | 空字符串 | 要检测的世界级生物事件。 |

### `minecraft:permute_type`

`minecraft:permute_type`用于在生成规则触发时按权重选择实际生成的实体置换，可用于形成自然的实体变体分布。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `entity_type` | 对象 | 空对象 | 被选中时要生成的实体类型说明。官方参考将该字段列为对象。 |
| `weight` | 整数 | 未设置 | 该置换在全部置换中的比例权重。 |
| `min_guaranteed` | 整数 | `0` | 该置换最少生成的数量。 |

### `minecraft:player_in_village_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `distance` | 整数 | 未设置 | 玩家与村庄范围相关的距离限制。官方参考未给出进一步说明。 |
| `village_border_tolerance` | 整数 | `10` | 村庄边界容差。 |

### `minecraft:spawn_event`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `event` | 字符串 | 空字符串 | 实体生成时触发的实体事件。 |

### `minecraft:spawns_on_block_filter`

`minecraft:spawns_on_block_filter`可写为单个方块名、方块名数组，或带`name`字段的方块说明对象数组。

```json title="spawns_on_block_filter示例"
{
  "minecraft:spawns_on_block_filter": [
    "minecraft:grass_block",
    { "name": "minecraft:podzol" }
  ]
}
```

### `minecraft:spawns_on_block_prevented_filter`

`minecraft:spawns_on_block_prevented_filter`是方块名数组。若生成位置下方方块匹配该数组，实体不会在该位置生成。

### `minecraft:weight`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `default` | 整数 | 未设置 | 该生成条件的基础权重。权重越高，在同一生物群系和生成池中越容易被选择。 |
| `rarity` | 整数 | `0` | 稀有度相关权重参数。官方参考未给出进一步说明。 |

### `minecraft:world_age_filter`

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `min` | 整数 | `0` | 允许生成前世界至少已存在的刻数。 |
| `max` | 整数 | `-1` | 允许生成的最大世界年龄。`-1`表示不设置上限。 |

## 已弃用组件

### `minecraft:spawns_above_block_filter`

/// warning | 已弃用
`minecraft:spawns_above_block_filter`是旧版生成条件组件。Microsoft Learn说明，该组件用于`1.17.20`及更早版本，并且在至少`1.18.0`格式版本之后不再工作。新内容不应依赖该组件。
///

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `blocks` | 对象 | `[]` | 要检测的方块列表。官方参考将该字段类型列为对象。 |
| `distance` | 整数 | `1` | 距生成点的检测距离。 |

## 示例

```json title="spawn_rules/zombie.json"
{
  "format_version": "1.20.80",
  "minecraft:spawn_rules": {
    "description": {
      "identifier": "demo:night_walker",
      "population_control": "monster"
    },
    "conditions": [
      {
        "minecraft:spawns_on_surface": {},
        "minecraft:brightness_filter": {
          "min": 0,
          "max": 7,
          "adjust_for_weather": true
        },
        "minecraft:difficulty_filter": {
          "min": "easy",
          "max": "hard"
        },
        "minecraft:distance_filter": {
          "min": 24,
          "max": 128
        },
        "minecraft:weight": {
          "default": 100
        },
        "minecraft:herd": {
          "min_size": 1,
          "max_size": 2
        },
        "minecraft:biome_filter": {
          "test": "has_biome_tag",
          "operator": "==",
          "value": "overworld"
        }
      }
    ]
  }
}
```
