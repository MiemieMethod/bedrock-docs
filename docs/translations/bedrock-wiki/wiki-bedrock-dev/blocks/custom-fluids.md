---
title: 自定义流体
category: 原版重现
tags:
    - 实验性
    - 中级
    - 脚本编写
mentions:
    - Provedule
    - JaylyDev
    - QuazChick
    - SmokeyStack
description: 重现原版流体。
hidden: true
---

::: tip 格式 & 最低引擎版本 `1.21.40`
本教程假设你对方块和执行命令有高级理解。
在开始之前，请查看[方块指南](../blocks/blocks-intro.md)。
:::

::: warning 实验性
需要使用 `Holiday Creator Features` 以使用方块标签 Molang 查询和触发方块事件。

需要 `Beta APIs` 以使用 [@minecraft/server](https://learn.microsoft.com/minecraft/creator/scriptapi/minecraft/server/minecraft-server) 模块版本 `1.6.0-beta`。
:::

创建与原版流体完全相同的流体目前还不可能，但你可以制作类似的东西！此模板/教程旨在帮助你创建自定义的“半流体”。

## 流动逻辑

- 流体方块具有定义其是否为源以及其深度的状态。
- 如果流体方块下方有空气，它将被转换为下落流体。
- 深度大于 `1` 的流体将水平扩散，深度逐渐减小。
    - 如果下方有下落流体，则不会发生此情况。
- 流动流体方块必须有相邻的另一个流体方块才能存活。
- 源方块不需要周围有其他流体方块。

**由于当前复杂性，此实现不包括面剔除。**

<WikiImage
  src="../assets/images/blocks/custom-fluids/fluid_display.png"
  alt=""
  pixelated
  width=608
/>

## 源流体方块

以下是自定义流体的代码。将 `custom_fluid` 替换为你的流体名称。当源方块在周围检测到空气时，它将用外部流体方块替换。如果源方块在下方检测到空气，它还将在下方放置一个下落流体方块。

<Button link="https://github.com/Bedrock-OSS/wiki-addon/blob/main/ma-custom_fluids/rp/models/blocks/fluid.geo.json">
    下载自定义流体几何体
</Button>

<Spoiler title="自定义流体方块 JSON">

<CodeHeader>BP/blocks/custom_fluid.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_fluid",
            "menu_category": {
                "category": "none"
            },
            "states": {
                "wiki:source": [true, false],
                // 流体深度 - 默认值为 4
                "wiki:depth": [4, 5, 3, 2, 1]
            }
        },
        "components": {
            "minecraft:light_dampening": 0,
            "minecraft:collision_box": false,
            "minecraft:selection_box": false,
            "minecraft:destructible_by_explosion": false,
            // 触发流体扩散
            "minecraft:queued_ticking": {
                "looping": true,
                "interval_range": [20, 20], // 流体速度（以刻为单位）
                "on_tick": {
                    "event": "wiki:flow"
                }
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "custom_fluid", // 在 `RP/textures/terrain_texture.json` 中定义的简短名称
                    "render_method": "blend",
                    "ambient_occlusion": false,
                    "face_dimming": false
                }
            },
            "minecraft:loot": "loot_tables/empty.json",
            "tag:custom_fluid": {}
        },
        "events": {
            "wiki:flow": {
                "sequence": [
                    // 干燥
                    {
                        "condition": "!q.block_state('wiki:source') && ((q.block_state('wiki:depth') == 5 && !q.block_neighbor_has_any_tag(0, 1, 0, 'custom_fluid')) || (q.block_state('wiki:depth') == 1 && !(q.block_neighbor_has_any_tag(1, 0, 0, 'custom_fluid_2') || q.block_neighbor_has_any_tag(-1, 0, 0, 'custom_fluid_2') || q.block_neighbor_has_any_tag(0, 0, 1, 'custom_fluid_2') || q.block_neighbor_has_any_tag(0, 0, -1, 'custom_fluid_2')) || q.block_state('wiki:depth') == 2 && !(q.block_neighbor_has_any_tag(1, 0, 0, 'custom_fluid_3') || q.block_neighbor_has_any_tag(-1, 0, 0, 'custom_fluid_3') || q.block_neighbor_has_any_tag(0, 0, 1, 'custom_fluid_3') || q.block_neighbor_has_any_tag(0, 0, -1, 'custom_fluid_3'))) || (q.block_state('wiki:depth') == 3 && !(q.block_neighbor_has_any_tag(1, 0, 0, 'custom_fluid_4', 'custom_fluid_5') || q.block_neighbor_has_any_tag(-1, 0, 0, 'custom_fluid_4', 'custom_fluid_5') || q.block_neighbor_has_any_tag(0, 0, 1, 'custom_fluid_4', 'custom_fluid_5') || q.block_neighbor_has_any_tag(0, 0, -1, 'custom_fluid_4', 'custom_fluid_5'))))",
                        "die": {}
                    },
                    // 扩散
                    {
                        "condition": "q.block_state('wiki:depth') == 4",
                        "run_command": {
                            "command": [
                                "execute if block ~~~1 air run setblock ~~~1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute if block ~~~-1 air run setblock ~~~-1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute if block ~1~~ air run setblock ~1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute if block ~-1~~ air run setblock ~-1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]"
                            ]
                        }
                    },
                    {
                        "condition": "q.block_state('wiki:source') && q.block_neighbor_has_any_tag(0, 1, 0, 'custom_fluid')",
                        "set_block_state": {
                            "wiki:depth": 5
                        }
                    },
                    {
                        "condition": "q.block_state('wiki:source') && !q.block_neighbor_has_any_tag(0, 1, 0, 'custom_fluid')",
                        "set_block_state": {
                            "wiki:depth": 4
                        }
                    },
                    {
                        "condition": "q.block_state('wiki:depth') == 3",
                        "run_command": {
                            "command": [
                                "execute if block ~~~1 air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~~~1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=2]",
                                "execute if block ~~~-1 air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~~~-1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=2]",
                                "execute if block ~1~~ air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=2]",
                                "execute if block ~-1~~ air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~-1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=2]"
                            ]
                        }
                    },
                    {
                        "condition": "q.block_state('wiki:depth') == 2",
                        "run_command": {
                            "command": [
                                "execute if block ~~~1 air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~~~1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=1]",
                                "execute if block ~~~-1 air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~~~-1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=1]",
                                "execute if block ~1~~ air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=1]",
                                "execute if block ~-1~~ air unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid run setblock ~-1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=1]"
                            ]
                        }
                    },
                    {
                        "condition": "q.block_state('wiki:depth') == 5 && q.block_neighbor_has_any_tag(0, 1, 0, 'custom_fluid')",
                        "run_command": {
                            "command": [
                                "execute if block ~~-1~ wiki:custom_fluid [\"wiki:depth\"=3] run setblock ~~-1~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=5]",
                                "execute if block ~~-1~ wiki:custom_fluid [\"wiki:depth\"=2] run setblock ~~-1~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=5]",
                                "execute if block ~~-1~ wiki:custom_fluid [\"wiki:depth\"=1] run setblock ~~-1~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=5]",
                                "execute unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid if block ~1~~ air run setblock ~1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid if block ~~~1 air run setblock ~~~1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid if block ~-1~~ air run setblock ~-1~~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]",
                                "execute unless block ~~-1~ air unless block ~~-1~ wiki:custom_fluid if block ~~~-1 air run setblock ~~~-1 wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=3]"
                            ]
                        }
                    },
                    // 下落
                    {
                        "run_command": {
                            "command": "execute if block ~~-1~ air run setblock ~~-1~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=5]"
                        }
                    },
                    {
                        "condition": "q.block_neighbor_has_any_tag(0, -1, 0, 'flowing_custom_fluid')",
                        "run_command": {
                            "command": "setblock ~~-1~ wiki:custom_fluid [\"wiki:source\"=false,\"wiki:depth\"=5]"
                        }
                    }
                ]
            },
            "wiki:pick_up": {
                "die": {},
                "decrement_stack": {},
                "run_command": {
                    "command": "give @s lava_bucket",
                    "target": "other"
                }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:source')",
                "components": {
                    // 允许该方块被选择的物品拾取
                    "minecraft:selection_box": {
                        "origin": [-7.5, 0.5, -7.5],
                        "size": [15, 13, 15]
                    },
                    "tag:custom_fluid_source": {}
                }
            },
            {
                "condition": "!q.block_state('wiki:source')",
                "components": {
                    "tag:flowing_custom_fluid": {}
                }
            },
            {
                "condition": "q.block_state('wiki:depth') == 5",
                "components": {
                    "minecraft:geometry": "geometry.fluid.5",
                    "tag:custom_fluid_5": {}
                }
            },
            {
                "condition": "q.block_state('wiki:depth') == 4",
                "components": {
                    "minecraft:geometry": "geometry.fluid.4",
                    "tag:custom_fluid_4": {}
                }
            },
            {
                "condition": "q.block_state('wiki:depth') == 3",
                "components": {
                    "minecraft:geometry": "geometry.fluid.3",
                    "tag:custom_fluid_3": {}
                }
            },
            {
                "condition": "q.block_state('wiki:depth') == 2",
                "components": {
                    "minecraft:geometry": "geometry.fluid.2",
                    "tag:custom_fluid_2": {}
                }
            },
            {
                "condition": "q.block_state('wiki:depth') == 1",
                "components": {
                    "minecraft:geometry": "geometry.fluid.1",
                    "tag:custom_fluid_1": {}
                }
            }
        ]
    }
}
```

</Spoiler>

## 流体桶

要放置你的自定义流体，你需要一个自定义桶物品。以下是自定义桶的 JSON。将任何 `custom_fluid` 的实例替换为你的流体名称。

<Spoiler title="自定义桶物品 JSON">

<CodeHeader>BP/items/custom_fluid_bucket.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_fluid_bucket",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:max_stack_size": 1,
            "minecraft:icon": {
                "texture": "custom_fluid_bucket" // 在 `RP/textures/item_texture.json` 中定义的简短名称
            },
            "minecraft:block_placer": {
                "block": "wiki:custom_fluid"
            }
        }
    }
}
```

</Spoiler>

## 脚本

这些流体使用脚本来增加玩家在流体中漂浮/下沉的能力。脚本还增加了雾效。要将你的流体添加到脚本中，请将新流体的 ID 放入 `fluids` 字符串数组中。

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
  "modules": [
    ...
    {
      "type": "script",
      "language": "javascript",
      "entry": "fluids.js",
      "uuid": ...,
      "version": [1, 0, 0]
    }
  ],
  "dependencies": [
    {
      "module_name": "@minecraft/server",
      "version": "1.6.0-beta"
    }
  ]
}
```

<Spoiler title="流体移动与雾效脚本">

<CodeHeader>BP/scripts/fluids.js</CodeHeader>

```javascript
import { system, world } from "@minecraft/server";

const fluids = ["wiki:custom_fluid"];

system.runInterval(() => {
    const players = world.getPlayers();

    for (const player of players) {
        // 流体效果
        if (
            fluids.includes(
                world
                    .getDimension(player.dimension.id)
                    .getBlock({ ...player.location, y: player.location.y + 1 }).typeId
            ) ||
            fluids.includes(
                world.getDimension(player.dimension.id).getBlock(player.location).typeId
            )
        ) {
            player.addEffect("slowness", 3, { amplifier: 2, showParticles: false });
            player.addEffect("slow_falling", 4, { showParticles: false });
            if (player.isJumping) {
                player.addEffect("levitation", 3, { amplifier: 2, showParticles: false });
            }
        }
        // 流体雾效
        if (
            fluids.includes(
                world
                    .getDimension(player.dimension.id)
                    .getBlock({ ...player.location, y: player.location.y + 1.63 }).typeId
            )
        ) {
            player.runCommand("fog @s push wiki:custom_fluid_fog fluid_fog");
        } else {
            player.runCommand("fog @s remove fluid_fog");
        }
    }
});
```

</Spoiler>

## 结果

到最后，你的 BP 文件夹应如下所示：

<FolderView
  :paths="[
    'BP/blocks/custom_fluid.json',
    'BP/items/custom_fluid_bucket.json',
    'BP/scripts/fluids.js',
    'RP/fogs/custom_fluid.json'
  ]"
></FolderView>

## 下载示例包

如果出现任何问题，或者你需要所有模板文件，它们可以在此处下载。该包包含功能性流体所需的一切。

<Button link="https://github.com/Bedrock-OSS/wiki-addon/releases/download/download/custom_fluids.mcaddon">
    下载 MCADDON
</Button>