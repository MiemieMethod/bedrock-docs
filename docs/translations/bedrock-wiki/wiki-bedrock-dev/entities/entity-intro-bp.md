---
title: 实体行为包简介
category: 一般
nav_order: 1
tags:
    - 指南
    - 初学者
mentions:
    - SirLich
    - solvedDev
    - stirante
    - Joelant05
    - destruc7ion
    - MedicalJewel105
    - ChibiMango
    - SmokeyStack
    - ThomasOrs
description: 实体行为包简介。
---

行为包实体文件的基础由三个主要结构组成。本文档将解释它们的含义以及如何使用它们。

将组件组与组件混淆是常见的错误来源。请仔细注意以理解二者之间的区别。

## 组件

组件是构成Minecraft实体的逻辑构建块。所有组件由Mojang编写并提供给我们使用。组件可以执行各种操作，例如设置实体的大小或赋予其游泳的能力。完整的组件列表可以在[这里](https://bedrock.dev/docs/stable/Entities)找到。

创建自己的组件是_不可能_的。整个组件列表是硬编码的，由Microsoft提供。

当你想为实体添加行为时，你需要将`components`添加到`minecraft:entity`对象的`components`对象中。例如，如果我们想赋予实体攀爬的能力，可以通过添加以下组件实现：`"minecraft:can_climb": {}`。

所有组件的格式为`"minecraft:<name>": { <setting> }`。每个组件接受不同类型的设置。

以下是实体中几个组件的示例：

<CodeHeader>BP/entities/example.json#minecraft:entity</CodeHeader>

```json
"components": {
    "minecraft:type_family": {
        "family": [
            "player"
        ]
    },
    "minecraft:collision_box": {
        "width": 0.6,
        "height": 1.8
    },
    "minecraft:can_climb": {}
}
```

请注意，`components`列表_仅_包含组件。

## 组件组

组件组是组件的“文件夹”。它们将组件分组，并可以通过`events`进行添加或移除，以创建自定义游戏玩法。

以下是一个示例：

<CodeHeader>BP/entities/example.json#minecraft:entity</CodeHeader>

```json
"component_groups": {

    //组件组的名称
    "minecraft:cat_persian": {

        //有效组件的列表。可以添加任意数量。
        "minecraft:variant": {
            "value": 6
        },
        "minecraft:physics": {}
    },

    //第二个组件组的名称
    "wiki:example_group": {
        "minecraft:type_family": {
            "family": [
                "wiki_is_awesome!"
            ]
        }
    }
}
```

所有组件组都是自定义创建的。你不能在你的实体中使用其他实体的组件组。

在原版Minecraft实体中，组件组以`minecraft:`命名空间命名，如上面的`minecraft:cat_persian`。但重要的是要记住，它们_不是组件_。当你创建组件组时，可以使用任意名称/命名空间:名称组合。例如，上面的`wiki:example_group`。有关命名空间的更多信息，请查看[这里](../concepts/namespaces.md)。

当组件放入组中时，它_不会_自动添加到你的实体中。在组被添加之前，它不会做任何事情。当组被添加时，组件将变为活动状态，并开始影响你的实体行为。你也可以同时添加多个组件组。

## 事件

事件是一种特殊的语法，用于在满足某些条件时添加和移除组件组。通过添加/移除组，我们可以为实体创建动态行为。

以下是一个示例：

<CodeHeader>BP/entities/example.json#minecraft:entity#events</CodeHeader>

```json
"minecraft:ageable_grow_up": { //事件名称
    "remove": { //要移除的组件组列表
        "component_groups": [
            "minecraft:cat_baby"
        ]
    },
    "add": {
        "component_groups": [
            "minecraft:cat_adult" //要添加的组件组列表。
        ]
    }
}
```

与组件组一样，事件在每个实体内部都是100%自定义创建的。你不能在自己的实体中使用其他实体的事件。不要试图在自己的实体中使用`"minecraft:ageable_grow_up"`。如果你想要成长功能，你需要自己定义组件组和事件。

你可以从实体中添加/移除的唯一内容是`component groups`。尽管直接尝试添加/移除组件是很诱人的，但这是不可能的。

事件在某些组件内部激活，当满足某些条件时。以下是一个示例：

<CodeHeader>BP/entities/example.json#minecraft:entity</CodeHeader>

```json
"components": {
    "minecraft:interact": {
        "interactions": [
            {
                "on_interact": {
                    "filters": [
                        {
                            "test":"is_family",
                            "subject": "other",
                            "value": "player"
                        }
                    ],
                    "target": "self",
                    "event": "wiki:on_interact"
                }
            }
        ]
    }
},
"component_groups": {
    "wiki:interacted": {
        "minecraft:scale": {
            "value": 2
        }
    }
},
"events": {
    "wiki:on_interact": {
        "add": {
            "component_groups": [ "wiki:interacted" ]
        }
    }
}
```

在这里，当实体被玩家互动时，将激活`"wiki:on_interact"`事件。该事件将添加组件组`"wiki:interacted"`。这将应用组件`"minecraft:scale"`。

有关事件可以做什么的更深入教程，请查看我们关于实体事件的页面。

<Button link="../entities/entity-events.md">实体事件</Button>

## 原版中的用途

组件组和事件是原版实体创建自定义和可适应行为的主要工具。以下是一些使用组件组和事件创建的原版特性：

-   僵尸被编程为在水下待太久后变成`淹死的僵尸`。

-   狐狸有两个组件组`minecraft:fox_red`和`minecraft:fox_active`，根据它们生成的位置具有两种颜色变体。

-   当被注视时，末影人会对玩家变得具有攻击性。