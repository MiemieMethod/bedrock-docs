---
title: 死亡命令
description: 实体死亡时执行命令。
---

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/animation-controllers/death-commands.html](https://wiki.bedrock.dev/animation-controllers/death-commands.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/death-commands.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/animation-controllers/death-commands.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@dded66a13b7daa57de21c828ddae2fc8429a35a9 -->
- 该页面的作者有：
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @BlueFrog130 -->
    - <!-- md:samp @SmokeyStack -->
    - <!-- md:samp @cda94581 -->
    - <!-- md:samp @MedicalJewel105 -->
    - <!-- md:samp @Kaioga5 -->
    - <!-- md:samp @TheItsNameless -->
    - <!-- md:samp @QuazChick -->
///

[了解更多关于动画控制器的信息](./animation-controllers-intro.md){ .md-button }

我将“死亡效果”定义为“当实体死亡时执行某些操作”。有几种错误的方法应该避免，包括：

- 在实体文件中检测死亡，添加组件，然后尝试在动画控制器中检测该组件。这是错误的，因为实体将在动画控制器有机会运行之前从世界中移除。
- 从外部来源检测实体死亡，例如定时命令方块。此方法并不严格错误，在某些情况下甚至可能更可取。然而，它运行成本高且容易出错。

## 使用q.is_alive

创建死亡效果的最佳方法是使用`is_alive`查询。

只需创建一个基于`is_alive`的动画控制器转移。最终的`on_entry`将在实体从世界中移除之前运行，从而允许你执行命令。

以下是一个示例动画控制器：

```json title="BP/animation_controllers/death.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.death": {
      "initial_state": "default",
      "states": {
        "default": {
          "transitions": [
            {
              "dead": "!q.is_alive"
            }
          ]
        },
        "dead": {
          "on_entry": ["/say 我死了！"]
        }
      }
    }
  }
}
```

## 用于玩家实体

对于玩家实体，必须在第二个动画状态中添加额外的转移，以确保状态在死亡之间重置：

```json title="BP/animation_controllers/death.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.death": {
      "initial_state": "default",
      "states": {
        "default": {
          "transitions": [
            {
              "dead": "!q.is_alive"
            }
          ]
        },
        "dead": {
          "on_entry": ["/say 我死了！"],
          "transitions": [
            {
              "default": "q.is_alive"
            }
          ]
        }
      }
    }
  }
}
```

## 使用minecraft:on_death

你还可以在行为包的`entity.json`文件中使用`minecraft:on_death`组件，这是一种相对简单的实现死亡时执行命令的方法。

首先将其添加到你的组件中，并使其在自身上运行事件；

```json
"minecraft:on_death" : {
  "event": "wiki:on_death",
  "target": "self"
}
```

然后，在你的事件部分添加该事件；

```json
"wiki:on_death": {
  "queue_command": {
    "command": [
      "say 我死了！"
    ]
  }
}
```

/// tip
你可以在实体死亡时使用此方法添加分数和标签。
///