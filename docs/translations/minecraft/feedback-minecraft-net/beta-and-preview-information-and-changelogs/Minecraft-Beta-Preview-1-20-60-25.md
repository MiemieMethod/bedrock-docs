---
title: Minecraft Beta & Preview - 1.20.60.25
date: 2024-01-10T14:20:32Z
updated: 2024-01-10T14:44:44Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/23082413763341-Minecraft-Beta-Preview-1-20-60-25
hash:
  h_01HBVR6KM8JCTEG8SDY8V3WBB3: 关于Minecraft预览和测试版的信息
  h_01HKSX5AVV6NVMCEQ8VM9EWZ3A: 实验性特性
  h_01HKSX5DPTHMFXCY9S391CY44Y: 试炼刷怪笼
  h_01HKSX5J4H9EBQP0HK0DB80GZD: 旋风人
  h_01HKSX5PY11VS7FJ4X9SVRQ7T7: 特性和漏洞修复
  h_01HKSX5TXZGAX6J0JWTM8B2XA8: 方块
  h_01HKSX5XS3SN2T0RHWPM1CZYEG: 双箱子--双陷阱箱
  h_01HKSX61GEHCSR9VHKB7MNTP75: 一般
  h_01HKSX64NA6DDT4MF1EZR6156K: 物品
  blocks: 方块-1
---

**发布于：** 2024年1月10日

## **关于Minecraft预览和测试版的信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](https://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。有关加入或退出测试版的详细说明，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)

![一幅Minecraft场景，展示了一个试炼室，里面有旋风人、一个穿着盔甲的僵尸疣猪兽和一些豹猫在背景中。](https://feedback.minecraft.net/hc/article_attachments/23082748746637)

以下是最新Minecraft预览和测试版中的新内容。我们始终欢迎您的反馈，请在 [这里](https://aka.ms/MinecraftArmadilloFeedback) 告诉我们您的想法，并在 [bugs.mojang.com](https://bugs.mojang.com/) 报告您可能遇到的任何漏洞。

# **实验性特性**

## **试炼刷怪笼**

- 当检测到玩家时，如果试炼刷怪笼剩余的生成时间少于两秒，则生成延迟设置为两秒

## **旋风人**

- 旋风人现在可以反射所有投射物
- 旋风人现在将投射物反射回射击实体，散布角度为40度
- 旋风人身体杆底部的像素现在与周围颜色匹配

# **特性和漏洞修复**

## **方块**

- 相同颜色的旗帜物品现在可以一致堆叠，无论它们之前是否作为方块放置在世界中（[MCPE-43391](https://bugs.mojang.com/browse/MCPE-43391)）
- 凋灵玫瑰现在每0.5秒对生物造成伤害，而不是每2秒（[MCPE-55878](https://bugs.mojang.com/browse/MCPE-55878)）
- 被克隆的容器不再保持其容器屏幕打开或导致崩溃

## **双箱子与双陷阱箱**

- 修复了双箱子和双陷阱箱盖上的像素阴影（[MCPE-169495](https://bugs.mojang.com/browse/MCPE-169495)）

## **一般**

- “你需要一枚薄荷”成就现在只能通过收集龙息解锁（[MCPE-177409](https://bugs.mojang.com/browse/MCPE-177409)）

## **物品**

- 玩家现在可以在饥饿条满时消费谜之炖菜（[MCPE-122491](https://bugs.mojang.com/browse/MCPE-122491)）

## **生物**

- 钓鱼时释放的经验球散布量已减少（[MCPE-170540](https://bugs.mojang.com/browse/MCPE-170540)）
- 僵尸疣猪兽在和平模式下不再生成，并且如果难度切换到和平模式将会消失（[MCPE-79480](https://bugs.mojang.com/browse/MCPE-79480)）
- 经验球不再与生物碰撞（[MCPE-87711](https://bugs.mojang.com/browse/MCPE-87711)）
- 甜浆果丛不再对穿过它们的蜜蜂造成伤害（[MCPE-114689](https://bugs.mojang.com/browse/MCPE-114689)）
- 狼现在可以在雪和顶部雪的雪林生物群系中生成（[MCPE-147656](https://bugs.mojang.com/browse/MCPE-147656)）

## **稳定性和性能**

- 修复了可能导致在加入领域时无限加载的漏洞

## **世界生成**

- 现在黑橡树和金合欢树可以替换的方块限制也适用于它们的树枝，而不仅仅是树干
- 在生成时放置的顶部雪现在也覆盖高草丛和花（[MCPE-142321](https://bugs.mojang.com/browse/MCPE-142321)）

# **技术更新**

## **API**

- 将“不支持或超出范围的值...”错误更改为使用 *ArgumentOutOfBoundsError* 错误类型

## **方块**

- 增加了数据驱动的方块在与完整且不透明的方块相邻时移除几何体面片的能力。为方块几何体组件添加了一个新字段，引用一个新的剔除.json文件（位于资源包的block_culling目录中），该文件设置了切割几何体的规则

## **维度API**

- *setWeather*方法的参数持续时间现在使用 *ArgumentOutOfBoundsError* 错误类型

## **编辑器**

编辑器及其 [对应的API](https://aka.ms/EditorAPI) 目前处于早期开发阶段，并在Windows PC基岩预览版构建中可通过键盘/鼠标使用。在社交媒体上标记我们，使用 **\#BedrockEditor**。

了解 [如何使用](https://www.aka.ms/LearnEditor) 编辑器，加入 [GitHub讨论论坛](https://github.com/Mojang/minecraft-editor/discussions) 与团队互动，并通过 [入门工具包](https://github.com/Mojang/minecraft-editor-extension-starter-kit) 和 [示例](https://github.com/Mojang/minecraft-editor-extension-samples) 开始构建扩展。

本周更新：

- 修复了一个漏洞，该漏洞导致子菜单项在刷新编辑器屏幕时错误地添加到根级别

# **实验性技术更新**

## **API**

- *PropertyOutOfBoundsError*
  - 添加了一个新的 *PropertyOutOfBoundsError*，当设置的属性超出范围时会抛出
- *ContainerSlot* API现在会抛出 *InvalidContainerSlotError*，如果容器槽无效，或者如果在空槽上设置了属性
- 属性 *typeId* 不再对空槽返回未定义，而是抛出 *InvalidContainerSlotError*
- 添加了函数 *hasItem* - 返回槽中是否包含物品
- 添加了函数 *getCanPlaceOn* - 返回物品可以放置的方块标识符数组
- 添加了函数 *getCanDestroy* - 返回物品在使用时可以摧毁的方块标识符数组

## **命令**

- 骑乘生物的生命条现在正确显示（[MCPE-177696](https://bugs.mojang.com/browse/MCPE-177696)）
- 执行命令在比较未加载的方块时现在会失败（[MCPE-177195](https://bugs.mojang.com/browse/MCPE-177195)）
- Hud命令现在按预期工作 - /hud命令允许创作者单独显示/隐藏每个元素，以及显示/隐藏所有元素。隐藏一个元素不再隐藏“所有”元素。

## **图形**

- 修复了一个问题，导致洞穴在延迟技术预览中看起来被阳光照亮（即“光泄漏”）
- 在延迟技术预览中，体积迷雾不再受封闭空间中阳光的影响