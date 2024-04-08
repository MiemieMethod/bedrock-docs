# `World`

> 文档版本：1.21.0.20

`World`类。

## 方法

/// define
`getAllPlayers`


///

```js
getAllPlayers(): Player[]
```

/// html | div.result
//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- 返回值。


////

///


/// define
`getDimension`


///

```js
getDimension(dimensionId: string): Dimension
```

/// html | div.result
//// define
`dimensionId`：`string`

- 参数1。


////

//// define
返回值：[`Dimension`](./dimension.md)

- 返回值。


////

///


/// define
`getPlayers`


///

```js
getPlayers(options?: EntityQueryOptions): Player[]
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- 返回值。


////

///


/// define
`sendMessage`


///

```js
sendMessage(message: RawMessage | string[] | RawMessage | string): void
```

/// html | div.result
//// define
`message`：`RawMessage | string[]`|[`RawMessage`](./rawmessage.md)|`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

