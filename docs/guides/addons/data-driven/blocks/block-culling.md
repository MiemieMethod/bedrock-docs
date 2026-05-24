# 方块剔除

方块剔除规则允许在相邻方块满足条件时隐藏自定义方块几何体的特定部分，从而避免渲染玩家看不到的面，提升性能。

## 创建剔除规则文件

剔除规则定义在资源包的 `block_culling/` 目录下：

```json title="RP/block_culling/my_block.json"
{
    "format_version": "1.21.80",
    "minecraft:block_culling_rules": {
        "description": {
            "identifier": "wiki:culling.my_block"
        },
        "rules": [
            {
                "geometry_part": {
                    "bone": "body",
                    "cube": 0,
                    "face": "north"
                },
                "conditions": [
                    {
                        "block_filter": "minecraft:glass",
                        "culling_condition": "same_block_permutation"
                    }
                ]
            }
        ]
    }
}
```

## 引用剔除规则

在方块JSON的 `minecraft:geometry` 组件中通过 `culling` 参数引用剔除规则：

```json title="BP/blocks/my_block.json > components"
"minecraft:geometry": {
    "identifier": "geometry.my_block",
    "culling": "wiki:culling.my_block"
}
```

## 剔除规则结构

每条规则由 `geometry_part` 和 `conditions` 两部分组成：

### geometry_part

指定要被剔除的几何体部分：

- `bone`：目标骨骼的名称。
- `cube`（可选）：骨骼中目标立方体的索引（从0开始），不填表示骨骼中所有立方体。
- `face`：被剔除的面方向（`north`、`south`、`east`、`west`、`up`、`down`）。

### conditions

条件数组中的所有条件同时满足时，对应的几何体部分被隐藏（逻辑与关系）。

每个条件包含：

- `block_filter`：相邻方块必须匹配的方块标识符。
- `culling_condition`：满足剔除的具体条件，可选值：
    - `"same_block"`：相邻位置是 `block_filter` 指定的任意同类方块。
    - `"same_block_permutation"`：相邻位置是完全相同置换的同类方块（包含相同的方块状态）。
    - `"same_culling_layer"`：相邻位置的方块使用了相同的剔除规则。

## 透明方块剔除示例

以下是一个类似玻璃的透明方块，相邻相同方块时隐藏接触面的完整示例：

```json title="RP/block_culling/custom_glass.json"
{
    "format_version": "1.21.80",
    "minecraft:block_culling_rules": {
        "description": {
            "identifier": "wiki:culling.custom_glass"
        },
        "rules": [
            {
                "geometry_part": { "bone": "glass", "face": "north" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            },
            {
                "geometry_part": { "bone": "glass", "face": "south" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            },
            {
                "geometry_part": { "bone": "glass", "face": "east" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            },
            {
                "geometry_part": { "bone": "glass", "face": "west" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            },
            {
                "geometry_part": { "bone": "glass", "face": "up" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            },
            {
                "geometry_part": { "bone": "glass", "face": "down" },
                "conditions": [{ "block_filter": "wiki:custom_glass", "culling_condition": "same_culling_layer" }]
            }
        ]
    }
}
```

对应的方块JSON：

```json title="BP/blocks/custom_glass.json > components"
"minecraft:geometry": {
    "identifier": "geometry.custom_glass",
    "culling": "wiki:culling.custom_glass"
}
```

/// note | 全方块的剔除
对于完全填满1×1×1空间的全方块，游戏会自动剔除被相邻不透明方块遮挡的面，不需要额外的剔除规则。剔除规则主要用于不完整方块（如栅栏顶部、特殊模型等）和透明方块。
///