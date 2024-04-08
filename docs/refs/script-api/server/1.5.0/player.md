# `Player`

> 文档版本：1.21.0.20

`Player`类，扩展自[`Entity`](./entity.md)。

## 属性

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


## 方法

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

