---
title: 死亡触发命令
description: 学习在实体死亡时可靠地执行命令的正确方法。
---

# 死亡触发命令

"实体死亡时做某事"是实体开发中的常见需求，但也很容易实现错误。本页介绍两种可靠的实现方式。

## 错误做法

以下两种方式**不应使用**：

- **在实体文件中检测死亡、添加组件，再在动画控制器中检测该组件**：实体在动画控制器有机会执行之前就已从世界中移除，命令永远不会执行。
- **从外部检测实体死亡（如计时命令方块）**：虽然并非完全错误，但代价高昂且容易失效。

## 使用q.is_alive查询

推荐的方法是在行为包动画控制器中使用`q.is_alive`查询。当实体即将被移除时，`q.is_alive`会返回假，触发转移到死亡状态，`on_entry`中的命令会在实体被移除**之前**执行完毕。

```json title="BP/animation_controllers/death.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.death": {
      "initial_state": "default",
      "states": {
        "default": {
          "transitions": [
            { "dead": "!q.is_alive" }
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

`dead`状态是终态——没有任何转移，因此命令只会在第一次死亡时执行一次。

## 对玩家实体的处理

玩家实体在死亡后可以复活，因此必须在`dead`状态中添加转回`default`状态的转移，确保下一次死亡时状态能够重新触发：

```json title="BP/animation_controllers/death.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.death": {
      "initial_state": "default",
      "states": {
        "default": {
          "transitions": [
            { "dead": "!q.is_alive" }
          ]
        },
        "dead": {
          "on_entry": ["/say 我死了！"],
          "transitions": [
            { "default": "q.is_alive" }
          ]
        }
      }
    }
  }
}
```

当玩家复活后，`q.is_alive`重新返回真，控制器转回`default`状态，等待下次死亡。

## 使用minecraft:on_death组件

对于简单的死亡回调，可以直接在行为包实体文件中使用`minecraft:on_death`组件，无须构建动画控制器。在`components`中添加：

```json
"minecraft:on_death": {
  "event": "wiki:on_death",
  "target": "self"
}
```

在`events`中定义事件：

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
使用`queue_command`方式时，即使实体已死亡，仍然可以对其添加分数和标签。
///

两种方法各有适用场景：`minecraft:on_death`更简洁，适合简单的死亡回调；`q.is_alive`动画控制器方法则更灵活，可以与其他状态机逻辑结合使用。
