---
title: API 模块
category: 一般
nav_order: 3
mentions:
    - cda94581
    - ConsoleTerm
---

## 概述
脚本 API 提供了供开发者与 Minecraft 互动的模块。此外，基于你在附加包中使用的模块，清单依赖项也需要进行设置。

|             模块名称              |                  UUID                  |      之前的名称别名      |  首个模块版本  |
| --------------------------------- | -------------------------------------- | ------------------------ | ---------------- |
| `@minecraft/common`               | `77ec12b4-1b2b-4c98-8d34-d1cd63f849d5` |                          | `引擎 1.20.40`   |
| `@minecraft/debug-utilities`      | `1796ea86-0daf-4409-99ee-fd6467cf1203` |                          | `引擎 1.20.70`   |
| `@minecraft/server`               | `b26a4d4c-afdf-4690-88f8-931846312678` | `Minecraft`, `mojang-minecraft` | `引擎 1.16.210`  |
| `@minecraft/server-ui`            | `2bd50a27-ab5f-4f40-a596-3641627c635e` | `mojang-minecraft-ui`    | `引擎 1.18.20`   |
| `@minecraft/server-gametest`      | `6f4b6893-1bb6-42fd-b458-7fa3d0c89616` | `GameTest`, `mojang-gametest` | `引擎 1.16.210`  |
| `@minecraft/server-net`           | `777b1798-13a6-401c-9cba-0cf17e31a81b` | `mojang-net`             | `引擎 1.19.10`   |
| `@minecraft/server-admin`         | `53d7f2bf-bf9c-49c4-ad1f-7c803d947920` | `mojang-minecraft-server-admin` | `引擎 1.19.10`   |
| `@minecraft/server-editor-bindings` | `8518d9c7-a1f5-4bf3-acc7-78e87df595fc` |                          | `引擎 1.19.80`   |
| `@minecraft/server-editor`        | `1d565354-296d-11ed-a261-0242ac120002` |                          | `引擎 1.19.80`   |

## 模块描述

### `@minecraft/common`

此模块的稳定版本较少，可以在不提及依赖项的情况下导入。它是一个包含基本资源的模块，例如错误类或接口。

### `@minecraft/debug-utilities`

这是一个实验性模块。此模块提供调试工具，但不应在附加包的公共版本中使用。

### `@minecraft/server`

此模块有很多稳定版本，但仍在积极开发中。它是服务器端附加包脚本的基石，旨在实现脚本引擎与你的世界之间的交互，例如区块、实体、物品、玩家和其他世界资源。

### `@minecraft/server-ui`

这是一个相对较小的模块，但对于服务器与你包的最终用户之间的交互非常有用。该模块提供通过可自定义表单向玩家发送数据的功能。

### `@minecraft/server-gametest`

这是目前存在的最旧模块，但没有一个稳定版本。此模块用于测试原版实验，以确保与其他自定义内容的兼容性、捕捉边缘案例或确保可重复性。此模块不适合内容创作者，也无需保证与稳定版本的向后兼容性。

### `@minecraft/server-net`

此模块仅允许在 [基岩专用服务器](https://www.minecraft.net/en-us/download/server/bedrock) 上使用，因为它可能会威胁到常见附加包用户的安全。此模块可以通过 GET、SET、POST 等网络请求访问互联网。此模块仅以实验形式存在。

### `@minecraft/server-admin`

此模块也仅允许在 [基岩专用服务器](https://www.minecraft.net/en-us/download/server/bedrock) 上使用。该模块负责处理存储在 JSON 管理文件中的基本数据，旨在设置包的行为而不干扰原始包。此模块仅以实验形式存在。

### `@minecraft/server-editor-bindings`

这是一个为编辑器模块提供的特殊本地函数集，此模块没有文档，不应被创作者使用，然而如果你在依赖项中引用它，可以导入此模块，但只能在作为编辑器项目创建的世界中使用。

### `@minecraft/server-editor`

此模块是特殊的，因为它的实现不是本地的，而是一个 JS 模块，尽管它是用 JS 实现的，因此其存在是硬编码的，但可以在依赖项中引用，但只能在作为编辑器项目创建的世界中使用。

## Alpha 版本
Alpha 版本是模块的过时版本，此版本不应在当前附加包中使用，并标记为实验性，只有两个模块具有此 alpha 版本，`@minecraft/server` 当时称为 `mojang-minecraft` 和 `@minecraft/server-gametest` 当时称为 `mojang-gametest`。如果你想尝试使用此版本，请记住它们只能在这些名称下导入。

### Alpha 2.X
现在你还可以注意到新的 alpha `2.X` 系列，但这与原始 alpha 版本不同，它也是一个实验版本，但可以在今天已知的名称下轻松导入，请记住，此版本与之前的 `1.X` 系列不兼容。

## 模块引用

模块引用是导入模块到你的 JS 代码中的必要条件。

::: warning
请勿在依赖项中同时使用 `"uuid"` 和 `"module_name"` 属性，选择其一即可。
:::

以下是 `@minecraft/server` 版本为 `1.13.0` 的示例。
<CodeHeader>BP/manifest.json#dependencies[0]</CodeHeader>

```json
{
	"module_name": "@minecraft/server",
	"version": "1.13.0"
}
```

标记你的包为编辑器扩展所需的能力，在这种情况下允许使用编辑器模块。

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
	"capabilities": [
		"editorExtension"
	]
}
```