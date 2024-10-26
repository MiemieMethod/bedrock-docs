---
title: MoLang 转换为记分板
mentions:
  - SirLich
  - MedicalJewel105
  - shanewolf38
  - Luthorius
  - TheItsNameless
  - ThomasOrs
description: 将 MoLang 变量值转换为记分板值。
---

以下提供了一种方法，可以立即将任何 MoLang（变量、查询等）读取为记分。确保在控制器的 `convert` 状态中调用的动画名称与实体中定义的动画名称（animation.namespace.molang_to_score）匹配。

**注意：** 这两个命令必须在世界中作为设置的一部分运行：
`/scoreboard objectives add MoLang dummy`
`/scoreboard players set "#10" MoLang 10`

<CodeHeader>BP/animation_controllers/molang_to_score.animation_controllers.json</CodeHeader>

```json
"controller.animation.namespace.molang_to_score": {
  "initial_state": "idle",
  "states": {
    "idle": {
      "transitions": [ { "convert": "<开始转换的条件>" } ],
      "on_exit": [ "/scoreboard players set @s MoLang 0", "/scoreboard players set \"#var\" MoLang 0", "v.convert = <要转换的变量>;", "v.digit = 1000000000;" ]
    },
    "convert": {
      "animations": [
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score",
        "molang_to_score"
      ],
      "transitions": [ { "idle": "1" } ]
    }
  }
}
```

<CodeHeader>BP/animations/molang_to_score.animation.json</CodeHeader>

```json
"animation.namespace.molang_to_score": {
  "animation_length": 10.0,
  "anim_time_update": "t.digit = Math.mod(Math.floor(v.convert / v.digit), 10) + 0.1; v.digit = v.digit / 10; return t.digit;",
  "timeline": {
    "0.0": [ "/scoreboard players operation @s MoLang *= \"#10\" MoLang", "/scoreboard players operation @s MoLang += \"#var\" MoLang", "/scoreboard players set \"#var\" MoLang 0" ],
    "1.0": [ "/scoreboard players set \"#var\" MoLang 1" ],
    "2.0": [ "/scoreboard players set \"#var\" MoLang 2" ],
    "3.0": [ "/scoreboard players set \"#var\" MoLang 3" ],
    "4.0": [ "/scoreboard players set \"#var\" MoLang 4" ],
    "5.0": [ "/scoreboard players set \"#var\" MoLang 5" ],
    "6.0": [ "/scoreboard players set \"#var\" MoLang 6" ],
    "7.0": [ "/scoreboard players set \"#var\" MoLang 7" ],
    "8.0": [ "/scoreboard players set \"#var\" MoLang 8" ],
    "9.0": [ "/scoreboard players set \"#var\" MoLang 9" ]
  }
}
```

**说明：** 当转换开始时，控制器重置玩家的 MoLang 记分和 `#var`（虚拟玩家）的 MoLang 记分。转换变量 `v.convert` 被初始化，数字变量 `v.digit` 被设置为获取第十位数字（10^10）。第一个动画运行时，将动画时间设置为第十位数字，并将数字变量设置为获取下一个数字（第九位数字，10^9）。由于所有时间线索引都在设置的时间之前运行，因此时间线的 "0.0" 条目将始终运行。这将玩家的 MoLang 记分乘以 10，以设置正确的数字，然后添加上最后获取的数字（对于第一次运行，这将始终为 0，因为 `#var` 被控制器重置）。该过程随后重复 10 次，以获取转换变量的所有 10 位数字。请记住，每个动画都获取由上一个动画设置的数字，这就是为什么动画运行 11 次的原因。

要在游戏中测试转换，将 `<开始转换的条件>` 设置为 `q.is_using_item`，并将 `<要转换的变量>` 设置为 `Math.random_integer(0, 9999)`。拿一个苹果，开始吃，看看数字如何变化。