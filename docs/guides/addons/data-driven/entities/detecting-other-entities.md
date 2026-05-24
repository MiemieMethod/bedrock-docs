# 检测其他实体

有时你希望实体在感应到附近有其他特定实体时触发事件。本文介绍两种常用方法。

## 方法一：实体传感器组件

`minecraft:entity_sensor`是最直接的检测方式，直接写在实体的行为包定义文件中，无需额外的动画或控制器：

```json title="BP/entities/my_entity.json > components"
"minecraft:entity_sensor": {
    "sensor_range": 2.5,
    "relative_range": false,
    "require_all": true,
    "minimum_count": 1,
    "maximum_count": 4,
    "event_filters": {
        "test": "is_family",
        "subject": "other",
        "value": "player"
    },
    "event": "wiki:on_player_detected"
}
```

字段说明：

| 字段 | 说明 |
|---|---|
| `sensor_range` | 检测半径（格） |
| `relative_range` | 若为`true`，检测半径叠加在实体碰撞箱大小之上 |
| `require_all` | 若为`true`，所有附近实体都必须满足过滤条件才会触发；若为`false`，有一个满足即触发 |
| `minimum_count` | 触发所需的最少实体数量，默认为1 |
| `maximum_count` | 触发所需的最多实体数量，默认为-1（不限） |
| `event_filters` | 过滤条件，使用标准过滤器语法 |
| `event` | 满足条件时触发的事件名称 |

/// note | 局限性
`minecraft:entity_sensor`只支持一个传感器条目，且检测"实体离开范围"的处理方式较为复杂，需要配合其他组件实现双向检测。如需更灵活的控制，考虑使用方法二。
///

## 方法二：行为包动画 + /execute命令

通过行为包动画和`/execute`命令，可以实现更灵活的检测逻辑，支持双向检测（检测到 / 未检测到）。

### 创建检测动画

```json title="BP/animations/detection_animation.json"
{
    "format_version": "1.10.0",
    "animations": {
        "animation.wiki.find_player": {
            "animation_length": 0.05,
            "loop": true,
            "timeline": {
                "0": [
                    "/execute as @s if entity @e[type=player,r=4] run event entity @s wiki:player_detected"
                ]
            }
        },
        "animation.wiki.find_no_player": {
            "animation_length": 0.05,
            "loop": true,
            "timeline": {
                "0": [
                    "/execute as @s unless entity @e[type=player,r=4] run event entity @s wiki:no_player_detected"
                ]
            }
        }
    }
}
```

两个动画分别负责：
- `find_player`：检测到玩家时触发`wiki:player_detected`事件
- `find_no_player`：未检测到玩家时触发`wiki:no_player_detected`事件

### 创建动画控制器

这里假设`wiki:player_detected`事件会给实体添加`minecraft:is_sheared`组件（或相应的实体属性），`wiki:no_player_detected`事件会移除它：

```json title="BP/animation_controllers/my_entity.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.wiki.find_player": {
            "initial_state": "default",
            "states": {
                "default": {
                    "animations": ["find_player"],
                    "transitions": [
                        { "detected": "q.is_sheared" }
                    ]
                },
                "detected": {
                    "animations": ["find_no_player"],
                    "transitions": [
                        { "default": "!q.is_sheared" }
                    ],
                    "on_entry": ["/say 检测到玩家！"]
                }
            }
        }
    }
}
```

### 在实体定义中注册

在行为包实体定义的`description`中添加：

```json title="BP/entities/my_entity.json > description"
"animations": {
    "manage_find_player": "controller.animation.wiki.find_player",
    "find_player": "animation.wiki.find_player",
    "find_no_player": "animation.wiki.find_no_player"
},
"scripts": {
    "animate": [
        "manage_find_player"
    ]
}
```

/// tip | 灵活应用
`/execute`中的目标选择器可以替换为任意实体类型或条件，检测逻辑非常灵活。例如替换`type=player`为`type=wiki:my_other_entity`，或添加更多目标选择器参数来缩小范围。
///