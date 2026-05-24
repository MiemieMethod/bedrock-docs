---
title: 复活触发命令
description: 学习在玩家复活时执行命令的方法。
---

# 复活触发命令

本页介绍如何通过行为包动画控制器检测玩家的复活时刻，并在复活时执行命令——例如重新赋予状态效果或给予物品。

## 动画控制器实现

将以下动画控制器添加到`player.json`的行为包动画控制器中：

```json title="BP/animation_controllers/respawn.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.player.respawn": {
      "initial_state": "initialization",
      "states": {
        "initialization": {
          "transitions": [
            { "has_died": "!q.is_alive" }
          ],
          "on_exit": [
            "v.delay = 0.2 + q.life_time;",
            "/<死亡时执行的命令>"
          ]
        },
        "has_died": {
          "on_exit": ["/<复活时执行的命令>"],
          "transitions": [
            { "initialization": "q.is_alive && (q.life_time >= v.delay)" }
          ]
        }
      }
    }
  }
}
```

将`/<死亡时执行的命令>`和`/<复活时执行的命令>`替换为实际需要执行的命令即可。

## 工作原理

该控制器有两个状态：

/// define
**initialization（初始化状态）**

- 等待玩家死亡（`!q.is_alive`为真）。离开此状态时记录死亡时间`v.delay = 0.2 + q.life_time`，并执行死亡时的命令。

**has_died（已死亡状态）**

- 等待玩家复活。转移条件为`q.is_alive && q.life_time >= v.delay`，即玩家已复活且当前存活时间已超过死亡时记录的延迟值。触发转移时（即刚复活后），执行`on_exit`中的复活命令，然后返回`initialization`状态。

///

`v.delay`引入了0.2秒的缓冲时间，确保不会在玩家刚死亡时立即误触发复活条件（此时`q.life_time`会重置为`0`，小于死亡时记录的值）。
