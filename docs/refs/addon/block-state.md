# 方块状态与置换

本页列出行为包方块定义中自定义方块状态、方块置换和原版方块状态查询相关的参考信息。概念说明见[方块状态](../../docs/general/block-state.md)和[方块置换](../../docs/general/block-permutation.md)。

## 自定义方块状态

自定义方块状态位于`minecraft:block.description.states`对象中。每个状态以状态名为键，状态名应使用开发者自己的命名空间；值为该状态允许的取值列表。

| 位置 | 类型 | 描述 |
| --- | --- | --- |
| `minecraft:block.description.states` | 对象 | 自定义方块状态集合。 |
| `<namespace:state_name>` | 数组或范围对象 | 单个状态允许的取值。键名必须带命名空间；取值可以是布尔值、数字或字符串。 |

数字范围可以写为范围对象。例如，`"example:integer_state":{"values":{"min":0,"max":3}}`等价于`"example:integer_state":[0,1,2,3]`。

## 方块置换

方块置换位于`minecraft:block.permutations`数组。每个置换在其条件为真时应用自己的组件集合，用于在同一个方块标识符下表现不同状态组合。

| 字段 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| `condition` | Molang表达式字符串 | 未设置 | 决定该置换是否生效。置换条件通常通过`query.block_state()`读取方块状态。 |
| `components` | 对象 | 未设置 | 当条件为真时应用的方块组件集合。 |

`/setblock`命令可以在放置方块时指定一个或多个方块状态值。例如：

```mcfunction
setblock ~ ~ ~ example:lamp_block ["example:is_lit"=true]
```

## 置换规模控制

方块状态值域的笛卡尔积决定该方块可能产生的置换数量。状态越多、每个状态的可选值越多，置换组合就越大，定义、测试和维护成本也越高。因此，自定义方块应只保留确有必要参与外观或行为分支的状态。

## 原版方块状态

原版方块状态由游戏引擎定义，可在命令、方块置换条件和部分API中出现。完整列表见[原版方块状态](../tables/blocks/block_states.md)。自定义方块通常不应直接复制原版状态名称，除非该状态由[方块萃取](block-trait.md)明确启用或文档明确允许。

## 附加值映射

旧式命令和旧版内容可能使用方块附加值表示方块形态。附加值与方块状态之间的官方映射见[附加值到方块状态映射](../tables/blocks/aux_value_to_block_state_map.md)。新内容应优先使用明确的方块状态，而不是依赖旧式附加值。