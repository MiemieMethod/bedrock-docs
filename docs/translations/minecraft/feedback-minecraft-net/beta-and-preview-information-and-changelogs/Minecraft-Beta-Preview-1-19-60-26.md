---
title: Minecraft Beta & Preview - 1.19.60.26
date: 2023-01-11T15:26:25Z
updated: 2023-01-11T17:41:04Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/12150896518669-Minecraft-Beta-Preview-1-19-60-26
---

**发布时间：** 2023年1月11日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![一张Minecraft的截图，展示了末地维度中的末地折跃门。背景中有一座末地城，周围散落着几只末影人。](https://feedback.minecraft.net/hc/article_attachments/12150766312205)

以下是本周Minecraft预览版和测试版的新内容！请记得将您的反馈发送至 [aka.ms/MC120Feedback](https://aka.ms/MC120Feedback)，并将任何漏洞报告给 [bugs.mojang.com](http://bugs.mojang.com/)。

# **实验性功能**

### **悬挂式告示牌**

- 在一个轴对齐的悬挂式告示牌下方放置悬挂式告示牌时，如果玩家没有潜行，将会生成带有双链的悬挂式告示牌

# **功能和漏洞修复**

## **命令**

- 修复了一个导致玩家在睡觉时被传送后无法醒来的漏洞 ([MCPE-162346](https://bugs.mojang.com/browse/MCPE-162346))

## **游戏玩法**

- 修复了“梦中梦”成就无法获得的问题

## **图形**

- Android上的用户界面在键盘弹出时不再闪烁 ([MCPE-142356](https://bugs.mojang.com/browse/MCPE-142356))
- 透明物体（如树苗）的高亮选择不再高亮整个卡片
- 选项中的垂直同步设置已正确配置（非ARM设备） ([MCPE-110006](https://bugs.mojang.com/browse/MCPE-110006))
- 资源包将在创建前导航到另一个屏幕后应用于世界
- 修复了某些资源包在下载后提示用户错误的问题

## **性能和稳定性**

- 修复了在通过末地折跃门滑翔时可能导致崩溃的问题
- 当杀死具有无效条件、函数或战利品表条目的实体时，游戏不再崩溃 ([MCPE-164623](https://bugs.mojang.com/browse/MCPE-164623))

## **原版趋同**

- 拉杆现在与石头按钮产生相同的音效 ([MCPE-163335](https://bugs.mojang.com/browse/MCPE-163335))

## **触控控制**

- 修复了非触控模式下的堆叠拆分功能

## **辅助功能**

- 新的创建新世界界面现在将对文本转语音用户可用。我们很高兴在这里收到您的反馈：<https://aka.ms/cnwnarration>

# **技术更新**

## **图形**

- 修复高炉、高炉和烟熏炉屏幕用户界面文本稍微偏左的问题 ([MCPE-151597](https://bugs.mojang.com/browse/MCPE-151597))

## **用户界面**

- 资源包将在创建前导航到另一个屏幕后应用于世界
- 修复了某些资源包在下载后提示错误的问题

# **实验性技术功能**

## **API**

- RawMessage
  - 将属性的签名从 *(string\[\] \| RawMessage)\[\]?*  更改为 *(string\[\] \| RawMessage)?*  
      
- EntityHealthComponent
  - 修复了死去的实体的生命值可以被修改的漏洞 ([MCPE-130687](https://bugs.mojang.com/browse/MCPE-130687))
- Scoreboard
  - 添加了 *setScore(ScoreboardObjective, ScoreboardIdentity, Number)*
  - 添加了 *getScore(ScoreboardObjective, ScoreboardIdentity)*
- ScoreboardObjective
  - 添加了 *setScore(ScoreboardIdentity, Number)*
  - 添加了 *getScore(ScoreboardIdentity)*
  - 添加了 *removeParticipant(ScoreboardIdentity)*
- ScoreboardIdentity
  - 添加了 *setScore(ScoreboardObjective, Number)*
  - 添加了 *getScore(ScoreboardObjective)*
  - 添加了 *removeFromObjective(ScoreboardObjective)*

## **命令**

- 撤销了“即将到来的创作者功能”实验中动画控制器命令延迟的实验性更改

## **一般**

- 在JSON格式1.19.60及更高版本中发布BlockPlacementFilterComponent，超出实验性切换