# `SimulatedPlayer`

> 文档版本：1.21.0.20

`SimulatedPlayer`类，扩展自[`Player`](../../server/1.8.0/player.md)。

## 属性

/// define
`headRotation`


///

```js
read-only headRotation: Vector2;
```

/// html | div.result
//// define
`headRotation`：[`Vector2`](../../server/1.8.0/vector2.md)

- 属性。


////

///


/// define
`isSprinting`


///

```js
isSprinting: boolean;
```

/// html | div.result
//// define
`isSprinting`：`boolean`

- 属性。


////

///


## 方法

/// define
`attack`


///

```js
attack(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`attackEntity`


///

```js
attackEntity(entity: Entity): boolean
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`breakBlock`


///

```js
breakBlock(blockLocation: Vector3, direction: Direction): boolean
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`chat`


///

```js
chat(message: string): void
```

/// html | div.result
//// define
`message`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`disconnect`


///

```js
disconnect(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`dropSelectedItem`


///

```js
dropSelectedItem(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`fly`


///

```js
fly(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`giveItem`


///

```js
giveItem(itemStack: ItemStack, selectSlot: boolean): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- 参数1。


////

//// define
`selectSlot`：`boolean`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`glide`


///

```js
glide(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`interact`


///

```js
interact(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`interactWithBlock`


///

```js
interactWithBlock(blockLocation: Vector3, direction: Direction): boolean
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`interactWithEntity`


///

```js
interactWithEntity(entity: Entity): boolean
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`jump`


///

```js
jump(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`lookAtBlock`


///

```js
lookAtBlock(blockLocation: Vector3, duration: LookDuration): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`duration`：[`LookDuration`](./lookduration.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`lookAtEntity`


///

```js
lookAtEntity(entity: Entity, duration: LookDuration): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`duration`：[`LookDuration`](./lookduration.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`lookAtLocation`


///

```js
lookAtLocation(location: Vector3, duration: LookDuration): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`duration`：[`LookDuration`](./lookduration.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`move`


///

```js
move(westEast: float, northSouth: float, speed: float): void
```

/// html | div.result
//// define
`westEast`：`float`

- 参数1。


////

//// define
`northSouth`：`float`

- 参数2。


////

//// define
`speed`：`float`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`moveRelative`


///

```js
moveRelative(leftRight: float, backwardForward: float, speed: float): void
```

/// html | div.result
//// define
`leftRight`：`float`

- 参数1。


////

//// define
`backwardForward`：`float`

- 参数2。


////

//// define
`speed`：`float`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`moveToBlock`


///

```js
moveToBlock(blockLocation: Vector3, options?: MoveToOptions): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`options`：[`MoveToOptions`](./movetooptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`moveToLocation`


///

```js
moveToLocation(location: Vector3, options?: MoveToOptions): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`options`：[`MoveToOptions`](./movetooptions.md)|`undefined`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`navigateToBlock`


///

```js
navigateToBlock(blockLocation: Vector3, speed: float): NavigationResult
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`speed`：`float`

- 参数2。


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- 返回值。


////

///


/// define
`navigateToEntity`


///

```js
navigateToEntity(entity: Entity, speed: float): NavigationResult
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`speed`：`float`

- 参数2。


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- 返回值。


////

///


/// define
`navigateToLocation`


///

```js
navigateToLocation(location: Vector3, speed: float): NavigationResult
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`speed`：`float`

- 参数2。


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- 返回值。


////

///


/// define
`navigateToLocations`


///

```js
navigateToLocations(locations: Vector3[], speed: float): void
```

/// html | div.result
//// define
`locations`：<code><a href="../../../server/1.8.0/vector3/">Vector3</a>[]</code>

- 参数1。


////

//// define
`speed`：`float`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`respawn`


///

```js
respawn(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`rotateBody`


///

```js
rotateBody(angleInDegrees: float): void
```

/// html | div.result
//// define
`angleInDegrees`：`float`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setBodyRotation`


///

```js
setBodyRotation(angleInDegrees: float): void
```

/// html | div.result
//// define
`angleInDegrees`：`float`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setItem`


///

```js
setItem(itemStack: ItemStack, slot: int32, selectSlot: boolean): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- 参数1。


////

//// define
`slot`：`int32`

- 参数2。


////

//// define
`selectSlot`：`boolean`

- 参数3。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`startBuild`


///

```js
startBuild(slot: int32): void
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopBreakingBlock`


///

```js
stopBreakingBlock(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopBuild`


///

```js
stopBuild(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopFlying`


///

```js
stopFlying(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopGliding`


///

```js
stopGliding(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopInteracting`


///

```js
stopInteracting(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopMoving`


///

```js
stopMoving(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopSwimming`


///

```js
stopSwimming(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`stopUsingItem`


///

```js
stopUsingItem(): ItemStack | undefined
```

/// html | div.result
//// define
返回值：[`ItemStack`](../../server/1.8.0/itemstack.md)|`undefined`

- 返回值。


////

///


/// define
`swim`


///

```js
swim(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`useItem`


///

```js
useItem(itemStack: ItemStack): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`useItemInSlot`


///

```js
useItemInSlot(slot: int32): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`useItemInSlotOnBlock`


///

```js
useItemInSlotOnBlock(slot: int32, blockLocation: Vector3, direction: Direction, faceLocation?: Vector3): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数3。


////

//// define
`faceLocation`：[`Vector3`](../../server/1.8.0/vector3.md)|`undefined`

- 参数4。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`useItemOnBlock`


///

```js
useItemOnBlock(itemStack: ItemStack, blockLocation: Vector3, direction: Direction, faceLocation?: Vector3): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数3。


////

//// define
`faceLocation`：[`Vector3`](../../server/1.8.0/vector3.md)|`undefined`

- 参数4。


////

//// define
返回值：`boolean`

- 返回值。


////

///

