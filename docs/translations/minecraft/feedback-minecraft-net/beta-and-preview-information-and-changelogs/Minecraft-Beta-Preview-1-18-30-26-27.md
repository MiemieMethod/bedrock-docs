---
title: Minecraft Beta & 预览 - 1.18.30.26/27
date: 2022-03-16T15:34:21Z
updated: 2022-03-16T16:52:05Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4847403346957-Minecraft-Beta-Preview-1-18-30-26-27
---

**发布于：** 2022年3月16日

## 关于Minecraft预览和Beta的信息：

- 预览版本：1.18.30.27 \| Beta版本：1.18.30.26
- 虽然预览和Beta的版本号不同，但游戏内容没有差异
- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![copper_horn_16x9.jpg](https://feedback.minecraft.net/hc/article_attachments/4847375150605/copper_horn_16x9.jpg)

以下是本周Beta的新内容！如往常一样，请在 [bugs.mojang.com](http://bugs.mojang.com/) 搜索并报告您可能发现的任何漏洞。

## **已知问题**

- 在1.18之前未探索的旧世界中，y=0以下的区域可能会出现生成问题。我们建议您备份您的世界，并避免在此Beta/预览版本中打开1.18之前的世界。

# **实验性特性**

## **铜角**

- 添加了铜角物品，通过将三个铜锭以“v”形状与中间的山羊角合成而成
- 可以通过仰望、蹲下和其他方式播放三种不同的声音
- 为从尖叫山羊获得的山羊角合成的铜角添加了特殊声音

## **山羊角**

- 添加了额外的山羊角声音，每只山羊的声音是随机的
- 为尖叫山羊添加了特殊声音
- 当至少有一个角的山羊撞击以下方块时，总是会掉落：石头、浮冰、铁矿石、铜矿石、绿宝石矿石或任何类型的主世界木头原木
- 可以使用3个铜锭以“v”形状与中间的山羊角合成铜角
- 山羊有小概率只生成一个角（小山羊总是会有两个角）

## **掠夺者前哨站**

- 添加了山羊角和铜角作为战利品

# **特性和漏洞修复**

## **游戏玩法**

- 修复了在某些市场世界中饥饿条不会减少的问题 ([MCPE-152533](https://bugs.mojang.com/browse/MCPE-152533))
- 修复了击败掠夺者队长后不应用不祥之兆效果的问题 ([MCPE-152846](https://bugs.mojang.com/browse/MCPE-152846))
- 生物的受伤和死亡声音不再重叠 ([MCPE-152852](https://bugs.mojang.com/browse/MCPE-152852))
- 击退抗性现在可以减弱来自铁傀儡攻击的垂直提升
- 保存结构方块现在可以正确检测到负Y轴的角落结构方块 ([MCPE-151511](https://bugs.mojang.com/browse/MCPE-151511))

### **原版趋同**

- 下界砖、铁/金粒、红/棕色蘑菇方块以及紫颂树/花方块不再可以用作熔炉的燃料 ([MCPE-114216](https://bugs.mojang.com/browse/MCPE-114216))
- 当玩家受到伤害时，摄像机现在会像Java版一样摇晃 ([MCPE-118510](https://bugs.mojang.com/browse/MCPE-118510))

## **生物**

- 修复了某些市场地图中的大型生物可能卡住的问题

## **用户界面**

- 在移动设备上使用新触控控制时，摇杆的大小现在可以在设置屏幕的按钮大小滑块中调整
- 修复了在口袋UI中，物品在自定义UI的方块中可能意外掉落的问题，并调整了这些屏幕的大小，以允许在侧面掉落物品
- 改善了多个UI元素的对比度
- 在新的创建新世界屏幕中启用了行为包选项卡

# **技术更新**

## **组件**

- 修复了击退目标中传递给过滤器评估函数的错误所有者问题

## **常规**

- 将CraftingTableComponent的crafting_tags字段中的元素数量限制为64

## **稳定性和性能**

- 修复了在加载包含1.18.30之前实体的区块时可能发生的崩溃问题

## **GameTest框架（实验性）**

- 添加了事件“leverActivate” - 当拉杆被切换时触发
- 为函数addEffect添加了可选参数showParticles: bool = true