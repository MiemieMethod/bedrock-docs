# 自定义农作物

这一页演示如何制作一个有8个生长阶段的农作物，从播种到成熟，并支持通过右键收割。

## 准备工作

农作物需要：

1. 一个记录阶段的整数状态（0～7）。
2. 种植在耕地上的逻辑（通过 `canPlace` 限制）。
3. 用 `onRandomTick` 事件随机生长。
4. 用 `onPlayerInteract` 事件右键收割。
5. 8种外观阶段用置换和骨骼控制。

## 已知问题

/// warning | 已知限制
- 随机刻触发频率受世界游戏规则 `randomTickSpeed` 影响，开发阶段建议调高该值以快速测试。
- 农作物模型需要设置 `face_dimming: false` 以获得正确的亮度效果。
///

## 方块定义

```json title="BP/blocks/custom_wheat.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_wheat",
            "states": {
                "wiki:growth": {
                    "values": { "min": 0, "max": 7 }
                }
            }
        },
        "components": {
            "wiki:crop_behavior": {
                "seed_item": "wiki:custom_wheat_seeds",
                "drop_item": "wiki:custom_wheat",
                "seeds_min": 1,
                "seeds_max": 3,
                "growth_chance": 0.14
            },
            "minecraft:geometry": {
                "identifier": "geometry.custom_wheat",
                "bone_visibility": {
                    "stage_0": "q.block_state('wiki:growth') == 0",
                    "stage_1": "q.block_state('wiki:growth') == 1",
                    "stage_2": "q.block_state('wiki:growth') == 2",
                    "stage_3": "q.block_state('wiki:growth') == 3",
                    "stage_4": "q.block_state('wiki:growth') == 4",
                    "stage_5": "q.block_state('wiki:growth') == 5",
                    "stage_6": "q.block_state('wiki:growth') == 6",
                    "stage_7": "q.block_state('wiki:growth') == 7"
                }
            },
            "minecraft:material_instances": {
                "*": {
                    "texture": "wiki:custom_wheat",
                    "render_method": "alpha_test",
                    "face_dimming": false,
                    "ambient_occlusion": false
                }
            },
            "minecraft:collision_box": false,
            "minecraft:selection_box": {
                "origin": [-8, 0, -8],
                "size": [16, 6, 16]
            },
            "minecraft:light_dampening": 0,
            "minecraft:destructible_by_mining": { "seconds_to_destroy": 0 },
            "minecraft:destructible_by_explosion": { "explosion_resistance": 0 },
            "minecraft:placement_filter": {
                "conditions": [
                    {
                        "allowed_faces": ["up"],
                        "block_filter": [
                            { "name": "minecraft:farmland" }
                        ]
                    }
                ]
            }
        }
    }
}
```

## 脚本逻辑

```js title="BP/scripts/crop_behavior.js"
import { system, EquipmentSlot } from "@minecraft/server";

const CropBehaviorComponent = {
    onRandomTick({ block }, { params }) {
        const current = block.permutation.getState("wiki:growth");
        if (current >= 7) return;
        if (Math.random() < params.growth_chance) {
            block.setPermutation(block.permutation.withState("wiki:growth", current + 1));
        }
    },

    onPlayerInteract({ block, player }, { params }) {
        const growth = block.permutation.getState("wiki:growth");
        if (growth < 7) return; // 未成熟

        // 掉落作物
        block.dimension.spawnItem(
            { typeId: params.drop_item, amount: 1 },
            block.center()
        );

        // 随机掉落种子
        const seedCount = params.seeds_min +
            Math.floor(Math.random() * (params.seeds_max - params.seeds_min + 1));
        for (let i = 0; i < seedCount; i++) {
            block.dimension.spawnItem(
                { typeId: params.seed_item, amount: 1 },
                block.center()
            );
        }

        // 重置到初始阶段
        block.setPermutation(block.permutation.withState("wiki:growth", 0));
    },

    onPlayerDestroy({ block, dimension }, { params }) {
        // 未成熟时破坏只掉落种子一粒
        const growth = block.permutation.getState("wiki:growth");
        const seedCount = growth < 7 ? 1 : params.seeds_min +
            Math.floor(Math.random() * (params.seeds_max - params.seeds_min + 1));
        for (let i = 0; i < seedCount; i++) {
            dimension.spawnItem(
                { typeId: params.seed_item, amount: 1 },
                block.center()
            );
        }
        if (growth >= 7) {
            dimension.spawnItem(
                { typeId: params.drop_item, amount: 1 },
                block.center()
            );
        }
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:crop_behavior", CropBehaviorComponent);
});
```

## 模型设计

在Blockbench中，制作8根骨骼（`stage_0`～`stage_7`），每根骨骼使用对应生长阶段的十字形（cross）形状，高度逐渐增加。通过 `bone_visibility` 控制可见骨骼。

## 种子物品

种子是一个使用 `minecraft:block_placer` 组件的物品：

```json title="BP/items/custom_wheat_seeds.json"
{
    "format_version": "1.26.10",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_wheat_seeds",
            "menu_category": { "category": "nature" }
        },
        "components": {
            "minecraft:block_placer": {
                "block": "wiki:custom_wheat",
                "replace_block_item": false
            }
        }
    }
}
```

## 本地化

```lang title="RP/texts/zh_CN.lang"
tile.wiki:custom_wheat.name=自定义小麦
item.wiki:custom_wheat_seeds.name=自定义小麦种子
item.wiki:custom_wheat.name=自定义小麦
```
