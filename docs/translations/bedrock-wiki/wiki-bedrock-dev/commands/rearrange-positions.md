---
title: 多人位置重排
category: 函数
mention:
    - BedrockCommands
    - zheaEvyline
    - jeanmajid
description: 随机重新定位所有选定目标，确保没有目标保持在其原始位置。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

多人位置重排函数，或更准确地说是多人位置错排函数，由 @ZheaEvyline 创建，允许你随机重新定位所有选定目标，确保没有目标保持在其原始位置。

错排是指 'N' 个元素的一个排列，其中没有元素出现在其原始位置。

例如，如果玩家1在 `(0, 0, 1)`，玩家2在 `(0, 0, 2)`，玩家3在 `(0, 0, 3)`，那么玩家1只能被重新定位到 `(0, 0, 2)` 或 `(0, 0, 3)`。同样的规则适用于其他所有玩家。

<br>

**此功能包的主要特点：**

1. 在一个游戏刻中保证错排。
2. 最小的迭代次数（重复/循环）。
3. 跨维度兼容性。

此功能包设计支持无限数量的目标。然而，由于基岩版的限制，一旦达到 `10,000` 次函数执行限制，它将停止。

例如，错排100个目标的位置仅需4-6次迭代，初始化时执行7条命令，每次迭代执行9条命令。总计约60条命令，远低于函数限制。

<br>

迭代次数与元素数量成正比增加。

以下是1到10个元素的可能错排数量供参考：

| 元素数量 (N) | 可能的错排数量 (D(N)) |
|--------------|-------------------------|
| 1            | 0                       |
| 2            | 1                       |
| 3            | 2                       |
| 4            | 9                       |
| 5            | 44                      |
| 6            | 265                     |
| 7            | 1,854                   |
| 8            | 14,833                  |
| 9            | 133,496                 |
| 10           | 1,334,961               |

随着元素数量的增加，错排的可能性迅速增加。

## 此方法涉及的步骤

1. 将每个目标重新定位到一个随机位置（不是其原始位置）。
2. 如果多个目标被重新定位到同一位置，则将其分配给其中一个，并对剩余目标重复该过程。
3. 如果最终目标只剩下一个可用位置是其原始位置，则将当前位于该位置的目标重新定位到其原始位置，从而将现在释放的位置分配给最终目标。

**示例可视化：**

![五名玩家位置错排]( /assets/images/commands/rearrange-positions/MPDVisualRep.gif)

## 函数

需要一个ID系统来索引所有目标的位置，从1到N，以便我们跟踪每个目标的原始位置。我们将在 `tick.json` 中运行此文件以自动分配ID。

```yaml title="BP/functions/scoreboards/player/id.mcfunction"
## 注册新玩家到 ID 目标
scoreboard players add @a id 0

## 创建新 ID
execute if entity @a [scores={id=0}] run scoreboard players add Total id 1

## 分配新 ID
scoreboard players operation @r [scores={id=0}] id = Total id
```

<br>

这是你每次需要错排所有目标位置时运行的函数（仅需运行一次）：

- `/function events/player/derange_position/initiate`

```yaml title="BP/functions/events/player/derange_position/initiate.mcfunction"
## 召唤位置标记
execute at @a run summon armor_stand "位置标记" ~~~

## 保存原始位置以忽略
execute as @a at @s run scoreboard players operation @e [type=armor_stand, name="位置标记", r=0.01, c=1] id = @s id

## 启动位置错排过程
function events/player/derange_position/process

## 如果最后一个玩家有有效位置可用，则最后一次运行过程
execute if score NonAllocatedPlayers count matches 1 unless score @a [tag=!posAllocated, c=1] id = @e [type=armor_stand, name="位置标记", c=1] id run function events/player/derange_position/process

## 如果最后一个玩家没有有效位置可用，则解决碰撞
### 将分配的玩家重新定位到其碰撞玩家的原始位置，以释放其位置供碰撞玩家使用
execute as @a [tag=!posAllocated] at @s run tp @r [tag=posAllocated, r=0.01] @e [type=armor_stand, name="位置标记", c=1]
### 移除碰撞玩家的位置标记和标签
kill @e [type=armor_stand, name="位置标记"]
tag @a remove posAllocated
```

如果只剩下一个目标没有可用位置，除了其原始位置，最后三条命令将解决碰撞。我们称之为碰撞，因为当这种情况发生时，目标将位于另一个目标的分配位置上。

<br>

实际的随机错排过程将由以下函数执行：

```yaml title="BP/functions/events/player/derange_position/process.mcfunction"
## 移动到不同位置
execute as @a [tag=!posAllocated] at @s run function events/player/derange_position/teleport

## 如果返回到原始位置则再次移动
execute as @a [tag=!posAllocated] at @s if score @s id = @e [type=armor_stand, name="位置标记", r=0.01, c=1] id run function events/player/derange_position/teleport

## 添加标签以忽略已分配位置的玩家
execute as @e [type=armor_stand, name="位置标记"] at @s run tag @a [tag=!posAllocated, r=0.01, c=1] add posAllocated

## 移除已分配位置标记
execute as @a [tag=posAllocated] at @s run kill @e [type=armor_stand, name="位置标记", r=0.01, c=1]


# 实体计数器

## 获取未分配位置的玩家数量
scoreboard players set NonAllocatedPlayers count 0
execute as @a [tag=!posAllocated] run scoreboard players add NonAllocatedPlayers count 1

## 如果有2个或更多玩家未分配位置则循环函数
execute if score NonAllocatedPlayers count matches 2.. run function events/player/derange_position/process
```

<br>

-   ❌️ `tp @s @r [type=armor_stand, name="位置标记", rm=0.01]`

直接使用此命令进行传送到新位置仅在当前维度内有效。因此，我们使用以下三个命令的函数以实现跨维度兼容性：

```yaml title="BP/functions/events/player/derange_position/teleport.mcfunction"
tag @e [type=armor_stand, name="位置标记", r=0.01, c=1] add ignoredPos
tp @s @r [type=armor_stand, name="位置标记", tag=!ignoredPos]
tag @e remove ignoredPos
```

<br>

现在，为了使我们的函数实际工作，我们需要在我们的世界中添加以下目标：

```yaml title="BP/functions/scoreboards/objective/add_all.mcfunction"
scoreboard objectives add id dummy
scoreboard objectives add count dummy
```

<br>

如果你希望在加载世界时自动添加目标，可以创建以下函数文件：

```yaml title="BP/functions/events/world/on_initialise.mcfunction"
## 初始化
### 添加目标
scoreboard objectives add world dummy
### 注册到目标
scoreboard players add Initialised world 0

## 执行的命令
execute if score Initialised world matches 0 run function scoreboards/objective/add_all

## 标记为已初始化
scoreboard players set Initialised world 1
```

## Tick JSON

最后，创建你的 `tick.json` 文件：

```json title="BP/functions/tick.json"
{
  "values": [
    "events/world/on_initialise",
    "scoreboards/player/id"
  ]
}
```

## 文件夹结构

<FolderView
	:paths="[
    'BP',
    'BP/functions',
    'BP/manifest.json',
    'BP/pack_icon.png',
    'BP/functions/scoreboards',
    'BP/functions/scoreboards/player',
    'BP/functions/scoreboards/player/id.mcfunction',
    'BP/functions/scoreboards/objective',
    'BP/functions/scoreboards/objective/add_all.mcfunction',
    'BP/functions/events',
    'BP/functions/events/world',
    'BP/functions/events/world/on_initialise.mcfunction',
    'BP/functions/events/player',
    'BP/functions/events/player/derange_position',
    'BP/functions/events/player/derange_position/initiate.mcfunction',
    'BP/functions/events/player/derange_position/process.mcfunction',
    'BP/functions/events/player/derange_position/teleport.mcfunction',
    'BP/functions/tick.json'
]"
></FolderView>

## 下载功能包

为方便起见，你可以在此处下载功能包的 `.mcpack` 文件：

<Card image="../assets/images/commands/BClogo.png" title="下载" link="https://github.com/BedrockCommands/developer-packs/releases/download/mpd/Multiplayer_Position_Derangement.FP.mcpack">

</Card>

只需在你的世界中激活该包，并在多人模式下运行以下命令（每次需要时）：

```yaml
/function events/player/derange_position/initiate
```