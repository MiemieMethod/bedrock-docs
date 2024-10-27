---
title: 方块排列
description: 方块排列表示方块可能处于的所有状态配置。
category: 一般
nav_order: 7
mentions:
    - QuazChick
    - SmokeyStack
---

:::tip 格式与最低引擎版本 `1.21.40`
在学习方块排列之前，您应该对[方块状态](../blocks/block-states.md)有一定的了解。

在处理方块状态时，请确保您的包清单中的 `min_engine_version` 至少为 `1.20.20` 或更高。
:::

## 什么是排列？

方块排列表示每个方块可能处于的所有状态值配置。

例如，如果您添加了一个具有两个布尔状态的自定义方块……

<CodeHeader>minecraft:block</CodeHeader>

```json
"description": {
    "identifier": "wiki:permutations_example",
    "states": {
        "wiki:first_state": [false, true],
        "wiki:second_state": [false, true]
    }
}
```

……那么以下 4 种方块排列将被添加到世界中：

| 方块标识符                  | wiki:first_state | wiki:second_state |
| ------------------------- | ---------------- | ----------------- |
| wiki:permutations_example | false            | false             |
| wiki:permutations_example | true             | false             |
| wiki:permutations_example | false            | true              |
| wiki:permutations_example | true             | true              |

要计算您的方块有多少个排列，请将每个状态的有效状态值数量相乘。
例如，上述示例的计算为 2 &times; 2，这意味着该方块有 4 种排列。

### 误解

-   所有方块都有排列，即使没有状态的方块也有 1 种排列，仅由方块标识符组成。
-   方块的排列数量取决于其状态，而不是 `permutations` 数组中的项目数量。

## 有条件地应用组件

方块的 `permutations` 数组提供了一种根据当前排列有条件地将组件（包括标签）应用于方块的方法。

`permutations` 数组中的组件可以覆盖方块的基础组件以及其他组件列表的组件。`permutations` 数组中的最新组件列表优先级最高。

_从实验 `假日创作者功能` 中发布，适用于格式版本 1.19.70 及更高版本。_

<CodeHeader>BP/blocks/custom_block.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_block",
            "states": {
                "wiki:integer_state_example": [2, 4, 6, 8],
                "wiki:boolean_state_example": [false, true],
                "wiki:string_state_example": ["red", "green", "blue"]
            }
        },
        "components": {},
        "permutations": [
            {
                "condition": "q.block_state('wiki:integer_state_example') == 2",
                "components": {
                    "minecraft:friction": 0.1
                }
            },
            {
                "condition": "q.block_state('wiki:boolean_state_example')",
                "components": {
                    "minecraft:friction": 0.8 // 覆盖之前的排列
                }
            },
            {
                "condition": "q.block_state('wiki:string_state_example') == 'red' && !q.block_state('wiki:boolean_state_example')",
                "components": {
                    "minecraft:geometry": "geometry.pig"
                }
            }
        ]
    }
}
```

### 排列条件

当条件被评估为真（不是 false 或 0）时，相关的组件列表将被应用。

排列条件以 Molang 表达式字符串的形式书写，具有非常有限的上下文：

-   条件完全基于方块的排列，因此仅能访问 `q.block_state` 查询函数。
-   这也意味着条件不能有副作用。
    -   以下数学函数不可使用：`math.die_roll`、`math.die_roll_integer`、`math.random`、`math.random_integer`。
    -   变量（包括 `temp` 变量）不能被赋值。

```c
q.block_state('wiki:integer_state_example') < 6 && !q.block_state('wiki:boolean_state_example')
```

## 排列限制

与所有方块一样，Mojang 对某些方面施加了限制，以防止不良行为。

### 每个方块的最大数量

一个方块 _不能_ 有超过 65,536 种排列（相当于 4 个状态，每个状态有 16 个值）。
超过此限制将导致内容日志错误，并且某些状态将缺失。

### 每个世界的最大数量

一个世界 _应该_ 不超过 65,536 个注册的方块排列（不一定是已放置的）。
超过此限制将导致以下内容日志警告：

> 超过 65536 个方块排列的世界可能会降低性能。当前世界有 XXXXX 种排列。