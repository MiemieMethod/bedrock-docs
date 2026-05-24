# 16向朝向

标准萃取只支持4个（水平）或6个（全方向）朝向。如果你需要16个方向（每隔22.5°一个），例如地毯、盔甲架头饰或风向标，就需要结合脚本API手动实现。

/// warning | 已知限制
基岩版目前没有原生的16向朝向萃取，完整实现需要自定义状态 + 自定义组件 + 特殊模型设计。
///

## 实现原理

思路如下：

1. 定义一个取值0～15的整数状态，每个值代表22.5°的旋转步进。
2. 在 `beforeOnPlayerPlace` 事件中，把玩家的 Y 轴旋转角度转换为0～15的整数，记入状态。
3. 模型中制作4根骨骼，分别旋转0°、22.5°、45°、67.5°，通过 `bone_visibility` 隐藏不需要的骨骼。
4. 用置换处理4个基本方向的90°旋转（每个旋转段处理4个22.5°小步）。

## 方向转换函数

```js title="BP/scripts/intercardinal.js"
/**
 * 将玩家Y旋转角转为0-15的朝向整数
 * 0=南，4=西，8=北，12=东（每步22.5°）
 */
function getIntercardinalDirection(yRotation) {
    const normalized = ((yRotation % 360) + 360) % 360;
    return Math.round(normalized / 22.5) % 16;
}
```

## 方块定义

```json title="BP/blocks/weathervane.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:weathervane",
            "states": {
                "wiki:direction_16": {
                    "values": { "min": 0, "max": 15 }
                }
            }
        },
        "components": {
            "wiki:intercardinal_placement": {},
            "minecraft:geometry": {
                "identifier": "geometry.weathervane",
                "bone_visibility": {
                    "dir_0": "math.mod(q.block_state('wiki:direction_16'), 4) == 0",
                    "dir_1": "math.mod(q.block_state('wiki:direction_16'), 4) == 1",
                    "dir_2": "math.mod(q.block_state('wiki:direction_16'), 4) == 2",
                    "dir_3": "math.mod(q.block_state('wiki:direction_16'), 4) == 3"
                }
            },
            "minecraft:material_instances": {
                "*": { "texture": "wiki:weathervane" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('wiki:direction_16') < 4",
                "components": { "minecraft:transformation": { "rotation": [0, 0, 0] } }
            },
            {
                "condition": "q.block_state('wiki:direction_16') >= 4 && q.block_state('wiki:direction_16') < 8",
                "components": { "minecraft:transformation": { "rotation": [0, 90, 0] } }
            },
            {
                "condition": "q.block_state('wiki:direction_16') >= 8 && q.block_state('wiki:direction_16') < 12",
                "components": { "minecraft:transformation": { "rotation": [0, 180, 0] } }
            },
            {
                "condition": "q.block_state('wiki:direction_16') >= 12",
                "components": { "minecraft:transformation": { "rotation": [0, 270, 0] } }
            }
        ]
    }
}
```

## 注册自定义组件

```js title="BP/scripts/intercardinal.js"
import { system } from "@minecraft/server";

function getIntercardinalDirection(yRotation) {
    const normalized = ((yRotation % 360) + 360) % 360;
    return Math.round(normalized / 22.5) % 16;
}

const IntercardinalPlacementComponent = {
    beforeOnPlayerPlace({ player, permutationToPlace }) {
        if (!player) return;
        const direction = getIntercardinalDirection(player.getRotation().y);
        permutationToPlace = permutationToPlace.withState("wiki:direction_16", direction);
    }
};

system.beforeEvents.startup.subscribe(({ blockComponentRegistry }) => {
    blockComponentRegistry.registerCustomComponent(
        "wiki:intercardinal_placement",
        IntercardinalPlacementComponent
    );
});
```

## 模型设计要点

在Blockbench中，制作4根骨骼，每根骨骼从同一轴心点（通常是方块中心）出发，Y轴旋转分别为：

- `dir_0`：0°
- `dir_1`：22.5°
- `dir_2`：45°
- `dir_3`：67.5°

通过 `bone_visibility` 只显示 `state % 4` 对应的骨骼，再通过置换在4个象限（0～3、4～7、8～11、12～15）之间旋转90°，就能覆盖完整的16个方向。

## y_rotation_offset参数

注册自定义组件时也可以支持参数化的旋转偏移：

```json title="components"
"wiki:intercardinal_placement": {
    "y_rotation_offset": 90
}
```

```js
beforeOnPlayerPlace({ player, permutationToPlace }, { params }) {
    if (!player) return;
    const offset = params?.y_rotation_offset ?? 0;
    const direction = getIntercardinalDirection(player.getRotation().y + offset);
    permutationToPlace = permutationToPlace.withState("wiki:direction_16", direction);
}
```