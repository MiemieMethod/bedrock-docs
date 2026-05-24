---
title: AFK检测
description: 通过行为包动画控制器检测玩家挂机（AFK）状态，并在进入或离开挂机时执行命令。
---

# AFK检测

本页介绍如何利用行为包动画控制器检测玩家是否处于挂机状态，并在玩家进入或离开挂机状态时执行命令。

## 动画控制器实现

将以下动画控制器添加到`player.json`的行为包动画控制器中：

```json title="BP/animation_controllers/afk.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.player.afk": {
      "states": {
        "default": {
          "transitions": [
            { "stands_still": "!q.is_moving" }
          ]
        },
        "stands_still": {
          "on_entry": ["v.afk = q.life_time;"],
          "transitions": [
            {
              "afk": "(q.life_time - v.afk) >= 30 && !q.is_moving"
            },
            { "default": "q.is_moving" }
          ]
        },
        "afk": {
          "on_entry": [
            "/tag @s add AFK",
            "/say 我现在处于挂机状态"
          ],
          "animations": ["afk_animation"],
          "transitions": [
            { "default": "q.is_moving" }
          ],
          "on_exit": [
            "/tag @s remove AFK",
            "/say 我不再挂机了"
          ]
        }
      }
    }
  }
}
```

## 工作原理

该控制器有三个状态：

/// define
**default（默认状态）**

- 玩家移动时处于此状态。当玩家停止移动（`!q.is_moving`）时转入`stands_still`状态。

**stands_still（静止状态）**

- 进入时记录当前存活时间`v.afk = q.life_time`。若玩家持续静止超过30秒（`q.life_time - v.afk >= 30`），则转入`afk`状态；若玩家重新开始移动，则返回`default`状态。

**afk（挂机状态）**

- 进入时添加`AFK`标签并广播消息，同时播放`afk_animation`动画。当玩家重新开始移动时，`on_exit`移除`AFK`标签并广播消息，然后返回`default`状态。

///

通过选择器`@a[tag=AFK]`即可在命令中定位所有处于挂机状态的玩家。

/// note | 关于挂机动画
`animations`字段中的`afk_animation`是客户端实体中定义的动画短名称，需要在`player.json`的`animations`字段中注册对应的全局动画标识符。如果不需要播放挂机动画，删除`"animations": ["afk_animation"]`这一行即可。
///