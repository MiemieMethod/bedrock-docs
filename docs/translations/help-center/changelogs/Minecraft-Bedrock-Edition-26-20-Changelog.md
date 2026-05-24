---
title: "Minecraft：基岩版26.20更新日志（开发向节选）"
date: 2026-04-27T14:19:24Z
updated: 2026-05-08T20:14:29Z
categories: 发布日志
original_link: https://feedback.minecraft.net/hc/en-us/articles/45400537384333-Minecraft-Bedrock-Edition-26-20-Changelog
---


/// details-info | 来源信息
- 原文仓库：[github.com/XeroAlpha/MinecraftHelpCenterArchive](https://github.com/XeroAlpha/MinecraftHelpCenterArchive)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

**发布时间**：2026年5月5日

/// note | 说明
本页为开发相关重点节选翻译，完整条目请以[官方原文](https://feedback.minecraft.net/hc/en-us/articles/45400537384333-Minecraft-Bedrock-Edition-26-20-Changelog)为准。
///

## 版本概览

26.20为功能量较大的更新，除玩法修复外，重点包含以下方向：

- “Chaos Cubed”实验性内容：硫磺立方体、硫磺洞穴、硫磺泉与配套方块组。
- 可访问性：加入可配置的闭合字幕。
- 命令与脚本：命令行为修复、脚本API版本推进、UI与调试能力扩展。
- 数据驱动与架构：方块、实体、AI意向等多类JSON架构在`1.26.20`起变得更严格。

## 功能与修复（节选）

### 可访问性与用户界面

- 新增闭合字幕功能，支持声音类别、显示位置、持续时间等配置。
- 修复了分辨率变化后的错误UI缩放问题。
- 修复了iOS外接键盘输入与光标行为问题。
- 改进了Ore UI在异形屏安全区内的滚动显示行为。

### 游戏玩法与图形

- 修复了部分击退行为，使其更接近Java版表现。
- 修复了多项鲜艳视效下的纹理、光照、遮挡与模型表现问题。
- 修复了部分幼年生物纹理、碰撞箱、动画与音效不一致问题。

### Realm与联机体验

- 党派系统（Beta）上线，支持跨世界组队与党派聊天。
- Realms引入Realm Hub及管理员日志、时间线等改动，并修复多项Realm稳定性问题。

## 技术更新（节选）

### 命令

- 修复了禁用跳跃后玩家仍可能自动跳跃的问题（`/inputpermission`相关，MCPE-235573）。
- 修复了`/loot`失败时可能中断`/execute`后续链的问题（MCPE-185887）。

### 脚本API与模块

- 发布`@minecraft/server 2.7.0`，新增`@minecraft/server 2.8.0-beta`。
- 多项瞄准辅助相关API从beta转正到`v2.6.0`。
- `Player`新增party信息只读字段（beta）。
- `@minecraft/server-ui`与Data Driven UI相关返回类型、关闭原因与错误类型发生调整。

### 方块与数据驱动加载

- 从`format_version 1.26.20`开始，方块与多类组件校验更严格，非法字段将导致内容加载失败。
- `minecraft:tags`写法发生约束变化：标签需置于`minecraft:tags`组件中，不再建议旧式顶层`tag:`写法。
- 多个`multi_block`相关组件与置换位置限制被收紧，错误写法将触发内容报错。

### 实体与组件

- 新增`minecraft:on_equipment_changed`、`minecraft:spawn_on_death`、`minecraft:bounciness`等组件。
- `minecraft:friction_modifier`行为修正为与文档描述一致；旧行为可通过`minecraft:uses_legacy_friction`保持。
- 引入实体定义的`entity_version`升级链机制（实验性），支持按版本顺序执行升级处理。

### 网络协议

- 修改了`PlayerEnchantOptionsPacket`的二进制格式。
- `UpdateClientOptionsPacket`新增`Filter Profanity Change`布尔字段。

## 实验性技术更新（节选）

- 新增“Custom Projectiles”实验开关，支持更完整的自定义弹射物物理与反射行为。
- Voxel Shapes实验扩展了更多原版方块的非单位立方体体素形状，用于改善面剔除。
- 增加了用于检查方块积雪日志行为的脚本方法。