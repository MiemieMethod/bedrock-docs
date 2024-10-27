---
title: 区块剔除
description: 区块剔除规则有助于提升性能，允许您根据周围完整的不透明区块移除区块模型的面。
category: 一般
tags:
    - 中级
mentions:
    - legopitstop
    - QuazChick
---

:::tip 创建您的模型
在开始之前，请确保您已为您的区块[创建了模型](../blocks/block-models.md)。否则您将没有内容可应用剔除规则！
:::

## 应用剔除规则

区块剔除规则允许您根据周围完整的不透明区块移除区块模型的面。这可以帮助提高游戏性能，因为资源不会浪费在不必要渲染隐藏部分上。

剔除规则添加在资源包的“block_culling”文件夹中，格式如下所示：

<CodeHeader>RP/block_culling/lamp.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block_culling_rules": {
        "description": {
            "identifier": "wiki:lamp_culling" // 在区块 JSON 几何组件中引用的标识符。
        },
        "rules": [ ... ] // 可以包含多个剔除规则的数组。
    }
}
```

然后将其应用于区块模型的[`minecraft:geometry`](../blocks/block-components.md#geometry)组件中：

<CodeHeader>minecraft:block > components</CodeHeader>

```json
"minecraft:geometry": {
    "identifier": "geometry.lamp", // 模型标识符
    "culling": "wiki:lamp_culling" // 区块剔除规则标识符
}
```

## 剔除整个骨骼

如果一个骨骼仅从一个方向可见，则应使用此类型的规则，这意味着整个骨骼可以被剔除，而不是单个立方体的面。

<CodeHeader>minecraft:block_culling_rules > rules</CodeHeader>

```json
{
    "direction": "up", // 如果上方有一个完整的不透明区块，则该骨骼将被剔除。
    "geometry_part": {
        "bone": "lamp_bulb" // 要被剔除的骨骼名称。
    }
}
```

## 剔除立方体面

当您想隐藏与完整不透明区块相邻的立方体的特定面时，应使用此类型的规则。

<CodeHeader>minecraft:block_culling_rules > rules</CodeHeader>

```json
{
    "direction": "down", // 如果下方有一个完整的不透明区块，则该骨骼将被剔除。
    "geometry_part": {
        "bone": "lamp_base", // 包含要被剔除的立方体的骨骼名称。
        "cube": 0, // 该骨骼的“cubes”数组中立方体的零基索引。
        "face": "down" // 要剔除的立方体面。这通常与规则的“direction”相同，除非您的立方体被旋转。
    }
}
```