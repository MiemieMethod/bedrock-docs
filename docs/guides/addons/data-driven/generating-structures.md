# 通过结构模板地物生成结构

结构模板地物（`structure_template_feature`）是将`.mcstructure`文件放置入世界的最基础方式。本教程涵盖五种常见的结构放置场景：地表结构、地下结构、漂浮结构、水下结构与水面结构。

/// note | 实验性玩法
本教程涉及的功能需要在世界设置中启用"自定义生物群系"实验性玩法开关。
///

/// warning | Android设备
从基岩版1.21.130起，Android设备无法导出`.mcstructure`文件。
///

## 准备结构文件

将`.mcstructure`文件放置在行为包的`structures/`目录中。第一层子文件夹名作为命名空间，例如`BP/structures/wiki/house.mcstructure`的结构名称为`wiki:house`。

/// tip | 拼图结构
若需要支持`/locate structure`命令的复杂多段结构，请参阅[生成拼图结构](jigsaw-structures.md)。
///

## 地表结构

地表结构生成在地面上，如房屋、村庄等。

```json title="BP/features/wiki_house_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:structure_template_feature": {
        "description": {
            "identifier": "wiki:house_feature"
        },
        "structure_name": "wiki:house",
        "adjustment_radius": 4,
        "facing_direction": "random",
        "constraints": {
            "grounded": {},
            "unburied": {},
            "block_intersection": {
                "block_allowlist": ["minecraft:air"]
            }
        }
    }
}
```

/// define
`adjustment_radius`

- 放置时允许的Y轴调整范围（方块数）。游戏在该半径内寻找合适的放置高度以使结构贴合地形。值越大结构对不规则地形的适应性越强。

`facing_direction`

- 结构朝向。`random`表示随机旋转，可选值包括`north`、`south`、`east`、`west`。

`constraints.grounded`

- 要求结构底部与地面接触，防止结构悬空。

`constraints.unburied`

- 要求结构顶部不被方块覆盖，防止结构被埋入地下。

`constraints.block_intersection.block_allowlist`

- 结构允许替换的方块列表。设为`minecraft:air`则结构只会放置在空气中，不会切割地形。

///

```json title="BP/feature_rules/wiki_plains_house_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:plains_house_feature",
            "places_feature": "wiki:house_feature"
        },
        "conditions": {
            "placement_pass": "first_pass",
            "minecraft:biome_filter": {
                "test": "has_biome_tag",
                "operator": "==",
                "value": "plains"
            }
        },
        "distribution": {
            "iterations": 1,
            "x": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "y": "q.heightmap(v.worldx, v.worldz)",
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 25
            }
        }
    }
}
```

`y`使用`q.heightmap`将地物的起始Y坐标设为该列最高实体方块的高度，结合`adjustment_radius`可以使结构贴合地表。`scatter_chance`设为1/25，每区块约4%概率尝试生成。

## 地下结构

地下结构（如地下掩体、矿洞房间等）需要去掉`grounded`和`unburied`约束，并在`block_allowlist`中允许石头等地下方块：

```json title="BP/features/wiki_bunker_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:structure_template_feature": {
        "description": {
            "identifier": "wiki:bunker_feature"
        },
        "structure_name": "wiki:bunker",
        "adjustment_radius": 4,
        "facing_direction": "random",
        "constraints": {
            "block_intersection": {
                "block_allowlist": ["minecraft:air", "minecraft:stone"]
            }
        }
    }
}
```

```json title="BP/feature_rules/wiki_overworld_bunker_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:overworld_bunker_feature",
            "places_feature": "wiki:bunker_feature"
        },
        "conditions": {
            "placement_pass": "first_pass",
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
            "y": {
                "extent": [11, 50],
                "distribution": "uniform"
            },
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 15
            }
        }
    }
}
```

`y.extent`固定在`[11, 50]`之间，将结构限制在Y坐标11至50的深度范围内。

## 漂浮结构

漂浮结构（如空中岛屿、飞行船等）需要将Y轴设在地表之上：

```json title="BP/features/wiki_balloon_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:structure_template_feature": {
        "description": {
            "identifier": "wiki:balloon_feature"
        },
        "structure_name": "wiki:balloon",
        "adjustment_radius": 4,
        "facing_direction": "random",
        "constraints": {
            "block_intersection": {
                "block_allowlist": ["minecraft:air"]
            }
        }
    }
}
```

```json title="BP/feature_rules/wiki_overworld_balloon_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:overworld_balloon_feature",
            "places_feature": "wiki:balloon_feature"
        },
        "conditions": {
            "placement_pass": "first_pass",
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
            "y": {
                "extent": [100, 200],
                "distribution": "uniform"
            },
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 25
            }
        }
    }
}
```

将`y.extent`设为`[100, 200]`，使结构生成在云层高度附近。

## 水下结构

/// warning | 含水处理
Minecraft不会自动对水下结构含水。导出前需手动将结构中所有应含水的方块设为含水状态，否则结构会将水排走，形成空腔。
///

水下结构需要将`block_allowlist`设为`minecraft:water`，并使用`q.above_top_solid`将Y轴定位到水面以下的最高实体方块处：

```json title="BP/features/wiki_aqua_temple_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:structure_template_feature": {
        "description": {
            "identifier": "wiki:aqua_temple_feature"
        },
        "structure_name": "wiki:aqua_temple",
        "adjustment_radius": 4,
        "facing_direction": "random",
        "constraints": {
            "block_intersection": {
                "block_allowlist": ["minecraft:water"]
            }
        }
    }
}
```

```json title="BP/feature_rules/wiki_ocean_aqua_temple_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:ocean_aqua_temple_feature",
            "places_feature": "wiki:aqua_temple_feature"
        },
        "conditions": {
            "placement_pass": "first_pass",
            "minecraft:biome_filter": {
                "test": "has_biome_tag",
                "operator": "==",
                "value": "ocean"
            }
        },
        "distribution": {
            "iterations": 1,
            "x": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "y": "q.above_top_solid(v.worldx, v.worldz)",
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 25
            }
        }
    }
}
```

`q.above_top_solid(v.worldx, v.worldz)`返回该列最高实体方块上方一格的Y坐标（水面以下），避免结构生成在水面上。

## 水面结构

水面结构（如木筏、浮岛等）需要`block_allowlist`同时包含`minecraft:water`和`minecraft:air`，并将Y轴固定在水面高度：

```json title="BP/features/wiki_raft_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:structure_template_feature": {
        "description": {
            "identifier": "wiki:raft_feature"
        },
        "structure_name": "wiki:raft",
        "adjustment_radius": 4,
        "facing_direction": "random",
        "constraints": {
            "block_intersection": {
                "block_allowlist": ["minecraft:water", "minecraft:air"]
            }
        }
    }
}
```

```json title="BP/feature_rules/wiki_ocean_raft_feature.json"
{
    "format_version": "1.13.0",
    "minecraft:feature_rules": {
        "description": {
            "identifier": "wiki:ocean_raft_feature",
            "places_feature": "wiki:raft_feature"
        },
        "conditions": {
            "placement_pass": "first_pass",
            "minecraft:biome_filter": {
                "test": "has_biome_tag",
                "operator": "==",
                "value": "ocean"
            }
        },
        "distribution": {
            "iterations": 1,
            "x": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "y": 62,
            "z": {
                "extent": [0, 16],
                "distribution": "uniform"
            },
            "scatter_chance": {
                "numerator": 1,
                "denominator": 25
            }
        }
    }
}
```

将`y`固定为`62`（主世界默认水面高度），使结构恰好生成在水面处。

## 各场景对比

| 场景 | `constraints` | Y轴设置 | `block_allowlist` |
| --- | --- | --- | --- |
| 地表结构 | `grounded`+`unburied` | `q.heightmap` | `air` |
| 地下结构 | 无特殊约束 | 固定范围 | `air`, `stone`等 |
| 漂浮结构 | 无特殊约束 | 高Y固定范围 | `air` |
| 水下结构 | 无特殊约束 | `q.above_top_solid` | `water` |
| 水面结构 | 无特殊约束 | 固定为62 | `water`, `air` |
