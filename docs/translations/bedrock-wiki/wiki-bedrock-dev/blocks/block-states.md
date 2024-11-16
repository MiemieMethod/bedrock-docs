---
title: 方块状态
description: 方块状态允许你的方块具有变体，每个变体都有其独特的功能和外观，通过使用排列组合实现。
category: 一般
nav_order: 4
mentions:
    - QuazChick
    - SmokeyStack
---

:::tip 格式与最低引擎版本 `1.21.40`
在处理方块状态时，请确保你的包清单中的 `min_engine_version` 至少为 `1.20.20` 或更高。
:::

方块状态允许你的方块具有变体，每个变体都有其独特的功能和外观，通过使用[排列组合](../blocks/block-permutations.md)实现。

## 定义状态

有效的状态值可以定义为布尔值、整数或字符串数组，也可以通过使用对象定义为整数范围。值数组中的第一个项目用作默认值。

每个状态最多可以定义 16 个有效值。对于整数范围状态，这意味着 `max` 值不能比 `min` 值高出 15。

_从实验“假日创作者功能”中发布，适用于格式版本 1.19.70 及更高版本。_

<CodeHeader>BP/blocks/custom_block.json</CodeHeader>

```json
{
  "format_version": "1.21.40",
  "minecraft:block": {
    "description": {
      "identifier": "wiki:custom_block",
      "states": {
        "wiki:string_state_example": ["red", "green", "blue"],
        "wiki:boolean_state_example": [false, true],
        "wiki:integer_state_example": [1, 2, 3],
        "wiki:integer_range_state_example": {
          "values": { "min": 0, "max": 5 } // 同 [0, 1, 2, 3, 4, 5]
        }
      }
    },
    "components": { ... },
    "permutations": [ ... ]
  }
}
```

## 获取状态值

以下是获取不同上下文中方块状态当前值的方法。

### Molang 查询函数

状态值由 `block_state` 查询函数返回。

<CodeHeader></CodeHeader>

```c
q.block_state('wiki:string_state_example') == 'blue'
```

### 命令参数

[方块状态参数](../commands/block-states.md)包含在 `execute` 和 `testforblock` 等命令中，可用于检查方块状态的值。

<CodeHeader></CodeHeader>

```c
execute if block ~~~ wiki:custom_block["wiki:string_state_example"="blue", "wiki:integer_state_example"=4] run kill
```

### 脚本 API

[`BlockPermutation.getState()`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/blockpermutation#getstate) 方法允许你获取不同状态的当前值。

<CodeHeader></CodeHeader>

```js
customBlock.permutation.getState("wiki:integer_state_example") === 3;
```

## 设置状态值

### 命令参数

[方块状态参数](../commands/block-states.md)包含在 `setblock` 和 `fill` 等命令中，可用于将状态更改为非默认值。

<CodeHeader></CodeHeader>

```c
setblock ~~~ wiki:custom_block["wiki:string_state_example"="blue", "wiki:integer_state_example"=4]
```

### 脚本 API

[`BlockPermutation.withState()`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/blockpermutation#withstate) 方法返回一个新的方块排列，其中指定的状态值已更改。此排列可以使用[`Block.setPermutation()`](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/block#setpermutation) 方法应用于方块，如下所示。

<CodeHeader></CodeHeader>

```js
customBlock.setPermutation(customBlock.permutation.withState("wiki:boolean_state_example", false));
```