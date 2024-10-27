---
title: 添加掉落表、生成规则和合成配方
category: 指南
description: 如何添加你的第一个掉落表、生成规则和合成配方
nav_order: 8
prefix: "8. "
mentions:
    - KaiFireborn
    - SirLich
    - sermah
    - cda94581
    - Ultr4Anubis
    - TheItsNameless
    - Ciosciaa
    - MedicalJewel105
    - ChibiMango
    - FrankyRay
---

接下来，我们将通过添加一些基本机制来增强自定义的幽灵实体：

## 掉落表

首先，我们将让幽灵在死亡时掉落灵质：创建以下文件：

<CodeHeader>BP/loot_tables/entities/ghost.json</CodeHeader>

```json
{
    "pools": [
        {
            "rolls": 1,
            "entries": [
                {
                    "type": "item",
                    "name": "wiki:ectoplasm",
                    "weight": 1,
                    "functions": [
                        {
                            "function": "set_count",
                            "count": {
                                "min": 1,
                                "max": 3
                            }
                        }
                    ]
                }
            ]
        }
    ]
}
```

-   掉落表由“`pools`”组成。每个池定义了不同的掉落。一个池由三个部分组成：“`rolls`”、“`entries`”和“`conditions`”。“`conditions`”是可选的，本指南将不涵盖。要了解更多关于条件的信息，请查看[掉落表](../loot/loot-tables.md)。
-   “`rolls`”部分定义了从以下“`entries`”对象中随机选择多少次。
-   “`entries`”部分定义了掉落表可以选择的物品。每次掷骰子时都会选择一个新物品。
-   “`type`”定义了将要选择的内容。可以将其设置为“`item`”或“`loot_table`”，以选择物品或其他掉落表。
-   “`name`”将设置为带有命名空间的物品标识符。它定义了将选择哪个物品。
-   “`weight`”是可选的，定义了选择此物品的可能性。如果“`entries`”部分中有多个物品，可以使用“`weight`”属性来调整某个物品的概率。如果未设置，则默认为1。
-   “`functions`”提供了一种强大的方式来定制将返回的物品。它们可以为物品添加附魔、设置物品名称或简单地设置将掉落的物品数量。要定义物品数量，我们使用“`set_count`”。它接受“`count`”属性，设置将掉落的物品的最大和最小数量。

有关掉落表的更多信息，请查看我们的扩展指南：[掉落表](../loot/loot-tables.md)!

## 生成规则

接下来，我们将让幽灵在夜间的沙漠中生成：

<CodeHeader>BP/spawn_rules/ghost.json</CodeHeader>

```json
{
    "format_version": "1.8.0",
    "minecraft:spawn_rules": {
        "description": {
            "identifier": "wiki:ghost",
            "population_control": "monster"
        },
        "conditions": [
            {
                "minecraft:spawns_on_surface": {},
                "minecraft:brightness_filter": {
                    "min": 0,
                    "max": 7,
                    "adjust_for_weather": true
                },
                "minecraft:difficulty_filter": {
                    "min": "easy",
                    "max": "hard"
                },
                "minecraft:weight": {
                    "default": 80
                },
                "minecraft:herd": {
                    "min_size": 1,
                    "max_size": 3
                },
                "minecraft:biome_filter": {
                    "test": "has_biome_tag",
                    "operator": "==",
                    "value": "desert"
                }
            }
        ]
    }
}
```

-   你已经知道“`format_version`”的作用。
-   在“`minecraft:spawn_rules`”部分中，我们定义了我们的生成规则。
-   “`description`”定义了文件的基本属性。“`identifier`”用于定义此生成规则适用于哪个实体。“`population_control`”用于限制生成的实体数量。一旦“`population_control`”中定义的池满了，就不会再生成实体。
-   使用“`conditions`”，我们可以定义限制此实体生成的特殊规则。我们将简要描述此处使用的每个条件，但你可以在[这里](../entities/vanilla-usage-spawn-rules.md)了解更多条件及其用法。
    -   “`spawns_on_surface`”允许生物仅在表面生成。
    -   “`minecraft:brightness_filter`”限制生成到光照水平在定义值之间的区域。如果“`adjust_for_weather`”为`true`，则在雨天和风暴期间光照水平的降低将被忽略。
    -   “`minecraft:difficulty_filter`”定义生成实体所需的难度级别。
    -   “`weight`”定义此实体生成的频率。此值越高，生物生成的频率越高。
    -   “`minecraft:herd`”定义一次生成多少实体。
    -   使用“`minecraft:biome_filter`”，我们定义实体能够生成的生物群落。

要了解有关生成规则的更多信息，请查看我们的[原版生成规则](../entities/vanilla-usage-spawn-rules.md)指南。

## 合成配方

最后，作为配方的介绍，我们将使灵质可以合成成粘液块：

<CodeHeader>BP/recipes/ectoplasm_slime_blocks.json</CodeHeader>

```json
{
    "format_version": "1.12.0",
    "minecraft:recipe_shaped": {
        "description": {
            "identifier": "wiki:ectoplasm_slime_block"
        },
        "tags": ["crafting_table"],
        "pattern": ["###", "###", "###"],
        "key": {
            "#": {
                "item": "wiki:ectoplasm"
            }
        },
        "result": {
            "item": "minecraft:slime"
        }
    }
}
```

-   “`format_version`”已经知道。
-   使用“`recipe_shaped`”，我们定义每个材料在合成网格中的固定位置。还有其他一些类型可以使用，更多信息请查看[这里](../loot/recipes.md)。
-   在“`description`”中，我们定义此配方的“`identifier`”，即配方的名称。
-   “`tags`”是能够使用此配方的工作台（合成台、熔炉等）的列表。在版本b1.16.100之后，可以使用由附加包创建的自定义工作台。
-   “`pattern`”定义了物品在合成网格中的排列。每个`#`代表在“`key`”下设置的物品。在这种情况下，整个3x3网格必须填满“`wiki:ectoplasm`”，我们的自定义物品。可以定义更多物品，只需向“`key`”添加一个条目，并将键设置为可以在“`pattern`”中使用的字符。
-   “`result`”包含一个“`item`”，该项设置为此配方的输出物品。

有关此主题的更多信息，请访问我们关于[配方](../loot/recipes.md)的页面！

## 你学到了什么

:::tip 你学到了什么：

-   如何创建掉落表并定义生物能够掉落的物品
-   如何设置生物生成的规则
-   如何创建新的合成配方

:::

## 你目前的进展

**你已完成：**

-   [x] 设置你的包
-   [x] 创建自定义物品
-   [x] 创建自定义实体
-   [x] 创建实体的掉落、生成规则和自定义配方

恭喜你！你已经完成了指南并创建了你的第一个附加包。🎉