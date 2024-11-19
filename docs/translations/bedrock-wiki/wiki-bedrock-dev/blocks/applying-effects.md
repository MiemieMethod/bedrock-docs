---
title: 应用持续效果
category: 教程
tags:
    - 简易
    - 脚本
mentions:
    - MysticChair
    - SirLich
    - MedicalJewel105
    - QuazChick
    - SmokeyStack
description: 本教程旨在展示如何在实体站在方块上时应用状态效果。
---

/// tip | 格式 & 最小引擎版本 `1.21.40`
本教程假设你对方块有基本的理解，包括 [方块状态](../blocks/block-states.md)。
在开始之前，请查看 [方块指南](../blocks/blocks-intro.md)。
///

本教程旨在展示如何在实体站在方块上时应用状态效果。

## 检测踏板

### 方块 JSON

我们需要在代码中添加一些内容，首先让我们从一个状态开始，当站在上面时为 `true`，否则为 `false`：

```json title="minecraft:block > description"
"states": {
    "wiki:stood_on": [false, true]
}
```

现在我们需要注册我们的自定义组件，以便挂钩 [`stepOn`](../blocks/block-events.md#step-on) 和 [`stepOff`](../blocks/block-events.md#step-off) 事件：

```json title="minecraft:block > components"
"minecraft:custom_components": [
    "wiki:detect_treaders"
]
```

### 自定义组件脚本

```js title="BP/scripts/detect_treaders.js"
import { BlockPermutation, GameMode, Player, world } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const DetectTreadersBlockComponent = {
    onStepOn({ entity, block }) {
        if (entity instanceof Player && entity.getGameMode() === GameMode.creative) return;

        block.setPermutation(
            BlockPermutation.resolve(block.typeId, {
                "wiki:stood_on": true,
            })
        );
    },
    onStepOff({ entity, block }) {
        if (entity instanceof Player && entity.getGameMode() === GameMode.creative) return;

        block.setPermutation(
            BlockPermutation.resolve(block.typeId, {
                "wiki:stood_on": false,
            })
        );
    },
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:detect_treaders",
        DetectTreadersBlockComponent
    );
});
```

## 对踏板应用效果

### 方块 JSON

我们还需要让方块每个 tick 都进行更新，以便应用所需的效果。为此，我们将使用 [变体](../blocks/block-permutations.md) 数组，以便仅在方块被踩踏时应用自定义组件：

```json title="minecraft:block"
"permutations": [
    {
        "condition": "q.block_state('wiki:stood_on')",
        "components": {
            "minecraft:custom_components": ["wiki:detect_treaders", "wiki:wither_treaders"],
            "minecraft:tick": {
                "interval_range": [1, 1],
                "looping": true
            }
        }
    }
]
```

### 自定义组件脚本

现在，让我们添加一个事件，使实体获得凋零效果：

```js title="BP/scripts/wither_treaders.js"
import { Entity, GameMode, Player, world } from "@minecraft/server";

/** @type {import("@minecraft/server").BlockCustomComponent} */
const WitherTreadersBlockComponent = {
    onTick(event) {
        const entities = event.dimension.getEntitiesAtBlockLocation(event.block.above().location);

        entities.forEach((entity) => {
            entity.addEffect("minecraft:wither", 2, { amplifier: 2 });
        });
    },
};

world.beforeEvents.worldInitialize.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:wither_treaders",
        WitherTreadersBlockComponent
    );
});
```

完成了！上述代码将触发所需的状态效果，只要实体站在方块上。

## 示例 JSON

/// details-info | 示例凋零方块

```json title="BP/blocks/wither_block.json"
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:wither_block",
            "states": {
                "wiki:stood_on": [false, true]
            }
        },
        "components": {
            "minecraft:loot": "loot_tables/empty.json",
            "minecraft:map_color": "#181818",
            "minecraft:geometry": "geometry.wither_block",
            "minecraft:material_instances": {
                "*": {
                    "texture": "wither_block"
                }
            },
            "minecraft:custom_components": ["wiki:detect_treaders"]
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:stood_on')",
                "components": {
                    "minecraft:custom_components": ["wiki:detect_treaders", "wiki:wither_treaders"],
                    "minecraft:tick": {
                        "interval_range": [1, 1],
                        "looping": true
                    }
                }
            }
        ]
    }
}
```

///