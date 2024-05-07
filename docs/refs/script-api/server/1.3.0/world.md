# `World`

> 文档版本：1.21.0.24

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

- script_api.@minecraft/server.world.getdimension.dimensionid.description


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
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.@minecraft/server.world.getplayers.options.description


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

- script_api.@minecraft/server.world.playmusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.@minecraft/server.world.playmusic.musicoptions.description


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

- script_api.@minecraft/server.world.playsound.soundid.description


////

//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.world.playsound.location.description


////

//// define
`soundOptions`?：[`WorldSoundOptions`](./worldsoundoptions.md)＝`null`

- script_api.@minecraft/server.world.playsound.soundoptions.description


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

- script_api.@minecraft/server.world.queuemusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.@minecraft/server.world.queuemusic.musicoptions.description


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

- script_api.@minecraft/server.world.sendmessage.message.description


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

