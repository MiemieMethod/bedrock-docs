# 生成地表斑块

本教程演示如何使用散植地物（`scatter_feature`）、加权随机地物（`weighted_random_feature`）和单方块地物（`single_block_feature`）组合，在主世界地表生成多种方块随机混合的斑块图案，常用于模拟地面装饰变化。

/// note | 实验性玩法
本教程涉及的功能需要在世界设置中启用"自定义生物群系"实验性玩法开关。
///

## 文件结构

/// html | div.treeview
- `demo_BP`
    - `features`
        - `wiki_coarse_dirt_feature.json`
        - `wiki_podzol_feature.json`
        - `wiki_cobblestone_feature.json`
        - `wiki_select_surface_block_feature.json`（加权随机地物）
        - `wiki_scatter_surface_block_feature.json`（散植地物）
    - `feature_rules`
        - `wiki_overworld_surface_blocks_feature.json`
///

## 单方块地物

单方块地物是斑块的基本构成单元，每个文件定义一种要放置的方块。通过`may_replace`字段限制方块只能替换草方块，确保地物仅在地表生成，而不深入地下。

```json title="BP/features/wiki_coarse_dirt_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:coarse_dirt_feature"
        },
        "places_block": {
            "name": "minecraft:dirt",
            "states": {
                "dirt_type": "coarse"
            }
        },
        "enforce_survivability_rules": false,
        "enforce_placement_rules": false,
        "may_replace": ["minecraft:grass"]
    }
}
```

/// note | 灰化土的写法
灰化土（Coarse Dirt）与普通泥土共用`minecraft:dirt`标识符，需要通过方块状态`dirt_type: "coarse"`来区分。其他无特殊状态的方块可以直接用字符串标识符。
///

```json title="BP/features/wiki_podzol_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:podzol_feature"
        },
        "places_block": "minecraft:podzol",
        "enforce_survivability_rules": false,
        "enforce_placement_rules": false,
        "may_replace": ["minecraft:grass"]
    }
}
```

```json title="BP/features/wiki_cobblestone_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:cobblestone_feature"
        },
        "places_block": "minecraft:cobblestone",
        "enforce_survivability_rules": false,
        "enforce_placement_rules": false,
        "may_replace": ["minecraft:grass"]
    }
}
```

## 加权随机地物

加权随机地物将三种单方块地物以指定权重混合，游戏每次放置时随机从中选取一种：

```json title="BP/features/wiki_select_surface_block_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:weighted_random_feature": {
        "description": {
            "identifier": "wiki:select_surface_block_feature"
        },
        "features": [
            ["wiki:coarse_dirt_feature", 5],
            ["wiki:podzol_feature", 3],
            ["wiki:cobblestone_feature", 2]
        ]
    }
}
```

权重总和为10，因此灰化土占50%、灰化泥炭占30%、圆石占20%。权重不必是整数或特定总和，只有比例关系起作用。

## 散植地物（斑块形状）

散植地物控制斑块的尺寸、形状和方块数量：

```json title="BP/features/wiki_scatter_surface_block_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:scatter_feature": {
        "description": {
            "identifier": "wiki:scatter_surface_block_feature"
        },
        "iterations": "math.random_integer(20, 25)",
        "x": {
            "extent": [0, 8],
            "distribution": "gaussian"
        },
        "z": {
            "extent": [0, 8],
            "distribution": "gaussian"
        },
        "y": "q.heightmap(v.worldx, v.worldz) - 1",
        "places_feature": "wiki:select_surface_block_feature"
    }
}
```

/// define
`iterations`

- 每次散植尝试放置的方块数。此处使用`math.random_integer(20, 25)`随机选取20至25。

`x`/`z`的`extent`

- 斑块在XZ平面的尺寸。`[0, 8]`表示在原点周围±8范围内分布，形成16×16大小的斑块区域。

`distribution: "gaussian"`

- 高斯分布使方块在斑块中心更密集，向外逐渐稀疏，产生自然的边缘渐变效果。

`y`

- `q.heightmap(v.worldx, v.worldz) - 1`将每个方块放置在该列最高实体方块下方一格，即草方块所在层，确保每个方块都精确落在地表。

///

## 地物规则

地物规则控制斑块出现的频率和范围：

```json title="BP/feature_rules/wiki_overworld_surface_blocks_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:overworld_surface_blocks_feature",
            "places_feature": "wiki:scatter_surface_block_feature"
        },
        "conditions": {
            "placement_pass": "surface_pass",
            "minecraft:biome_filter": {
                "test": "has_biome_tag",
                "operator": "==",
                "value": "overworld"
            }
        },
        "distribution": {
            "iterations": 1,
            "x": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "y": 0,
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 5
            }
        }
    }
}
```

`placement_pass`使用`surface_pass`以在地表地物生成阶段运行。`scatter_chance`设置为1/5，即每个区块有20%的概率生成一个斑块。

## 调参参考

| 参数 | 作用 |
| --- | --- |
| `iterations`（散植地物） | 斑块内的方块数量 |
| `x`/`z` `extent` | 斑块在XZ方向的扩展范围 |
| `distribution` | `gaussian`产生中心密集斑块；`uniform`产生均匀分布 |
| `scatter_chance` | 每区块斑块出现的概率 |
| 加权随机地物的权重 | 各种方块的相对出现频率 |

若要将斑块限定在特定生物群系（如仅在平原），可将`has_biome_tag`的`value`改为`"plains"`。