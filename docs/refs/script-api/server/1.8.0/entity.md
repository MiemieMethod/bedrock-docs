# `Entity`

> 文档版本：1.21.50.25

`Entity`类。script_api.@minecraft/server.entity.description

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

- script_api.@minecraft/server.entity.dimension.description


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

- script_api.@minecraft/server.entity.id.description


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

- script_api.@minecraft/server.entity.isclimbing.description


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

- script_api.@minecraft/server.entity.isfalling.description


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

- script_api.@minecraft/server.entity.isinwater.description


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

- script_api.@minecraft/server.entity.isonground.description


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

- script_api.@minecraft/server.entity.issleeping.description


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

- script_api.@minecraft/server.entity.issneaking.description


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

- script_api.@minecraft/server.entity.issprinting.description


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

- script_api.@minecraft/server.entity.isswimming.description


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

- script_api.@minecraft/server.entity.location.description


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

- script_api.@minecraft/server.entity.nametag.description


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

- script_api.@minecraft/server.entity.scoreboardidentity.description


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

- script_api.@minecraft/server.entity.typeid.description


////

///


## 方法

/// define
`addEffect`


///

script_api.@minecraft/server.entity.addeffect.description

```js
addEffect(effectType: EffectType | string, duration: int32, options?: EntityEffectOptions): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.addeffect.effecttype.description


////

//// define
`duration`：`int32`∈[`1`, `20000000`]

- script_api.@minecraft/server.entity.addeffect.duration.description


////

//// define
`options`?：[`EntityEffectOptions`](./entityeffectoptions.md)＝`null`

- script_api.@minecraft/server.entity.addeffect.options.description


////

//// define
返回值：[`Effect`](./effect.md)|`undefined`

- script_api.@minecraft/server.entity.addeffect.return


////

///


/// define
`addTag`


///

script_api.@minecraft/server.entity.addtag.description

```js
addTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.entity.addtag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.addtag.return


////

///


/// define
`applyDamage`


///

script_api.@minecraft/server.entity.applydamage.description

```js
applyDamage(amount: float, options?: EntityApplyDamageByProjectileOptions | EntityApplyDamageOptions): boolean
```

/// html | div.result
//// define
`amount`：`float`

- script_api.@minecraft/server.entity.applydamage.amount.description


////

//// define
`options`?：[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)＝`null`

- script_api.@minecraft/server.entity.applydamage.options.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.applydamage.return


////

///


/// define
`applyImpulse`


///

script_api.@minecraft/server.entity.applyimpulse.description

```js
applyImpulse(vector: Vector3): void
```

/// html | div.result
//// define
`vector`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.applyimpulse.vector.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.applyimpulse.return


////

///


/// define
`applyKnockback`


///

script_api.@minecraft/server.entity.applyknockback.description

```js
applyKnockback(directionX: float, directionZ: float, horizontalStrength: float, verticalStrength: float): void
```

/// html | div.result
//// define
`directionX`：`float`

- script_api.@minecraft/server.entity.applyknockback.directionx.description


////

//// define
`directionZ`：`float`

- script_api.@minecraft/server.entity.applyknockback.directionz.description


////

//// define
`horizontalStrength`：`float`

- script_api.@minecraft/server.entity.applyknockback.horizontalstrength.description


////

//// define
`verticalStrength`：`float`

- script_api.@minecraft/server.entity.applyknockback.verticalstrength.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.applyknockback.return


////

///


/// define
`clearDynamicProperties`


///

script_api.@minecraft/server.entity.cleardynamicproperties.description

```js
clearDynamicProperties(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.entity.cleardynamicproperties.return


////

///


/// define
`clearVelocity`


///

script_api.@minecraft/server.entity.clearvelocity.description

```js
clearVelocity(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.entity.clearvelocity.return


////

///


/// define
`getBlockFromViewDirection`


///

script_api.@minecraft/server.entity.getblockfromviewdirection.description

```js
getBlockFromViewDirection(options?: BlockRaycastOptions): BlockRaycastHit | undefined
```

/// html | div.result
//// define
`options`?：[`BlockRaycastOptions`](./blockraycastoptions.md)＝`null`

- script_api.@minecraft/server.entity.getblockfromviewdirection.options.description


////

//// define
返回值：[`BlockRaycastHit`](./blockraycasthit.md)|`undefined`

- script_api.@minecraft/server.entity.getblockfromviewdirection.return


////

///


/// define
`getComponent`


///

script_api.@minecraft/server.entity.getcomponent.description

```js
getComponent(componentId: string): EntityComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.entity.getcomponent.componentid.description


////

//// define
返回值：[`EntityComponent`](./entitycomponent.md)|`undefined`

- script_api.@minecraft/server.entity.getcomponent.return


////

///


/// define
`getComponents`


///

script_api.@minecraft/server.entity.getcomponents.description

```js
getComponents(): EntityComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../entitycomponent/">EntityComponent</a>[]</code>

- script_api.@minecraft/server.entity.getcomponents.return


////

///


/// define
`getDynamicProperty`


///

script_api.@minecraft/server.entity.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | string | Vector3 | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.entity.getdynamicproperty.identifier.description


////

//// define
返回值：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)|`undefined`

- script_api.@minecraft/server.entity.getdynamicproperty.return


////

///


/// define
`getDynamicPropertyIds`


///

script_api.@minecraft/server.entity.getdynamicpropertyids.description

```js
getDynamicPropertyIds(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.entity.getdynamicpropertyids.return


////

///


/// define
`getDynamicPropertyTotalByteCount`


///

script_api.@minecraft/server.entity.getdynamicpropertytotalbytecount.description

```js
getDynamicPropertyTotalByteCount(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server.entity.getdynamicpropertytotalbytecount.return


////

///


/// define
`getEffect`


///

script_api.@minecraft/server.entity.geteffect.description

```js
getEffect(effectType: EffectType | string): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.geteffect.effecttype.description


////

//// define
返回值：[`Effect`](./effect.md)|`undefined`

- script_api.@minecraft/server.entity.geteffect.return


////

///


/// define
`getEffects`


///

script_api.@minecraft/server.entity.geteffects.description

```js
getEffects(): Effect[]
```

/// html | div.result
//// define
返回值：<code><a href="../effect/">Effect</a>[]</code>

- script_api.@minecraft/server.entity.geteffects.return


////

///


/// define
`getEntitiesFromViewDirection`


///

script_api.@minecraft/server.entity.getentitiesfromviewdirection.description

```js
getEntitiesFromViewDirection(options?: EntityRaycastOptions): EntityRaycastHit[]
```

/// html | div.result
//// define
`options`?：[`EntityRaycastOptions`](./entityraycastoptions.md)＝`null`

- script_api.@minecraft/server.entity.getentitiesfromviewdirection.options.description


////

//// define
返回值：<code><a href="../entityraycasthit/">EntityRaycastHit</a>[]</code>

- script_api.@minecraft/server.entity.getentitiesfromviewdirection.return


////

///


/// define
`getHeadLocation`


///

script_api.@minecraft/server.entity.getheadlocation.description

```js
getHeadLocation(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getheadlocation.return


////

///


/// define
`getProperty`


///

script_api.@minecraft/server.entity.getproperty.description

```js
getProperty(identifier: string): boolean | float | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.entity.getproperty.identifier.description


////

//// define
返回值：`boolean`|`float`|`string`|`undefined`

- script_api.@minecraft/server.entity.getproperty.return


////

///


/// define
`getRotation`


///

script_api.@minecraft/server.entity.getrotation.description

```js
getRotation(): Vector2
```

/// html | div.result
//// define
返回值：[`Vector2`](./vector2.md)

- script_api.@minecraft/server.entity.getrotation.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.entity.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.entity.gettags.return


////

///


/// define
`getVelocity`


///

script_api.@minecraft/server.entity.getvelocity.description

```js
getVelocity(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getvelocity.return


////

///


/// define
`getViewDirection`


///

script_api.@minecraft/server.entity.getviewdirection.description

```js
getViewDirection(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.getviewdirection.return


////

///


/// define
`hasComponent`


///

script_api.@minecraft/server.entity.hascomponent.description

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.entity.hascomponent.componentid.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.hascomponent.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.entity.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.entity.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.hastag.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.entity.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.isvalid.return


////

///


/// define
`kill`


///

script_api.@minecraft/server.entity.kill.description

```js
kill(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.kill.return


////

///


/// define
`matches`


///

script_api.@minecraft/server.entity.matches.description

```js
matches(options: EntityQueryOptions): boolean
```

/// html | div.result
//// define
`options`：[`EntityQueryOptions`](./entityqueryoptions.md)

- script_api.@minecraft/server.entity.matches.options.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.matches.return


////

///


/// define
`remove`


///

script_api.@minecraft/server.entity.remove.description

```js
remove(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server.entity.remove.return


////

///


/// define
`removeEffect`


///

script_api.@minecraft/server.entity.removeeffect.description

```js
removeEffect(effectType: EffectType | string): boolean
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.removeeffect.effecttype.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.removeeffect.return


////

///


/// define
`removeTag`


///

script_api.@minecraft/server.entity.removetag.description

```js
removeTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.entity.removetag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.removetag.return


////

///


/// define
`resetProperty`


///

script_api.@minecraft/server.entity.resetproperty.description

```js
resetProperty(identifier: string): boolean | float | string
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.entity.resetproperty.identifier.description


////

//// define
返回值：`boolean`|`float`|`string`

- script_api.@minecraft/server.entity.resetproperty.return


////

///


/// define
`runCommand`


///

script_api.@minecraft/server.entity.runcommand.description

```js
runCommand(commandString: string): CommandResult
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.@minecraft/server.entity.runcommand.commandstring.description


////

//// define
返回值：[`CommandResult`](./commandresult.md)

- script_api.@minecraft/server.entity.runcommand.return


////

///


/// define
`runCommandAsync`


///

script_api.@minecraft/server.entity.runcommandasync.description

```js
runCommandAsync(commandString: string): Promise<CommandResult>
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.@minecraft/server.entity.runcommandasync.commandstring.description


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- script_api.@minecraft/server.entity.runcommandasync.return


////

///


/// define
`setDynamicProperty`


///

script_api.@minecraft/server.entity.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value?: boolean | double | float | string | Vector3): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.entity.setdynamicproperty.identifier.description


////

//// define
`value`?：`boolean`|`double`|`float`|`string`|[`Vector3`](./vector3.md)＝`null`

- script_api.@minecraft/server.entity.setdynamicproperty.value.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.setdynamicproperty.return


////

///


/// define
`setProperty`


///

script_api.@minecraft/server.entity.setproperty.description

```js
setProperty(identifier: string, value: boolean | float | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.@minecraft/server.entity.setproperty.identifier.description


////

//// define
`value`：`boolean`|`float`|`string`

- script_api.@minecraft/server.entity.setproperty.value.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.setproperty.return


////

///


/// define
`setRotation`


///

script_api.@minecraft/server.entity.setrotation.description

```js
setRotation(rotation: Vector2): void
```

/// html | div.result
//// define
`rotation`：[`Vector2`](./vector2.md)

- script_api.@minecraft/server.entity.setrotation.rotation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.setrotation.return


////

///


/// define
`teleport`


///

script_api.@minecraft/server.entity.teleport.description

```js
teleport(location: Vector3, teleportOptions?: TeleportOptions): void
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.teleport.location.description


////

//// define
`teleportOptions`?：[`TeleportOptions`](./teleportoptions.md)＝`null`

- script_api.@minecraft/server.entity.teleport.teleportoptions.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.teleport.return


////

///


/// define
`triggerEvent`


///

script_api.@minecraft/server.entity.triggerevent.description

```js
triggerEvent(eventName: string): void
```

/// html | div.result
//// define
`eventName`：`string`

- script_api.@minecraft/server.entity.triggerevent.eventname.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.triggerevent.return


////

///


/// define
`tryTeleport`


///

script_api.@minecraft/server.entity.tryteleport.description

```js
tryTeleport(location: Vector3, teleportOptions?: TeleportOptions): boolean
```

/// html | div.result
//// define
`location`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.entity.tryteleport.location.description


////

//// define
`teleportOptions`?：[`TeleportOptions`](./teleportoptions.md)＝`null`

- script_api.@minecraft/server.entity.tryteleport.teleportoptions.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.tryteleport.return


////

///

