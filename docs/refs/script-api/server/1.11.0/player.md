# `Player`

> 文档版本：1.21.0.20

`Player`类，扩展自[`Entity`](./entity.md)。

## 属性

/// define
`camera`


///

```js
read-only camera: Camera;
```

/// html | div.result
//// define
`camera`：[`Camera`](./camera.md)

- 属性。


////

///


/// define
`isEmoting`


///

```js
read-only isEmoting: boolean;
```

/// html | div.result
//// define
`isEmoting`：`boolean`

- 属性。


////

///


/// define
`isFlying`


///

```js
read-only isFlying: boolean;
```

/// html | div.result
//// define
`isFlying`：`boolean`

- 属性。


////

///


/// define
`isGliding`


///

```js
read-only isGliding: boolean;
```

/// html | div.result
//// define
`isGliding`：`boolean`

- 属性。


////

///


/// define
`isJumping`


///

```js
read-only isJumping: boolean;
```

/// html | div.result
//// define
`isJumping`：`boolean`

- 属性。


////

///


/// define
`level`


///

```js
read-only level: int32;
```

/// html | div.result
//// define
`level`：`int32`

- 属性。


////

///


/// define
`name`


///

```js
read-only name: string;
```

/// html | div.result
//// define
`name`：`string`

- 属性。


////

///


/// define
`onScreenDisplay`


///

```js
read-only onScreenDisplay: ScreenDisplay;
```

/// html | div.result
//// define
`onScreenDisplay`：[`ScreenDisplay`](./screendisplay.md)

- 属性。


////

///


/// define
`totalXpNeededForNextLevel`


///

```js
read-only totalXpNeededForNextLevel: int32;
```

/// html | div.result
//// define
`totalXpNeededForNextLevel`：`int32`

- 属性。


////

///


/// define
`xpEarnedAtCurrentLevel`


///

```js
read-only xpEarnedAtCurrentLevel: int32;
```

/// html | div.result
//// define
`xpEarnedAtCurrentLevel`：`int32`

- 属性。


////

///


## 方法

/// define
`addExperience`


///

```js
addExperience(amount: int32): uint32
```

/// html | div.result
//// define
`amount`：`int32`

- 参数1。


////

//// define
返回值：`uint32`

- 返回值。


////

///


/// define
`addLevels`


///

```js
addLevels(amount: int32): int32
```

/// html | div.result
//// define
`amount`：`int32`

- 参数1。


////

//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getSpawnPoint`


///

```js
getSpawnPoint(): DimensionLocation | undefined
```

/// html | div.result
//// define
返回值：[`DimensionLocation`](./dimensionlocation.md)|`undefined`

- 返回值。


////

///


/// define
`getTotalXp`


///

```js
getTotalXp(): uint32
```

/// html | div.result
//// define
返回值：`uint32`

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
playSound(soundId: string, soundOptions?: PlayerSoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- 参数1。


////

//// define
`soundOptions`：[`PlayerSoundOptions`](./playersoundoptions.md)|`undefined`

- 参数2。


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
`resetLevel`


///

```js
resetLevel(): void
```

/// html | div.result
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
`setSpawnPoint`


///

```js
setSpawnPoint(spawnPoint?: DimensionLocation): void
```

/// html | div.result
//// define
`spawnPoint`：[`DimensionLocation`](./dimensionlocation.md)|`undefined`

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

