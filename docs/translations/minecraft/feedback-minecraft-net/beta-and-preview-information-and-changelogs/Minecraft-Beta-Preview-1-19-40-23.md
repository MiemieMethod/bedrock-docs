---
title: Minecraft Beta & Preview - 1.19.40.23
date: 2022-09-29T14:48:32Z
updated: 2022-09-29T15:44:50Z
categories: Beta和预览信息及更新日志
link: https://feedback.minecraft.net/hc/en-us/articles/9527647861005-Minecraft-Beta-Preview-1-19-40-23
---

**发布时间：** 2022年9月29日

## **Minecraft预览版和测试版信息：**

- 这些正在开发中的版本可能不稳定，且可能无法代表最终版本的质量
- Minecraft预览版可在Xbox、Windows 10/11和iOS设备上使用。更多信息请访问 [aka.ms/PreviewFAQ](http://aka.ms/PreviewFAQ)
- 测试版可在Android（Google Play）上使用。要加入或退出测试版，请参见 [aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta) 获取详细说明

![与本周预览中的修复相关的Minecraft截图，场景中有下界传送门遗迹、凋灵骷髅、村民和其他各种生物。](https://feedback.minecraft.net/hc/article_attachments/9527542833677/R19U4_4_16x9.jpg)

以下是本周Minecraft预览版和测试版的新内容！如往常一样，请搜索并报告您可能发现的任何漏洞，欢迎随时向我们发送 [您的反馈](https://aka.ms/MinecraftBetaFeedback)。

# **新特性和漏洞修复**

## **原版趋同**

- 被重命名武器的生物击杀时，现在会产生包含物品名称的死亡信息 ([MCPE-162055](https://bugs.mojang.com/browse/MCPE-162055))
- 凋灵骷髅现在可以在凋灵玫瑰内生成 ([MCPE-110127](https://bugs.mojang.com/browse/MCPE-110127))
- 游泳时消耗的饥饿值减少，以与Java版保持一致 ([MCPE-154452](https://bugs.mojang.com/browse/MCPE-154452))
- 图书管理员村民现在可以提供带有消失诅咒和绑定诅咒的附魔书 ([MCPE-84906](https://bugs.mojang.com/browse/MCPE-84906))

## **旁观模式（实验性）**

- 潜影弹不再追踪旁观者 ([MCPE-162069](https://bugs.mojang.com/browse/MCPE-162069))
- 旁观者现在对普通玩家不可见
- 如果玩家处于旁观模式且服务器上有其他非旁观玩家，旁观玩家将不再影响生物的毁除
- 如果服务器上只有旁观玩家，生物的毁除现在将被暂停

## **用户界面**

- 修复了死亡信息有时过长以至于无法在屏幕上显示的漏洞 ([MCPE-156550](https://bugs.mojang.com/browse/MCPE-156550))
- 触摸设备的物品栏按钮在关闭物品栏后现在会重置为默认外观
- 修复了合成界面搜索字符串未正确保存的问题
- 修复了Xbox物品栏界面上耐久条缺失的问题 ([MCPE-162063](https://bugs.mojang.com/browse/MCPE-162063))
- 修复了“创建新世界”中的登录按钮在某些平台上无法使用的漏洞

## **移动触控控制**

- 修复了在移动设备的创造模式物品栏中，无法通过将物品移动到其他物品上来移除快捷栏物品的漏洞
- 修复了堆叠拆分进度条在触控模式下未对齐的问题
- 根据用户反馈调整了触控工具栏和状态效果图标的布局
- 在我们处理反馈期间，暂时禁用了新触控堆叠拆分用户体验的预览

## **生物**

- 当生物作为船的乘客时，船和生物都不允许更改维度 ([MCPE-154919](https://bugs.mojang.com/browse/MCPE-154919))

## **方块**

- 附魔台的书现在正确朝向附近的玩家 ([MCPE-29924](https://bugs.mojang.com/browse/MCPE-29924))

## **NPC（教育版）**

- NPC现在可以没有名字，从而隐藏其头顶的名牌

## **市场**

- 修复了市场捆绑包价格在购买后未显示为免费的问题

## **性能和稳定性**

- 修复了爆炸中的潜在崩溃源
- 修复了离开分屏会话时可能发生的崩溃

# **技术更新**

## **实验性特性**

## **API**

**对实验性JavaScript API的重大破坏性更改：**

所有脚本模块已重命名以遵循新约定。

- *mojang-gametest* -> *@minecraft/server-gametest*
- *mojang-minecraft* -> *@minecraft/server*
- *mojang-minecraft-ui* -> *@minecraft/server-ui*
- *mojang-minecraft-server-admin* -> *@minecraft/server-admin*
- *mojang-net* -> *@minecraft/server-net*

例如，使用：

import \* as mc from “mojang-minecraft”;

改为使用

import \* as mc from “@minecraft/server”;

- 必须在json中显式启用脚本eval()和Function()
  - 为此，请设置script_evalin能力

"capabilities": \[ "script_eval"\]

- 导入的根路径已更改；不再允许使用scripts/prefix。
- 对于导入，使用import "./source.js"或import "source.js"
- 不再推荐使用import "scripts/source.js"

## **活动对象属性**

- 修复了未指定“值”的“bool_property”过滤器

## **命令**

- 在解决漏洞期间，暂时禁用了/summon命令的旋转
- 修复了命令方块执行'execute facing'和'execute rotated'时的旋转问题 ([MCPE-162256](https://bugs.mojang.com/browse/MCPE-162256))
- 实现了'/execute in'命令
- 实现了'/execute anchored \<eyes\|feet\>'命令

## **通用**

- 将BlockGeometryComponent从实验性发布到1.19.40及更高版本的JSON格式
- 将BlockMaterialInstancesComponent从实验性发布到1.19.40及更高版本的JSON格式
- 将*minecraft:block_light_filter*组件重命名为*minecraft:light_dampening*