---
title: 高级清单
category: 额外
description: 如何使用清单 - 更详细的指南 [建设中]
nav_order: 4
prefix: 'd. '
mentions:
    - MRBBATES1
    - Luthorius
    - SirLich
    - smell-of-curry
    - MedicalJewel105
    - QuazChick
---

/// tip
这是一个附录页面。你可以从[这里](../guide/index.md)开始阅读指南。
///

本页面旨在详细介绍manifest.json文件，我们将更深入地讨论UUID是什么以及如何添加它们。我们将解释依赖项的使用、不同的格式版本以及如何包含元数据。

我们还将讨论行为包、资源包和皮肤包之间的版本差异。

## UUID

UUID是通用唯一标识符（Universal Unique Identifier）的缩写，共有5个UUID版本以及一个常见的非官方版本。UUID是一个包含数字、字母和破折号的36个字符字符串。

Minecraft使用版本4：变体1，这完全是随机的。这就是你在Minecraft中创建包的唯一标识。

### 如何生成正确的UUID

你可以使用在线网站，如[UUID生成器](https://www.uuidgenerator.net/version4/)和[UUID工具](https://www.uuidtools.com/generate/v4)来生成Minecraft所需的正确版本。

##

### UUID常见问题

-   **UUID区分大小写吗？**

    -   _不，UUID以16进制书写，使用数字0-9和字符a-f。大小写字母没有区别。_

-   **我可以为头部和模块使用相同的UUID吗？**
    -   _不，头部和模块的UUID需要不同。_

/// warning
本页面正在建设中！
///