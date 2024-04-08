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

/// html | div.result
//// define
`afterEvents`：[`WorldAfterEvents`](./worldafterevents.md)

- 属性。


////

///


/// define
`beforeEvents`


///

```js
read-only beforeEvents: WorldBeforeEvents;
```

/// html | div.result
//// define
`beforeEvents`：[`WorldBeforeEvents`](./worldbeforeevents.md)

- 属性。


////

///


/// define
`scoreboard`


///

```js
read-only scoreboard: Scoreboard;
```

/// html | div.result
//// define
`scoreboard`：[`Scoreboard`](./scoreboard.md)

- 属性。


////

///


## 方法

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

