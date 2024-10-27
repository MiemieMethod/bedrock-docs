---
title: 简单聊天命令
category: 教程
tags:
    - 实验性
mentions:
    - cda94581
    - FrankyRay
    - destruc7ion
    - jannik-de
    - riesters
    - Fabrimat
    - SmokeyStack
    - CrackedMatter
    - JaylyDev
    - Herobrine643928
    - ConsoleTerm
    - kumja1
    - modmaker101
    - AmethystDevbyFK
description: 使用脚本创建自定义命令。
---

::: warning
脚本 API 目前正在积极开发中，破坏性更改频繁。此页面假设使用 Minecraft 1.21.30 的格式。
:::

谁不想要酷炫的自定义命令呢？通过脚本 API，您可以创建自己的命令。在本文中，我们将使用脚本 API 创建这些命令。

## 设置包

:::tip
在创建脚本之前，建议先学习 JavaScript、附加包和脚本 API 的基础知识。要了解脚本 API 的功能，请参见 [Microsoft 文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/)
:::

假设您已经理解了脚本的基础知识，让我们开始创建包。

<CodeHeader>manifest.json</CodeHeader>

```json
{
	"format_version": 2,
	"header": {
		"name": "自定义命令",
		"description": "使用脚本 API 的自定义命令",
		"uuid": "c8c3239f-027f-4e80-890f-880eba65027d",
		"min_engine_version": [1, 19, 40],
		"version": [1, 0, 0]
	},
	"modules": [
		{
			"description": "行为包模块",
			"type": "data",
			"uuid": "cd2cd41a-1849-410e-8f0a-5d30fde4bd9a",
			"version": [1, 0, 0]
		},
		{
			"description": "游戏测试模块",
			"type": "script",
			"language": "javascript",
			"entry": "scripts/main.js",
			"uuid": "f626740d-50a6-49f1-a24a-834983b72134",
			"version": [1, 0, 0]
		}
	],
	"dependencies": [
		{
			"module_name": "@minecraft/server",
			"version": "1.15.0-beta" // 需要是最新版本，否则会出现问题（截至 1.21.30 的最新版本）
		}
  ]
}
```

在我们的清单中，我们添加了脚本模块。`entry` 是我们的脚本文件存储的位置。通常在行为包的 `scripts` 文件夹中。依赖项允许我们在脚本中使用该脚本模块。

<FolderView
	:paths="[
		'BP/manifest.json',
		'BP/pack_icon.png',
        'BP/scripts/main.js'
	]"
/>

## 创建自定义命令

现在进入有趣的部分 - 创建我们的自定义命令。首先，我们将添加模块。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
import { world } from '@minecraft/server';
```

接下来，我们将添加简单的命令，例如 `!gmc` 用于将游戏模式更改为创造模式，`!gms` 用于更改为生存模式。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
world.beforeEvents.chatSend.subscribe((eventData) => {
	const player = eventData.sender;
	switch (eventData.message) {
		case '!gmc':
			eventData.cancel = true;
			player.runCommandAsync('gamemode c');
			break;
		case '!gms':
			eventData.cancel = true;
			player.runCommandAsync('gamemode s');
			break;
		default: break;
	}
});
```

这是执行我们命令的主要功能。`world.beforeEvents.chatSend.subscribe()` 将在聊天消息发送之前运行。

-   `switch` 语句遍历可能的选项，如果匹配，则运行代码直到下一个 `break` 语句。
-   `eventData.cancel = true` 将取消将要发送的聊天消息 - 类似于原版命令的工作方式。
-   `const player = eventData.sender` 声明变量 `player` 以供后续使用。
-   `player.runCommandAsync('gamemode c')` 在消息发送者上运行命令。

## 限制标签的命令使用

此功能将始终检查玩家是否输入特殊消息以激活命令，即使玩家不应有访问权限。为防止这种情况，我们可以使用标签将这些命令限制为特定人员。

例如，让我们使我们的命令仅对拥有 `Admin` 标签的玩家可用。

<CodeHeader>BP/scripts/main.js</CodeHeader>

```js
import { world } from "@minecraft/server";

world.beforeEvents.chatSend.subscribe((eventData) => {
	const player = eventData.sender;
	if (!player.hasTag('Admin')) return;
	switch (eventData.message) {
		case '!gmc':
			eventData.cancel = true;
			player.runCommandAsync('gamemode c');
			break;
		case '!gms':
			eventData.cancel = true;
			player.runCommandAsync('gamemode s');
			break;
		default: break;
	}
});
```

用简单的话来说，`if (!eventData.sender.hasTag('Admin')) return;` 的意思是：“如果玩家没有 (`!`) 'Admin' 标签，则停止脚本继续执行 (`return`)”

有关脚本 API 的更多信息，您可以参考 [wiki](../scripting/starting-scripts.md) 或 [Microsoft 文档](https://docs.microsoft.com/en-us/minecraft/creator/documents/gametestgettingstarted)