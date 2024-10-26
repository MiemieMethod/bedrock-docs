---
title: 开始脚本编写
category: 常规
nav_order: 1
mentions:
    - cda94581
    - Herobrine643928
    - JaylyDev
    - SmokeyStack
    - kumja1
description: 在MCBE中开始脚本编写。
---

::: tip
本脚本API页面假设您对附加包的打包设置有基本了解。有关如何设置行为包的信息，请参阅[附加包简介](/guide/introduction)页面。
:::

::: warning
脚本API目前正在积极开发中，破坏性更改频繁。此页面假设使用的是Minecraft 1.21.20的格式。
:::

## 概述

脚本API（前称GameTests，且与[遗留脚本API](/scripting/scripting-intro)不同）是一项允许创建新类型创作的功能，这些创作使用行为包文件夹中的JavaScript文件构建。脚本API的某些部分并非实验性。

本页面将为您介绍Minecraft创作者API概念中您每天将使用的80%。

## 创建您的第一个项目

目前，脚本只能在行为包中使用。

在行为包的清单中，您需要添加一个`script`模块并为您的脚本项目设置一个`entry`点。目前，仅支持`"javascript"`作为有效语言。

<CodeHeader>BP/manifest.json#modules[0]</CodeHeader>

```json
{
    "uuid": "239c134f-67bf-4738-9bcc-8c69d31b1f72",
    "version": [1, 0, 0],
    "type": "script",
    "language": "javascript",
    "entry": "scripts/main.js"
}
```

此外，依赖项需要根据使用的模块进行设置。要导入和使用脚本API模块，您必须使用`module_name`和`version`指定依赖项。在此示例中，使用了`@minecraft/server`模块。

:::warning
存在一个错误，您无法将资源包应用于具有脚本模块的依赖项。

此问题导致Minecraft停止运行脚本并抛出与“未知依赖项”相关的错误。
:::

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
    "format_version": 2,
    "header": {
        "name": "基岩附加包",
        "description": "脚本API模板",
        "uuid": "<UUID>",
        "version": [0, 1, 0],
        "min_engine_version": [1, 20, 0]
    },
    "modules": [
        {
            "type": "script",
            "language": "javascript",
            "uuid": "<UUID>",
            // 您的入口文件；Minecraft将从中读取您的代码。
            "entry": "scripts/main.js",
            "version": [0, 1, 0]
        }
    ],
    // 如果您的代码中需要使用eval()和Function()，请在不必要时移除
    "capabilities": ["script_eval"],
    "dependencies": [
        {
            // 启用使用@minecraft/server模块，版本为1.13.0。
            "module_name": "@minecraft/server",
            "version": "1.13.0"
        },
        {
            // 启用使用@minecraft/server-ui模块，版本为1.2.0。
            "module_name": "@minecraft/server-ui",
            "version": "1.2.0"
        }
    ]
}
```

如果您的项目需要其他模块来运行代码，请按照上述格式添加其他依赖项。

**稳定API模块**，这些模块不需要启用Beta API实验。大多数功能包含在稳定API中，并且在Minecraft更新时不会破坏或更改。

-   `@minecraft/server`:

    -   [`1.13.0`](https://www.npmjs.com/package/@minecraft/server/v/1.13.0)（最新版本）
    -   [`1.12.0`](https://www.npmjs.com/package/@minecraft/server/v/1.12.0)
    -   [`1.11.0`](https://www.npmjs.com/package/@minecraft/server/v/1.11.0)
    -   [`1.10.0`](https://www.npmjs.com/package/@minecraft/server/v/1.10.0)
    -   [`1.9.0`](https://www.npmjs.com/package/@minecraft/server/v/1.9.0)
    -   [`1.8.0`](https://www.npmjs.com/package/@minecraft/server/v/1.8.0)
    -   [`1.7.0`](https://www.npmjs.com/package/@minecraft/server/v/1.7.0)
    -   [`1.6.0`](https://www.npmjs.com/package/@minecraft/server/v/1.6.0)
    -   [`1.5.0`](https://www.npmjs.com/package/@minecraft/server/v/1.5.0)
    -   [`1.4.0`](https://www.npmjs.com/package/@minecraft/server/v/1.4.0)
    -   [`1.3.0`](https://www.npmjs.com/package/@minecraft/server/v/1.3.0)
    -   [`1.2.0`](https://www.npmjs.com/package/@minecraft/server/v/1.2.0）
    -   [`1.1.0`](https://www.npmjs.com/package/@minecraft/server/v/1.1.0)
    -   [`1.0.0`](https://www.npmjs.com/package/@minecraft/server/v/1.0.0)

-   `@minecraft/server-ui`:
    -   [`1.2.0`](https://www.npmjs.com/package/@minecraft/server-ui/v/1.2.0)（最新版本）
    -   [`1.1.0`](https://www.npmjs.com/package/@minecraft/server-ui/v/1.1.0）
    -   [`1.0.0`](https://www.npmjs.com/package/@minecraft/server-ui/v/1.0.0)（需要`@minecraft/server@1.2.0`）

**Beta API模块**，需要在世界设置中启用Beta API实验，并添加许多实验性功能。这些API可能会在没有太多警告的情况下更改、删除或添加，并且容易出现问题。请注意！

-   `@minecraft/server`:

    -   [`1.14.0-beta`](https://www.npmjs.com/package/@minecraft/server/v/1.14.0-beta.1.21.20-stable)

-   `@minecraft/server-ui`:
    -   [`1.3.0-beta`](https://www.npmjs.com/package/@minecraft/server-ui/v/1.3.0-beta.1.21.20-stable)
-   `@minecraft/server-gametest`:

    -   [`1.0.0-beta`](https://www.npmjs.com/package/@minecraft/server-gametest/v/1.0.0-beta.1.21.20-stable)

-   `@minecraft/server-net`:

    -   [`1.0.0-beta`](https://www.npmjs.com/package/@minecraft/server-net/v/1.0.0-beta.1.21.20-stable)（仅限基岩专用服务器模块，必须在`permission.json`中启用，因为默认情况下未启用）

-   `@minecraft/server-admin`:

    -   [`1.0.0-beta`](https://www.npmjs.com/package/@minecraft/server-admin/v/1.0.0-beta.1.21.20-stable)（仅限基岩专用服务器模块）

为了在您的代码中使用`eval()`函数或`Function()`构造函数，您可以在清单功能中添加以下内容：

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
    "capabilities": ["script_eval"]
}
```

入口文件可以包含脚本和/或导入其他脚本文件。只能指定一个入口文件。

## 使用JS编写脚本

Minecraft的脚本引擎仅运行JavaScript，类似于其他JavaScript项目。请查看[使用TypeScript编写脚本](/scripting/typescript#script-api)以将TS直接编译为JavaScript。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
// 此文件演示代码是否正常工作，通过
// 在聊天中重复发送“Hello World”

// 从“@minecraft/server”导入世界和系统组件，用于世界和游戏逻辑。
import { world, system } from "@minecraft/server";

// 创建并运行一个每个Minecraft滴答调用的间隔
system.runInterval(() => {
    // 使用API中的world.sendMessage函数向聊天发送“Hello World”
    world.sendMessage("Hello World");
}, 1);
```

## 参考文档

官方文档托管在Microsoft Learn上，可以在此找到：

-   [`@minecraft/server`](https://learn.microsoft.com/minecraft/creator/scriptapi/mojang-minecraft/mojang-minecraft)
-   [`@minecraft/server-gametest`](https://learn.microsoft.com/minecraft/creator/scriptapi/mojang-gametest/mojang-gametest)
-   [`@minecraft/server-ui`](https://learn.microsoft.com/minecraft/creator/scriptapi/mojang-minecraft-ui/mojang-minecraft-ui)
-   [`@minecraft/server-admin`](https://learn.microsoft.com/minecraft/creator/scriptapi/mojang-minecraft-server-admin/mojang-minecraft-server-admin)
-   [`@minecraft/server-net`](https://learn.microsoft.com/minecraft/creator/scriptapi/mojang-net/mojang-net)

最新Beta API模块的官方TypeScript声明可以在此找到：

-   [`@minecraft/server`](https://www.npmjs.com/package/@minecraft/server/v/beta)
-   [`@minecraft/server-gametest`](https://www.npmjs.com/package/@minecraft/server-gametest/v/beta)
-   [`@minecraft/server-ui`](https://www.npmjs.com/package/@minecraft/server-ui/v/beta)
-   [`@minecraft/server-admin`](https://www.npmjs.com/package/@minecraft/server-admin/v/beta)
-   [`@minecraft/server-net`](https://www.npmjs.com/package/@minecraft/server-net/v/beta)

这些可以在您的编辑器中提供增强的自动补全和验证。

-   bridge. v2：内置GameTest支持。
-   Visual Studio Code：安装Node.js和npm，然后在命令行中运行以下命令：

最新Beta API模块：

```bash
npm i @minecraft/server@1.14.0-beta.1.21.20-stable
npm i @minecraft/server-ui@1.3.0-beta.1.21.20-stable
npm i @minecraft/server-gametest@1.0.0-beta.1.21.20-stable
npm i @minecraft/server-admin@1.0.0-beta.1.21.20-stable
npm i @minecraft/server-net@1.0.0-beta.1.21.20-stable
```

最新稳定API模块：

```bash
npm i @minecraft/server@1.13.0
npm i @minecraft/server-ui@1.2.0
```