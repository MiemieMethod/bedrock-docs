# `World`

> 文档版本：1.21.0.20

`World`类。

## 属性

/// define
`events`


///

```js
read-only events: Events;
```

/// html | div.result
//// define
`events`：[`Events`](./events.md)

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
getDynamicProperty(identifier: string): boolean | double | float | Location | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`|`undefined`

- 返回值。


////

///


/// define
`getPlayers`


///

```js
getPlayers(options?: EntityQueryOptions): PlayerIterator
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：[`PlayerIterator`](./playeriterator.md)

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
playSound(soundID: string, soundOptions?: SoundOptions): void
```

/// html | div.result
//// define
`soundID`：`string`

- 参数1。


////

//// define
`soundOptions`：[`SoundOptions`](./soundoptions.md)|`undefined`

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
`removeDynamicProperty`


///

```js
removeDynamicProperty(identifier: string): boolean
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`setDynamicProperty`


///

```js
setDynamicProperty(identifier: string, value: boolean | double | float | Location | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`

- 参数2。


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

