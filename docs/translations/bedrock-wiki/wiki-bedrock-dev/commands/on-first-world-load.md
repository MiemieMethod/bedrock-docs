---
title: 首次加载世界时
category: 事件系统
mentions:
    - BedrockCommands
    - zheaEvyline
    - SmokeyStack
    - cda94581
nav_order: 6
description: 此系统将在应用您的附加包后，首次加载世界时运行您所需的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

此系统将在应用您的附加包后，首次加载世界时运行您所需的命令。
> 注意：要实现此系统，需要一个 [功能](../commands/mcfunctions.md) 包，因为 `tick.json` 文件使我们能够在世界初始化后立即运行命令。

## Tick JSON

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "events/world/on_initialise"
  ]
}
```

## 系统

<CodeHeader>BP/functions/events/world/on_initialise.mcfunction</CodeHeader>
```yaml
## 初始化
### 添加目标
scoreboard objectives add world dummy
### 注册到目标
scoreboard players add Initialised world 0

## 在此处输入您的命令（示例）
execute if score Initialised world matches 0 run say 新世界已创建！

## 标记为已初始化
scoreboard players set Initialised world 1
```

在这里，我们使用了一个 `/execute - say` 命令作为示例，但您可以使用任何您喜欢的命令，并根据需要使用多个命令。

只需确保遵循给定的顺序，并正确应用 `/execute if score` 条件，如所示，以运行您所需的命令。

## 解释

- **` Initialised=0 `** 世界刚刚初始化，我们尚未运行所需的初始化命令。
- **` Initialised=1 `** 世界已初始化，我们已执行初始化命令。

添加名为 `world` 的目标，以便我们可以将分数保存到其中，从而跟踪世界是否已初始化。这也使我们能够将命令结构化，仅在世界初始化时执行。

在创建目标后，向虚拟玩家名称 'Initialised' 添加分数 `0`。这将使其注册到目标，并使我们能够使用 `/execute if score` 条件来运行所需的命令。

最后，在执行所有命令后，将虚拟玩家名称 'Initialised' 的分数设置为 `1`。这样可以防止进入循环并执行多次。

## 文件夹结构

<FolderView
	:paths="[
    'BP',
    'BP/functions',
    'BP/pack_icon.png',
    'BP/manifest.json',
    'BP/functions/events',
    'BP/functions/events/world',
    'BP/functions/events/world/on_initialise.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

:::info 注意：

记分板名称（在本例中为 'world'）可能会被其他人使用。在后面添加 ` _ ` 和一组随机生成的字符可以减少冲突的概率。类似的技术也可以用于 ` .mcfunction ` 文件名。例如：
- ` world_0fe678 `
- ` on_initialise_0fe678.mcfunction `

:::