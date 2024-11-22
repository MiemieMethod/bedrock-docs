---
title: Minecraft Beta & Preview - 1.19.0.32/33
date: 2022-05-12T15:06:56Z
updated: 2022-05-12T15:55:08Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/6183919308301-Minecraft-Beta-Preview-1-19-0-32-33
---

## Minecraft预览版和测试版信息：

- 测试版：1.19.0.32 \| 预览版：1.19.0.33 \| Xbox预览版：1.19.0.66
- 尽管预览版和测试版的版本号不同，但游戏内容没有差异
- 这些进行中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，展示了新的生物悦灵，位于红树林沼泽附近](https://feedback.minecraft.net/hc/article_attachments/6183833141901/beta19_6_16x9.jpg)

以下是本周测试版的新内容！如往常一样，请在[bugs.mojang.com](http://bugs.mojang.com/)搜索并报告您可能发现的任何漏洞，并向我们发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

  
**Minecraft测试版**

Windows上的Minecraft测试版即将退役！要继续测试新的预发布功能，您需要安装Minecraft预览版。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ) 

# **新特性和漏洞修复**

## **悦灵**

- 目前，悦灵不会与其主人一起传送到下界。这是一个临时更改，直到我们修复悦灵有时会被传送到方块内部并窒息的问题（[MCPE-155678](https://bugs.mojang.com/browse/MCPE-155678)）

## **方块**

- 非生成的幽匿尖啸体现在在激活之间有冷却时间，就像它们生成的对应物一样（[MCPE-153944](https://bugs.mojang.com/browse/MCPE-153944)）
- 幽匿尖啸体和幽匿感测体在使用精准采集时不再掉落经验值（[MCPE-153359](https://bugs.mojang.com/browse/MCPE-153359)，[MCPE-153965](https://bugs.mojang.com/browse/MCPE-153965)）
- 增加了摧毁强化深板岩所需的时间，并使其与使用的工具无关，以更好地匹配Java版（[MCPE-154097](https://bugs.mojang.com/browse/MCPE-154097)）
- 幽匿块不再通过火和灵魂火传播

## **红树林沼泽**

- 红树现在可以在负Y坐标处正常生长（[MCPE-154983](https://bugs.mojang.com/browse/MCPE-154983)）

## **图形**

- 修复了Android上的图形损坏问题（[MCPE-155509](https://bugs.mojang.com/browse/MCPE-155509)）
- 修复了在使用表情超过一次时可能导致严重视觉故障的问题（[MCPE-155049](https://bugs.mojang.com/browse/MCPE-155049)）

## **移动**

- 使用移动预测的活动对象将再次平滑传送

## **稳定性和性能**

- 改善了某些Android设备上的游戏性能（[MCPE-142934](https://bugs.mojang.com/browse/MCPE-142934)）
- 修复了尝试渲染依赖于生物群系数据的方块时可能发生的崩溃

## **用户界面**

- 按住Shift键点击物品将再次将相同类型的物品合并为一堆（[MCPE-153992](https://bugs.mojang.com/browse/MCPE-153992)）
- 添加了更改通知持续时间的设置

# **技术更新**

## **方块**

- 修复了在克隆另一个命令方块到自身时命令方块的行为，克隆的命令方块在切换红石信号之前不会执行其命令  

## **游戏测试框架（实验性）**

- 专用服务器已更新，以允许服务器明确列出它们希望在运行脚本时加载的脚本模块。默认配置文件位于/config/default/permissions.json。没有这个新文件，所有脚本模块默认情况下都是禁用的