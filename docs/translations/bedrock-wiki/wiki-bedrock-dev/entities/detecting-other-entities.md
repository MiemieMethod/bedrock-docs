---
title: 检测其他实体
category: 教程
tags:
    - 中级
mentions:
    - ANightDazingZoroark
    - SmokeyStack
    - MedicalJewel105
    - SirLich
    - Luthorius
    - TheItsNameless
description: 当其他实体靠近时触发事件。
---

你可能想过让你的实体在其他实体靠近时触发事件。本文详细介绍了各种已知的方法来实现这一点。

## minecraft:entity_sensor

这可能是检测其他实体的最基本方法。主要问题是它只接受一个条目，测试实体是否超出范围可能非常棘手。由于它是一个实体组件，你可以直接将其放入你的实体行为文件中，并编辑Minecraft过滤器。以下是一个示例：

```json title="BP/entities/my_entity.json#components"
"minecraft:entity_sensor": {
    "sensor_range": 2.5, //这是它将检测其他实体的半径（以区块为单位）
    "relative_range": false, //如果为true，传感器范围将在实体的碰撞箱大小上加成
    "require_all": true, //如果为true，所有附近的实体必须通过过滤条件才能发送事件
    "minimum_count": 1, //触发事件所需的最小实体数量，默认为1
    "maximum_count": 4, //触发事件所需的最大实体数量，默认为-1，表示无限
    "event_filters": { //你可以在这里放置任何过滤器，这个示例中使用的过滤器仅检测玩家
        "test": "is_family",
        "subject": "other",
        "value": "player"
    },
    "event": "event:on_player_detected" //当event_filters中的所有条件满足时触发的事件
}
```

## `/execute`

使用自1.19.50版本引入的新`/execute`命令，你可以在其他实体靠近时执行命令。

你将遵循的这个示例将使猪在检测到玩家时说“哼哼”，不过你可以将其替换为你想要的任何内容。首先，复制并粘贴以下BP动画。

```json title="BP/animations/detection_animation.json"
{
        "format_version": "1.10.0",
        "animations": {
                "animation.pig.find_player": {
                        "animation_length": 0.05,
                        "loop": true,
                        "timeline": {
                                "0": [
                                        "/execute as @s if entity @e[type=player, r=4] run event entity @s wiki:player_detected"
                                ]
                        }
                },
                "animation.pig.find_no_player": {
                        "animation_length": 0.05,
                        "loop": true,
                        "timeline": {
                                "0": [
                                        "/execute as @s unless entity @e[type=player, r=4] run event entity @s wiki:no_player_detected"
                                ]
                        }
                }
        }
}
```

第一个用于检测实体是否存在，另一个用于检测实体是否不存在。`/execute`命令中的`/event`部分使用的事件可以用于添加[虚拟组件](../entities/dummy-components.md)或更新[实体属性](https://learn.microsoft.com/en-us/minecraft/creator/documents/introductiontoentityproperties)。

接下来，复制并粘贴以下BP动画控制器。这假设你已设置`/execute`命令的`/event`部分以添加或移除`minecraft:is_sheared`。

```json title="BP/animation_controllers/pig_animation_controllers.json"
{
        "format_version": "1.10.0",
        "animation_controllers": {
                "controller.animation.pig_find_player": {
                        "initial_state": "default",
                        "states": {
                                "default": {
                                        "animations": ["find_player"],
                                        "transitions": [
                                                {
                                                        "detected": "q.is_sheared"
                                                }
                                        ]
                                },
                                "detected": {
                                        "animations": ["find_no_player"],
                                        "transitions": [
                                                {
                                                        "default": "!q.is_sheared"
                                                }
                                        ],
                                        "on_entry": ["/say oink oink"]
                                }
                        }
                }
        }
}
```

最后，将以下代码片段复制并粘贴到猪类的行为文件中。确保将其插入到`description`中。

```json title="BP/entities/my_entity.json#description"
"animations": {
        "manage_find_player": "controller.animation.pig_find_player",
        "find_player": "animation.pig.find_player",
        "find_no_player": "animation.pig.find_no_player"
},
"scripts": {
    "animate": [
            "manage_find_player"
        ]
}
```

## Molang、BP动画和动画控制器

`for_each`函数和`q.get_nearby_entities`或`q.get_nearby_entities_except_self`也可以用于检测其他实体。它们比使用`minecraft:entity_sensor`更有效，因为它们更擅长检测你想要检测的实体是否离开，而不是使用`minecraft:entity_sensor`。唯一的缺点是它们仍处于实验阶段。

就像在前面的方法中一样，我们将使猪在检测到玩家时说“哼哼”，不过你可以将其替换为你想要的任何内容。首先，复制并粘贴以下BP动画：

```json title="BP/animations/detection_animation.json"
{
	"format_version": "1.10.0",
	"animations": {
		"animation.pig.find_player": {
			"animation_length": 0.05,
			"loop": true,
			"timeline": {
				"0": [
					"v.x = 0.0; for_each(t.player, q.get_nearby_entities_except_self(16, 'minecraft:player'), { v.x = v.x + 1; }); return v.x > 0.0;"
				]
			}
		}
	}
}
```

`q.get_nearby_entities_except_self`需要的第一个参数是它将检测其他实体的半径（以区块为单位）。第二个参数是你想要检测的生物的标识符。

现在这很好，但如果你想让猪通过某个可以用Molang检测的属性来检测玩家，可以使用以下代码。

```json title="BP/animations/detection_animation.json"
{
	"format_version": "1.10.0",
	"animations": {
		"animation.pig.find_player": {
			"animation_length": 0.05,
			"loop": true,
			"timeline": {
				"0": [
					"v.x = 0.0; for_each(t.player, q.get_nearby_entities_except_self(2, 'minecraft:player'), { v.x = v.x + (t.player -> q.is_sheared); }); return v.x > 0.0;"
				]
			}
		}
	}
}
```

接下来，复制并粘贴以下BP动画控制器：

```json title="BP/animation_controllers/pig_animation_controllers.json"
{
	"format_version": "1.10.0",
	"animation_controllers": {
		"controller.animation.pig_find_player": {
			"initial_state": "default",
			"states": {
				"default": {
					"animations": ["find_player"],
					"transitions": [
						{
							"detected": "v.x > 0"
						}
					]
				},
				"detected": {
					"animations": ["find_player"],
					"transitions": [
						{
							"default": "v.x <= 0"
						}
					],
					"on_entry": ["/say oink oink"]
				}
			}
		}
	}
}
```

最后，将以下代码片段复制并粘贴到猪类的行为文件中。确保将其插入到`description`中。

```json title="BP/entities/my_entity.json#description"
"animations": {
	"manage_find_player": "controller.animation.pig_find_player",
	"find_player": "animation.pig.find_player"
},
"scripts": {
    "animate": [
	    "manage_find_player"
	]
}
```