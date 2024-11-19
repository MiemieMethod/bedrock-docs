---
title: 故障排除物品
category: 常规
tags:
    - 帮助
mentions:
    - SmokeyStack
    - yanasakana
    - SirLich
    - MedicalJewel105
    - TheDoctor15
    - ThomasOrs
    - QuazChick
description: 物品故障排除指南。
---

:::tip
本页面包含有关_物品_的故障排除信息。在继续之前，请阅读我们的[全局故障排除](../guide/troubleshooting.md)文档。
:::

## 从这里开始

> “我跟随了一个教程或者尝试制作自己的物品，但出现了问题！”

不用惊慌！本页面将帮助你调试常见问题。

### 物品不存在

-   确认你的包确实应用到了你的世界中
-   确认你的物品位于文件夹 `BP/items/` 中
-   确认你的物品是有效的，可以通过 [jsonlint](https://jsonlint.com/) 进行验证。
-   确认你的标识符全部为小写，并且类似于：`wiki:my_item`

### 缺少纹理

导航到你的 `item_texture.json` 文件。确保其命名正确，并位于正确的文件夹中。一些错误命名的示例：

-   ⚠️ `texture/item_texture.json`
-   ⚠️ `textures/Item_texture.json`
-   ⚠️ `textures/item_textures.json`

以下是一个可供对比的示例文件：

```json title="RP/textures/item_texture.json"
{
    "resource_pack_name": "wiki",
    "texture_name": "atlas.items",
    "texture_data": {
        "your_item_icon": {
            "textures": "textures/items/your_item_icon"
        }
    }
}
```

接下来，导航到你的物品 BP 文件。在组件部分下，将 `minecraft:icon` 组件放入你的物品文件中。确保其命名正确。

```json title="BP/items/your_item.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:your_item",
            "menu_category": {
                "category": "items"
            }
        },
        "components": {
            "minecraft:icon": "your_item_icon" // 确保此字符串与你在 item_texture.json 中放置的短名称匹配
        }
    }
}
```

如果你正确遵循了上述步骤，你的物品现在应该有纹理了。

## 接下来怎么办？

你已到达指南的末尾。如果你仍然遇到任何问题，请随时[加入 Discord 服务器](/discord)并在那儿提问。