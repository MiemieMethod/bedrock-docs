# 服务端HTTP请求<!-- md:flag vanilla -->

`@minecraft/server-net`模块允许脚本API从基岩版专用服务端（BDS）发出HTTP请求，适用于服务端与外部系统集成的场景，如统计数据上报、身份验证等。

/// warning | 仅限BDS
`@minecraft/server-net`模块只能在基岩版专用服务端上运行，无法在普通Minecraft客户端（含自托管服务器）中使用。
///

## 配置清单文件

在行为包的`manifest.json`中声明依赖：

```json title="BP/manifest.json（依赖部分）"
{
    "dependencies": [
        {
            "module_name": "@minecraft/server",
            "version": "2.0.0"
        },
        {
            "module_name": "@minecraft/server-net",
            "version": "1.0.0-beta"
        }
    ]
}
```

同时，还需要在BDS的`config/default/permissions.json`中授权该行为包使用网络功能：

```json title="BDS/config/default/permissions.json"
{
    "allowed_modules": [
        {
            "module_name": "@minecraft/server-net",
            "version": "1.0.0-beta"
        }
    ]
}
```

## 发送GET请求

使用`http.get(url)`发出GET请求，返回`Promise<HttpResponse>`：

```javascript
import { http, HttpRequest, HttpRequestMethod } from "@minecraft/server-net";
import { world } from "@minecraft/server";

// 简写GET请求
http.get("https://jsonplaceholder.typicode.com/todos/1")
    .then((response) => {
        world.sendMessage(`响应状态码：${response.status}`);
        world.sendMessage(`响应内容：${response.body}`);
    })
    .catch((error) => {
        console.error("请求失败：", error);
    });
```

## 发送POST请求

通过`HttpRequest`对象构建更复杂的请求：

```javascript
import { http, HttpRequest, HttpRequestMethod, HttpHeader } from "@minecraft/server-net";
import { world } from "@minecraft/server";

const request = new HttpRequest("https://api.example.com/data");
request.method = HttpRequestMethod.Post;
request.headers = [
    new HttpHeader("Content-Type", "application/json"),
    new HttpHeader("Authorization", "Bearer YOUR_TOKEN"),
];
request.body = JSON.stringify({
    playerId: "some-player-id",
    event: "playerJoin",
});
request.timeout = 10;  // 超时秒数（默认10秒）

http.request(request)
    .then((response) => {
        console.log(`状态码：${response.status}`);
        const data = JSON.parse(response.body);
        world.sendMessage(`服务器回复：${data.message}`);
    })
    .catch((err) => {
        console.error("POST请求失败：", err);
    });
```

## HttpResponse属性

`HttpResponse`对象包含以下属性：

/// define
`status: number`

- HTTP状态码，如200、404等。

`body: string`

- 响应体文本内容。

`headers: HttpHeader[]`

- 响应头数组，每个元素有`key`和`value`属性。

`request: HttpRequest`

- 发起请求的原始`HttpRequest`对象。

///

## 注意事项

- 每次脚本执行最多可以同时发起**10个并发请求**。
- 请求结果是异步的，不阻塞游戏主线程。
- 请避免在响应回调中直接调用需要受限执行模式权限的API，改用`system.run()`包裹。
