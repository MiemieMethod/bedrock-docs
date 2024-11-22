---
title: Minecraft Beta - 1.18.20.25 (Xbox / Windows / Android)
date: 2022-02-09T15:48:46Z
updated: 2022-02-10T10:17:06Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/4424787358221-Minecraft-Beta-1-18-20-25-Xbox-Windows-Android
---

**发布于：** 2022年2月9日

**请在参与Minecraft Beta之前阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，也无法在预览测试期间加入非测试版玩家
- 在测试版中玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的备份以防丢失
- 测试版构建可能不稳定，并且不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上可用。有关加入或退出测试版的详细说明，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)
- Minecraft预览玩家可能会收到略有不同的版本号，但此处的修复和功能应相同。更多信息请查看：[aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)。

![froglight_beta.jpg](https://feedback.minecraft.net/hc/article_attachments/4424787313677/froglight_beta.jpg)

 

是时候进行另一次更新了，以下是本周测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，网址为[bugs.mojang.com](http://bugs.mojang.com/)。

**请注意：** 在下一个测试版和预览更新之前，已注册的Xbox玩家将保持在1.18.20.24版本。

# **实验性功能**

## **青蛙卵**

- 从下方观察时，青蛙卵不再是隐形的
- 青蛙和海龟现在可以被垂直诱惑

## **蛙明灯**

- 蛙明灯块不再随机旋转，并获得了新的纹理（[MCPE-151514](https://bugs.mojang.com/browse/MCPE-151514)）

## **山羊角**

- 当山羊的角断裂时会播放声音
- 在第一人称和第三人称视角使用山羊角时现在会显示动画（[MCPE-104158](https://bugs.mojang.com/browse/MCPE-104158)）  
    

# **非实验性功能和漏洞修复**

## **游戏玩法**

- 放置紫水晶簇时，移除了额外方块中的水（[MCPE-148394](https://bugs.mojang.com/browse/MCPE-148394)）
- 撤回珊瑚扇路径的修复
  - 请注意 - 此撤回是暂时的变化，我们正在考虑玩家的反馈以及整体游戏平衡
- 调整了饥饿消耗速率，以更好地匹配Java版（[MCPE-56031](https://bugs.mojang.com/browse/MCPE-56031)）
  - 玩家在疾跑或游泳时现在可以正确消耗饥饿
  - 玩家跳跃时消耗的饥饿显著减少
  - 疲劳度的消耗速率现在可以在行为包中进行调整

## **生物**

- 修复了实体未受到抗火效果保护的火焰伤害问题
- 例如，骑在船上的生物现在无法使用JumpToBlockGoal（[MCPE-150750](https://bugs.mojang.com/browse/MCPE-150750)）

## **用户界面**

- 玩家死亡时，蹲伏状态现在会重置，以避免在重生后卡在蹲伏状态
- 新的创建新世界界面中的资源包选项卡现在可用

## **原版趋同**

### **村民**

- 渔民的船交易现在根据村民的生物群系类型改变木材类型
- 牧师现在提供荧石而不是荧石粉
- 武器匠的附魔铁剑交易移至新手
- 盔甲匠的钻石交易移至老手

## **命令**

- 使用/playanimation命令现在会更新纸娃娃和物品栏角色（[MCPE-137353](https://bugs.mojang.com/browse/MCPE-137353)）

# **技术更新**

## **附加包和脚本引擎**

- 在覆盖迷雾设置时，使用特定生物群系的原版迷雾设置作为默认值

## **命令**

- 在客户端完成加入之前触发的标题命令现在会显示，而不是被忽略

## **图形**

- 修复了在从启用RTX的世界退出时，光线追踪资源被过早销毁的情况

**实验性技术**

- 音量定义现在存储并从行为包中读取，而不是作为关卡目录的一部分

## **GameTest框架**

- BlockInventoryComponent
  - 修复了在双箱子中访问物品时崩溃/不一致的问题
- 添加了nameTag属性
- 添加了id属性
- 添加了MinecraftDimensionTypes，包含内置维度ID的常量
- 添加了spawnItem，用于在该维度中生成物品堆
- 为实体暴露了以下组件：
  - minecraft:can_climb
  - minecraft:can_fly
  - minecraft:can_power_jump
  - minecraft:fire_immune
  - minecraft:floats_in_liquid
  - minecraft:is_dyable
  - minecraft:is_baby
  - minecraft:is_charged
  - minecraft:is_chested
  - minecraft:is_hidden_when_invisible
  - minecraft:is_ignited
  - minecraft:is_illager_captain
  - minecraft:is_saddled
  - minecraft:is_shaking
  - minecraft:is_sheared
  - minecraft:is_stackable
  - minecraft:is_stunned
  - minecraft:is_tamed
  - minecraft:wants_jockey