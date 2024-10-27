---
title: 软件与准备
category: 指南
description: 如何设置开发环境
nav_order: 3
prefix: "3. "
mentions:
    - SirLich
    - Dreamedc2015
    - sermah
    - cda94581
    - Joelant05
    - MedicalJewel105
    - TheItsNameless
    - TheDoctor15
    - ChibiMango
    - profeplaysminecraft
    - solvedDev
    - retr0cube
    - SmokeyStack
    - ThomasOrs
---

在开始创建附加包之前，您需要先安装所需的工具和应用程序。虽然在Windows 10上进行开发会更为方便，但我们也提供了适用于Android和iOS的移动替代方案（如适用）。

本页面将为您提供需要安装的软件列表以及设置的配置提示。

## 下载Minecraft基岩版

-   [Windows 10](https://www.microsoft.com/en-us/p/minecraft-for-windows-10/9nblggh2jhxj?activetab=pivot:overviewtab)
-   [Android](https://play.google.com/store/apps/details?id=com.mojang.minecraftpe&hl=en)
-   [iOS](https://apps.apple.com/us/app/minecraft/id479516143)
-   [在Linux上运行MC](https://discord.gg/VJTZ3KaTx6)

## 选择编辑器

附加包可以使用任何文本编辑器创建，但在专用编辑器中工作会更加舒适。一个好的编辑器可以提供代码补全、错误检测和内置文档。

关于初学者最佳编辑器的看法各不相同，但一般来说，选择VSCode或bridge都不会出错。如果您使用移动设备，则需要使用移动替代方案。

### VSCode

VSCode是一个通用文本编辑器和集成开发环境（IDE）。使用VSCode，您可以以纯文本编辑附加包，并借助强大的扩展和附加包进行指导。VSCode是程序员和高级用户的绝佳选择。

[⚙️安装VSCode](https://code.visualstudio.com/)

<Spoiler title="配置VSCode">

许多VSCode的插件使得编辑附加包更加容易：

-   [Blockception的Minecraft基岩开发](https://marketplace.visualstudio.com/items?itemName=BlockceptionLtd.blockceptionvscodeminecraftbedrockdevelopmentextension)
-   [.mcfunction支持](https://marketplace.visualstudio.com/items?itemName=arcensoth.language-mcfunction)
-   [.lang支持](https://marketplace.visualstudio.com/items?itemName=zz5840.minecraft-lang-colorizer)
-   [基岩定义](https://marketplace.visualstudio.com/items?itemName=destruc7i0n.vscode-bedrock-definitions)
-   [Prettify-json](https://marketplace.visualstudio.com/items?itemName=mohsen1.prettify-json)
-   [拼写检查器（用于编写维基）](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
-   [雪暴粒子编辑器](https://marketplace.visualstudio.com/items?itemName=JannisX11.snowstorm)
-   [UUID生成器](https://marketplace.visualstudio.com/items?itemName=netcorext.uuid-generator)

</Spoiler>

### bridge.

[bridge.](https://bridge-core.app/)是一个轻量级的专用IDE，用于Minecraft附加包开发。它具有[创新功能](https://bridge-core.app/guide/features/)，如[实体和区块预览](https://bridge-core.app/guide/features/index.html#file-previews)、[丰富的自动补全和文件验证](https://bridge-core.app/guide/features/index.html#auto-completions-and-validation)以及[带预设的高级文件创建](https://bridge-core.app/guide/features/index.html#advanced-file-creation)。bridge.包括一个常规文本编辑器，适合经验丰富的附加包创建者，以及一个树形编辑器，方便初学者开始编辑JSON文件。

<Spoiler title="配置Bridge">

-   [了解更多关于使用bridge.的原因](https://bridge-core.app/guide/why-bridge)
-   [阅读我们的bridge入门指南](https://bridge-core.app/guide/index)
-   [在线试用bridge.](https://editor.bridge-core.app/)

</Spoiler>

### 移动编辑器

#### Android

-   [ACode编辑器](https://play.google.com/store/apps/details?id=com.foxdebug.acodefree)
-   [bridge. v2](https://bridge-core.app/)

#### iOS

-   [Kodex](https://apps.apple.com/us/app/kodex/id1038574481)
-   [bridge. v2](https://bridge-core.app/)

## Blockbench

-   [Blockbench](https://blockbench.net/)是一个“方形3D模型编辑器”，通常用于创建Minecraft模型、纹理和动画。还提供与移动设备兼容的网页版本。

## 图像编辑器

选择图像编辑器时，重要的是要记住传统的Minecraft风格由简单的16x16像素艺术组成。有许多强大且免费的艺术程序可供您使用。然而，许多这些程序的工具超出了您在Minecraft图形设计中所需的范围，并且这些工具需要时间去学习。

:::tip
选择一个让您感到舒适且易于使用的程序。许多附加包创建者会为不同的任务使用不同的艺术程序。（例如：一个人可能会使用paint.net进行大部分艺术创作，而使用piskel进行Minecraft区块动画）。选择最适合您的工具！
:::

### Krita

Krita是一个强大的开源艺术程序，旨在为艺术家提供免费的强大数字艺术工具。Krita拥有足够的功能来满足您的Minecraft需求，并可在MAC或PC上运行。

-   **+ 优点：**功能丰富，包括直观用户界面的像素画笔。
-   **- 缺点：**需要一些时间来熟悉工具。

[下载Krita](https://krita.org/en/)

### GIMP

GIMP与Krita类似，是一个免费的开源数字艺术程序，拥有丰富的工具。Krita更侧重于插图，而GIMP则更侧重于图像处理（类似于Photoshop）。GIMP同样可以在MAC或PC上运行。

-   **+ 优点：**GIMP拥有足够的工具来编辑Minecraft艺术作品。
-   **- 缺点：**界面不够直观。尽管GIMP功能强大，但学习曲线较陡峭。

[下载GIMP](https://www.gimp.org/)

### Paint.net

Paint.net是一个简单但功能强大的图像编辑和艺术软件。Paint.net可能没有Krita和GIMP那样丰富的工具，但它提供了简单易用的体验。

-   **+ 优点：**易于使用和学习。
-   **- 缺点：**仅适用于Windows。

[下载Paint.net](https://www.getpaint.net)

### Pixilart

Pixilart是一个基于网页的像素艺术软件。由于专注于像素艺术，它非常简单易用。它还具有强大的调整大小选项，可以在不失去像素艺术细节的情况下调整您的艺术作品大小。

-   **+ 优点：**易于使用和学习。专门为像素艺术设计。
-   **- 缺点：**必须连接互联网。可能缺少您所需的工具。

[使用Pixilart](https://www.pixilart.com/)

### Piskel

Piskel是一个基于网页的像素艺术软件，专注于制作像素化的精灵（或视频游戏角色动画）。这个工具与Pixilart类似，简单易用。它也是制作翻页书（Minecraft区块或皮肤动画）的绝佳工具。

-   **+ 优点：**易于使用和学习。非常适合翻页动画。
-   **- 缺点：**必须连接互联网。仅提供最基本的工具。

[下载Piskel](https://www.piskelapp.com/)

### Libresprite

LibreSprite是一个免费的开源程序，用于创建和动画您的精灵。基于最后一个GPLv2提交的aseprite。

-   **+ 优点：**基本且易于使用，可定制，专为像素艺术家设计。
-   **- 缺点：**可能无法在Mac上运行，仅由小型社区维护。

## 附加材料

:::tip
本指南将引导您完成附加包开发的初始阶段，但并不全面！要了解更多关于附加包的信息，您需要使用和参考其他信息来源，我们将在此处提供链接。
:::

### 加入Discord

获取本指南帮助的最佳地方是加入[Discord服务器](/discord)(s)。

### 原版包

Minecraft的原版文件是很好的参考材料。您应下载这些包，并将其存储在计算机上的方便位置。当您需要某个物品、实体或动画的示例时，可以参考这些文件以获取灵感。

-   [原版包](https://github.com/Mojang/bedrock-samples/releases)

### 文档

有许多良好的附加包文档来源。熟悉所有这些文档，并考虑将其添加到书签中。

-   [bedrock.dev](https://bedrock.dev/): 参考文档。
-   [wiki.bedrock.dev](https://wiki.bedrock.dev/): 教程和指南。
-   [MS Docs](https://docs.microsoft.com/en-us/minecraft/creator/): 官方微软附加包创作者门户。

### 故障排除与额外帮助

-   如果JSON格式对您来说非常棘手，可以考虑阅读[理解JSON指南](../guide/understanding-json.md)。
-   如果您遇到奇怪的错误，可以考虑阅读[故障排除指南](../guide/troubleshooting.md)。
-   您可以在[这里](../meta/useful-links.md)探索其他工具。

## 下一步

:::tip 您所学到的

-   [x] 安装了必要的软件
-   [x] 下载了原版示例文件
-   [ ] 找到您的`com.mojang`文件夹并创建附加包的工作区。
-   [ ] 为您的第一个附加包创建清单和包图标。

:::

<Button link="../guide/project-setup.md">下一步：项目设置</Button>