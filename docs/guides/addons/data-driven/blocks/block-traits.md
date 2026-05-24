# 方块萃取的使用

方块萃取让自定义方块无需手写完整的状态更新逻辑，就能获得原版方块常见的放置行为。这一页重点讲如何实际使用它们，以及搭配置换调整外观。

## 声明萃取

萃取在方块定义文件的 `description.traits` 中声明：

```json title="BP/blocks/my_block.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:my_block",
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"]
                }
            }
        }
    }
}
```

## 放置方向萃取

`minecraft:placement_direction` 在玩家放置方块时自动记录玩家面对的方向。可以启用以下状态：

- `minecraft:cardinal_direction`：水平四向（`north`、`south`、`east`、`west`）
- `minecraft:facing_direction`：六面朝向（水平四向加 `up`、`down`）
- `minecraft:corner_and_cardinal_direction`：水平四向加四个转角方向（适合楼梯类方块）

启用 `y_rotation_offset` 可以旋转记录方向的偏移量（可选值：`0.0`、`90.0`、`180.0`、`270.0`）。

**示例：方向性方块，根据朝向旋转模型**

```json title="BP/blocks/directional_block.json"
{
    "format_version": "1.26.10",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:directional_block",
            "traits": {
                "minecraft:placement_direction": {
                    "enabled_states": ["minecraft:cardinal_direction"],
                    "y_rotation_offset": 180.0
                }
            }
        },
        "components": {
            "minecraft:geometry": "geometry.directional_block",
            "minecraft:material_instances": {
                "*": { "texture": "wiki:directional_block" },
                "front": { "texture": "wiki:directional_block_front" }
            }
        },
        "permutations": [
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'north'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 0, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'south'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 180, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'east'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, -90, 0] }
                }
            },
            {
                "condition": "q.block_state('minecraft:cardinal_direction') == 'west'",
                "components": {
                    "minecraft:transformation": { "rotation": [0, 90, 0] }
                }
            }
        ]
    }
}
```

## 放置位置萃取

`minecraft:placement_position` 记录方块相对于所附着的方块面或上下半部。可以启用：

- `minecraft:block_face`：方块附着的相邻面（`north`、`south`、`east`、`west`、`up`、`down`）
- `minecraft:vertical_half`：上半或下半（`top`、`bottom`），适合台阶类方块

**示例：可附着在任意面的按钮**

```json title="description > traits"
"minecraft:placement_position": {
    "enabled_states": ["minecraft:block_face"]
}
```

然后在置换中根据附着面调整几何体：

```json title="permutations（节选）"
{
    "condition": "q.block_state('minecraft:block_face') == 'up'",
    "components": {
        "minecraft:transformation": { "rotation": [0, 0, 0] }
    }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'down'",
    "components": {
        "minecraft:transformation": { "rotation": [180, 0, 0] }
    }
},
{
    "condition": "q.block_state('minecraft:block_face') == 'north'",
    "components": {
        "minecraft:transformation": { "rotation": [90, 0, 0] }
    }
}
```

## 连接关系萃取 <!-- md:flag experimental -->

`minecraft:connection` 萃取根据相邻方块自动更新水平连接状态，类似栅栏、玻璃板的连接行为。该萃取目前仍属于实验性功能，需要启用"即将推出的创作者功能"实验性开关，且要求 `format_version` 不低于 `1.21.130`。

它目前只能启用 `minecraft:cardinal_connections` 状态组，由此提供 `minecraft:connection_north`、`minecraft:connection_south`、`minecraft:connection_east`、`minecraft:connection_west` 四个布尔状态：

```json title="description > traits"
"minecraft:connection": {
    "enabled_states": ["minecraft:cardinal_connections"]
}
```

在置换中可以用这些状态控制骨骼显示：

```json title="components（在置换中）"
"minecraft:geometry": {
    "identifier": "geometry.my_fence",
    "bone_visibility": {
        "arm_north": "q.block_state('minecraft:connection_north')",
        "arm_south": "q.block_state('minecraft:connection_south')",
        "arm_east": "q.block_state('minecraft:connection_east')",
        "arm_west": "q.block_state('minecraft:connection_west')"
    }
}
```

还可以通过 `minecraft:connection_rule` 组件控制哪些类型的方块可以连接到你的方块：

```json title="components"
"minecraft:connection_rule": {
    "accepts_connections_from": "only_fences"
}
```

## 多方块萃取 <!-- md:flag experimental -->

`minecraft:multi_block` 萃取允许一个方块定义跨越多个位置，例如双高门、双高花、大型机器等。该萃取仍处于实验性阶段，需要启用"即将推出的创作者功能"实验性开关。

关于多方块的详细用法，请参考[多方块结构](multi-blocks.md)教程。

## 组合两种萃取

放置方向和放置位置萃取可以同时使用，这是实现"可附着多面、且每面有朝向"的方块（例如按钮、告示牌）的基础：

```json title="description > traits"
"minecraft:placement_direction": {
    "enabled_states": ["minecraft:cardinal_direction"]
},
"minecraft:placement_position": {
    "enabled_states": ["minecraft:block_face"]
}
```