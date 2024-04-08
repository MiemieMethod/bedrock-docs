# `Dimension`

> 文档版本：1.21.0.20

`Dimension`类。

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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`containsBlock`


///

```js
containsBlock(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks: boolean): boolean
```

/// html | div.result
//// define
`volume`：[`BlockVolumeBase`](./blockvolumebase.md)

- 参数1。


////

//// define
`filter`：[`BlockFilter`](./blockfilter.md)

- 参数2。


////

//// define
`allowUnloadedChunks`：`boolean`

- 参数3。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`createExplosion`


///

```js
createExplosion(location: Vector3, radius: float, explosionOptions?: ExplosionOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`radius`：`float`

- 参数2。


////

//// define
`explosionOptions`：[`ExplosionOptions`](./explosionoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`fillBlocks`


///

```js
fillBlocks(begin: Vector3, end: Vector3, block: BlockPermutation | BlockType | string, options?: BlockFillOptions): uint32
```

/// html | div.result
//// define
`begin`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`end`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`block`：[`BlockPermutation`](./blockpermutation.md)|[`BlockType`](./blocktype.md)|`string`

- 参数3。


////

//// define
`options`：[`BlockFillOptions`](./blockfilloptions.md)|`undefined`

- 参数4。


////

//// define
返回值：`uint32`

- 返回值。


////

///


/// define
`findClosestBiome`


///

```js
findClosestBiome(pos: Vector3, biomeToFind: BiomeType | string, options?: BiomeSearchOptions): Vector3 | undefined
```

/// html | div.result
//// define
`pos`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`biomeToFind`：[`BiomeType`](./biometype.md)|`string`

- 参数2。


////

//// define
`options`：[`BiomeSearchOptions`](./biomesearchoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：[`Vector3`](./vector3.md)|`undefined`

- 返回值。


////

///


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
`getBlockFromRay`


///

```js
getBlockFromRay(location: Vector3, direction: Vector3, options?: BlockRaycastOptions): BlockRaycastHit | undefined
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`direction`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：[`BlockRaycastHit`](./blockraycasthit.md)|`undefined`

- 返回值。


////

///


/// define
`getBlocks`


///

```js
getBlocks(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks: boolean): ListBlockVolume
```

/// html | div.result
//// define
`volume`：[`BlockVolumeBase`](./blockvolumebase.md)

- 参数1。


////

//// define
`filter`：[`BlockFilter`](./blockfilter.md)

- 参数2。


////

//// define
`allowUnloadedChunks`：`boolean`

- 参数3。


////

//// define
返回值：[`ListBlockVolume`](./listblockvolume.md)

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
`getEntitiesFromRay`


///

```js
getEntitiesFromRay(location: Vector3, direction: Vector3, options?: EntityRaycastOptions): EntityRaycastHit[]
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`direction`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：<code><a href="../entityraycasthit/">EntityRaycastHit</a>[]</code>

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
`getWeather`


///

```js
getWeather(): WeatherType
```

/// html | div.result
//// define
返回值：[`WeatherType`](./weathertype.md)

- 返回值。


////

///


/// define
`playSound`


///

```js
playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`soundOptions`：[`WorldSoundOptions`](./worldsoundoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`runCommand`


///

```js
runCommand(commandString: string): CommandResult
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：[`CommandResult`](./commandresult.md)

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


/// define
`setBlockPermutation`


///

```js
setBlockPermutation(location: Vector3, permutation: BlockPermutation): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setBlockType`


///

```js
setBlockType(location: Vector3, blockType: BlockType | string): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`blockType`：[`BlockType`](./blocktype.md)|`string`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setWeather`


///

```js
setWeather(weatherType: WeatherType, duration?: int32): void
```

/// html | div.result
//// define
`weatherType`：[`WeatherType`](./weathertype.md)

- 参数1。


////

//// define
`duration`：`int32`|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`spawnEntity`


///

```js
spawnEntity(identifier: string, location: Vector3, options?: SpawnEntityOptions): Entity
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`options`：[`SpawnEntityOptions`](./spawnentityoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：[`Entity`](./entity.md)

- 返回值。


////

///


/// define
`spawnItem`


///

```js
spawnItem(itemStack: ItemStack, location: Vector3): Entity
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- 参数1。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](./entity.md)

- 返回值。


////

///


/// define
`spawnParticle`


///

```js
spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void
```

/// html | div.result
//// define
`effectName`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`molangVariables`：[`MolangVariableMap`](./molangvariablemap.md)|`undefined`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///

