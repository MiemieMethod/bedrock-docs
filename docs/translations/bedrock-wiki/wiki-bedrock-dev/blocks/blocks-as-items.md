---
title: 块作为物品
description: 了解在用户界面、容器中以及掉落在地面上的代表块的物品。
category: 一般
tags:
    - 实验性
mentions:
    - QuazChick
---

## 自动块物品

当你手中握着一个块时，实际上你握着的是一个放置该块的物品。当一个自定义块被注册到游戏中时，Minecraft也会自动注册一个新的物品来代表该块在物品栏中的显示。

该物品使用块定义的菜单类别和显示名称，但自动块物品的其他组件无法被修改。
为了应用其他组件，例如为你的块提供一个2D图标，你需要用自己的物品替换块的物品。

## 替换块物品

/// warning | 格式版本 1.21.40（实验性）
替换块物品需要启用“即将到来的创作者功能”实验。
///

为了替换块物品，你需要创建一个新的物品JSON文件，其标识符与块相同。

你的新物品还需要包含 [块放置器](/items/item-components#block-placer) 组件，这将允许该物品放置块。
块放置器组件还会默认赋予物品块的3D外观，但可以通过 [图标](/items/item-components#icon) 组件覆盖，以显示2D精灵。

### 自定义花朵示例

一个需要替换块物品的情况示例是花块，它们应该以物品形式显示为图标，而不是3D形式。

```json title="BP/blocks/daffodil.json"
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:daffodil"
        },
        "components": {
            "minecraft:geometry": "minecraft:geometry.cross",
            "minecraft:material_instances": {
                "*": {
                    "texture": "daffodil",
                    "render_method": "alpha_test"
                }
            }
        }
    }
}
```

```json title="BP/items/daffodil.json"
{
    "format_version": "1.21.40",
    "minecraft:item": {
        "description": {
            "identifier": "wiki:daffodil", // 与块的ID相同
            "menu_category": {
                "category": "nature",
                "group": "itemGroup.name.flower"
            }
        },
        "components": {
            "minecraft:icon": "daffodil",
            "minecraft:block_placer": {
                "block": "wiki:daffodil",
                "replace_block_item": true
            }
        }
    }
}
```