---
title: 附加物
category: 文档
tags:
    - 初学者
mentions:
    - Sprunkles317
    - MedicalJewel105
    - AdamRaichu
    - Luthorius
    - TheItsNameless
description: 附加物的文档。
---

::: tip
本文件假设您对Molang、渲染控制器、动画和客户端实体定义有基本了解。请确保您熟悉[客户端实体](../entities/entity-intro-rp.md)的基础知识！
:::

## 介绍

当我们设计一个自定义物品或方块时，Minecraft会根据模板构建一个模型，以便在持有时显示该物品。这表现为物品的精灵是一个挤压的纹理网格，或者方块以其模型显示。通过使用一种称为**附加物**的系统，我们可以设计自己的模型，在这些物品被持有时显示。

想让木棍看起来像望远镜吗？或者挥舞一把旋转链条的大电锯？附加物就是实现这些效果的方法！

本文涵盖了**两种不同的方法**来创建附加物，具体取决于所使用几何体的构造方式。

## 概述

附加物是一种在物品或方块被装备时渲染实体模型的系统。这意味着物品被持在主手、副手或盔甲槽中。

附加物定义的设计与客户端实体定义非常相似；它们允许我们定义纹理、材料、几何体和动画，以显示附加物。

### 文件结构

附加物定义放在“attachables”文件夹内。文件布局与自定义实体相同。

<FolderView
	:paths="[
    'RP/animations/my_item.animation.json',
    'RP/attachables/my_item.entity.json',
    'RP/models/entity/my_item.geo.json',
    'RP/textures/entity/my_item.png',
    'RP/manifest.json'
  ]"
></FolderView>

### 附加物定义

以下是一个附加物的基本示例。

<CodeHeader>RP/attachables/stick.entity.json</CodeHeader>

```json
{
    "format_version": "1.10.0",
    "minecraft:attachable": {
        "description": {
            "identifier": "minecraft:stick",
            "materials": {
                "default": "entity",
                "enchanted": "entity_alphatest_glint"
            },
            "textures": {
                "default": "textures/entity/steve",
                "enchanted": "textures/misc/enchanted_item_glint"
            },
            "geometry": {
                "default": "geometry.wiki.steve_head"
            },
            "animations": {
                "hold_first_person": "animation.steve_head.hold_first_person",
                "hold_third_person": "animation.steve_head.hold_third_person"
            },
            "scripts": {
                "animate": [
                    {
                        "hold_first_person": "context.is_first_person == 1.0"
                    },
                    {
                        "hold_third_person": "context.is_first_person == 0.0"
                    }
                ]
            },
            "render_controllers": ["controller.render.item_default"]
        }
    }
}
```

关于这个附加物定义，有几点需要注意：

-   标识符与现有的方块或物品ID匹配。当物品被装备时，这将激活附加物，并替换持有时显示的原始模型。
-   列出了材料和纹理用于附魔闪光。如果您的物品在附魔时应该有闪光效果，这一点非常重要。

制作附加物比制作客户端实体文件稍微复杂一些。我们需要正确地装配几何体的骨架，以确保在装备时看起来正确。

## 方法一 - 附加到骨架

<Label name="初学者" color="blue"></Label>

在第一种方法中，我们将使用玩家的骨架副本构建附加物，将您的模型附加到玩家的一个骨骼上。

这种解决方案非常适合仅涉及一种类型的生物/实体（尤其是玩家）和仅涉及一个装备槽的模型。使用Blockbench查看模型的外观非常简单。

### 设置骨架

我们需要重建玩家的骨架，以便我们的模型能够正确附加到相应的骨骼上，否则它将不会附加到任何东西上，并会在玩家身上自由漂浮。

使用文本编辑器，从提供的玩家骨架文件中复制骨骼到您的几何体文件中，然后将`rightItem`骨骼设置为您模型中立方体的父骨骼。将此几何体保存到您的资源包中。

为了方便，这里准备了一个这样的模型。玩家模型中的立方体已经被移除：

<Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_one/steve_head.geo.json?raw=true">
    📄 几何体文件
</Button>

### 显示设置

让您的模型漂浮在玩家的脚下并不是理想的。我们的下一步是创建动画，以便能够正确显示模型。

创建两个新动画，一个用于第一人称持有物品，另一个用于第三人称持有物品。选择您的第三人称动画，并根据需要进行定位。将此动画保存到您的资源包中。

以下是一个这样的动画示例。这也包括一个第一人称动画，制作方法在下面的部分中详细说明。

<Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_one/steve_head.animation.json?raw=true">
    📄 动画文件
</Button>

### 第一人称动画

为了更轻松地创建第一人称动画，我们需要模拟手臂在第一人称中的位置。

:::tip
要为玩家的手添加动画，您需要使用玩家的动画，而不是附加物的动画。
:::

使用以下引导动画并将其导入Blockbench。它对右臂骨骼应用了(95, -45, 115)的旋转和(13.5, -10, 12)的平移，完美模拟了第一人称中手臂的位置。

<Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_one/attachable_guide.animation.json?raw=true">
    📄 附加物引导文件
</Button>

:::warning 注意
这时事情变得复杂。两个动画需要同时播放；您的第一人称动画和引导的第一人称动画。

确保在进行更改时正在编辑您的动画。首先选择它，然后在上面播放引导的第一人称动画。
:::

### 结论

设置完成后，如果玩家骨架中还有任何立方体，请将其删除，但保留骨骼。检查游戏中的模型效果！

## 方法二 - 绑定到骨骼

<Label name="中级" color="orange"></Label>

在第二种方法中，附加物几何体将通过模型绑定构建。这允许模型直接附加到生物几何体中的一个骨骼上，与其装备的槽相对应。Minecraft为其附加物品（包括三叉戟、望远镜、弓和盾牌）采用模型绑定。

虽然这种方法允许附加物更动态地应用于其他生物和装备槽，但模型绑定也有一些奇怪的特性，下面将进行说明。一些开发者可能会发现这种方法更难以实现。

### 模型绑定

我们的第一步是将模型文件格式版本升级到`"1.16.0"`，如果尚未升级。如果模型是遗留文件，请在继续之前进行转换；Blockbench有一个工具可以做到这一点（文件 → 转换项目）。

接下来是修改我们几何体的根骨骼，使其绑定到物品放置的装备槽。请注意以下来自骨架头几何体文件的第4行：

<CodeHeader>RP/models/entity/skeleton_head.geo.json</CodeHeader>

```json
// 一个骨骼
{
    "name": "skeleton_head",
    "binding": "q.item_slot_to_bone_name(context.item_slot)",
    "pivot": [0, 4, 0],
    "cubes": [
        {
            "origin": [-4, 0, -4],
            "size": [8, 8, 8],
            "uv": [0, 0]
        }
    ]
}
```

骨骼中的`"parent"`键接受一个字符串，输入的任何骨骼名称将被设置为当前骨骼的父骨骼；子骨骼保持其位置，但相对于父骨骼移动。

另一方面，`"binding"`键接受Molang，输入的任何骨骼名称的枢轴点被设置为子骨骼及其子骨骼应继承的**根位置**。

对于`"binding"`的值，我们使用Molang查询`q.item_slot_to_bone_name`，它将槽名称转换为骨骼名称，使用上下文变量`context.item_slot`作为参数。这将此物品所在的装备槽名称转换为玩家几何体中的相应骨骼名称。转换如下：

-   `'main_hand'` → "rightitem"
-   `'off_hand'` → "leftitem"

将模型绑定应用到您的骨骼，并将几何体保存到您的资源包中。

提供了一个应用了此绑定的示例模型：

<Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_two/skeleton_head.geo.json?raw=true">
    📄 几何体文件
</Button>

### 显示设置

完成后，下一步是设置动画，以便在第一人称和第三人称中显示模型。

创建两个新动画，一个用于第一人称持有物品，另一个用于第三人称持有物品。

为了更轻松地创建这些动画，请执行以下操作：

-   下载以下玩家骨架模型。我们将其用作定位模型的视觉辅助。

    <Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_two/player_skeleton.geo.json?raw=true">
        📄 玩家骨架文件
    </Button>

-   使用文本编辑器，将模型中的骨骼和立方体添加到玩家骨架模型中，然后将玩家骨架模型导入Blockbench。
-   将您模型的根骨骼设置为玩家骨架中的`rightItem`骨骼的子骨骼。
-   下载以下动画文件并导入`wiki.third_person_guide`动画。稍后将用于简化定位。

    <Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_two/attachable_guide.animation.json?raw=true">
        📄 附加物引导文件
    </Button>

这些引导动画有一个显著的特点：它们对右物品骨骼的y位置应用了-24的偏移，以抵消Minecraft对绑定骨骼应用的类似-24 y位置偏移。我们目前不确定为什么会这样。

:::warning 注意
与方法一类似，**两个**动画需要同时播放以确保正确定位。

确保在进行更改时正在编辑您的动画。首先选择它，然后在上面播放引导动画。
:::

播放两个动画，并根据需要定位您的模型。将动画保存到您的资源包中。

以下是一个用于此定位的示例动画文件：

<Button link="https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/public/assets/packs/tutorials/attachables/method_two/skeleton_head.animation.json?raw=true">
    📄 动画文件
</Button>

### 第一人称动画

与第三人称动画类似，请查看附加物引导文件并将`wiki.first_person_guide`动画导入Blockbench。将您的动画与引导的第一人称动画一起播放，然后进行更改并保存文件。

## 示例包

这两种方法已被编译成一个示例包，供您参考，以防您遇到困难或只是想查看一个工作示例。

<Button link="https://github.com/Bedrock-OSS/wiki-addon/releases/download/download/attachable-example.mcpack">
    💾 示例包
</Button>