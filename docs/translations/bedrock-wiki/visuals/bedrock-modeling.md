---
title: 基岩建模
description: 建模时需要注意的几个常见问题。
category: 说明
---

/// details-info | 译文信息
- 原文：[https://wiki.bedrock.dev/visuals/bedrock-modeling](https://wiki.bedrock.dev/visuals/bedrock-modeling)
- 作者或组织：Bedrock OSS
- 许可：[知识共享署名-相同方式共享4.0国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/)
///

这篇文章主要讲建模时容易踩的坑，而不是建模软件本身的操作。

## 常见问题

- **纹理抖动**：小于1个单位的面容易出现UV映射问题。
- **顶点吸附**：适合做轮子、圆角之类的形状。
- **半透明顺序**：半透明部件通常要放在元素列表后面。
- **Z-fighting**：两个面重叠时会闪烁，可通过微小膨胀错开。

## 材质

模型是否能正确表现透明、发光等效果，最终还是取决于材质。

## 动画

基岩版模型最常用的还是几何体模型。它可以配合动画控制器、定位器和脚本做出很复杂的表现。