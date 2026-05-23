# 动画与动画控制器

动画负责“骨骼怎样动”，动画控制器负责“什么时候播放哪段动画”。如果你只是让实体持续播放一个循环动画，可以直接在客户端实体的`scripts.animate`中列出动画；如果你需要按状态切换、重新播放一次性动画或同时触发声音和粒子，就应该使用动画控制器。

## 引用一个动画

资源包结构：

/// html | div.treeview
- `demo_RP`
    - `animations`
        - `robot.animation.json`
    - `entity`
        - `robot.entity.json`
///

在客户端实体中注册短名称：

```json hl_lines="8-15"
{
  "format_version": "1.10.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "demo:robot",
      "...": "...",
      "animations": {
        "look_at_target": "animation.common.look_at_target",
        "sway": "animation.robot.sway"
      },
      "scripts": {
        "animate": [
          "look_at_target",
          { "sway": "!query.is_on_ground" }
        ]
      }
    }
  }
}
```

这里`look_at_target`和`sway`是短名称，只在这个实体文件内使用；右侧的`animation.robot.sway`才是动画文件里定义的全局动画标识符。

## 创建动画控制器

资源包中创建`animation_controllers/robot.animation_controllers.json`：

```json title="robot.animation_controllers.json"
{
  "format_version": "1.10.0",
  "animation_controllers": {
    "controller.animation.robot.ground": {
      "states": {
        "default": {
          "transitions": [
            { "swaying": "!query.is_on_ground" }
          ]
        },
        "swaying": {
          "animations": [ "sway" ],
          "transitions": [
            { "default": "query.all_animations_finished && query.is_on_ground" }
          ]
        }
      }
    }
  }
}
```

再在客户端实体中引用控制器：

```json
"animations": {
  "ground_controller": "controller.animation.robot.ground",
  "sway": "animation.robot.sway"
},
"scripts": {
  "animate": [
    "ground_controller"
  ]
}
```

## 状态、转移和条件

- `states`定义状态。
- 每个状态可以播放`animations`、`sound_effects`和`particle_effects`。
- `transitions`使用Molang表达式判断是否切换到另一个状态。
- `query.all_animations_finished`适合等待一次性动画播放完。

动画问题通常来自三个地方：骨骼名不一致、动画标识符不一致、Molang条件一直不满足。调试时先把条件改成`1`，确认动画本身能播放，再逐步恢复条件。
