# `Dimension`

> 文档版本：1.21.60.21

`Dimension`类。script_api.mojang-minecraft.dimension.description

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

- script_api.mojang-minecraft.dimension.id.description


////

///


## 方法

/// define
`createExplosion`


///

script_api.mojang-minecraft.dimension.createexplosion.description

```js
createExplosion(location: Location, radius: float, explosionOptions: ExplosionOptions): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.createexplosion.location.description


////

//// define
`radius`：`float`

- script_api.mojang-minecraft.dimension.createexplosion.radius.description


////

//// define
`explosionOptions`：[`ExplosionOptions`](./explosionoptions.md)

- script_api.mojang-minecraft.dimension.createexplosion.explosionoptions.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.dimension.createexplosion.return


////

///


/// define
`getBlock`


///

script_api.mojang-minecraft.dimension.getblock.description

```js
getBlock(location: BlockLocation): Block
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- script_api.mojang-minecraft.dimension.getblock.location.description


////

//// define
返回值：[`Block`](./block.md)

- script_api.mojang-minecraft.dimension.getblock.return


////

///


/// define
`getBlockFromRay`


///

script_api.mojang-minecraft.dimension.getblockfromray.description

```js
getBlockFromRay(location: Location, direction: Vector, options?: BlockRaycastOptions): Block | undefined
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.getblockfromray.location.description


////

//// define
`direction`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.dimension.getblockfromray.direction.description


////

//// define
`options`?：[`BlockRaycastOptions`](./blockraycastoptions.md)＝`null`

- script_api.mojang-minecraft.dimension.getblockfromray.options.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.mojang-minecraft.dimension.getblockfromray.return


////

///


/// define
`getEntities`


///

script_api.mojang-minecraft.dimension.getentities.description

```js
getEntities(options?: EntityQueryOptions): EntityIterator
```

/// html | div.result
//// define
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.mojang-minecraft.dimension.getentities.options.description


////

//// define
返回值：[`EntityIterator`](./entityiterator.md)

- script_api.mojang-minecraft.dimension.getentities.return


////

///


/// define
`getEntitiesAtBlockLocation`


///

script_api.mojang-minecraft.dimension.getentitiesatblocklocation.description

```js
getEntitiesAtBlockLocation(location: BlockLocation): Entity[]
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- script_api.mojang-minecraft.dimension.getentitiesatblocklocation.location.description


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.mojang-minecraft.dimension.getentitiesatblocklocation.return


////

///


/// define
`getEntitiesFromRay`


///

script_api.mojang-minecraft.dimension.getentitiesfromray.description

```js
getEntitiesFromRay(location: Location, direction: Vector, options?: EntityRaycastOptions): Entity[]
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.getentitiesfromray.location.description


////

//// define
`direction`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.dimension.getentitiesfromray.direction.description


////

//// define
`options`?：[`EntityRaycastOptions`](./entityraycastoptions.md)＝`null`

- script_api.mojang-minecraft.dimension.getentitiesfromray.options.description


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.mojang-minecraft.dimension.getentitiesfromray.return


////

///


/// define
`getPlayers`


///

script_api.mojang-minecraft.dimension.getplayers.description

```js
getPlayers(options?: EntityQueryOptions): PlayerIterator
```

/// html | div.result
//// define
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.mojang-minecraft.dimension.getplayers.options.description


////

//// define
返回值：[`PlayerIterator`](./playeriterator.md)

- script_api.mojang-minecraft.dimension.getplayers.return


////

///


/// define
`isEmpty`


///

script_api.mojang-minecraft.dimension.isempty.description

```js
isEmpty(location: BlockLocation): boolean
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- script_api.mojang-minecraft.dimension.isempty.location.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.dimension.isempty.return


////

///


/// define
`runCommand`


///

script_api.mojang-minecraft.dimension.runcommand.description

```js
runCommand(commandString: string): any
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.mojang-minecraft.dimension.runcommand.commandstring.description


////

//// define
返回值：`any`

- script_api.mojang-minecraft.dimension.runcommand.return


////

///


/// define
`spawnEntity`


///

script_api.mojang-minecraft.dimension.spawnentity.description

```js
spawnEntity(identifier: string, location: BlockLocation | Location): Entity
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.dimension.spawnentity.identifier.description


////

//// define
`location`：[`BlockLocation`](./blocklocation.md)|[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.spawnentity.location.description


////

//// define
返回值：[`Entity`](./entity.md)

- script_api.mojang-minecraft.dimension.spawnentity.return


////

///


/// define
`spawnItem`


///

script_api.mojang-minecraft.dimension.spawnitem.description

```js
spawnItem(item: ItemStack, location: BlockLocation | Location): Entity
```

/// html | div.result
//// define
`item`：[`ItemStack`](./itemstack.md)

- script_api.mojang-minecraft.dimension.spawnitem.item.description


////

//// define
`location`：[`BlockLocation`](./blocklocation.md)|[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.spawnitem.location.description


////

//// define
返回值：[`Entity`](./entity.md)

- script_api.mojang-minecraft.dimension.spawnitem.return


////

///


/// define
`spawnParticle`


///

script_api.mojang-minecraft.dimension.spawnparticle.description

```js
spawnParticle(effectName: string, location: Location, molangVariables: MolangVariableMap): void
```

/// html | div.result
//// define
`effectName`：`string`

- script_api.mojang-minecraft.dimension.spawnparticle.effectname.description


////

//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.dimension.spawnparticle.location.description


////

//// define
`molangVariables`：[`MolangVariableMap`](./molangvariablemap.md)

- script_api.mojang-minecraft.dimension.spawnparticle.molangvariables.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.dimension.spawnparticle.return


////

///

