# `World`

> 文档版本：1.21.0.20

`World`类。

## 属性

/// define
afterEvents

- ```js
read-only afterEvents: WorldAfterEvents
```



///


/// define
beforeEvents

- ```js
read-only beforeEvents: WorldBeforeEvents
```



///


/// define
gameRules

- ```js
read-only gameRules: GameRules
```



///


/// define
scoreboard

- ```js
read-only scoreboard: Scoreboard
```



///


/// define
structureManager

- ```js
read-only structureManager: StructureManager
```



///


## 方法

/// define
broadcastClientMessage

- ```js
broadcastClientMessage(id: string, value: string): void
```



///


/// define
clearDynamicProperties

- ```js
clearDynamicProperties(): void
```



///


/// define
getAbsoluteTime

- ```js
getAbsoluteTime(): int32
```



///


/// define
getAllPlayers

- ```js
getAllPlayers(): Player[]
```



///


/// define
getDay

- ```js
getDay(): int32
```



///


/// define
getDefaultSpawnLocation

- ```js
getDefaultSpawnLocation(): Vector3
```



///


/// define
getDimension

- ```js
getDimension(dimensionId: string): Dimension
```



///


/// define
getDynamicProperty

- ```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```



///


/// define
getDynamicPropertyIds

- ```js
getDynamicPropertyIds(): string[]
```



///


/// define
getDynamicPropertyTotalByteCount

- ```js
getDynamicPropertyTotalByteCount(): int32
```



///


/// define
getEntity

- ```js
getEntity(id: string): Entity | undefined
```



///


/// define
getMoonPhase

- ```js
getMoonPhase(): MoonPhase
```



///


/// define
getPlayers

- ```js
getPlayers(options?: EntityQueryOptions): Player[]
```



///


/// define
getTimeOfDay

- ```js
getTimeOfDay(): int32
```



///


/// define
playMusic

- ```js
playMusic(trackId: string, musicOptions?: MusicOptions): void
```



///


/// define
playSound

- ```js
playSound(soundId: string, location: Vector3, soundOptions?: WorldSoundOptions): void
```



///


/// define
queueMusic

- ```js
queueMusic(trackId: string, musicOptions?: MusicOptions): void
```



///


/// define
sendMessage

- ```js
sendMessage(message: RawMessage | string[] | RawMessage | string): void
```



///


/// define
setAbsoluteTime

- ```js
setAbsoluteTime(absoluteTime: int32): void
```



///


/// define
setDefaultSpawnLocation

- ```js
setDefaultSpawnLocation(spawnLocation: Vector3): void
```



///


/// define
setDynamicProperty

- ```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```



///


/// define
setTimeOfDay

- ```js
setTimeOfDay(timeOfDay: int32 | TimeOfDay): void
```



///


/// define
stopMusic

- ```js
stopMusic(): void
```



///

