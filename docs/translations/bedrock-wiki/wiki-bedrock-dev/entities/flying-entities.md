---
title: 飞行实体
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - Joelant05
    - Dreamedc2015
    - MedicalJewel105
    - aexer0e
    - imsolucid
    - nebulacrab
    - Luthorius
    - TheItsNameless
    - Halo333X
description: 学习如何为你的实体创建飞行行为。
---

无论是制作飞机还是龙，为飞行实体添加可控性可能会挑战大多数没有接触过这个概念的开发者。由于没有“正确”的方法来为飞行实体添加驾驶机制，我将展示三种主要的变通方法，供你使用。

## 大跳跃，缓慢下落

虽然不完全是“飞行”，但将实体的跳跃力量设置得很高，并在下落时给予缓慢下落和速度效果，可能是最简单的方法。

要实现这一点，我们需要为实体添加 `"minecraft:horse.jump_strength"` 组件。添加此组件后，你可以控制其跳跃力量，并在玩家按下跳跃按钮时禁用下马。

<CodeHeader></CodeHeader>

```json
"minecraft:horse.jump_strength": {
    "value": 7
}
```

我们还可以将 `"value"` 作为对象来利用玩家按住跳跃按钮时看到的 **范围条**。

<CodeHeader></CodeHeader>

```json
"minecraft:horse.jump_strength": {
    "value": { "range_min": 0.6, "range_max": 1.2 }
}
```

现在我们将在下落时给予实体缓慢下落和速度效果，以防止其瞬间下落。为此，我们将创建一个动画控制器，并在实体不在地面时给予这些效果，如下所示：

（你可以在 [这里](../animation-controllers/entity-commands.md) 阅读关于如何使用动画控制器执行命令的教程。）

<CodeHeader></CodeHeader>

```json
"controller.animation.dragon.flying":{
    "states":{
        "default":{
            "transitions":[
                {
                    "jumping":"!q.is_on_ground"
                }
            ]
        },
        "jumping":{
            "transitions":[
                {
                    "default":"q.is_on_ground"
                }
            ],
            "on_entry":[
                "/effect @s slow_falling 20000 0 true",
                "/effect @s speed 20000 10 true"
            ],
            "on_exit":[
                "/effect @s clear"
            ]
        }
    }
}
```

我们还需要将其连接到我们的实体，如下所示：

<CodeHeader></CodeHeader>

```json
"description":{
    "identifier":"wiki:dragon",
    "is_spawnable":true,
    "is_summonable":true,
    "is_experimental":false,
    "scripts":{
        "animate":[
            "flying"
        ]
    },
    "animations":{
        "flying":"controller.animation.dragon.flying"
    }
}
```

现在，我们应该至少有一个类似于飞行的机制。你可以更改像 jump_strength 和 speed 这样的值，但使用此方法时，实体总是会下落。

## 通过视角控制

这可能是控制飞行实体的最流行方法，与第一种方法不同，这种方法使玩家能够控制实体的垂直移动，因此你不必每次跳跃时都下落，缺点是你不能在不改变实体垂直轨迹的情况下自由查看周围。

此方法检测骑乘玩家的垂直旋转，并相应地将漂浮/缓慢下落效果应用于实体。

有多种方法可以实现这一点，但在本教程中，我们将使用目标选择器 `rym`（最小 y 旋转）和 `ry`（最大 y 旋转）在一系列重复的命令方块中检测玩家的俯仰，并根据范围给予我们的实体漂浮或缓慢下落。

<CodeHeader></CodeHeader>

```
execute as @a[rxm=-90,rx=-25] run effect @e[type=wiki:dragon,r=1] levitation 1 6 true
execute as @a[rxm=-25,rx=-15] run effect @e[type=wiki:dragon,r=1] levitation 1 3 true
execute as @a[rxm=-15,rx=-5] run effect @e[type=wiki:dragon,r=1] levitation 1 2 true
execute as @a[rxm=-5,rx=20] run effect @e[type=wiki:dragon,r=1] levitation 1 1 true
execute as @a[rxm=20,rx=35] run effect @e[type=wiki:dragon,r=1] slow_falling 1 1 true
execute as @a[rxm=35,rx=90] run effect @e[type=wiki:dragon,r=1] clear
```

**根据你的实体大小和玩家座位距离其支点的远近，你可能需要将半径 `r` 更改为更大的值。**

在重复命令方块中运行这些命令后，你应该可以通过上下看来控制其垂直移动，或者你可以使用一个简单的动画控制器并将其链接到实体，以便它始终播放该功能。

建议将此动画控制器链接到玩家。

<CodeHeader></CodeHeader>

```json
{
	"format_version": "1.10.0",
	"animation_controllers": {
		"controller.animation.base": {
			"initial_state": "default",
			"states": {
				"default": {
					"transitions": [
						{
							"base": "(1.0)"
						}
					],
					"on_entry": [
                        "/function dragon_control"
                    ]
				},
				"base": {
					"transitions": [
						{
							"default": "(1.0)"
						}
					],
					"on_entry": [
                        "/function dragon_control"
                    ]
				}
			}
		}
	}
}
```

当飞行时，实体可能仍然太慢，因此我们将借用第一种方法的动画控制器，并进行一些更改，以在飞行时给予实体速度。

<CodeHeader></CodeHeader>

```json
"controller.animation.dragon.flying":{
    "states":{
        "default":{
            "transitions":[
                {
                    "jumping_1":"!q.is_on_ground"
                }
            ]
        },
        "jumping_1":{
            "transitions":[
                {
                    "transition_to_default":"q.is_on_ground"
                },
                {
                    "jumping_2":"true"
                }
            ],
            "on_entry":[
                "/effect @s speed 15 10 true"
            ]
        },
        "jumping_2":{
            "transitions":[
                {
                    "transition_to_default":"q.is_on_ground"
                },
                {
                    "jumping_1":"true"
                }
            ],
            "on_entry":[
                "/effect @s speed 15 10 true"
            ]
        },
        "transition_to_default":{
            "transitions":[
                {
                    "transition_to_default":"true"
                }
            ],
            "on_entry":[
                "/effect @s clear"
            ]
        }
    }
}
```

_由于在飞行时可能会清除实体的效果，我们更改了动画控制器，以便在实体不在地面时每个刻都给予其速度。_

你可能还会注意到，当你靠近实体时，它会漂浮。我们可以通过在骑乘时给予实体一个标签（在不骑乘时移除它），并仅在实体拥有该标签时应用这些效果，来修复此问题。我们可以创建并动画化另一个动画控制器，并更新我们的命令。

<CodeHeader></CodeHeader>

```json
"controller.animation.dragon.test_rider":{
    "states":{
        "default":{
            "transitions":[
                {
                    "has_rider":"q.has_rider"
                }
            ]
        },
        "has_rider":{
            "transitions":[
                {
                    "default":"!q.has_rider"
                }
            ],
            "on_entry":[
                "/tag @s add has_rider"
            ],
            "on_exit":[
                "/tag @s remove has_rider"
            ]
        }
    }
}
```

<CodeHeader></CodeHeader>

```
execute as @a[rxm=-90,rx=-25] run effect @e[type=wiki:dragon,r=1,tag=has_rider] levitation 1 6 true
execute as @a[rxm=-25,rx=-15] run effect @e[type=wiki:dragon,r=1,tag=has_rider] levitation 1 3 true
execute as @a[rxm=-15,rx=-5] run effect @e[type=wiki:dragon,r=1,tag=has_rider] levitation 1 2 true
execute as @a[rxm=-5,rx=20] run effect @e[type=wiki:dragon,r=1,tag=has_rider] levitation 1 1 true
execute as @a[rxm=20,rx=35] run effect @e[type=wiki:dragon,r=1,tag=has_rider] slow_falling 1 1 true
execute as @a[rxm=35,rx=90] run effect @e[type=wiki:dragon,r=1,tag=has_rider] clear
```

## 通过跳跃控制

第三种控制飞行实体的方法使用玩家的跳跃按钮。当玩家按住跳跃按钮时，实体上升；当他们释放跳跃按钮时，实体下落。

为此，我们需要一个附加到玩家的动画控制器，而不是实体本身，以检测玩家何时使用跳跃按钮。我们还需要在玩家按下跳跃按钮时禁用下马。

首先，在实体上禁用下马和跳跃：

<CodeHeader></CodeHeader>

```json
"minecraft:horse.jump_strength": {
    "value": 0
},
"minecraft:can_power_jump": {}
```

接下来，我们需要一个动画控制器，当玩家使用跳跃按钮时使实体漂浮，并在他们释放跳跃按钮时重置漂浮。

<CodeHeader></CodeHeader>

```json
"controller.animation.fly_dragon":{
    "initial_state":"falling",
    "states":{
        "falling":{
            "on_entry":[
                "/effect @e[type=wiki:dragon,r=1,c=1] levitation 0"
            ],
            "transitions":[
                {
                    "rising":"q.is_jumping"
                }
            ]
        },
        "rising":{
            "on_entry":[
                "/effect @e[type=wiki:dragon,r=1,c=1] levitation 100000 6 true"
            ],
            "transitions":[
                {
                    "falling":"!q.is_jumping"
                }
            ]
        }
    }
}
```

现在，我们需要玩家行为文件的副本，我们将稍作修改。你可以在 Mojang 提供的原版行为包中找到玩家的行为文件（可以在 [这里](https://aka.ms/behaviorpacktemplate) 找到）。将玩家的行为文件复制到你自己的行为包后，找到他们的 `"description"` 对象并添加动画控制器。我们还希望确保实体仅在玩家骑乘时对玩家的跳跃输入做出响应，因此我们可以在玩家的行为中使用 Molang 查询，仅在玩家骑乘时激活动画控制器。

<CodeHeader></CodeHeader>

```json
"description":{
    "identifier":"minecraft:player",
    "is_spawnable":false,
    "is_summonable":false,
    "animations":{
        "fly_dragon":"controller.animation.fly_dragon"
    },
    "scripts":{
        "animate":[
            {
                "fly_dragon":"q.is_riding"
            }
        ]
    }
}
```

现在，实体可以通过跳跃键进行控制，但存在一个错误。如果玩家在按住跳跃键时下马，实体将继续上升。我们可以通过在实体本身上添加一个动画控制器来修复此问题，该控制器在玩家下马时重置漂浮。

<CodeHeader></CodeHeader>

```json
"controller.animation.reset_levitation":{
    "initial_state":"no_rider",
    "states":{
        "no_rider":{
            "transitions":[
                {
                    "has_rider":"q.has_rider"
                }
            ]
        },
        "has_rider":{
            "on_exit":[
                "/effect @s levitation 0"
            ],
            "transitions":[
                {
                    "no_rider":"!q.has_rider"
                }
            ]
        }
    }
}
```

## 通过脚本控制

第四种方法允许我们调整下落速度、移动速度，并在玩家跳跃时生效。重要的是要添加马的跳跃功能，以便当玩家跳跃时，他们不会从实体上掉下来，同时也很重要的是添加表示可以飞行的家族类型，因为我们在脚本中处理这个。

<CodeHeader>minecraft:entity</CodeHeader>

```json
"components": {
    "minecraft:behavior.player_ride_tamed": {},
    "minecraft:input_ground_controlled": {},
    "minecraft:can_power_jump": {},
    "minecraft:horse.jump_strength": {
        "value": 0
    },
    "minecraft:damage_sensor": {
        "triggers": [
            {
                "cause": "fall",
                "deals_damage": false
            }
        ]
    },
    "minecraft:rideable": {
        "seat_count": 1,
        "interact_text": "action.interact.mount",
        "family_types": ["player"],
        "seats": {
            "position": [0.0, 0.63, 0.0]
        }
    },
    "minecraft:type_family": {
        "family": ["pig", "mob", "wiki:can_fly"] // 表示实体可以飞行
    }
}
```

在用之前的配置调整实体后，我们将添加脚本以赋予其功能。

<CodeHeader>BP/scripts/utils.js</CodeHeader>

```js
import { Entity } from "@minecraft/server";
class Utils {
    /**
     * @param {Entity} entity
     */
    constructor(entity) {
        this.entity = entity;
        this.rideable = entity?.getComponent("rideable");
        this.player = this.rideable?.getRiders()[0];
        this.riding = this.player?.getComponent("riding");
    }

    /**
     * @param {number} flySpeed
     * @param {number} fallSpeed
     * @param {number} XZspeed
     */
    flySystem(flySpeed, fallSpeed, XZspeed) {
        if (!this.riding) return;
        const direction = {
            x: 0,
            y: this.player.isJumping ? flySpeed : fallSpeed,
            z: 0,
        };
        this.entity.addEffect("speed", 5, {
            showParticles: false,
            amplifier: XZspeed,
        });
        this.entity.applyImpulse(direction);
    }
}

export default Utils;
```

utils.js 文件创建了一个函数，使实体能够飞行。
现在我们需要将其应用于我们的实体，以使其生效。

<CodeHeader>BP/scripts/index.js</CodeHeader>

```js
import { system, world } from "@minecraft/server";
import Utils from "./utils";

system.runInterval(() => {
    const dim = world.getDimension('overworld');
    // 你可以使用标签代替家族类型
    for (const entity of dim.getEntities({ families: [ "wiki:can_fly" ] })) {
        const utils = new Utils(entity);
        // 推荐值
        utils.flySystem(0.09, 0.07, 5);
    }
});
```

你可以从 index.js 调整速度。

-   Y 轴上的速度（向上）

    **flySpeed: 0.09**

-   Y 轴上的速度（向下）

    **fallSpeed: 0.07**

-   X 轴上的速度（水平）

    **XZspeed: 5**

这些只是推荐值，你可以自由更改速度。