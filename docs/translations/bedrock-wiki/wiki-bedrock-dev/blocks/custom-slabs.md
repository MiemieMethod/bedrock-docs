---
title: 自定义半砖
category: 原版重建
tags:
    - 实验性
    - 简单
mentions:
    - Kaioga5
    - QuazChick
    - SmokeyStack
hidden: true
description: 原版半砖的重建。
---

::: tip 格式与最低引擎版本 `1.21.40`
本教程假设你对方块有基本的了解。
在开始之前，请查看[方块指南](../blocks/blocks-intro.md)。
:::

## 介绍

制作自定义半砖是一项简单的任务，但如果在重建半砖时遇到任何问题，本教程将为你提供帮助，并提供一个模板供你使用。

问题：

- 你的自定义半砖在携带时会垂直居中显示。
- 你的自定义半砖在物品形式下（在地面、物品框中、手中）可能会显示为完整大小。

## 自定义半砖

这将创建一个类似于原版的自定义半砖。

<CodeHeader>BP/blocks/custom_slab.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "components": {
            "minecraft:destructible_by_explosion": {
                "explosion_resistance": 30
            },
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 2
            },
            "minecraft:geometry": {
                "bone_visibility": {
                    "bottom": "q.block_state('minecraft:vertical_half') == 'bottom' || q.block_state('wiki:is_double')",
                    "top": "q.block_state('minecraft:vertical_half') == 'top' || q.block_state('wiki:is_double')"
                },
                "identifier": "geometry.slab"
            },
            "minecraft:map_color": [229, 229, 51],
            "minecraft:material_instances": {
                "*": {
                    "texture": "honeycomb_bricks"
                },
                "ends": {
                    "texture": ""
                }
            }
        },
        "description": {
            "identifier": "wiki:honeycomb_bricks_slab",
            "menu_category": {
                "category": "construction",
                "group": "itemGroup.name.slab"
            },
            "states": {
                "wiki:is_double": [false, true]
            },
            "traits": {
                "minecraft:placement_position": {
                    "enabled_states": ["minecraft:vertical_half"]
                }
            }
        },
        "permutations": [
            {
                "components": {
                    "minecraft:collision_box": {
                        "origin": [-8, 0, -8],
                        "size": [16, 8, 16]
                    },
                    "minecraft:custom_components": ["adk-lib:before_on_player_place_double_slab"],
                    "minecraft:selection_box": {
                        "origin": [-8, 0, -8],
                        "size": [16, 8, 16]
                    }
                },
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && !q.block_state('wiki:is_double')"
            },
            {
                "components": {
                    "minecraft:collision_box": {
                        "origin": [-8, 8, -8],
                        "size": [16, 8, 16]
                    },
                    "minecraft:custom_components": ["adk-lib:before_on_player_place_double_slab"],
                    "minecraft:selection_box": {
                        "origin": [-8, 8, -8],
                        "size": [16, 8, 16]
                    }
                },
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && !q.block_state('wiki:is_double')"
            },
            {
                "components": {
                    "minecraft:loot": "loot_tables/wiki/blocks/honeycomb_bricks_slab.json"
                },
                "condition": "q.block_state('wiki:is_double')"
            }
        ]
    }
}
```

## 几何体

这将是你自定义半砖使用的几何体。

<Spoiler title="几何体 JSON">
  
<CodeHeader>RP/models/blocks/slab.geo.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.slab",
                "texture_width": 16,
                "texture_height": 16,
                "visible_bounds_width": 2,
                "visible_bounds_height": 2.5,
                "visible_bounds_offset": [0, 0.75, 0]
            },
            "bones": [
                {
                    "name": "root",
                    "pivot": [0, 0, 0]
                },
                {
                    "name": "bottom",
                    "parent": "root",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 8, 16],
                            "uv": {
                                "north": { "uv": [0, 8], "uv_size": [16, 8] },
                                "east": { "uv": [0, 8], "uv_size": [16, 8] },
                                "south": { "uv": [0, 8], "uv_size": [16, 8] },
                                "west": { "uv": [0, 8], "uv_size": [16, 8] },
                                "up": { "uv": [16, 16], "uv_size": [-16, -16] },
                                "down": { "uv": [16, 16], "uv_size": [-16, -16] }
                            }
                        }
                    ]
                },
                {
                    "name": "top",
                    "parent": "root",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 8, -8],
                            "size": [16, 8, 16],
                            "uv": {
                                "north": { "uv": [0, 8], "uv_size": [16, 8] },
                                "east": { "uv": [0, 8], "uv_size": [16, 8] },
                                "south": { "uv": [0, 8], "uv_size": [16, 8] },
                                "west": { "uv": [0, 8], "uv_size": [16, 8] },
                                "up": { "uv": [16, 16], "uv_size": [-16, -16] },
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