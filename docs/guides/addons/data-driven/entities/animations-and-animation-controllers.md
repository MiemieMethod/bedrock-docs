---
title: 动画与动画控制器
description: 学习如何在实体中定义和引用动画与动画控制器，以及如何利用状态机管理动画播放逻辑。
---

# 动画与动画控制器

**动画（Animation）**负责定义骨骼如何运动，**动画控制器（Animation Controller）**负责定义何时播放哪段动画。二者共同构成了基岩版实体视觉表现的核心机制。如果只需要让实体持续循环一个动画，可以直接在客户端实体的`scripts.animate`中列出该动画；如果需要按条件切换动画、在特定时机触发一次性动画、播放音效或粒子特效，就应当使用动画控制器。

## 状态机

动画控制器的核心是**状态机（State Machine）**——一种在任意时刻只处于一个特定状态中的逻辑结构。每个状态定义了两件事：

- **当前状态要做什么**：播放哪些动画、触发哪些音效或粒子特效
- **如何切换到其他状态**：若干条状态转移（State Transition）条件

以直升机螺旋桨为例，可以定义两个状态：

- **ground（地面状态）**：不播放动画；若实体离地则切换到飞行状态
- **flying（飞行状态）**：播放螺旋桨旋转动画；若实体落地则切换到地面状态

<!-- 需要绘制两状态有限状态机流程图（矩形=状态，箭头=转移）。参考知识库 two_state_FSM.png -->
![两状态有限状态机示意](../../../../../assets/images/guides/addons/data-driven/entities/animations-and-animation-controllers/two-state-fsm.png)

在这个流程图中，矩形代表状态，箭头代表从一个状态转移到另一个状态的条件。在此基础上加入第三个`explode`（爆炸）状态，就变成三状态机：

<!-- 需要绘制三状态有限状态机流程图（含 explode 终态）。参考知识库 three_state_FSM.png -->
![三状态有限状态机示意](../../../../../assets/images/guides/addons/data-driven/entities/animations-and-animation-controllers/three-state-fsm.png)

状态可以转移到多个不同的目标状态，也可以是没有任何转移的终态（例如直升机爆炸后不需要继续动画）。正是这种分支流程赋予了动画控制器强大的表达能力。

## 引用动画

资源包结构应如下组织：

/// html | div.treeview
- `demo_RP`
    - `animation_controllers`
        - `robot.animation_controllers.json`
    - `animations`
        - `robot.animation.json`
    - `entity`
        - `robot.entity.json`
///

在客户端实体的`description`中，先以`animations`字段将动画（或动画控制器）的全局标识符映射为短名称，再在`scripts.animate`中声明每帧需要执行的短名称：

```json hl_lines="8-16"
{
  "format_version": "1.10.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "demo:robot",
      "...": "...",
      "animations": {
        "look_at_target": "animation.common.look_at_target",
        "sway": "animation.robot.sway",
        "ground_controller": "controller.animation.robot.ground"
      },
      "scripts": {
        "animate": [
          "look_at_target",
          "ground_controller"
        ]
      }
    }
  }
}
```

此处`look_at_target`、`sway`和`ground_controller`是短名称，仅在该实体文件内有效；`animations`字段右侧的`animation.robot.sway`和`controller.animation.robot.ground`才是在对应文件中定义的全局标识符。

如需**有条件地**运行某个动画或控制器，可以用对象语法传入Molang表达式——求值为真时执行，否则不执行：

```json
"scripts": {
  "animate": [
    { "ground_controller": "q.has_rider" }
  ]
}
```

此时只有实体有骑手时，控制器才会运行。

## 创建动画控制器

在资源包的`animation_controllers/`目录下创建动画控制器文件，对应两状态直升机示例的内容如下：

```json title="RP/animation_controllers/helicopter.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.helicopter.blade": {
      "initial_state": "ground",
      "states": {
        "ground": {
          "transitions": [
            { "flying": "!q.is_on_ground" }
          ]
        },
        "flying": {
          "animations": ["flying"],
          "transitions": [
            { "ground": "q.is_on_ground" }
          ]
        }
      }
    }
  }
}
```

逐步解读：

- `controller.animation.helicopter.blade`：控制器标识符，格式通常为`controller.animation.<实体名>.<功能名>`
- `"initial_state": "ground"`：控制器从`ground`状态开始；若省略，则从名为`default`的状态开始，若该状态也不存在则产生内容日志错误
- `ground`状态：只有一个转移条件——当`!q.is_on_ground`（不在地面）为真时转移到`flying`
- `flying`状态：播放短名称为`flying`的动画，并在`q.is_on_ground`为真时转回`ground`

以下是含三个状态（包括终态`explode`）的完整示例：

```json title="RP/animation_controllers/helicopter.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.helicopter.blade": {
      "initial_state": "ground",
      "states": {
        "ground": {
          "transitions": [
            { "flying": "!q.is_on_ground" },
            { "explode": "!q.is_alive" }
          ]
        },
        "flying": {
          "animations": ["flying"],
          "transitions": [
            { "ground": "q.is_on_ground" },
            { "explode": "!q.is_alive" }
          ]
        },
        "explode": {
          "animations": ["explode"]
        }
      }
    }
  }
}
```

`explode`状态没有任何转移，直升机毁坏后动画停在爆炸帧。

## 状态、转移和条件

/// define
`transitions`

- 有序的转移条件列表。每一项是`{ "目标状态名": "Molang条件" }`的对象。每刻从上到下依次求值，取第一个结果为真（非`0`）的条件执行状态转移，每刻最多发生一次转移。

`animations`

- 在当前状态下播放的动画短名称列表。可以是字符串（总是播放）或`{ "短名称": "Molang条件" }`对象（有条件播放）。

`on_entry`

- 进入该状态时执行的命令列表（仅在进入瞬间执行一次）。

`on_exit`

- 离开该状态时执行的命令列表（仅在离开瞬间执行一次）。

///

`q.all_animations_finished`查询在当前状态的所有动画都播放完毕后返回真，适合等待一次性动画结束再转移状态时使用。

常见调试思路：先将转移条件改为`1`（恒真），确认动画本身能够播放，再逐步恢复条件。问题通常来自骨骼名不一致、动画标识符不一致或Molang条件始终不满足三个方面。

## 资源包动画控制器

资源包动画控制器（RPAC）除了`animations`字段外，还支持在状态中使用`sound_effects`和`particle_effects`字段播放音效和粒子特效。使用前须在客户端实体文件的`description`中声明对应短名称：

```json title="RP/entities/custom_tnt.json（部分）"
"sound_effects": {
  "explosion": "wiki.custom_tnt.explosion"
},
"particle_effects": {
  "fuse_lit": "wiki:tnt_fuse_lit_particle"
}
```

随后即可在动画控制器状态中引用：

```json title="RP/animation_controllers/custom_tnt.ac.json（部分）"
"explode_state": {
  "sound_effects": [
    { "effect": "explosion" }
  ],
  "particle_effects": [
    { "effect": "fuse_lit" }
  ],
  "transitions": [
    { "default": "q.mark_variant == 0" }
  ]
}
```

/// warning | 粒子兼容性
并非所有粒子都能在动画控制器中正常触发。若遇到问题，请尝试换用其他粒子，例如烈焰人动画控制器中使用的粒子。
///

## 行为包动画控制器

行为包动画控制器（BPAC）与资源包动画控制器格式相同，但用途不同：它不控制视觉动画，而是执行命令和触发实体事件。`on_entry`和`on_exit`字段接受字符串数组，每个字符串可以是：

- **斜杠命令**：如`/say 你好！`
- **实体事件**：格式为`@s <事件名>`，如`@s wiki:transform`
- **Molang表达式**：如`v.counter += 1;`（资源包动画控制器也支持此格式）

```json title="BP/animation_controllers/helicopter.ac.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.helicopter.commands": {
      "initial_state": "ground",
      "states": {
        "ground": {
          "on_entry": ["/say 我落地了！"],
          "transitions": [
            { "flying": "!q.is_on_ground" }
          ]
        },
        "flying": {
          "on_entry": ["/say 我起飞了！"],
          "transitions": [
            { "ground": "q.is_on_ground" }
          ]
        }
      }
    }
  }
}
```

行为包动画控制器的文件存放于行为包的`animation_controllers/`目录，并在行为包实体定义文件（`.se.json`）的`description`中以相同方式挂接。

/// tip | 进阶用法
利用行为包动画控制器在特定时机触发命令是基岩版实体开发中的常见技巧。参见[实体触发命令](entity-commands.md)、[死亡触发命令](death-commands.md)和[复活触发命令](respawn-commands.md)等进阶页面。
///

## 执行流程

### 加载

实体加载进世界时，进入每个已挂接动画控制器的初始状态。每刻执行步骤如下：

1. 若刚进入该状态，执行`on_entry`中的命令
2. 播放当前状态中列出的动画（循环动画持续播放，一次性动画播放一次）
3. 按顺序检查`transitions`，第一个求值为真的条件触发状态转移：执行`on_exit`命令后进入目标状态

每刻最多发生一次状态转移。

### 重置

当实体重新加载（玩家重新进入世界、区块重载等情况），动画控制器会**重置**回初始状态。因此，初始状态的逻辑必须能够正确处理重载场景，而不能假设实体是"第一次"加载。若需要区分首次生成与重载，需借助额外的查询条件（如`q.skin_id`）来实现。

## 控制器内变量

动画控制器的状态中可以声明并重映射变量，供该状态下引用的动画使用：

```json
{
  "format_version": "1.17.30",
  "animation_controllers": {
    "controller.animation.sheep.move": {
      "states": {
        "default": {
          "variables": {
            "ground_speed_curve": {
              "input": "q.ground_speed",
              "remap_curve": {
                "0.0": 0.2,
                "1.0": 0.7
              }
            }
          },
          "animations": [
            "wiggle_nose",
            { "walk": "v.ground_speed_curve" }
          ]
        }
      }
    }
  }
}
```

`ground_speed_curve`变量将`q.ground_speed`（0到1）重映射到0.2至0.7的区间，再作为`walk`动画的播放权重。这样动画在低速时仍有轻微表现，同时限制了高速时的最大幅度。
