---
title: 解释附加包
category: 指南
description: 附加包的基础知识
---

/// details-info | 署名信息
- 该页面翻译自[https://wiki.bedrock.dev/guide/addons.html](https://wiki.bedrock.dev/guide/addons.html)
- 该页面仓库地址为[https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/addons.md](https://github.com/Bedrock-OSS/bedrock-wiki/blob/wiki/docs/guide/addons.md)
- 该页面的版本为<!-- md:samp Bedrock-OSS/bedrock-wiki@9ad60cd0a2743e3ed5a7aa2af010e4e5987e218b -->
- 该页面的作者有：
    - <!-- md:samp @SirLich -->
    - <!-- md:samp @Dreamedc2015 -->
    - <!-- md:samp @sermah -->
    - <!-- md:samp @cda94581 -->
    - <!-- md:samp @RedSmarty -->
    - <!-- md:samp @TheItsNameless -->
    - <!-- md:samp @MedicalJewel105 -->
    - <!-- md:samp @ChibiMango -->
    - <!-- md:samp @profeplaysminecraft -->
    - <!-- md:samp @retr0cube -->
    - <!-- md:samp @SmokeyStack -->
    - <!-- md:samp @QuazChick -->
///

## 什么是附加包？

附加包允许我们通过*修改*或*移除*现有内容以及*添加*我们自己的内容来修改我们的Minecraft体验。附加包非常强大，允许我们创建自定义实体、物品和方块，以及自定义战利品表和合成配方等内容。你的想象力是唯一的限制！

附加包主要使用[json](../guide/understanding-json.md)编写，这是一种结构化的数据格式。附加包本质上是一个包含json文件、图像和声音的集合，以某种方式修改或添加到游戏中。

/// tip | JavaScript编程
自本指南编写以来，“附加包”的定义已扩展到包括JavaScript脚本API。你可以在本网站的其他地方了解更多关于此API的信息。
///

## 行为包与资源包有什么区别？

附加包分为两种包类型：资源包和行为包。两者可以独立运行，但通常是一起使用的。当你同时拥有资源包和行为包时，这被称为*附加包*。

### 资源包

资源包，也称为*客户端*或RP，负责附加包中的*视觉*和*声音*。这包括以下内容：

- 纹理
- 声音
- 几何体
- 动画
- 粒子

### 行为包

行为包，也称为*服务端*或BP，负责附加包的*逻辑*。这可以包括以下内容：

- 实体的行为
- 合成配方
- 战利品表
- 自定义功能

### 包之间的通信

在大多数情况下，你会同时拥有RP和BP。这些包可以相互通信，或者需要彼此才能正常工作，因为在一个包中定义的资源可以在另一个包中访问。例如，在创建自定义实体时，你需要两个文件：

- 一个RP实体定义，描述你的实体将*看起来*如何
- 一个BP实体定义，描述你的实体将如何*行动*

## 下一步

/// tip | 你所学到的

- [x] 附加包可以用于修改Minecraft内容或添加自己的内容
- [x] 附加包使用json编写
- [x] 附加包分为**资源包**和**行为包**：
    - 资源包包含纹理、声音等，并控制游戏的外观
    - 行为包包含实体文件、合成配方等，并控制游戏的逻辑

///

[下一步：软件和准备](./software-preparation.md){ .md-button }