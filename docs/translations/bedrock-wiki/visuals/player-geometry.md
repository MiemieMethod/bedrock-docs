---
title: 玩家几何体
description: 用于制作玩家型实体的几何体结构。
category: 教程
---


/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/player-geometry](https://wiki.bedrock.dev/visuals/player-geometry)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

本文展示的是玩家型实体的几何体写法。它的核心不是“教你画模型”，而是说明如何组织一个可用于玩家NPC的骨骼结构。

## 结构要点

玩家几何体通常至少包含：

- `root`
- `waist`
- `body`
- `head`
- 双臂与双腿
- `hat`、`jacket`、`sleeve`、`pants`等外层部件
- `leftItem`、`rightItem`和`lead`等定位器

## 为什么要这样做

这样组织的好处是可以直接复用原版玩家的动画逻辑，并让不同部件分别响应动作、装备和显示切换。

## 实际使用

如果只是想做一个“像玩家”的NPC，通常不需要从零重写所有动画。更稳妥的做法是先复用原版玩家骨架，再逐步替换外观和少量部件。