---
title: Minecraft Beta - 1.17.30.23 (Xbox One/Windows 10/Android)
date: 2021-08-25T14:42:26Z
updated: 2021-08-25T15:48:47Z
categories: Beta 和预览信息及更新日志
tags:
  - beta
  - beta_changelog
  - caves&cliffs
link: https://feedback.minecraft.net/hc/en-us/articles/4407848671117-Minecraft-Beta-1-17-30-23-Xbox-One-Windows-10-Android
hash:
  caves-cliffs-experimental-features: caves--cliffs-experimental-features
---

**发布于:** 2021年8月25日

**在参与Minecraft Beta之前，请阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防止丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出测试版，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

 

![worldgen1170x500.jpg](https://feedback.minecraft.net/hc/article_attachments/4407848582157/worldgen1170x500.jpg)

 

我们经历了许多风暴，穿越了暴风雪，幸存于炽热的阳光下，然后叫了一辆出租车，以便我们能够发布一个新的基岩版更新测试版！您只需启用“洞穴与山崖”实验性功能切换，然后沉浸在新的功能中，比如具有多噪声生成的3D生物群系！

这些功能仍处于早期阶段，但我们非常希望听到您的反馈，您可以在[aka.ms/CavesCliffsFeedback](https://aka.ms/CavesCliffsFeedback)上反馈，您也可以在bugs.mojang.com上搜索和报告您可能遇到的任何新漏洞。您可以在[aka.ms/MCExperimentalToggle](https://aka.ms/MCExperimentalToggle)上阅读更多关于实验性切换的信息。

**在您游玩之前！此测试版中的世界生成预计会很慢，特别是如果您在较旧的设备上游玩。我们正在努力提高生成速度，以便在“洞穴与山崖第二部分”发布之前完成这些修复，但这些修复尚未准备好实施。您可以通过这个简短的调查告诉我们游戏的运行情况：** [**aka.ms/MCBetaPerf**](https://aka.ms/MCBetaPerf)

 

# **洞穴与山崖实验性功能**

**多噪声世界生成**

- 新的改进地形和生物群系生成算法，创建更自然的地形和生物群系过渡
- 改进的表面装饰，能够检测块在水下和地下生成时的差异
- 引入大型矿脉到世界生成中，为开采增加更多策略
- 引入面条洞穴到世界生成中，创建较大洞穴之间的小通道
- 引入干燥洞穴入口的可能性，使访问新的噪声洞穴变得更容易
- 引入一种新算法，找到更接近原点的合适生成位置
- 添加逻辑以通过绝对Y索引保存和加载子区块，以支持数据驱动的维度高度范围

# **非实验性功能和漏洞修复**

## **游戏玩法**

- 营火和灵魂营火现在可以在物品栏中堆叠 ([MCPE-67890](https://bugs.mojang.com/browse/MCPE-67890))
- 当蛋糕被活塞推动时，蜡烛现在会掉落 ([MCPE-130594](https://bugs.mojang.com/browse/MCPE-130594))
- 收集鱼或美西螈不再会立即释放它们 (<u>[MCPE-44320](https://bugs.mojang.com/browse/MCPE-44320)</u>)
- 重命名的结构方块在创建时将不再有错误的数据模式 ([MCPE-41625](https://bugs.mojang.com/browse/MCPE-41625))
- 从脚手架上摔下时不再受到跌落伤害 ([MCPE-108459](https://bugs.mojang.com/browse/MCPE-108459))
- 修复了在使用§l进行宽字母和荧光墨囊时告示牌右侧缺失的轮廓像素 ([MCPE-137802](https://bugs.mojang.com/browse/MCPE-137802))
- 荆棘魔咒现在会对生物造成击退 ([MCPE-56212](https://bugs.mojang.com/browse/MCPE-56212))
- 调整了铁傀儡生成逻辑，以更好地匹配Java版
- 绯红菌索现在在使用骨粉时有小概率在诡异菌岩块上生长 ([MCPE-83616](https://bugs.mojang.com/browse/MCPE-83616))

## **命令**

- 现在可以在玩家睡觉时使用'/spawnpoint'命令，并在设置到玩家现有生成点时输出成功 ([MCPE-106720](https://bugs.mojang.com/browse/MCPE-106720))
- 当使用"@s"作为选择器时，相机震动命令不再会震动每个玩家的屏幕 ([MCPE-120383](https://bugs.mojang.com/browse/MCPE-120383))

## **市场**

- 修复了某些显示语言中“CR”字符错误出现在行末的问题

## **用户界面**

- 修复了可能导致“登录”按钮出现在市场按钮后面的错误
- 修复了在Windows和Xbox平台的日语区域中Noto Sans Smooth字体的可读性和正确字符使用问题

 

# **技术更新**

## **活动对象**

- 修复了在更多场景中使用无效数据进行运动预测插值的问题 ([MCPE-108568](https://bugs.mojang.com/browse/MCPE-108568))

## **物品**

- 修复了触发变换物品事件后崩溃的问题

## **Molang**

- 添加了物品冷却的实验性查询：'query.is_cooldown_type'，'query.cooldown_time'和'query.cooldown_time_remaining'
- 更新了许多Molang内容错误，以指定涉及的操作符或查询

## **命令**

- “run_command”事件响应现在将正确使用版本化命令

## **数据驱动物品**

- 更新了'IconItemComponent'的文档，现在提供'legacy_id'字段的所有ID列表

## **数据驱动声音**

- 从'sound_definitions.json'中删除了“replace”元素，因为其用法模糊（并且从未使用过）

## **游戏玩法**

- 数据驱动的方块现在可以添加到创造模式菜单中
- 击退咆哮不再比以前更强

## **图形**

- 修复了在使用动画控制器时粒子未发射的问题

## **玩家**

- 在第一人称视角中可见的附着物将不再反向渲染