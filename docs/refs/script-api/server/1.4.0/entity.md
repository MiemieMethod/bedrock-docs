# `Entity`

> 文档版本：1.21.0.20

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
addEffect(effectType: EffectType | string, duration: int32, options?: EntityEffectOptions): void
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.effecttype.addeffect.description


////

//// define
`duration`：`int32`

- script_api.@minecraft/server.entity.duration.addeffect.description


////

//// define
`options`：[`EntityEffectOptions`](./entityeffectoptions.md)|`undefined`

- script_api.@minecraft/server.entity.options.addeffect.description


////

//// define
返回值：`void`

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

- script_api.@minecraft/server.entity.tag.addtag.description


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

- script_api.@minecraft/server.entity.amount.applydamage.description


////

//// define
`options`：[`EntityApplyDamageByProjectileOptions`](./entityapplydamagebyprojectileoptions.md)|[`EntityApplyDamageOptions`](./entityapplydamageoptions.md)|`undefined`

- script_api.@minecraft/server.entity.options.applydamage.description


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

- script_api.@minecraft/server.entity.vector.applyimpulse.description


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

- script_api.@minecraft/server.entity.directionx.applyknockback.description


////

//// define
`directionZ`：`float`

- script_api.@minecraft/server.entity.directionz.applyknockback.description


////

//// define
`horizontalStrength`：`float`

- script_api.@minecraft/server.entity.horizontalstrength.applyknockback.description


////

//// define
`verticalStrength`：`float`

- script_api.@minecraft/server.entity.verticalstrength.applyknockback.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.applyknockback.return


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
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- script_api.@minecraft/server.entity.options.getblockfromviewdirection.description


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

- script_api.@minecraft/server.entity.componentid.getcomponent.description


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
`getEffect`


///

script_api.@minecraft/server.entity.geteffect.description

```js
getEffect(effectType: EffectType | string): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.effecttype.geteffect.description


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
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- script_api.@minecraft/server.entity.options.getentitiesfromviewdirection.description


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

- script_api.@minecraft/server.entity.componentid.hascomponent.description


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

- script_api.@minecraft/server.entity.tag.hastag.description


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
`removeEffect`


///

script_api.@minecraft/server.entity.removeeffect.description

```js
removeEffect(effectType: EffectType | string): boolean
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)|`string`

- script_api.@minecraft/server.entity.effecttype.removeeffect.description


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

- script_api.@minecraft/server.entity.tag.removetag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.removetag.return


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

- script_api.@minecraft/server.entity.commandstring.runcommand.description


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

- script_api.@minecraft/server.entity.commandstring.runcommandasync.description


////

//// define
返回值：<code>Promise&lt;<a href="../commandresult/">CommandResult</a>&gt;</code>

- script_api.@minecraft/server.entity.runcommandasync.return


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

- script_api.@minecraft/server.entity.location.teleport.description


////

//// define
`teleportOptions`：[`TeleportOptions`](./teleportoptions.md)|`undefined`

- script_api.@minecraft/server.entity.teleportoptions.teleport.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.entity.teleport.return


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

- script_api.@minecraft/server.entity.location.tryteleport.description


////

//// define
`teleportOptions`：[`TeleportOptions`](./teleportoptions.md)|`undefined`

- script_api.@minecraft/server.entity.teleportoptions.tryteleport.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.entity.tryteleport.return


////

///

