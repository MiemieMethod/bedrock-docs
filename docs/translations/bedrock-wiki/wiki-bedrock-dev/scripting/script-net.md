---
title: 脚本请求API
category: 教程
tags:
    - 实验性
mentions:
    - JaylyDev
    - ConsoleTerm
    - SmokeyStack
    - ThomasOrs
description: 基岩版专用服务器的脚本请求API。
---

::: warning
脚本API目前正在积极开发中，可能会频繁发生破坏性更改。本页面假设使用Minecraft 1.21.20的格式。
:::

::: warning
此模块仅可在基岩版专用服务器上使用。
:::

在脚本API中，你可以发送和接收基于HTTP的请求与互联网进行交互。有关更详细的信息，请访问[Microsoft文档](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/minecraft-server-net)。

## 设置

**依赖项**

与其他模块一样，你需要在`manifest.json`中添加依赖项。

```json
{
	"dependencies": [
		{
			"module_name": "@minecraft/server-net",
			"version": "1.0.0-beta"
		}
	]
}
```

## 在基岩版专用服务器中启用模块

1. 从[Minecraft官网](https://www.minecraft.net/en-us/download/server/bedrock)下载基岩版专用服务器包。

2. 将压缩文件解压到一个文件夹中。

这是默认基岩版专用服务器的目录结构：

<FolderView :paths="[
	'BedrockServer/behavior_packs',
	'BedrockServer/config/default/permissions.json',
	'BedrockServer/definitions',
	'BedrockServer/development_behavior_packs',
	'BedrockServer/development_resource_packs',
	'BedrockServer/development_skin_packs',
	'BedrockServer/resource_packs',
	'BedrockServer/structures',
    'BedrockServer/worlds/BedrockLevel/behavior_packs',
    'BedrockServer/worlds/BedrockLevel/db',
    'BedrockServer/worlds/BedrockLevel/resource_packs',
    'BedrockServer/world_templates',
]"></FolderView>

3. 在`config/<pack_id>/permissions.json`或`config/default/permissions.json`中，启用`@minecraft/server-net`模块，通过在`allowed_modules`键中添加`"@minecraft/server-net"`。此模块在服务器中默认未启用。

- 修改默认配置文件夹中的文件允许每个带有server-net模块的附加包访问`@minecraft/server-net`模块。
- 建议为每个脚本行为包分配单独的权限。

```json title="BedrockServer/config/default/permissions.json"
{
  "allowed_modules": [
    "@minecraft/server-gametest",
    "@minecraft/server",
    "@minecraft/server-ui",
    "@minecraft/server-admin",
    "@minecraft/server-editor",
    "@minecraft/server-net"
  ]
}
```

## HTTP请求方法

脚本API支持以下HTTP请求方法：

- [`DELETE`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)
- [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)
- [`HEAD`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD)
- [`POST`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)
- [`PUT`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT)

## 简单HTTP请求

`http.get(url)` - 在行为包中执行简单的HTTP GET请求。

- `url`: `string`
- 返回: `Promise<`[`HttpResponse`](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/httpresponse)`>`

由于大多数请求是没有主体的GET请求，`@minecraft/server-net`提供了这个便利方法。此方法与`http.request()`的唯一区别是它会自动将方法设置为`GET`。

示例：

```js
import { http } from '@minecraft/server-net';

http.get('http://example.com/').then((response) => {
  // HTTP响应的主体内容。
  // 类型: string
  const body = response.body;
});
```

## 高级HTTP请求

### http.request

向Web服务器发送请求。

- `config`: [`HttpRequest`](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/httprequest)
- 返回: `Promise<`[`HttpResponse`](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server-net/httpresponse)`>`

配置必须是一个新的HttpRequest实例，以便构建请求。

## 示例

以下是向Web服务器发送请求的几种方法，包括每个可用的HTTP请求方法。

**创建HttpRequest对象**

```js
import { HttpRequest } from "@minecraft/server-net";

const request = new HttpRequest("http://localhost:8000/"); // 你必须将URL作为参数传入
```

**设置HTTP方法**

有关HTTP请求方法的更多信息，请访问：https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

**GET**

```js
import { HttpRequestMethod } from '@minecraft/server-net';
request.method = HttpRequestMethod.Get;
```

**HEAD**

```js
import { HttpRequestMethod } from '@minecraft/server-net';
request.method = HttpRequestMethod.Head;
```

**POST**

```js
import { HttpRequestMethod } from '@minecraft/server-net';
request.method = HttpRequestMethod.Post;
```

**PUT**

```js
import { HttpRequestMethod } from '@minecraft/server-net';
request.method = HttpRequestMethod.Put;
```

**DELETE**

```js
import { HttpRequestMethod } from '@minecraft/server-net';
request.method = HttpRequestMethod.Delete;
```

**设置HTTP头**

HTTP头可以在HTTP请求中使用，以提供有关请求上下文的信息，以便服务器可以定制响应。

```js
import { HttpHeader } from '@minecraft/server-net';
request.headers = [
    new HttpHeader("Content-Type", "application/json"),
    new HttpHeader("auth", "my-auth-token"),
];
```

HttpHeader的值参数还接受`@minecraft/server-admin`模块中的SecretString对象。

```js
import { HttpHeader } from '@minecraft/server-net';
import { secrets } from '@minecraft/server-admin';

const secret = secrets.get('TOKEN');
request.headers = [
  new HttpHeader('Authorization', secret)
];
```

**设置请求主体**

HTTP请求主体的内容，这些信息将发送到Web服务器。

```js
request.body = 'Message';
```

**设置响应超时**

设置请求超时并被放弃之前的时间（以秒为单位）。

此属性在HTTP请求中不常用。

```js
request.timeout = 10; // 10秒
```

**发送请求**

将请求发送到Web服务器，返回一个Promise HttpResponse。

```js
http.request(request).then((response) => {
  // HTTP请求响应的主体内容。
  // 类型: string
  response.body;
});
```

**示例**：

一个简单的脚本，将发送的聊天消息发送到Discord webhook。

```js
import { world } from "@minecraft/server";
import { http, HttpRequest, HttpRequestMethod, HttpHeader } from "@minecraft/server-net";

// 请注意，此事件需要服务器模块版本1.14.0-beta。
world.afterEvents.chatSend.subscribe((data) => {
	// 玩家发送的消息。
	const chatMsg = data.message;

	// 创建一个新的请求到Discord webhook URL。
	const request = new HttpRequest("https://discord.com/api/webhooks/your-webhook-here");

	// 将方法设置为POST类型（仅发送）。
	request.method = HttpRequestMethod.Post;

	// 将请求的主体设置为Discord所需的格式。
	// 有关此主题的更多信息，请访问：https://discord.com/developers/docs/resources/webhook
	request.body = JSON.stringify({
		content: chatMsg,
	});

	// 设置请求的头部。
	request.headers = [
		new HttpHeader("Content-Type", "application/json")
	];

	// 执行请求。
	http.request(request).then((response) => {
		// HTTP请求响应的主体。
		response.body;
	});
});
```

---

[原始来源](https://github.com/JaylyDev/ScriptAPI/tree/main/docs/MinecraftApi/%40minecraft/server-net)