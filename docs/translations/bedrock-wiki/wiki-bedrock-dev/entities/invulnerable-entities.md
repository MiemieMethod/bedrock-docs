---
title: 无敌实体
category: 教程
tags:
    - 初学者
mentions:
    - SirLich
    - Joelant05
    - solvedDev
    - MedicalJewel105
description: 学习如何制作无敌实体。
---

## 使用伤害传感器

禁用实体伤害的最佳且灵活的方法是使用 `minecraft:damage_sensor` 组件。该组件允许我们使用 `filters` 来确定哪些伤害来源可以对我们的实体造成伤害。

学习此组件的最佳方式是使用原版的伤害传感器示例或阅读 [文档](https://bedrock.dev/docs/stable/Entities#minecraft:damage_sensor)。

### 完全无敌实体

<CodeHeader>BP/entities/entity.json#minecraft:entity/components</CodeHeader>

```json
"minecraft:damage_sensor": {
    "triggers": {
        "cause": "all",
        "deals_damage": false
    }
}
```

### 禁用玩家造成的伤害

<CodeHeader>BP/entities/entity.json#minecraft:entity/components</CodeHeader>

```json
"minecraft:damage_sensor": {
    "triggers": {
        "on_damage": {
            "filters": {
                "test": "is_family",
                "subject": "other",
                "value": "player"
            }
        },
        "deals_damage": false
    }
}
```

## 最小生命值

`minecraft:health` 组件中的 `min` 属性允许我们制作无法死亡的无敌实体。这包括使用 `/kill @e` 时。这并不是一个好的解决方案，因为这样的实体很难处理。

如果选择使用此组件，请确保有其他方法可以消灭该实体。通过环境传感器、计时器或交互触发 `minecraft:instant_despawn` 是一个不错的解决方案。你也可以使用 `/event` 调用它。

<CodeHeader>BP/entities/entity.json#minecraft:entity/components</CodeHeader>

```json
"minecraft:health": {
    "value": 1,
    "max": 1,
    "min": 1
}
```

请注意，将其设置为 0 会破坏某些死亡和生成动画/效果。