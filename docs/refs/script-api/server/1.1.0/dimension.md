# `Dimension`

> 文档版本：1.21.0.20

`Dimension`类。

## 属性

/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- 属性。


////

///


## 方法

/// define
`getBlock`


///

```js
getBlock(location: Vector3): Block | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`getEntities`


///

```js
getEntities(options?: EntityQueryOptions): Entity[]
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- 返回值。


////

///


/// define
`getEntitiesAtBlockLocation`


///

```js
getEntitiesAtBlockLocation(location: Vector3): Entity[]
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

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
`runCommandAsync`


///

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- 返回值。


////

///

