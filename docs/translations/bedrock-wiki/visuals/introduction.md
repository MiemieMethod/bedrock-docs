---
title: 简介
description: 基岩版实体视觉章节的概览。
category: 教程
---


/// details-info | 来源信息
- 原文仓库：[github.com/Bedrock-OSS/bedrock-wiki](https://github.com/Bedrock-OSS/bedrock-wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/introduction](https://wiki.bedrock.dev/visuals/introduction)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

## 这一章讲什么

这里讨论的是实体、皮肤、材质、动画与结构展示一类“看得见”的内容。重点不在机制本身，而在如何让内容更好看、更容易展示，也更容易在资源包里被整理和复用。

## 适合从哪里开始

- 想做玩家皮肤：先看[皮肤包](skin-packs.md)。
- 想改实体外观：先看[玩家几何体](player-geometry.md)和[实体纹理动画](animated-entity-texture.md)。
- 想处理材质与发光：先看[材质](materials.md)和[发光纹理](glowing-texture.md)。
- 想做演示图：先看[结构展示](structure-presentation.md)。

## 这一章的核心判断

视觉类内容大致分成三层：

1. **模型层**：几何体、骨骼、定位器和结构形状。
2. **渲染层**：材质、渲染控制器、纹理与覆盖色。
3. **表现层**：动画、特效、受伤反馈、死亡反馈与展示方式。

只要这三层分清楚，后面的很多问题都会变得非常直观。