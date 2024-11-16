---
title: 玩家加入时
category: 事件系统
mentions:
    - BedrockCommands
    - zheaEvyline
nav_order: 2
description: 此系统将在玩家加入世界时运行你所需的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

此系统将在玩家加入世界时运行你所需的命令。

## 设置

_在聊天中输入：_

`/scoreboard objectives add joined dummy`

如果你正在使用函数，并希望在世界初始化时自动添加目标，请按照 [首次加载世界](../commands/on-first-world-load.md) 中的流程进行操作。

## 系统

<CodeHeader>BP/functions/events/player/on_join.mcfunction</CodeHeader>

```yaml
## 注册首次加入或之前被清除的玩家到 'joined' 目标
scoreboard players add @a joined 0

## 在此处输入你的命令（示例）
tp @a [scores={joined=0}] 0 65 0

### 标记玩家为已加入
### 清除在线和离线玩家的 'joined' 分数
scoreboard players reset * joined
### 将在线玩家的分数设置为 1
scoreboard players set @a joined 1
```

![四个命令方块的链](../assets/images/commands/commandBlockChain/4.png)

在这里，我们使用了 `/tp` 命令作为示例，但你可以使用任何你喜欢的命令，并根据需要使用多个命令。

只需确保遵循给定的顺序，并正确应用 `scores={joined=0}` 选择器参数，如示例所示。

## 解释

当玩家加入时，他们的 `joined` 目标会添加一个 `0` 的分数。这使我们能够使用 `scores` 选择器参数从他们那里运行命令。

在命令运行后，我们使用通配符 **`*`** 重置所有目标上的分数。只有保持在线的玩家的分数会被设置为 `1`。

这样，由于我们的命令只针对分数为 `0` 的玩家，因此对于保持在线的玩家，命令不会重复，除非他们离开并重新加入，或者我们运行：

<br>`/scoreboard players set <player> joined 0`

这是因为将 `0` 的分数添加到 `1` 的分数不会产生变化。但将 `0` 的分数添加到没有分数的玩家会将他们的分数设置为 `0`。

## Tick JSON

如果你使用函数而不是命令方块，则必须将 `on_join` 函数添加到 `tick.json` 中，以便循环并持续运行。可以通过在每个字符串后添加逗号将多个文件添加到 `tick.json` 中。有关更多信息，请参阅 [函数](../commands/mcfunctions.md#tick-json) 文档。

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "events/player/on_join"
  ]
}
```

如果使用函数，则你的包文件夹结构将如下所示：

<FolderView
	:paths="[
    'BP',
    'BP/functions',
    'BP/pack_icon.png',
    'BP/manifest.json',
    'BP/functions/events',
    'BP/functions/events/player',
    'BP/functions/events/player/on_join.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

:::info 注意：

记分板名称（在此情况下为 'joined'）可能会被其他人使用。在后面附加 `_` 和一组随机生成的字符将减少冲突的概率。类似的技术也可以用于 `.mcfunction` 文件名。例如：

-   `joined_0fe678`
-   `on_join_0fe678.mcfunction`

:::