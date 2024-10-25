# `Entity`

> 文档版本：1.21.50.25

`Entity`类。script_api.@minecraft/server.entity.description

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension;
```

/// html | div.result
//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.entity.dimension.description


////

///


/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server.entity.id.description


////

///


/// define
`location`


///

```js
read-only location: Vector3;
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.location.description


////

///


/// define
`nameTag`


///

```js
nameTag: string;
```

/// html | div.result
//// define
`nameTag`：`string`

- script_api.@minecraft/server.entity.nametag.description


////

///


/// define
`typeId`


///

```js
read-only typeId: string;
```

/// html | div.result
//// define
`typeId`：`string`

- script_api.@minecraft/server.entity.typeid.description


////

///


## 方法

/// define
`getHeadLocation`


///

script_api.@minecraft/server.entity.getheadlocation.description

```js
getHeadLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getheadlocation.return


////

///


/// define
`getVelocity`


///

script_api.@minecraft/server.entity.getvelocity.description

```js
getVelocity(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getvelocity.return


////

///


/// define
`getViewDirection`


///

script_api.@minecraft/server.entity.getviewdirection.description

```js
getViewDirection(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getviewdirection.return


////

///


/// define
`runCommandAsync`


///

script_api.@minecraft/server.entity.runcommandasync.description

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.@minecraft/server.entity.runcommandasync.commandstring.description


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- script_api.@minecraft/server.entity.runcommandasync.return


////

///

