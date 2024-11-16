---
title: AOE云的介绍
category: 教程
tags:
    - 中级
mentions:
    - Sprunkles137
    - MedicalJewel105
description: AOE云的介绍。
---

**区域效果云**，也称为AOE云，内部标识为`minecraft:area_effect_cloud`，是一种具有许多独特属性的特殊实体。通常，这些实体是通过投掷持续药水创建的，但通过结构和一些NBT编辑技巧，我们可以在地图制作中以非常强大的方式操控它们。

## 概述

区域效果云具有几个我们可以利用的特殊功能：

-   作为[虚拟实体](../entities/dummy-entities.md)，它们性能高，几乎不影响帧率，并且完全静态，与世界没有碰撞。这使得它们非常适合玩家周围或需要精确定位的情况。
-   它不会向客户端发送更新。一旦生成，它在视觉上会看起来被冻结，直到消失。然而，它仍然可以通过命令进行移动。
-   它可以以高度可配置的方式应用任何药水效果。持续时间可以精确到每个刻，并且可以设置效果是否为环境效果、是否在屏幕上显示、是否发出粒子等。
-   具有运行时标识符`minecraft:area_effect_cloud`的实体继承这些相同的属性。

## 方法1：投射物组件

投射物组件支持在命中时生成区域效果云。Minecraft使用此功能从持续药水中生成AOE云。

[投射物文档](../entities/projectiles.md#spawn-aoe-cloud)

## 方法2：NBT编辑

生成这些区域效果云的另一种方法是通过结构文件。这使我们能够更精细地控制云可以拥有的药水效果。因此，我们的首要任务是获取编辑这些结构的工具。

### NBT编辑器

推荐使用以下NBT编辑器：

-   [NBT Studio](https://github.com/tryashtar/nbt-studio)（tryashtar开发的独立程序）
-   [NBT Viewer](https://marketplace.visualstudio.com/items?itemName=Misodee.vscode-nbt)（Misode开发的Visual Studio Code扩展）

### 结构文件

为了方便，本文包含一个预制的结构文件，你可以下载并使用。里面有一个存在时间最长的AOE云。

<Button link="../assets/packs/entities/aec/aec.mcstructure" download>
    下载MCSTRUCTURE
</Button>

请参考本文以编辑结构文件：[.mcstructure](../nbt/mcstructure.md)

### NBT格式

| 标签                  | 类型    | 描述                                                   |
| -------------------- | ------- | ----------------------------------------------------- |
| Duration             | 整数    | 云存在的时间（以刻为单位）。                          |
| DurationOnUse        | 整数    | 应用效果时持续时间的变化量。                          |
| InitialRadius        | 浮点数  | 创建时云的半径大小。                                  |
| ParticleColor        | 整数    | 粒子效果的颜色（十进制）。                            |
| ParticleId           | 整数    | 此云发出的粒子效果。0表示不发出粒子。                |
| PotionId             | 短整数  | 创建时此云的药水效果ID。无效。                        |
| RadiusChangeOnPickup | 浮点数  | 未知。                                                |
| RadiusOnUse          | 浮点数  | 应用效果时半径的变化量。                              |
| RadiusPerTick        | 浮点数  | 每个刻半径变化的量。                                  |
| ReapplicationDelay   | 整数    | 应用效果的间隔（以刻为单位）。                        |
| mobEffects           | 列表    | 描述应应用哪些药水效果。                              |

以下是`mobEffects`标签的参数。

| 标签                             | 类型    | 描述                                                             |
| -------------------------------- | ------- | --------------------------------------------------------------- |
| Ambient                         | 字节    | 定义此效果的粒子是否应为半透明。                               |
| Amplifier                       | 字节    | 此药水效果的强度。                                             |
| DisplayOnScreenTextureAnimation  | 字节    | 未知。                                                          |
| Duration                        | 整数    | 此效果应用的时间（以刻为单位）。                               |
| DurationEasy                    | 整数    | 未知，似乎未使用。                                            |
| DurationNormal                  | 整数    | 未知，似乎未使用。                                            |
| DurationHard                    | 整数    | 未知，似乎未使用。                                            |
| Id                              | 字节    | 此效果的药水效果ID。                                         |
| ShowParticles                   | 字节    | 定义此效果的粒子是否应出现。                                   |