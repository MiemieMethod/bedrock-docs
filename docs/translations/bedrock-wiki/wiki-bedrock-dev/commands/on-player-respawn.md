---
title: 玩家重生机制
category: 事件系统
mentions:
    - BedrockCommands
    - zheaEvyline
nav_order: 5
description: 该系统将在玩家从死亡状态重生时执行你所需的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

该系统将在玩家从死亡状态重生时执行你所需的命令。

## 设置

*在聊天中输入：*

`/scoreboard objectives add respawn dummy`

如果你正在使用函数，并希望在世界初始化时自动添加该目标，请按照[首次加载世界](../commands/on-first-world-load.md)中的流程进行操作。

## 系统

```yaml title="BP/functions/events/player/on_respawn.mcfunction"
## 在此输入你的命令（示例）
execute as @e [scores={respawn=1}] run say 我死了并重生了。

## 设置玩家状态
### 当前重生中
scoreboard players set @a respawn 1
### 当前未重生
scoreboard players set @e [type=player] respawn 0
```
![三块命令方块链](../assets/images/commands/commandBlockChain/3.png)

在这里，我们使用了一个 `/execute - say` 命令作为示例，但你可以使用任何你喜欢的命令，并根据需要使用多个命令。

只需确保遵循给定的顺序，并正确应用 `@e [scores={respawn=1}]` 选择器参数，以便执行你所需的命令。

## 解释

- **`respawn=0`** 玩家处于存活状态或已经重生。
- **`respawn=1`** 玩家处于死亡状态或刚刚重生（在当前游戏刻）。
- **`@a`** 选择器将针对所有存活/死亡的玩家。因此，我们将使用它将玩家标记为 `1` '重生中'。
- **`@e`** 选择器则只会针对存活的玩家，因此我们可以用它将所有存活的玩家标记为 `0` '已重生'。

现在，*重生中*的玩家为 `1`，*已重生*的玩家为 `0`，我们可以利用这一知识在得分为 `1` 的玩家从死亡状态重生时执行我们所需的命令。它们是通过 `@e` 选择器进行定位的。

在系统中，你所需的命令必须在其他两个命令之前，因为玩家在游戏刻开始时会从死亡状态转变为存活状态，随后才会执行命令。

因此，如果我们将它们放在最后，其他两个命令将首先将重生中的玩家得分设置为 `0`，而你想要执行的命令将无法选择这些玩家，因为我们的选择器参数是 `@e [scores={respawn=1}]`，而不是 `0`。使用 `0` 将不起作用，因为这将导致即使是已经重生的玩家也会无限重复。

## Tick JSON

如果你使用函数而不是命令方块，则必须将 `on_respawn` 函数添加到 `tick.json` 中，以便循环并持续运行。可以通过在每个字符串后添加逗号来将多个文件添加到 `tick.json` 中。有关更多信息，请参阅[函数](../commands/mcfunctions.md#tick-json)文档。

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "events/player/on_respawn"
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
    'BP/functions/events/player/on_respawn.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

:::info 注意：

记分板名称（在此案例中为：'respawn'）可能会被其他人使用。在后面附加 `_` 和一组随机生成的字符将减少冲突的概率。类似的技术也可以用于 `.mcfunction` 文件名。例如：
- `respawn_0fe678`
- `on_respawn_0fe678.mcfunction`

:::