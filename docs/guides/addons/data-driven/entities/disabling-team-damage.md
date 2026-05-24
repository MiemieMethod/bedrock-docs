# 禁用队伍伤害

在多人游戏地图中，让同队玩家互相免疫伤害是常见需求。本文介绍如何通过修改玩家实体文件来实现这一功能。

/// warning | Realms上无效
截至1.20.15版本，在Realms上，行为包中修改过的`player.json`会被游戏**直接忽略**，导致此方案无效。这是Realms的已知问题，不只影响此功能，而是影响所有对玩家实体的自定义。此问题同样影响旧版本。如需在Realms上实现类似功能，请使用脚本API的伤害事件来处理。
///

## 禁用近战伤害

通过`minecraft:damage_sensor`组件，可以过滤掉来自同队玩家的伤害。你需要为每个队伍中的玩家添加对应的标签（例如`team1`、`team2`等），然后在`player.json`中加入以下组件：

```json title="BP/entities/player.json > minecraft:entity > components"
"minecraft:damage_sensor": {
    "triggers": [
        {
            "on_damage": {
                "filters": {
                    "any_of": [
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team1" },
                                { "test": "has_tag", "subject": "other", "value": "team1" }
                            ]
                        },
                        {
                            "all_of": [
                                { "test": "has_tag", "value": "team2" },
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
                        }
                    ]
                }
            },
            "deals_damage": "no"
        }
    ]
}
```

逻辑说明：
- `subject`默认为`self`（攻击方），`subject: "other"`指被攻击方
- 当攻击方和被攻击方**都拥有相同的队伍标签**时，伤害被取消
- `any_of`保证任意一个队伍的条件成立即可触发

如果你的`player.json`已经有了`minecraft:damage_sensor`，只需将这个对象添加到已有的`triggers`数组中即可。

## 禁用弹射物伤害

弹射物实体的过滤器功能有限，无法直接检测攻击方的标签，因此需要一套不同的机制：

**流程**：
1. 玩家的计时器每刻触发，将自己的队伍标签传递给附近无标签的弹射物
2. 弹射物命中时，只对非同队玩家添加`damage`标签
3. 玩家身上的`hurt_on_condition`组件响应`damage`标签造成伤害
4. 伤害发生后立即移除`damage`标签

### 修改player.json

在`components`中添加：

```json title="BP/entities/player.json > minecraft:entity > components（追加）"
"minecraft:timer": {
    "time": [0, 0],
    "looping": true,
    "time_down_event": {
        "event": "wiki:projectile_team",
        "target": "self"
    }
},
"minecraft:hurt_on_condition": {
    "damage_conditions": [
        {
            "filters": {
                "test": "has_tag",
                "value": "damage"
            },
            "cause": "projectile",
            "damage_per_tick": 4
        }
    ]
},
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "projectile",
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
```

在`events`中添加：

```json title="BP/entities/player.json > minecraft:entity > events（追加）"
"wiki:projectile_team": {
    "queue_command": {
        "command": ["function wiki-apply_team"]
    }
},
"wiki:stop_damage": {
    "queue_command": {
        "command": ["tag @s remove damage"]
    }
}
```

### 创建函数文件

```mcfunction title="BP/functions/wiki-apply_team.mcfunction"
execute as @s[tag=team1] at @s run tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team1
execute as @s[tag=team2] at @s run tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team2
execute as @s[tag=team3] at @s run tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team3
execute as @s[tag=team4] at @s run tag @e[rm=0,r=1,c=1,type=arrow,tag=] add team4
```

```mcfunction title="BP/functions/wiki-apply_damage.mcfunction"
execute as @s[tag=team1] at @s run tag @p[rm=0,r=1,tag=!team1] add damage
execute as @s[tag=team2] at @s run tag @p[rm=0,r=1,tag=!team2] add damage
execute as @s[tag=team3] at @s run tag @p[rm=0,r=1,tag=!team3] add damage
execute as @s[tag=team4] at @s run tag @p[rm=0,r=1,tag=!team4] add damage
```

### 修改arrow.json

```json title="BP/entities/arrow.json > minecraft:entity > components（追加）"
"minecraft:projectile": {
    "on_hit": {
        "definition_event": {
            "affect_projectile": true,
            "event_trigger": {
                "event": "wiki:hit",
                "target": "self"
            }
        },
        "remove_on_hit": {}
    }
}
```

```json title="BP/entities/arrow.json > minecraft:entity > events（追加）"
"wiki:hit": {
    "queue_command": {
        "command": ["function wiki-apply_damage"]
    }
}
```

/// note | 组件组兼容性
如果你的`arrow.json`中已经有了`minecraft:projectile`，需要注意组件组（component_groups）可能也定义了该组件，修改时要确保所有相关的组件组也做了对应修改。
///