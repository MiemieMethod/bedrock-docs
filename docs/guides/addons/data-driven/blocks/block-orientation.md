# 方块朝向

自定义方块可以通过多种方式实现朝向功能。本文介绍四种常见的朝向类型及其实现方式。

## 轴对齐朝向

轴对齐朝向类似于原版木头（木原木）的放置方式——方块沿X、Y或Z轴对齐，根据玩家放置时所在的面决定轴向。

使用 `minecraft:placement_direction` 特质并启用 `minecraft:facing_direction`，然后在置换中用旋转变换对应：

```json title="BP/blocks/axial_block.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:axial_block",
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:facing_direction"]
                }
            }
        },
        "components": {
            "minecraft:geometry": "geometry.axial_block",
            "minecraft:material_instances": {
                "*": { "texture": "wiki:axial_side" },
                "end": { "texture": "wiki:axial_end" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('minecraft:facing_direction') == 'up' || q.block_state('minecraft:facing_direction') == 'down'",
                "components": { "minecraft:transformation": { "rotation": [0, 0, 0] } }
            },
            {
                "condition": "q.block_state('minecraft:facing_direction') == 'north' || q.block_state('minecraft:facing_direction') == 'south'",
                "components": { "minecraft:transformation": { "rotation": [90, 0, 0] } }
            },
            {
                "condition": "q.block_state('minecraft:facing_direction') == 'east' || q.block_state('minecraft:facing_direction') == 'west'",
                "components": { "minecraft:transformation": { "rotation": [0, 0, 90] } }
            }
        ]
    }
}
```

## 方块面附着朝向

类似于按钮和火把——方块附着在某个面上。使用 `minecraft:placement_position` 特质并启用 `minecraft:block_face`：

```json title="description > traits"
"minecraft:placement_position": {
    "enabled_states": ["minecraft:block_face"]
}
```

置换中根据 `minecraft:block_face` 的值（`up`、`down`、`north`、`south`、`east`、`west`）旋转模型：

```json title="permutations（节选）"
{
    "condition": "q.block_state('minecraft:block_face') == 'down'",
    "components": { "minecraft:transformation": { "rotation": [180, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'north'",
    "components": { "minecraft:transformation": { "rotation": [90, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'south'",
    "components": { "minecraft:transformation": { "rotation": [-90, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'east'",
    "components": { "minecraft:transformation": { "rotation": [0, 0, -90] } }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'west'",
    "components": { "minecraft:transformation": { "rotation": [0, 0, 90] } }
}
```

## 基本四向朝向（水平）

类似于原版熔炉和发射器——方块面向玩家放置时的方向。使用 `minecraft:placement_direction` 特质并启用 `minecraft:cardinal_direction`，用 `y_rotation_offset: 180.0` 使方块面向玩家：

```json title="description > traits"
"minecraft:placement_direction": {
    "enabled_states": ["minecraft:cardinal_direction"],
    "y_rotation_offset": 180.0
}
```

在置换中应用Y轴旋转：

```json title="permutations"
[
    {
        "condition": "q.block_state('minecraft:cardinal_direction') == 'north'",
        "components": { "minecraft:transformation": { "rotation": [0, 0, 0] } }
    },
    {
        "condition": "q.block_state('minecraft:cardinal_direction') == 'south'",
        "components": { "minecraft:transformation": { "rotation": [0, 180, 0] } }
    },
    {
        "condition": "q.block_state('minecraft:cardinal_direction') == 'east'",
        "components": { "minecraft:transformation": { "rotation": [0, -90, 0] } }
    },
    {
        "condition": "q.block_state('minecraft:cardinal_direction') == 'west'",
        "components": { "minecraft:transformation": { "rotation": [0, 90, 0] } }
    }
]
```

## 面朝向（六面）

类似于漏斗和活塞——方块可以朝向六个方向中的任意一个。使用 `minecraft:placement_direction` 特质并启用 `minecraft:facing_direction`，再在置换中处理六个方向：

```json title="description > traits"
"minecraft:placement_direction": {
    "enabled_states": ["minecraft:facing_direction"],
    "y_rotation_offset": 180.0
}
```

六个方向对应的旋转变换：

```json title="permutations（节选）"
{
    "condition": "q.block_state('minecraft:facing_direction') == 'up'",
    "components": { "minecraft:transformation": { "rotation": [-90, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:facing_direction') == 'down'",
    "components": { "minecraft:transformation": { "rotation": [90, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:facing_direction') == 'north'",
    "components": { "minecraft:transformation": { "rotation": [0, 0, 0] } }
},
{
    "condition": "q.block_state('minecraft:facing_direction') == 'south'",
    "components": { "minecraft:transformation": { "rotation": [0, 180, 0] } }
},
{
    "condition": "q.block_state('minecraft:facing_direction') == 'east'",
    "components": { "minecraft:transformation": { "rotation": [0, -90, 0] } }
},
{
    "condition": "q.block_state('minecraft:facing_direction') == 'west'",
    "components": { "minecraft:transformation": { "rotation": [0, 90, 0] } }
}
```

## 16向朝向（斜角方向）

如果需要16个方向（4个基本方向加12个斜向），游戏目前没有内置特质支持，需要结合脚本API自定义实现。详见[16向朝向](intercardinal-orientation.md)教程。