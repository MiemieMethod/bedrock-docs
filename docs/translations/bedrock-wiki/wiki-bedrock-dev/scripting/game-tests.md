---
title: 游戏测试
category: 教程
tags:
    - 实验性
mentions:
    - cda94581
    - SirLich
    - Joelant05
    - solvedDev
    - sermah
    - stirante
    - Paty007gr
    - JaylyDev
    - Fabrimat
    - Herobrine643928
    - kumja1
description: 游戏测试框架允许我们创建单元测试（“游戏测试”），使测试游戏机制是否正常工作变得更加容易。
---

::: warning
脚本 API 目前正在积极开发中，破坏性更改频繁。此页面假设使用 Minecraft 1.20.40 的格式。
:::

游戏测试框架允许我们创建单元测试（“游戏测试”），使测试游戏机制是否正常工作变得更加容易。

游戏测试可以与 `/gametest` 命令一起使用。

-   `/gametest runthis` - 运行范围内最近的游戏测试。
-   `/gametest runthese` - 运行范围内的所有游戏测试。
-   `/gametest pos` - 告诉您最近游戏测试的相对坐标。
-   `/gametest clearall [radius: int]` - 移除指定半径内的所有游戏测试。
-   `/gametest run <testName: GameTestName> [rotationSteps: int]` - 创建并运行指定的游戏测试。
-   `/gametest runset [tagTag: GameTestTag] [rotationSteps: int]` - 创建并运行所有带有指定标签的游戏测试。
-   `/gametest create <testName: string> [width: int] [height: int] [depth: int]` - 创建一个具有指定尺寸的空白游戏测试区域。
-   `/reload` - 从所有行为包重新加载所有功能和脚本文件。（1.19+）

（1.19.40+）原版游戏测试已从 Minecraft 游戏文件中移除，因此您无法在不添加自定义行为包的情况下运行任何游戏测试。您可以在 [**官方仓库**](https://github.com/microsoft/minecraft-gametests/tree/main/behavior_packs/vanilla_gametest) 中找到它们。

## 开始使用游戏测试

要开始，您需要拥有自己的行为包，并对脚本和 API 有一定的了解。如果您刚入门，可以查看 [这篇文章](../scripting/starting-scripts.md)。

要使用游戏测试框架，必须使用 `@minecraft/server-gametest` 模块。游戏测试 API 模块还需要 `@minecraft/server` 模块，因此在您的 manifest.json 中的依赖项需要如下所示：

<CodeHeader>BP/manifest.json/</CodeHeader>

```json
"dependencies": [
    {
        "module_name": "@minecraft/server",
        "version": "1.7.0-beta"
    },
    {
        "module_name": "@minecraft/server-gametest",
        "version": "1.0.0-beta"
    }
]
```

要运行游戏测试，您的行为包中需要一个结构文件，并且命令需要通过 `register` 函数进行注册。

<CodeHeader>BP/scripts/Main.js</CodeHeader>

```js
import * as GameTest from "@minecraft/server-gametest";

// 注册我们测试的代码
GameTest.register(
    "wiki",         // 测试类的名称。
    "simpleTest",   // 此测试的名称。
    (test) => {     // 测试的实现
        /**
         * @type {import("@minecraft/server").Vector3}
         * 牛应该生成的位置
         */
        const location = { x: 0, y: 0, z: 0 };
        const cow = test.spawn("minecraft:cow", location); // 返回实体实例

        test.succeedWhen(() => {
          test.assertEntityPresentInArea("minecraft:cow", true);
        });
    }
)
    .maxTicks(410)
    .structureName("mystructure:wiki"); /* 使用 wiki.mcstructure 文件 */
```

当命令被注册时，测试函数是锁定的，这意味着在命令注册后，测试函数无法访问测试函数外部的变量。

如果您在使用脚本 API 时遇到问题，可以查看 Microsoft Learn 中的 [**构建第一个游戏测试**](https://learn.microsoft.com/en-us/minecraft/creator/documents/gametestbuildyourfirstgametest) 文章，或者加入 **Bedrock 附加包** 以获取支持，您可以在 [有用链接](../meta/useful-links.md#discord-links) 页面找到它，以及其他各种资源！