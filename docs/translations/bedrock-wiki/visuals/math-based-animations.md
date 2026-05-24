---
title: 基于数学的动画
description: 使用Molang表达式驱动平滑动画。
category: 教程
---

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/math-based-animations](https://wiki.bedrock.dev/visuals/math-based-animations)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

基于数学的动画，指的是用Molang表达式直接控制骨骼变换。它的优点是循环自然、参数连续、可与游戏状态直接联动。

## 核心思路

传统关键帧动画适合做明确动作；数学动画更适合做持续变化的效果，例如摆动、呼吸、轮转和轻微抖动。

```json
"front_wheels": {
    "rotation": ["q.modified_distance_moved * -30", 0, 0]
}
```

上面的例子表示：实体移动越多，轮子转得越快。

## 常用查询

- `q.modified_distance_moved`
- `q.modified_move_speed`
- `q.anim_time`
- `q.life_time`

## 在Blockbench里做

直接在关键帧值位置填写表达式即可。若要预览依赖游戏上下文的查询，可以用变量占位符模拟。

## 结论

数学动画不是关键帧的替代品，而是一种更适合连续、循环、联动型表现的写法。