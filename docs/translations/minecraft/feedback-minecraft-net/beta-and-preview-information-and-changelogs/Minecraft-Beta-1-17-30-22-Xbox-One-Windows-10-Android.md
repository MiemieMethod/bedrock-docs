---
title: Minecraft Beta - 1.17.30.22 (Xbox One/Windows 10/Android)
date: 2021-08-18T14:08:57Z
updated: 2021-08-18T15:32:50Z
categories: Beta和预览信息及更新日志
tags:
  - beta
  - beta_changelog
link: https://feedback.minecraft.net/hc/en-us/articles/4407359965837-Minecraft-Beta-1-17-30-22-Xbox-One-Windows-10-Android
---

**发布于：** 2021年8月18日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版期间无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![Screen_Shot_08-11-21_at_11.09_AM.JPG](https://feedback.minecraft.net/hc/article_attachments/4407359848461/Screen_Shot_08-11-21_at_11.09_AM.JPG)

又到了Bedrock Beta更新的时刻！请继续在<https://aka.ms/CavesCliffsFeedback>的讨论中向我们反馈您的意见，并在[https://bugs.mojang.com](https://bugs.mojang.com/)搜索并报告您可能遇到的任何新漏洞。

# 实验性特性

## 生物

- 修复了在负世界高度下下马时位置不正确的问题（[MCPE-136622](https://bugs.mojang.com/browse/MCPE-136622)）

# 特性和漏洞修复

## 制图师

- 制图师现在只会给未发现的纪念碑地图（[MCPE-29375](https://bugs.mojang.com/browse/MCPE-29375)）

## 附魔

- 附魔台的附魔概率现在进行了加权（[MCPE-101588](https://bugs.mojang.com/browse/MCPE-101588)）

## 原版趋同

- 修复了未持有屏障方块时屏障方块的击中箱缺失的问题（[MCPE-137646](https://bugs.mojang.com/browse/MCPE-137646)）
- 修复了屏障方块无法阻挡投射物的问题（[MCPE-137646](https://bugs.mojang.com/browse/MCPE-137646)）
- 修复了屏障方块无法阻挡玩家与其后方方块的交互
- 潜影盒在被摧毁时现在会掉落其内容作为物品（[MCPE-129470](https://bugs.mojang.com/browse/MCPE-129470)，[MCPE-87877](https://bugs.mojang.com/browse/MCPE-87877)）
- 弓和三叉戟的持握方式现在更类似于Java版（[MCPE-126717](https://bugs.mojang.com/browse/MCPE-126717)，[MCPE-44418](https://bugs.mojang.com/browse/MCPE-44418)）
- 草和水方块的色调不再稍微随机化
- 被遗弃的村庄现在变得更加稀有，更加接近Java版的设置（[MCPE-71769](https://bugs.mojang.com/browse/MCPE-71769)）

## 图形

- 修复了一个漏洞，该漏洞可能导致三叉戟、盾牌和弩在通过互联网连接的额外玩家使用市场皮肤时渲染不正确（[MCPE-118358](https://bugs.mojang.com/browse/MCPE-118358)）
- 修复了一个漏洞，该漏洞可能导致在使用自定义皮肤时望远镜看起来像是被投掷（[MCPE-127498](https://bugs.mojang.com/browse/MCPE-127498)）
- 通过增加辐照缓存样本大小修复了光线追踪模式下的自发光光传播问题（[MCPE-135157](https://bugs.mojang.com/browse/MCPE-135157)）
- 当抗锯齿增加时，快捷栏不再过于黑暗（[MCPE-54213](https://bugs.mojang.com/browse/MCPE-54213)）
- 十字准星在多人游戏会话中不再闪烁（[MCPE-123918](https://bugs.mojang.com/browse/MCPE-123918)）

## 市场

- 在市场中用新的加载旋转器替换了加载条

## 用户界面

- 修复了快捷栏与经验条错位1像素的问题（[MCPE-46975](https://bugs.mojang.com/browse/MCPE-46975)）
- 使用触摸界面时，按住切石机或织布机的输出槽将快速制作物品（[MCPE-128423](https://bugs.mojang.com/browse/MCPE-128423)）
- 修复了尝试激活缺失依赖的包时出现的不正确弹窗（[MCPE-130978](https://bugs.mojang.com/browse/MCPE-130978)）
- 修复了某些包含大写字母的键的翻译问题

# 技术更新

## 命令

- 行为包中定义的动画和事件现在可以运行需要作弊的命令，而无需玩家启用作弊（例如使用/gamerule命令设置某些规则）

## 药水

- "potion.prefix"和"potion.*.postfix"药水字符串资源已重命名为"potion.*.name"
- 药水名称字符串资源已更改，现在有单独的"闪烁"和"持续"字符串资源
- 旧式的使用"potion.prefix"和"potion.*.postfix"仍然被支持

## 用户界面

- 内容警告消息现在会在语言文件格式无效时通知用户存在问题