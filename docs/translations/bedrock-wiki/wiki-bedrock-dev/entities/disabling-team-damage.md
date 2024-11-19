---
title: 禁用团队伤害
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - MedicalJewel105
    - Luthorius
    - TCLynx
    - QuazChick
description: 学习如何禁用玩家之间的团队伤害。
---

:::warning REALMS

此方法在游戏服务器上无效，原因是游戏服务器存在一个错误，导致行为包中的修改过的player.json文件无法生效，游戏会直接忽略它们。

这个问题可能在未来得到修复，但截至1.20.15版本仍未修复。这个问题同样适用于旧版本的Minecraft。

:::

如果你希望禁用团队伤害（即玩家无法伤害自己的队友），请为每个队友分配一个带有团队名称的标签（在本例中，我将使用`team1`、`team2`、`team3`和`team4`）。

现在将此伤害传感器组件添加到你的`player.json`的`"components": {}`中。请参阅注释以获取说明。

```json title="BP/entities/player.json#components"
"minecraft:damage_sensor": {
    "triggers": [
        {
            //如果你已经有一个伤害传感器，只需将此对象复制到"triggers"数组中
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team1" }, //玩家是否有此标签？
                                { "test": "has_tag", "subject": "other", "value": "team1" } //如果有，玩家试图伤害的实体是否有此标签？
                            ]
                        },
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team2" }, //对每个团队重复
                                { "test": "has_tag", "subject": "other", "value": "team2" }
                            ]
                        },
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team3" },
                                { "test": "has_tag", "subject": "other", "value": "team3" }
                            ]
                        },
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team4" },
                                { "test": "has_tag", "subject": "other", "value": "team4" }
                            ]
                        },
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team5" },
                                { "test": "has_tag", "subject": "other", "value": "team5" }
                            ]
                        }
                    ]
                }
            },
            "deals_damage": false //如果这些过滤器在当前攻击交互中评估为真，目标将不会受到伤害。
        }
    ]
}
```

### 投射物

由于投射物实体使用的原始过滤器，你必须使用完全不同的方法来实现这一点。

该过程使用：

- 标签
- 定时
- 条件伤害
- 函数

```json title="BP/entities/player.json#components"

//"components"
"minecraft:timer": { //用于将团队应用于附近的投射物
    "time": [         //未标记的投射物，通过事件。
        0.0,
        0.1
    ],
    "looping": true,
    "time_down_event": {
        "event": "wiki:projectile_team",
        "target": "self"
    }
},
"minecraft:hurt_on_condition": { //投射物将无法直接造成
    "damage_conditions": [        //伤害，因此我们将为
        {                          //玩家应用标签，这将触发这个...
            "filters": {
                "test": "has_tag",
                "value": "damage"
            },
            "cause": "projectile",
            "damage_per_tick": 4
        }
    ]
},
"minecraft:damage_sensor": {     //. . . 这将触发一个事件
    "triggers": {                //以移除此标签，因此伤害只
        "cause": "projectile",   //发生一次。
        "deals_damage": true,
        "on_damage": {
            "filters": {
                "test": "has_tag",
                "value": "damage"
            },
            "event": "wiki:stop_damage"
        }
    }
}

//"events"
"wiki:projectile_team": {  //此函数将根据
    "queue_command": {     //玩家拥有的团队标签应用标签。
        "command": [
            "function wiki-apply_team"
        ]
    }
},
"wiki:stop_damage": {      //此事件简单地移除伤害标签。
    "queue_command": {
        "command": [
            "tag @s remove damage"
        ]
    }
}
```

``` title="BP/functions/wiki-apply_team.mcfunction"
execute @s[tag=team1] ~ ~ ~ tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team1
execute @s[tag=team2] ~ ~ ~ tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team2
execute @s[tag=team3] ~ ~ ~ tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team3
execute @s[tag=team4] ~ ~ ~ tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team4
```

```json title="BP/entities/arrow.json"

//"components"
"on_hit": {               //命中时，触发一个事件...
   "definition_event": {
        "affect_projectile": true,
        "event_trigger": {
            "event": "wiki:hit",
            "target": "self"
        }
   },
   "remove_on_hit": {}
}

//"events"
"wiki:hit": {             //. . . 这将执行一个函数，为
   "queue_command": {       //不同团队的任何玩家应用
        "command": [
            "function wiki-apply_damage"
        ]
   }
}
```

``` title="BP/functions/wiki-apply_damage.mcfunction"
execute @s[tag=team1] ~ ~ ~ tag @p[rm=0,r=1,tag=!team1] add damage
execute @s[tag=team2] ~ ~ ~ tag @p[rm=0,r=1,tag=!team2] add damage
execute @s[tag=team3] ~ ~ ~ tag @p[rm=0,r=1,tag=!team3] add damage
execute @s[tag=team4] ~ ~ ~ tag @p[rm=0,r=1,tag=!team4] add damage
```

如果你修改`arrow.json`，请考虑组件组的结构。