---
title: 自定义活板门
description: 重新创建原版活板门。
category: 原版重建
tags:
    - 中级
    - 脚本编写
mentions:
    - Kaioga5
    - QuazChick
    - SmokeyStack
---

::: tip 格式 & 最小引擎版本 `1.21.40`
本教程假设你对方块有良好的理解，并具备基本的脚本知识。
在开始之前，请查看[方块指南](../blocks/blocks-intro.md)。
:::

活板门是多功能方块，适合作为门、栅栏、装饰的一部分，当然——也可以作为活板门！难怪你想制作自己的活板门，以丰富Minecraft的方块库。以下是制作方法：

## 方块 JSON

这是你需要的基本活板门功能的方块 JSON。它包含了活板门每种排列的旋转信息，意味着它可以以与原版活板门相同的方向放置。

<CodeHeader>BP/blocks/custom_trapdoor.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_trapdoor",
            "menu_category": {
                "category": "construction",
                "group": "itemGroup.name.trapdoor"
            },
            "states": {
                "wiki:open": [false, true]
            },
            "traits": {
                "minecraft:placement_position": {
                    "enabled_states": ["minecraft:vertical_half"]
                },
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"]
                }
            }
        },
        "components": {
            "minecraft:custom_components": ["wiki:custom_trapdoor"],
            "minecraft:collision_box": {
                "origin": [-8, 0, -8],
                "size": [16, 3, 16]
            },
            "tag:one_way_collidable": {}, // 防止玩家被活板门碰撞推开，类似于原版
            "minecraft:selection_box": {
                "origin": [-8, 0, -8],
                "size": [16, 3, 16]
            },
            "minecraft:geometry": "geometry.trapdoor",
            "minecraft:material_instances": {
                "*": {
                    "texture": "acacia_trapdoor",
                    "render_method": "alpha_test_single_sided"
                }
            }
        },
        "permutations": [
            // 顶部关闭
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'north' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 0, 180] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'south' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [180, 0, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'east' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [180, -270, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'west' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [180, 270, 0] }
                }
            },
            // 顶部打开
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'north' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [-270, 0, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'south' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [270, 0, -180] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'east' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 270, 90] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && q.block_state('minecraft:cardinal_direction') == 'west' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [180, -270, -270] }
                }
            },
            // 底部关闭
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'north' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 0, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'south' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 180, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'east' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 270, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'west' && !q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, -270, 0] }
                }
            },
            // 底部打开
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'north' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [90, 0, 180] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'south' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [270, 0, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'east' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [0, -270, 90] }
                }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && q.block_state('minecraft:cardinal_direction') == 'west' && q.block_state('wiki:open')",
                "components": {
                    "minecraft:transformation": { "rotation": [180, 270, -270] }
                }
            }
        ]
    }
}
```

## 自定义组件脚本

现在，是时候将这些排列付诸实践了。以下脚本将允许玩家通过与活板门交互来打开和关闭它。别忘了将此脚本导入到你的主脚本入口中。

<CodeHeader>BP/scripts/custom_trapdoor.js</CodeHeader>

```js
import { world } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const CustomTrapdoorBlockComponent = {
    onPlayerInteract({ block, dimension }) {
        const isOpen = block.permutation.getState("wiki:open");
        const sound = isOpen ? "close.wooden_trapdoor" : "open.wooden_trapdoor";

        block.setPermutation(block.permutation.withState("wiki:open", !isOpen));

        dimension.playSound(sound, block.center(), {
            pitch: 0.9,
            volume: 0.9,
        });
    },
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:custom_trapdoor",
        CustomTrapdoorBlockComponent
    );
});
```

## 方块模型

这将是你自定义活板门使用的几何体。

<Spoiler title="几何 JSON">
  
<CodeHeader>RP/models/blocks/trapdoor.geo.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.trapdoor",
                "texture_width": 16,
                "texture_height": 16
            },
            "bones": [
                {
                    "name": "trapdoor",
                    "pivot": [0, 0, 0],
                    "cubes": [
                        {
                            "origin": [-8, 0, -8],
                            "size": [16, 3, 16],
                            "uv": {
                                "north": { "uv": [16, 3], "uv_size": [-16, -3] },
                                "east": { "uv": [16, 3], "uv_size": [-16, -3] },
                                "south": { "uv": [16, 3], "uv_size": [-16, -3] },
                                "west": { "uv": [16, 3], "uv_size": [-16, -3] },
                                "up": { "uv": [16, 16], "uv_size": [-16, -16] },
                                "down": { "uv": [0, 0], "uv_size": [16, 16] }
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

:::tip
原版活板门在某些面上的纹理方向存在一些问题，并且高度为2.95，而应该为3。此方块模板和几何体修复了这两个问题。
:::