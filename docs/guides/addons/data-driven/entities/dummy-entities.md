# 虚拟实体

**虚拟实体**是附加包中一类特殊的不可见辅助实体，本身不参与任何游戏玩法，而是被用作各种幕后机制的载体。由于其高度轻量、无碰撞、无渲染开销的特性，虚拟实体在地图制作和附加包开发中有着极为广泛的应用。

## 应用场景

虚拟实体并不是某种特定实体，而是一种设计模式。常见的应用场景包括：

- **数据存储**：通过为实体添加标签，将其作为一个"游戏管理器"存储状态，类似于曾经被广泛使用的盔甲架。
- **命名参照**：为虚拟实体命名，再用`/execute`命令对其执行，让命令方块以指定的显示名称发言。
- **位置标记**：在某个坐标放置虚拟实体，再以其为基准用`/execute`执行相对坐标命令，从而在任意位置触发逻辑。
- **寻路路标**：将实体的攻击目标设为某族的虚拟实体，然后把虚拟实体放置在目的地，驱使主体实体自动寻路前往。详见[实体移动](entity-movement.md)的寻路路段。

## 创建虚拟实体

### 行为包定义

以下是一个标准的虚拟实体行为包模板。关键要点是：无法受伤、无法被推动、几乎没有碰撞箱。

```json title="BP/entities/dummy.json"
{
    "format_version": "1.21.50",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:dummy",
            "is_summonable": true,
            "is_spawnable": false,
            "is_experimental": false
        },
        "components": {
            "minecraft:cannot_be_attacked": {},
            "minecraft:breathable": {
                "breathes_water": true
            },
            "minecraft:physics": {
                "has_gravity": false,
                "has_collision": false
            },
            "minecraft:custom_hit_test": {
                "hitboxes": [
                    {
                        "pivot": [0, 100, 0],
                        "width": 0,
                        "height": 0
                    }
                ]
            },
            "minecraft:damage_sensor": {
                "triggers": {
                    "deals_damage": false
                }
            },
            "minecraft:pushable": {
                "is_pushable": false,
                "is_pushable_by_piston": false
            },
            "minecraft:collision_box": {
                "width": 0.0001,
                "height": 0.0001
            }
        }
    }
}
```

如果需要禁用所有碰撞，使得其他实体和命令可以在其位置放置方块，可以使用`minecraft:arrow`运行时标识符，不过需要注意该标识符可能带来一些副作用。

### 资源包定义

```json title="RP/entity/dummy.json"
{
    "format_version": "1.10.0",
    "minecraft:client_entity": {
        "description": {
            "identifier": "wiki:dummy",
            "materials": {
                "default": "entity_alphatest"
            },
            "geometry": {
                "default": "geometry.dummy"
            },
            "render_controllers": ["controller.render.dummy"],
            "textures": {
                "default": "textures/wiki/entity/dummy"
            }
        }
    }
}
```

### 几何体

虚拟实体不需要任何可见的几何体，因此可以使用一个没有任何骨骼的空几何体：

```json title="RP/models/entity/dummy.json"
{
    "format_version": "1.12.0",
    "minecraft:geometry": [
        {
            "description": {
                "identifier": "geometry.dummy",
                "texture_width": 16,
                "texture_height": 16
            }
        }
    ]
}
```

### 渲染控制器（可选）

```json title="RP/render_controllers/dummy.json"
{
    "format_version": "1.10.0",
    "render_controllers": {
        "controller.render.dummy": {
            "geometry": "Geometry.default",
            "textures": ["Texture.default"],
            "materials": [{ "*": "Material.default" }]
        }
    }
}
```

### 纹理（可选）

纹理路径可以留空，或者在Blockbench中打开模型并创建一张空白纹理。虚拟实体在游戏中本就不会被渲染出来，因此纹理内容不重要。

## 使用说明

虚拟实体可以用`/summon wiki:dummy`召唤。由于`is_spawnable`设为`false`，它不会出现在创造模式物品栏中，也没有刷怪蛋。召唤后，可以像对待普通实体一样用`/tag`、`/execute`、`/tp`等命令操作它。

/// tip | 清理虚拟实体
使用`/kill @e[type=wiki:dummy]`可以一次性移除所有虚拟实体。建议在地图/附加包中预留好统一的清理机制。
///