# `World`

> 文档版本：1.21.0.20

`World`类。

## 属性

/// define
`afterEvents`


///

```js
read-only afterEvents: WorldAfterEvents;
```


/// define
`beforeEvents`


///

```js
read-only beforeEvents: WorldBeforeEvents;
```


/// define
`gameRules`


///

```js
read-only gameRules: GameRules;
```


/// define
`scoreboard`


///

```js
read-only scoreboard: Scoreboard;
```


/// define
`structureManager`


///

```js
read-only structureManager: StructureManager;
```


## 方法

/// define
`broadcastClientMessage`


///

```js
broadcastClientMessage(id: string, value: string): void
```

/// html | div.result
//// define
`id`：`string`

- 参数1。


////

//// define
`value`：`string`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`clearDynamicProperties`


///

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`getAbsoluteTime`


///

```js
getAbsoluteTime(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


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
`getDay`


///

```js
getDay(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getDefaultSpawnLocation`


///

```js
getDefaultSpawnLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

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
`getDynamicProperty`


///

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- 返回值。


////

///


/// define
`getDynamicPropertyIds`


///

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getEntity`


///

```js
getEntity(id: string): Entity | undefined
```

/// html | div.result
//// define
`id`：`string`

- 参数1。


////

//// define
返回值：[`Entity`](./entity.md)|`undefined`

- 返回值。


////

///


/// define
`getMoonPhase`


///

```js
getMoonPhase(): MoonPhase
```

/// html | div.result
//// define
返回值：[`MoonPhase`](./moonphase.md)

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
`getTimeOfDay`


///

```js
getTimeOfDay(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`playMusic`


///

```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- 参数1。


////

//// define
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

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
`queueMusic`


///

```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- 参数1。


////

//// define
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

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


/// define
`setAbsoluteTime`


///

```js
setAbsoluteTime(absoluteTime: int32): void
```

/// html | div.result
//// define
`absoluteTime`：`int32`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setDefaultSpawnLocation`


///

```js
setDefaultSpawnLocation(spawnLocation: Vector3): void
```

/// html | div.result
//// define
`spawnLocation`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setDynamicProperty`


///

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setTimeOfDay`


///

```js
setTimeOfDay(timeOfDay: int32 | TimeOfDay): void
```

/// html | div.result
//// define
`timeOfDay`：`int32`|[`TimeOfDay`](./timeofday.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopMusic`


///

```js
stopMusic(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///

