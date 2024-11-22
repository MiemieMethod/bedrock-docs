---
title: Minecraft Beta - 1.16.100.50 (Xbox One/Windows 10/Android)
date: 2020-07-30T15:47:42Z
updated: 2020-07-30T17:19:54Z
categories: Beta和预览信息及更新日志
tags:
  - beta
  - beta_changelog
link: https://feedback.minecraft.net/hc/en-us/articles/360047105331-Minecraft-Beta-1-16-100-50-Xbox-One-Windows-10-Android
---

**在参与Minecraft Beta之前，请阅读以下内容：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

**成就屏幕**

- 新的成就屏幕设计，并添加了新的成就详情屏幕（在逐步推出后可用）。我们希望您在[这篇帖子](https://aka.ms/mcAchievementBeta)中分享您的反馈！

**常规**

- 自定义名称现在可以修改Boss的条形图（[MCPE-43473](https://bugs.mojang.com/browse/MCPE-43473)）
- 修复了游戏未遵循简体和繁体中文系统语言设置的漏洞
- 任天堂Switch现在可以再次将世界上传到Realm（[REALMS-474](https://bugs.mojang.com/browse/REALMS-474)）
  - 注意：此修复仍处于测试版中，因此尚未在Realm或非测试版平台上可用，但我们想提前告知您此修复正在进行中！
- 如果玩家在重新加入多人游戏会话后打开他们站立的潜影盒，游戏将不再崩溃
- 修复了一些墙在加载世界时未正确连接的问题
- 钓鱼竿现在在靠近生物时将正确投放（[MCPE-65249](https://bugs.mojang.com/browse/MCPE-65249)）
- 修复了块高亮/选择框延伸到块上方的问题
- 修复了损坏竹子时缺失动画的问题
- 在设置屏幕（个人资料部分）中添加了Noto Sans字体许可证按钮和弹出对话框

**图形**

- 修复了在City Living世界中玻璃块的图形问题，该问题影响了一些Windows 10设备
- 修复了在某些设备上天空盒背景图形未正确渲染的问题

**技术变更**

**活动对象**

- “minecraft:behavior.controlled_by_player”目标现在是数据驱动的
- 物理组件的has_gravity现在用于决定生物是否应应用水的重力，如果生物没有导航组件
- 末影水晶现在无法被推动
- 鱿鱼的渲染现在是数据驱动的
- 矿车现在是数据驱动的。将可骑乘的矿车、带箱子的矿车、带漏斗的矿车、带命令方块的矿车和带TNT的矿车转换为数据驱动

**显示名称组件**

- 物品现在可以用本地化的“值”覆盖其显示名称。如果未提供值，组件将保持其默认名称。如果提供的值不在本地化文件中，显示名称将为值字符串

**物品解析**

- **示例 1**
  - **any_tag功能已添加到多个活动对象组件。除了以JSON中的物品名称表示物品外，它们现在还可以表示为一组标签**
  - "item": {"any_tag": "food"}
  - "item": {"any_tag": \["food", "wood"\]}
  - "bribe_items": \["emerald", {"any_tag": "stone"}\]
  - minecraft:ageable的feed_items现在可以使用any_tag功能
  - minecraft:breedable的breed_items现在可以使用any_tag功能
  - minecraft:bribeable的bribe_items现在可以使用any_tag功能
  - minecraft:giveable的items现在可以使用any_tag功能
  - minecraft:healable的items现在可以使用any_tag功能
  - minecraft:tamemount的feed_items和auto_reject_items现在可以使用any_tag功能
  - minecraft:equippable的accepted_items现在可以使用any_tag功能
- **示例 2**
  - **在原版本地化中查找“apple”键以用作显示文本，由于未找到值，因此显示名称将仅为“apple”**
  - "minecraft:display_name": {  
    "value": "apple"  
    }
- **示例 3**
  - **在原版本地化中查找“item.apple.name”键以用作显示文本，找到的值为“Apple”。注意不需要“minecraft:”命名空间。**
  - "minecraft:display_name": {  
    "value": "item.apple.name"  
    }
- **示例 4**
  - **查找资源包中提供的自定义字符串，如果未找到，显示名称将为“item.my_namespace:My_Awesome_Item.name”。**
  - "minecraft:display_name": {  
    "value": "item.my_namespace:My_Awesome_Item.name"  
    }