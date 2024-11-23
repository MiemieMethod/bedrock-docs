# `Player`

> 文档版本：1.21.60.21

`Player`类，扩展自[`Entity`](./entity.md)。script_api.@minecraft/server.player.description

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

- script_api.@minecraft/server.player.name.description


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

- script_api.@minecraft/server.player.onscreendisplay.description


////

///


## 方法

/// define
`getSpawnPoint`


///

script_api.@minecraft/server.player.getspawnpoint.description

```js
getSpawnPoint(): DimensionLocation | undefined
```

/// html | div.result
//// define
返回值：[`DimensionLocation`](./dimensionlocation.md)|`undefined`

- script_api.@minecraft/server.player.getspawnpoint.return


////

///


/// define
`playSound`


///

script_api.@minecraft/server.player.playsound.description

```js
playSound(soundId: string, soundOptions?: PlayerSoundOptions): void
```

/// html | div.result
//// define
`soundId`：`string`

- script_api.@minecraft/server.player.playsound.soundid.description


////

//// define
`soundOptions`?：[`PlayerSoundOptions`](./playersoundoptions.md)＝`null`

- script_api.@minecraft/server.player.playsound.soundoptions.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.playsound.return


////

///


/// define
`sendMessage`


///

script_api.@minecraft/server.player.sendmessage.description

```js
sendMessage(message: (RawMessage | string)[] | RawMessage | string): void
```

/// html | div.result
//// define
`message`：`(RawMessage | string)[]`|[`RawMessage`](./rawmessage.md)|`string`

- script_api.@minecraft/server.player.sendmessage.message.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.sendmessage.return


////

///


/// define
`setSpawnPoint`


///

script_api.@minecraft/server.player.setspawnpoint.description

```js
setSpawnPoint(spawnPoint?: DimensionLocation): void
```

/// html | div.result
//// define
`spawnPoint`?：[`DimensionLocation`](./dimensionlocation.md)＝`null`

- script_api.@minecraft/server.player.setspawnpoint.spawnpoint.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.setspawnpoint.return


////

///

