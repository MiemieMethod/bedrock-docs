# 睡眠实体

本文介绍两种让实体进入睡眠状态的方式：像村民一样睡床，以及像狐狸一样打盹。

## 睡床

这种行为的灵感来自原版村民——实体夜晚会寻找床铺并在其中睡觉，白天或被打扰时醒来。

### 功能概述

- 实体在夜晚入睡，在白天醒来
- 玩家与实体交互可将其叫醒，等待一段时间后实体会再次入睡
- 实体受到攻击时自动醒来

### 行为包配置

#### 基础组件

首先，你的实体需要一个导航组件，否则它无法移动到床的位置。然后添加以下组件：

```json title="BP/entities/sleeping_entity.json > components"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "can_find_poi": true
}
```

/// note | 关于此组件
`minecraft:dweller`是让实体具备睡床能力的必要组件，目前官方文档中记录不完整。
///

```json title="BP/entities/sleeping_entity.json > components"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "is_daytime",
                "value": false
            },
            "event": "wiki:sleep"
        }
    ]
}
```

这个传感器在夜晚触发`wiki:sleep`事件，让实体开始准备入睡。

#### 组件组

```json title="BP/entities/sleeping_entity.json > component_groups"
"wiki:sleeping": {
    "minecraft:behavior.sleep": {
        "priority": 0,
        "goal_radius": 1.5,
        "speed_multiplier": 1.25,
        "sleep_collider_height": 0.3,
        "sleep_collider_width": 1,
        "sleep_y_offset": 0.6,
        "timeout_cooldown": 10
    },
    "minecraft:damage_sensor": {
        "triggers": {
            "on_damage": {
                "event": "wiki:wake_up"
            }
        }
    },
    "minecraft:environment_sensor": {
        "triggers": [
            {
                "filters": {
                    "test": "is_daytime",
                    "value": true
                },
                "event": "wiki:wake_up"
            }
        ]
    },
    "minecraft:interact": {
        "interactions": [
            {
                "on_interact": {
                    "filters": {
                        "all_of": [
                            {
                                "test": "is_family",
                                "subject": "other",
                                "value": "player"
                            }
                        ]
                    },
                    "event": "wiki:woken_up"
                }
            }
        ]
    }
},
"wiki:sleep_timer": {
    "minecraft:timer": {
        "time": 15,
        "time_down_event": {
            "event": "wiki:sleep_again"
        }
    }
}
```

- `minecraft:behavior.sleep`：实体的睡眠AI意向，优先级必须为`0`（最高）
- `minecraft:damage_sensor`：受伤时触发`wiki:wake_up`事件
- `minecraft:environment_sensor`：白天触发`wiki:wake_up`事件
- `minecraft:interact`：玩家点击时触发`wiki:woken_up`事件
- `wiki:sleep_timer`：玩家叫醒实体后，15秒后重新入睡

#### 事件

```json title="BP/entities/sleeping_entity.json > events"
"wiki:sleep": {
    "add": { "component_groups": ["wiki:sleeping"] }
},
"wiki:wake_up": {
    "remove": { "component_groups": ["wiki:sleeping"] }
},
"wiki:woken_up": {
    "remove": { "component_groups": ["wiki:sleeping"] },
    "add": { "component_groups": ["wiki:sleep_timer"] }
},
"wiki:sleep_again": {
    "add": { "component_groups": ["wiki:sleeping"] },
    "remove": { "component_groups": ["wiki:sleep_timer"] }
}
```

### 资源包配置

你需要为实体添加睡眠动画和对应的动画控制器。

#### 睡眠动画

```json title="RP/animations/sleeping_entity.animation.json"
{
    "format_version": "1.8.0",
    "animations": {
        "animation.sleeping_entity.sleep": {
            "loop": "hold_on_last_frame",
            "animation_length": 0.5,
            "bones": {
                "body": {
                    "rotation": {
                        "0.0": [0, 0, 0],
                        "0.5": [-90, 0, 0]
                    },
                    "position": [0, 2, -15]
                }
            }
        }
    }
}
```

#### 动画控制器

```json title="RP/animation_controllers/sleeping_entity.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.sleeping_entity.sleep": {
            "initial_state": "default",
            "states": {
                "default": {
                    "transitions": [
                        { "sleep": "q.is_sleeping" }
                    ]
                },
                "sleep": {
                    "animations": ["sleeping"],
                    "transitions": [
                        { "default": "!q.is_sleeping" }
                    ]
                }
            }
        }
    }
}
```

动画在客户端实体定义中注册：
```json
"sleeping": "animation.sleeping_entity.sleep"
```

## 打盹

这种行为的灵感来自原版狐狸——实体在感到安全时自发打盹，靠近时会被吵醒。

### 功能概述

- 实体在安全、远离生物且天气不是雷暴时入睡
- 接近实体会将其吵醒，但被信任的玩家（蹲行）或同族实体不会打扰它
- 受到攻击时自动醒来

### 行为包配置

打盹行为只需一个组件：

```json title="BP/entities/sleeping_entity.json > components"
"minecraft:behavior.nap": {
    "priority": 8,
    "cooldown_min": 2.0,
    "cooldown_max": 7.0,
    "mob_detect_dist": 12.0,
    "mob_detect_height": 6.0,
    "can_nap_filters": {
        "all_of": [
            {
                "test": "in_water",
                "subject": "self",
                "operator": "==",
                "value": false
            },
            {
                "test": "on_ground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_underground",
                "subject": "self",
                "operator": "==",
                "value": true
            },
            {
                "test": "weather_at_position",
                "subject": "self",
                "operator": "!=",
                "value": "thunderstorm"
            }
        ]
    },
    "wake_mob_exceptions": {
        "any_of": [
            {
                "test": "trusts",
                "subject": "other",
                "operator": "==",
                "value": true
            },
            {
                "test": "is_family",
                "subject": "other",
                "operator": "==",
                "value": "sleeping_entity"
            },
            {
                "test": "is_sneaking",
                "subject": "other",
                "operator": "==",
                "value": true
            }
        ]
    }
}
```

如需支持"信任"机制（如驯服后的实体），还需添加：

```json title="BP/entities/sleeping_entity.json > components"
"minecraft:trust": {}
```

### 资源包配置

动画控制器与睡床部分相同，可复用。使用`q.is_sleeping`作为转移条件，当实体进入打盹状态时`q.is_sleeping`会返回`true`。不要忘记为你的实体创建并注册专属的睡眠动画，可参考[Blockbench动画教程](../../tools/blockbench/how-to-use.md)。
