# `Dimension`

> 文档版本：1.21.60.21

`Dimension`类。script_api.@minecraft/server.dimension.description

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

- script_api.@minecraft/server.dimension.id.description


////

///


## 方法

/// define
`getBlock`


///

script_api.@minecraft/server.dimension.getblock.description

```js
getBlock(location: Vector3): Block | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getblock.location.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.dimension.getblock.return


////

///


/// define
`getBlockFromRay`


///

script_api.@minecraft/server.dimension.getblockfromray.description

```js
getBlockFromRay(location: Vector3, direction: Vector3, options?: BlockRaycastOptions): BlockRaycastHit | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getblockfromray.location.description


////

//// define
`direction`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getblockfromray.direction.description


////

//// define
`options`?：[`BlockRaycastOptions`](./blockraycastoptions.md)＝`null`

- script_api.@minecraft/server.dimension.getblockfromray.options.description


////

//// define
返回值：[`BlockRaycastHit`](./blockraycasthit.md)|`undefined`

- script_api.@minecraft/server.dimension.getblockfromray.return


////

///


/// define
`getEntities`


///

script_api.@minecraft/server.dimension.getentities.description

```js
getEntities(options?: EntityQueryOptions): Entity[]
```

/// html | div.result
//// define
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.@minecraft/server.dimension.getentities.options.description


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.@minecraft/server.dimension.getentities.return


////

///


/// define
`getEntitiesAtBlockLocation`


///

script_api.@minecraft/server.dimension.getentitiesatblocklocation.description

```js
getEntitiesAtBlockLocation(location: Vector3): Entity[]
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getentitiesatblocklocation.location.description


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.@minecraft/server.dimension.getentitiesatblocklocation.return


////

///


/// define
`getEntitiesFromRay`


///

script_api.@minecraft/server.dimension.getentitiesfromray.description

```js
getEntitiesFromRay(location: Vector3, direction: Vector3, options?: EntityRaycastOptions): EntityRaycastHit[]
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getentitiesfromray.location.description


////

//// define
`direction`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.getentitiesfromray.direction.description


////

//// define
`options`?：[`EntityRaycastOptions`](./entityraycastoptions.md)＝`null`

- script_api.@minecraft/server.dimension.getentitiesfromray.options.description


////

//// define
返回值：<code><a href="../entityraycasthit/">EntityRaycastHit</a>[]</code>

- script_api.@minecraft/server.dimension.getentitiesfromray.return


////

///


/// define
`getPlayers`


///

script_api.@minecraft/server.dimension.getplayers.description

```js
getPlayers(options?: EntityQueryOptions): Player[]
```

/// html | div.result
//// define
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.@minecraft/server.dimension.getplayers.options.description


////

//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.dimension.getplayers.return


////

///


/// define
`runCommand`


///

script_api.@minecraft/server.dimension.runcommand.description

```js
runCommand(commandString: string): CommandResult
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.@minecraft/server.dimension.runcommand.commandstring.description


////

//// define
返回值：[`CommandResult`](./commandresult.md)

- script_api.@minecraft/server.dimension.runcommand.return


////

///


/// define
`runCommandAsync`


///

script_api.@minecraft/server.dimension.runcommandasync.description

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.@minecraft/server.dimension.runcommandasync.commandstring.description


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- script_api.@minecraft/server.dimension.runcommandasync.return


////

///


/// define
`spawnEntity`


///

script_api.@minecraft/server.dimension.spawnentity.description

```js
spawnEntity(identifier: string, location: Vector3): Entity
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.dimension.spawnentity.identifier.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.spawnentity.location.description


////

//// define
返回值：[`Entity`](./entity.md)

- script_api.@minecraft/server.dimension.spawnentity.return


////

///


/// define
`spawnItem`


///

script_api.@minecraft/server.dimension.spawnitem.description

```js
spawnItem(itemStack: ItemStack, location: Vector3): Entity
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- script_api.@minecraft/server.dimension.spawnitem.itemstack.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.spawnitem.location.description


////

//// define
返回值：[`Entity`](./entity.md)

- script_api.@minecraft/server.dimension.spawnitem.return


////

///

