---
title: Minecraft Beta & Preview - 1.20.10.21
date: 2023-06-01T13:33:37Z
updated: 2023-06-01T14:28:05Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/16314419988493-Minecraft-Beta-Preview-1-20-10-21
---

**发布时间：** 2023年6月1日

**关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请查看 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明。

![一张Minecraft截图，展示了一位村民站在工作台旁边，背景中有一个盔甲架，旁边还有一只骆驼。](https://feedback.minecraft.net/hc/article_attachments/16316195911949)

新的Minecraft预览版和测试版更新来了，更多调整和更改以改善您的游戏体验！请继续向我们发送您的 [反馈](https://aka.ms/MC120Feedback) 和 [漏洞报告](https://bugs.mojang.com/)！以下是更新内容的概述：

![新配方解锁！](https://feedback.minecraft.net/hc/article_attachments/16316164692237)

# **实验性功能**

## **配方解锁**

- 配方解锁——现在在基岩版中实现！
  - 添加了配方解锁作为实验功能
  - 收集材料以解锁相关配方
  - 当您找到新的合成材料时，会有通知告知您
  - 拾取物品将教会您如何合成该物品。对于朋友给您一个您之前未合成过的工具时非常有用
  - 我们希望听到您对这个功能的看法，请通过 [aka.ms/MCRecipeUnlocks](https://aka.ms/MCRecipeUnlocks) 向我们发送反馈

## **潜行与爬行**

- 玩家在用活板门爬入炼药锅或堆肥桶时将不再被卡住 ([MCPE-170836](https://bugs.mojang.com/browse/MCPE-170836))
- 爬行时纸娃娃现在会正确显示
- 修复了滑翔或游泳有时会导致玩家出现不正确的碰撞盒的问题 ([MCPE-170882](https://bugs.mojang.com/browse/MCPE-170882))

# **功能和漏洞修复**

## **游戏玩法**

- 可疑的沙砾和可疑的沙子块现在在地图上正确显示
- 修复了在末地放置末地水晶时可能发生的崩溃问题 ([MCPE-170858](https://bugs.mojang.com/browse/MCPE-170858))
- 盾牌在反击姿势下不再与盔甲架模型重叠
- 修复了在启用客户端区块生成时船只在冰面上消失的问题 ([MCPE-169313](https://bugs.mojang.com/browse/MCPE-169313))

## **图形**

- 水下和迷雾效果现在基于相机位置而不是玩家位置
- 修复了允许视场影响第一人称手部外观和望远镜框架的问题 ([MCPE-170832](https://bugs.mojang.com/browse/MCPE-170832))
- 精美树叶设置现在立即应用，并且不再导致透视效果 ([MCPE-123608](https://bugs.mojang.com/browse/MCPE-123608))

## **生物**

- 生物在夜间的消失率恢复正常 ([MCPE-170208](https://bugs.mojang.com/browse/MCPE-170208))
- 骆驼在静止时受到伤害时现在会播放行走动画 ([MCPE-166566](https://bugs.mojang.com/browse/MCPE-166566))
- 嗅探兽现在无法在空中挖掘种子

## **用户界面**

- 重新排序了游戏手柄的提示框，以便按钮与控制器的同一侧对齐

## **原版趋同**

- 更新竹筏配方，不再将锹作为成分 ([MCPE-170896](https://bugs.mojang.com/browse/MCPE-170896))

# **技术更新**

## **一般**

- 将*"properties"*转换为*"states"*以用于自定义区块
- 修复了在运行*"go_and_give_items_to_noteblock"*目标时可能发生的崩溃
- 修复了在尝试更改生物的缩放时可能发生的崩溃问题 ([MCPE-170645](https://bugs.mojang.com/browse/MCPE-170645))

## **专用服务器**

- **Linux用户注意：** Ubuntu 18.04 LTS（Bionic Beaver）将在2023年结束标准支持。因此，Linux Minecraft专用服务器将在以后的R20更新中将其最低目标Ubuntu版本提高到20.04 LTS（Focal Fossa）（确切发布日期待定）。使用Ubuntu的Minecraft服务器运营商被鼓励尽快更新其部署到20.04 LTS，以便为这一过渡做好准备。

## **物品**

- 带有*"minecraft:block_placer"*组件的物品现在将以正确的方向放置区块
- 在json格式1.20.10及更高版本中，将*"minecraft:max_stack_size"*物品组件从实验性中发布
- 带有*"minecraft:block_placer"*的自定义物品将不再在错误的位置放置某些区块
- 在json格式1.20.10及更高版本中，将*"minecraft:block_placer"*物品组件从实验性中发布
- 在json格式1.20.10及更高版本中，将*"minecraft:record"*物品组件从实验性中发布

# **实验性技术功能**

## **API**

- 系统
  - 将*events*替换为*system.beforeEvents*和*system.afterEvents*。
  - 将事件*beforeWatchdogTerminate*重命名为*watchdogTerminate*并移至*beforeEvents*
  - 将*scriptEventReceive*移至*afterEvents*
- MessageReceiveAfterEvent
  - 移除属性*sourceType*
- ScriptEventSource
  - 将枚举*MessageSourceType*替换为新的枚举*ScriptEventSource*
- ScriptEventCommandMessageAfterEvent
  - 将属性*sourceType*从*MessageSourceType*更改为*ScriptEventSource*
  - 最大消息长度从256增加到2048个字符

## **相机**

- 限制自由相机JSON，使相机俯仰角不超过正负90度
- 修复了/*camerashake*命令，使相机晃动而不影响玩家
- 实验性minecraft:free相机的渲染不再受玩家状态（如夜视）的影响