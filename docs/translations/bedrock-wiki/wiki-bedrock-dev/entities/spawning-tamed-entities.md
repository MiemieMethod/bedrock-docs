---
title: 生成驯服实体
category: 教程
tags:
    - 中级
mentions:
    - Axelpvz2030
    - aexer0e
    - SirLich
    - MedicalJewel105
    - SmokeyStack
    - ThomasOrs
description: 在本教程中，你将学习如何通过在目标玩家上运行事件并投掷一个在碰撞时变为驯服实体的物品来生成一个预先驯服的实体。
---

在本教程中，你将学习如何通过在目标玩家上运行事件并投掷一个在碰撞时变为驯服实体的物品来生成一个预先驯服的实体。

## 概述

传统上，如果你想让玩家驯服一个实体，你必须强制玩家通过 `minecraft:tameable` 与该实体进行交互。然而，你也可以利用原版投射物跟踪生成它们的实体这一事实，来生成一个预先驯服的实体。

为此，我们将通过 `minecraft:spawn_entity` 召唤一个虚拟的中介投射物实体，该实体将立即转变为我们在本教程中想要生成的预先驯服的实体，即通过 `minecraft:transformation` 将其转变为原版狼，并将 `keep_owner` 设置为 `true`。

\*: _生成_ 不应与 _召唤_ 混淆。如果投射物是通过生成蛋或 `minecraft:spawn_entity` 组件生成的，它将跟踪玩家，但如果是通过 `/summon` 命令生成的则不会。

## player.json

在这里，我们需要一份玩家行为文件的副本，我们将稍作修改。我们将添加一个简单的事件，添加一个组件组，以生成我们的自定义中介实体。

你可以在 Mojang 提供的原版行为包中找到 BP 玩家实体文件 [这里](https://aka.ms/behaviorpacktemplate)。

<CodeHeader>BP/entities/player.json</CodeHeader>

```json
{
    "format_version":"1.16.0",
    "minecraft:entity":{
        "description":{
            "identifier":"minecraft:player",
            "is_spawnable":false,
            "is_summonable":false,
            "is_experimental":false
        },
        "component_groups":{
            "wiki:spawn_tamed_wolf":{
                "minecraft:spawn_entity":{
                    "entities":{
                        "min_wait_time":0,
                        "max_wait_time":0,
                        "spawn_entity":"wiki:pretamed_wolf",
                        "single_use":true,
                        "num_to_spawn":1
                    }
                }
            }
		},
        ...
		"events":{
            "wiki:spawn_tamed_wolf":{
                "add":{
                    "component_groups":[
                        "wiki:spawn_tamed_wolf"
                    ]
                }
            }
        }
    }
}
```

## pretamed_wolf.json

接下来，我们需要创建一个简单的自定义实体，该实体将具有 `minecraft:arrow` 的运行时标识符（其他投射物的运行时标识符也可以），一个空的投射物组件，以及一个转换组件以变为驯服的狼。

<CodeHeader>BP/entities/pretamed_wolf.json</CodeHeader>

```json
{
	"format_version": "1.16.0",
	"minecraft:entity": {
		"description": {
			"identifier": "wiki:pretamed_wolf",
			"runtime_identifier": "minecraft:arrow",
			"is_spawnable": false,
			"is_summonable": true,
			"is_experimental": false
		},
		"components": {
			"minecraft:projectile": {},
			"minecraft:transformation": {
				"into": "minecraft:wolf<minecraft:on_tame>",
				"keep_owner": true
			}
		}
	}
}
```

现在，你可以通过 `/event entity @p wiki:spawn_tamed_wolf` 在玩家旁边生成一只驯服的狼。你还可以通过将 `is_spawnable` 设置为 `true` 使用 `wiki:pretamed_wolf` 生成蛋来生成它！

:::warning
如果你想使用此方法生成自定义实体而不是狼，你需要确保该实体具有 `minecraft:is_tamed` 组件，以使其正常工作。否则，一些行为将无法按预期在驯服实体上正常运作。
:::

## 集成物品投射物（替代方法）

作为 [1.16 的实验性物品功能之一](/items/item-components)，`shoot` 事件属性可用于制作在碰撞时变为驯服实体的投射物。

<CodeHeader>BP/items/throwable_pretamed_wolf.json</CodeHeader>

```json
{
    "format_version":"1.16.100",
    "minecraft:item":{
        "description":{
            "identifier":"wiki:throwable_pretamed_wolf"
        },
        "components":{
            "minecraft:on_use":{
                "on_use":{
                    "event":"wiki:on_use"
                }
            }
        },
        "events":{
            "wiki:on_use":{
                "shoot":{
                    "projectile":"wiki:pretamed_wolf"
                }
            }
        }
    }
}
```

我们还需要对我们的自定义投射物实体进行一些调整，以便它在生成时不会立即转变。

<CodeHeader>BP/entities/pretamed_wolf.json</CodeHeader>

```json
{
    "minecraft:entity":{
        "description":{
            "identifier":"wiki:pretamed_wolf",
            "runtime_identifier":"minecraft:arrow",
            "is_spawnable":false,
            "is_summonable":true,
            "is_experimental":false
        },
        "component_groups":{
            "wiki:transform_to_entity":{
                "minecraft:transformation":{
                    "into":"minecraft:wolf<minecraft:on_tame>",
                    "keep_owner":true
                }
            }
        },
        "components":{
            "minecraft:projectile":{
                "on_hit":{
                    "impact_damage":{
                        "damage":0
                    },
                    "stick_in_ground":{},
                    "definition_event":{
                        "event_trigger":{
                            "event":"wiki:on_hit"
                        }
                    }
                }
            }
        },
        "events":{
            "wiki:on_hit":{
                "add":{
                    "component_groups":[
                        "wiki:transform_to_entity"
                    ]
                }
            }
        }
    }
}
```

特别感谢 [Zarkmend ZAN](https://twitter.com/Zarkmend_ZAN) 的发现 :)