---
title: Minecraft Beta与预览 - 1.19.30.23
date: 2022-08-24T14:00:53Z
updated: 2022-08-29T18:20:34Z
categories: Beta与预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/8653419896589-Minecraft-Beta-Preview-1-19-30-23
---

**发布于：** 2022年8月25日

## **关于Minecraft预览和Beta的信息：**

- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版可在Android（Google Play）上使用。要加入或退出Beta，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![一张Minecraft截图，展示了村庄中的村民和悦灵，围栏里有粉色的绵羊。](https://feedback.minecraft.net/hc/article_attachments/8653339179533/beta19U3_4_16x9.jpg)

以下是本周Minecraft预览和Beta中的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，访问[bugs.mojang.com](https://bugs.mojang.com/)并向我们发送[您的反馈](https://aka.ms/MinecraftBetaFeedback)。  
  

# **功能与漏洞修复**

## **原版趋同**

### **旁观模式（实验性）**

- 在旁观模式下，披风不再被渲染（[MCPE-156929](https://bugs.mojang.com/browse/MCPE-156929)）
- 在装有熔岩的炼药锅中的旁观玩家不再显示燃烧动画（[MCPE-160331](https://bugs.mojang.com/browse/MCPE-160331)）

## **方块**

- 旗帜现在在新生成的结构中正确生成（[MCPE-160696](https://bugs.mojang.com/browse/MCPE-160696)）

## **游戏玩法**

- 玩家纹理和用户界面元素在高度拥挤的服务器上长时间游戏后不再变成粉色（[MCPE-105487](https://bugs.mojang.com/browse/MCPE-105487)）
- 修复了玩家在穿着鞘翅时潜入顶部雪中时看到内部的情况

## **图形**

- 修复了命名牌背景略微偏移的漏洞（[MCPE-160254](https://bugs.mojang.com/browse/MCPE-160254)）

## **性能与稳定性**

- 修复了在Xbox上恢复游戏时可能发生的崩溃

## **物品**

- 通过方块拾取不再可能在物品栏中获得老化的树苗
- 物品堆叠在达到指定刻阈值后现在会合并在一起

## **移动控制**

- 解决了新触控控制中，当静止时无法切换冲刺按钮的问题
- 添加了逻辑，当玩家释放屏幕上的摇杆时，自动关闭冲刺按钮

## **生物**

- 将末影人的传送范围减少到32x32x32，以确保其无法通过传送自我毁除（[MCPE-152268](https://bugs.mojang.com/browse/MCPE-152268)）
- 恢复了溺尸生成的更改，它们再次在暖水海洋生物群系中生成，以匹配Java版

## **用户界面**

- 在更新的创建新世界界面中添加了缺失的设置按钮
- 添加了新的断开连接错误信息 - “无法连接，请重启客户端”
- 在命令方块界面中添加了粘贴按钮
- 更新了闪烁标语
- 修复了导致非Unicode字符消息间距不正确的问题

## **常规**

- 修复了删除云同步世界时，当玩家在本地删除世界时不会删除云版本的漏洞
- 教育版切换：NPC名称默认仅在查看时显示

## **音频**

- 修复了PS4在帧率低时音频卡顿的问题（[MCPE-158902](https://bugs.mojang.com/browse/MCPE-158902)）

# **技术更新**

## **常规**

- 修复了与未染色潜影贝相关的崩溃问题

## **命令**

- '/execute at' 和 '/execute as' 命令现在将在正确的相对旋转下执行（[MCPE-156277](https://bugs.mojang.com/browse/MCPE-156277)）
- '/execute at @e run kill @e' 在地面上有物品时不再导致游戏崩溃（[MCPE-161029](https://bugs.mojang.com/browse/MCPE-161029)）
- 当实体被"/ride summon_ride no_ride_change"跳过时，添加聊天输出（[MCPE-129486](https://bugs.mojang.com/browse/MCPE-129486)）

# **实验性技术特性**

## **活动对象属性**

- 当默认或set_property表达式包含副作用（例如Molang变量赋值）时，添加内容错误

## **GameTest框架**

- 内存监控
  - `script-watchdog-memory-warning-` 当合并内存使用量超过给定阈值（以兆字节为单位）时，生成内容日志警告。将此值设置为0将禁用警告。（默认值 = 100）
  - `script-watchdog-memory-limit-` 当合并内存使用量超过给定阈值（以兆字节为单位）时，保存并关闭世界。将此值设置为0将禁用限制。（默认值 = 250）
- 玩家
  - setVelocity现在在调用玩家类型时将抛出异常
- 监控
  - 将慢代码警告阈值从2毫秒提高到6毫秒
- 物品
  - 将`Items`重命名为`ItemTypes`
- ItemTypes
  - 添加`function getAll(): ItemTypeIterator-` 返回所有可用物品类型的迭代器