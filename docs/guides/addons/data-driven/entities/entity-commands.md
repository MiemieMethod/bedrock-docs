---
title: 实体触发命令
description: 学习如何通过行为包动画控制器让实体在特定时机执行斜杠命令。
---

# 实体触发命令

行为包动画控制器不仅能管理服务端逻辑状态，还能让实体在进入或离开状态时执行斜杠命令、触发实体事件或运算Molang表达式。本页介绍如何利用这一机制让实体在特定时机执行命令。

/// tip | 更简便的方法
如果只需要在实体事件发生时执行命令，可以直接使用实体事件的`queue_command`响应，无须构建动画控制器。动画控制器方法适合需要更复杂状态管理的场景。
///

## 基本结构

触发命令的核心是行为包动画控制器的`on_entry`字段。以下是在实体进入世界时执行命令的最简示例：

```json title="BP/animation_controllers/entity_commands.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.example.commands": {
      "states": {
        "default": {
          "transitions": [
            { "on_summon": "1" }
          ]
        },
        "on_summon": {
          "on_entry": ["/say 我被召唤了！"]
        }
      }
    }
  }
}
```

`"1"`作为Molang表达式求值恒为真，因此实体进入世界后立即从`default`状态转移到`on_summon`状态，执行`on_entry`中的命令。

在实体行为定义文件中挂接此控制器：

```json title="BP/entities/entity_commands.se.json（部分）"
"description": {
  "identifier": "wiki:entity_commands",
  "animations": {
    "wiki:entity_commands": "controller.animation.example.commands"
  },
  "scripts": {
    "animate": [
      "wiki:entity_commands"
    ]
  }
}
```

/// warning | 重载问题
动画控制器在实体每次重新加载（区块重载、玩家重新进入世界）时都会重置回初始状态并重新求值转移条件。这意味着上述`on_summon`状态每次加载都会触发，而不仅仅是在实体首次生成时。若需要只在首次生成时执行命令，请参阅下方的皮肤ID方案。
///

## 使用皮肤ID管理状态

为了解决重载问题并支持多个可重复使用的命令状态，常用的技巧是将**皮肤ID（Skin ID）**作为状态标志。皮肤ID通过`minecraft:skin_id`组件设置，可在动画控制器中通过`q.skin_id`查询。工作逻辑如下：

- 实体初始皮肤ID为`0`（空闲状态）
- 触发命令时，通过事件将皮肤ID设为特定值（如`1`或`2`）
- 动画控制器检测到皮肤ID变化，进入对应命令状态并执行命令
- 命令执行完毕后触发`execute_no_commands`事件，将皮肤ID重置为`0`
- 动画控制器返回`default`状态，等待下一次触发

```json title="BP/animation_controllers/entity_commands.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.example.commands": {
      "states": {
        "default": {
          "transitions": [
            { "command_example": "q.skin_id == 1" },
            { "command_zombies": "q.skin_id == 2" }
          ]
        },
        "command_example": {
          "transitions": [
            { "default": "q.skin_id != 1" }
          ],
          "on_entry": [
            "/say 命令示例已执行！",
            "@s execute_no_commands"
          ]
        },
        "command_zombies": {
          "transitions": [
            { "default": "q.skin_id != 2" }
          ],
          "on_entry": [
            "/say 召唤了僵尸！",
            "/summon minecraft:zombie ~ ~ ~",
            "/summon minecraft:zombie ~ ~ ~",
            "@s execute_no_commands"
          ]
        }
      }
    }
  }
}
```

注意：`==`测试相等，`!=`测试不等，不要使用单个`=`作为相等判断。

## 组件组与事件

在实体行为定义文件中，用组件组存储各皮肤ID，用事件切换组件组：

```json title="BP/entities/entity_commands.se.json（部分）"
"component_groups": {
  "execute_no_commands": {
    "minecraft:skin_id": { "value": 0 }
  },
  "command_example": {
    "minecraft:skin_id": { "value": 1 }
  },
  "command_zombies": {
    "minecraft:skin_id": { "value": 2 }
  }
},
"events": {
  "minecraft:entity_spawned": {
    "add": { "component_groups": ["execute_no_commands"] }
  },
  "execute_no_commands": {
    "add": { "component_groups": ["execute_no_commands"] }
  },
  "command_example": {
    "add": { "component_groups": ["command_example"] }
  },
  "command_zombies": {
    "add": { "component_groups": ["command_zombies"] }
  }
}
```

`minecraft:entity_spawned`事件在实体首次生成时触发，确保皮肤ID从`0`开始。由于该事件**不会**在区块重载时再次触发，皮肤ID在重载后会保持之前的值——这正是这一技巧避免重载误触发的关键。

## 触发方式

设置好组件组和事件后，可以通过多种方式触发命令：

### 交互组件

每当玩家点击实体时触发命令：

```json title="BP/entities/entity_commands.se.json（部分）"
"minecraft:interact": {
  "interactions": [{
    "on_interact": {
      "filters": {
        "all_of": [
          { "test": "is_family", "subject": "other", "value": "player" }
        ]
      },
      "event": "command_zombies"
    }
  }]
}
```

### 计时器组件

每10秒循环触发一次：

```json title="BP/entities/entity_commands.se.json（部分）"
"minecraft:timer": {
  "looping": true,
  "time": 10,
  "time_down_event": {
    "event": "command_example"
  }
}
```

## 工作流程回顾

1. 通过交互、计时器等组件触发某个实体事件
2. 事件将对应组件组添加到实体，设置皮肤ID
3. 动画控制器查询到皮肤ID变化，转移到对应命令状态
4. 进入新状态时执行`on_entry`中的命令
5. `@s execute_no_commands`触发重置事件，皮肤ID归零
6. 动画控制器返回`default`状态，等待下一次触发
