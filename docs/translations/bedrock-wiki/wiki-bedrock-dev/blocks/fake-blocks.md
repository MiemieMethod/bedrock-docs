---
title: 虚假区块
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - MedicalJewel105
    - aexer0e
    - ThijsHankelMC
    - QuazChick
    - SmokeyStack
description: 有时候你的区块需要具备Minecraft不允许的特性。一个可能的解决方案是创建一个复制区块特性的实体。
---

有时候你的区块需要具备Minecraft不允许的特性。一个可能的解决方案是创建一个复制区块特性的实体。

## 创建碰撞

[固体实体](../entities/solid-entities.md)教程概述了四种不同的创建碰撞的方法，包括`runtime_identifiers`、区块和组件。

## 基本组件

以下组件是使实体表现得像一个区块所必需的，并且不要在其中添加`"minecraft:physics": {}`组件，因为这会使你的实体掉落或与某些区块（如水或岩浆）发生碰撞。

<CodeHeader>BP/entities/your_entity.json#minecraft:entity/components</CodeHeader>

```json
{
    // 击退抗性是为了使其不被实体击退。
    "minecraft:knockback_resistance": {
        "value": 1
    },
    // 指示实体是否可以被推动。
    "minecraft:pushable": {
        "is_pushable": false,
        "is_pushable_by_piston": true
    },
    // 设置实体可以推动的距离。
    "minecraft:push_through": {
        "value": 1
    },
    // 使其无敌。
    "minecraft:damage_sensor": {
        "triggers": [
            {
                "deals_damage": false,
                "cause": "all"
            }
        ]
    }
}
```

## 对齐实体旋转

要对齐实体的旋转，你需要一些数学运算。

<CodeHeader></CodeHeader>

```json
"rotation": [ 0, "-q.body_y_rotation + (Math.round(q.body_y_rotation / 90) * 90)", 0 ]
```

将该代码应用于模型的核心文件夹（包含所有其他组），确保枢轴点在X和Z轴上为0，以避免视觉错误。同时，你不需要添加如下组件：

-   `"minecraft:behavior.look_at_entity": {}`
-   `"minecraft:behavior.look_at_player": {}`
-   `"minecraft:behavior.look_at_target": {}`

原因是这些组件会改变目标Y旋转，导致身体Y旋转移动，从而使模型移动。也不要添加行走组件。

## 对齐实体位置

对齐实体位置会更棘手。

首先，在`minecraft:entity_spawned`事件中，创建一个带有queue_command的自定义区块，并创建一个新的虚拟实体，通过变换事件将虚拟实体转换为原始实体，以避免再次触发`minecraft:entity_spawned`。

<CodeHeader>BP/entities/your_entity.json#minecraft:entity/events</CodeHeader>

```json
// 原始实体中的事件。
"minecraft:entity_spawned": {
    "add": {
        "components_groups": [
            "despawn" // 我们还需要让第一个实体消失。
        ]
    },
    "queue_command": {
        "command": ["setblock ~~~ wiki:align"]
    }
}
```

<CodeHeader>BP/entities/your_entity.json#minecraft:entity/component_groups</CodeHeader>

```json
// 原始实体中的组件组。
"component_groups": {
    "despawn": {
        "minecraft:despawn": {}
    }
}
```

用于在区块上召唤虚拟实体的区块，由于区块是居中的，实体也会居中：

<CodeHeader>BP/blocks/your_dummy_block.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:align"
        },
        "components": {
            "minecraft:light_dampening": 0,
            "minecraft:collision_box": false,
            "minecraft:selection_box": false,
            "minecraft:loot": "loot_tables/empty.json",
            "minecraft:geometry": "geometry.empty",
            "minecraft:material_instances": {
                "*": {
                    "texture": "empty"
                }
            },
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 2
            },
            "minecraft:custom_components": ["wiki:align_entity"]
        }
    }
}
```

对于我们的自定义组件脚本，我们将利用`beforeOnPlayerPlace`事件。我们使用此事件来防止区块被放置，而是直接召唤我们的实体。

```js
import { world } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const AlignEntityBlockComponent = {
    beforeOnPlayerPlace(event) {
        event.cancel = true;

        const location = event.block.center();
        event.dimension.spawnEntity("wiki:dummy_align", location);
    },
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:align_entity", AlignEntityBlockComponent);
});
```

<CodeHeader>BP/entities/your_dummy_entity.json</CodeHeader>

```json
{
    "format_version": "1.13.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:dummy_align", // 虚拟实体用于避免触发原始实体中的entity_spawned事件。
            "is_spawnable": false,
            "is_summonable": true,
            "is_experimental": false
        },
        "component_groups": {
            "transform": {
                "minecraft:transformation": {
                    "into": "wiki:your_entity",
                    "delay": 0
                }
            }
        },
        "components": {
            "minecraft:physics": {
                "has_gravity": false
            },
            "minecraft:collision_box": {
                "width": 0.1,
                "height": 0.1
            },
            "minecraft:damage_sensor": {
                "triggers": {
                    "cause": "all",
                    "deals_damage": false
                }
            }
        },
        "events": {
            "minecraft:entity_spawned": {
                "add": {
                    "component_groups": ["transform"]
                }
            }
        }
    }
}
```

## 裂纹纹理

原版区块在被破坏时会出现裂纹纹理。这里我将向你展示如何将此效果添加到你的实体中。

首先，我们需要在你的实体文件中添加一些纹理，确保使用原版纹理而不是自定义纹理（这是为了与资源包兼容）。

<CodeHeader>RP/entity/your_entity.json#description</CodeHeader>

```json
{
    "textures": {
        "default": "textures/entity/your_texture",
        "destroy_stage_0": "textures/environment/destroy_stage_0",
        "destroy_stage_1": "textures/environment/destroy_stage_1",
        "destroy_stage_2": "textures/environment/destroy_stage_2",
        "destroy_stage_3": "textures/environment/destroy_stage_3",
        "destroy_stage_4": "textures/environment/destroy_stage_4",
        "destroy_stage_5": "textures/environment/destroy_stage_5",
        "destroy_stage_6": "textures/environment/destroy_stage_6",
        "destroy_stage_7": "textures/environment/destroy_stage_7",
        "destroy_stage_8": "textures/environment/destroy_stage_8",
        "destroy_stage_9": "textures/environment/destroy_stage_9"
    }
}
```

并添加一个几何体，其所有立方体的膨胀值为0.1，以避免Z-Fighting。

<CodeHeader>RP/entity/your_entity.json#description</CodeHeader>

```json
{
    "geometry": {
        "default": "geometry.your_geometry",
        "broken": "geometry.broken"
    }
}
```

现在我们需要添加一个新的渲染控制器。这个控制器将根据破坏阶段选择不同的纹理。（记得不要替换你的实际控制器，你需要两个控制器，第一个是添加模型、纹理和材料到你的正常实体，第二个是定义裂纹纹理的控制器）

<CodeHeader>RP/render_controllers/my_entity.json</CodeHeader>

```json
{
    "controller.render.broken": {
        "arrays": {
            "textures": {
                "array.broken": [
                    "texture.destroy_stage_9",
                    "texture.destroy_stage_8",
                    "texture.destroy_stage_7",
                    "texture.destroy_stage_6",
                    "texture.destroy_stage_5",
                    "texture.destroy_stage_4",
                    "texture.destroy_stage_3",
                    "texture.destroy_stage_2",
                    "texture.destroy_stage_1",
                    "texture.destroy_stage_0",
                    "texture.normal"
                ]
            }
        },
        "geometry": "Geometry.broken",
        "materials": [
            {
                "*": "Material.default"
            }
        ],
        "textures": [
            "array.broken[q.health * 1]" // 在这里你可以计算实体的生命值，以确保它不会出现错误。如果你的实体有10点生命值，保持不变。如果有20点，应该是`q.health * 0.5`。如果是40点，则需要0.25，等等...
        ]
    }
}
```