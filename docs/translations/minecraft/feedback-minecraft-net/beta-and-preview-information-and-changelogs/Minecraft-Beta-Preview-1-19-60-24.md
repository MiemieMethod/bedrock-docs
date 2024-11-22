---
title: Minecraft Beta & Preview - 1.19.60.24
date: 2022-12-14T15:58:59Z
updated: 2022-12-15T10:15:07Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/11448661481229-Minecraft-Beta-Preview-1-19-60-24
hash:
  vex-allay: vex--allay
---

**发布于：** 2022年12月14日

**注意：** 本次预览/测试版将是2022年的最后一次，我们将在2023年重新开始发布！

**关于Minecraft预览和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 以获取详细说明

![一张Minecraft的截图，展示了在栅栏区域内的马、一只被牵引的骆驼，以及在船上的恼鬼和悦灵。](https://feedback.minecraft.net/hc/article_attachments/11448528540045)

以下是本周Minecraft预览和测试版的新内容！记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告至 [bugs.mojang.com](http://bugs.mojang.com/)。

在上周的预览中，我们修复了营火的一个漏洞，这引发了一些关于其使用和设计的讨论。首先：感谢您提供的所有反馈！过去几年我们专注于新功能的趋同，并致力于确保新功能在所有平台上对所有玩家的表现基本一致。对于营火这一较早的功能，我们从未打算让其点燃生物和玩家——这一行为在基岩版中是一个漏洞。

我们理解一些巧妙的设计是围绕这个有问题的机制构建的，但经过仔细考虑，我们决定坚持其原始设计意图，类似于火把的工作方式。火把不会伤害与之接触的实体。而营火则会导致玩家受到伤害，仿佛他们站在岩浆块上一样。

我们想向您保证，这一决定是在修复之前与我们的游戏团队讨论过的，我们对此表示感谢！

# **实验性功能**

## **方块**

- 雕纹书架现在在玩家将书籍投放到连接的漏斗或投掷器时会填满 ([MCPE-164023](https://bugs.mojang.com/browse/MCPE-164023))

# **功能和漏洞修复**

## **游戏玩法**

- 史莱姆和岩浆怪不再在高度为2个方块或更低的空间生成 ([MCPE-46540](https://bugs.mojang.com/browse/MCPE-46540))

### **袭击**

- 当拥有不祥之兆的玩家骑乘/滑翔进入村庄时，袭击现在会正确触发 ([MCPE-152774](https://bugs.mojang.com/browse/MCPE-152774))

## **物品**

- 修复了快速攻击生物时物品降解的问题 ([MCPE-157150](https://bugs.mojang.com/browse/MCPE-157150))

### **漏斗**

- 漏斗在尝试吸取多种物品时不再无法收集物品 ([MCPE-38963](https://bugs.mojang.com/browse/MCPE-38963))

## **生物**

### **马**

- 马不再能被放置在顶部有地毯的栅栏上推倒 ([MCPE-164717](https://bugs.mojang.com/browse/MCPE-164717))

### **恼鬼**

- 恼鬼的击中箱现在与其模型垂直居中
- 恼鬼在空手时现在使用单独的充能动画 ([MCPE-164490](https://bugs.mojang.com/browse/MCPE-164490))
- 恼鬼现在可以渲染副手物品

### **恼鬼与悦灵**

- 恼鬼与悦灵现在可以正确坐在船和矿车中 ([MCPE-164441](https://bugs.mojang.com/browse/MCPE-164441))

## **触控**

- 修复了一个导致物品无法在创造模式物品栏和玩家扩展物品栏之间间接移动的漏洞

## **触控控制**

- 修复了在按住左右移动按钮时触控方向盘的前进按钮无法使用的问题

## **用户界面**

- 主菜单上的反馈按钮现在会在重定向到浏览器之前提示玩家一个模态窗口

# **技术更新**

## **命令**

- 移除了将原始文本JSON对象的*with*属性设置为JSON对象数组的意外能力

## **生物**

- "minecraft:variable_max_auto_step"组件现在有一个新属性"controlled_value"
  - 当生物被玩家控制时，此属性将覆盖"base_value"
  - "jump_prevented_value"将优先于其他两个值

# **实验性技术功能**

## **API**

- 添加了方法*getEffects*，返回实体上所有活动效果的数组

## **命令**

- 修复了在启用即将到来的创作者功能实验时，@initiator选择器无法正常工作的漏洞 ([MCPE-164727](https://bugs.mojang.com/browse/MCPE-164727))
- 作为即将到来的命令运行方式潜在变化的预览，新的实验性功能将在即将到来的创作者功能实验中导致所有行为包动画事件在当前刻的结束时运行