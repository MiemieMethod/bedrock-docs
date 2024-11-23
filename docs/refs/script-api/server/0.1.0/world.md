# `World`

> 文档版本：1.21.60.21

`World`类。script_api.mojang-minecraft.world.description

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

- script_api.mojang-minecraft.world.events.description


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

- script_api.mojang-minecraft.world.scoreboard.description


////

///


## 方法

/// define
`broadcastClientMessage`


///

script_api.mojang-minecraft.world.broadcastclientmessage.description

```js
broadcastClientMessage(id: string, value: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.mojang-minecraft.world.broadcastclientmessage.id.description


////

//// define
`value`：`string`

- script_api.mojang-minecraft.world.broadcastclientmessage.value.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.world.broadcastclientmessage.return


////

///


/// define
`getDimension`


///

script_api.mojang-minecraft.world.getdimension.description

```js
getDimension(dimensionId: string): Dimension
```

/// html | div.result
//// define
`dimensionId`：`string`

- script_api.mojang-minecraft.world.getdimension.dimensionid.description


////

//// define
返回值：[`Dimension`](./dimension.md)

- script_api.mojang-minecraft.world.getdimension.return


////

///


/// define
`getDynamicProperty`


///

script_api.mojang-minecraft.world.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | Location | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.world.getdynamicproperty.identifier.description


////

//// define
返回值：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`|`undefined`

- script_api.mojang-minecraft.world.getdynamicproperty.return


////

///


/// define
`getPlayers`


///

script_api.mojang-minecraft.world.getplayers.description

```js
getPlayers(options?: EntityQueryOptions): PlayerIterator
```

/// html | div.result
//// define
`options`?：[`EntityQueryOptions`](./entityqueryoptions.md)＝`null`

- script_api.mojang-minecraft.world.getplayers.options.description


////

//// define
返回值：[`PlayerIterator`](./playeriterator.md)

- script_api.mojang-minecraft.world.getplayers.return


////

///


/// define
`playMusic`


///

script_api.mojang-minecraft.world.playmusic.description

```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.mojang-minecraft.world.playmusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.mojang-minecraft.world.playmusic.musicoptions.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.world.playmusic.return


////

///


/// define
`playSound`


///

script_api.mojang-minecraft.world.playsound.description

```js
playSound(soundID: string, soundOptions?: SoundOptions): void
```

/// html | div.result
//// define
`soundID`：`string`

- script_api.mojang-minecraft.world.playsound.soundid.description


////

//// define
`soundOptions`?：[`SoundOptions`](./soundoptions.md)＝`null`

- script_api.mojang-minecraft.world.playsound.soundoptions.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.world.playsound.return


////

///


/// define
`queueMusic`


///

script_api.mojang-minecraft.world.queuemusic.description

```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.mojang-minecraft.world.queuemusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.mojang-minecraft.world.queuemusic.musicoptions.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.world.queuemusic.return


////

///


/// define
`removeDynamicProperty`


///

script_api.mojang-minecraft.world.removedynamicproperty.description

```js
removeDynamicProperty(identifier: string): boolean
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.world.removedynamicproperty.identifier.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.world.removedynamicproperty.return


////

///


/// define
`setDynamicProperty`


///

script_api.mojang-minecraft.world.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value: boolean | double | float | Location | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.world.setdynamicproperty.identifier.description


////

//// define
`value`：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`

- script_api.mojang-minecraft.world.setdynamicproperty.value.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.world.setdynamicproperty.return


////

///


/// define
`stopMusic`


///

script_api.mojang-minecraft.world.stopmusic.description

```js
stopMusic(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.mojang-minecraft.world.stopmusic.return


////

///

