# 实体攻击

实体攻击是一个需要多个系统协同的复杂话题，要让一个实体正确地攻击目标，你需要：

1. 移动与导航能力，以便接近目标
2. 目标选择组件，确定攻击谁
3. 攻击类型组件，定义如何攻击
4. 伤害与效果的配置

## 移动准备

在实体能够攻击之前，它需要先能够移动并导航到目标。请先阅读[实体移动](entity-movement.md)教程，确保你的实体具备基本的移动和导航能力。

/// warning | 不移动的实体也需要导航组件
即使是固定不动的实体（如炮塔），也需要导航组件——否则实体无法定位要射击的目标。
///

## 选择目标

### 触发敌对行为

最常用的目标选择组件是`minecraft:behavior.nearest_attackable_target`，它让实体主动搜索并锁定符合条件的目标：

```json title="BP/entities/my_entity.json（components节选）"
"minecraft:behavior.nearest_attackable_target": {
    "must_see": true,
    "reselect_targets": true,
    "within_radius": 25.0,
    "must_see_forget_duration": 17.0,
    "entity_types": [
        {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            },
            "max_dist": 48.0
        }
    ]
}
```

其他可用的目标选择组件：

| 组件 | 说明 |
|---|---|
| `minecraft:behavior.nearest_attackable_target` | 锁定满足过滤条件的最近实体 |
| `minecraft:behavior.nearest_prioritized_attackable_target` | 支持在每个过滤条件上设置`priority`字段，更精细地控制目标优先级 |
| `minecraft:behavior.defend_trusted_target` | 当被信任的实体受到攻击时，锁定攻击者 |

### 视线触发

`minecraft:lookat`组件是特殊的一类——它不主动搜索目标，而是被动响应试图与自己对视的实体：

```json title="BP/entities/enderman.json（参考原版）"
"minecraft:lookat": {
    "search_radius": 64.0,
    "set_target": true,
    "look_cooldown": 5.0,
    "filters": {
        "all_of": [
            {
                "subject": "other",
                "test": "is_family",
                "value": "player"
            },
            {
                "test": "has_equipment",
                "domain": "head",
                "subject": "other",
                "operator": "not",
                "value": "carved_pumpkin"
            }
        ]
    }
}
```

### 过滤器配置

通过`entity_types`中的过滤器，可以精确控制目标范围：

```json title="entity_types配置示例"
"entity_types": [
    {
        "filters": {
            "any_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "snow_golem"
                },
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "iron_golem"
                }
            ]
        },
        "max_dist": 24
    },
    {
        "filters": {
            "all_of": [
                {
                    "test": "is_family",
                    "subject": "other",
                    "value": "player"
                },
                {
                    "test": "has_equipment",
                    "subject": "other",
                    "domain": "head",
                    "operator": "!=",
                    "value": "turtle_helmet"
                }
            ]
        },
        "max_dist": 24
    }
]
```

上例会攻击雪傀儡、铁傀儡，以及**头部没有戴海龟头盔的**玩家。

## 攻击类型

以下是四种主要的攻击类型：

| 组件 | 说明 |
|---|---|
| `minecraft:behavior.melee_attack` | 近战攻击，对单个目标造成伤害 |
| `minecraft:behavior.ranged_attack` | 远程攻击，向目标发射弹射物 |
| `minecraft:area_attack` | 范围攻击，对半径内所有符合条件的实体造成持续伤害 |
| `minecraft:behavior.knockback_roar` | 击退咆哮，类似范围攻击但更灵活 |

### 近战攻击

近战攻击最为常见，会造成击退，命中率100%。

```json title="组件组示例"
"wiki:melee_mode": {
    "minecraft:attack": {
        "damage": 3,
        "effect_name": "slowness",
        "effect_duration": 20
    },
    "minecraft:behavior.melee_attack": {
        "priority": 3,
        "melee_fov": 90.0,
        "speed_multiplier": 1,
        "track_target": false,
        "require_complete_path": true
    }
}
```

`damage`可以是一个固定值，也可以是一个范围数组：
- `"damage": 3` — 每次造成3点伤害
- `"damage": [2, 6]` — 随机造成2到6点伤害

`effect_name`和`effect_duration`（秒）是可选的。可用的效果名称：

/// details | 可用状态效果列表
    type: info
`speed`、`slowness`、`haste`、`mining_fatigue`、`strength`、`instant_health`、`instant_damage`、`jump_boost`、`nausea`、`regeneration`、`resistance`、`fire_resistance`、`water_breathing`、`invisibility`、`blindness`、`night_vision`、`hunger`、`weakness`、`poison`、`wither`、`health_boost`、`absorption`、`saturation`、`levitation`、`fatal_poison`、`slow_falling`、`conduit_power`、`bad_omen`、`village_hero`、`darkness`
///

### 远程攻击

远程攻击组件`minecraft:behavior.ranged_attack`需要与`minecraft:shooter`配合，向目标发射弹射物：

```json title="组件组示例"
"wiki:ranged_mode": {
    "minecraft:behavior.ranged_attack": {
        "priority": 2,
        "ranged_fov": 90.0,
        "attack_interval_min": 1.0,
        "attack_interval_max": 3.0,
        "attack_radius": 15.0
    },
    "minecraft:shooter": {
        "def": "wiki:my_projectile"
    }
}
```

可以使用的原版弹射物标识符：`minecraft:arrow`、`minecraft:fireball`、`minecraft:small_fireball`、`minecraft:snowball`、`minecraft:egg`、`minecraft:ender_pearl`、`minecraft:splash_potion`、`minecraft:lingering_potion`、`minecraft:thrown_trident`、`minecraft:wither_skull`等。

如果实体手持弩，还需要先充弩后才能射击：

```json title="BP/entities/my_entity.json（components节选）"
"minecraft:behavior.charge_held_item": {
    "priority": 2,
    "items": ["minecraft:arrow"]
}
```

### 范围攻击

`minecraft:area_attack`会对一定半径内满足过滤条件的所有实体持续造成伤害，不需要目标，类似于原版凋灵花：

```json title="BP/entities/my_entity.json（components节选）"
"minecraft:area_attack": {
    "damage_range": 1,
    "damage_per_tick": 2,
    "cause": "contact",
    "entity_filter": {
        "any_of": [
            { "test": "is_family", "subject": "other", "value": "player" },
            { "test": "is_family", "subject": "other", "value": "monster" }
        ]
    }
}
```

`cause`字段决定伤害来源类型，这会影响盔甲附魔保护等效果是否生效。

### 击退咆哮

`minecraft:behavior.knockback_roar`类似范围攻击，但更灵活，可以指定击退距离、击退强度，并在咆哮结束时触发事件：

```json title="组件组示例"
"wiki:roar_mode": {
    "minecraft:behavior.knockback_roar": {
        "priority": 2,
        "duration": 0.7,
        "attack_time": 0.2,
        "knockback_damage": 1,
        "knockback_horizontal_strength": 1,
        "knockback_vertical_strength": 1,
        "knockback_range": 5,
        "knockback_filters": {
            "test": "is_family",
            "subject": "other",
            "value": "player"
        },
        "damage_filters": {
            "test": "is_family",
            "subject": "other",
            "value": "player"
        },
        "on_roar_end": {
            "event": "wiki:after_roar"
        },
        "cooldown_time": 10
    }
}
```

击退咆哮会产生粒子效果，如需禁用可在资源包的`particles`文件夹中覆盖`knockback_roar.json`。

## 进阶：难度自适应攻击

通过将不同难度的配置放在各自的组件组中，可以实现难度越高伤害越大的效果：

```json title="component_groups节选"
"wiki:easy_attack": {
    "minecraft:attack": { "damage": 2 }
},
"wiki:normal_attack": {
    "minecraft:attack": { "damage": 2, "effect_name": "poison", "effect_duration": 10 }
},
"wiki:hard_attack": {
    "minecraft:attack": { "damage": 2, "effect_name": "poison", "effect_duration": 18 }
}
```

## 进阶：动态切换攻击模式

使用组件组和事件可以让实体在近战与远程之间切换。典型的触发条件是目标距离（`minecraft:target_nearby_sensor`）或环境（`minecraft:environment_sensor`）。

### 定义攻击组件组

```json title="component_groups节选"
"wiki:ranged_components": {
    "minecraft:shooter": { "def": "wiki:projectile" },
    "minecraft:behavior.ranged_attack": {
        "priority": 3,
        "attack_interval_min": 1.0,
        "attack_interval_max": 3.0,
        "attack_radius": 15.0
    }
},
"wiki:melee_components": {
    "minecraft:attack": { "damage": 6 },
    "minecraft:behavior.melee_attack": { "priority": 3 }
}
```

### 定义切换事件

```json title="events节选"
"wiki:switch_to_melee": {
    "remove": { "component_groups": ["wiki:ranged_components"] },
    "add": { "component_groups": ["wiki:melee_components"] }
},
"wiki:switch_to_ranged": {
    "remove": { "component_groups": ["wiki:melee_components"] },
    "add": { "component_groups": ["wiki:ranged_components"] }
}
```

### 定义传感器触发

```json title="组件组节选"
"wiki:switcher": {
    "minecraft:target_nearby_sensor": {
        "inside_range": 4.0,
        "outside_range": 5.0,
        "must_see": true,
        "on_inside_range": {
            "event": "wiki:switch_to_melee",
            "target": "self"
        },
        "on_outside_range": {
            "event": "wiki:switch_to_ranged",
            "target": "self"
        }
    }
}
```

/// tip | 可以有更多攻击模式
攻击模式不限于两种！只要对应地增加组件组、事件和传感器，你可以设计任意多种攻击模式组合。
///
