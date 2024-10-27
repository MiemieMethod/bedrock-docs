---
title: 实体计数器
category: 记分板系统
mentions:
    - BedrockCommands
    - zheaEvyline
nav_order: 3
description: 此系统允许您跟踪世界中玩家/实体的总数，并根据获得的值执行所需的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

此系统允许您跟踪世界中玩家/实体的总数，并根据获得的值执行所需的命令。

> 注意：未加载区块中的实体将不会被跟踪。然而，玩家可以被跟踪。

## 设置

_在聊天中输入：_

`/scoreboard objectives add count dummy`

如果您正在使用函数，并希望在世界初始化时自动添加目标，请按照[首次加载世界](../commands/on-first-world-load.md)中的流程进行操作。

## 系统

<CodeHeader>BP/functions/scoreboards/entity_counter.mcfunction</CodeHeader>

```yaml
## 重置先前的计数
scoreboard players set * count 0

## 获取当前计数（示例）
### 活着的玩家
execute as @e[type=player] run scoreboard players add AlivePlayers count 1
### 苦力怕
execute as @e[type=creeper] run scoreboard players add Creepers count 1

## 在此处输入您的命令（示例）
### 当活着的玩家数量大于等于4时发送消息
execute if score AlivePlayers count matches 4.. run title @a actionbar 世界中有超过4名玩家。
### 当苦力怕数量小于等于3时发送消息
execute if score Creepers count matches ..3 run title @a actionbar 世界中有少于3只苦力怕。
```

![5个命令方块的链](../assets/images/commands/commandBlockChain/5.png)

在这里，我们跟踪活着的玩家和苦力怕作为示例，但您可以跟踪任何您喜欢的实体，并根据需要跟踪多个实体。您还可以根据自己的喜好更改假玩家名称。例如：将 'AlivePlayers' 改为 'Players'。

同样，我们运行 `/title` 命令作为示例：

-   a) 当玩家数量为4或更多时 `4..`
-   b) 当苦力怕数量为3或更少时 `..3`

您也可以修改/扩展这些命令。例如：用 `/kill` 命令替代 `/title` 命令。

## 解释

1. **命令1：** 将所有假玩家名称在 `count` 记分板目标中的分数设置为 `0`，包括任何被跟踪的玩家和实体。
2. **命令2, 3：** 从每个您希望跟踪计数的目标中，将分数添加到其对应的假玩家名称中，从而获得它们的总计数。
    - 示例：将苦力怕生物计数到 'Creepers' 假玩家名称。
3. **命令4, 5：** 这些是可以修改/扩展的示例命令。
    - 根据获得的总计数，我们可以使用 `/execute if score` 条件在满足特定值时运行所需的命令。
        - **`n`** 任何数字 _n_
        - **`n..`** 任何数字 _n_ 及以上
        - **`..n`** 任何数字 _n_ 及以下
        - **`n..n1`** 从任何数字 _n_ 到任何数字 _n1_。（较小的数字在前）

## Tick JSON

如果您使用函数而不是命令方块，则必须将 `entity_counter` 函数添加到 `tick.json` 中，以便循环并持续运行。可以通过在每个字符串后添加逗号来将多个文件添加到 `tick.json` 中。有关更多信息，请参阅[函数](../commands/mcfunctions.md#tick-json)文档。

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "scoreboards/entity_counter"
  ]
}
```

如果使用函数，您的资源包文件夹结构将如下所示：

<FolderView
	:paths="[
    'BP',
    'BP/functions',
    'BP/pack_icon.png',
    'BP/manifest.json',
    'BP/functions/scoreboards',
    'BP/functions/scoreboards/entity_counter.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

:::info 注意：

记分板名称（在本例中为 'count'）可能会被其他人使用。在后面附加 `_` 和一组随机生成的字符将减少冲突的概率。类似的技术也可以用于 `.mcfunction` 文件名。例如：

-   `count_0fe678`
-   `entity_counter_0fe678.mcfunction`

:::