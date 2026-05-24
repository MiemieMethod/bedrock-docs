# 仿村庄机制

本文介绍如何使自定义实体模仿村庄机制：居住、工作、聚集、日程调度、进入室内、开关门等。这些行为的核心是`minecraft:dweller`组件与`minecraft:scheduler`组件的配合使用。

## 导航基础

首先为自定义村民配置优先路径导航，让其偏好走在特定方块上：

```json title="BP/entities/custom_villager.json（components）"
"minecraft:preferred_path": {
    "max_fall_blocks": 1,
    "jump_cost": 5,
    "default_block_cost": 1.5,
    "preferred_path_blocks": [
        {
            "cost": 0,
            "blocks": ["grass_path"]
        },
        {
            "cost": 1,
            "blocks": ["cobblestone", "stone"]
        },
        {
            "cost": 50,
            "blocks": ["bed", "lectern"]
        }
    ]
}
```

- `cost`值越低，越优先选择该路径
- `default_block_cost`是未列出方块的默认代价

随机漫步与回归居住范围：

```json
"minecraft:behavior.random_stroll": {
    "priority": 9,
    "speed_multiplier": 0.55,
    "xz_dist": 10,
    "y_dist": 5
},
"minecraft:behavior.move_towards_dwelling_restriction": {
    "priority": 4,
    "speed_multiplier": 1.0
}
```

## 门的交互

让实体能够打开和关闭门，并在室内停留：

```json
"minecraft:navigation.walk": {
    "can_pass_doors": true,
    "can_open_doors": true
},
"minecraft:annotation.open_door": {},
"minecraft:behavior.open_door": {
    "priority": 6,
    "close_door_after": true
},
"minecraft:behavior.move_indoors": {
    "priority": 5
},
"minecraft:behavior.restrict_open_door": {
    "priority": 5
}
```

## 核心：居住组件

`minecraft:dweller`是实现村庄机制的核心组件：

```json title="BP/entities/custom_villager.json（components）"
"minecraft:dweller": {
    "dwelling_type": "village",
    "dweller_role": "inhabitant",
    "preferred_profession": "farmer",
    "update_interval_base": 60,
    "update_interval_variant": 40,
    "can_find_poi": true,
    "can_migrate": true,
    "first_founding_reward": 5
}
```

| 字段 | 说明 |
|---|---|
| `dwelling_type` | 居住的村庄类型，通常为`"village"` |
| `dweller_role` | `"inhabitant"`：认领床和钟；`"defender"`：铁傀儡用 |
| `preferred_profession` | 首选职业（如`"farmer"`），影响寻找工作台的逻辑 |
| `can_find_poi` | 是否能寻找兴趣点（POI），包括`bed`、`jobsite`、`meeting_area` |
| `can_migrate` | 是否可以迁移到其他村庄 |

## 睡眠

参见[睡眠实体](sleeping-entities.md)教程。居住组件中的`dweller_role: "inhabitant"`会让实体尝试寻找床。

## 工作

工作行为需要`dweller_role`为`"inhabitant"`。如果没有`preferred_profession`，实体会尝试移向最近的任意工作台。

```json
"minecraft:behavior.work": {
    "priority": 4,
    "active_time": 250,
    "speed_multiplier": 0.5,
    "goal_cooldown": 200,
    "sound_delay_min": 100,
    "sound_delay_max": 200,
    "can_work_in_rain": false,
    "work_in_rain_tolerance": 1000,
    "on_arrival": {
        "event": "minecraft:resupply_trades",
        "target": "self"
    }
}
```

## 聚集

让实体在钟声附近与其他同类型实体聚集交流：

```json
"minecraft:behavior.mingle": {
    "priority": 4,
    "speed_multiplier": 0.5,
    "duration": 30,
    "cooldown_time": 10,
    "mingle_partner_type": "wiki:custom_villager",
    "mingle_distance": 2.0
}
```

## 日程调度

使用`minecraft:scheduler`将工作和聚集行为按时间段切换：

### 组件组定义

```json title="component_groups"
"work_schedule": {
    "minecraft:behavior.work": {
        "priority": 4,
        "active_time": 250,
        "speed_multiplier": 0.5,
        "goal_cooldown": 200,
        "sound_delay_min": 100,
        "sound_delay_max": 200,
        "can_work_in_rain": false,
        "work_in_rain_tolerance": 1000,
        "on_arrival": {
            "event": "minecraft:resupply_trades",
            "target": "self"
        }
    }
},
"gather_schedule": {
    "minecraft:behavior.mingle": {
        "priority": 5,
        "speed_multiplier": 0.8,
        "cooldown_time": 10.0,
        "duration": 30.0,
        "mingle_dist": 1.5,
        "mingle_partner_type": "wiki:custom_villager"
    }
}
```

### 调度器配置

```json title="components"
"minecraft:scheduler": {
    "min_delay_secs": 0,
    "max_delay_secs": 10,
    "scheduled_events": [
        {
            "filters": {
                "all_of": [
                    { "test": "hourly_clock_time", "operator": ">=", "value": 0 },
                    { "test": "hourly_clock_time", "operator": "<", "value": 12000 }
                ]
            },
            "event": "wiki:work"
        },
        {
            "filters": {
                "all_of": [
                    { "test": "hourly_clock_time", "operator": ">=", "value": 21000 },
                    { "test": "hourly_clock_time", "operator": "<", "value": 24000 }
                ]
            },
            "event": "wiki:gather"
        }
    ]
}
```

`hourly_clock_time`的范围是0到24000，0对应早晨，12000对应傍晚，18000对应午夜。

### 事件定义

```json title="events"
"wiki:work": {
    "remove": { "component_groups": ["gather_schedule"] },
    "add": { "component_groups": ["work_schedule"] }
},
"wiki:gather": {
    "remove": { "component_groups": ["work_schedule"] },
    "add": { "component_groups": ["gather_schedule"] }
}
```

## 测试

在世界中生成实体，然后放置一张床，若能看到绿色粒子，说明实体成功认领了床位。

## 其他相关行为

以下AI意向也可用于自定义实体，与村庄机制相关：

| 行为 | 说明 |
|---|---|
| `minecraft:behavior.move_to_village` | 让实体前往村庄内随机位置（掠夺者、女巫使用） |
| `minecraft:behavior.stroll_towards_village` | 让实体寻找并前往一个村庄（狐狸使用） |
| `minecraft:behavior.inspect_bookshelf` | 让实体注视并检查书架（图书管理员村民使用） |
| `minecraft:behavior.explore_outskirts` | 让实体探索村庄边界之外的区域 |
| `minecraft:behavior.defend_village_target` | 攻击伤害了`"inhabitant"`角色实体的攻击者；**推荐仅用于近战攻击**，远程攻击可能误伤友军 |
| `minecraft:behavior.hide` | 让实体在指定POI处隐藏停留（村民躲避掠夺者时使用） |
| `minecraft:behavior.move_through_village` | 让实体在村庄内巡逻（铁傀儡使用） |