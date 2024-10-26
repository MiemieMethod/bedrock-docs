---
title: 视线检测
category: 技术
mention:
  - BedrockCommands
  - AjaxGb
  - Plagiatus
  - zheaEvyline
description: 此命令技术允许您检测目标何时注视玩家/实体/坐标，并随后运行您所需的命令。
---

## 介绍

[来源于 Bedrock Commands 社区 Discord](https://discord.gg/SYstTYx5G5)

**致谢:** *@AjaxGb*

此命令技术允许您检测目标何时注视玩家/实体/坐标，并随后运行您所需的命令。

## 命令

<CodeHeader>BP/functions/states/player/is_looking_at.mcfunction</CodeHeader>

```yaml
execute as <target> at @s anchored eyes facing <entity | coordinate> positioned ^^^1 positioned ~~-1.62~ rotated as @s positioned ^^^-1 if entity @s [r=0.2] run <command>
```
![一个重复的命令方块](/assets/images/commands/commandBlockChain/1.png)

**可视化:**

![Alex 注视猪的头部](/assets/images/commands/lookDetectionVisualRep.gif)

> *注意: 这是一个粗略的可视化表示，并非精确测量。*

**命令解析:**

- `as <target>`
  - 设置执行目标。例如：
      - `as @p`（最近的玩家）
      - `as @e [type=zombie]`（所有僵尸）
- `at @s`
  - 将执行位置设置为目标的脚下。
- `anchored eyes`
  - 将执行位置提升到目标的眼睛高度。
- `facing <entity | coordinate>`
  - 设置执行旋转面向某个实体或坐标。例如：
      - `facing 0 0 0` 面向坐标: 0,0,0。
      - `facing entity @e [type=pig, c=1] eyes`（面向最近的猪的眼睛）
      - `facing entity @e [type=cow, r=30] feet`（面向30个区块半径内的牛的眼睛）
      - `facing entity @e [type=zombie] feet`（面向僵尸的脚）
- `positioned ^^^1`
  - 从前一个点，将执行位置向实体/坐标的方向推移1个区块。
- `positioned ~~-1.62~`
  - 将执行位置降低到玩家脚下的y轴位置，即低于眼睛高度1.62个区块。
  - 注意: 由于[MCPE-165051](https://bugs.mojang.com/browse/MCPE-165051)的错误，您不能用`anchored feet`替代此项。
- `rotated as @s`
  - 将执行旋转恢复为目标的旋转。
- `positioned ^^^-1`
  - 从前一个点，将执行位置向目标面向的相反方向推移1个区块。
- `if entity @s [r=0.2]`
  - 检查目标是否在执行位置的0.2个区块半径内。即，检查在前后移动后是否大致回到了目标的脚下位置。
  - 要增加或减少被认为“足够接近”的容忍度，请更改`0.2`的距离参数。
      - 该值需要在`0.2`和`2`之间，因为`2`基本上意味着您可以朝相反方向看，仍然被视为“足够接近”。因此，实际上，您可能希望保持在`1`以下。
  - 要计算确切的视锥角度，请参见下文。

**示例:**

1. 当注视标记为'target'的牛或羊的眼睛时运行`/say`命令：

<CodeHeader>BP/functions/states/player/is_looking_at/target.mcfunction</CodeHeader>

```yaml
execute as @a at @s anchored eyes facing entity @e [type=cow, tag=target] eyes positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s [r=0.2] run say hello cow!
execute as @a at @s anchored eyes facing entity @e [type=sheep, tag=target] eyes positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s [r=0.2] run say hello sheep!
```
![一个重复的命令方块](/assets/images/commands/commandBlockChain/1.png)

2. 当注视位置`(10, 20, 30)`或`(6, 7, 8)`时运行`/say`命令：

<CodeHeader>BP/functions/states/player/is_looking_at/position.mcfunction</CodeHeader>

```yaml
execute as @a at @s anchored eyes facing 10 20 30 positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s [r=0.2] run say hello block!
execute as @a at @s anchored eyes facing 6 7 8 positioned ~~-1.62~ positioned ^^^1 rotated as @s positioned ^^^-1 if entity @s [r=0.2] run say hello block!
```
![一个重复的命令方块](/assets/images/commands/commandBlockChain/1.png)

**替代结构:**

<CodeHeader>BP/functions/states/player/is_looking_at.mcfunction</CodeHeader>

```yaml
execute as <target> at <coordinate | entity> facing entity @s eyes positioned as @s positioned ^^^1 rotated as @s positioned ^^^1 if entity @s[r=0.02] run <command>
```
![一个重复的命令方块](/assets/images/commands/commandBlockChain/1.png)

如果您不需要检测目标注视实体的*眼睛*而是它们的脚或某个坐标，您可以使用此结构，这样就不需要`anchored eyes`指令，因为执行位置是从实体/坐标开始的，而不是目标。

## 计算视角

要根据您的视角近似您想要使用的距离/半径，您可以使用以下公式，其中`α`是您希望此方法在目标的左右触发的角度：
```
r = 2 * sin ( α / 2 )
```

或者，使用反向公式计算某个半径/距离（`r`）值将给您什么视角：
```
α = sin^(-1) (r / 2) * 2
```
> 注意: 根据您的计算器，您需要将弧度转换为度数。

通过上述计算，示例值`r=0.2`大致留下了一个12°的角度，在这个角度内我们可以在任一方向上错过确切目标，仍然被视为“足够接近”。