# `Player`

> 文档版本：1.21.0.20

`Player`类，扩展自`Entity`。

## 属性

/// define
`camera`


///

```js
read-only camera: Camera;
```


/// define
`inputPermissions`


///

```js
read-only inputPermissions: PlayerInputPermissions;
```


/// define
`isEmoting`


///

```js
read-only isEmoting: boolean;
```


/// define
`isFlying`


///

```js
read-only isFlying: boolean;
```


/// define
`isGliding`


///

```js
read-only isGliding: boolean;
```


/// define
`isJumping`


///

```js
read-only isJumping: boolean;
```


/// define
`level`


///

```js
read-only level: int32;
```


/// define
`name`


///

```js
read-only name: string;
```


/// define
`onScreenDisplay`


///

```js
read-only onScreenDisplay: ScreenDisplay;
```


/// define
`selectedSlot`


///

```js
selectedSlot: int32;
```


/// define
`totalXpNeededForNextLevel`


///

```js
read-only totalXpNeededForNextLevel: int32;
```


/// define
`xpEarnedAtCurrentLevel`


///

```js
read-only xpEarnedAtCurrentLevel: int32;
```


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
`eatItem`


///

```js
eatItem(itemStack: ItemStack): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](./itemstack.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`getGameMode`


///

```js
getGameMode(): GameMode
```

/// html | div.result

///


/// define
`getItemCooldown`


///

```js
getItemCooldown(cooldownCategory: string): int32
```

/// html | div.result
//// define
`cooldownCategory`：`string`

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

///


/// define
`getTotalXp`


///

```js
getTotalXp(): uint32
```

/// html | div.result

///


/// define
`isOp`


///

```js
isOp(): boolean
```

/// html | div.result

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
`postClientMessage`


///

```js
postClientMessage(id: string, value: string): void
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

///


/// define
`sendMessage`


///

```js
sendMessage(message: RawMessage | string[] | RawMessage | string): void
```

/// html | div.result
//// define
`message`：RawMessage | string[]|RawMessage|string

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setGameMode`


///

```js
setGameMode(gameMode?: GameMode): void
```

/// html | div.result
//// define
`gameMode`：[`GameMode`](./gamemode.md)|`undefined`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setOp`


///

```js
setOp(isOp: boolean): void
```

/// html | div.result
//// define
`isOp`：`boolean`

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
`spawnParticle`


///

```js
spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void
```

/// html | div.result
//// define
`effectName`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](./vector3.md)

- 参数2。


////

//// define
`molangVariables`：[`MolangVariableMap`](./molangvariablemap.md)|`undefined`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`startItemCooldown`


///

```js
startItemCooldown(cooldownCategory: string, tickDuration: int32): void
```

/// html | div.result
//// define
`cooldownCategory`：`string`

- 参数1。


////

//// define
`tickDuration`：`int32`

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

///

