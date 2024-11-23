# `HttpClient`

> 文档版本：1.21.60.21

`HttpClient`类。script_api.@minecraft/server-net.httpclient.description

## 方法

/// define
`cancelAll`


///

script_api.@minecraft/server-net.httpclient.cancelall.description

```js
cancelAll(reason: string): void
```

/// html | div.result
//// define
`reason`：`string`

- script_api.@minecraft/server-net.httpclient.cancelall.reason.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-net.httpclient.cancelall.return


////

///


/// define
`get`


///

script_api.@minecraft/server-net.httpclient.get.description

```js
get(uri: string): Promise<HttpResponse>
```

/// html | div.result
//// define
`uri`：`string`

- script_api.@minecraft/server-net.httpclient.get.uri.description


////

//// define
返回值：<code>Promise&lt;<a href="../httpresponse/">HttpResponse</a>&gt;</code>

- script_api.@minecraft/server-net.httpclient.get.return


////

///


/// define
`request`


///

script_api.@minecraft/server-net.httpclient.request.description

```js
request(config: HttpRequest): Promise<HttpResponse>
```

/// html | div.result
//// define
`config`：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httpclient.request.config.description


////

//// define
返回值：<code>Promise&lt;<a href="../httpresponse/">HttpResponse</a>&gt;</code>

- script_api.@minecraft/server-net.httpclient.request.return


////

///

