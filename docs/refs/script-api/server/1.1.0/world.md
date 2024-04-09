# `World`

> 文档版本：1.21.0.20

`World`类。script_api.@minecraft/server.world.description

## 方法

/// define
`getAllPlayers`


///

script_api.@minecraft/server.world.getallplayers.description

```js
getAllPlayers(): Player[]
```

/// html | div.result
//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.world.getallplayers.return


////

///


/// define
`getDimension`


///

script_api.@minecraft/server.world.getdimension.description

```js
getDimension(dimensionId: string): Dimension
```

/// html | div.result
//// define
`dimensionId`：`string`

- script_api.@minecraft/server.world.dimensionid.getdimension.description


////

//// define
返回值：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.world.getdimension.return


////

///


/// define
`getPlayers`


///

script_api.@minecraft/server.world.getplayers.description

```js
getPlayers(options?: EntityQueryOptions): Player[]
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- script_api.@minecraft/server.world.options.getplayers.description


////

//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.world.getplayers.return


////

///


/// define
`sendMessage`


///

script_api.@minecraft/server.world.sendmessage.description

```js
sendMessage(message: (RawMessage | string)[] | RawMessage | string): void
```

/// html | div.result
//// define
`message`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.world.message.sendmessage.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.sendmessage.return


////

///

