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


/// define
`id`


///

```js
read-only id: string;
```


## 方法

/// define
`containsBlock`


///

```js
containsBlock(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks: boolean): boolean
```


/// define
`createExplosion`


///

```js
createExplosion(location: Vector3, radius: float, explosionOptions?: ExplosionOptions): boolean
```


/// define
`fillBlocks`


///

```js
fillBlocks(begin: Vector3, end: Vector3, block: BlockPermutation | BlockType | string, options?: BlockFillOptions): uint32
```


/// define
`findClosestBiome`


///

```js
findClosestBiome(pos: Vector3, biomeToFind: BiomeType | string, options?: BiomeSearchOptions): Vector3 | undefined
```


/// define
`getBlock`


///

```js
getBlock(location: Vector3): Block | undefined
```


/// define
`getBlockFromRay`


///

```js
getBlockFromRay(location: Vector3, direction: Vector3, options?: BlockRaycastOptions): BlockRaycastHit | undefined
```


/// define
`getBlocks`


///

```js
getBlocks(volume: BlockVolumeBase, filter: BlockFilter, allowUnloadedChunks: boolean): ListBlockVolume
```


/// define
`getEntities`


///

```js
getEntities(options?: EntityQueryOptions): Entity[]
```


/// define
`getEntitiesAtBlockLocation`


///

```js
getEntitiesAtBlockLocation(location: Vector3): Entity[]
```


/// define
`getEntitiesFromRay`


///

```js
getEntitiesFromRay(location: Vector3, direction: Vector3, options?: EntityRaycastOptions): EntityRaycastHit[]
```


/// define
`getPlayers`


///

```js
getPlayers(options?: EntityQueryOptions): Player[]
```


/// define
`getWeather`


///

```js
getWeather(): WeatherType
```


/// define
`playSound`


///

```js
playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void
```


/// define
`runCommand`


///

```js
runCommand(commandString: string): CommandResult
```


/// define
`runCommandAsync`


///

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```


/// define
`setBlockPermutation`


///

```js
setBlockPermutation(location: Vector3, permutation: BlockPermutation): void
```


/// define
`setBlockType`


///

```js
setBlockType(location: Vector3, blockType: BlockType | string): void
```


/// define
`setWeather`


///

```js
setWeather(weatherType: WeatherType, duration?: int32): void
```


/// define
`spawnEntity`


///

```js
spawnEntity(identifier: string, location: Vector3, options?: SpawnEntityOptions): Entity
```


/// define
`spawnItem`


///

```js
spawnItem(itemStack: ItemStack, location: Vector3): Entity
```


/// define
`spawnParticle`


///

```js
spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void
```

