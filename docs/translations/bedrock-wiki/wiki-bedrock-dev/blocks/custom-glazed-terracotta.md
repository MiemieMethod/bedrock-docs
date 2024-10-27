---
title: 自定义釉面陶瓦
category: 原版重建
tags:
    - 简单
mentions:
    - Kaioga5
    - QuazChick
description: 原版釉面陶瓦的重建。
---

::: tip 格式 & 最低引擎版本 `1.21.40`
本教程假设您对方块有基本的了解。
在开始之前，请查看[方块指南](../blocks/blocks-intro.md)。
:::

## 介绍

釉面陶瓦具有独特的旋转机制，使玩家能够为墙壁、地板和天花板制作美观的图案。本指南将指导您创建自己的类似釉面陶瓦的方块。

## 自定义釉面陶瓦

这将创建一个类似原版的自定义釉面陶瓦。

<CodeHeader>BP/blocks/custom_glazed_terracotta.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:glazed_terracotta_template",
            "menu_category": {
                "category": "construction",
                "group": "itemGroup.name.glazedTerracotta"
            },
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"]
                }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'north'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 0, 0] },
                    "minecraft:geometry": {
                        "identifier": "geometry.glazed_terracotta",
                        "bone_visibility": {
                            "bottom_1": false,
                            "bottom_2": false,
                            "bottom_3": false,
                            "bottom_4": true
                        }
                    }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'west'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 90, 0] },
                    "minecraft:geometry": {
                        "identifier": "geometry.glazed_terracotta",
                        "bone_visibility": {
                            "bottom_1": false,
                            "bottom_2": false,
                            "bottom_3": true,
                            "bottom_4": false
                        }
                    }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'south'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 180, 0] },
                    "minecraft:geometry": {
                        "identifier": "geometry.glazed_terracotta",
                        "bone_visibility": {
                            "bottom_1": false,
                            "bottom_2": true,
                            "bottom_3": false,
                            "bottom_4": false
                        }
                    }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'east'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, -90, 0] },
                    "minecraft:geometry": {
                        "identifier": "geometry.glazed_terracotta",
                        "bone_visibility": {
                            "bottom_1": true,
                            "bottom_2": false,
                            "bottom_3": false,
                            "bottom_4": false
                        }
                    }
                }
            }
        ],
        "components": {
            "minecraft:geometry": {
                "identifier": "geometry.glazed_terracotta"
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "purple_glazed_terracotta",
                    "render_method": "opaque"
                }
            }
        }
    }
}
```

## 几何体

原版釉面陶瓦以特定的值旋转方块的某些面，这就是赋予方块魔力的原因。使用以下几何体来复制该行为。

<Spoiler title="几何体 JSON">
  
<CodeHeader>RP/models/blocks/glazed_terracotta.geo.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.glazed_terracotta",
                "texture_width": 16,
                "texture_height": 16
            },
            "bones": [
                {
                    "name": "glazed_terracotta",
                    "pivot": [0, 0, 0]
                },
                {
                    "name": "top",
                    "parent": "glazed_terracotta",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 16, 16],
                            "uv": {
                                "up": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "north",
                    "parent": "glazed_terracotta",
                    "pivot": [0, 8, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 16, 0],
                            "pivot": [0, 8, 0],
                            "rotation": [180, 0, 90],
                            "uv": {
                                "north": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "south",
                    "parent": "glazed_terracotta",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [0, -8, 8],
                            "size": [16, 16, 0],
                            "pivot": [0, 0, 0],
                            "rotation": [180, 0, 270],
                            "uv": {
                                "south": { "uv": [0, 0], "uv_size": [16, 16] }
                            }
                        }
                    ]
                },
                {
                    "name": "east",
                    "parent": "glazed_terracotta",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, -16, -8],
                            "size": [0, 16, 16],
                            "pivot": [0, 0, 0],
                            "rotation": [0, 0, -180],
                            "uv": {
                                "east": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "west",
                    "parent": "glazed_terracotta",
                    "pivot": [-16, 0, 0],
                    "cubes": [
                        {
                            "origin": [-24, 0, -8],
                            "size": [0, 16, 16],
                            "pivot": [-16, 0, 0],
                            "rotation": [0, 180, 0],
                            "uv": {
                                "west": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "bottom",
                    "parent": "glazed_terracotta",
                    "pivot": [0, 0, 0]
                },
                {
                    "name": "bottom_1",
                    "parent": "bottom",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 0, 16],
                            "uv": {
                                "down": { "uv": [0, 0], "uv_size": [16, 16] }
                            }
                        }
                    ]
                },
                {
                    "name": "bottom_2",
                    "parent": "bottom",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 0, 16],
                            "uv": {
                                "down": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "bottom_3",
                    "parent": "bottom",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 0, 16],
                            "uv": {
                                "down": { "uv": [0, 0], "uv_size": [16, 16] }
                            }
                        }
                    ]
                },
                {
                    "name": "bottom_4",
                    "parent": "bottom",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 0, 16],
                            "uv": {
                                "down": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```

</Spoiler>