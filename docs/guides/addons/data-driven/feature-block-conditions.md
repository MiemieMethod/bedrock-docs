# 利用方块条件控制地物放置

许多地物类型不提供原生的"条件检查"机制——例如，矿石地物（`ore_feature`）无法直接检测其放置位置的周围方块。本教程介绍一种利用聚合地物（`aggregate_feature`）与单方块地物（`single_block_feature`）组合实现任意地物的方块条件检测技术。

/// note | 实验性玩法
本教程涉及的功能需要在世界设置中启用"自定义生物群系"实验性玩法开关。
///

## 原理

`single_block_feature`提供了`may_replace`（可替换方块列表）和`may_attach_to`（可附着方块列表）两种条件字段，可以细粒度地控制单个方块的放置条件。利用这一特性，我们可以将其作为"探针"：

1. **条件探针**：一个单方块地物，配置了所需的放置条件，放置一个临时方块（"哑地物"）。若条件不满足则放置失败。
2. **清理地物**：将上一步放置的临时方块替换回原来的方块（如空气）。
3. **目标地物**：真正要放置的地物（如矿石地物）。

三者通过聚合地物串联，配合`early_out: "first_failure"`实现：若条件探针失败，后续步骤全部取消。

## 示例：仅在草方块上方的空气中生成岩石堆

本示例让矿石地物（岩石堆）只在草方块正上方的空气格中生成。

### 文件结构

/// html | div.treeview
- `demo_BP`
    - `features`
        - `wiki_block_condition_feature.json`（条件探针）
        - `wiki_block_replacement_feature.json`（清理地物）
        - `wiki_rock_ore_feature.json`（目标地物）
        - `wiki_aggregate_placement_rock_feature.json`（聚合地物）
    - `feature_rules`
        - `wiki_overworld_after_surface_rock_feature.json`
///

### 条件探针

条件探针定义了真正的放置条件：仅在`minecraft:air`中、且下方为`minecraft:grass`时放置一个圆石。选择圆石是因为本例中目标地物不会放置圆石，不会造成干扰；实际使用时可选择任意不影响目标地物的方块。

```json title="BP/features/wiki_block_condition_feature.json"
{
    "format_version": "1.18.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:block_condition_feature"
        },
        "places_block": "minecraft:cobblestone",
        "enforce_placement_rules": false,
        "enforce_survivability_rules": false,
        "may_replace": ["minecraft:air"],
        "may_attach_to": {
            "bottom": ["minecraft:grass"]
        }
    }
}
```

/// define
`may_replace`

- 该地物只能放置在`minecraft:air`中，不会替换其他方块。

`may_attach_to.bottom`

- 该地物下方必须是`minecraft:grass`，否则放置失败，触发`early_out`逻辑。

///

### 清理地物

清理地物将条件探针留下的圆石替换为空气，恢复原始状态：

```json title="BP/features/wiki_block_replacement_feature.json"
{
    "format_version": "1.18.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:block_replacement_feature"
        },
        "places_block": "minecraft:air",
        "enforce_placement_rules": false,
        "enforce_survivability_rules": false,
        "may_replace": ["minecraft:cobblestone"]
    }
}
```

### 目标地物

目标地物是真正要放置的内容，不需要任何特殊条件配置：

```json title="BP/features/wiki_rock_ore_feature.json"
{
    "format_version": "1.18.0",
    "minecraft:ore_feature": {
        "description": {
            "identifier": "wiki:rock_ore_feature"
        },
        "count": 12,
        "replace_rules": [
            {
                "places_block": "minecraft:stone",
                "may_replace": ["minecraft:air", "minecraft:grass"]
            },
            {
                "places_block": {
                    "name": "minecraft:dirt",
                    "states": {
                        "dirt_type": "coarse"
                    }
                },
                "may_replace": ["minecraft:dirt"]
            }
        ]
    }
}
```

### 聚合地物

聚合地物将上述三个地物按顺序串联，并通过`early_out: "first_failure"`确保条件探针失败时立即中止：

```json title="BP/features/wiki_aggregate_placement_rock_feature.json"
{
    "format_version": "1.18.0",
    "minecraft:aggregate_feature": {
        "description": {
            "identifier": "wiki:aggregate_placement_rock_feature"
        },
        "features": [
            "wiki:block_condition_feature",
            "wiki:block_replacement_feature",
            "wiki:rock_ore_feature"
        ],
        "early_out": "first_failure"
    }
}
```

`features`数组按顺序执行：首先尝试条件探针，若成功则继续执行清理地物，最后放置目标地物；若条件探针失败，`early_out: "first_failure"`立即停止，后续地物不会执行。

### 地物规则

地物规则将聚合地物分发到生物群系中，并沿高度图放置：

```json title="BP/feature_rules/wiki_overworld_after_surface_rock_feature.json"
{
    "format_version": "1.18.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:overworld_after_surface_rock_feature",
            "places_feature": "wiki:aggregate_placement_rock_feature"
        },
        "conditions": {
            "placement_pass": "after_surface_pass",
            "minecraft:biome_filter": [
                {
                    "any_of": [
                        {
                            "test": "has_biome_tag",
                            "operator": "==",
                            "value": "overworld"
                        },
                        {
                            "test": "has_biome_tag",
                            "operator": "==",
                            "value": "overworld_generation"
                        }
                    ]
                }
            ]
        },
        "distribution": {
            "scatter_chance": 33,
            "iterations": 1,
            "coordinate_eval_order": "xzy",
            "x": {
                "distribution": "uniform",
                "extent": [0, 15]
            },
            "y": "q.heightmap(v.worldx, v.worldz)",
            "z": {
                "distribution": "uniform",
                "extent": [0, 15]
            }
        }
    }
}
```

`placement_pass`使用`after_surface_pass`（地表地物生成之后阶段），`scatter_chance: 33`表示每区块约33%的概率尝试一次，`y`使用`q.heightmap`将地物放置在地表。

## 扩展思路

此技术不局限于矿石地物，可以与任何地物类型配合：

- 用`may_attach_to.top`检测上方方块，在洞穴顶部放置悬挂地物
- 用`may_attach_to`的多个方向同时检测，实现更复杂的空间条件
- 将条件探针的`may_replace`设为特定方块，实现"仅在该方块处生成"的精确控制
- 在聚合地物的`features`列表中添加更多目标地物，形成多地物组合条件生成