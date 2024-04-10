# `Player`

> 文档版本：1.21.0.20

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


## 方法

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
`soundOptions`：[`PlayerSoundOptions`](./playersoundoptions.md)|`undefined`

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

