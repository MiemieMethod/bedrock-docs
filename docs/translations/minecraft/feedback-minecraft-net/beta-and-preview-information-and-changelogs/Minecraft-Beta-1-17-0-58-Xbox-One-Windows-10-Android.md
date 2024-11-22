---
title: Minecraft Beta - 1.17.0.58 (Xbox One/Windows 10/Android)
date: 2021-05-20T15:04:22Z
updated: 2021-05-20T15:45:47Z
categories: Beta和预览信息及更新日志
tags:
  - beta
  - beta_changelog
link: https://feedback.minecraft.net/hc/en-us/articles/360061124392-Minecraft-Beta-1-17-0-58-Xbox-One-Windows-10-Android
---

**发布于：** 2021年5月20日

**请在参与Minecraft Beta之前阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realms，并且在预览Beta期间无法加入非Beta玩家
- 在Beta中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- Beta构建可能不稳定，并不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

又到了更新《洞穴与山崖》Beta的时刻！请继续在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)的讨论串中留下您的反馈，并在[bugs.mojang.com](https://bugs.mojang.com/)搜索和报告您可能遇到的任何新漏洞。

 

![crystal_16x9.jpg](https://feedback.minecraft.net/hc/article_attachments/360095995171/crystal_16x9.jpg)

 

## **特性与漏洞修复**

**滴水石**

- 长的钟乳石仅从尖端滴水
- 钟乳石在填充炼药锅时现在稍微更频繁地滴水
- 小型滴水石锥在其放置的方块被方块更新破坏后现在正确被摧毁

**用户界面**

- 调整了设置屏幕的背景颜色

**图形**

- 修复了一个可能在旧世界中出现的漏洞，在矿车中向上看时会显示矿车内部，阻挡玩家视野
- 荧光物品展示框内的地图不再导致附近物品发光

**物品**

- 拾取或破坏荧光物品展示框现在会给予正确的物品（[MCPE-117514](https://bugs.mojang.com/browse/MCPE-117514)）
- 高级拾取块现在会正确保存复制方块的数据（[MCPE-126040](https://bugs.mojang.com/browse/MCPE-126040)）
- 熔炉、烟熏炉和高炉在燃料耗尽时现在会熄灭（[MCPE-127550](https://bugs.mojang.com/browse/MCPE-127550)，[MCPE-127559](https://bugs.mojang.com/browse/MCPE-127559)）
- 修复了一个漏洞，导致地图在创建时以玩家位置为中心（[MCPE-126607](https://bugs.mojang.com/browse/MCPE-126607)）
- 幼美西螈在用热带鱼桶喂食时不再消耗铁桶
- 用于喂食美西螈的铁桶现在可以与其他空铁桶堆叠在一起（[MCPE-127426](https://bugs.mojang.com/browse/MCPE-127426)）

**游戏玩法**

- 修复了传送门上的涟漪效果和创建大量传送门方块时的崩溃（[MCPE-126674](https://bugs.mojang.com/browse/MCPE-126674)，[MCPE-126690](https://bugs.mojang.com/browse/MCPE-126690)）
- 修复了自然生成的岩浆块上的气泡柱（[MCPE-127196](https://bugs.mojang.com/browse/MCPE-127196)）

**命令**

- 函数的位移偏移不再在使用'/execute'命令运行时对函数内的每个命令重新评估。现在仅对整个函数评估一次（[MCPE-124890](https://bugs.mojang.com/browse/MCPE-124890)）

## **技术更新**

**物品**

- 修复了告示牌在放置时不显示保存文本的问题
- “has_equipment”过滤器再次支持数据值

**生物**

- 在“minecraft:ageable”组件中添加了一个新字段“transform_to_item”。如果该字段填入物品名称，当使用任何“feed_items”时，将返回该物品。类似于“minecraft:breedable”组件中的“transform_to_item”