---
title: 物品简介
description: 一个“你好，世界”的物品制作指南。了解物品格式以及如何创建基本的自定义物品。
category: 通用
nav_order: 1
tags:
    - 指南
    - 初学者
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - yanasakana
    - destruc7ion
    - aexer0e
    - stirante
    - ChibiMango
    - MedicalJewel105
    - Sprunkles317
    - mark-wiemer
    - TheItsNameless
    - s1050613
    - SmokeyStack
    - QuazChick
---

Minecraft基岩版允许我们向世界中添加具有各种类似原版属性的自定义物品。

本教程将介绍如何为Minecraft的稳定版本创建基本物品。

## 注册物品

物品定义的结构与实体相似：它们包含描述和定义物品行为的组件列表。

以下是将自定义物品添加到创造模式库存的**最低**行为代码。

<CodeHeader>BP/items/custom_item.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "construction"
            }
        },
        "components": {} // 必须在此处，即使为空！
    }
}
```

### 物品描述

-   定义物品的标识符 - 以`命名空间:标识符`格式的唯一ID。
-   配置物品放置到哪个`menu_category`中。
    -   还可以使用可选参数`group`和`is_hidden_in_commands`。

## 添加组件

现在，我们的自定义物品正在使用默认组件值（可以在[这里](/items/item-components)找到）。

让我们配置自己的功能吧！

<CodeHeader>BP/items/custom_item.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "construction"
            }
        },
        "components": {
            "minecraft:damage": 10,
            "minecraft:durability": {
                "max_durability": 36
            },
            "minecraft:hand_equipped": true
        }
    }
}
```

更多物品组件请浏览[这里](/items/item-components)!

## 应用纹理

我们需要创建一个纹理短名称，将其链接到`RP/textures/item_texture.json`中的图像。

<CodeHeader>RP/textures/item_texture.json</CodeHeader>

```json
{
    "resource_pack_name": "wiki",
    "texture_name": "atlas.items",
    "texture_data": {
        "custom_item": {
            "textures": "textures/items/custom_item"
        }
    }
}
```

在我们的物品文件中，我们将添加`minecraft:icon`组件以应用纹理。

<CodeHeader>BP/items/custom_item.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:custom_item",
            "menu_category": {
                "category": "construction"
            }
        },
        "components": {
            "minecraft:icon": "custom_item"
        }
    }
}
```

## 定义名称

最后，我们将为物品命名。此外，您可以使用[显示名称](/items/item-components#display-name)组件。

<CodeHeader>RP/texts/en_US.lang</CodeHeader>

```c
tile.wiki:custom_item.name=自定义物品
```

## 结果

在本页中，您已了解以下内容：

-   [x] 物品的基本特性
-   [x] 如何应用纹理
-   [x] 如何在`item_textures.json`中使用短名称链接纹理
-   [x] 如何在语言文件中定义名称