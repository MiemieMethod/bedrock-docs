---
title: 自定义受伤动画
description: 在实体受伤时播放自定义动画。
category: 教程
---

/// details-info | 署名信息
- 该页面内容翻译自[Hurt Animations](https://wiki.bedrock.dev/visuals/custom-hurt-animations.html)
- 原文版权归原作者所有
///

这个技巧的核心思路是：用一个同步到客户端的布尔属性记录“是否受伤”，再让动画控制器根据这个属性切换状态。

## 行为包

先在实体描述中加入属性：

```json
"properties": {
    "wiki:is_hurt": {
        "client_sync": true,
        "type": "bool",
        "default": false
    }
}
```

然后在受伤事件里把它设为`true`，并启动一个短计时器，计时结束后再设回`false`。

## 动画控制器

在RP里，根据`q.property('wiki:is_hurt')`切换到受伤动画状态即可。

## 适用场景

这种写法很适合做船、机车、道具或其他需要“受击反馈”的自定义实体。
