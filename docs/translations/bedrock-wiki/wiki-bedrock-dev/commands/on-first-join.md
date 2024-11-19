---
title: 玩家首次加入时
category: 事件系统
mentions:
    - BedrockCommands
    - zheaEvyline
    - SmokeyStack
nav_order: 1
description: 此系统将在玩家首次加入世界时运行你指定的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

此系统将在玩家首次加入世界时运行你指定的命令。

## 系统

```yaml title="BP/functions/events/player/on_first_join.mcfunction"
## 在这里输入你的命令（示例）
### 给石镐 ×1
give @a [tag=!joined] stone_pickaxe
### 给面包 ×16
give @a [tag=!joined] bread 16

## 标记为已加入
tag @a [tag=!joined] add joined
```

![三个命令方块的链](../assets/images/commands/commandBlockChain/3.png)

在这里，我们使用了两个 `/give` 命令作为示例，但你可以使用任何你喜欢的命令，并根据需要添加多个命令。

只需确保遵循给定的顺序，并正确应用 `tag=!joined` 选择器参数，如示例所示。

## 说明

当玩家首次加入世界时，他们将没有已加入的标签。

一旦我们为没有该标签的玩家运行所需的命令，他们将立即获得该标签，除非我们使用以下命令移除他们的标签：

<br>`/tag <player> remove joined`

## Tick JSON

如果你使用函数而不是命令方块，则必须将 `on_first_join` 函数添加到 `tick.json` 中，以便循环并持续运行。可以通过在每个字符串后添加逗号来将多个文件添加到 `tick.json` 中。有关更多信息，请参阅 [Functions](../commands/mcfunctions.md#tick-json) 文档。

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "events/player/on_first_join"
  ]
}
```

如果使用函数，你的包文件夹结构将如下所示：

<FolderView
	:paths="[
    'BP',
    'BP/functions',
    'BP/pack_icon.png',
    'BP/manifest.json',
    'BP/functions/events',
    'BP/functions/events/player',
    'BP/functions/events/player/on_first_join.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

/// info | 注意：

标签名称（在本例中为 'joined'）可能会被其他人使用。可以在后面附加 `_` 和一组随机生成的字符，以减少冲突的概率。类似的技术也可以应用于 `.mcfunction` 文件名。例如：

-   `joined_0fe678`
-   `on_first_join_0fe678.mcfunction`

///