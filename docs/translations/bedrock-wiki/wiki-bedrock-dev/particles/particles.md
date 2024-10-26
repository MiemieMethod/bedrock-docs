---
title: "粒子介绍"
category: 一般
tags:
    - 指南
mentions:
    - SirLich
    - MedicalJewel105
    - TheItsNameless
description: Minecraft基岩版粒子介绍。
---

## 粒子系统

[粒子系统](https://www.wikiwand.com/en/Particle_system)是一种在游戏物理、运动图形和计算机图形中使用的技术，它利用许多小精灵来创建逼真的效果，如烟雾、火焰或昆虫群。您可以通过使用自定义纹理和运动逻辑在Minecraft基岩版中创建新的粒子系统。这使得粒子变得非常有趣和强大！

粒子中的MoLang集成也非常成熟，这允许您在不同粒子之间，或在实体与粒子之间传递数据。

### 粒子

“粒子”或“粒子实例”是一个放置在三维空间中的单个精灵（纹理），并具有自己的移动和外观变化逻辑。粒子的示例包括：

-   一片雪花
-   一滴雨水
-   一缕烟雾

### 发射器

“发射器”或“粒子发射器”是一个可以生成许多粒子的系统，可以是一次性生成（爆炸），也可以是逐渐生成（稳定）。发射器具有自己的移动逻辑、生成粒子的数量和位置。发射器的示例包括：

-   一场暴风雪（生成雪花）
-   一场雨storm（生成雨滴）
-   一根冒烟的烟囱（生成烟雾）

## 创建您的第一个粒子

要创建一个粒子，您需要一个资源包、一个纹理和一个粒子定义文件：

<FolderView
:paths="[
    'RP/particles/snowflake.json',
    'RP/textures/particles/snowflake.png'
]"
> </FolderView>
 
您可以使用[Snowstorm](https://jannisx11.github.io/snowstorm/)来创建粒子。