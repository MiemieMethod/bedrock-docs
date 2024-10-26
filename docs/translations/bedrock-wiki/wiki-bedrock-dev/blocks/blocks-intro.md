---
title: 方块简介
description: 制作方块的Hello World指南。了解方块格式以及如何创建基本的自定义方块。
category: 一般
nav_order: 1
tags:
    - 指南
    - 初学者
mentions:
    - SirLich
    - solvedDev
    - Joelant05
    - Dreamedc2015
    - sermah
    - yanasakana
    - aexer0e
    - SmokeyStack
    - MedicalJewel105
    - stirante
    - ChibiMango
    - Hatchibombotar
    - FrankyRay
    - Ciosciaa
    - Sprunkles137
    - ThomasOrs
    - QuazChick
---

:::tip 格式与最低引擎版本 `1.21.40`
本页面讨论基本方块特性。您可以在[这里](/blocks/block-components)了解更多关于其他方块组件的信息。
:::
:::danger 注意
原版方块是硬编码的。您无法覆盖或访问它们。
:::

Minecraft基岩版允许我们将自定义方块添加到我们的世界中，具有各种类似原版的属性。自定义方块可以具有多个阶段（如植物）、方向朝向和其他有用的特性。

本教程将介绍如何为Minecraft的稳定版本创建基本方块。

## 注册方块

方块定义的结构与实体类似：它们包含描述和定义方块行为的组件列表。

与实体不同，方块除了在`RP/blocks.json`中没有其他资源定义。

以下是将自定义方块添加到创造模式库存的**最小**行为侧代码。

<CodeHeader>BP/blocks/custom_block.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_block",
            "menu_category": {
                "category": "construction", // 方块放置的创造模式库存或配方书标签
                "group": "itemGroup.name.concrete", // 方块所属的可扩展组。（可选）
                "is_hidden_in_commands": false // 方块是否在命令中隐藏？（可选）
            }
        },
        "components": {} // 必须存在，即使为空！
    }
}
```

### 方块描述

-   定义方块的`identifier` - 以`namespace:identifier`格式的唯一ID。
-   配置方块放置的`menu_category`。
    -   还可以使用可选参数`group`和`is_hidden_in_commands`。

_方块描述也是[状态](/blocks/block-states)和[特性](/blocks/block-traits)的所在，它们在各自的页面中进行了介绍。_

## 添加组件

现在，我们的自定义方块使用的是默认组件值（可以在[这里](/blocks/block-components)找到）。

让我们配置我们自己的功能吧！

<CodeHeader>BP/blocks/custom_block.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "minecraft:block": {
        "description": {
            "identifier": "wiki:custom_block",
            "menu_category": {
                "category": "construction"
            }
        },
        "components": {
            "minecraft:destructible_by_mining": {
                "seconds_to_destroy": 3
            },
            "minecraft:destructible_by_explosion": {
                "explosion_resistance": 3
            },
            "minecraft:friction": 0.4,
            "minecraft:map_color": "#ffffff",
            "minecraft:light_dampening": 0,
            "minecraft:light_emission": 4,
            "minecraft:loot": "loot_tables/blocks/custom_block.json"
        }
    }
}
```

-   [`minecraft:destructible_by_mining`](/blocks/block-components#destructible-by-mining) 定义玩家需要挖掘方块到破坏所需的时间。目前，无法为不同工具设置不同的破坏时间。
-   [`minecraft:destructible_by_explosion`](/blocks/block-components#destructible-by-explosion) 定义对爆炸的抵抗力。值越高，破坏的几率越低。
-   [`minecraft:friction`](/blocks/block-components#friction) 定义方块的摩擦力。例如，灵魂沙的摩擦力值较高，因此会减缓玩家的移动。冰的摩擦力值较低，因此具有滑动效果。经典方块如木头或石头的摩擦力为`0.4`。
-   [`minecraft:map_color`](/blocks/block-components#map-color) 是在Minecraft地图上显示该方块的十六进制颜色代码。`#ffffff`表示白色。您可以在[这里](https://www.google.com/search?q=hex+color+picker)获取其他颜色的十六进制代码。
-   [`minecraft:light_dampening`](/blocks/block-components#light-dampening) 定义有多少光线会被阻挡。
-   [`minecraft:light_emission`](/blocks/block-components#light-emission) 定义方块输出的光照等级。
-   [`minecraft:loot`](/blocks/block-components#loot) 定义方块掉落的战利品表路径。如果删除此项，方块将掉落自身。您可以在[这里](/loot/loot-tables)了解更多关于战利品表的信息。

_在[这里](/blocks/block-components)浏览更多方块组件！_

## 应用纹理

:::warning
`RP/blocks.json`忽略标识符命名空间。您可以在此处放置任何内容，或者根本不包含命名空间，结果没有区别。如果您创建一个与现有原版方块同名（但没有命名空间）的自定义方块，可能会导致问题。
:::
:::tip <nbsp/>
[方块声音](/blocks/block-sounds)也可以在`RP/blocks.json`中定义。
:::

对于我们的基本16×16×16像素方块，纹理应在`RP/blocks.json`中定义。

如果您想应用自定义模型，则应使用[几何体](/blocks/block-components#geometry)和[材质实例](/blocks/block-components#material-instances)组件。

<CodeHeader>RP/blocks.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "wiki:custom_block": {
        "textures": "custom_block", // 此纹理短名称应在`terrain_texture.json`中定义，如下所示
        "sound": "grass"
    }
}
```

现在，我们需要在`RP/textures/terrain_texture.json`中将纹理短名称链接到图像文件路径：

<CodeHeader>RP/textures/terrain_texture.json</CodeHeader>

```json
{
    "texture_name": "atlas.terrain",
    "resource_pack_name": "wiki", // 您的资源包ID
    "padding": 8, // 防止纹理在视觉上溢出
    "num_mip_levels": 4, // 从远处或角度查看时的纹理质量
    "texture_data": {
        // 我们的纹理短名称：
        "custom_block": {
            "textures": "textures/blocks/custom_block" // 链接到图像文件名
        }
    }
}
```

### 每面纹理

纹理也可以按面应用。例如，一个自定义的“指南针方块”可以使用以下✨惊艳✨的纹理：

-   `textures/blocks/compass_block_down.png`

    <WikiImage
        src="/assets/images/blocks/blocks-intro/compass_block_down.png"
        pixelated
        width="64"
    />

-   `textures/blocks/compass_block_up.png`

    <WikiImage src="/assets/images/blocks/blocks-intro/compass_block_up.png" pixelated width="64" />

-   `textures/blocks/compass_block_north.png`

    <WikiImage
        src="/assets/images/blocks/blocks-intro/compass_block_north.png"
        pixelated
        width="64"
    />

-   `textures/blocks/compass_block_east.png`

    <WikiImage
        src="/assets/images/blocks/blocks-intro/compass_block_east.png"
        pixelated
        width="64"
    />

-   `textures/blocks/compass_block_south.png`

    <WikiImage
        src="/assets/images/blocks/blocks-intro/compass_block_south.png"
        pixelated
        width="64"
    />

-   `textures/blocks/compass_block_west.png`

    <WikiImage
        src="/assets/images/blocks/blocks-intro/compass_block_west.png"
        pixelated
        width="64"
    />

`blocks.json`条目将如下所示：

<CodeHeader>RP/blocks.json</CodeHeader>

```json
{
    "format_version": "1.21.40",
    "wiki:compass_block": {
        "textures": {
            "down": "compass_block_down",
            "up": "compass_block_up",
            "north": "compass_block_north",
            "east": "compass_block_east",
            "south": "compass_block_south",
            "west": "compass_block_west"
        }
    }
}
```

或者，如果您使用[材质实例](/blocks/block-components#material-instances)，它们应如下所示：

<CodeHeader>minecraft:block > components</CodeHeader>

```json
"minecraft:material_instances": {
  "*": {
    "texture": "compass_block_down" // 此纹理出现在破坏粒子中
  },
  "up": {
    "texture": "compass_block_up"
  },
  "north": {
    "texture": "compass_block_north"
  },
  "east": {
    "texture": "compass_block_east"
  },
  "south": {
    "texture": "compass_block_south"
  },
  "west": {
    "texture": "compass_block_west"
  }
}
```

以及以下`terrain_texture.json`数据：

<CodeHeader>RP/textures/terrain_texture.json</CodeHeader>

```json
{
    "texture_name": "atlas.terrain",
    "resource_pack_name": "wiki",
    "padding": 8,
    "num_mip_levels": 4,
    "texture_data": {
        "compass_block_down": {
            "textures": "textures/blocks/compass_block_down"
        },
        "compass_block_up": {
            "textures": "textures/blocks/compass_block_up"
        },
        "compass_block_north": {
            "textures": "textures/blocks/compass_block_north"
        },
        "compass_block_east": {
            "textures": "textures/blocks/compass_block_east"
        },
        "compass_block_west": {
            "textures": "textures/blocks/compass_block_west"
        },
        "compass_block_south": {
            "textures": "textures/blocks/compass_block_south"
        }
    }
}
```

## 定义名称

最后，让我们像这样定义我们的方块名称：

<CodeHeader>RP/texts/en_US.lang</CodeHeader>

```c
tile.wiki:custom_block.name=自定义方块
tile.wiki:compass_block.name=指南针方块
```

您可以在[这里](/concepts/text-and-translations)了解更多关于翻译的信息。

## 结果

在本页面中，您已了解以下内容：

-   [x] 方块的基本特性
-   [x] 如何将纹理应用于所有方块面
-   [x] 如何按面应用纹理

...但这仅仅是开始，看看您还可以做些什么吧！

## 接下来做什么？

<CardGrid>
<Card title="添加功能" image="/assets/images/homepage/crafting_table_0.png">

了解可用的方块[组件](/blocks/block-components)，以打造独特的游戏体验。

为什么不为您的方块添加一个自定义模型，使用[几何体](/blocks/block-components#geometry)组件呢？
您还可以配置自己的[碰撞](/blocks/block-components#collision-box)和[选择](/blocks/block-components#selection-box)框，以匹配！

</Card>
<Card title="创建变体" image="/assets/images/homepage/scripting.png">

利用方块[状态](/blocks/block-states)和[排列](/blocks/block-permutations)有条件地启用方块上的组件。

例如，您可以为自定义水箱方块添加液体深度级别，支持多种液体类型。

</Card>
<Card title="复制原版" image="/assets/images/homepage/diamond_ore_0.png">

浏览**原版重建**类别中现有方块的多个完整复制品。

从[自定义玻璃方块](/blocks/custom-glass-blocks)开始，使用[材质实例](/blocks/block-components#material-instances)进行简单的实现！

</Card>
</CardGrid>