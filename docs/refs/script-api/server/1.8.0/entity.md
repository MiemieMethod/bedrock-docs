# `Entity`

> 文档版本：1.21.0.20

`Entity`类。

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension;
```

/// html | div.result
//// define
`dimension`：[`Dimension`](./dimension.md)

- 属性。


////

///


/// define
`id`


///

```js
read-only id: string;
```

/// html | div.result
//// define
`id`：`string`

- 属性。


////

///


/// define
`isClimbing`


///

```js
read-only isClimbing: boolean;
```

/// html | div.result
//// define
`isClimbing`：`boolean`

- 属性。


////

///


/// define
`isFalling`


///

```js
read-only isFalling: boolean;
```

/// html | div.result
//// define
`isFalling`：`boolean`

- 属性。


////

///


/// define
`isInWater`


///

```js
read-only isInWater: boolean;
```

/// html | div.result
//// define
`isInWater`：`boolean`

- 属性。


////

///


/// define
`isOnGround`


///

```js
read-only isOnGround: boolean;
```

/// html | div.result
//// define
`isOnGround`：`boolean`

- 属性。


////

///


/// define
`isSleeping`


///

```js
read-only isSleeping: boolean;
```

/// html | div.result
//// define
`isSleeping`：`boolean`

- 属性。


////

///


/// define
`isSneaking`


///

```js
isSneaking: boolean;
```

/// html | div.result
//// define
`isSneaking`：`boolean`

- 属性。


////

///


/// define
`isSprinting`


///

```js
read-only isSprinting: boolean;
```

/// html | div.result
//// define
`isSprinting`：`boolean`

- 属性。


////

///


/// define
`isSwimming`


///

```js
read-only isSwimming: boolean;
```

/// html | div.result
//// define
`isSwimming`：`boolean`

- 属性。


////

///


/// define
`location`


///

```js
read-only location: Vector3;
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 属性。


////

///


/// define
`nameTag`


///

```js
nameTag: string;
```

/// html | div.result
//// define
`nameTag`：`string`

- 属性。


////

///


/// define
`scoreboardIdentity`


///

```js
read-only scoreboardIdentity: ScoreboardIdentity | undefined;
```

/// html | div.result
//// define
`scoreboardIdentity`：[`ScoreboardIdentity`](./scoreboardidentity.md)|`undefined`

- 属性。


////

///


/// define
`typeId`


///

```js
read-only typeId: string;
```

/// html | div.result
//// define
`typeId`：`string`

- 属性。


////

///


## 方法

/// define
`addEffect`


///

```js
addEffect(effectType: EffectType | string, duration: int32, options?: EntityEffectOptions): void
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- 参数1。


////

//// define
`duration`：`int32`

- 参数2。


////

//// define
`options`：[`EntityEffectOptions`](./entityeffectoptions.md)|`undefined`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`addTag`


///

```js
addTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`applyDamage`


///

```js
applyDamage(amount: float, options?: EntityApplyDamageByProjectileOptions | EntityApplyDamageOptions): boolean
```

/// html | div.result
//// define
`amount`：`float`

- 参数1。


////

//// define
`options`：[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`applyImpulse`


///

```js
applyImpulse(vector: Vector3): void
```

/// html | div.result
//// define
`vector`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`applyKnockback`


///

```js
applyKnockback(directionX: float, directionZ: float, horizontalStrength: float, verticalStrength: float): void
```

/// html | div.result
//// define
`directionX`：`float`

- 参数1。


////

//// define
`directionZ`：`float`

- 参数2。


////

//// define
`horizontalStrength`：`float`

- 参数3。


////

//// define
`verticalStrength`：`float`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`clearDynamicProperties`


///

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`clearVelocity`


///

```js
clearVelocity(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`getBlockFromViewDirection`


///

```js
getBlockFromViewDirection(options?: BlockRaycastOptions): BlockRaycastHit | undefined
```

/// html | div.result
//// define
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：[`BlockRaycastHit`](./blockraycasthit.md)|`undefined`

- 返回值。


////

///


/// define
`getComponent`


///

```js
getComponent(componentId: string): EntityComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：[`EntityComponent`](./entitycomponent.md)|`undefined`

- 返回值。


////

///


/// define
`getComponents`


///

```js
getComponents(): EntityComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../entitycomponent/">EntityComponent</a>[]</code>

- 返回值。


////

///


/// define
`getDynamicProperty`


///

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- 返回值。


////

///


/// define
`getDynamicPropertyIds`


///

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`getEffect`


///

```js
getEffect(effectType: EffectType | string): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- 参数1。


////

//// define
返回值：[`Effect`](./effect.md)|`undefined`

- 返回值。


////

///


/// define
`getEffects`


///

```js
getEffects(): Effect[]
```

/// html | div.result
//// define
返回值：<code><a href="../effect/">Effect</a>[]</code>

- 返回值。


////

///


/// define
`getEntitiesFromViewDirection`


///

```js
getEntitiesFromViewDirection(options?: EntityRaycastOptions): EntityRaycastHit[]
```

/// html | div.result
//// define
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：<code><a href="../entityraycasthit/">EntityRaycastHit</a>[]</code>

- 返回值。


////

///


/// define
`getHeadLocation`


///

```js
getHeadLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getProperty`


///

```js
getProperty(identifier: string): boolean | float | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`float`|`string`|`undefined`

- 返回值。


////

///


/// define
`getRotation`


///

```js
getRotation(): Vector2
```

/// html | div.result
//// define
返回值：[`Vector2`](./vector2.md)

- 返回值。


////

///


/// define
`getTags`


///

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 返回值。


////

///


/// define
`getVelocity`


///

```js
getVelocity(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`getViewDirection`


///

```js
getViewDirection(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 返回值。


////

///


/// define
`hasComponent`


///

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`hasTag`


///

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`kill`


///

```js
kill(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`matches`


///

```js
matches(options: EntityQueryOptions): boolean
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`remove`


///

```js
remove(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`removeEffect`


///

```js
removeEffect(effectType: EffectType | string): boolean
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`removeTag`


///

```js
removeTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`resetProperty`


///

```js
resetProperty(identifier: string): boolean | float | string
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`float`|`string`

- 返回值。


////

///


/// define
`runCommand`


///

```js
runCommand(commandString: string): CommandResult
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：[`CommandResult`](./commandresult.md)

- 返回值。


////

///


/// define
`runCommandAsync`


///

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- 返回值。


////

///


/// define
`setDynamicProperty`


///

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setProperty`


///

```js
setProperty(identifier: string, value: boolean | float | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`float`|`string`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setRotation`


///

```js
setRotation(rotation: Vector2): void
```

/// html | div.result
//// define
`rotation`：[`Vector2`](./vector2.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`teleport`


///

```js
teleport(location: Vector3, teleportOptions?: TeleportOptions): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`teleportOptions`：[`TeleportOptions`](./teleportoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`triggerEvent`


///

```js
triggerEvent(eventName: string): void
```

/// html | div.result
//// define
`eventName`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`tryTeleport`


///

```js
tryTeleport(location: Vector3, teleportOptions?: TeleportOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
`teleportOptions`：[`TeleportOptions`](./teleportoptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///

