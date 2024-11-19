---
title: 添加战利品表、生成规则和合成配方
category: 指南
description: 如何添加你的第一个战利品表、生成规则和合成配方
---

# 添加战利品表、生成规则和合成配方

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/guide/loot-table.html](https://wiki.bedrock.dev/guide/loot-table.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/loot-table.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/loot-table.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@991bc8ccbc8aa7db2b4015eb05d03c92c3c91145 -->
- 该页面的作者有：
    - <!-- md:samp @KaiFireborn -->
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @sermah -->
    - <!-- md:samp @cda94581 -->
    - <!-- md:samp @Ultr4Anubis -->
    - <!-- md:samp @TheItsNameless -->
    - <!-- md:samp @Ciosciaa -->
    - <!-- md:samp @MedicalJewel105 -->
    - <!-- md:samp @ChibiMango -->
    - <!-- md:samp @FrankyRay -->
///

接下来，我们将通过添加一些基本机制来增强自定义的幽灵实体：

## 战利品表

首先，我们将让幽灵在死亡时掉落灵异物质：创建以下文件：

```json title="BP/loot_tables/entities/ghost.json"
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

-   战利品表由`pools`组成。每个池定义了不同的掉落。一个池由三个部分组成：`rolls`、`entries`和`conditions`。`conditions`是可选的，本指南将不涵盖这部分。要了解更多关于条件的信息，请查看[战利品表](../loot/loot-tables.md)。
-   `rolls`部分定义了从以下`entries`对象中随机选择多少次。
-   `entries`部分定义了战利品表可以选择的物品。每次掷骰子时都会选择一个新物品。
-   `type`定义了将要选择的内容。可以将其设置为`item`或`loot_table`，以选择物品或其他战利品表。
-   `name`将设置为带有命名空间的物品标识符。它定义了将选择哪个物品。
-   `weight`是可选的，定义了选择此物品的可能性。如果`entries`部分中有多个物品，可以使用`weight`属性来调整某个物品的概率。如果未设置，则默认为1。
-   `functions`提供了一种强大的方式来定制将返回的物品。它们可以为物品添加附魔、设置物品名称或简单地设置将掉落的物品数量。要定义物品数量，我们使用`set_count`。它接受`count`属性，设置将掉落的物品的最大和最小数量。

有关战利品表的更多信息，请查看我们的扩展指南：[战利品表](../loot/loot-tables.md)!

## 生成规则

接下来，我们将让幽灵在夜间的沙漠中生成：

```json title="BP/spawn_rules/ghost.json"
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

-   你已经知道`format_version`的作用。
-   在`minecraft:spawn_rules`部分中，我们定义了我们的生成规则。
-   `description`定义了文件的基本属性。`identifier`用于定义此生成规则适用于哪个实体。`population_control`用于限制生成的实体数量。一旦`population_control`中定义的池满了，就不会再生成实体。
-   使用`conditions`，我们可以定义限制此实体生成的特殊规则。我们将简要描述此处使用的每个条件，但你可以在[这里](../entities/vanilla-usage-spawn-rules.md)了解更多条件及其用法。
    -   `spawns_on_surface`允许生物仅在表面生成。
    -   `minecraft:brightness_filter`限制生成到光照水平在定义值之间的区域。如果`adjust_for_weather`为`true`，则在雨雪和雷暴期间光照水平的降低将被忽略。
    -   `minecraft:difficulty_filter`定义生成实体所需的难度级别。
    -   `weight`定义此实体生成的频率。此值越高，生物生成的频率越高。
    -   `minecraft:herd`定义一次生成多少实体。
    -   使用`minecraft:biome_filter`，我们定义实体能够生成的生物群系。

要了解有关生成规则的更多信息，请查看我们的[原版生成规则](../entities/vanilla-usage-spawn-rules.md)指南。

## 合成配方

最后，作为配方的介绍，我们将使灵异物质可以合成成粘液块：

```json title="BP/recipes/ectoplasm_slime_blocks.json"
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

-   `format_version`已经知道。
-   使用`recipe_shaped`，我们定义每个材料在合成网格中的固定位置。还有其他一些类型可以使用，更多信息请查看[这里](../loot/recipes.md)。
-   在`description`中，我们定义此配方的`identifier`，即配方的名称。
-   `tags`是能够使用此配方的桌台类型（工作台、熔炉等）的列表。在版本b1.16.100之后，可以使用由附加包创建的自定义工作台。
-   `pattern`定义了物品在合成网格中的排列。每个`#`代表在`key`下设置的物品。在此情况下，整个3x3网格必须填满`wiki:ectoplasm`，即我们的自定义物品。你可以定义更多物品，只需向`key`添加一个条目，并将键设置为可以在`pattern`中使用的字符。
-   `result`包含一个`item`，该项设置为此配方的输出物品。

有关此主题的更多信息，请访问我们关于[配方](../loot/recipes.md)的页面！

## 你学到了什么

/// tip | 你学到了什么：

-   如何创建战利品表并定义生物能够掉落的物品
-   如何设置生物生成的规则
-   如何创建新的合成配方

///

## 你目前的进展

**你已完成：**

-   [x] 设置你的包
-   [x] 创建自定义物品
-   [x] 创建自定义实体
-   [x] 创建实体的掉落、生成规则和自定义配方

恭喜你！你已经完成了指南并创建了你的第一个附加包。🎉