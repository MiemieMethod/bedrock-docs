# 实体计时器

在地图和附加包开发中，时间控制是极其常用的工具——延迟执行事件、周期性触发行为、随机化等待时间……实现这些的方案很多，本文整理了两大类：基于组件的计时器和基于动画的计时器。

## 基于组件的计时器

基于组件的计时器写在行为包的实体JSON文件中。**优点**是实体重载（卸载区块再加载）后计时仍会继续，因为组件状态会持久化。**缺点**是同种组件只能有一个实例，定义多个`minecraft:timer`时后者会覆盖前者。

### minecraft:timer

这是最简单也最直接的计时组件，支持三种计时方式：

- **精确计时**：在指定时间（秒）后触发事件
- **随机区间**：在指定范围内随机选取一个时间触发
- **加权随机**：从多个时间中按权重随机选取一个触发

**精确计时示例**（5.6秒后触发事件）：

```json title="minecraft:entity > components（节选）"
"minecraft:timer": {
    "time": 5.6,
    "time_down_event": {
        "event": "wiki:my_event"
    }
}
```

**加权随机示例**（分别有25%概率在0.5s、10s、30s、120s后触发）：

```json title="minecraft:entity > components（节选）"
"minecraft:timer": {
    "looping": false,
    "random_time_choices": [
        { "weight": 25, "value": 0.5 },
        { "weight": 25, "value": 10 },
        { "weight": 25, "value": 30 },
        { "weight": 25, "value": 120 }
    ],
    "time_down_event": {
        "event": "wiki:event",
        "target": "self"
    }
}
```

**循环计时器结合随机事件**：将`looping`设为`true`，每次到时间时触发一个使用`randomize`参数的事件，可以用一个计时器模拟多种概率行为：

```json title="minecraft:entity > events（节选）"
"wiki:on_tick": {
    "randomize": [
        {
            "weight": 1,
            "add": { "component_groups": ["wiki:rare_event"] }
        },
        {
            "weight": 5,
            "add": { "component_groups": ["wiki:common_event"] }
        },
        {
            "weight": 50
        }
    ]
}
```

### minecraft:environment_sensor

通过`hourly_clock_time`或`clock_time`过滤器，可以在特定游戏时间触发事件。以下示例在白天第800刻触发（游戏时间范围为0~24000）：

```json title="minecraft:entity > components（节选）"
"minecraft:environment_sensor": {
    "triggers": [
        {
            "filters": {
                "test": "hourly_clock_time",
                "operator": "=",
                "value": 800
            },
            "event": "wiki:my_daily_event"
        }
    ]
}
```

### minecraft:ageable

如果这个组件在实体行为中没有被用于其他用途，可以将其作为额外的计时器。它需要同时定义`minecraft:is_baby`组件才能正常工作。以下示例在4秒后触发事件：

```json title="minecraft:entity > components（节选）"
"minecraft:is_baby": {},
"minecraft:ageable": {
    "duration": 4,
    "grow_up": {
        "event": "wiki:my_event",
        "target": "self"
    }
}
```

### 其他可用组件

凡是有`time_down_event`或`duration`字段的组件，理论上都可以作为计时器使用。常见的还有：

- `minecraft:angry`（需要目标，时间必须是整数）
- `minecraft:behavior.hide`
- `minecraft:behavior.celebrate`

## 基于动画的计时器

行为包动画是实现时间控制的另一种强大手段。**优点**是可以定义近乎"无限"数量的独立计时器。**缺点**是实体重载（区块卸载再加载）时所有动画会重置。

行为包动画的工作方式与资源包不同，如果你不熟悉，建议先阅读[动画与动画控制器](animations-and-animation-controllers.md)教程。

### 简单时间轴计时器

通过动画的`timeline`字段，可以在指定时间触发命令、Molang表达式或实体事件：

```json title="BP/animations/my_entity.json"
{
    "format_version": "1.8.0",
    "animations": {
        "animation.wiki.example_timeline": {
            "timeline": {
                "0.0": "/say 这条命令立即执行",
                "3.0": "/say 这条命令3秒后执行"
            },
            "animation_length": 3.1
        },
        "animation.wiki.long_timeline": {
            "timeline": {
                "0.0": ["/say 可以在同一时刻触发多条命令", "/say 只需用数组即可"],
                "55.55": "/say 55.55秒后触发",
                "100": "/say 100秒后触发"
            },
            "animation_length": 100.1
        }
    }
}
```

### 随机区间计时器

使用动画控制器配合`math.random()`可以模拟`minecraft:timer`的随机区间功能。以下示例在进入`active`状态后，随机等待2到7秒后退出：

```json title="BP/animation_controllers/my_entity.json（片段）"
"controller.animation.wiki.random_interval": {
    "initial_state": "inactive",
    "states": {
        "inactive": {
            "transitions": [{ "active": "q.is_sheared" }]
        },
        "active": {
            "on_entry": [
                "v.random_interval = math.random(2, 7);"
            ],
            "animations": ["wiki:animate_interval"],
            "transitions": [
                { "inactive": "q.anim_time >= v.random_interval" }
            ],
            "on_exit": ["@s wiki:on_interval_end"]
        }
    }
}
```

```json title="BP/animations/my_entity.json（片段）"
"animation.wiki.animate_interval": {
    "animation_length": 100
}
```

/// note | 说明
`animation_length`要大于随机区间的最大值（这里是7），100是一个通用安全值。
///

### 加权随机计时器

以下示例实现加权随机：在2s（权重30%）、5s（权重60%）或9s（权重10%）后触发事件。

```json title="BP/animation_controllers/my_entity.json（片段）"
"controller.animation.wiki.random_choices": {
    "initial_state": "inactive",
    "states": {
        "inactive": {
            "transitions": [{ "active": "q.is_powered" }]
        },
        "active": {
            "on_entry": [
                "v.choice = math.random(0, 100);"
            ],
            "animations": ["wiki:animate_choices"],
            "transitions": [
                { "inactive": "q.anim_time >= 2.0 && v.choice < 30" },
                { "inactive": "q.anim_time >= 5.0 && v.choice < 90" },
                { "inactive": "q.anim_time >= 9.0 && v.choice <= 100" }
            ],
            "on_exit": ["@s wiki:on_choice_end"]
        }
    }
}
```

/// tip | 权重计算方式
各行的阈值是权重的累加：30%取0~30，60%取30~90，10%取90~100。转移条件从时间最短到最长排列，确保短时间条件优先判断。
///
