# `World`

> 文档版本：1.21.0.20

`World`类。script_api.@minecraft/server.world.description

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

- script_api.@minecraft/server.world.afterevents.description


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

- script_api.@minecraft/server.world.beforeevents.description


////

///


/// define
`gameRules`


///

```js
read-only gameRules: GameRules;
```

/// html | div.result
//// define
`gameRules`：[`GameRules`](./gamerules.md)

- script_api.@minecraft/server.world.gamerules.description


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

- script_api.@minecraft/server.world.scoreboard.description


////

///


/// define
`structureManager`


///

```js
read-only structureManager: StructureManager;
```

/// html | div.result
//// define
`structureManager`：[`StructureManager`](./structuremanager.md)

- script_api.@minecraft/server.world.structuremanager.description


////

///


## 方法

/// define
`broadcastClientMessage`


///

script_api.@minecraft/server.world.broadcastclientmessage.description

```js
broadcastClientMessage(id: string, value: string): void
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server.world.broadcastclientmessage.id.description


////

//// define
`value`：`string`

- script_api.@minecraft/server.world.broadcastclientmessage.value.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.broadcastclientmessage.return


////

///


/// define
`clearDynamicProperties`


///

script_api.@minecraft/server.world.cleardynamicproperties.description

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.world.cleardynamicproperties.return


////

///


/// define
`getAbsoluteTime`


///

script_api.@minecraft/server.world.getabsolutetime.description

```js
getAbsoluteTime(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.world.getabsolutetime.return


////

///


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
`getDay`


///

script_api.@minecraft/server.world.getday.description

```js
getDay(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.world.getday.return


////

///


/// define
`getDefaultSpawnLocation`


///

script_api.@minecraft/server.world.getdefaultspawnlocation.description

```js
getDefaultSpawnLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.world.getdefaultspawnlocation.return


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
`getDynamicProperty`


///

script_api.@minecraft/server.world.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.world.getdynamicproperty.identifier.description


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.world.getdynamicproperty.return


////

///


/// define
`getDynamicPropertyIds`


///

script_api.@minecraft/server.world.getdynamicpropertyids.description

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.world.getdynamicpropertyids.return


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

script_api.@minecraft/server.world.getdynamicpropertytotalbytecount.description

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.world.getdynamicpropertytotalbytecount.return


////

///


/// define
`getEntity`


///

script_api.@minecraft/server.world.getentity.description

```js
getEntity(id: string): Entity | undefined
```

/// html | div.result
//// define
`id`：`string`

- script_api.@minecraft/server.world.getentity.id.description


////

//// define
返回值：[`Entity`](./entity.md)|`undefined`

- script_api.@minecraft/server.world.getentity.return


////

///


/// define
`getMoonPhase`


///

script_api.@minecraft/server.world.getmoonphase.description

```js
getMoonPhase(): MoonPhase
```

/// html | div.result
//// define
返回值：[`MoonPhase`](./moonphase.md)

- script_api.@minecraft/server.world.getmoonphase.return


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

- script_api.@minecraft/server.world.getplayers.options.description


////

//// define
返回值：<code><a href="../player/">Player</a>[]</code>

- script_api.@minecraft/server.world.getplayers.return


////

///


/// define
`getTimeOfDay`


///

script_api.@minecraft/server.world.gettimeofday.description

```js
getTimeOfDay(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.world.gettimeofday.return


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
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

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
`soundOptions`：[`WorldSoundOptions`](./worldsoundoptions.md)|`undefined`

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
`musicOptions`：[`MusicOptions`](./musicoptions.md)|`undefined`

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
`setAbsoluteTime`


///

script_api.@minecraft/server.world.setabsolutetime.description

```js
setAbsoluteTime(absoluteTime: int32): void
```

/// html | div.result
//// define
`absoluteTime`：`int32`

- script_api.@minecraft/server.world.setabsolutetime.absolutetime.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.setabsolutetime.return


////

///


/// define
`setDefaultSpawnLocation`


///

script_api.@minecraft/server.world.setdefaultspawnlocation.description

```js
setDefaultSpawnLocation(spawnLocation: Vector3): void
```

/// html | div.result
//// define
`spawnLocation`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.world.setdefaultspawnlocation.spawnlocation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.setdefaultspawnlocation.return


////

///


/// define
`setDynamicProperty`


///

script_api.@minecraft/server.world.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.world.setdynamicproperty.identifier.description


////

//// define
`value`：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.world.setdynamicproperty.value.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.setdynamicproperty.return


////

///


/// define
`setTimeOfDay`


///

script_api.@minecraft/server.world.settimeofday.description

```js
setTimeOfDay(timeOfDay: int32 | TimeOfDay): void
```

/// html | div.result
//// define
`timeOfDay`：`int32`|[`TimeOfDay`](./timeofday.md)

- script_api.@minecraft/server.world.settimeofday.timeofday.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.world.settimeofday.return


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

