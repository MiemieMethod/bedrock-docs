# `Dimension`

> 文档版本：1.21.60.21

`Dimension`类。script_api.@minecraft/server.dimension.description

## 属性

/// define
`heightRange`


///

```js
read-only heightRange: NumberRange;
```

/// html | div.result
//// define
`heightRange`：[`NumberRange`](../../common/1.1.0/numberrange.md)

- script_api.@minecraft/server.dimension.heightrange.description


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

- script_api.@minecraft/server.dimension.id.description


////

///


## 方法

/// define
`createExplosion`


///

script_api.@minecraft/server.dimension.createexplosion.description

```js
createExplosion(location: Vector3, radius: float, explosionOptions?: ExplosionOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.createexplosion.location.description


////

//// define
`radius`：`float`∈[`0.0`, `1000.0`]

- script_api.@minecraft/server.dimension.createexplosion.radius.description


////

//// define
`explosionOptions`?：[`ExplosionOptions`](./explosionoptions.md)＝`null`

- script_api.@minecraft/server.dimension.createexplosion.explosionoptions.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.dimension.createexplosion.return


////

///


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
`getTopmostBlock`


///

script_api.@minecraft/server.dimension.gettopmostblock.description

```js
getTopmostBlock(locationXZ: VectorXZ, minHeight?: float): Block | undefined
```

/// html | div.result
//// define
`locationXZ`：[`VectorXZ`](./vectorxz.md)

- script_api.@minecraft/server.dimension.gettopmostblock.locationxz.description


////

//// define
`minHeight`?：`float`＝`null`

- script_api.@minecraft/server.dimension.gettopmostblock.minheight.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.dimension.gettopmostblock.return


////

///


/// define
`playSound`


///

script_api.@minecraft/server.dimension.playsound.description

```js
playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- script_api.@minecraft/server.dimension.playsound.soundid.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.playsound.location.description


////

//// define
`soundOptions`?：[`WorldSoundOptions`](./worldsoundoptions.md)＝`null`

- script_api.@minecraft/server.dimension.playsound.soundoptions.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.dimension.playsound.return


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
`setBlockPermutation`


///

script_api.@minecraft/server.dimension.setblockpermutation.description

```js
setBlockPermutation(location: Vector3, permutation: BlockPermutation): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.setblockpermutation.location.description


////

//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.dimension.setblockpermutation.permutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.dimension.setblockpermutation.return


////

///


/// define
`setBlockType`


///

script_api.@minecraft/server.dimension.setblocktype.description

```js
setBlockType(location: Vector3, blockType: BlockType | string): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.setblocktype.location.description


////

//// define
`blockType`：[`BlockType`](./blocktype.md)|`string`

- script_api.@minecraft/server.dimension.setblocktype.blocktype.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.dimension.setblocktype.return


////

///


/// define
`setWeather`


///

script_api.@minecraft/server.dimension.setweather.description

```js
setWeather(weatherType: WeatherType, duration?: int32): void
```

/// html | div.result
//// define
`weatherType`：[`WeatherType`](./weathertype.md)

- script_api.@minecraft/server.dimension.setweather.weathertype.description


////

//// define
`duration`?：`int32`＝`null`∈[`1`, `1000000`]

- script_api.@minecraft/server.dimension.setweather.duration.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.dimension.setweather.return


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


/// define
`spawnParticle`


///

script_api.@minecraft/server.dimension.spawnparticle.description

```js
spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void
```

/// html | div.result
//// define
`effectName`：`string`

- script_api.@minecraft/server.dimension.spawnparticle.effectname.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.dimension.spawnparticle.location.description


////

//// define
`molangVariables`?：[`MolangVariableMap`](./molangvariablemap.md)＝`null`

- script_api.@minecraft/server.dimension.spawnparticle.molangvariables.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.dimension.spawnparticle.return


////

///

