# 自定义活板门

这一页演示如何创建一个功能完整的自定义活板门——支持四个方向放置、上下两个位置，以及右键开关交互。

## 实现要点

活板门的逻辑需要：

1. 两个萃取：`minecraft:placement_direction`（记录面对方向）和 `minecraft:placement_position`（记录上/下半）。
2. 一个 `wiki:open` 自定义状态（布尔值）。
3. 一个处理右键交互的自定义组件。
4. 完整的置换矩阵：4方向 × 2位置 × 开/关 = 16个置换。

## 方块定义

```json title="BP/blocks/custom_trapdoor.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_trapdoor",
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"],
                    "y_rotation_offset": 180.0
                },
                "minecraft:placement_position": {
                    "enabled_states": ["minecraft:vertical_half"]
                }
            },
            "states": {
                "wiki:open": [false, true]
            }
        },
        "components": {
            "wiki:toggleable": {
                "state": "wiki:open",
                "open_sound": "open.wooden_trapdoor",
                "close_sound": "close.wooden_trapdoor"
            },
            "minecraft:geometry": "geometry.custom_trapdoor",
            "minecraft:material_instances": {
                "*": { "texture": "wiki:custom_trapdoor", "render_method": "alpha_test" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'bottom' && !q.block_state('wiki:open')",
                "components": { "minecraft:transformation": { "rotation": [0, 0, 0] } }
            },
            {
                "condition": "q.block_state('minecraft:vertical_half') == 'top' && !q.block_state('wiki:open')",
                "components": { "minecraft:transformation": { "rotation": [180, 0, 0] } }
            },
            {
                "condition": "q.block_state('wiki:open') && q.block_state('minecraft:cardinal_direction') == 'north'",
                "components": { "minecraft:transformation": { "rotation": [90, 0, 0] } }
            },
            {
                "condition": "q.block_state('wiki:open') && q.block_state('minecraft:cardinal_direction') == 'south'",
                "components": { "minecraft:transformation": { "rotation": [-90, 0, 0] } }
            },
            {
                "condition": "q.block_state('wiki:open') && q.block_state('minecraft:cardinal_direction') == 'east'",
                "components": { "minecraft:transformation": { "rotation": [0, 0, -90] } }
            },
            {
                "condition": "q.block_state('wiki:open') && q.block_state('minecraft:cardinal_direction') == 'west'",
                "components": { "minecraft:transformation": { "rotation": [0, 0, 90] } }
            }
        ]
    }
}
```

/// note | 碰撞箱和选取箱
完整实现还需要在每个置换中配置对应的 `minecraft:collision_box` 和 `minecraft:selection_box`，使其与模型形状匹配。以上为简化示意。
///

## 开关自定义组件

```js title="BP/scripts/toggleable.js"
import { system } from "@minecraft/server";

const ToggleableComponent = {
    onPlayerInteract({ block }, { params }) {
        const currentState = block.permutation.getState(params.state);
        block.setPermutation(block.permutation.withState(params.state, !currentState));
        block.dimension.playSound(
            currentState ? params.close_sound : params.open_sound,
            block.center()
        );
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent("wiki:toggleable", ToggleableComponent);
});
```

## 方块模型

在Blockbench中为活板门建模时，基础姿态应是"关闭、底部"：

- 方块位于Y=0～3（底部，3像素厚）。
- 纹理面向北方。

置换通过 `minecraft:transformation` 旋转模型来实现其他位置和方向，无需为每种状态单独制作模型。

## 本地化

```lang title="RP/texts/zh_CN.lang"
tile.wiki:custom_trapdoor.name=自定义活板门
```