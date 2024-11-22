---
title: Minecraft Beta - 1.18.0.25 (Xbox One/Windows 10/Android)
date: 2021-11-04T14:20:06Z
updated: 2021-11-04T16:17:35Z
categories: 测试版和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4412728960141-Minecraft-Beta-1-18-0-25-Xbox-One-Windows-10-Android
---

**发布于：** 2021年11月4日

**请在参与Minecraft测试版之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft的截图，展示了一艘沉船和一座壮观的山脉](https://feedback.minecraft.net/hc/article_attachments/4412728857357/beta18_5wrd.jpg)

 

又到了Bedrock测试版的时间！一如既往，我们非常感谢您发送到[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)的所有反馈，请在发现任何漏洞时报告至[bugs.mojang.com](http://bugs.mojang.com/)。

 

# **特性与漏洞修复**

## **游戏玩法**

- 加载旧世界将不再导致区块为空（[MCPE-98789](https://bugs.mojang.com/browse/MCPE-98789)）
- 修复了一个可能导致某些音乐曲目在下界无法播放的问题（[MCPE-146266](https://bugs.mojang.com/browse/MCPE-146266)）
- 修复了叶块在被按钮或台阶等部分块包围时不保持透明的问题（[MCPE-139213](https://bugs.mojang.com/browse/MCPE-139213)，[MCPE-53731](https://bugs.mojang.com/browse/MCPE-53731)）
- 修复了叶块下方区块的面剔除问题，修复了透视效果
- 修复了在蹲下时打开物品栏时，盾牌会被锁定在玩家副手槽位的问题（[MCPE-146003](https://bugs.mojang.com/browse/MCPE-146003)）
- 修复了某些市场包在测试版构建中将玩家生成在错误位置的问题
- 修复了可能导致双箱子分裂并变得无法使用的漏洞（[MCPE-146983](https://bugs.mojang.com/browse/MCPE-146983)）

## **世界生成**

- 冻结生物群系不再在更新区块的世界中生成冰柱（[MCPE-125128](https://bugs.mojang.com/browse/MCPE-125128)）
- 海底废墟和沉船的生成频率已降低（[MCPE-143478](https://bugs.mojang.com/browse/MCPE-143478)）
- 杜鹃树不再在水下生成（[MCPE-125919](https://bugs.mojang.com/browse/MCPE-125919)）
- 杜鹃树现在可以在浅水中生成
- 缠根泥土不再在没有杜鹃树的情况下生成（[MCPE-140867](https://bugs.mojang.com/browse/MCPE-140867)）
- 原版趋同：从生物群系生成中移除了深暖水海洋（[MCPE-147051](https://bugs.mojang.com/browse/MCPE-147051)）
- 修复了之前可能在主世界表面生成的滴水石锥柱子的问题（[MCPE-139877](https://bugs.mojang.com/browse/MCPE-139877)）
- 修复了防止小型垂滴叶块被放置在熔岩块内的问题

## **Android**

- 游戏已暂时从API 30降级到API 29。具有现有外部存储的玩家将在启动时迁移到新位置。如果您手动迁移了外部存储，则不会受到影响（[MCPE-144801](https://bugs.mojang.com/browse/MCPE-144801)，[MCPE-144776](https://bugs.mojang.com/browse/MCPE-144776)，[MCPE-144806](https://bugs.mojang.com/browse/MCPE-144806)）
- 由于Google要求的存储更改，具有外部存储的玩家将在启动时迁移到新位置。如果迁移失败，您仍然可以通过关闭结果窗口继续游戏
- 随着外部存储迁移到新位置以准备Google的新API要求，如果您卸载Minecraft，您将丢失数据，除非您勾选保留数据的选项。如果您希望在选择重新安装Minecraft时保留您的世界，建议勾选此选项

## **用户界面**

- 更新了“存储不足”的消息

# **技术更新**

## **Molang**

- 修复了当Molang表达式没有令牌时的内容错误，仅在'min_engine_version'为1.17.40或更高时触发
