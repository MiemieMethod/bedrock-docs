# `Player`

> 文档版本：1.21.50.25

`Player`类，扩展自[`Entity`](./entity.md)。script_api.@minecraft/server.player.description

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

- script_api.@minecraft/server.player.camera.description


////

///


/// define
`inputPermissions`


///

```js
read-only inputPermissions: PlayerInputPermissions;
```

/// html | div.result
//// define
`inputPermissions`：[`PlayerInputPermissions`](./playerinputpermissions.md)

- script_api.@minecraft/server.player.inputpermissions.description


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

- script_api.@minecraft/server.player.isemoting.description


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

- script_api.@minecraft/server.player.isflying.description


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

- script_api.@minecraft/server.player.isgliding.description


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

- script_api.@minecraft/server.player.isjumping.description


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

- script_api.@minecraft/server.player.level.description


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


/// define
`selectedSlotIndex`


///

```js
selectedSlotIndex: int32;
```

/// html | div.result
//// define
`selectedSlotIndex`：`int32`

- script_api.@minecraft/server.player.selectedslotindex.description


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

- script_api.@minecraft/server.player.totalxpneededfornextlevel.description


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

- script_api.@minecraft/server.player.xpearnedatcurrentlevel.description


////

///


## 方法

/// define
`addExperience`


///

script_api.@minecraft/server.player.addexperience.description

```js
addExperience(amount: int32): uint32
```

/// html | div.result
//// define
`amount`：`int32`∈[`-16777216`, `16777216`]

- script_api.@minecraft/server.player.addexperience.amount.description


////

//// define
返回值：`uint32`

- script_api.@minecraft/server.player.addexperience.return


////

///


/// define
`addLevels`


///

script_api.@minecraft/server.player.addlevels.description

```js
addLevels(amount: int32): int32
```

/// html | div.result
//// define
`amount`：`int32`∈[`-16777216`, `16777216`]

- script_api.@minecraft/server.player.addlevels.amount.description


////

//// define
返回值：`int32`

- script_api.@minecraft/server.player.addlevels.return


////

///


/// define
`getGameMode`


///

script_api.@minecraft/server.player.getgamemode.description

```js
getGameMode(): GameMode
```

/// html | div.result
//// define
返回值：[`GameMode`](./gamemode.md)

- script_api.@minecraft/server.player.getgamemode.return


////

///


/// define
`getItemCooldown`


///

script_api.@minecraft/server.player.getitemcooldown.description

```js
getItemCooldown(cooldownCategory: string): int32
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.@minecraft/server.player.getitemcooldown.cooldowncategory.description


////

//// define
返回值：`int32`

- script_api.@minecraft/server.player.getitemcooldown.return


////

///


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
`getTotalXp`


///

script_api.@minecraft/server.player.gettotalxp.description

```js
getTotalXp(): uint32
```

/// html | div.result
//// define
返回值：`uint32`

- script_api.@minecraft/server.player.gettotalxp.return


////

///


/// define
`playMusic`


///

script_api.@minecraft/server.player.playmusic.description

```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.@minecraft/server.player.playmusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.@minecraft/server.player.playmusic.musicoptions.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.playmusic.return


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
`queueMusic`


///

script_api.@minecraft/server.player.queuemusic.description

```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```

/// html | div.result
//// define
`trackId`：`string`

- script_api.@minecraft/server.player.queuemusic.trackid.description


////

//// define
`musicOptions`?：[`MusicOptions`](./musicoptions.md)＝`null`

- script_api.@minecraft/server.player.queuemusic.musicoptions.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.queuemusic.return


////

///


/// define
`resetLevel`


///

script_api.@minecraft/server.player.resetlevel.description

```js
resetLevel(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.player.resetlevel.return


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
`setGameMode`


///

script_api.@minecraft/server.player.setgamemode.description

```js
setGameMode(gameMode?: GameMode): void
```

/// html | div.result
//// define
`gameMode`?：[`GameMode`](./gamemode.md)＝`null`

- script_api.@minecraft/server.player.setgamemode.gamemode.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.setgamemode.return


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


/// define
`startItemCooldown`


///

script_api.@minecraft/server.player.startitemcooldown.description

```js
startItemCooldown(cooldownCategory: string, tickDuration: int32): void
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- script_api.@minecraft/server.player.startitemcooldown.cooldowncategory.description


////

//// define
`tickDuration`：`int32`∈[`0`, `32767`]

- script_api.@minecraft/server.player.startitemcooldown.tickduration.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.player.startitemcooldown.return


////

///


/// define
`stopMusic`


///

script_api.@minecraft/server.player.stopmusic.description

```js
stopMusic(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.player.stopmusic.return


////

///

