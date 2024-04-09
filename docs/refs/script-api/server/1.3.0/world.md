# `World`

> 文档版本：1.21.0.20

`World`类。script_api.@minecraft/server.world.description

## 方法

/// define
`getAllPlayers`


///

script_api.@minecraft/server.world.getallplayers.description

```js
getAllPlayers(): Player[]
```

/// html | div.result
//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.world.getallplayers.return


////

///


/// define
`getDimension`


///

script_api.@minecraft/server.world.getdimension.description

```js
getDimension(dimensionId: string): Dimension
```

/// html | div.result
//// define
`dimensionId`：`string`

- script_api.@minecraft/server.world.dimensionid.getdimension.description


////

//// define
返回值：[`Dimension`](./dimension.md)

- script_api.@minecraft/server.world.getdimension.return


////

///


/// define
`getPlayers`


///

script_api.@minecraft/server.world.getplayers.description

```js
getPlayers(options?: EntityQueryOptions): Player[]
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)|`undefined`

- script_api.@minecraft/server.world.options.getplayers.description


////

//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.world.getplayers.return


////

///


/// define
`playMusic`


///

script_api.@minecraft/server.world.playmusic.description

```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.@minecraft/server.world.trackid.playmusic.description


////

//// define
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

- script_api.@minecraft/server.world.musicoptions.playmusic.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.playmusic.return


////

///


/// define
`playSound`


///

script_api.@minecraft/server.world.playsound.description

```js
playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- script_api.@minecraft/server.world.soundid.playsound.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.world.location.playsound.description


////

//// define
`soundOptions`：[`WorldSoundOptions`](./worldsoundoptions.md)|`undefined`

- script_api.@minecraft/server.world.soundoptions.playsound.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.playsound.return


////

///


/// define
`queueMusic`


///

script_api.@minecraft/server.world.queuemusic.description

```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.@minecraft/server.world.trackid.queuemusic.description


////

//// define
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

- script_api.@minecraft/server.world.musicoptions.queuemusic.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.queuemusic.return


////

///


/// define
`sendMessage`


///

script_api.@minecraft/server.world.sendmessage.description

```js
sendMessage(message: (RawMessage | string)[] | RawMessage | string): void
```

/// html | div.result
//// define
`message`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.world.message.sendmessage.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.sendmessage.return


////

///


/// define
`stopMusic`


///

script_api.@minecraft/server.world.stopmusic.description

```js
stopMusic(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.world.stopmusic.return


////

///

