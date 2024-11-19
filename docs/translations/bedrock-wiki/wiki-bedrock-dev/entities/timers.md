---
title: 实体计时器
category: 教程
tags:
  - 中级
mentions:
  - SirLich
  - Joelant05
  - MedicalJewel105
  - aexer0e
  - Justash01
  - TheItsNameless
  - zheaEvyline
description: 本文旨在提供一个详尽的列表，详细说明实体计时器的多种制作方式。
---

基于时间的交互是地图制作中非常有用的工具。本文希望提供一个详尽的列表，详细说明计时器的多种制作方式。为了方便起见，本页面将分为两个主要部分：基于组件的计时器和基于动画的计时器。每种方法都有其优缺点，将在各自的部分中进行说明。
你可能还会发现有用的[记分板计时器](../commands/scoreboard-timers.md)。

## 基于组件的计时器

基于组件的计时器是在行为包的entity.json文件中完成的。它们具有在实体重新加载时保持持久性的明显优势，但受限于计时组件的数量（重复的组件会相互替换，这意味着无法使用`minecraft:timer`组件定义多个计时器）。

### minecraft:timer

这是触发事件的最简单但最有效的组件，事件将在经过一定时间后触发。组件[minecraft:timer](https://bedrock.dev/docs/1.14.0.0/1.14.30.2/Entities#minecraft:timer)提供了三种主要方式来定义事件发生前的时间：

-   精确计时：定义事件触发的确切时间（例如，3.4秒）
-   随机间隔：定义一个间隔，在该间隔内事件将在随机时间触发（例如，3到5秒之间）
-   加权随机选择：定义多个时间并分配权重，其中一个将被选择以触发事件（例如，事件在5秒时有20%的触发概率，在20秒时有80%的触发概率）

在原版行为包中，此组件在各种情况下使用。例如：

-   海豚只能在陆地上待20秒，否则会干涸
-   蜜蜂在叮咬后会在10到60秒之间死亡
-   游荡商人只会停留2400或3600秒

一个简单的示例，在5.6秒后触发事件：

```json title=""
"minecraft:timer": {
  "time": 5.6,
  "time_down_event": {
      "event": "wiki:my_event"
  }
}
```

一个更复杂的示例，在随机延迟后触发事件，使用加权值：

```json title=""
"minecraft:timer": {
  "looping": false, // true将在每次执行后触发事件，false只会触发一次。
  "random_time_choices": [
    {
      "weight": 25,
      "value": 0.5 // 半秒的延迟
    },
    {
      "weight": 25,
      "value": 10 // 十秒的延迟
    },
    {
      "weight": 25,
      "value": 30 // 三十秒的延迟
    },
    {
      "weight": 25,
      "value": 120 // 两分钟的延迟
    }
  ],
  "time_down_event": {
    "event": "wiki:event",
    "target": "self"
  }
}
```

处理时间事件的一个特别有用的方法是使用单个循环的`minecraft:timer`组件，并在每个刻（tick）上处理事件（或根据你决定的频率触发计时器）。这可以通过在事件中使用`randomize`参数来实现，其中权重可以用来确定其他事件的运行频率。这可以让你从单个计时器组件中获得更多的额外收益。

```json title=""
"wiki:do_event": {
  "randomize": [
    {
      "weight": 1,
      "add": {
        "component_groups": [
          "wiki:my_event"
        ]
      }
    },
    {
      "weight": 5,
      "add": {
        "component_groups": [
          "wiki:my_more_frequent_event"
        ]
      }
    },
    {
      "weight": 50 // 不触发任何事件
    }
  ]
}
```

### minecraft:environment_sensor

另一个非常有用的组件是[minecraft:environment_sensor](https://bedrock.dev/docs/stable/Entities#minecraft:environment_sensor)，它可以用于基于时间的事件。将此传感器与`hourly_clock_time`或`clock_time`过滤器配对，可以根据游戏内时间触发事件。

以下是一个示例，在白天开始后800个刻（ticks）触发事件（有效范围为0到24000）：

```json title=""
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

如果此组件（[minecraft:ageable](https://bedrock.dev/docs/stable/Entities#minecraft:ageable)）未在实体的行为中用于其他目的，它可以作为额外的计时器使用。需要注意的是，它需要定义`minecraft:is_baby`组件才能正常工作。

以下是一个在四秒后触发事件的示例：

```json title=""
"minecraft:is_baby": {},
"minecraft:ageable": {
  "duration": 4,
  "grow_up": {
    "event": "wiki:my_other_event",
    "target": "self"
  }
}
```

### 其他虚拟计时器：

查看文档可以发现还有其他组件也可以用于计时。基本上，你要寻找任何带有“时间到事件”或“持续时间”的组件。

一些有前景的示例（非详尽列表）：

-   `minecraft:angry`（需要实体有目标，时间必须是整数）
-   `minecraft.behavior.hide`
-   `minecraft:behavior.celebrate`

## 基于动画的计时器

行为包动画是触发基于时间事件的极其强大的工具。它们具有提供“无限”计时器的明显优势，但在实体重新加载时会重新启动（离开并重新加入世界或包含实体的区块卸载时，计时器将在实体重新加载时重新启动）。

动画在行为包中的功能与资源包不同。如果你不熟悉它们的操作，建议通过查看官方文档或本维基的其他页面来了解更多信息。

### 简单计时器

通过从动画控制器或直接从脚本部分触发动画，你可以按时间顺序执行特定事件、命令或Molang表达式，称为时间线。

你可以这样设置时间线：

```json title=""
{
	"format_version": "1.8.0",
	"animations": {
		"animation.command.example_timeline": {
			"timeline": {
				"0.0": "/say 这将立即触发",
				"3.0": "/say 这将在3秒后触发"
			},
			"animation_length": 3.1
		},
		"animation.command.example_timeline_2": {
			"timeline": {
				"100": "/say 这将在100秒后触发",
				"0.0": [
					"/say 你可以同时触发多个事件",
					"/say 通过使用时间线。"
				],
				"55.55": "/say 这将在55.55秒后触发。"
			},
			"animation_length": 100.1
		}
	}
}
```

### 随机间隔

计时器组件的一个非常有用的功能是能够定义一个随机间隔，在该间隔内事件将被触发。此功能可以通过动画和控制器复制。以下是一个示例，通过将`minecraft:is_sheared`组件添加到实体上触发的动画，该动画在激活后随机在2到7秒之间触发事件。动画和控制器版本为1.10.0。

```json title=""
"controller.animation.shanewolf.random_interval": {
  "initial_state": "inactive",
  "states": {
    "inactive": {
      "transitions": [
        {
          "active": "q.is_sheared"
        }
      ]
    },
    "active": {
      "on_entry": [
        "v.random_interval = math.random(2, 7);",
        "/say 随机间隔已开始"
      ],
      "animations": [
        "wiki:animate_interval"
      ],
      "transitions": [
        {
          "inactive": "q.anim_time >= v.random_interval"
        }
      ],
      "on_exit": [
        "@s wiki:stop_random_interval",
        "/say 随机间隔已结束"
      ]
    }
  }
}
```

```json title=""
"animation.shanewolf.random_interval": {
  "animation_length": 100
}
```

说明：在进入开始动画的状态时，变量被赋予一个在2到7之间的随机值。当当前动画时间大于或等于该值时，动画结束。

**注意**：
-   动画长度可以设置为大于时间范围最大值的任何值（100作为一般模板）
-   math.random(a, b)用于在范围[a, b]内触发事件
-   math.floor(math.random(a, b.99))可用于在整数值处结束计时器（0.99必须加到b上）
-   动画结束时要运行的任何事件或命令都放在on_exit中

### 加权随机选择

计时器组件的另一个有用功能是能够在由加权值列表确定的时间触发事件。此功能也可以通过动画和控制器复制。以下是一个示例，通过将`minecraft:is_charged`组件添加到实体上触发的动画，该动画在2、5或9秒时随机触发事件，权重分别为30、60和10。动画和控制器版本为1.10.0。

```json title=""
"controller.animation.shanewolf.random_choices": {
  "initial_state": "inactive",
  "states": {
    "inactive": {
      "transitions": [
        {
          "active": "q.is_powered"
        }
      ]
    },
    "active": {
      "on_entry": [
        "v.random_choices = math.random(0, 100);",
        "/say 随机选择已开始"
      ],
      "animations": [
        "wiki:animate_choices"
      ],
      "transitions": [
        {
          "inactive": "q.anim_time >= 2.0 && v.random_choices < 30"
        },
        {
          "inactive": "q.anim_time >= 5.0 && v.random_choices < 90"
        },
        {
          "inactive": "q.anim_time >= 9.0 && v.random_choices <= 100"
        }
      ],
      "on_exit": [
        "@s wiki:stop_random_choices",
        "/say 随机选择已结束"
      ]
    }
  }
}
```

```json title=""
"animation.shanewolf.random_choices": {
  "animation_length": 100
}
```

说明：在进入开始动画的状态时，变量被赋予一个在0到100之间的随机值（权重之和）。过渡按从最小时间到最大时间的顺序排列。这样做是为了避免在后续过渡中需要多个&&运算符来定义变量的范围（查询最小时间的条件首先返回true，并在检查其他条件之前检查其权重——如果将2和5调换位置，将导致2错误地具有90的权重而不是30）。当当前动画时间大于或等于列表中的某个时间，并且随机变量的值落在该时间的定义权重范围内时，动画结束。

**注意**：
-   动画长度可以设置为大于时间范围最大值的任何值（100作为一般模板）
-   为了使此特定格式正常工作，按从最小到最大排列有效时间列表
-   要为列表中的时间分配权重，请将权重添加到随机变量在列表前一项中必须小于的值（例如，5秒的权重为90 - 30 = 60）
-   动画结束时要运行的任何事件或命令都放在on_exit中

希望这能为处理Minecraft基岩版中的时间问题提供一些启示！如上所示，有许多可能的方法可以实现，每种方法都有其优缺点。如果你有任何其他有用的方法来创建基于时间的事件，请[为维基贡献](/contribute)!