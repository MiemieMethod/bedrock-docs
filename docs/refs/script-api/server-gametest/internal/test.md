# `Test`

> 文档版本：1.21.0.20

`Test`类。

## 方法

/// define
`assert`


///

```js
assert(condition: boolean, message: string): void
```

/// html | div.result
//// define
`condition`：`boolean`

- 参数1。


////

//// define
`message`：`string`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertBlockPresent`


///

```js
assertBlockPresent(blockType: BlockType | string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`isPresent`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertBlockState`


///

```js
assertBlockState(blockLocation: Vector3, callback: (arg: Block) => boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`callback`：<code>(<a href="../../../server/1.8.0/block/">Block</a>) =&gt; boolean</code>

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertCanReachLocation`


///

```js
assertCanReachLocation(mob: Entity, blockLocation: Vector3, canReach: boolean): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`canReach`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertContainerContains`


///

```js
assertContainerContains(itemStack: ItemStack, blockLocation: Vector3): void
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
返回值：`void`

- 返回值。


////

///


/// define
`assertContainerEmpty`


///

```js
assertContainerEmpty(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityHasArmor`


///

```js
assertEntityHasArmor(entityTypeIdentifier: string, armorSlot: int32, armorName: string, armorData: int32, blockLocation: Vector3, hasArmor: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`armorSlot`：`int32`

- 参数2。


////

//// define
`armorName`：`string`

- 参数3。


////

//// define
`armorData`：`int32`

- 参数4。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数5。


////

//// define
`hasArmor`：`boolean`

- 参数6。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityHasComponent`


///

```js
assertEntityHasComponent(entityTypeIdentifier: string, componentIdentifier: string, blockLocation: Vector3, hasComponent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`componentIdentifier`：`string`

- 参数2。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数3。


////

//// define
`hasComponent`：`boolean`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityInstancePresent`


///

```js
assertEntityInstancePresent(entity: Entity, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`isPresent`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityInstancePresentInArea`


///

```js
assertEntityInstancePresentInArea(entity: Entity, isPresent: boolean): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`isPresent`：`boolean`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityPresent`


///

```js
assertEntityPresent(entityTypeIdentifier: string, blockLocation: Vector3, searchDistance: float, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`searchDistance`：`float`

- 参数3。


////

//// define
`isPresent`：`boolean`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityPresentInArea`


///

```js
assertEntityPresentInArea(entityTypeIdentifier: string, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`isPresent`：`boolean`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityState`


///

```js
assertEntityState(blockLocation: Vector3, entityTypeIdentifier: string, callback: (arg: Entity) => boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`entityTypeIdentifier`：`string`

- 参数2。


////

//// define
`callback`：<code>(<a href="../../../server/1.8.0/entity/">Entity</a>) =&gt; boolean</code>

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertEntityTouching`


///

```js
assertEntityTouching(entityTypeIdentifier: string, location: Vector3, isTouching: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`isTouching`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertIsWaterlogged`


///

```js
assertIsWaterlogged(blockLocation: Vector3, isWaterlogged: boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`isWaterlogged`：`boolean`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertItemEntityCountIs`


///

```js
assertItemEntityCountIs(itemType: ItemType | string, blockLocation: Vector3, searchDistance: float, count: int32): void
```

/// html | div.result
//// define
`itemType`：[`ItemType`](../../server/1.8.0/itemtype.md)|`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`searchDistance`：`float`

- 参数3。


////

//// define
`count`：`int32`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertItemEntityPresent`


///

```js
assertItemEntityPresent(itemType: ItemType | string, blockLocation: Vector3, searchDistance: float, isPresent: boolean): void
```

/// html | div.result
//// define
`itemType`：[`ItemType`](../../server/1.8.0/itemtype.md)|`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`searchDistance`：`float`

- 参数3。


////

//// define
`isPresent`：`boolean`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`assertRedstonePower`


///

```js
assertRedstonePower(blockLocation: Vector3, power: int32): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`power`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`destroyBlock`


///

```js
destroyBlock(blockLocation: Vector3, dropResources: boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`dropResources`：`boolean`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`fail`


///

```js
fail(errorMessage: string): void
```

/// html | div.result
//// define
`errorMessage`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`failIf`


///

```js
failIf(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`getBlock`


///

```js
getBlock(blockLocation: Vector3): Block
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Block`](../../server/1.8.0/block.md)

- 返回值。


////

///


/// define
`getDimension`


///

```js
getDimension(): Dimension
```

/// html | div.result
//// define
返回值：[`Dimension`](../../server/1.8.0/dimension.md)

- 返回值。


////

///


/// define
`getFenceConnectivity`


///

```js
getFenceConnectivity(blockLocation: Vector3): FenceConnectivity
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`FenceConnectivity`](./fenceconnectivity.md)

- 返回值。


////

///


/// define
`getSculkSpreader`


///

```js
getSculkSpreader(blockLocation: Vector3): SculkSpreader | undefined
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`SculkSpreader`](./sculkspreader.md)|`undefined`

- 返回值。


////

///


/// define
`getTestDirection`


///

```js
getTestDirection(): Direction
```

/// html | div.result
//// define
返回值：[`Direction`](../../server/1.8.0/direction.md)

- 返回值。


////

///


/// define
`idle`


///

```js
idle(tickDelay: int32): Promise<void>
```

/// html | div.result
//// define
`tickDelay`：`int32`

- 参数1。


////

//// define
返回值：`Promise<void>`

- 返回值。


////

///


/// define
`killAllEntities`


///

```js
killAllEntities(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`onPlayerJump`


///

```js
onPlayerJump(mob: Entity, jumpAmount: int32): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`jumpAmount`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`pressButton`


///

```js
pressButton(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`print`


///

```js
print(text: string): void
```

/// html | div.result
//// define
`text`：`string`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`pullLever`


///

```js
pullLever(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`pulseRedstone`


///

```js
pulseRedstone(blockLocation: Vector3, duration: int32): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`duration`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`relativeBlockLocation`


///

```js
relativeBlockLocation(worldBlockLocation: Vector3): Vector3
```

/// html | div.result
//// define
`worldBlockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- 返回值。


////

///


/// define
`relativeLocation`


///

```js
relativeLocation(worldLocation: Vector3): Vector3
```

/// html | div.result
//// define
`worldLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- 返回值。


////

///


/// define
`removeSimulatedPlayer`


///

```js
removeSimulatedPlayer(simulatedPlayer: SimulatedPlayer): void
```

/// html | div.result
//// define
`simulatedPlayer`：[`SimulatedPlayer`](./simulatedplayer.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`rotateDirection`


///

```js
rotateDirection(direction: Direction): Direction
```

/// html | div.result
//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数1。


////

//// define
返回值：[`Direction`](../../server/1.8.0/direction.md)

- 返回值。


////

///


/// define
`rotateVector`


///

```js
rotateVector(vector: Vector3): Vector3
```

/// html | div.result
//// define
`vector`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- 返回值。


////

///


/// define
`runAfterDelay`


///

```js
runAfterDelay(delayTicks: int32, callback: () => void): void
```

/// html | div.result
//// define
`delayTicks`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`runAtTickTime`


///

```js
runAtTickTime(tick: int32, callback: () => void): void
```

/// html | div.result
//// define
`tick`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setBlockPermutation`


///

```js
setBlockPermutation(blockData: BlockPermutation, blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockData`：[`BlockPermutation`](../../server/1.8.0/blockpermutation.md)

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setBlockType`


///

```js
setBlockType(blockType: BlockType | string, blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setFluidContainer`


///

```js
setFluidContainer(location: Vector3, type: FluidType): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`type`：[`FluidType`](../../server/1.8.0/fluidtype.md)

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setTntFuse`


///

```js
setTntFuse(entity: Entity, fuseLength: int32): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`fuseLength`：`int32`

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`spawn`


///

```js
spawn(entityTypeIdentifier: string, blockLocation: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- 返回值。


////

///


/// define
`spawnAtLocation`


///

```js
spawnAtLocation(entityTypeIdentifier: string, location: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- 返回值。


////

///


/// define
`spawnItem`


///

```js
spawnItem(itemStack: ItemStack, location: Vector3): Entity
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- 返回值。


////

///


/// define
`spawnSimulatedPlayer`


///

```js
spawnSimulatedPlayer(blockLocation: Vector3, name: string, gameMode: GameMode): SimulatedPlayer
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`name`：`string`

- 参数2。


////

//// define
`gameMode`：[`GameMode`](../../server/1.8.0/gamemode.md)

- 参数3。


////

//// define
返回值：[`SimulatedPlayer`](./simulatedplayer.md)

- 返回值。


////

///


/// define
`spawnWithoutBehaviors`


///

```js
spawnWithoutBehaviors(entityTypeIdentifier: string, blockLocation: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- 返回值。


////

///


/// define
`spawnWithoutBehaviorsAtLocation`


///

```js
spawnWithoutBehaviorsAtLocation(entityTypeIdentifier: string, location: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- 返回值。


////

///


/// define
`spreadFromFaceTowardDirection`


///

```js
spreadFromFaceTowardDirection(blockLocation: Vector3, fromFace: Direction, direction: Direction): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`fromFace`：[`Direction`](../../server/1.8.0/direction.md)

- 参数2。


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`startSequence`


///

```js
startSequence(): GameTestSequence
```

/// html | div.result
//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- 返回值。


////

///


/// define
`succeed`


///

```js
succeed(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedIf`


///

```js
succeedIf(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedOnTick`


///

```js
succeedOnTick(tick: int32): void
```

/// html | div.result
//// define
`tick`：`int32`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedOnTickWhen`


///

```js
succeedOnTickWhen(tick: int32, callback: () => void): void
```

/// html | div.result
//// define
`tick`：`int32`

- 参数1。


////

//// define
`callback`：<code>() =&gt; void</code>

- 参数2。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedWhen`


///

```js
succeedWhen(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedWhenBlockPresent`


///

```js
succeedWhenBlockPresent(blockType: BlockType | string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`isPresent`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedWhenEntityHasComponent`


///

```js
succeedWhenEntityHasComponent(entityTypeIdentifier: string, componentIdentifier: string, blockLocation: Vector3, hasComponent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`componentIdentifier`：`string`

- 参数2。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数3。


////

//// define
`hasComponent`：`boolean`

- 参数4。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`succeedWhenEntityPresent`


///

```js
succeedWhenEntityPresent(entityTypeIdentifier: string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`isPresent`：`boolean`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`triggerInternalBlockEvent`


///

```js
triggerInternalBlockEvent(blockLocation: Vector3, event: string, eventParameters: float[]): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
`event`：`string`

- 参数2。


////

//// define
`eventParameters`：`float[]`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`until`


///

```js
until(callback: () => void): Promise<void>
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- 参数1。


////

//// define
返回值：`Promise<void>`

- 返回值。


////

///


/// define
`walkTo`


///

```js
walkTo(mob: Entity, blockLocation: Vector3, speedModifier: float): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`speedModifier`：`float`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`walkToLocation`


///

```js
walkToLocation(mob: Entity, location: Vector3, speedModifier: float): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- 参数1。


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数2。


////

//// define
`speedModifier`：`float`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`worldBlockLocation`


///

```js
worldBlockLocation(relativeBlockLocation: Vector3): Vector3
```

/// html | div.result
//// define
`relativeBlockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- 返回值。


////

///


/// define
`worldLocation`


///

```js
worldLocation(relativeLocation: Vector3): Vector3
```

/// html | div.result
//// define
`relativeLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- 参数1。


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- 返回值。


////

///

