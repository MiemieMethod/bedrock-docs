---
title: Minecraft Beta & Preview - 1.19.30.22
date: 2022-08-17T15:17:38Z
updated: 2022-08-17T15:54:53Z
categories: Beta和预览信息与更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/8485757633293-Minecraft-Beta-Preview-1-19-30-22
---

**发布于：** 2022年8月17日

## **关于Minecraft预览版和测试版的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，展示了箱船和悦灵](https://feedback.minecraft.net/hc/article_attachments/8485735950989/beta19U3_3_16x9.jpg)

以下是本周Minecraft预览版和测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](https://bugs.mojang.com/)并发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。

**请注意：** Android上的测试版更新将延迟至少24小时，感谢您的耐心等待！

# **原版趋同**

### **旁观模式（实验性）**

- 旁观模式中的玩家不再受到细雪迷雾效果的影响（[MCPE-156683](https://bugs.mojang.com/browse/MCPE-156683)）
- 可惜的是，任何被牵引的动物将不再跟随旁观者（[MCPE-157065](https://bugs.mojang.com/browse/MCPE-157065)）
- 旁观模式中的玩家在疾跑时不再发出粒子（[MCPE-160397](https://bugs.mojang.com/browse/MCPE-160397)）
- 施加状态效果的旁观者不再发出粒子（[MCPE-160398](https://bugs.mojang.com/browse/MCPE-160398)）

### **箱船**

- 修复了一个问题，即被/kill命令摧毁的箱船不会掉落箱子的内容物（[MCPE-160186](https://bugs.mojang.com/browse/MCPE-160186)）

### **物品**

- 吃掉炖菜后，空碗将留在所吃的槽位中（[MCPE-56367](https://bugs.mojang.com/browse/MCPE-56367)）
- 喝药水后，空玻璃瓶将留在您饮用的槽位中，而不是您的第一个空物品栏槽位（[MCPE-26436](https://bugs.mojang.com/browse/MCPE-26436)）

### **生物**

- 溺尸不再在暖水海洋生物群系中生成

## **方块**

- 橡树和红树木栅栏门现在是可燃的（[MCPE-160098](https://bugs.mojang.com/browse/MCPE-160098)）

# **地物和漏洞修复**

## **游戏玩法**

- 禁止火球通过传送门，以防止它们永久卡住的问题（[MCPE-160938](https://bugs.mojang.com/browse/MCPE-160938)）
- 修复了掉落物品在流动水边缘卡住的问题（[MCPE-157167](https://bugs.mojang.com/browse/MCPE-157167)）

## **图形**

- 修复了某些水纹理与含水方块显示错误纹理的问题（[MCPE-156281](https://bugs.mojang.com/browse/MCPE-156281)）
- 末地维度的天空在主世界下雨时进入时不再看起来像静态（[MCPE-148843](https://bugs.mojang.com/browse/MCPE-148843)）

## **物品**

- 修复了一个漏洞，即某些自定义物品（来自创作者功能包）在使用后，在玩家死亡时会被复制（[MCPE-128897](https://bugs.mojang.com/browse/MCPE-128897)）
- 修复了一个回归问题，即未损坏的工具（例如镐）在铁砧上更改名称后，第一次使用时无法正常工作（[MCPE-152637](https://bugs.mojang.com/browse/MCPE-152637)）
- 修复了一个漏洞，即某些需要支撑方块的方块（例如地毯或作物）在放置在非完整方块或空气方块上时未在地图上显示（[MCPE-159713](https://bugs.mojang.com/browse/MCPE-159713)）

## **市场**

- 大多数常见的市场连接问题将在条件改善时自动解决，无需重启Minecraft（[MCPE-155025](https://bugs.mojang.com/browse/MCPE-155025)）

## **生物**

- 悦灵和蜜蜂不再卡在灯笼或其他低悬物体上（[MCPE-155777](https://bugs.mojang.com/browse/MCPE-155777)）

## **音乐**

- 移动应用中现在包含音乐，无需从市场下载

## **性能和稳定性**

- 修复了当炽足兽被幼年炽足兽骑乘时的性能问题（[MCPE-146478](https://bugs.mojang.com/browse/MCPE-146478)）

## **用户界面**

- 合成口袋用户界面中的箭头现在适当地适合，没有任何剪裁问题

## **命令**

- 修复了一个漏洞，即在“/scoreboard players reset”的聊天输出中，玩家名称前面会添加一个“%”（[MCPE-151389](https://bugs.mojang.com/browse/MCPE-151389)）
- 尝试在创造模式中使用“/kill”命令杀死玩家时，现在会显示一条消息，告知玩家无法执行此操作（[MCPE-16732](https://bugs.mojang.com/browse/MCPE-16732)）

# **技术更新**

## **活动对象**

- 玩家肩上的非鹦鹉生物在玩家蹲下时将调整其位置（[MCPE-153996](https://bugs.mojang.com/browse/MCPE-153996)）

## **数据驱动方块组件**

- 允许创作者在常规方块单位立方体的任一侧添加几何体，最多可达0.875单位

## **游戏玩法**

- 珊瑚扇在朝北、西、东和南放置时现在看起来相同（[MCPE-125311](https://bugs.mojang.com/browse/MCPE-125311)）

## **市场**

- 语音合成在启动时不再忽略音量设置

## **Molang**

- 澄清了*equipment_count*的文档，以表明它仅计算装备的盔甲，以及如何查询持有的物品（[MCPE-136134](https://bugs.mojang.com/browse/MCPE-136134)）

# **实验性功能**

## **命令**

- “/execute at”命令现在可以正确从指定的“at”位置执行过滤器（[MCPE-156283](https://bugs.mojang.com/browse/MCPE-156283)）

## **GameTest框架**

- 脚本命令
  - 添加了新的子命令*/script watchdog exportstats* - 导出包含内存使用和对象句柄统计信息的文件

## **触控控制**

- 现在可以在船上目标方块时切换快捷栏槽位（[MCPE-156814](https://bugs.mojang.com/browse/MCPE-156814)）