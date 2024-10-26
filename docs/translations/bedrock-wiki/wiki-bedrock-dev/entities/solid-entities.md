---
title: 实体碰撞
category: 教程
tags:
    - 中级
mentions:
    - SirLich
    - Joelant05
    - Chikorita-Lover
    - Luthorius
    - MedicalJewel105
    - ThomasOrs
description: 实体碰撞是玩家可以与之碰撞、踩踏或以其他方式进行物理交互而不会穿透的实体。
---

实体碰撞是玩家可以与之碰撞、踩踏或以其他方式进行物理交互而不会穿透的实体。这类实体有许多用途，例如模拟方块。

本页将讨论一些创建实体碰撞的方法。

并非所有技术都适用于所有场景。请进行实验，找出最适合您的方法。

## 运行时标识符

[运行时标识符](/entities/runtime-identifier)可用于实现实体碰撞，但目前仅有两个，每个都有特定形状和自身的副作用。碰撞形状无法更改或缩放。

### 船

<CodeHeader>BP/entities/entity_name.json</CodeHeader>

```json
{
  "format_version": "1.16.0",
  "minecraft:entity": {
    "description": {
      "identifier": "wiki:solid_entity",
      "runtime_identifier": "minecraft:boat"
       . . .
    }
  }
}
```

-   船形实体碰撞
-   某些其他类似船的效果

### 末影箱

<CodeHeader>BP/entities/entity_name.json</CodeHeader>

```json
{
  "format_version": "1.16.0",
  "minecraft:entity": {
    "description": {
      "identifier": "wiki:solid_entity",
      "runtime_identifier": "minecraft:shulker"
       . . .
    }
  }
}
```

-   1x1方块大小的实体碰撞。
-   固定在方块网格上。
-   当支撑方块被移除时随机传送。

## minecraft:is_stackable

将 `minecraft:is_stackable` 添加到您希望被视为实体碰撞的实体中。
**注意：** 如果希望该实体对玩家是实体碰撞，则需要编辑 `player.json`。

`"minecraft:is_stackable": {}`

您还需要添加 `minecraft:push_through` 并将其 `value` 参数设置为 1。

`"minecraft:push_through": 1`

（这两个都应放在 `components` 中）

## 使用方块伪装

在某些场景中，使用 `/setblock` 或 `/fill` 放置障碍方块，可能更为合适，无论是静态还是动态。需要有放置障碍物和移除障碍物的方式。

`/fill ~ ~ ~ ~ ~1 ~ barrier 0 replace air`
在 1x1x2 区域内放置障碍物。

`/fill ~1 ~1 ~1 ~-1 ~-1 ~-1 air 0 replace barrier`
在 3x3x3 区域内移除障碍物。

这些 [命令](/animation-controllers/entity-commands) 必须以恒定的速率触发，以确保一致性。它们可以通过实体组件或动画控制器触发。

## 命令方法

此方法由 Reddit 用户 [u/Maxed_Out10](https://www.reddit.com/user/Maxed_Out10/) 开发，允许您使用盔甲架和一些顺序的 `/playanimation` 命令创建几乎完美的 Minecraft 方块实体复制。

<Button link="/commands/block-entities">方块实体</Button>