---
title: Minecraft Beta & 预览 - 1.19.40.21
date: 2022-09-14T14:30:20Z
updated: 2022-09-14T15:47:03Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/9159676401933-Minecraft-Beta-Preview-1-19-40-21
---

**发布于:** 2022年9月14日

## **关于Minecraft预览和Beta的信息：**

- 这些开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一张Minecraft截图，展示了一个箱子船、一只劫掠兽、一名村民和一些悦灵](https://feedback.minecraft.net/hc/article_attachments/9159295764621/R19U4_2_16x9.jpg)

以下是本周Minecraft预览和Beta中的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问 [bugs.mojang.com](https://bugs.mojang.com/)，并随时向我们发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。

我们也非常希望听到您在此调查中的想法和反馈 – 您可以在这里查看：[redsto.ne/Minecraft-Survey](https://redsto.ne/Minecraft-Survey)

# **新特性和漏洞修复**

## **原版趋同**

### **旁观模式（实验性）**

- 旁观模式下玩家的水迷雾不再被移除（[MCPE-161105](https://bugs.mojang.com/browse/MCPE-161105)）

## **游戏玩法**

- 修复了玩家在气泡柱顶部的活板门方块内时，掉落伤害累积的问题（[MCPE-158858](https://bugs.mojang.com/browse/MCPE-158858)）

## **生物**

- 修复了生物的长攻击范围可以穿墙攻击玩家的漏洞（[MCPE-55790](https://bugs.mojang.com/browse/MCPE-55790)）

## **用户界面**

- 修复了在口袋UI中，物品可以在工作台界面物品网格周围的深灰色区域掉落的漏洞
- 修复了在口袋UI中，物品可以在马、骡、驴和羊驼的物品栏中物品网格周围的深灰色区域掉落的漏洞
- 修复了当showdeathmessage游戏规则设置为false时，死亡屏幕消息仍然可见的问题

## **原版趋同**

- 甜浆果现在可以种植在耕地上（[MCPE-99632](https://bugs.mojang.com/browse/MCPE-99632)）
- 气泡柱的强度已更改为与Java版相匹配（[MCPE-158858](https://bugs.mojang.com/browse/MCPE-158858)）

### **方块**

- 泥径和耕地方块的碰撞现在降低了一个纹素（[MCPE-12109](https://bugs.mojang.com/browse/MCPE-12109)）
- 玩家现在会在灵魂沙和泥巴方块中下沉（[MCPE-154973](https://bugs.mojang.com/browse/MCPE-154973)）
- 玩家在泥巴上游泳时，屏幕不会被遮挡（[MCPE-153737](https://bugs.mojang.com/browse/MCPE-153737)）
- 投射物落在泥巴上时不会反复晃动（[MCPE-153744](https://bugs.mojang.com/browse/MCPE-153744)）
- 两栖生物在泥巴方块周围不再遇到路径寻找问题（[MCPE-153961](https://bugs.mojang.com/browse/MCPE-153961)）

### **生物**

- 劫掠兽现在可以被唤魔者尖牙伤害
- 劫掠兽的碰撞箱大小已增加，以与Java版相匹配（[MCPE-142171](https://bugs.mojang.com/browse/MCPE-142171)，[MCPE-45531](https://bugs.mojang.com/browse/MCPE-45531)）
- 劫掠兽的速度已增加，以与Java版相匹配（[MCPE-48145](https://bugs.mojang.com/browse/MCPE-48145)）

## **命令**

- 为/summon命令添加了新的重载，增加了旋转参数
  - 新的重载为/summon \[ spawnPos : x y z\] \[yRot: float\] \[xRot: float\] \[spawnEvent: string\] \[nametag: string\]
  - 之前的重载为'/summon \[ spawnPos : x y z\] \[spawnEvent: string\] \[nametag: string\]'

# **技术更新**

## **稳定性和性能**

- 修复了使用*hasItem*选择器并为物品数据指定负值时可能发生的崩溃（[MCPE-152314](https://bugs.mojang.com/browse/MCPE-152314)）

# **实验性特性**

## **命令**

- 实现了"/execute facing "和"/execute facing entity "命令
- 实现了"/execute align "命令

## **数据驱动方块**

- "minecraft:direction"不再作为数据驱动的blockProperty暴露。当使用"minecraft"命名空间时，方块会抛出内容错误

## **GameTest框架**

- 移除了内置的GameTest行为包

## **一般**

- 在*menu_category*中添加了标志*is_hidden_in_commands*以控制方块是否可以在命令中使用