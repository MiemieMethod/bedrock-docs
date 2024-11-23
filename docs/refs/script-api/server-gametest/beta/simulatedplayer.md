# `SimulatedPlayer`

> 文档版本：1.21.60.21

`SimulatedPlayer`类，扩展自[`Player`](../../server/1.8.0/player.md)。script_api.@minecraft/server-gametest.simulatedplayer.description

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

- script_api.@minecraft/server-gametest.simulatedplayer.headrotation.description


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

- script_api.@minecraft/server-gametest.simulatedplayer.issprinting.description


////

///


## 方法

/// define
`attack`


///

script_api.@minecraft/server-gametest.simulatedplayer.attack.description

```js
attack(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.attack.return


////

///


/// define
`attackEntity`


///

script_api.@minecraft/server-gametest.simulatedplayer.attackentity.description

```js
attackEntity(entity: Entity): boolean
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.simulatedplayer.attackentity.entity.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.attackentity.return


////

///


/// define
`breakBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.breakblock.description

```js
breakBlock(blockLocation: Vector3, direction: Direction): boolean
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.breakblock.blocklocation.description


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)＝`1`

- script_api.@minecraft/server-gametest.simulatedplayer.breakblock.direction.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.breakblock.return


////

///


/// define
`chat`


///

script_api.@minecraft/server-gametest.simulatedplayer.chat.description

```js
chat(message: string): void
```

/// html | div.result
//// define
`message`：`string`

- script_api.@minecraft/server-gametest.simulatedplayer.chat.message.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.chat.return


////

///


/// define
`disconnect`


///

script_api.@minecraft/server-gametest.simulatedplayer.disconnect.description

```js
disconnect(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.disconnect.return


////

///


/// define
`dropSelectedItem`


///

script_api.@minecraft/server-gametest.simulatedplayer.dropselecteditem.description

```js
dropSelectedItem(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.dropselecteditem.return


////

///


/// define
`fly`


///

script_api.@minecraft/server-gametest.simulatedplayer.fly.description

```js
fly(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.fly.return


////

///


/// define
`giveItem`


///

script_api.@minecraft/server-gametest.simulatedplayer.giveitem.description

```js
giveItem(itemStack: ItemStack, selectSlot: boolean): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.simulatedplayer.giveitem.itemstack.description


////

//// define
`selectSlot`：`boolean`＝`False`

- script_api.@minecraft/server-gametest.simulatedplayer.giveitem.selectslot.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.giveitem.return


////

///


/// define
`glide`


///

script_api.@minecraft/server-gametest.simulatedplayer.glide.description

```js
glide(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.glide.return


////

///


/// define
`interact`


///

script_api.@minecraft/server-gametest.simulatedplayer.interact.description

```js
interact(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.interact.return


////

///


/// define
`interactWithBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.interactwithblock.description

```js
interactWithBlock(blockLocation: Vector3, direction: Direction): boolean
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.interactwithblock.blocklocation.description


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)＝`1`

- script_api.@minecraft/server-gametest.simulatedplayer.interactwithblock.direction.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.interactwithblock.return


////

///


/// define
`interactWithEntity`


///

script_api.@minecraft/server-gametest.simulatedplayer.interactwithentity.description

```js
interactWithEntity(entity: Entity): boolean
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.simulatedplayer.interactwithentity.entity.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.interactwithentity.return


////

///


/// define
`jump`


///

script_api.@minecraft/server-gametest.simulatedplayer.jump.description

```js
jump(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.jump.return


////

///


/// define
`lookAtBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.lookatblock.description

```js
lookAtBlock(blockLocation: Vector3, duration: LookDuration): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.lookatblock.blocklocation.description


////

//// define
`duration`：[`LookDuration`](./lookduration.md)＝`2`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatblock.duration.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatblock.return


////

///


/// define
`lookAtEntity`


///

script_api.@minecraft/server-gametest.simulatedplayer.lookatentity.description

```js
lookAtEntity(entity: Entity, duration: LookDuration): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.simulatedplayer.lookatentity.entity.description


////

//// define
`duration`：[`LookDuration`](./lookduration.md)＝`2`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatentity.duration.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatentity.return


////

///


/// define
`lookAtLocation`


///

script_api.@minecraft/server-gametest.simulatedplayer.lookatlocation.description

```js
lookAtLocation(location: Vector3, duration: LookDuration): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.lookatlocation.location.description


////

//// define
`duration`：[`LookDuration`](./lookduration.md)＝`2`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatlocation.duration.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.lookatlocation.return


////

///


/// define
`move`


///

script_api.@minecraft/server-gametest.simulatedplayer.move.description

```js
move(westEast: float, northSouth: float, speed: float): void
```

/// html | div.result
//// define
`westEast`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.move.westeast.description


////

//// define
`northSouth`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.move.northsouth.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.move.speed.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.move.return


////

///


/// define
`moveRelative`


///

script_api.@minecraft/server-gametest.simulatedplayer.moverelative.description

```js
moveRelative(leftRight: float, backwardForward: float, speed: float): void
```

/// html | div.result
//// define
`leftRight`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.moverelative.leftright.description


////

//// define
`backwardForward`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.moverelative.backwardforward.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.moverelative.speed.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.moverelative.return


////

///


/// define
`moveToBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.movetoblock.description

```js
moveToBlock(blockLocation: Vector3, options?: MoveToOptions): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.movetoblock.blocklocation.description


////

//// define
`options`?：[`MoveToOptions`](./movetooptions.md)＝`null`

- script_api.@minecraft/server-gametest.simulatedplayer.movetoblock.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.movetoblock.return


////

///


/// define
`moveToLocation`


///

script_api.@minecraft/server-gametest.simulatedplayer.movetolocation.description

```js
moveToLocation(location: Vector3, options?: MoveToOptions): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.movetolocation.location.description


////

//// define
`options`?：[`MoveToOptions`](./movetooptions.md)＝`null`

- script_api.@minecraft/server-gametest.simulatedplayer.movetolocation.options.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.movetolocation.return


////

///


/// define
`navigateToBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.navigatetoblock.description

```js
navigateToBlock(blockLocation: Vector3, speed: float): NavigationResult
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoblock.blocklocation.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoblock.speed.description


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoblock.return


////

///


/// define
`navigateToEntity`


///

script_api.@minecraft/server-gametest.simulatedplayer.navigatetoentity.description

```js
navigateToEntity(entity: Entity, speed: float): NavigationResult
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoentity.entity.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoentity.speed.description


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetoentity.return


////

///


/// define
`navigateToLocation`


///

script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocation.description

```js
navigateToLocation(location: Vector3, speed: float): NavigationResult
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocation.location.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocation.speed.description


////

//// define
返回值：[`NavigationResult`](./navigationresult.md)

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocation.return


////

///


/// define
`navigateToLocations`


///

script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocations.description

```js
navigateToLocations(locations: Vector3[], speed: float): void
```

/// html | div.result
//// define
`locations`：<code><a href="../../../server/1.8.0/vector3/">Vector3</a>[]</code>

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocations.locations.description


////

//// define
`speed`：`float`＝`1.0`∈[`0.0`, `1.0`]

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocations.speed.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.navigatetolocations.return


////

///


/// define
`respawn`


///

script_api.@minecraft/server-gametest.simulatedplayer.respawn.description

```js
respawn(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.respawn.return


////

///


/// define
`rotateBody`


///

script_api.@minecraft/server-gametest.simulatedplayer.rotatebody.description

```js
rotateBody(angleInDegrees: float): void
```

/// html | div.result
//// define
`angleInDegrees`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.rotatebody.angleindegrees.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.rotatebody.return


////

///


/// define
`setBodyRotation`


///

script_api.@minecraft/server-gametest.simulatedplayer.setbodyrotation.description

```js
setBodyRotation(angleInDegrees: float): void
```

/// html | div.result
//// define
`angleInDegrees`：`float`

- script_api.@minecraft/server-gametest.simulatedplayer.setbodyrotation.angleindegrees.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.setbodyrotation.return


////

///


/// define
`setItem`


///

script_api.@minecraft/server-gametest.simulatedplayer.setitem.description

```js
setItem(itemStack: ItemStack, slot: int32, selectSlot: boolean): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.simulatedplayer.setitem.itemstack.description


////

//// define
`slot`：`int32`

- script_api.@minecraft/server-gametest.simulatedplayer.setitem.slot.description


////

//// define
`selectSlot`：`boolean`＝`False`

- script_api.@minecraft/server-gametest.simulatedplayer.setitem.selectslot.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.setitem.return


////

///


/// define
`startBuild`


///

script_api.@minecraft/server-gametest.simulatedplayer.startbuild.description

```js
startBuild(slot: int32): void
```

/// html | div.result
//// define
`slot`：`int32`＝`0`

- script_api.@minecraft/server-gametest.simulatedplayer.startbuild.slot.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.startbuild.return


////

///


/// define
`stopBreakingBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopbreakingblock.description

```js
stopBreakingBlock(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopbreakingblock.return


////

///


/// define
`stopBuild`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopbuild.description

```js
stopBuild(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopbuild.return


////

///


/// define
`stopFlying`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopflying.description

```js
stopFlying(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopflying.return


////

///


/// define
`stopGliding`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopgliding.description

```js
stopGliding(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopgliding.return


////

///


/// define
`stopInteracting`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopinteracting.description

```js
stopInteracting(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopinteracting.return


////

///


/// define
`stopMoving`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopmoving.description

```js
stopMoving(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopmoving.return


////

///


/// define
`stopSwimming`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopswimming.description

```js
stopSwimming(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.stopswimming.return


////

///


/// define
`stopUsingItem`


///

script_api.@minecraft/server-gametest.simulatedplayer.stopusingitem.description

```js
stopUsingItem(): ItemStack | undefined
```

/// html | div.result
//// define
返回值：[`ItemStack`](../../server/1.8.0/itemstack.md)|`undefined`

- script_api.@minecraft/server-gametest.simulatedplayer.stopusingitem.return


////

///


/// define
`swim`


///

script_api.@minecraft/server-gametest.simulatedplayer.swim.description

```js
swim(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.simulatedplayer.swim.return


////

///


/// define
`useItem`


///

script_api.@minecraft/server-gametest.simulatedplayer.useitem.description

```js
useItem(itemStack: ItemStack): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.simulatedplayer.useitem.itemstack.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.useitem.return


////

///


/// define
`useItemInSlot`


///

script_api.@minecraft/server-gametest.simulatedplayer.useiteminslot.description

```js
useItemInSlot(slot: int32): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslot.slot.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslot.return


////

///


/// define
`useItemInSlotOnBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.description

```js
useItemInSlotOnBlock(slot: int32, blockLocation: Vector3, direction: Direction, faceLocation?: Vector3): boolean
```

/// html | div.result
//// define
`slot`：`int32`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.slot.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.blocklocation.description


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)＝`1`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.direction.description


////

//// define
`faceLocation`?：[`Vector3`](../../server/1.8.0/vector3.md)＝`null`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.facelocation.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.useiteminslotonblock.return


////

///


/// define
`useItemOnBlock`


///

script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.description

```js
useItemOnBlock(itemStack: ItemStack, blockLocation: Vector3, direction: Direction, faceLocation?: Vector3): boolean
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.itemstack.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.blocklocation.description


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)＝`1`

- script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.direction.description


////

//// define
`faceLocation`?：[`Vector3`](../../server/1.8.0/vector3.md)＝`null`

- script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.facelocation.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-gametest.simulatedplayer.useitemonblock.return


////

///

