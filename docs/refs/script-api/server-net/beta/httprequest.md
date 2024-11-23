# `HttpRequest`

> 文档版本：1.21.60.21

`HttpRequest`类。script_api.@minecraft/server-net.httprequest.description

## 属性

/// define
`body`


///

```js
body: string;
```

/// html | div.result
//// define
`body`：`string`

- script_api.@minecraft/server-net.httprequest.body.description


////

///


/// define
`headers`


///

```js
headers: HttpHeader[];
```

/// html | div.result
//// define
`headers`：<code><a href="../httpheader/">HttpHeader</a>[]</code>

- script_api.@minecraft/server-net.httprequest.headers.description


////

///


/// define
`method`


///

```js
method: HttpRequestMethod;
```

/// html | div.result
//// define
`method`：[`HttpRequestMethod`](./httprequestmethod.md)

- script_api.@minecraft/server-net.httprequest.method.description


////

///


/// define
`timeout`


///

```js
timeout: uint32;
```

/// html | div.result
//// define
`timeout`：`uint32`

- script_api.@minecraft/server-net.httprequest.timeout.description


////

///


/// define
`uri`


///

```js
uri: string;
```

/// html | div.result
//// define
`uri`：`string`

- script_api.@minecraft/server-net.httprequest.uri.description


////

///


## 方法

/// define
`addHeader`


///

script_api.@minecraft/server-net.httprequest.addheader.description

```js
addHeader(key: string, value: SecretString | string): HttpRequest
```

/// html | div.result
//// define
`key`：`string`

- script_api.@minecraft/server-net.httprequest.addheader.key.description


////

//// define
`value`：[`SecretString`](../../server-admin/beta/secretstring.md)|`string`

- script_api.@minecraft/server-net.httprequest.addheader.value.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.addheader.return


////

///


/// define
`constructor`


///

script_api.@minecraft/server-net.httprequest.constructor.description

```js
new constructor(uri: string): HttpRequest
```

/// html | div.result
//// define
`uri`：`string`

- script_api.@minecraft/server-net.httprequest.constructor.uri.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.constructor.return


////

///


/// define
`setBody`


///

script_api.@minecraft/server-net.httprequest.setbody.description

```js
setBody(body: string): HttpRequest
```

/// html | div.result
//// define
`body`：`string`

- script_api.@minecraft/server-net.httprequest.setbody.body.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.setbody.return


////

///


/// define
`setHeaders`


///

script_api.@minecraft/server-net.httprequest.setheaders.description

```js
setHeaders(headers: HttpHeader[]): HttpRequest
```

/// html | div.result
//// define
`headers`：<code><a href="../httpheader/">HttpHeader</a>[]</code>

- script_api.@minecraft/server-net.httprequest.setheaders.headers.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.setheaders.return


////

///


/// define
`setMethod`


///

script_api.@minecraft/server-net.httprequest.setmethod.description

```js
setMethod(method: HttpRequestMethod): HttpRequest
```

/// html | div.result
//// define
`method`：[`HttpRequestMethod`](./httprequestmethod.md)

- script_api.@minecraft/server-net.httprequest.setmethod.method.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.setmethod.return


////

///


/// define
`setTimeout`


///

script_api.@minecraft/server-net.httprequest.settimeout.description

```js
setTimeout(timeout: uint32): HttpRequest
```

/// html | div.result
//// define
`timeout`：`uint32`∈[`0`, +∞]

- script_api.@minecraft/server-net.httprequest.settimeout.timeout.description


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- script_api.@minecraft/server-net.httprequest.settimeout.return


////

///

