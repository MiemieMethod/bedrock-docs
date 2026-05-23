# 飞行实体的骑乘控制

让玩家能够骑乘并控制飞行实体（例如飞龙或自制飞机）是附加包中颇受欢迎的玩法。本文介绍两种实现方式。

## 方法一：空中输入控制（推荐）

`minecraft:input_air_controlled`组件是目前推荐的飞行骑乘方式，原版快乐幽灵（Happy Ghast）也使用了这个组件。玩家骑乘后，可通过移动输入（PC上的WASD键）向摄像机面朝方向的三维空间内飞行。

该组件要求实体拥有`minecraft:movement.hover`移动类型，或没有重力。

如需让玩家按住跳跃键时实体上升，还需添加`minecraft:vertical_movement_action`组件。

### 组件配置

```json title="BP/entities/my_flyer.json > components"
"minecraft:input_air_controlled": {
    "strafe_speed_modifier": 1,
    "backwards_movement_modifier": 0.5
},
"minecraft:vertical_movement_action": {
    "vertical_velocity": 0.5
},
"minecraft:rideable": {
    "seat_count": 1,
    "interact_text": "action.interact.ride.horse",
    "family_types": ["player"],
    "seats": {
        "position": [0.0, 0.63, 0.0]
    },
    "on_rider_enter_event": "wiki:start_flying",
    "on_rider_exit_event": "wiki:stop_flying"
},
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "fall",
        "deals_damage": "no"
    }
}
```

### 组件组（重力切换）

为实现"无骑手时站在地上、有骑手时在空中飞行"的效果，通过组件组来动态切换重力：

```json title="BP/entities/my_flyer.json > component_groups"
"wiki:walking": {
    "minecraft:physics": {
        "has_gravity": true
    }
},
"wiki:flying": {
    "minecraft:physics": {
        "has_gravity": false
    },
    "minecraft:flying_speed": {
        "value": 0.08
    }
}
```

### 事件

```json title="BP/entities/my_flyer.json > events"
"wiki:start_flying": {
    "add": { "component_groups": ["wiki:flying"] },
    "remove": { "component_groups": ["wiki:walking"] }
},
"wiki:stop_flying": {
    "remove": { "component_groups": ["wiki:flying"] },
    "add": { "component_groups": ["wiki:walking"] }
}
```

## 方法二：大跳跃+缓速下落

这种方式虽然不是真正的飞行，但通过极高的跳跃力和骑乘时施加缓速下落与速度效果，能够模拟出类飞行的感觉，操作直觉较强。

### 跳跃力配置

使用`minecraft:horse.jump_strength`控制跳跃力，并可以使用范围值呈现蓄力跳跃效果：

```json title="BP/entities/my_flyer.json > components"
"minecraft:horse.jump_strength": {
    "value": { "range_min": 0.6, "range_max": 1.2 }
}
```

### 飞行效果动画控制器

当实体离地时自动给予缓速下落和速度效果，落地时清除效果：

```json title="RP/animation_controllers/my_flyer.json"
{
    "format_version": "1.10.0",
    "animation_controllers": {
        "controller.animation.wiki.flying": {
            "states": {
                "default": {
                    "transitions": [
                        { "jumping": "!q.is_on_ground" }
                    ]
                },
                "jumping": {
                    "transitions": [
                        { "default": "q.is_on_ground" }
                    ],
                    "on_entry": [
                        "/effect @s slow_falling 20000 0 true",
                        "/effect @s speed 20000 10 true"
                    ],
                    "on_exit": [
                        "/effect @s clear"
                    ]
                }
            }
        }
    }
}
```

在实体定义的`description`中注册：

```json title="BP/entities/my_flyer.json > description"
"scripts": {
    "animate": ["flying"]
},
"animations": {
    "flying": "controller.animation.wiki.flying"
}
```

/// note | 始终会下落
使用此方法时，实体飞行后最终总会落地。如需真正的悬停或持续飞行，请选择方法一。
///
