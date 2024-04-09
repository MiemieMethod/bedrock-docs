# `Entity`

> 文档版本：1.21.0.20

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

- script_api.mojang-minecraft.entity.effecttype.addeffect.description


////

//// define
`duration`：`int32`

- script_api.mojang-minecraft.entity.duration.addeffect.description


////

//// define
`amplifier`：`int32`

- script_api.mojang-minecraft.entity.amplifier.addeffect.description


////

//// define
`showParticles`：`boolean`

- script_api.mojang-minecraft.entity.showparticles.addeffect.description


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

- script_api.mojang-minecraft.entity.tag.addtag.description


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
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- script_api.mojang-minecraft.entity.options.getblockfromviewvector.description


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

- script_api.mojang-minecraft.entity.componentid.getcomponent.description


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

- script_api.mojang-minecraft.entity.identifier.getdynamicproperty.description


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

- script_api.mojang-minecraft.entity.effecttype.geteffect.description


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
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- script_api.mojang-minecraft.entity.options.getentitiesfromviewvector.description


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

- script_api.mojang-minecraft.entity.componentid.hascomponent.description


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

- script_api.mojang-minecraft.entity.tag.hastag.description


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

- script_api.mojang-minecraft.entity.identifier.removedynamicproperty.description


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

- script_api.mojang-minecraft.entity.tag.removetag.description


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

- script_api.mojang-minecraft.entity.commandstring.runcommand.description


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

- script_api.mojang-minecraft.entity.identifier.setdynamicproperty.description


////

//// define
`value`：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`

- script_api.mojang-minecraft.entity.value.setdynamicproperty.description


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

- script_api.mojang-minecraft.entity.degreesx.setrotation.description


////

//// define
`degreesY`：`float`

- script_api.mojang-minecraft.entity.degreesy.setrotation.description


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

- script_api.mojang-minecraft.entity.velocity.setvelocity.description


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

- script_api.mojang-minecraft.entity.location.teleport.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.mojang-minecraft.entity.dimension.teleport.description


////

//// define
`xRotation`：`float`

- script_api.mojang-minecraft.entity.xrotation.teleport.description


////

//// define
`yRotation`：`float`

- script_api.mojang-minecraft.entity.yrotation.teleport.description


////

//// define
`keepVelocity`：`boolean`

- script_api.mojang-minecraft.entity.keepvelocity.teleport.description


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

- script_api.mojang-minecraft.entity.location.teleportfacing.description


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- script_api.mojang-minecraft.entity.dimension.teleportfacing.description


////

//// define
`facingLocation`：[`Location`](./location.md)

- script_api.mojang-minecraft.entity.facinglocation.teleportfacing.description


////

//// define
`keepVelocity`：`boolean`

- script_api.mojang-minecraft.entity.keepvelocity.teleportfacing.description


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

- script_api.mojang-minecraft.entity.eventname.triggerevent.description


////

//// define
返回值：`void`

- script_api.mojang-minecraft.entity.triggerevent.return


////

///

