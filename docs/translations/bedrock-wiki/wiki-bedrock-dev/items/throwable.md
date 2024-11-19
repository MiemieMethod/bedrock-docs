---
title: 可投掷物品
category: 教程
tags:
    - 中级
mentions:
    - Fabrimat
    - MedicalJewel105
    - Luthorius
    - IlkinQafarov
    - seeit360
    - TheItsNameless
    - SmokeyStack
    - ThomasOrs
description: 重现原版投掷机制。
---

::: tip
本教程假设你对Molang、动画控制器和实体定义有基本了解。
:::

像药水和三叉戟这样的物品是可以被投掷的特殊物品。

### 物品

首先，你需要创建实际的物品：

```json title="BP/items/throwable_item.item.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:throwable_item"
        },
        "components": {
            "minecraft:max_stack_size": 16,
            "minecraft:throwable": {
                "do_swing_animation": true
            },
            "minecraft:projectile": {
                "projectile_entity": "wiki:throwable_item_entity"
            },
            "minecraft:icon": "throwable_item"
        }
    }
}
```

### 实体

该实体将是实际被投掷的物品，并且它将像投射物一样行为。
确保添加雪球的运行时标识符，以使你的投射物实际被射出，而不是生成。你还可以尝试其他投射物的运行时ID。

```json title="BP/entities/throwable_item_entity.se.json"
{
    "format_version": "1.16.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:throwable_item_entity",
            "is_spawnable": false,
            "is_summonable": true,
            "is_experimental": false,
            "runtime_identifier": "minecraft:snowball"
        },
        "components": {
            "minecraft:collision_box": {
                "width": 0.25,
                "height": 0.25
            },
            "minecraft:projectile": {
                "on_hit": {
                    "grant_xp": {
                        "minXP": 3,
                        "maxXP": 5
                    },
                    "impact_damage": {
                        "damage": 16
                    },
                    "remove_on_hit": {}
                },
                "power": 0.7,
                "gravity": 0.03,
                "angle_offset": -20,
                "hit_sound": "glass"
            },
            "minecraft:physics": {},
            "minecraft:pushable": {
                "is_pushable": true,
                "is_pushable_by_piston": true
            },
            "minecraft:conditional_bandwidth_optimization": {
                "default_values": {
                    "max_optimized_distance": 80,
                    "max_dropped_ticks": 10,
                    "use_motion_prediction_hints": true
                }
            }
        }
    }
}
```

该实体基于原版的药水。

你可以通过编辑`minecraft:projectile`组件来自定义其行为，在这种情况下，投掷的物品将给予一些经验并对其命中的任何实体造成伤害。

## 结论

一旦你拥有了可投掷物品，就可以开始尝试多种事情，例如调整其威力、效果、动画或将其与[AOE云](../entities/introduction-to-aec.md)结合。唯一的限制是你的想象力。