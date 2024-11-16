---
title: 方块状态
category: 一般
mentions:
    - BedrockCommands
    - zheaEvyline
    - SmokeyStack
    - ThomasOrs
description: 学习如何在命令中使用方块状态。
---

## 介绍

[来源于 Bedrock Commands Community Discord](https://discord.gg/SYstTYx5G5)

方块状态或方块属性是定义方块外观或行为的附加数据。例如，方块的朝向、颜色、变体、是否通电等。

这在多种命令中使用，例如 `/clone`、`/execute`、`/fill`、`/setblock` 和 `/testforblock`。

在基岩版中，我们使用辅助值（也称为元数据）来定义方块。然而，从 1.19.70 及之后的版本开始，这种方式不再支持，已完全被方块状态所取代。

<CodeHeader></CodeHeader>

```yaml
# 辅助值示例:
/setblock ~ ~ ~ wool 1
# 它的方块状态等效:
/setblock ~ ~ ~ wool ["color"="orange"]
```

- 使用辅助值的任何命令方块将继续正常工作。然而，在更新时需要采用方块状态。
- 同样，任何在行为包/功能包中使用辅助值且 `min_engine_version` 为 1.19.63 或以下的命令也将继续正常工作。然而，一旦 `min_engine_version` 更新至 1.19.70 或以上，必须用方块状态替换。

## 方块状态示例与语法

<CodeHeader>示例</CodeHeader>

```yaml
/setblock ~ ~ ~ wool ["color"="white"]
/setblock ~ ~ ~ wheat ["growth"=0]
/setblock ~ ~ ~ wood ["wood_type"="birch","stripped_bit"=true]
/setblock ~ ~ ~ wool []
```

- 方块状态用方括号 ` [ ] ` 括起来。
- 指定多个方块状态时，用逗号 ` , ` 分隔。
- 字符串用引号 ` " " ` 括起来，例如 `"birch"`、`"spruce"` 等。
- 整数值 `0, 1, 2..` 和布尔值 `true/false` 不应使用引号。
- 留空方括号将默认为 0。
    - 示例：`wool 0` 是白色羊毛。因此，你可以简单地写为 `wool []` 或 `wool`，而不是 `wool ["color"="white"]`。

### 初学者注意事项

- **整数** 是整数值。它们用于定义方块的“范围”值。
    - 示例：红石电力 1 到 15
    - `["redstone_power"=10]`

- **布尔值** 是一个编程术语，指的是 `true/false` 值。你可以将其理解为是非问题。
    - 这个活塞是否通电？ `是/否`
    - 这个按钮是否被按下？ `是/否`
    - 这个原木是否被剥离？ `是/否`
    - 示例：`["stripped_bit"=true]`

- **字符串** 是独特的“文本”输入。你可以将其理解为多项选择问题。
    - 这个羊毛是什么颜色？ `"white"`、`"orange"`、`"brown"` 等。
    - 这个原木是什么木材类型？ `"spruce"`、`"birch"`、`"acacia"` 等。
    - 示例：`["wood_type"="spruce"]`。

## 方块状态列表

当前在基岩版中可用的所有方块状态列表可以在以下网址找到：
https://learn.microsoft.com/en-us/minecraft/creator/reference/content/blockreference/examples/blockstateslist

- 注意：在网站上，方块状态可能以 `camelCase` 列出，但在命令中，仅需以 `snake_case` 输入。
    - 示例：`buttonPressedBit` → `"button_pressed_bit"`。

## 将辅助值转换为方块状态

为了方便你使用，你可以通过 *@SmokeyStack* 提供的 [查找表](https://auxval-to-blockstates.netlify.app/) 获取所有方块 ID、其辅助值和方块状态等效的最新列表。

## 已知问题

指定方块的命令必须留空方块状态字段，或包含 **所有** 相应的方块状态。否则，命令将无法工作。

例如，以下命令将正常工作：
<CodeHeader></CodeHeader>

```yaml
# 测试石按钮（辅助值 0）
/execute if block ~~~ stone_button run say success

# 测试朝西的未按下石按钮（辅助值 1）
/execute if block ~~~ stone_button [“button_pressed_bit”=false,”facing_direction”=1] run say success
```

- 第一个命令之所以有效，是因为方块状态字段留空。
- 第二个命令之所以有效，是因为它包含了石按钮的所有方块状态。包括：
    - `button_pressed_bit`（按钮是否被按下）
    - `facing_direction`（按钮朝上/下/北/南/东/西）
    - 按钮没有其他方块状态。

现在，如果我们想测试一个可能朝 *任意* 方向的按下的石按钮，我们可以使用如下命令：
<CodeHeader></CodeHeader>

```yaml
/execute if block ~~~ stone_button [“button_pressed_bit”=true] run say success
```

然而，这个命令将无法工作，因为缺少 `facing_direction` 方块状态。

总之：尽管方块状态已取代辅助值，但我们仍然无法像使用选择器参数对实体进行测试那样，基于特定条件/过滤器对方块进行测试。

**相关错误报告：**
- [MCPE-133360](https://bugs.mojang.com/browse/MCPE-133360)
- [MCPE-168391](https://bugs.mojang.com/browse/MCPE-168391)