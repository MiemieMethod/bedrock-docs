# 使用噪声高度图生成地形

本教程使用`q.noise`查询函数与散植地物（`scatter_feature`）结合，实现基于柏林噪声的连续地形生成效果。与直接修改生物群系的高度参数不同，本方案通过方块列生成来构造地表形态，适合用于在特定生物群系中叠加自定义地形变化。

/// note | 前置知识
本教程需要你对Molang表达式、地物（feature）和地物规则（feature rule）有基本了解。
///

/// note | 实验性玩法
本教程涉及的功能需要在世界设置中启用"自定义生物群系"实验性玩法开关。
///

## 原理说明

`q.noise(x, z)`是Minecraft提供的柏林噪声查询函数，返回值范围约为-1至1。与完全随机值不同，相邻坐标的噪声值会平滑过渡，这使其非常适合用于地形生成。

本教程的核心思路是：通过散植地物在每个区块的每一列（16×16 = 256列）上放置一根方块柱，柱的高度由该列坐标的噪声值决定。柱内每一个Y坐标都会放置一个单方块地物。

## 文件结构

/// html | div.treeview
- `demo_BP`
    - `features`
        - `wiki_stone_feature.json`（单方块地物）
        - `wiki_column_feature.json`（散植地物，生成方块柱）
    - `feature_rules`
        - `wiki_column_grid_placement.json`（地物规则）
///

## 单方块地物

首先定义构成方块柱的单个方块：

```json title="BP/features/wiki_stone_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:single_block_feature": {
        "description": {
            "identifier": "wiki:stone_feature"
        },
        "places_block": "minecraft:stone",
        "enforce_survivability_rules": false,
        "enforce_placement_rules": false
    }
}
```

关闭`enforce_survivability_rules`和`enforce_placement_rules`可以确保方块在任意位置放置，不受方块生存规则的限制。

## 散植地物（方块柱）

散植地物是本技术的关键部分，它控制方块柱的高度和形态：

```json title="BP/features/wiki_column_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:scatter_feature": {
        "description": {
            "identifier": "wiki:column"
        },
        "iterations": "t.height = 64 + (q.noise(v.originz / 64, v.originx / 64)) * 16; return t.height;",
        "places_feature": "wiki:stone_feature",
        "x": 0,
        "z": 0,
        "y": {
            "extent": [-64, "t.height"],
            "distribution": "fixed_grid"
        }
    }
}
```

### `iterations`字段解析

`iterations`字段计算本次散植尝试放置的次数，即方块柱的高度。这里使用了Molang临时变量：

1. `t.height = 64 + (q.noise(v.originz / 64, v.originx / 64)) * 16`：
   - `64`是基础高度（基准地表Y坐标）
   - `q.noise(v.originz / 64, v.originx / 64)`返回-1至1的噪声值，除以64是为了在更大范围内平滑采样，使地形起伏更加平缓
   - `* 16`是高度变化幅度，乘以16意味着地形高度在基础高度±16范围内波动
2. `return t.height`：将计算出的高度值作为迭代次数

### Y轴分布

`y.extent`设置为`[-64, "t.height"]`，配合`fixed_grid`分布，确保从Y=-64到`t.height`的每一个Y坐标都放置一个方块，形成连续的方块柱。

### 地图坐标

`x`和`z`固定为0，意味着整根方块柱都位于由地物规则传入的原点坐标处。

## 地物规则

地物规则确保每个区块的16×16列都被覆盖：

```json title="BP/feature_rules/wiki_column_grid_placement.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:column_grid_placement",
            "places_feature": "wiki:column"
        },
        "conditions": {
            "placement_pass": "first_pass",
            "minecraft:biome_filter": {
                "any_of": [
                    {
                        "test": "has_biome_tag",
                        "value": "overworld"
                    },
                    {
                        "test": "has_biome_tag",
                        "value": "overworld_generation"
                    }
                ]
            }
        },
        "distribution": {
            "iterations": 256,
            "x": {
                "extent": [0, 15],
                "distribution": "fixed_grid"
            },
            "y": 0,
            "z": {
                "extent": [0, 15],
                "distribution": "fixed_grid"
            }
        }
    }
}
```

`iterations`设置为256（16×16），配合`fixed_grid`分布，确保区块内每一列坐标（x, z从0到15）各被尝试一次。`placement_pass`使用`first_pass`以在基础地形生成最早阶段运行。

## 调参参考

| 参数 | 作用 | 建议范围 |
| --- | --- | --- |
| 基础高度（`64`） | 地形整体高度偏移 | 根据生物群系调整 |
| 采样间隔（`/ 64`） | 值越大地形越平缓，越小越起伏剧烈 | `32`至`128` |
| 高度幅度（`* 16`） | 地形起伏的垂直范围 | `8`至`64` |
| `y.extent`最小值（`-64`） | 方块柱的底部，通常设为世界底部 | 不低于`-64` |

## 注意事项

- 本技术是在原有地形上叠加方块柱，会与自然地形重叠。如果需要替换地形，需结合其他地物或调整生物群系的高度参数。
- `q.noise`的采样坐标除以较大的值（如64）可使地形更平缓；若想要更锯齿化的地形，可减小该值（如`/ 16`）。
- 若只想在特定生物群系中生成，将`has_biome_tag`的`value`改为对应的标签即可，例如`"desert"`或`"ocean"`。
