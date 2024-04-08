# `HttpClient`

> 文档版本：1.21.0.20

`HttpClient`类。

## 方法

/// define
`cancelAll`


///

```js
cancelAll(reason: string): void
```

/// html | div.result
//// define
`reason`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`get`


///

```js
get(uri: string): Promise<HttpResponse>
```

/// html | div.result
//// define
`uri`：`string`

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../httpresponse/">HttpResponse</a>&gt;</code>

- 返回值。


////

///


/// define
`request`


///

```js
request(config: HttpRequest): Promise<HttpResponse>
```

/// html | div.result
//// define
`config`：[`HttpRequest`](./httprequest.md)

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../httpresponse/">HttpResponse</a>&gt;</code>

- 返回值。


////

///

