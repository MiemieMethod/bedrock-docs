---
title: 使用装备物品运行命令
category: 教程
tags:
    - 实验性
    - 中级
mentions:
    - Chikorita-Lover
    - MedicalJewel105
    - Luthorius
    - TheItsNameless
description: 当物品被装备时运行命令。
---

## 介绍

附加包的一个常见概念是实现具有独特效果的新盔甲套装，就像海龟壳和下界合金盔甲一样。虽然物品具有击退抗性组件，但它们并没有在特定条件下施加生物效果、发出粒子等的组件。然而，利用服务器动画、Molang和物品标签，这可以轻松实现！

请记住，这需要修改玩家行为，这是许多附加包的共同主题；因此，如果你希望这样做，你的附加包可能与其他附加包不兼容。

> 不过，有些人找到了不使用player.json的方法。他们用虚拟实体替代它。可以自己尝试一下！

## 服务器动画

第一步是创建一个服务器动画，这是一个在特定关键帧运行命令或事件的文件。虽然客户端动画在资源包中，但服务器动画在行为包中。你可以在[这里](../entities/timers.md#animation-based-timers)阅读更多信息。我们可以使用以下内容作为模板：

```json title="BP/animations/player.json"
{
    "format_version": "1.10.0",
    "animations": {
        "animation.player.emerald_armor": {
            "timeline": {
                "0.0": []
            },
            "animation_length": 0.05,
            "loop": true
        }
    }
}
```

让我们来看看这个模板中的内容以及它的作用：

- `animation.player.emerald_armor`是我们动画的标识符；你可以将其更改为其他名称，例如`animation.player.phantom_armor`。
- `timeline`在给定关键帧运行命令和事件。
- `animation_length`是动画持续的时间；我们将使用0.05秒，因为这是游戏内一个刻的长度。
- `loop`非常简单；将其设置为true会使动画循环。

我们可以在时间线的`0.0`数组中添加要执行的命令，例如`/effect`命令，如下所示：

```json title="BP/animations/player.json#timeline"
{
    "0.0": ["/effect @s speed 1 0"]
}
```

当然，我们不局限于`/effect`。如果你想使用其他命令，例如`/function`或`/particle`，请随意使用！

完成后，我们在服务器动画中的工作就结束了，接下来我们将快速添加到物品的行为文件中。

## 物品行为

要实际检查我们的物品是否被装备，我们可以使用一个检查物品标签的Molang查询。

如果你想：

- 检查一个原版物品，例如通过`minecraft:iron_tier`标签检查铁盔甲件
- 通过`q.is_item_name_any`检查物品，该查询检查任何槽中的物品标识符

你可以跳过本节。

在我们物品的行为中，我们需要在`components`中添加一个标签。例如，如果我们想添加`example:emerald_tier`标签，我们将添加`tag:example:emerald_tier`组件：

```json title="BP/items/my_item.json#components"
"tag:example:emerald_tier": {}
```

就这样，现在你的物品拥有你分配的任何标签！如果你想添加更多标签也可以，但这就是我们所需的全部。

## 玩家行为

最后，我们需要修改玩家的行为以运行服务器动画。我们将完全在`description`中进行操作。

首先，我们需要为我们的动画设置一个短名称。如果你有任何客户端动画的经验，这个过程会非常相似。将`animations`添加到`description`中，并设置一个短名称，如下所示：

```json title="BP/entities/player.json#description"
{
    "identifier": "minecraft:player",
    "is_spawnable": false,
    "is_summonable": false,
    "is_experimental": false,
    "animations": {
        "emerald_armor": "animation.player.emerald_armor"
    }
}
```

现在设置了短名称，我们可以运行我们的动画。

将`scripts`添加到`description`中，并设置一个Molang查询来运行。要检查物品，我们可以使用以下之一：

- `q.is_item_name_any`，检查任何槽中的给定物品标识符。此示例将检查`example:totem_of_retreat`是否在任一手中：

```
q.is_item_name_any('slot.weapon.mainhand',0,'example:totem_of_retreat') || q.is_item_name_any('slot.weapon.offhand',0,'example:totem_of_retreat')
```

- `q.equipped_item_any_tag`，检查给定槽中是否至少有一个给定标签的物品。此示例将允许使用翡翠或幻影等级的盔甲件：

```
q.equipped_item_any_tag('slot.armor.head','example:emerald_tier','example:phantom_tier')
```

- `q.equipped_item_all_tags`，检查给定槽中是否所有给定标签的物品。此示例将仅允许同时具有翡翠和古代等级的盔甲件：

```
q.equipped_item_all_tags('slot.armor.head','example:ancient_tier','example:emerald_tier')
```

让我们看看一个使用`q.equipped_item_any_tag`的示例：

```json title="BP/entities/player.json#description"
{
    "identifier": "minecraft:player",
    "is_spawnable": false,
    "is_summonable": false,
    "is_experimental": false,
    "animations": {
        "emerald_armor": "animation.player.emerald_armor"
    },
    "scripts": {
        "animate": [
            {
                "emerald_armor": "q.equipped_item_any_tag('slot.armor.head','example:emerald_tier')"
            }
        ]
    }
}
```

如果在头盔槽中装备了翡翠等级的物品，则此示例将运行带有`emerald_armor`短名称的服务器动画。你可以更改Molang字段以匹配你的物品标签，使用不同的查询或添加其他查询。

你可以在[Minecraft Wiki](https://minecraft.wiki/w/Slot#Bedrock_Edition)查看其他槽标识符的列表。

## 结论

通过设置服务器动画、玩家行为和物品标签，你的装备物品现在可以运行命令了！这种技术允许比仅限于物品组件更大的物品自定义。如果你想为效果或附加包添加更多内容，请查看下一部分；否则，恭喜你，完成了！

## 附加内容

### 多个必需物品

如果你希望在装备多个盔甲套装的部件时运行命令，我们可以扩展之前的Molang：

```json title="BP/entities/player.json#scripts"
"animate": [
    {
        "emerald_armor": "q.equipped_item_any_tag('slot.armor.head','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.chest','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.legs','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.feet','example:emerald_tier')"
    }
]
```

此示例将检查所有四个盔甲槽中是否装备了翡翠等级的盔甲，并在全部装备时运行动画。

### 进一步条件

海龟壳并不总是施加水下呼吸效果，而是仅在玩家首次进入水中时持续10秒。如果我们希望我们的翡翠盔甲仅在我们健康值较低时运行动画，我们可以在Molang中添加另一个查询：

```json title="BP/entities/player.json#scripts"
"animate": [
    {
        "emerald_armor": "q.equipped_item_any_tag('slot.armor.head','example:emerald_tier') && q.health <= 5"
    }
]
```

此示例将在剩余2.5颗心或更少时运行动画，允许玩家在危险时迅速逃脱。

我们还可以将其应用于要求多个盔甲件，使用更长的Molang：

```json title="BP/entities/player.json#scripts"
{
    "animate": [
        {
            "emerald_armor": "q.equipped_item_any_tag('slot.armor.head','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.chest','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.legs','example:emerald_tier') && q.equipped_item_any_tag('slot.armor.feet','example:emerald_tier') && q.health <= 5"
        }
    ]
}
```

你可以在[bedrock.dev](https://bedrock.dev/docs/stable/Molang#List%20of%20Entity%20Queries)查看已记录的Molang查询列表。

### 带有效果的多个物品

如果你想添加更多具有独特效果的物品，不用担心；这很简单。你可以创建一个新的服务器动画文件，或者在之前的文件中添加，如下所示：

```json title="BP/animations/player.json"
{
    "format_version": "1.10.0",
    "animations": {
        "animation.player.emerald_armor": {
            "timeline": {
                "0.0": ["..."]
            },
            "animation_length": 0.05,
            "loop": true
        },
        "animation.player.phantom_armor": {
            "timeline": {
                "0.0": ["..."]
            },
            "animation_length": 0.05,
            "loop": true
        }
    }
}
```

在我们的玩家行为中，你还需要在`animations`和`scripts`中添加内容。

```json title="BP/entities/player.json#description"
{
    "identifier": "minecraft:player",
    "is_spawnable": false,
    "is_summonable": false,
    "is_experimental": false,
    "animations": {
        "emerald_armor": "animation.player.emerald_armor",
        "phantom_armor": "animation.player.phantom_armor"
    },
    "scripts": {
        "animate": [
            {
                "emerald_armor": "q.equipped_item_any_tag('slot.armor.head','example:emerald_tier')"
            },
            {
                "phantom_armor": "q.equipped_item_any_tag('slot.armor.head','example:phantom_tier')"
            }
        ]
    }
}
```