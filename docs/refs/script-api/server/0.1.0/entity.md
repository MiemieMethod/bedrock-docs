# `Entity`

> 文档版本：1.21.60.21

`Entity`类。script_api.mojang-minecraft.entity.description

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

- script_api.mojang-minecraft.entity.dimension.description


////

///


/// define
`headLocation`


///

```js
read-only headLocation: Location;
```

/// html | div.result
//// define
`headLocation`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.headlocation.description


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

- script_api.mojang-minecraft.entity.id.description


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

- script_api.mojang-minecraft.entity.issneaking.description


////

///


/// define
`location`


///

```js
read-only location: Location;
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.location.description


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

- script_api.mojang-minecraft.entity.nametag.description


////

///


/// define
`rotation`


///

```js
read-only rotation: XYRotation;
```

/// html | div.result
//// define
`rotation`：[`XYRotation`](./xyrotation.md)

- script_api.mojang-minecraft.entity.rotation.description


////

///


/// define
`target`


///

```js
target: Entity;
```

/// html | div.result
//// define
`target`：[`Entity`](./entity.md)

- script_api.mojang-minecraft.entity.target.description


////

///


/// define
`velocity`


///

```js
read-only velocity: Vector;
```

/// html | div.result
//// define
`velocity`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.entity.velocity.description


////

///


/// define
`viewVector`


///

```js
read-only viewVector: Vector;
```

/// html | div.result
//// define
`viewVector`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.entity.viewvector.description


////

///


## 方法

/// define
`addEffect`


///

script_api.mojang-minecraft.entity.addeffect.description

```js
addEffect(effectType: EffectType, duration: int32, amplifier: int32, showParticles: boolean): void
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)

- script_api.mojang-minecraft.entity.addeffect.effecttype.description


////

//// define
`duration`：`int32`

- script_api.mojang-minecraft.entity.addeffect.duration.description


////

//// define
`amplifier`：`int32`＝`0`∈[`0`, `255`]

- script_api.mojang-minecraft.entity.addeffect.amplifier.description


////

//// define
`showParticles`：`boolean`＝`True`

- script_api.mojang-minecraft.entity.addeffect.showparticles.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.addeffect.return


////

///


/// define
`addTag`


///

script_api.mojang-minecraft.entity.addtag.description

```js
addTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.mojang-minecraft.entity.addtag.tag.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entity.addtag.return


////

///


/// define
`getBlockFromViewVector`


///

script_api.mojang-minecraft.entity.getblockfromviewvector.description

```js
getBlockFromViewVector(options?: BlockRaycastOptions): Block | undefined
```

/// html | div.result
//// define
`options`?：[`BlockRaycastOptions`](./blockraycastoptions.md)＝`null`

- script_api.mojang-minecraft.entity.getblockfromviewvector.options.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.mojang-minecraft.entity.getblockfromviewvector.return


////

///


/// define
`getComponent`


///

script_api.mojang-minecraft.entity.getcomponent.description

```js
getComponent(componentId: string): IEntityComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.mojang-minecraft.entity.getcomponent.componentid.description


////

//// define
返回值：[`IEntityComponent`](./ientitycomponent.md)|`undefined`

- script_api.mojang-minecraft.entity.getcomponent.return


////

///


/// define
`getComponents`


///

script_api.mojang-minecraft.entity.getcomponents.description

```js
getComponents(): IEntityComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../ientitycomponent/">IEntityComponent</a>[]</code>

- script_api.mojang-minecraft.entity.getcomponents.return


////

///


/// define
`getDynamicProperty`


///

script_api.mojang-minecraft.entity.getdynamicproperty.description

```js
getDynamicProperty(identifier: string): boolean | double | float | Location | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.entity.getdynamicproperty.identifier.description


////

//// define
返回值：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`|`undefined`

- script_api.mojang-minecraft.entity.getdynamicproperty.return


////

///


/// define
`getEffect`


///

script_api.mojang-minecraft.entity.geteffect.description

```js
getEffect(effectType: EffectType): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)

- script_api.mojang-minecraft.entity.geteffect.effecttype.description


////

//// define
返回值：[`Effect`](./effect.md)|`undefined`

- script_api.mojang-minecraft.entity.geteffect.return


////

///


/// define
`getEntitiesFromViewVector`


///

script_api.mojang-minecraft.entity.getentitiesfromviewvector.description

```js
getEntitiesFromViewVector(options?: EntityRaycastOptions): Entity[]
```

/// html | div.result
//// define
`options`?：[`EntityRaycastOptions`](./entityraycastoptions.md)＝`null`

- script_api.mojang-minecraft.entity.getentitiesfromviewvector.options.description


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

- script_api.mojang-minecraft.entity.getentitiesfromviewvector.return


////

///


/// define
`getTags`


///

script_api.mojang-minecraft.entity.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.mojang-minecraft.entity.gettags.return


////

///


/// define
`hasComponent`


///

script_api.mojang-minecraft.entity.hascomponent.description

```js
hasComponent(componentId: string): boolean
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.mojang-minecraft.entity.hascomponent.componentid.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entity.hascomponent.return


////

///


/// define
`hasTag`


///

script_api.mojang-minecraft.entity.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.mojang-minecraft.entity.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entity.hastag.return


////

///


/// define
`kill`


///

script_api.mojang-minecraft.entity.kill.description

```js
kill(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.mojang-minecraft.entity.kill.return


////

///


/// define
`removeDynamicProperty`


///

script_api.mojang-minecraft.entity.removedynamicproperty.description

```js
removeDynamicProperty(identifier: string): boolean
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.entity.removedynamicproperty.identifier.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entity.removedynamicproperty.return


////

///


/// define
`removeTag`


///

script_api.mojang-minecraft.entity.removetag.description

```js
removeTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.mojang-minecraft.entity.removetag.tag.description


////

//// define
返回值：`boolean`

- script_api.mojang-minecraft.entity.removetag.return


////

///


/// define
`runCommand`


///

script_api.mojang-minecraft.entity.runcommand.description

```js
runCommand(commandString: string): any
```

/// html | div.result
//// define
`commandString`：`string`

- script_api.mojang-minecraft.entity.runcommand.commandstring.description


////

//// define
返回值：`any`

- script_api.mojang-minecraft.entity.runcommand.return


////

///


/// define
`setDynamicProperty`


///

script_api.mojang-minecraft.entity.setdynamicproperty.description

```js
setDynamicProperty(identifier: string, value: boolean | double | float | Location | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- script_api.mojang-minecraft.entity.setdynamicproperty.identifier.description


////

//// define
`value`：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`

- script_api.mojang-minecraft.entity.setdynamicproperty.value.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.setdynamicproperty.return


////

///


/// define
`setRotation`


///

script_api.mojang-minecraft.entity.setrotation.description

```js
setRotation(degreesX: float, degreesY: float): void
```

/// html | div.result
//// define
`degreesX`：`float`

- script_api.mojang-minecraft.entity.setrotation.degreesx.description


////

//// define
`degreesY`：`float`

- script_api.mojang-minecraft.entity.setrotation.degreesy.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.setrotation.return


////

///


/// define
`setVelocity`


///

script_api.mojang-minecraft.entity.setvelocity.description

```js
setVelocity(velocity: Vector): void
```

/// html | div.result
//// define
`velocity`：[`Vector`](./vector.md)

- script_api.mojang-minecraft.entity.setvelocity.velocity.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.setvelocity.return


////

///


/// define
`teleport`


///

script_api.mojang-minecraft.entity.teleport.description

```js
teleport(location: Location, dimension: Dimension, xRotation: float, yRotation: float, keepVelocity: boolean): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.teleport.location.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.mojang-minecraft.entity.teleport.dimension.description


////

//// define
`xRotation`：`float`

- script_api.mojang-minecraft.entity.teleport.xrotation.description


////

//// define
`yRotation`：`float`

- script_api.mojang-minecraft.entity.teleport.yrotation.description


////

//// define
`keepVelocity`：`boolean`＝`False`

- script_api.mojang-minecraft.entity.teleport.keepvelocity.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.teleport.return


////

///


/// define
`teleportFacing`


///

script_api.mojang-minecraft.entity.teleportfacing.description

```js
teleportFacing(location: Location, dimension: Dimension, facingLocation: Location, keepVelocity: boolean): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.teleportfacing.location.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.mojang-minecraft.entity.teleportfacing.dimension.description


////

//// define
`facingLocation`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.teleportfacing.facinglocation.description


////

//// define
`keepVelocity`：`boolean`＝`False`

- script_api.mojang-minecraft.entity.teleportfacing.keepvelocity.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.teleportfacing.return


////

///


/// define
`triggerEvent`


///

script_api.mojang-minecraft.entity.triggerevent.description

```js
triggerEvent(eventName: string): void
```

/// html | div.result
//// define
`eventName`：`string`

- script_api.mojang-minecraft.entity.triggerevent.eventname.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.triggerevent.return


////

///

