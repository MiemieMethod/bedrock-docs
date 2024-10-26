---
title: MBE - Max的区块实体
category: 技巧
mention:
    - BedrockCommands
    - zheaEvyline
description: 使用命令创建Max的区块实体系统。
---

## 介绍

[来源于Bedrock Commands社区Discord](https://discord.gg/SYstTYx5G5)

此方法由Reddit用户 [u/Maxed_Out10](https://www.reddit.com/user/Maxed_Out10/) 开发，允许您使用盔甲架和一些顺序的 `/playanimation` 命令创建几乎完美的Minecraft区块实体复制品。

为了保留创作者的版权，社区将此方法称为“Max的区块实体”，简称MBE。

### 注意事项

1. 此方法每个区块实体使用1个盔甲架。因此，过多的盔甲架（如任何实体）可能会导致服务器延迟。
2. 玩家仍然可以穿过它们并与之互动（如果没有限制）。
3. 虽然区块实体可能在一个位置渲染，但它的实际碰撞盒会有轻微的偏移。

## 视频演示

<YouTubeEmbed id="kb8rz9ItE_M" />

## 设置

_在聊天中输入：_

1. `/summon armor_stand ~~~ 81 ~ default "Grumm"`
    - 我们将Y（水平）旋转设置为 `81` 以与正常的Minecraft区块网格对齐。
    - 必须将其命名为'Grumm'以避免反转的区块纹理。

:::tip

-   蹲下并右键点击（在mcpe中：长按）盔甲架6次，使其处于“娱乐”姿势。
-   这样做可以省去下面系统中第一个命令的需要。
-   **仅在您希望减少系统中的一个命令时使用此方法。**

:::

2. 最后，将所需的区块物品放入盔甲架的主手中。

:::tip

-   `/replaceitem entity @e [name=Grumm] slot.weapon.offhand 0 <itemID>`
    -   使用此命令将所需的区块物品放入盔甲架的副手中，以防止玩家拿走该物品，而不是手动放入主手中。

:::

## 系统

<CodeHeader>BP/functions/mbe/render.mcfunction</CodeHeader>

```yaml
## 对齐手臂
playanimation @e [type=armor_stand, name=Grumm] animation.armor_stand.entertain_pose null 0 "0" wiki:align.arms

## 微型区块大小
playanimation @e [type=armor_stand, name=Grumm] animation.player.move.arms.zombie null 0 "0" wiki:size.mini_block

## 完整区块（可选）
### 大小
playanimation @e [type=armor_stand, name=Grumm] animation.ghast.scale null 0 "0" wiki:size.full_block
### 对齐
playanimation @e [type=armor_stand, name=Grumm] animation.fireworks_rocket.move null 0 "0" wiki:align.full_block

## 冻结盔甲架
execute as @e [type=armor_stand, name=Grumm] at @s run tp ~~~

## 隐藏盔甲架身体
effect @e [type=armor_stand, name=Grumm] invisibility 999999 1 true
```

![commandBlockChain6](/assets/images/commands/commandBlockChain/6.png)

### 每个命令的目的

1. 自动将盔甲架姿势设置为“娱乐”，以对齐手臂。如果您希望手动设置，请跳过此命令。
2. **必需命令**。增加大小以呈现为微型区块。
3. _可选命令。_ 增加大小以呈现为完整区块。
4. _可选命令。_ 正确对齐完整区块大小的MBE。
    - 如果您不需要完整区块大小的MBE，请跳过3和4。
5. 锁定盔甲架位置，以防止在下面的区块被移除时掉落。
6. 隐藏盔甲架身体。

注意：提供控制器名称允许我们堆叠动画而不覆盖之前的动画。例如：

-   `wiki:align.full_block`（其中`wiki`是命名空间）。

使用上述相同的控制器名称并不是必需的，但可以帮助避免与其他playanimation命令的冲突。

## 旋转与对齐

> 注意：这些旋转命令（当物品放置在主手中时）需要通过命令方块触发一次。

<Spoiler title="完整区块">

<CodeHeader></CodeHeader>

```yaml
# 面朝北
/tp @e [type=armor_stand, name=Grumm, c=1] ~-1.1245 ~0.2260 ~-0.097 81

# 面朝南
/tp @e [type=armor_stand, name=Grumm, c=1] ~1.1245 ~0.2260 ~0.097 260

# 面朝东
/tp @e [type=armor_stand, name=Grumm, c=1] ~0.097 ~0.2260 ~-1.1245 171

# 面朝西
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.097 ~0.2260 ~1.1245 350
```

</Spoiler>

<Spoiler title="微型区块">

<CodeHeader></CodeHeader>

```yaml
# 面朝北
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.417~-0.5 ~-0.035 81

# 面朝南
/tp @e [type=armor_stand, name=Grumm, c=1] ~0.417 ~-0.5 ~0.035 260

# 面朝东
/tp @e [type=armor_stand, name=Grumm, c=1] ~0.035 ~-0.5 ~-0.417 171

# 面朝西
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.035 ~-0.5 ~0.417 350
```

</Spoiler>

<Spoiler title="楼梯">

<CodeHeader></CodeHeader>

```yaml
# 面朝北
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.097 ~0.2325 ~1.1245 350

# 面朝南
/tp @e [type=armor_stand, name=Grumm, c=1] ~0.097 ~0.2325 ~-1.1245 171

# 面朝东
/tp @e [type=armor_stand, name=Grumm, c=1] ~-1.1245 ~0.2325 ~-0.097 81

# 面朝西
/tp @e [type=armor_stand, name=Grumm, c=1] ~1.1245 ~0.2325 ~0.097 260
```

</Spoiler>

<Spoiler title="底部半砖">

<CodeHeader></CodeHeader>

```yaml
# 面朝北
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.097 ~0.2325 ~1.1245 350

# 面朝南
/tp @e [type=armor_stand, name=Grumm, c=1] ~0.097 ~0.2325 ~-1.1245 171

# 面朝东
/tp @e [type=armor_stand, name=Grumm, c=1] ~-1.1245 ~0.2325 ~-0.097 81

# 面朝西
/tp @e [type=armor_stand, name=Grumm, c=1] ~1.1245 ~0.2325 ~0.097 260
```

</Spoiler>

<Spoiler title="顶部半砖">

<CodeHeader></CodeHeader>

```yaml
# 面朝北
/tp @e [type=armor_stand, name=Grumm, c=1] ~-1.1245 ~0.484 ~-0.097 81

# 面朝南
/tp @e [type=armor_stand, name=Grumm, c=1] ~1.1245 ~0.484 ~0.097 260

# 面朝东
/ tp @e [type=armor_stand, name=Grumm, c=1] ~0.097 ~0.484 ~-1.1245 171

# 面朝西
/tp @e [type=armor_stand, name=Grumm, c=1] ~-0.097 ~0.484 ~1.1245 350
```

</Spoiler>

## 保存与加载MBE

1. 要保存，请运行：

    - `/execute at @e [type=armor_stand, name=Grumm, c=1] run structure save wiki ~~~ ~~~ true disk false`

2. 要加载，请运行：
    - `/structure load wiki <to: x y z>`

> 注意：结构名称`wiki`可以更改为您喜欢的名称。