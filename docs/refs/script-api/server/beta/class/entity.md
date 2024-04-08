# `Entity`

> 文档版本：1.21.0.20

`Entity`类。

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension
```


/// define
`fallDistance`


///

```js
read-only fallDistance: float
```


/// define
`id`


///

```js
read-only id: string
```


/// define
`isClimbing`


///

```js
read-only isClimbing: boolean
```


/// define
`isFalling`


///

```js
read-only isFalling: boolean
```


/// define
`isInWater`


///

```js
read-only isInWater: boolean
```


/// define
`isOnGround`


///

```js
read-only isOnGround: boolean
```


/// define
`isSleeping`


///

```js
read-only isSleeping: boolean
```


/// define
`isSneaking`


///

```js
isSneaking: boolean
```


/// define
`isSprinting`


///

```js
read-only isSprinting: boolean
```


/// define
`isSwimming`


///

```js
read-only isSwimming: boolean
```


/// define
`lifetimeState`


///

```js
read-only lifetimeState: EntityLifetimeState
```


/// define
`location`


///

```js
read-only location: Vector3
```


/// define
`nameTag`


///

```js
nameTag: string
```


/// define
`scoreboardIdentity`


///

```js
read-only scoreboardIdentity: ScoreboardIdentity | undefined
```


/// define
`target`


///

```js
read-only target: Entity | undefined
```


/// define
`typeId`


///

```js
read-only typeId: string
```


## 方法

/// define
addEffect

- ```js
addEffect(effectType: EffectType | string, duration: int32, options?: EntityEffectOptions): Effect | undefined
```



///


/// define
addTag

- ```js
addTag(tag: string): boolean
```



///


/// define
applyDamage

- ```js
applyDamage(amount: float, options?: EntityApplyDamageByProjectileOptions | EntityApplyDamageOptions): boolean
```



///


/// define
applyImpulse

- ```js
applyImpulse(vector: Vector3): void
```



///


/// define
applyKnockback

- ```js
applyKnockback(directionX: float, directionZ: float, horizontalStrength: float, verticalStrength: float): void
```



///


/// define
clearDynamicProperties

- ```js
clearDynamicProperties(): void
```



///


/// define
clearVelocity

- ```js
clearVelocity(): void
```



///


/// define
extinguishFire

- ```js
extinguishFire(useEffects: boolean): boolean
```



///


/// define
getBlockFromViewDirection

- ```js
getBlockFromViewDirection(options?: BlockRaycastOptions): BlockRaycastHit | undefined
```



///


/// define
getComponent

- ```js
getComponent(componentId: string): EntityComponent | undefined
```



///


/// define
getComponents

- ```js
getComponents(): EntityComponent[]
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
getEffect

- ```js
getEffect(effectType: EffectType | string): Effect | undefined
```



///


/// define
getEffects

- ```js
getEffects(): Effect[]
```



///


/// define
getEntitiesFromViewDirection

- ```js
getEntitiesFromViewDirection(options?: EntityRaycastOptions): EntityRaycastHit[]
```



///


/// define
getHeadLocation

- ```js
getHeadLocation(): Vector3
```



///


/// define
getProperty

- ```js
getProperty(identifier: string): boolean | float | string | undefined
```



///


/// define
getRotation

- ```js
getRotation(): Vector2
```



///


/// define
getTags

- ```js
getTags(): string[]
```



///


/// define
getVelocity

- ```js
getVelocity(): Vector3
```



///


/// define
getViewDirection

- ```js
getViewDirection(): Vector3
```



///


/// define
hasComponent

- ```js
hasComponent(componentId: string): boolean
```



///


/// define
hasTag

- ```js
hasTag(tag: string): boolean
```



///


/// define
isValid

- ```js
isValid(): boolean
```



///


/// define
kill

- ```js
kill(): boolean
```



///


/// define
matches

- ```js
matches(options: EntityQueryOptions): boolean
```



///


/// define
playAnimation

- ```js
playAnimation(animationName: string, options?: PlayAnimationOptions): void
```



///


/// define
remove

- ```js
remove(): void
```



///


/// define
removeEffect

- ```js
removeEffect(effectType: EffectType | string): boolean
```



///


/// define
removeTag

- ```js
removeTag(tag: string): boolean
```



///


/// define
resetProperty

- ```js
resetProperty(identifier: string): boolean | float | string
```



///


/// define
runCommand

- ```js
runCommand(commandString: string): CommandResult
```



///


/// define
runCommandAsync

- ```js
runCommandAsync(commandString: string): Promise<CommandResult>
```



///


/// define
setDynamicProperty

- ```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```



///


/// define
setOnFire

- ```js
setOnFire(seconds: int32, useEffects: boolean): boolean
```



///


/// define
setProperty

- ```js
setProperty(identifier: string, value: boolean | float | string): void
```



///


/// define
setRotation

- ```js
setRotation(rotation: Vector2): void
```



///


/// define
teleport

- ```js
teleport(location: Vector3, teleportOptions?: TeleportOptions): void
```



///


/// define
triggerEvent

- ```js
triggerEvent(eventName: string): void
```



///


/// define
tryTeleport

- ```js
tryTeleport(location: Vector3, teleportOptions?: TeleportOptions): boolean
```



///

