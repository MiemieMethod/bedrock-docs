---
title: 玩家死亡事件
category: 事件系统
mentions:
    - BedrockCommands
    - zheaEvyline
nav_order: 4
description: 当玩家死亡时，此系统将执行你指定的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

当玩家死亡时，此系统将执行你指定的命令。

## 设置

_在聊天中输入：_

`/scoreboard objectives add is_alive dummy`

如果你正在使用函数并希望在世界初始化时自动添加目标，请按照 [首次加载世界](../commands/on-first-world-load.md) 中的流程进行操作。

## 系统

<CodeHeader>BP/functions/events/player/on_death.mcfunction</CodeHeader>

```yaml
## 设置玩家状态
### 不活跃
scoreboard players set @a [scores={is_alive=!2}] is_alive 0
### 活跃
scoreboard players set @e [type=player] is_alive 1

## 在此处输入你的命令（示例）
execute as @a [scores={is_alive=0}] run say 我死了

## 标记已执行死者命令
scoreboard players set @a [scores={is_alive=0}] is_alive 2
```

![commandBlockChain4](../assets/images/commands/commandBlockChain/4.png)

在这里，我们使用了 `/execute - say` 命令作为示例，但你可以使用任何你喜欢的命令，并根据需要添加多个命令。

只需确保按照给定的顺序，并正确应用 `scores={alive=0}` 选择器参数，如所示，以便执行你想要的命令。

## 解释

-   **`is_alive=0`** 玩家是 _不活跃_（死亡）。
-   **`is_alive=1`** 玩家是活跃的。
-   **`is_alive=2`** 玩家已经死亡，我们已对他们执行了所需的命令。

**每个命令的目的：**

1. **命令 1：** 所有玩家默认标记为 _不活跃_（0）。
    - 我们将忽略分数 `2`，否则我们想在玩家死亡时运行的命令将触发多次。
2. **命令 2：** 所有活跃玩家将被标记为 '活跃'（1）。
    - `@e` 选择器允许我们专门针对活跃的玩家。
    - `@a` 选择器将针对所有玩家，无论他们是否活跃。
3. **命令 3：** 现在活跃玩家的分数为 1，而不活跃玩家的分数为 0，我们将利用这一知识在玩家死亡（0）时运行所需的命令。
4. **命令 4：** 由于我们希望在玩家死亡时只执行一次所需的命令，因此我们将他们的分数设置为 `2`。不这样做将导致命令在他们复活之前重复执行。

## Tick JSON

如果你使用函数而不是命令方块，则必须将 `on_death` 函数添加到 `tick.json` 中，以便循环并持续运行。可以通过在每个字符串后添加逗号将多个文件添加到 `tick.json` 中。有关更多信息，请参考 [函数](../commands/mcfunctions.md#tick-json) 文档。

<CodeHeader>BP/functions/tick.json</CodeHeader>
```json
{
  "values": [
    "events/player/on_death"
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
    'BP/functions/events/player/on_death.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

:::info 注意：

记分板名称（在本例中为 'is*alive'）可能会被其他人使用。在后面附加 ` * ` 和一组随机生成的字符将减少冲突的可能性。类似的技术也可以用于 `.mcfunction` 文件名。例如：

-   `is_alive_0fe678`
-   `on_death_0fe678.mcfunction`

:::

## 替代方法

此方法在 Minecraft `1.19.50` 中引入了新的 `/execute` 语法后成为可能。

:::warning 已知问题：
如果两个或更多玩家被传送到同一点，其中一个玩家死亡而其他玩家不移动，系统将无法执行命令。
:::

-   确保添加 `is_dead` 记分板目标：
    -   `/scoreboard objectives add is_dead dummy`

<CodeHeader>BP/functions/states/is_dead.mcfunction</CodeHeader>

```yaml
## 设置玩家状态
### 不死亡
scoreboard players set @e [type=player] is_dead 0
### 死亡
execute as @a at @s unless entity @e [type=player, r=0.01] run scoreboard players add @s is_dead 1

## 在此处输入你的命令（示例）
### 在死亡位置召唤盔甲架
execute as @a [scores={is_dead=1}] at @s run summon armor_stand "死去的玩家" ~~~
### 聊天中的死亡消息
execute as @a [scores={is_dead=1..}] run say 我死了，还没有复活..
```

![commandBlockChain4](../assets/images/commands/commandBlockChain/4.png)

**状态：**

-   **`is_dead=0`** 玩家是 _不死亡_（活跃）。
-   **`is_dead=1`** 玩家刚刚死亡。（用于 '触发' 动作）
-   **`is_dead=1..`** 玩家仍然死亡。（用于重复动作）

**每个命令的目的：**

1. **命令 1：** 所有活跃玩家标记为 _不死亡_（0）。
2. **命令 2：** 如果在玩家周围 0.01 个方块半径内没有活跃玩家，他们将被标记为死亡（1）。
    - 逻辑是只有玩家自己可以在如此小的半径内存在。两个或多个玩家精确站在同一点的概率几乎为零。
3. **命令 3、4：** 这些是示例命令（针对每个状态），可以进行修改/扩展。