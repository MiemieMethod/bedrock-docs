---
title: 实体攻击
category: 教程
mentions:
  - Luthorius
  - TheDoctor15
  - SirLich
  - MedicalJewel105
  - epxzzy
  - ThomasOrs
tags:
  - intermediate
description: 学习如何以正确的方式制作实体攻击。
---

实体攻击是一个复杂的主题，涉及许多不同的要素以确保其正常工作：

- 导航和移动能力，以靠近目标
- 目标选择能力，以决定攻击哪个实体
- 攻击类型，如近战或远程
- 攻击伤害和效果

## 选择目标

### 移动

在一个怪物能够攻击之前，它需要各种[移动组件](../entities/entity-movement.md)。

在开始创建实体攻击之前，你应该确保你的实体能够行走并导航其周围环境。

/// warning
即使你正在创建一个不移动的实体（比如炮塔），你仍然需要添加导航组件，以便实体能够找到要攻击的目标。
///

### 触发敌意

有许多方法可以触发敌意。最常见的类型 `nearest_attackable_target`，如下所示。它通常允许你定义这个实体有兴趣攻击哪些实体：

```json title=""
"minecraft:behavior.nearest_attackable_target": {
  "must_see": true, //如果为真，潜在目标必须在怪物的视线范围内
  "reselect_targets": true, //如果有更近的目标，允许怪物选择新的目标
  "within_radius": 25.0, //潜在目标必须在的半径内
  "must_see_forget_duration": 17.0, //如果 "must_see" = true，忘记目标前的时间
  "entity_types": [
    {
      "filters": { //要攻击的实体
        "test": "is_family",
        "subject": "other",
        "value": "player"
      },
      "max_dist": 48.0
    }
  ]
}
```

为了更精细的控制，你还可以考虑使用以下组件之一：

| 组件                                                    | 注释                                                            |
|---------------------------------------------------------|-----------------------------------------------------------------|
| minecraft:behavior.nearest_attackable_target           | 目标符合给定要求的实体                                          |
| minecraft:behavior.nearest_prioritized_attackable_target | 允许在每个过滤器后设置“priority”： [整数]                   |
| minecraft:behavior.defend_trusted_target               | 目标伤害任何在过滤器中指定的实体                                |

但还有一个 - `minecraft:lookat`

这个最后的组件与其他三个稍有不同，因为它用于检测并锁定试图进行眼神接触的实体。其结构如下：

```json title="BP/entities/enderman.json"
"minecraft:lookat": {
  "search_radius": 64.0,
  "set_target": true, //如果为真，成为一个有效目标
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
        "value": "carved_pumpkin"  //所有头部未装备 carved_pumpkin 的玩家
      }
    ]
  }
}
```

### 目标选择

/// tip
本节展示如何配置上述“目标选择”组件。
///

怪物通过使用[过滤器](https://bedrock.dev/docs/stable/Entities#Filters)来查找目标，可以通过 `test`、`subject`、`operator` 和 `value` 来确定哪些实体是有效目标。

```json title=""
"entity_types":[
    {
        "filters":{
            "any_of":[
                {
                    "test":"is_family",
                    "subject":"other",
                    "operator":"==",
                    "value":"snow_golem"
                },
                {
                    "test":"is_family",
                    "subject":"other",
                    "operator":"==",
                    "value":"iron_golem"
                }
                //任何等于 "snow_golem" 或 "iron_golem"
            ]
        },
        "max_dist":24
    },
    {
        "filters":{
            "all_of":[
                {
                    "test":"is_family",
                    "subject":"other",
                    "operator":"==",
                    "value":"player"
                },
                {
                    "test":"has_equipment",
                    "subject":"other",
                    "domain":"head",
                    "operator":"=!",
                    "value":"turtle_helmet"
                }
                //任何等于 player 且未在头部装备 "turtle_helmet"
            ]
        },
        "max_dist":24
    }
]
```

这将只针对 `snow_golem`，`iron_golem` 和没有佩戴 `turtle_helmet` 的 `player`。

## 攻击类型

以下是可用的攻击类型：

| 组件                                          | 注释                                                     |
|-----------------------------------------------|----------------------------------------------------------|
| [minecraft:behavior.melee_attack](#melee)     | 对单一目标造成伤害                                       |
| [minecraft:behavior.ranged_attack](#ranged)   | 向目标发射投射物                                         |
| [minecraft:area_attack](#area)                | 对范围内的所有实体进行近战攻击                           |
| [minecraft:behavior.knockback_roar](#knockback-roar) | 类似于 minecraft:area_attack，但更灵活                  |

### 近战

近战攻击是最常见的攻击类型，它会造成击退，并且在准确率上有100%的成功率。

```json title=""
"wiki:melee_attack": {
  "minecraft:attack": {
    "damage": 3,
    "effect_name": "slowness",
    "effect_duration": 20
  },
  "minecraft:behavior.melee_attack": {
    "priority": 3,
    "melee_fov": 90.0, //实体用于确定是否可以进行有效近战攻击的允许视野范围
    "speed_multiplier": 1,
    "track_target": false,
    "require_complete_path": true
  }
}
```

设置伤害，选择一个怪物效果，并更改一些附加属性。

在组件中定义的表示伤害整数的值可以是常量，或者包含两个数字的字符串，用于表示可能值的范围。

`"damage": 3` 将每次造成3点伤害

`"damage": [ 2, 6 ]` 将造成2到6之间的任意整数伤害

怪物效果和持续时间是可选的，但使用时，可用的效果如下：

| 效果名称         |
|-----------------|
| speed           |
| slowness        |
| haste           |
| mining_fatigue  |
| strength        |
| instant_health  |
| instant_damage  |
| jump_boost      |
| nausea          |
| regeneration    |
| resistance      |
| fire_resistance |
| water_breathing |
| invisibility    |
| blindness       |
| night_vision    |
| hunger          |
| weakness        |
| poison          |
| wither          |
| health_boost    |
| absorption      |
| saturation      |
| levitation      |
| fatal_poison    |
| slow_falling    |
| conduit_power   |
| bad_omen        |
| village_hero    |
| darkness        |

### 远程

向目标以设定的间隔发射指定的[投射物](../entities/projectiles.md)。

```json title=""
"wiki:ranged_attack": {
  "minecraft:behavior.ranged_attack": {
    "priority": 2,
    "ranged_fov": 90.0, //实体用于确定是否可以进行有效远程攻击的允许视野范围
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 15.0
  },
  "minecraft:shooter": {
    "def": "wiki:projectile"
  }
}
```

原版投射物列表：

| 原版投射物                       |
|----------------------------------|
| minecraft:arrow                  |
| minecraft:dragon_fireball        |
| minecraft:egg                    |
| minecraft:ender_pearl            |
| minecraft:fireball               |
| minecraft:fishing_hook           |
| minecraft:lingering_potion       |
| minecraft:llama_spit             |
| minecraft:skulker_bullet         |
| minecraft:small_fireball         |
| minecraft:snowball               |
| minecraft:splash_potion          |
| minecraft:thrown_trident         |
| minecraft:wither_skull           |
| minecraft:wither_skull_dangerous |
| minecraft:xp_bottle              |

只有一种物品会影响实体的远程攻击。十字弓。如果装备了十字弓，则首先需要“充能”它，然后实体才能发射任何东西。无论 `minecraft:shooter` 中指定的投射物是什么，用于充能十字弓的物品应始终是 `minecraft:arrow`。

```json title=""
"minecraft:behavior.charge_held_item": {
  "priority": 2,
  "items": [
    "minecraft:arrow"
  ]
}
```

一旦实现了 `minecraft:behavior.charge_held_item`，实体将能够执行 `minecraft:behavior.ranged_attack` 的过程，然后需要再次充能。

### 范围

这些攻击对设定半径内的所有实体造成伤害。它不同于远程和近战，因为此组件实际上不需要目标。无论实体行为如何，所有实体都将受到影响。它类似于近战攻击，因为它以类似的方式造成击退，但以恒定的速率造成伤害。

```json title=""
"minecraft:area_attack" : {
  "damage_range": 1, //距离，以区块为单位
  "damage_per_tick": 2,
  "cause": "contact",
  "entity_filter": {
     "any_of": [
      {
        "test": "is_family",
        "subject": "other",
        "value": "player"
      },
      {
        "test": "is_family",
        "subject": "other",
        "value": "monster"
      }
    ]
  }
}
```

[实体伤害来源](https://bedrock.dev/docs/stable/Addons#Entity%20Damage%20Source)。考虑这些非常重要，因为原版中的某些物品可以防御部分伤害，例如护甲附魔，你还可以使用 `minecraft:damage_sensor` 使怪物对特定来源免疫。

### 击退咆哮

与 `minecraft:area_attack` 有许多相似之处，但此组件具有更高的灵活性。

```json title=""
"wiki:roar_attack": {
  "minecraft:behavior.knockback_roar":{
    "priority":2,
    "duration":0.7,
    "attack_time":0.2,
    "knockback_damage":1,
    "knockback_horizontal_strength":1,
    "knockback_vertical_strength":1,
    "knockback_range":5,
    "knockback_filters":{
      "test":"is_family",
      "subject":"other",
      "operator":"==",
      "value":"player"
    },
    "damage_filters":{
      "test":"is_family",
      "subject":"other",
      "operator":"==",
      "value":"player"
    },
    "on_roar_end":{
      "event":"wiki:other_event"
    },
    "cooldown_time":10
  }
}
```

这更像是一个伤害的冲击波。在使用上极其多功能。产生粒子效果，可以通过在资源包的粒子文件夹中添加修改后的 `knockback_roar.json` 来禁用该效果。

## 更多关于攻击

实体攻击不必仅仅是怪物对 X 目标敌对，执行 X 攻击，造成 X 伤害。

### 难度依赖性攻击

表达每个难度级别使用的组件和数值。

```json title="BP/entities/bee.json"
"easy_attack": {
    "minecraft:attack": {
        "damage": 2
    }
},
"normal_attack": {
    "minecraft:attack": {
        "damage": 2,
        "effect_name": "poison",
        "effect_duration": 10
    }
},
"hard_attack": {
    "minecraft:attack": {
        "damage": 2,
        "effect_name": "poison",
        "effect_duration": 18
    }
}
```

### 模式切换

你可以使用事件使你的怪物仅在特定情况下攻击，或在不同类型的攻击之间切换。这可以通过简单地使用[事件](../entities/entity-events.md)和组件组来实现。两个典型的例子是 `minecraft:environment_sensor` 和 `minecraft:target_nearby_sensor`。两者在结构上非常相似，区别在于一个用于感知环境，另一个用于测试目标距离。

#### 攻击

需要使用组件组来定义不同的攻击模式，例如：

```json title=""
"wiki:ranged_components": {
  "minecraft:shooter": {
    "def": "wiki:projectile"
  },
  "minecraft:behavior.ranged_attack": {
    "priority": 3,
    "ranged_fov": 90.0,
    "attack_interval_min": 1.0,
    "attack_interval_max": 3.0,
    "attack_radius": 15.0
  }
}
```

```json title=""
"wiki:melee_components": {
  "minecraft:attack": {
    "damage": 6
  },
  "minecraft:behavior.melee_attack": {
    "priority": 3
  }
}
```

这些是你的攻击模式的示例，但它们不是你可以使用的唯一模式。`wiki:ranged_components` 和 `wiki:melee_components` 是它们内部组件的通用名称，可以使用任何名称，但关键在于它们内部嵌套的内容。

#### 事件

这些组件组本身不会实际做任何事情。需要另一个组件组和一些事件来添加/移除攻击模式。

```json title=""
"wiki:melee_swap": {    //触发时，添加远程组件组并移除近战组件组
  "remove": {
    "component_groups": [
      "wiki:ranged_components"
    ]
  },
  "add": {
    "component_groups": [
      "wiki:melee_components"
    ]
  }
}
```

```json title=""
"wiki:ranged_swap": {   //触发时，添加近战组件组并移除远程组件组
  "remove": {
    "component_groups": [
      "wiki:melee_components"
    ]
  },
  "add": {
    "component_groups": [
      "wiki:ranged_components"
    ]
  }
}
```

这些事件实际上只是通过添加和移除不同的组件组来开启和关闭攻击模式。

#### 传感器

要触发事件，使用另一个组件组。传感器是当满足某些条件时可以触发事件的组件。以下是两种不同传感器的示例：

- 感知怪物与目标之间的距离

```json title=""
"wiki:switcher_range": {
  "minecraft:target_nearby_sensor": {
    "inside_range": 4.0,
    "outside_range": 5.0,
    "must_see":  true,
    "on_inside_range": { //当目标在4区块范围内时，触发 "wiki:melee_swap" 事件
      "event": "wiki:melee_swap",
      "target": "self"
    },
    "on_outside_range": { //当目标超出5区块范围时，触发 "wiki:ranged_swap" 事件
      "event": "wiki:ranged_swap",
      "target": "self"
    }
  }
}
```

- 感知怪物所处环境的某些特征

```json title=""
"wiki:switcher_environment": {
  "minecraft:environment_sensor": {
    "triggers": [
      {
        "filters": { //当在水下时，触发 "wiki:melee_swap" 事件
          "test": "is_underwater",
          "subject": "self",
          "operator": "==",
          "value": true
        },
        "event": "wiki:melee_swap"
      },
      {
        "filters": { //当不在水下时，触发 "wiki:ranged_swap" 事件
          "test": "is_underwater",
          "subject": "self",
          "operator": "==",
          "value": false
        },
        "event": "wiki:ranged_swap"
      }
    ]
  }
}
```

这使用了 `过滤器`，类似于[最初选择目标的方式](#目标选择)。

/// tip
你不仅限于两个攻击类型，你可以有任意多个攻击类型！只需确保事件和传感器能相应地补偿它们。
///

## 视觉动画

攻击和动画密不可分。在资源包中，需要以下三个目录：

- animations (entityname.animation.json)
- animation_controllers (entityname.animation_controller.json)
- entity (entityname.json)

或者，只要你知道原版动画和动画控制器的名称，你可以在后一个目录和文件夹中定义它们。

### 动画

动画不言自明。文件本身包含给定实体的所有具体动画。推荐使用[Blockbench](../guide/blockbench.md)制作动画。

尽管也可以在简单的文本编辑器中创建它们。

| 原版攻击动画                              |
|------------------------------------------|
| "animation.zombie.attack_bare_hand"      |
| "animation.skeleton.attack.v1.0"         |
| "animation.humanoid.bow_and_arrow.v1.0"  |
| "animation.humanoid.damage_nearby_mobs.v1.0" |

一些动画的示例。位于 /vanilla_resource_pack/animations 中。

### 动画控制器

列出触发动画的状态。

| 原版攻击动画控制器                               |
|-------------------------------------------------|
| "controller.animation.zombie.attack_bare_hand"  |
| "controller.animation.skeleton.attack"          |
| "controller.animation.humanoid.bow_and_arrow"   |
| "controller.animation.humanoid.attack"          |

一些动画控制器的示例。位于 /vanilla_resource_pack/animation_controllers 中。

有关动画的更多信息，请参见[这里](https://bedrock.dev/docs/stable/Animations)。