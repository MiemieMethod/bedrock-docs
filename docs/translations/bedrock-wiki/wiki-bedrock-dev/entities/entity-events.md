---
title: 实体事件
category: 通用
mentions:
    - ChibiMango
    - SirLich
    - Joelant05
    - MedicalJewel105
    - aexer0e
    - SmokeyStack
    - ThomasOrs
    - QuazChick
tags:
    - 初学者
description: 学习实体最重要的内容之一——事件。
---

实体事件是行为的基本构建模块之一，与组件和组件组并列。它们作为组件组的控制中心，可以从组件、动画、动画控制器和其他事件中调用。本页旨在介绍如何在实体内及其他实体中调用事件，以及事件的格式。

## 事件响应

事件允许我们执行动作，例如向实体添加和移除组件组，使实体在满足特定条件时能够改变其行为。之所以称为事件，是因为我们可以在事件发生时激活它们，例如计时器耗尽、玩家与实体互动或环境变化发生。当事件被触发时，它将执行所有列出的事件响应。

### 添加/移除

事件最基本和最常见的用途是直接添加和/或移除组件组。这些几乎总是在你的事件中使用，并与其他键一起使用。以下名为 `wiki:ranged_attacker` 的事件添加了两个组件组 "attacker" 和 "ranged"，并移除了组件组 "standby" 和 "melee"：

```json title="minecraft:entity > events"
"wiki:ranged_attacker": {
    "add": {
        "component_groups": [
            "attacker",
            "ranged"
        ]
    },
    "remove":{
        "component_groups": [
            "standby",
            "melee"
        ]
    }
}
```

/// tip
当你添加一个组件组时，如果目前活跃的组件组中包含相同的组件，它将被最近添加的组覆盖。
///

### 排队命令

将命令排队，由目标在当前刻的结束时执行。

```json title="minecraft:entity > events"
"wiki:execute_event": {
    "queue_command": {
        "target": "self", // 可选 - 默认是 'self'（目标实体）
        "command": "summon pig"
    }
}
```

可以使用数组来排队多个命令：

```json title="minecraft:entity > events"
"wiki:execute_event": {
    "queue_command": {
        "target": "self", // 可选 - 默认是 'self'（目标实体）
        "command": [
            "summon pig",
            "say Everybody welcome the pig!"
        ]
    }
}
```

### 随机化

随机化是一个可以在实体事件中使用的参数，用于根据加权随机化添加或移除组件组。当应基于随机机会添加不同的组件组时，这是一个非常有用的工具。

牛的 `minecraft:entity_spawned` 事件使用随机化，使牛以95%的概率生成成年牛，5%的概率生成小牛（组件组 `minecraft:cow_adult` 和 `minecraft:cow_baby`）。

```json title="minecraft:entity > events"
"minecraft:entity_spawned": {
    "randomize": [
        {
            "weight": 95,
            "add": {
                "component_groups": [
                    "minecraft:cow_adult"
                ]
            }
        },
        {
            "weight": 5,
            "add": {
                "component_groups": [
                    "minecraft:cow_baby"
                ]
            }
        }
    ]
}
```

注意，`randomize` 只会从选项池中选择一个选项。

### 序列/过滤器

序列是一个可以在实体事件中使用的参数，根据过滤器添加或移除组件组。过滤器允许我们创建条件事件，只有在满足条件时才会添加/移除组件组。僵尸的 `minecraft:convert_to_drowned` 事件使用 `sequence` 参数，根据僵尸是否是幼年来添加不同的组件组。

```json title="minecraft:entity > events"
"minecraft:convert_to_drowned": {
    "sequence": [
        {
            "filters": {
                "test": "has_component",
                "operator": "!=",
                "value": "minecraft:is_baby"
            },
            "add": {
                "component_groups": [
                    "minecraft:convert_to_drowned"
                ]
            },
            "remove": {
                "component_groups": [
                    "minecraft:start_drowned_transformation"
                ]
            }
        },
        {
            "filters": {
                "test":"has_component",
                "value":"minecraft:is_baby"
            },
            "add": {
                "component_groups": [
                    "minecraft:convert_to_baby_drowned"
                ]
            },
            "remove": {
                "component_groups": [
                    "minecraft:start_drowned_transformation"
                ]
            }
        }
    ]
}
```

此外，`sequence` 允许我们按顺序运行多个参数。它逐个评估每个部分，如果有效，则应用它。

/// tip
序列中的条目不是互斥的；如果其中一个条目的过滤器通过，它不会阻止其他条目的运行。在上面的例子中，第一个条目没有过滤器，因此它会自动运行。这不会阻止其他条目被检查并在有效时随之运行。
///

以下是一个广泛使用序列结合过滤器、随机化和添加/移除组件组的示例：

<Spoiler title="序列示例">

当实体被玩家或投射物击中时运行此事件。有60%的机会什么都不会发生，有40%的机会激活攻击序列。此攻击序列根据实体当前的健康状态（实体低于半血时给予更高的强攻机会）和与最近玩家的距离（当玩家距离较远时，远程攻击优先级较高）选择一个随机攻击。

```json title="minecraft:entity > events"
"wiki:on_hit": {
    "randomize":[
        // 60%的机会什么都不会发生
        {
            "weight": 60
        },
        // 40%的机会运行此条目
        {
            "weight": 40,
            "sequence": [
                // 运行所有攻击所需的独立事件
                {
                    "trigger": "attack_event"
                },
                // 如果实体未被剃毛（实体半血以下时变为剃毛状态），则运行
                {
                    "filters": {
                        "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:is_sheared"
                    },
                    "sequence": [
                        // 如果玩家在5个区块内运行
                        {
                            "filters": {
                                "test": "distance_to_nearest_player",
                                "operator": "<=",
                                "value": 5.0
                            },
                            "randomize": [
                                {
                                    "weight": 10,
                                    "add": {
                                        "component_groups": [
                                            "explode"
                                        ]
                                    }
                                },
                                {
                                    "weight": 60,
                                    "add": {
                                        "component_groups": [
                                            "attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 20,
                                    "add": {
                                        "component_groups": [
                                            "range_attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 10
                                }
                            ]
                        },
                        // 如果玩家距离超过5个区块且实体仍有目标，则运行
                        {
                            "filters": {
                                "all_of": [
                                    {
                                        "test": "distance_to_nearest_player",
                                        "operator": ">",
                                        "value": 5.0
                                    },
                                    {
                                        "test": "has_target",
                                        "operator": "equals",
                                        "value": true
                                    }
                                ]
                            },
                            "randomize": [
                                {
                                    "weight": 30,
                                    "add": {
                                        "component_groups": [
                                            "attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 60,
                                    "add":{
                                        "component_groups": [
                                            "range_attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 10
                                }
                            ]
                        }
                    ]
                },
                // 如果实体被剃毛（低于半血）
                {
                    "filters": {
                        "test": "has_component",
                        "value": "minecraft:is_sheared"
                    },
                    "sequence": [
                        // 如果玩家在5个区块内运行
                        {
                            "filters": {
                                "test": "distance_to_nearest_player",
                                "operator": "<=",
                                "value": 5.0
                            },
                            "randomize": [
                                {
                                    "weight": 20,
                                    "add":{
                                        "component_groups": [
                                            "explode"
                                        ]
                                    }
                                },
                                {
                                    "weight": 60,
                                    "add": {
                                        "component_groups": [
                                            "strong_attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 20,
                                    "add": {
                                        "component_groups": [
                                            "strong_range_attack"
                                        ]
                                    }
                                }
                            ]
                        },
                        // 如果玩家距离超过5个区块且实体仍有目标，则运行
                        {
                            "filters": {
                                "all_of": [
                                    {
                                        "test": "distance_to_nearest_player",
                                        "operator": ">",
                                        "value": 5.0
                                    },
                                    {
                                        "test": "has_target",
                                        "operator": "equals",
                                        "value": true
                                    }
                                ]
                            },
                            "randomize": [
                                {
                                    "weight": 60,
                                    "add": {
                                        "component_groups": [
                                            "strong_range_attack"
                                        ]
                                    }
                                },
                                {
                                    "weight": 40,
                                    "randomize": [
                                        {
                                            "weight": 30,
                                            "trigger": "rapid_fire"
                                        },
                                        {
                                            "weight": 70,
                                            "add": {
                                                "component_groups": [
                                                    "strong_blast"
                                                ]
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}
```

</Spoiler>

### 设置属性

设置实体属性值（每个值可以设置为Molang表达式字符串的返回值）。

/// warning
字符串值将作为Molang进行评估。这意味着，要设置字符串属性，必须将值括在 `'` 中（如下例所示）。
///

```json title="minecraft:block > events"
"wiki:change_properties": {
    "set_property": {
        "wiki:boolean_property_example": false,
        "wiki:integer_property_example": "q.property('wiki:integer_property_example') + 1",
        "wiki:string_property_example": "'red'"
    }
}
```

### 触发器

触发器是一个可以在实体事件中使用的参数，根据过滤器在选择的目标上运行其他事件。我们可以使用它在实体内触发另一个事件，并将其与 `sequence` 结合使用，以便整齐地组织我们的事件。

我们还可以为事件指定过滤器和目标。目标参数将在后面详细讨论。如果以下事件由 `minecraft:interact` 组件调用，那么如果被互动的实体具有 `pig` 家族标签，它将运行玩家与该实体互动时的 `wiki:interacted` 事件。

```json title="minecraft:entity > events"
"wiki:on_interact": {
    "trigger": {
        "filters": {
            "test": "is_family",
            "subject": "self",
            "value": "pig"
        },
        "event": "wiki:interacted",
        "target": "other"
    }
}
```

/// tip
事件能够保留被调用组件的实体上下文。例如，如果事件是使用 `minecraft:interact` 组件触发的，我们可以将过滤器应用于与实体互动的玩家。然而，如果调用事件的方法没有这种上下文，使用目标将不起作用。
///

将其与 `sequence` 参数结合使用，这允许我们在多个实体中运行事件，只要有相应的上下文。我们将在目标部分中进一步讨论这一点。

```json title="minecraft:entity > events"
"wiki:on_interact": {
    "sequence": [
        {
            "trigger": {
                "event": "wiki:interacted",
                "target": "other"
            }
        },
        {
            "trigger": {
                "event": "wiki:interacted_with",
                "target": "self"
            }
        }
    ]
}
```

## 调用事件

为了让一个事件运行，我们需要知道如何激活它，这就是通过调用事件来完成的。主要有五种方法：

-   在组件内
-   在动画内
-   在动画控制器内
-   在另一个事件内
-   使用命令

一些组件允许玩家基于设置的参数调用事件。在这里，我们输入当满足参数时要运行的事件。例如，僵尸使用的 `minecraft:environment_sensor` 组件在实体处于水下时调用事件 `minecraft:start_transforming`。

```json title="minecraft:entity > components"
"minecraft:environment_sensor": {
    "triggers": {
        "filters": {
            "test": "is_underwater",
            "operator": "==",
            "value": true
        },
        "event": "minecraft:start_transforming"
    }
}
```

我们还可以在动画和动画控制器内直接在实体上运行事件。这种基于行为的动画用于在10秒后调用事件 `wiki:start_pouncing`。

```json title=""
"animation.entity.pounce_timer": {
    "timeline": {
        "10.0": "@s wiki:start_pouncing"
    },
    "animation_length": 10.1
}
```

这种基于行为的动画控制器用于在转换到 "run" 状态时调用事件 `wiki:running`。

```json title=""
"controller.animation.entity.movement":{
    "initial_state":"walk",
    "states":{
        "walk":{
            "transitions":[
                {
                    "run":"q.is_sheared"
                }
            ]
        },
        "run":{
            "on_entry":[
                "@s wiki:running"
            ],
            "transitions":[
                {
                    "walk":"!q.is_sheared"
                }
            ]
        }
    }
}
```

这里的 `@s` 用于将事件应用于实体自身。动画控制器功能强大，可以用于创建更自定义的行为，尽管它们更为高级。有关更多信息，请查看我们的[页面](../animation-controllers/animation-controllers-intro.md)。

在一个事件内，除了添加和移除组件组，我们还可以 `trigger` 其他事件。这只猪灵中的事件在 `minecraft:entity_born` 事件中调用 `spawn_baby` 事件。

```json title="minecraft:entity > events"
"minecraft:entity_born": {
    "trigger": "spawn_baby"
}
```

我们还可以使用命令 `/event` 在实体上激活事件。以下命令将组件组 `wiki:example` 添加到所有猪。
`/event entity @e[type=minecraft:pig] wiki:example`。

### 在其他实体中调用事件

一些组件，例如伤害传感器，可以在调用事件时目标其他实体。特别设计用于在其他实体中调用事件的组件是 `minecraft:behavior.send_event`。我们将首先讨论这个组件。

`minecraft:behavior.send_event` 组件用于在召唤师的激活范围内调用任何蓝色羊群中的 `wololo` 事件。

```json title=""
"minecraft:behavior.send_event": {
    "priority": 3,
    "event_choices": [
        {
            "min_activation_range": 0.0,
            "max_activation_range": 16.0,
            "cooldown_time": 5.0,
            "cast_duration": 3.0,
            "particle_color": "#FFB38033",
            "weight": 3,
            "filters": {
                "all_of": [
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "sheep"
                    },
                    {
                        "test": "is_color",
                        "subject": "other",
                        "value": "blue"
                    }
                ]
            },
            "start_sound_event": "cast.spell",
            "sequence": [
                {
                    "base_delay": 2.0,
                    "event": "wololo",
                    "sound_event": "prepare.wololo"
                }
            ]
        }
    ]
}
```

你也可以在生成实体时调用事件。为此，在可以召唤实体的组件的字符串末尾添加 `<my:event_name>`。

```json title="BP/entities/zombie.json#component_groups/minecraft:convert_to_drowned"
"minecraft:transformation": {
    "into": "minecraft:drowned<minecraft:as_adult>",
    "transformation_sound": "convert_to_drowned",
    "drop_equipment": true,
    "delay": {
        "value":15
    }
}
```

### 目标

`minecraft:damage_sensor` 组件内的组件调用事件 `minecraft:gain_bad_omen` 给杀死它的玩家。注意事件的目标被设置为 "other"。

```json title=""
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "all_of": [
                    {
                        "test": "has_damage",
                        "value": "fatal"
                    },
                    {
                        "test": "is_family",
                        "subject": "other",
                        "value": "player"
                    }
                ]
            },
            "event": "minecraft:gain_bad_omen",
            "target": "other"
        }
    }
}
```

一些组件具有这些 `targets`，每个组件都有特定的可用目标。例如，`minecraft:interact` 的目标可以是 `self` 或 `other`，其中 `other` 是与实体互动的实体。所有有效的组件都应该有 `self` 和 `target` 作为选项，其中 `target` 是目标实体。

### 内置事件

通常，使用原版生物的组件组不会起作用。例如，除非使用上述方法之一调用，否则 `minecraft:convert_to_drowned` 不会在你的实体中被调用。然而，有一些事件在满足条件时会自动调用：

-   `minecraft:entity_spawned` ：当实体生成时调用。适用于设置初始组件组。
-   `minecraft:entity_born` ：当通过繁殖生成实体时调用。
-   `minecraft:entity_transformed` ：当另一个实体转变为此实体时调用。
-   `minecraft:on_prime` ：当实体的引信被点燃并准备爆炸时调用。

一个很好的使用例子是牛。这展示了我们如何确保牛在生成/转变时始终具有 `minecraft:cow_adult` 或 `minecraft:cow_baby` 之一。

```json title="BP/entities/cow.json#events"
"events": {
    "minecraft:entity_spawned": {
        "randomize": [
            {
                "weight": 95,
                "add": {
                    "component_groups": ["minecraft:cow_adult"]
                }
            },
            {
                "weight": 5,
                "add": {
                    "component_groups": ["minecraft:cow_baby"]
                }
            }
    ]
    },
    "minecraft:entity_born": {
        "add": {
            "component_groups": ["minecraft:cow_baby"]
        }
    },
    "minecraft:entity_transformed": {
        "add": {
            "component_groups": ["minecraft:cow_adult"]
        }
    }
}
```