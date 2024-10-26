---
title: 自定义死亡动画
tags:
    - 中级
category: 一般
mentions:
    - SirLich
    - Joelant05
    - Dreamedc2015
    - MedicalJewel105
    - aexer0e
    - Xterionix
    - ChibiMango
    - SmokeyStack
    - ThomasOrs
description: 更改或禁用实体死亡动画。
---

死亡动画是指实体在死亡时的旋转。这伴随着红色的着色，并在实体几何体消失后不久出现死亡粒子。

## 取消死亡动画

这一部分将解释如何完全移除死亡动画。

### 传送实体

一种常见的移除实体而不造成死亡效果的方法是将其传送到虚空。这可以通过动画控制器使用 `!q.is_alive` 来实现，例如：
`/teleport @s ~ ~-1000 ~`

请注意，这将移除所有死亡效果，包括声音、粒子、掉落物和实体的视觉死亡效果。

### minecraft:instant_despawn

如果你想让实体直接消失，可以添加一个组件组 `"minecraft:instant_despawn":{}`，并运行一个事件来添加这个组件组。

请注意，这将移除所有死亡效果，包括声音、粒子、掉落物和实体的视觉死亡效果。

### 转换为另一个实体

与传送类似，实体在死亡时触发实体转换。使用动画控制器中的 `!q.is_alive` 发送一个事件，该事件将添加包含 `"minecraft:transformation"` 组件的组件组。使用此组件，实体将转换为另一个实体：

<CodeHeader></CodeHeader>

```json
"minecraft:transformation": {
	"into": "wiki:death_animation_entity",
	"transformation_sound" : "converted_to_zombified",
	"keep_level": true,
	"drop_inventory": true,
	"preserve_equipment": false,
	"drop_equipment": true,
	"delay": {
		"block_assist_chance": 0.0,
		"block_radius": 0,
		"block_max": 0,
		"value": 10
	}
}
```

### 取消动画

我们还可以取消实体的旋转值，使实体以更传统的方式死亡（粒子、红色着色、掉落物），而不进行90度旋转。

如果你需要有关从实体死亡触发动画的更多信息，请参阅[此文档](/animation-controllers/death-commands)了解死亡效果。

旋转需要应用于所有其他骨骼的骨骼父级，枢轴位于 [0,0,0]，并且动画应仅在 `!q.is_alive` 时开始。

动画：

<CodeHeader></CodeHeader>

```json
"rotation" : [ 0, 0, "Math.min(Math.sqrt(Math.max(0, q.anim_time * 20 - 0.5) / 20 * 1.6), 1) * -90" ]
```

动画控制器：

（`q.all_animations_finished` 仅在重生实体时需要，例如玩家）

<CodeHeader>RP/animation_controllers/custom_death.animation.controllers.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.player.cancel_death_animaton": {
            "initial_state": "default",
            "states": {
                "default": {
                    "transitions": [
                        {
                            "cancel_animation": "!q.is_alive"
                        }
                    ]
                },
                "cancel_animation": {
                    "animations": ["my.animation"],
                    "transitions": [
                        {
                            "default": "q.is_alive && q.all_animations_finished"
                        }
                    ]
                }
            }
        }
    }
}
```

请注意，你需要在资源包的 `.entity.json` 文件中附加动画和动画控制器。

## 自定义死亡动画

这一部分将解释如何自定义死亡动画。

### 更改伤害颜色覆盖

你可以移除/自定义实体的伤害颜色覆盖。

在开始之前，你必须了解渲染控制器的基础知识，因此请查看[渲染控制器教程](/entities/render-controllers)。

要在实体受到伤害时移除其伤害覆盖颜色，我们将使用 `is_hurt_color` 并在实体受到岩浆或火焰伤害时移除伤害覆盖颜色，使用 `on_fire_color`。
首先，你需要将 rgba 值设置为 0。
以下是移除伤害和火焰覆盖颜色的示例。

<CodeHeader>RP/render_controllers/custom_death.render_controllers.json</CodeHeader>

```json
{
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.sample": {
            "geometry": "Geometry.default",
            "materials": [{ "*": "Material.default" }],
            "textures": ["Texture.default"],
            "is_hurt_color": {},
            "on_fire_color": {}
        }
    }
}
```

上述代码将移除红色伤害覆盖颜色。

你还可以通过将不同的值放入 rgba 来更改伤害颜色覆盖为不同的颜色。你可以查看各种网站以获取所有颜色的 rgba 值。
以下是另一个示例，其中伤害颜色覆盖变为粉色。

<CodeHeader>RP/render_controllers/custom_death.render_controllers.json</CodeHeader>

```json
{
    "format_version": "1.8.0",
    "render_controllers": {
        "controller.render.kbg": {
            "geometry": "Geometry.default",
            "materials": [{ "*": "Material.default" }],
            "textures": ["Texture.default"],
            "is_hurt_color": {
                "r": "1.0",
                "g": "0.4",
                "b": "0.7",
                "a": "0.5"
            },
            "on_fire_color": {
                "r": "1.0",
                "g": "0.4",
                "b": "0.7",
                "a": "0.5"
            }
        }
    }
}
```

### 使用伤害传感器触发即时消失和掉落一件物品

你可以使用 damage_sensor 组件在致命伤害时触发事件；该事件添加一个特定的消失组件组，包含 spawn_entity 和 instant_despawn 组件。带有 0 等待时间的 spawn_entity 将在实体消失之前掉落一件物品。对于像家具这样的简单实体，只需一件物品，这非常方便。

当实体受到致命伤害时，会触发一个事件，添加一个虚拟组件。然后我们可以使用这个虚拟组件播放动画，并使用 `minecraft:timer` 来使其消失。

请注意，你需要为具有库存的实体找到其他方法。你还应确保在使用 entity_spawned 事件生成实体时不添加消失组件组。如果你有一个执行其他动作（移动和攻击）的实体，你可能还想移除那些组件。

以下是 BP 中的示例文件

<CodeHeader>BP/entities/entity.json</CodeHeader>

```json
{
    "format_version": "1.14.0",
    "min_engine_version": "1.16.100",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:entity",
            "is_spawnable": true,
            "is_summonable": true,
            "is_experimental": true
        },
        "component_groups": {
            "wiki:death": {
                "minecraft:spawn_entity": {
                    "max_wait_time": 0,
                    "min_wait_time": 0,
                    "spawn_item": "egg",
                    "single_use": true
                },
                "minecraft:is_sheared": {},
                "minecraft:timer": {
                    "looping": true,
                    "time": [2.56, 2.56], // 将此更改为匹配你的动画时间
                    "time_down_event": {
                        "event": "wiki:despawn"
                    }
                }
            },
            "wiki:despawn": {
                "minecraft:instant_despawn": {}
            }
        },
        "components": {
            "minecraft:type_family": {
                "family": ["cart", "inanimate"]
            },
            "minecraft:collision_box": {
                "width": 0.8,
                "height": 0.5
            },
            "minecraft:health": {
                "value": 8,
                "max": 8
            },
            "minecraft:physics": {},
            "minecraft:pushable": {
                "is_pushable": true,
                "is_pushable_by_piston": true
            },
            "minecraft:damage_sensor": {
                "triggers": {
                    "on_damage": {
                        "filters": {
                            "all_of": [
                                {
                                    "test": "has_damage",
                                    "value": "fatal"
                                }
                            ]
                        },
                        "target": "self",
                        "event": "wiki:death",
                        "deals_damage": false,
                        "cause": "fatal"
                    }
                }
            }
        },
        "events": {
            "wiki:death": {
                "add": {
                    "component_groups": ["wiki:death"]
                },
                "wiki:despawn": {
                    "add": {
                        "component_groups": ["wiki:despawn"]
                    }
                }
            }
        }
    }
}
```

以下是动画控制器的示例文件。

<CodeHeader>RP/animation_controllers/animation_controller.entity.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.entity": {
            "states": {
                "default": {
                    "blend_transition": 0.2,
                    "transitions": [
                        {
                            "dead": "q.is_sheared"
                        }
                    ]
                },
                "death": {
                    "blend_transition": 0.2,
                    "animations": ["death"]
                }
            }
        }
    }
}
```

注意：你还可以通过设置 `"spawn_item"` 为你的实体 ID 和一个 `spawn_egg` 的后缀，使用 `minecraft:spawn_entity` 组件生成自定义生成蛋物品，效果如下。

<CodeHeader>BP/entities/my_entity.json#components</CodeHeader>

```json
{
    "minecraft:spawn_entity": [
        {
            "min_wait_time": 0,
            "max_wait_time": 0,
            "spawn_item": "wiki:custom_zombie_spawn_egg",
            "single_use": true
        }
    ]
}
```

如果你想掉落一个掉落表，你可以触发一个事件（如下所示），并召唤另一个具有此组件的实体：

<CodeHeader></CodeHeader>

```json
{
    "minecraft:behavior.drop_item_for": {
        "seconds_before_pickup": 0.0,
        "cooldown": 5,
        "drop_item_chance": 1,
        "offering_distance": 0.0,
        "minimum_teleport_distance": 1024.0,
        "target_range": [64.0, 64.0, 64.0],
        "teleport_offset": [0.0, 1.0, 0.0],
        "speed_multiplier": 1.0,
        "search_range": 64,
        "search_height": 64,
        "search_count": 0,
        "goal_radius": 64.0,
        "entity_types": [
            {
                "filters": {
                    "test": "is_family",
                    "subject": "other",
                    "value": "player"
                },
                "max_dist": 64
            }
        ],
        "priority": 1,
        "loot_table": "loot_tables/entities/example.loot_table.json",
        "time_of_day_range": [0.0, 1.0]
    },
    "minecraft:timer": {
        "time": 2,
        "time_down_event": {
            "event": "wiki:my_despawn_event"
        }
    }
}
```

然后通过 `wiki:my_despawn_event` 添加包含 instant_despawn 的组件组使其消失。

### 使用命令检测死亡

<Button link="/commands/tick_json-creations#death-detection">查看</Button>