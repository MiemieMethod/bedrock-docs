---
title: Minecraft Beta 和预览 - 1.18.30.20/21
date: 2022-03-03T14:10:27Z
updated: 2022-03-03T18:44:33Z
categories: Beta 和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4577469770381-Minecraft-Beta-Preview-1-18-30-20-21
---

**发布时间：** 2022年3月3日

## 关于Minecraft预览和Beta的信息：

- 预览版本：1.18.30.21 \| Beta版本：1.18.30.20
- 尽管预览和Beta的版本号不同，但游戏内容没有差异
- 这些正在开发中的版本可能不稳定，可能无法代表最终版本的质量
- Minecraft预览可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- Beta版本可在Xbox、Windows 10/11和Android（Google Play）上使用。要加入或退出Beta，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![Minecraft村庄场景与盔甲架](https://feedback.minecraft.net/hc/article_attachments/4577434378125/beta18U3_1_16x9_resized.jpg)

任何搬家都需要大量准备。你需要确保有足够的空间放置想要搬入的家具，为新物品腾出空间，并确保光线始终处于最佳状态。幸运的是，这次搬家进行得相当顺利。我仍然可以快速移动，更重要的是，可以大声移动，因为我们在这个阶段只带入幽匿块，不用担心惊醒监守者。因此，借助这个Beta版本，您可以安心熟悉幽匿块家族。但不要太过放松，监守者最终会加入深暗之域。以下是本周Beta中的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，网址为 [bugs.mojang.com](http://bugs.mojang.com/)。

# **实验性特性**

### **深暗之域**

- 在为监守者的加入做准备时，实施了尖啸体的调整，监守者将在稍后添加！
  - 幽匿尖啸体现在会监听幽匿感测体触须的点击声
  - 将导致监守者未来生成的威胁等级现在会随时间降低

# **非实验性特性和漏洞修复**

## **稳定性和性能**

- 修复了在游戏过程中可能发生的多个崩溃
- 修复了在Android上挂起或恢复应用时可能发生的崩溃

## **游戏玩法**

- 垂直视野在横向分屏中不再减半，使得在分屏游戏时更容易查看书与羽毛笔等物品
- 在世界生成期间调整了村庄等结构周围的地形（[MCPE-145659](https://bugs.mojang.com/browse/MCPE-145659)）
- 当“ TNT爆炸”游戏规则被禁用且“火焰蔓延”游戏规则被启用时，TNT不再消失（[MCPE-82485](https://bugs.mojang.com/browse/MCPE-82485)）
- 受重力影响的方块现在在放置在顶部雪上时会掉落，而不是悬浮在上面（[MCPE-151407](https://bugs.mojang.com/browse/MCPE-151407)）

## **原版趋同**

- 在创造模式中飞行的玩家不再受到液体流动的推动（[MCPE-84592](https://bugs.mojang.com/browse/MCPE-84592)）
- 农民村民现在可以在作物上使用骨粉，并可以在堆肥桶中将多余的种子转化为骨粉（[MCPE-74079](https://bugs.mojang.com/browse/MCPE-74079)）
- 保护魔咒现在在大多数伤害类型上正常工作（[MCPE-40651](https://bugs.mojang.com/browse/MCPE-40651)）
- 修复了一个不同步问题，有时会导致生命只在视觉上恢复
- 降落在钟乳石上现在被正确视为跌落伤害（[MCPE-151192](https://bugs.mojang.com/browse/MCPE-151192)）
- 修复了一些伤害无敌状态未正确应用的问题
- 修复了保护魔咒减免过多伤害的问题。此问题已更改以匹配Java版（[MCPE-113191](https://bugs.mojang.com/browse/MCPE-113191)）
- 吸收心不再在凋零效果下保持黄色（[MCPE-131852](https://bugs.mojang.com/browse/MCPE-131852)）
- 添加了盔甲韧性
- 钻石盔甲和下界合金盔甲的韧性值分别为2和3
- 调整了盔甲减伤计算以考虑韧性
- 下界合金盔甲现在比钻石盔甲减少更多伤害
- 降低了下界合金盔甲提供的击退抗性（[MCPE-109408](https://bugs.mojang.com/browse/MCPE-109408)）
- 击打造成的伤害现在减少，以更好地匹配Java版（[MCPE-152713](https://bugs.mojang.com/browse/MCPE-152713)）

## **图形**

- 修复了发光鱿鱼纹理中的一个错误，导致在alpha通道中的发光图不正确，造成非发光纹理的斑块（[MCPE-117507](https://bugs.mojang.com/browse/MCPE-117507)）
- 修复了在禁用方块轮廓选择时十字准星消失的问题
- 着火的玩家在物品栏屏幕上渲染的火焰现在始终位于玩家前方，无论游戏内相机视角如何（[MCPE-147777](https://bugs.mojang.com/browse/MCPE-147777)）
- 修复了皮革盔甲在纸娃娃上出现高亮效果的问题（[MCPE-75321](https://bugs.mojang.com/browse/MCPE-75321)）

## **物品**

- 热带鱼桶在捕获鱼后不再显示错误的名称

## **市场**

- 装备皮肤时的警告提示再次出现在产品页面上

## **生物**

- 劫掠兽现在会攻击流浪商人（[MCPE-44606](https://bugs.mojang.com/browse/MCPE-44606)）
- 从发射器生成的生物现在是持久的（[MCPE-110521](https://bugs.mojang.com/browse/MCPE-110521)）
- 潜影贝不再喜欢与其他潜影贝占用同一个方块（[MCPE-43972](https://bugs.mojang.com/browse/MCPE-43972)）
- 潜影贝现在优先附着在相邻方块的面上，而不是尝试传送
- 如果当前附着的方块面有效，潜影贝现在会保持附着，而不是切换到直立位置

## **用户界面**

- 修复了在新的创建新世界界面中某些语言的文本未正确渲染的问题（[MCPE-151948](https://bugs.mojang.com/browse/MCPE-151948)）

### **村民**

- 制图师现在始终解锁林地探险家地图交易（[MCPE-152725](https://bugs.mojang.com/browse/MCPE-152725)）

## **命令**

- 当尝试使用/loot spawn命令并传入未加载区域的位置且没有掉落物时，现在会正确显示错误输出
- 添加了'/loot '命令插入掉落和插入击杀重载
- 在客户端完成加入之前触发的标题命令现在会显示，而不是被忽略

# **技术更新**

## **实验性**

## **GameTest框架**

- BlockExplodeEvent
  - 移除了属性destroyedBlockPermutation
- 音乐管理的世界添加：
  - queueMusic(trackName : string, musicOptions : MusicOptions)
  - playMusic(trackName : string, musicOptions : MusicOptions)
  - stopMusic()
  - 添加了MusicOptions JS类，包含音量、渐变秒数和循环属性
- 添加事件 entityHurt(entityHurtEvent: EntityHurtEvent, options?: EntityEventOptions) - 当实体受到伤害时触发
- 移除了'Minecraft'和'GameTest'导入；请使用'mojang-minecraft'和'mojang-gametest'

## **一般**

- 从数据驱动方块中移除了“preventsjumpingcomponent”

## **图形**

- 在所有Android和iOS设备上测试RenderDragon

## **JumpToBlock行为**

- JumpToBlock行为现在正确受到跳跃提升生物效果的影响（[MCPE-137432](https://bugs.mojang.com/browse/MCPE-137432)）

## **方块组件**

- 修复了实验性BlockCollisionComponents未允许部分指定的情况