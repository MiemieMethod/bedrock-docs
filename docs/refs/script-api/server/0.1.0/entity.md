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
`headLocation`


///

```js
read-only headLocation: Location;
```

/// html | div.result
//// define
`headLocation`：[`Location`](./location.md)

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
`location`


///

```js
read-only location: Location;
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

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
`rotation`


///

```js
read-only rotation: XYRotation;
```

/// html | div.result
//// define
`rotation`：[`XYRotation`](./xyrotation.md)

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`addEffect`


///

```js
addEffect(effectType: EffectType, duration: int32, amplifier: int32, showParticles: boolean): void
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)

- 参数1。


////

//// define
`duration`：`int32`

- 参数2。


////

//// define
`amplifier`：`int32`

- 参数3。


////

//// define
`showParticles`：`boolean`

- 参数4。


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
`getBlockFromViewVector`


///

```js
getBlockFromViewVector(options?: BlockRaycastOptions): Block | undefined
```

/// html | div.result
//// define
`options`：[`BlockRaycastOptions`](./blockraycastoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`getComponent`


///

```js
getComponent(componentId: string): IEntityComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：[`IEntityComponent`](./ientitycomponent.md)|`undefined`

- 返回值。


////

///


/// define
`getComponents`


///

```js
getComponents(): IEntityComponent[]
```

/// html | div.result
//// define
返回值：<code><a href="../ientitycomponent/">IEntityComponent</a>[]</code>

- 返回值。


////

///


/// define
`getDynamicProperty`


///

```js
getDynamicProperty(identifier: string): boolean | double | float | Location | string | undefined
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`|`undefined`

- 返回值。


////

///


/// define
`getEffect`


///

```js
getEffect(effectType: EffectType): Effect | undefined
```

/// html | div.result
//// define
`effectType`：[`EffectType`](./effecttype.md)

- 参数1。


////

//// define
返回值：[`Effect`](./effect.md)|`undefined`

- 返回值。


////

///


/// define
`getEntitiesFromViewVector`


///

```js
getEntitiesFromViewVector(options?: EntityRaycastOptions): Entity[]
```

/// html | div.result
//// define
`options`：[`EntityRaycastOptions`](./entityraycastoptions.md)|`undefined`

- 参数1。


////

//// define
返回值：<code><a href="../entity/">Entity</a>[]</code>

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
`kill`


///

```js
kill(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`removeDynamicProperty`


///

```js
removeDynamicProperty(identifier: string): boolean
```

/// html | div.result
//// define
`identifier`：`string`

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
`runCommand`


///

```js
runCommand(commandString: string): any
```

/// html | div.result
//// define
`commandString`：`string`

- 参数1。


////

//// define
返回值：`any`

- 返回值。


////

///


/// define
`setDynamicProperty`


///

```js
setDynamicProperty(identifier: string, value: boolean | double | float | Location | string): void
```

/// html | div.result
//// define
`identifier`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`double`|`float`|[`Location`](./location.md)|`string`

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
setRotation(degreesX: float, degreesY: float): void
```

/// html | div.result
//// define
`degreesX`：`float`

- 参数1。


////

//// define
`degreesY`：`float`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setVelocity`


///

```js
setVelocity(velocity: Vector): void
```

/// html | div.result
//// define
`velocity`：[`Vector`](./vector.md)

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
teleport(location: Location, dimension: Dimension, xRotation: float, yRotation: float, keepVelocity: boolean): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- 参数1。


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- 参数2。


////

//// define
`xRotation`：`float`

- 参数3。


////

//// define
`yRotation`：`float`

- 参数4。


////

//// define
`keepVelocity`：`boolean`

- 参数5。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`teleportFacing`


///

```js
teleportFacing(location: Location, dimension: Dimension, facingLocation: Location, keepVelocity: boolean): void
```

/// html | div.result
//// define
`location`：[`Location`](./location.md)

- 参数1。


////

//// define
`dimension`：[`Dimension`](./dimension.md)

- 参数2。


////

//// define
`facingLocation`：[`Location`](./location.md)

- 参数3。


////

//// define
`keepVelocity`：`boolean`

- 参数4。


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

