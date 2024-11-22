---
标题: Minecraft Beta - 1.17.20.23 (Xbox One/Windows 10/Android)
日期: 2021-07-22T14:28:18Z
更新: 2021-07-22T15:48:21Z
分类: Beta 和预览信息及更新日志
标签:
  - beta
  - beta_changelog
  - 洞穴与悬崖
链接: https://feedback.minecraft.net/hc/en-us/articles/4405541243405-Minecraft-Beta-1-17-20-23-Xbox-One-Windows-10-Android
哈希:
  gametest-framework-experimental: gametestframework-experimental
  user-interface-1: userinterface
---

**发布时间:** 2021年7月22日

**在参与Minecraft Beta之前请阅读：**

- 加入Beta将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问Realm，并且在预览Beta期间无法加入非Beta玩家
- 在Beta期间玩过的任何世界无法在游戏的早期版本中打开，因此请制作世界的备份以防丢失
- Beta版本可能不稳定，并且不代表最终版本的质量
- Beta仅在Xbox One、Windows 10和Android（Google Play）上可用。要加入或退出Beta，请查看[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

 

![Screen_Shot_07-22-21_at_02.38_PM.JPG](https://feedback.minecraft.net/hc/article_attachments/4405554717581/Screen_Shot_07-22-21_at_02.38_PM.JPG)

我们今天发布了另一个基岩版Beta更新，并修复了一些漏洞！

请在<https://aka.ms/CavesCliffsFeedback>的讨论区发送您的反馈，并在[https://bugs.mojang.com](https://bugs.mojang.com/)搜索并报告您可能遇到的任何新漏洞。

 

# **功能和漏洞修复**

## **稳定性和性能**

- 修复了在游戏过程中可能发生的多个崩溃
- 优化了将Unicode文本粘贴到书与羽毛笔中的操作（[MCPE-119651](https://bugs.mojang.com/browse/MCPE-119651)）
- 修复了在启用游戏提示时合成工作台可能导致的崩溃

## **游戏玩法**

- 修复了床的显示问题，如果床的脚部在比头部更亮的区域时显示不正确（[MCPE-123592](https://bugs.mojang.com/browse/MCPE-123592)）
- 修复了大箱子的显示，以便选择箱子最亮的一端（[MCPE-123592](https://bugs.mojang.com/browse/MCPE-123592)）
- 通过末地传送门旅行不再导致玩家受到坠落伤害（[MCPE-135226](https://bugs.mojang.com/browse/MCPE-135226)，[MCPE-132484](https://bugs.mojang.com/browse/MCPE-132484)）

## **物品**

- 远离玩家时，投射物品的移动更加平滑（[MCPE-101102](https://bugs.mojang.com/browse/MCPE-101102)）
- 在市场地图中持有盾牌不再显示内容错误
- 强力/长效/闪烁/滞留药水可以手动放置在酿造台中（[MCPE-86636](https://bugs.mojang.com/browse/MCPE-86636)）

## **生物**

- 站在细雪附近的亡灵生物现在会正常燃烧（[MCPE-131005](https://bugs.mojang.com/browse/MCPE-131005)）
- 亡灵生物上方的细雪现在可以防止燃烧效果
- 多个潜影贝不再能够从刷怪蛋或末地城生成在同一位置生成（[MCPE-43972](https://bugs.mojang.com/browse/MCPE-43972)）
- 生物现在可以在紫晶芽上正确寻路（[MCPE-130010](https://bugs.mojang.com/browse/MCPE-130010)）
- 修复了玩家下马后马有时变得不可见的问题（[MCPE-108568](https://bugs.mojang.com/browse/MCPE-108568)）
- 成年的山羊在重新加载世界时不再失去角
- 雷电不再随机击中处于方块下方的生物（[MCPE-121688](https://bugs.mojang.com/browse/MCPE-121688)）

## **方块**

- 孢子花不再有随机偏移的击中箱（[MCPE-121658](https://bugs.mojang.com/browse/MCPE-121658)）
- 苔藓块和覆地苔藓在被活塞移动时现在会破坏，黏性活塞不再能拉动它们（[MCPE-121751](https://bugs.mojang.com/browse/MCPE-121751)）（[MCPE-122004](https://bugs.mojang.com/browse/MCPE-122004)）
- 从小型滴水石锥滴落的水不再能填充炼药锅中的药水（[MCPE-131180](https://bugs.mojang.com/browse/MCPE-131180)）
- 孢子花的击中箱测量现在与Java版一致
- 修复了导致史莱姆和蜂蜜块移动减速未完全应用于玩家的问题

## **用户界面**

- 在游戏中按下Ctrl+B时不再出现表情轮（[MCPE-125246](https://bugs.mojang.com/browse/MCPE-125246)）
- 修复了在Windows 10上暂停游戏后输入法编辑器（IME）无法工作的情况（[MCPE-59722](https://bugs.mojang.com/browse/MCPE-59722)）
- 在市场和着装间相关屏幕中添加了新的侧边栏，以帮助改善这些区域的导航体验
- 取消选择配方时现在有物品转移动画

## **命令**

- 使用“/structure”命令加载结构时现在显示正确的输出消息（[MCPE-132813](https://bugs.mojang.com/browse/MCPE-132813)）

# **技术更新**

## **游戏测试框架（实验性）**

- 将模块“Minecraft”重命名为“mojang-minecraft”
- 将模块“GameTest”重命名为“mojang-gametest”
  - 将函数assertBlockTypePresent重命名为assertBlockPresent
  - 将函数assertEntityData重命名为assertEntityState
  - 移除函数assertBlockTypeNotPresent
  - 移除函数assertEntityNotPresent
  - 移除函数assertEntityNotPresentInArea
  - 移除函数assertEntityNotTouching
  - 移除函数succeedWhenEntityNotPresent
  - 修改函数assertBlockState(blockLocation: BlockLocation, callback: (Block) => boolean)的签名
  - 修改函数assertBlockPresent(blockType: BlockType, blockLocation: BlockLocation, isPresent: boolean)的签名
  - 修改函数assertEntityPresent(entityTypeIdentifier: string, blockLocation: BlockLocation, isPresent: boolean)的签名
  - 修改函数assertEntityPresentInArea(entityTypeIdentifier: string, isPresent: boolean)的签名
  - 修改函数assertEntityTouching(entityTypeIdentifier: string, location: Location, isTouching: boolean)的签名
  - 修改函数succeedWhenEntityPresent(entityTypeIdentifier: string, location: Location, isPresent: boolean)的签名
  - 添加GameTestExtension函数assertBlockProperty(propertyName: string, value: number | string | boolean, blockLocation: BlockLocation)

## **命令**

- '/particle'命令的位置参数现在是可选的（[MCPE-128379](https://bugs.mojang.com/browse/MCPE-128379)）
- '/particle'命令现在在成功时输出（[MCPE-80348](https://bugs.mojang.com/browse/MCPE-80348)）
- '/particle'命令在通过'/execute'成功运行时不再显示错误（[MCPE-129001](https://bugs.mojang.com/browse/MCPE-129001)）

## **游戏玩法**

- 数据驱动的方块现在可以添加到创造模式菜单中

## **Molang**

- 资源包和行为包清单中的'min_engine_version'现在传递到Molang表达式解析中。这允许与特定引擎版本相关的未来破坏性更改

## **用户界面**

- UI绑定对象现在可以使用忽略字段