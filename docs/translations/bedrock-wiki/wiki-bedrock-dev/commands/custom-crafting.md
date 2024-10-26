---
title: 自定义合成器
description: 如何使用命令制作一个模拟的自定义合成系统
category: 指南
tags: [简单, 指南]
---

## 介绍

这是一个关于如何使用仅两个命令方块制作自定义合成系统的指南。一些使用案例可能是为服务器或冒险地图“合成”具有自定义名称和附魔的工具或武器。

_**这个系统最初是由CrunchyCookie创建的。所有关于这个系统的荣誉归他所有。你可以在[这里](https://www.youtube.com/watch?v=pzQzldaSORs)找到他的视频。**_

:::warning
这并不是制作自定义合成配方的实际方法。这是一种创造性且迂回的方式，使用克隆命令和投掷器来实现自定义合成。有关使用合成台的自定义合成配方，请参见[此维基页面](../loot/recipes)。
:::

## 系统

:::info 注意
每当我们使用词语 `<crafter>` 时，我们指的是用作合成器的投掷器的坐标。如果你看到 `<crafterX>`、`<crafterY>` 或 `<crafterZ>`，我们指的是投掷器的 X、Y、Z 坐标。
:::

1. 放置一个朝下的投掷器。这将用于模拟原版合成器，并将在本页面的其余部分中称为“合成器”。
2. 将一个重复命令方块横向放置，并粘贴以下命令：`execute if blocks ~ ~1 ~ ~ ~1 ~ <crafter> masked run playsound random.orb @a[x=<crafterX>, y=<crafterY>, z=<crafterZ>, r=6]`
3. 在重复命令方块前放置一个链式命令方块，并将其设置为条件。然后粘贴以下命令：`clone ~ ~1 ~ ~ ~1 ~ <crafter>`
4. 在命令方块上方放置两个朝下的投掷器。将第一个投掷器填充为你制作的自定义配方。然后将第二个投掷器填充为合成出的物品。（提示：将合成出的物品放在第二个投掷器的中间槽中，这样看起来更美观。）

完成后，你应该得到如下结构：

<WikiImage
    src="/assets/images/commands/customCrafterEnd.png"
    alt="替代文本"
    width=800
/>

## 解释

命令 1: `execute if blocks ~ ~1 ~ ~ ~1 ~ <crafter> masked run playsound random.orb @a[x=<crafterX>, y=<crafterY>, z=<crafterZ>, r=6]`

每个游戏刻，重复命令方块都会检查其上方一个区块的投掷器是否与玩家交互的投掷器具有相同的状态和内容。如果这两个区块相同，则执行播放声音命令，并继续到下一个命令方块。

命令 2: `clone ~ ~1 ~ ~ ~1 ~ <crafter>`

因为这个命令方块是条件性的，它不会在后面的命令方块成功之前激活。当这个命令方块激活时，它会运行一个克隆命令，将其上方一个区块的内容克隆到另一个投掷器的位置。

以下是一个示例结构：

<Button link="/assets/packs/structures/customCrafter/customCrafterExample.mcstructure" download>
    下载 MCSTRUCTURE
</Button>

:::info 注意
你仍然需要在命令中将 `<crafter>` 替换为玩家将要交互的输入投掷器的坐标。
:::