# 生成自定义矿石

矿石地物（`ore_feature`）是世界生成中最基础也最重要的地物类型之一。它通过替换指定方块来生成矿脉形态的方块集群。本教程将演示如何让自定义方块以矿石形式自然生成于世界中。

/// note | 实验性玩法
使用地物和地物规则需要在世界设置中启用"自定义生物群系"实验性玩法开关。若你的矿石没有生成，请先确认此开关已开启。
///

## 文件结构

自定义矿石需要两个文件：

/// html | div.treeview
- `demo_BP`
    - `features`
        - `titanite_ore_feature.json`（地物定义）
    - `feature_rules`
        - `overworld_underground_titanite_ore_feature.json`（地物规则）
///

## 地物文件

地物文件定义矿脉的组成方式：将哪种方块放置到哪些方块位置。

```json title="BP/features/titanite_ore_feature.json"
{
    "format_version": "1.17.0",
    "minecraft:ore_feature": {
        "description": {
            "identifier": "wiki:titanite_ore_feature"
        },
        "count": 8,
        "replace_rules": [
            {
                "places_block": "wiki:titanite_ore",
                "may_replace": ["minecraft:stone"]
            },
            {
                "places_block": "wiki:deepslate_titanite_ore",
                "may_replace": ["minecraft:deepslate"]
            }
        ]
    }
}
```

/// define
`count`

- 每次矿脉尝试放置的方块数量上限。

`replace_rules`

- 替换规则列表。规则按顺序匹配：对于矿脉中的每个位置，游戏依次尝试各条规则，找到第一条`may_replace`列表包含该位置方块的规则，并用`places_block`替换之。

`places_block`

- 要放置的方块。可以是方块标识符字符串，或包含`name`和`states`的对象。

`may_replace`

- 允许被替换的方块列表。若某位置的方块不在列表中，该位置跳过。

///

## 地物规则文件

地物规则控制矿石在哪个生物群系、哪个高度范围、以多大密度生成：

```json title="BP/feature_rules/overworld_underground_titanite_ore_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:overworld_underground_titanite_ore_feature",
            "places_feature": "wiki:titanite_ore_feature"
        },
        "conditions": {
            "placement_pass": "underground_pass",
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
            "iterations": 10,
            "coordinate_eval_order": "zyx",
            "x": {
                "distribution": "uniform",
                "extent": [0, 16]
            },
            "y": {
                "distribution": "uniform",
                "extent": [0, 62]
            },
            "z": {
                "distribution": "uniform",
                "extent": [0, 16]
            }
        }
    }
}
```

/// define
`placement_pass`

- 地物放置阶段。矿石通常使用`underground_pass`。

`iterations`

- 每个区块尝试放置矿脉的次数。每次尝试会随机选取一个位置放置整个矿脉。注意：`iterations`是矿脉数量，而`count`是每个矿脉的方块数量。

`distribution`

- `uniform`：在`extent`范围内均匀分布。
- `triangle`：三角分布，使矿石在范围中间更常见、两端更稀少，适合模拟钻石矿等集中在某深度的矿石。

`extent`

- `[最小值, 最大值]`范围。Y轴的`extent`即矿石的高度范围。

///

/// tip | 调整Y轴范围
`y.extent`的值是绝对Y坐标，而非相对地表的深度。主世界的地层从Y=-64开始，石头主要分布在Y=-64至Y=128之间，深板岩层大约在Y=-64至Y=0。若要模拟钻石矿，可设置`extent: [-64, 16]`并使用`triangle`分布让矿石集中在深层。
///

## 测试方法

矿石生成于地下，普通探索可能较难发现。可以使用以下命令快速验证矿石是否正常生成：

```
execute at @a run fill ~8 ~8 ~8 ~-8 ~-8 ~-8 air replace wiki:titanite_ore
```

在低Y坐标区域执行此命令，它会将选定范围内所有钛石矿石替换为空气，从而让你看到矿石是否出现在该区域。

## 深层矿石示例

如需让矿石仅在深板岩层生成，可修改规则如下：

```json
"distribution": {
    "iterations": 8,
    "coordinate_eval_order": "zyx",
    "x": {
        "distribution": "uniform",
        "extent": [0, 16]
    },
    "y": {
        "distribution": "triangle",
        "extent": [-64, 0]
    },
    "z": {
        "distribution": "uniform",
        "extent": [0, 16]
    }
}
```

`triangle`分布使矿石在Y=-32附近最密集，向上下两端逐渐减少，与钻石矿的分布规律相似。