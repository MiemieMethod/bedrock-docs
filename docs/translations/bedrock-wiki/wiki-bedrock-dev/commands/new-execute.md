---
title: 执行
category: 命令
tags:
    - 简单
mentions:
    - JaylyDev
    - Sprunkles137
    - Hatchibombotar
    - TheItsNameless
    - SmokeyStack
description: /execute 命令的解释。
---

## 介绍

随着1.19.50版本的发布，`/execute` 命令进行了语法重构。虽然新的语法更冗长且书写起来更复杂，但它提供了对命令上下文组件的更精细控制，并为命令添加了条件支持，取代了像 `/testfor`、`/testforblock` 和 `/testforblocks` 这样的命令。

在深入了解语法及其书写方式之前，我们需要理解旧版 `/execute` 命令的工作原理，以及发生了什么变化和原因。这将使解释语法中的概念变得更加容易。

## 理解执行上下文

对于命令初学者和熟悉旧版 `/execute` 行为的用户，复习命令的 **执行上下文** 概念可能是个好主意。

简而言之，这些是影响命令运行方式的参数。命令将以谁的身份执行（即其执行者）、命令将在何处运行以及在哪个维度运行，以及应用于命令的旋转，都是可以更改的参数。

每个命令都有这个上下文，且上下文会根据命令的运行方式而变化。从命令方块触发的命令没有执行者，位置设置为该命令方块；从聊天中运行的命令将执行者定义为玩家，并在玩家的位置运行。

## 执行及其变化原因

`/execute` 命令代表一个或多个实体执行命令。旧语法如下：

```
/execute <目标> <位置> <命令>
/execute <目标> <位置> detect <位置> <方块> <数据值> <命令>
```

你指定一个目标作为执行者，然后命令的上下文将更改为以该目标身份执行，并在该目标位置运行。任何位置的变化都始终相对于该目标。

虽然这在大多数情况下很有用，但它也强制要求命令的目标和位置始终绑定在一起（除非你手动插入世界坐标替代 `<位置>`）。在制作条件语句时，它也不够灵活，因为你每次都必须以实体身份执行。

在2017年夏季的水域更新开发期间，Minecraft: Java Edition的开发者从社区获得了关于如何改进 `/execute` 命令语法的反馈，基本概念是：`/execute` 接受无限数量的 **子命令**，按你指定的顺序操作命令的某些方面，然后在最后放置一个“运行”子命令来执行命令。

这使得 `/execute` 对命令的控制大大增强，并允许将执行者和命令的位置分开。

## 语法

现在，让我们回顾一下 `/execute` 的语法。它们如下：

### `/execute as`

更改命令的执行者，或目标选择器 `@s` 将选择的对象。

```
/execute as <origin: target> -> execute
```

这不会更改命令的上下文中的位置、旋转或维度。

如果指定了多个目标，则每个目标将各自运行一次命令，`@s` 将依次选择每个实体。

### `/execute at`

更改命令运行的位置，设置命令的上下文位置、旋转和维度为实体。

```
/execute at <origin: target> -> execute
```

这不会更改命令的执行者，因此 `@s` 将保持为最后被目标的实体。

如果指定了多个目标，则每个目标将各自运行一次命令，将位置、旋转和维度上下文设置为每个目标。

### `/execute in`

设置命令应运行的维度。

```
/execute in <dimension: string> -> execute
```

当前接受的值为 `overworld`、`nether` 和 `the_end`。

例如，要在末地作为目标执行，可以运行：

```
/execute in the_end positioned 0 -100 0 as @a [rm=1] run say I'm in the End dimension
```

注意：维度的变化将遵循该维度的比例；从主世界到下界将对位置应用 x0.125 的比例，反之则对位置应用 x8 的比例。

### `/execute positioned`

直接设置命令的位置上下文。

```
/execute positioned <position: x y z> -> execute
```

将命令的位置设置为特定值。[相对和本地坐标](/commands/relative-coordinates) 是基于命令的当前位置。

```
/execute positioned as <origin: target> -> execute
```

将命令的位置设置为目标的位置。这与 `/execute at` 的工作方式相似，但仅设置命令的位置，而不设置其旋转或维度。

如果指定了多个目标，则每个目标将各自运行一次命令，将位置上下文设置为目标的位置。

### `/execute align`

将命令的当前位置与方块网格对齐。

```
/execute align <axes: swizzle> -> execute
```

对齐位置将向下取整。此子命令接受任何不重复的字母组合 "x"、"y" 和 "z"，并将在每个指定的轴上向下取整。

要将目标对齐到方块的中心，可以运行：

```
/execute as <target> at @s align xyz run tp @s ~0.5 ~0.5 ~0.5
```

### `/execute anchored`

将命令的锚点设置为执行者的脚或眼睛。更改锚点将影响本地坐标的起始位置。

```
/execute anchored (eyes|feet) -> execute
```

当以目标执行时，默认锚点为其脚。

当锚点设置为 `eyes` 时，命令的本地位置会根据当前执行者的“眼高”进行偏移。

此偏移应仅适用于本地坐标，但由于一个错误，目前会影响相对坐标：[MCPE-162681](https://bugs.mojang.com/browse/MCPE-162681)。

此外，`anchored` 子命令在同一 `/execute` 命令中只能指令一次。第二个 `anchored` 指令将无效。这是由于另一个错误：[MCPE-165051](https://bugs.mojang.com/browse/MCPE-165051)。

### `/execute rotated`

直接设置命令的旋转上下文。

```
/execute rotated <yaw: value> <pitch: value> -> execute
```

将命令的旋转设置为特定值。相对和本地坐标是基于命令的当前旋转。默认情况下，俯仰和偏航的值均为0，除非之前已更改旋转。

```
/execute rotated as <origin: target> -> execute
```

将命令的旋转设置为目标的旋转。

如果指定了多个目标，则每个目标将各自运行一次命令，将旋转上下文设置为目标的旋转。

### `/execute facing`

将命令的旋转设置为面向某个位置。此旋转是基于命令的当前位置计算的。

```
/execute facing <position: x y z> -> execute
```

设置旋转以面向方块位置。相对和本地坐标是基于命令的当前位置。

```
/execute facing entity <origin: target> (eyes|feet) -> execute
```

设置旋转以面向目标的位置。将锚点设置为 `feet` 将使旋转面向他们当前站立的位置，而将锚点设置为 `eyes` 将使命令朝向该目标的“眼睛位置”（见 [`/execute anchored`](/commands/new-execute#execute-anchored)）。

如果指定了多个目标，则每个目标将各自运行一次命令，将旋转上下文设置为面向该目标。

### `/execute (if|unless)`

根据条件防止运行命令。如果条件为真，则命令将继续，否则将停止。

`/execute unless` 的作用相反，测试条件是否为假以继续。

```
/execute if entity <target: target> -> execute
```

类似于 `/testfor`。如果目标存在，则返回真。

```
/execute if block <position: x y z> <block: string> -> execute
```

类似于 `/testforblock`。如果指定位置的方块存在，则返回真。

可以另外指定数据值或方块状态，否则将忽略方块状态（相当于设置为 `-1`）。

```
/execute if blocks <begin: x y z> <end: x y z> <destination: x y z> (all|masked) -> execute
```

类似于 `/testforblocks`。它构建一个从起始位置到结束位置的体积，如果目标位置的体积与原始体积匹配，则返回真。

参数 `all` 测试所有方块是否匹配，而 `masked` 将忽略空气方块。

```
/execute if score <target: target> <objective: string> matches <range: integer range> -> execute
```

测试指定分数是否为某个值。使用整数范围语法。

```
/execute if score <target: target> <objective: string> (=|<|<=|>|>=) <source: target> <objective: string> -> execute
```

测试指定分数是否与另一个分数进行某种逻辑比较。运算符包括等于（`=`）、大于（`>`）、大于或等于（`>=`）、小于（`<`）和小于或等于（`<=`）。

### `/execute run`

```
/execute run <command: command>
```

使用所有当前应用的上下文修改运行命令。此子命令始终在一个 `/execute` 命令的最后。

然而，此子命令并非总是必需的；以 `if` 或 `unless` 子命令结束的 `/execute` 命令也是有效的，并将返回其执行的测试结果。

## 示例及旧命令的升级

由于子命令可以无限链式调用，因此几乎存在无限的 `/execute` 命令参数组合，无法一一列出。相反，这里列出了一些常见的命令示例。

旧版 `/execute` 的功能可以通过 `as <target> at @s` 进行复制。如果你需要相对于实体的位移偏移，添加 `positioned`。如果你想检测方块是否存在，添加 `if block`。以下是一些等效命令：

1. 带偏移的传送。

```yaml
# 旧语法:
/execute @p ~ ~1.62 ~ teleport @s ^ ^ ^3
# 新语法:
/execute as @p at @s positioned ~ ~1.62 ~ run teleport @s ^ ^ ^3
```

2. 链接多个执行。

```yaml
# 旧语法:
/execute @e[type=sheep] ~ ~ ~ execute @e[type=item,r=5] ~ ~ ~ detect ~ ~-1 ~ stone kill @s
# 新语法:
/execute at @e[type=sheep] as @e[type=item,r=5] at @s if block ~ ~-1 ~ stone run kill @s
```

（注意，我们不使用 `as @e[type=sheep] at @s`，因为在此上下文中我们不需要以羊的身份执行；仅需要位置。）

现在是一些在引入新语法之前无法在一个命令中完成或更难执行的示例。

```yaml
# 测试假玩家名称的分数:
/execute if score game_settings var matches 3.. run say [Game] Difficulty set to Hard.

# 比较两个分数是否相等:
/execute as @a if score @s x = @s y run say My X is equal to my Y.

# 测试一个实体而不针对它:
/execute as @a at @s if entity @e[type=armor_stand,r=10] run gamemode survival @s
```

**（推荐）接下来阅读: [执行逻辑门](/commands/logic-gates)**
