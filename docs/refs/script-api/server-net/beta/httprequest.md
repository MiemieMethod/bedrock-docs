# `HttpRequest`

> 文档版本：1.21.0.20

`HttpRequest`类。

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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`addHeader`


///

```js
addHeader(key: string, value: SecretString | string): HttpRequest
```

/// html | div.result
//// define
`key`：`string`

- 参数1。


////

//// define
`value`：[`SecretString`](../../server-admin/beta/secretstring.md)|`string`

- 参数2。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///


/// define
`constructor`


///

```js
new constructor(uri: string): HttpRequest
```

/// html | div.result
//// define
`uri`：`string`

- 参数1。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///


/// define
`setBody`


///

```js
setBody(body: string): HttpRequest
```

/// html | div.result
//// define
`body`：`string`

- 参数1。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///


/// define
`setHeaders`


///

```js
setHeaders(headers: HttpHeader[]): HttpRequest
```

/// html | div.result
//// define
`headers`：<code><a href="../httpheader/">HttpHeader</a>[]</code>

- 参数1。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///


/// define
`setMethod`


///

```js
setMethod(method: HttpRequestMethod): HttpRequest
```

/// html | div.result
//// define
`method`：[`HttpRequestMethod`](./httprequestmethod.md)

- 参数1。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///


/// define
`setTimeout`


///

```js
setTimeout(timeout: uint32): HttpRequest
```

/// html | div.result
//// define
`timeout`：`uint32`

- 参数1。


////

//// define
返回值：[`HttpRequest`](./httprequest.md)

- 返回值。


////

///

