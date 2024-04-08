# `Player`

> 文档版本：1.21.0.20

`Player`类。

## 属性

/// define
`camera`


///

```js
read-only camera: Camera
```


/// define
`inputPermissions`


///

```js
read-only inputPermissions: PlayerInputPermissions
```


/// define
`isEmoting`


///

```js
read-only isEmoting: boolean
```


/// define
`isFlying`


///

```js
read-only isFlying: boolean
```


/// define
`isGliding`


///

```js
read-only isGliding: boolean
```


/// define
`isJumping`


///

```js
read-only isJumping: boolean
```


/// define
`level`


///

```js
read-only level: int32
```


/// define
`name`


///

```js
read-only name: string
```


/// define
`onScreenDisplay`


///

```js
read-only onScreenDisplay: ScreenDisplay
```


/// define
`selectedSlot`


///

```js
selectedSlot: int32
```


/// define
`totalXpNeededForNextLevel`


///

```js
read-only totalXpNeededForNextLevel: int32
```


/// define
`xpEarnedAtCurrentLevel`


///

```js
read-only xpEarnedAtCurrentLevel: int32
```


## 方法

/// define
`addExperience`


///

```js
addExperience(amount: int32): uint32
```


/// define
`addLevels`


///

```js
addLevels(amount: int32): int32
```


/// define
`eatItem`


///

```js
eatItem(itemStack: ItemStack): void
```


/// define
`getGameMode`


///

```js
getGameMode(): GameMode
```


/// define
`getItemCooldown`


///

```js
getItemCooldown(cooldownCategory: string): int32
```


/// define
`getSpawnPoint`


///

```js
getSpawnPoint(): DimensionLocation | undefined
```


/// define
`getTotalXp`


///

```js
getTotalXp(): uint32
```


/// define
`isOp`


///

```js
isOp(): boolean
```


/// define
`playMusic`


///

```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```


/// define
`playSound`


///

```js
playSound(soundId: string, soundOptions?: PlayerSoundOptions): void
```


/// define
`postClientMessage`


///

```js
postClientMessage(id: string, value: string): void
```


/// define
`queueMusic`


///

```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```


/// define
`resetLevel`


///

```js
resetLevel(): void
```


/// define
`sendMessage`


///

```js
sendMessage(message: RawMessage | string[] | RawMessage | string): void
```


/// define
`setGameMode`


///

```js
setGameMode(gameMode?: GameMode): void
```


/// define
`setOp`


///

```js
setOp(isOp: boolean): void
```


/// define
`setSpawnPoint`


///

```js
setSpawnPoint(spawnPoint?: DimensionLocation): void
```


/// define
`spawnParticle`


///

```js
spawnParticle(effectName: string, location: Vector3, molangVariables?: MolangVariableMap): void
```


/// define
`startItemCooldown`


///

```js
startItemCooldown(cooldownCategory: string, tickDuration: int32): void
```


/// define
`stopMusic`


///

```js
stopMusic(): void
```

