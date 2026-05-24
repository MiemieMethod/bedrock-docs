---
title: Molang值转记分板
description: 将任意Molang查询或变量的数值读取到实体记分板分数中的高级技巧。
---

# Molang值转记分板

本页介绍一种通过动画控制器与动画配合将任意Molang表达式的值转换为记分板分数的技巧。该方法可以将一个不超过10位的整数Molang值实时写入实体的记分板分数。

## 前置设置

在世界中运行以下两条命令（仅需执行一次）：

```mcfunction
/scoreboard objectives add MoLang dummy
/scoreboard players set "#10" MoLang 10
```

第一条命令创建名为`MoLang`的记分项，第二条命令为虚拟玩家`#10`设置基数值`10`，用于进位计算。

## 动画控制器

将以下动画控制器添加到需要读取Molang值的实体（行为包）：

```json title="BP/animation_controllers/molang_to_score.ac.json（部分）"
"controller.animation.namespace.molang_to_score": {
  "initial_state": "idle",
  "states": {
    "idle": {
      "transitions": [ { "convert": "<转换触发条件>" } ],
      "on_exit": [
        "/scoreboard players set @s MoLang 0",
        "/scoreboard players set \"#var\" MoLang 0",
        "v.convert = <要转换的变量或查询>;",
        "v.digit = 1000000000;"
      ]
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

将`<转换触发条件>`替换为触发转换的Molang条件，将`<要转换的变量或查询>`替换为需要读取的Molang值。

## 动画文件

在行为包的`animations/`目录中创建以下动画文件：

```json title="BP/animations/molang_to_score.animation.json（部分）"
"animation.namespace.molang_to_score": {
  "animation_length": 10.0,
  "anim_time_update": "t.digit = Math.mod(Math.floor(v.convert / v.digit), 10) + 0.1; v.digit = v.digit / 10; return t.digit;",
  "timeline": {
    "0.0": [
      "/scoreboard players operation @s MoLang *= \"#10\" MoLang",
      "/scoreboard players operation @s MoLang += \"#var\" MoLang",
      "/scoreboard players set \"#var\" MoLang 0"
    ],
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

## 工作原理

转换的核心思路是**逐位提取数字**，共执行11次动画：

1. 动画控制器离开`idle`状态时（`on_exit`）：
   - 将实体和虚拟玩家`#var`的`MoLang`分数归零
   - 将目标值存入`v.convert`，设置初始进位量`v.digit = 1000000000`（即10^9）
2. 进入`convert`状态，连续执行同一动画11次
3. 每次执行动画时：
   - `anim_time_update`提取当前位数字：`Math.mod(Math.floor(v.convert / v.digit), 10)`，将`v.digit`缩小10倍（移到下一位），返回该数字作为动画时间（0到9之间加上0.1以确保精度）
   - 由于时间轴上所有小于等于当前时间的条目都会执行，`"0.0"`处的命令总是执行：将当前分数乘以10进位，加上上一次提取的数字（`#var`），然后将`#var`清零
   - 当前时间对应的条目（如时间约为`3.0`则执行`"3.0"`的命令）将`#var`设为当前位的数字
4. 经过11次动画后，各位数字从高位到低位依次累加，最终实体的`MoLang`分数即等于`v.convert`的整数值

该方法支持最多10位的非负整数。

/// tip | 测试方法
将触发条件设为`q.is_using_item`，将转换变量设为`Math.random_integer(0, 9999)`。拿起苹果开始食用，观察实体的`MoLang`分数变化即可验证转换是否正常工作。
///
