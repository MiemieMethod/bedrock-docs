---
title: "阻止方块放置（稳定版）"
mentions:
    - JWForever5504
category: 教程
description: 通过脚本阻止方块放置。
---

本教程分为两个部分：一个是稳定方法，一个是测试版方法。你可以根据使用的脚本 API 版本独立使用这两个部分。

::: warning
脚本 API 当前正在积极开发中，可能会频繁发生重大更改。本页面假设使用的是 Minecraft 1.21.20 的格式。
:::

是否曾经需要阻止特定方块的放置？在 1.20.10 中，一些危险的不可获取方块可以被获取，因此你可以使用此脚本来保护你的世界或服务器！

## 设置

::: tip
在创建脚本之前，建议先学习 JavaScript、附加包和脚本 API 的基础知识。要了解脚本 API 的功能，请参见 [Microsoft 文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/)。
:::

与其他脚本一样，你需要在 `manifest.json` 中添加依赖项。我们使用的是 `@minecraft/server` 模块，具体版本为 `1.14.0-beta`。

```json title="manifest.json"
{
    "format_version": 2,
    "header": {
        "name": "阻止方块放置",
        "description": "使用脚本 API 阻止某些方块的放置",
        "uuid": "6f3a4325-4ce5-42f5-b141-12641c8823c3",
        "min_engine_version": [1, 20, 10],
        "version": [1, 0, 0]
    },
    "modules": [
        {
            "description": "行为包模块",
            "type": "data",
            "uuid": "5a080d1d-bef8-47ce-aae1-a2ec3e0010ab",
            "version": [1, 0, 0]
        },
        {
            "description": "游戏测试模块",
            "type": "script",
            "language": "javascript",
            "entry": "scripts/main.js",
            "uuid": "53a5804b-fb35-4f7d-a89e-e4a925fadb77",
            "version": [1, 0, 0]
        }
    ],
    "dependencies": [
        {
            // Minecraft 原生模块 - 需要使用 "@minecraft/server" 模块
            "module_name": "@minecraft/server",
            "version": "1.14.0-beta"
        }
    ]
}
```

在我们的清单中，我们添加了脚本模块。`entry` 是我们的脚本文件存储的位置，位于行为包的 `scripts` 文件夹中。依赖项使我们能够在代码中使用所需的脚本模块。

<FolderView
	:paths="[
		'BP/manifest.json',
		'BP/pack_icon.png',
        'BP/scripts/main.js'
	]"
/>

## 第一个预防措施（稳定版）

即使你打算使用其他方块，如果这是你第一次创建此脚本，请严格按照教程进行。在确认脚本正确后，你可以更改方块。

这是因为方块的标识符通常与你想象的不同。例如，发光物品框在内部被称为 `minecraft:glow_frame`。

我们将首先添加将在代码中使用的模块导入。

```js title="BP/scripts/main.js"
import { world, system } from "@minecraft/server";
```

::: tip
了解更多关于 `system` 的信息，请访问 [系统事件](../scripting/script-server.md#events)。
:::

添加模块后，我们将添加阻止方块放置的措施。

```js title="BP/scripts/main.js"
world.beforeEvents.playerPlaceBlock.subscribe((event) => {
    const player = event.source;
    if (event.permutationBeingPlaced.type.id === "minecraft:bedrock") {
        event.cancel = true;
        system.run(() => {
            player.sendMessage("你无法放置基岩");
        });
    }
});
```

这是执行我们代码的主要功能。`world.beforeEvents.playerPlaceBlock.subscribe()` 将在任何方块放置之前运行。

-   `const player = event.source;` 将变量 `player` 定义为事件的源（放置方块的玩家）。使用 `const` 而不是 `var` 或 `let` 表示该源 _不能_ 被更改，并且是常量。
-   `if()` 语句要求条件评估为真，以便括号内的代码运行。
    -   `event.permutationBeingPlaced.type.id === 'minecraft:bedrock'` 验证正在放置的方块是否为 'minecraft:bedrock'。
    -   `event.block.typeId != "minecraft:frame" && event.block.typeId != "minecraft:glow_frame"` 检查目标方块不是物品框，以便被取消放置的方块仍然可以放置在物品框中。
-   `event.cancel = true;` 取消该事件将执行的放置操作。
-   `system.run()` 是一个系统调用，告诉 Minecraft 将正在运行的代码推送到下一个游戏刻。这是必要的，因为在事件之前无法修改世界状态（在我们的例子中是向玩家发送消息），使用系统运行使代码不受此限制。有关系统回调和循环的更多信息，请参见 [这里](https://learn.microsoft.com/en-us/minecraft/creator/documents/systemrunguide)。
-   `player.sendMessage()` 向玩家发送一条消息，告知他们无法放置该方块。

## 结论（稳定版）

消息 `你无法放置基岩` 可以根据需要修改或替换为你自己的逻辑。

你还可以更改在 `event.permutationBeingPlaced.type.id === 'minecraft:bedrock'` 中检查的方块的 typeId。将命名空间和标识符替换为 `minecraft:bedrock`。

要了解更多关于脚本 API 的信息，你可以查看 [维基](../scripting/starting-scripts.md) 或 [Microsoft 文档](https://learn.microsoft.com/en-us/minecraft/creator/documents/scriptdevelopertools)。