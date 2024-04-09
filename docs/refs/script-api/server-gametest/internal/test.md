# `Test`

> 文档版本：1.21.0.20

`Test`类。script_api.@minecraft/server-gametest.test.description

## 方法

/// define
`assert`


///

script_api.@minecraft/server-gametest.test.assert.description

```js
assert(condition: boolean, message: string): void
```

/// html | div.result
//// define
`condition`：`boolean`

- script_api.@minecraft/server-gametest.test.condition.assert.description


////

//// define
`message`：`string`

- script_api.@minecraft/server-gametest.test.message.assert.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assert.return


////

///


/// define
`assertBlockPresent`


///

script_api.@minecraft/server-gametest.test.assertblockpresent.description

```js
assertBlockPresent(blockType: BlockType | string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.blocktype.assertblockpresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertblockpresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertblockpresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertblockpresent.return


////

///


/// define
`assertBlockState`


///

script_api.@minecraft/server-gametest.test.assertblockstate.description

```js
assertBlockState(blockLocation: Vector3, callback: (arg: Block) => boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertblockstate.description


////

//// define
`callback`：<code>(<a href="../../../server/1.8.0/block/">Block</a>) =&gt; boolean</code>

- script_api.@minecraft/server-gametest.test.callback.assertblockstate.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertblockstate.return


////

///


/// define
`assertCanReachLocation`


///

script_api.@minecraft/server-gametest.test.assertcanreachlocation.description

```js
assertCanReachLocation(mob: Entity, blockLocation: Vector3, canReach: boolean): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.mob.assertcanreachlocation.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertcanreachlocation.description


////

//// define
`canReach`：`boolean`

- script_api.@minecraft/server-gametest.test.canreach.assertcanreachlocation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertcanreachlocation.return


////

///


/// define
`assertContainerContains`


///

script_api.@minecraft/server-gametest.test.assertcontainercontains.description

```js
assertContainerContains(itemStack: ItemStack, blockLocation: Vector3): void
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.test.itemstack.assertcontainercontains.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertcontainercontains.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertcontainercontains.return


////

///


/// define
`assertContainerEmpty`


///

script_api.@minecraft/server-gametest.test.assertcontainerempty.description

```js
assertContainerEmpty(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertcontainerempty.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertcontainerempty.return


////

///


/// define
`assertEntityHasArmor`


///

script_api.@minecraft/server-gametest.test.assertentityhasarmor.description

```js
assertEntityHasArmor(entityTypeIdentifier: string, armorSlot: int32, armorName: string, armorData: int32, blockLocation: Vector3, hasArmor: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentityhasarmor.description


////

//// define
`armorSlot`：`int32`

- script_api.@minecraft/server-gametest.test.armorslot.assertentityhasarmor.description


////

//// define
`armorName`：`string`

- script_api.@minecraft/server-gametest.test.armorname.assertentityhasarmor.description


////

//// define
`armorData`：`int32`

- script_api.@minecraft/server-gametest.test.armordata.assertentityhasarmor.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertentityhasarmor.description


////

//// define
`hasArmor`：`boolean`

- script_api.@minecraft/server-gametest.test.hasarmor.assertentityhasarmor.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.return


////

///


/// define
`assertEntityHasComponent`


///

script_api.@minecraft/server-gametest.test.assertentityhascomponent.description

```js
assertEntityHasComponent(entityTypeIdentifier: string, componentIdentifier: string, blockLocation: Vector3, hasComponent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentityhascomponent.description


////

//// define
`componentIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.componentidentifier.assertentityhascomponent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertentityhascomponent.description


////

//// define
`hasComponent`：`boolean`

- script_api.@minecraft/server-gametest.test.hascomponent.assertentityhascomponent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentityhascomponent.return


////

///


/// define
`assertEntityInstancePresent`


///

script_api.@minecraft/server-gametest.test.assertentityinstancepresent.description

```js
assertEntityInstancePresent(entity: Entity, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.entity.assertentityinstancepresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertentityinstancepresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertentityinstancepresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentityinstancepresent.return


////

///


/// define
`assertEntityInstancePresentInArea`


///

script_api.@minecraft/server-gametest.test.assertentityinstancepresentinarea.description

```js
assertEntityInstancePresentInArea(entity: Entity, isPresent: boolean): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.entity.assertentityinstancepresentinarea.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertentityinstancepresentinarea.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentityinstancepresentinarea.return


////

///


/// define
`assertEntityPresent`


///

script_api.@minecraft/server-gametest.test.assertentitypresent.description

```js
assertEntityPresent(entityTypeIdentifier: string, blockLocation: Vector3, searchDistance: float, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentitypresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertentitypresent.description


////

//// define
`searchDistance`：`float`

- script_api.@minecraft/server-gametest.test.searchdistance.assertentitypresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertentitypresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentitypresent.return


////

///


/// define
`assertEntityPresentInArea`


///

script_api.@minecraft/server-gametest.test.assertentitypresentinarea.description

```js
assertEntityPresentInArea(entityTypeIdentifier: string, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentitypresentinarea.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertentitypresentinarea.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentitypresentinarea.return


////

///


/// define
`assertEntityState`


///

script_api.@minecraft/server-gametest.test.assertentitystate.description

```js
assertEntityState(blockLocation: Vector3, entityTypeIdentifier: string, callback: (arg: Entity) => boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertentitystate.description


////

//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentitystate.description


////

//// define
`callback`：<code>(<a href="../../../server/1.8.0/entity/">Entity</a>) =&gt; boolean</code>

- script_api.@minecraft/server-gametest.test.callback.assertentitystate.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentitystate.return


////

///


/// define
`assertEntityTouching`


///

script_api.@minecraft/server-gametest.test.assertentitytouching.description

```js
assertEntityTouching(entityTypeIdentifier: string, location: Vector3, isTouching: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.assertentitytouching.description


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.assertentitytouching.description


////

//// define
`isTouching`：`boolean`

- script_api.@minecraft/server-gametest.test.istouching.assertentitytouching.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertentitytouching.return


////

///


/// define
`assertIsWaterlogged`


///

script_api.@minecraft/server-gametest.test.assertiswaterlogged.description

```js
assertIsWaterlogged(blockLocation: Vector3, isWaterlogged: boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertiswaterlogged.description


////

//// define
`isWaterlogged`：`boolean`

- script_api.@minecraft/server-gametest.test.iswaterlogged.assertiswaterlogged.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertiswaterlogged.return


////

///


/// define
`assertItemEntityCountIs`


///

script_api.@minecraft/server-gametest.test.assertitementitycountis.description

```js
assertItemEntityCountIs(itemType: ItemType | string, blockLocation: Vector3, searchDistance: float, count: int32): void
```

/// html | div.result
//// define
`itemType`：[`ItemType`](../../server/1.8.0/itemtype.md)|`string`

- script_api.@minecraft/server-gametest.test.itemtype.assertitementitycountis.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertitementitycountis.description


////

//// define
`searchDistance`：`float`

- script_api.@minecraft/server-gametest.test.searchdistance.assertitementitycountis.description


////

//// define
`count`：`int32`

- script_api.@minecraft/server-gametest.test.count.assertitementitycountis.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertitementitycountis.return


////

///


/// define
`assertItemEntityPresent`


///

script_api.@minecraft/server-gametest.test.assertitementitypresent.description

```js
assertItemEntityPresent(itemType: ItemType | string, blockLocation: Vector3, searchDistance: float, isPresent: boolean): void
```

/// html | div.result
//// define
`itemType`：[`ItemType`](../../server/1.8.0/itemtype.md)|`string`

- script_api.@minecraft/server-gametest.test.itemtype.assertitementitypresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertitementitypresent.description


////

//// define
`searchDistance`：`float`

- script_api.@minecraft/server-gametest.test.searchdistance.assertitementitypresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.assertitementitypresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertitementitypresent.return


////

///


/// define
`assertRedstonePower`


///

script_api.@minecraft/server-gametest.test.assertredstonepower.description

```js
assertRedstonePower(blockLocation: Vector3, power: int32): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.assertredstonepower.description


////

//// define
`power`：`int32`

- script_api.@minecraft/server-gametest.test.power.assertredstonepower.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.assertredstonepower.return


////

///


/// define
`destroyBlock`


///

script_api.@minecraft/server-gametest.test.destroyblock.description

```js
destroyBlock(blockLocation: Vector3, dropResources: boolean): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.destroyblock.description


////

//// define
`dropResources`：`boolean`

- script_api.@minecraft/server-gametest.test.dropresources.destroyblock.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.destroyblock.return


////

///


/// define
`fail`


///

script_api.@minecraft/server-gametest.test.fail.description

```js
fail(errorMessage: string): void
```

/// html | div.result
//// define
`errorMessage`：`string`

- script_api.@minecraft/server-gametest.test.errormessage.fail.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.fail.return


////

///


/// define
`failIf`


///

script_api.@minecraft/server-gametest.test.failif.description

```js
failIf(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.failif.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.failif.return


////

///


/// define
`getBlock`


///

script_api.@minecraft/server-gametest.test.getblock.description

```js
getBlock(blockLocation: Vector3): Block
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.getblock.description


////

//// define
返回值：[`Block`](../../server/1.8.0/block.md)

- script_api.@minecraft/server-gametest.test.getblock.return


////

///


/// define
`getDimension`


///

script_api.@minecraft/server-gametest.test.getdimension.description

```js
getDimension(): Dimension
```

/// html | div.result
//// define
返回值：[`Dimension`](../../server/1.8.0/dimension.md)

- script_api.@minecraft/server-gametest.test.getdimension.return


////

///


/// define
`getFenceConnectivity`


///

script_api.@minecraft/server-gametest.test.getfenceconnectivity.description

```js
getFenceConnectivity(blockLocation: Vector3): FenceConnectivity
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.getfenceconnectivity.description


////

//// define
返回值：[`FenceConnectivity`](./fenceconnectivity.md)

- script_api.@minecraft/server-gametest.test.getfenceconnectivity.return


////

///


/// define
`getSculkSpreader`


///

script_api.@minecraft/server-gametest.test.getsculkspreader.description

```js
getSculkSpreader(blockLocation: Vector3): SculkSpreader | undefined
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.getsculkspreader.description


////

//// define
返回值：[`SculkSpreader`](./sculkspreader.md)|`undefined`

- script_api.@minecraft/server-gametest.test.getsculkspreader.return


////

///


/// define
`getTestDirection`


///

script_api.@minecraft/server-gametest.test.gettestdirection.description

```js
getTestDirection(): Direction
```

/// html | div.result
//// define
返回值：[`Direction`](../../server/1.8.0/direction.md)

- script_api.@minecraft/server-gametest.test.gettestdirection.return


////

///


/// define
`idle`


///

script_api.@minecraft/server-gametest.test.idle.description

```js
idle(tickDelay: int32): Promise<void>
```

/// html | div.result
//// define
`tickDelay`：`int32`

- script_api.@minecraft/server-gametest.test.tickdelay.idle.description


////

//// define
返回值：`Promise<void>`

- script_api.@minecraft/server-gametest.test.idle.return


////

///


/// define
`killAllEntities`


///

script_api.@minecraft/server-gametest.test.killallentities.description

```js
killAllEntities(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.killallentities.return


////

///


/// define
`onPlayerJump`


///

script_api.@minecraft/server-gametest.test.onplayerjump.description

```js
onPlayerJump(mob: Entity, jumpAmount: int32): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.mob.onplayerjump.description


////

//// define
`jumpAmount`：`int32`

- script_api.@minecraft/server-gametest.test.jumpamount.onplayerjump.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.onplayerjump.return


////

///


/// define
`pressButton`


///

script_api.@minecraft/server-gametest.test.pressbutton.description

```js
pressButton(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.pressbutton.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.pressbutton.return


////

///


/// define
`print`


///

script_api.@minecraft/server-gametest.test.print.description

```js
print(text: string): void
```

/// html | div.result
//// define
`text`：`string`

- script_api.@minecraft/server-gametest.test.text.print.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.print.return


////

///


/// define
`pullLever`


///

script_api.@minecraft/server-gametest.test.pulllever.description

```js
pullLever(blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.pulllever.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.pulllever.return


////

///


/// define
`pulseRedstone`


///

script_api.@minecraft/server-gametest.test.pulseredstone.description

```js
pulseRedstone(blockLocation: Vector3, duration: int32): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.pulseredstone.description


////

//// define
`duration`：`int32`

- script_api.@minecraft/server-gametest.test.duration.pulseredstone.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.pulseredstone.return


////

///


/// define
`relativeBlockLocation`


///

script_api.@minecraft/server-gametest.test.relativeblocklocation.description

```js
relativeBlockLocation(worldBlockLocation: Vector3): Vector3
```

/// html | div.result
//// define
`worldBlockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.worldblocklocation.relativeblocklocation.description


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.relativeblocklocation.return


////

///


/// define
`relativeLocation`


///

script_api.@minecraft/server-gametest.test.relativelocation.description

```js
relativeLocation(worldLocation: Vector3): Vector3
```

/// html | div.result
//// define
`worldLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.worldlocation.relativelocation.description


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.relativelocation.return


////

///


/// define
`removeSimulatedPlayer`


///

script_api.@minecraft/server-gametest.test.removesimulatedplayer.description

```js
removeSimulatedPlayer(simulatedPlayer: SimulatedPlayer): void
```

/// html | div.result
//// define
`simulatedPlayer`：[`SimulatedPlayer`](./simulatedplayer.md)

- script_api.@minecraft/server-gametest.test.simulatedplayer.removesimulatedplayer.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.removesimulatedplayer.return


////

///


/// define
`rotateDirection`


///

script_api.@minecraft/server-gametest.test.rotatedirection.description

```js
rotateDirection(direction: Direction): Direction
```

/// html | div.result
//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- script_api.@minecraft/server-gametest.test.direction.rotatedirection.description


////

//// define
返回值：[`Direction`](../../server/1.8.0/direction.md)

- script_api.@minecraft/server-gametest.test.rotatedirection.return


////

///


/// define
`rotateVector`


///

script_api.@minecraft/server-gametest.test.rotatevector.description

```js
rotateVector(vector: Vector3): Vector3
```

/// html | div.result
//// define
`vector`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.vector.rotatevector.description


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.rotatevector.return


////

///


/// define
`runAfterDelay`


///

script_api.@minecraft/server-gametest.test.runafterdelay.description

```js
runAfterDelay(delayTicks: int32, callback: () => void): void
```

/// html | div.result
//// define
`delayTicks`：`int32`

- script_api.@minecraft/server-gametest.test.delayticks.runafterdelay.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.runafterdelay.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.runafterdelay.return


////

///


/// define
`runAtTickTime`


///

script_api.@minecraft/server-gametest.test.runatticktime.description

```js
runAtTickTime(tick: int32, callback: () => void): void
```

/// html | div.result
//// define
`tick`：`int32`

- script_api.@minecraft/server-gametest.test.tick.runatticktime.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.runatticktime.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.runatticktime.return


////

///


/// define
`setBlockPermutation`


///

script_api.@minecraft/server-gametest.test.setblockpermutation.description

```js
setBlockPermutation(blockData: BlockPermutation, blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockData`：[`BlockPermutation`](../../server/1.8.0/blockpermutation.md)

- script_api.@minecraft/server-gametest.test.blockdata.setblockpermutation.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.setblockpermutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.setblockpermutation.return


////

///


/// define
`setBlockType`


///

script_api.@minecraft/server-gametest.test.setblocktype.description

```js
setBlockType(blockType: BlockType | string, blockLocation: Vector3): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.blocktype.setblocktype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.setblocktype.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.setblocktype.return


////

///


/// define
`setFluidContainer`


///

script_api.@minecraft/server-gametest.test.setfluidcontainer.description

```js
setFluidContainer(location: Vector3, type: FluidType): void
```

/// html | div.result
//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.setfluidcontainer.description


////

//// define
`type`：[`FluidType`](../../server/1.8.0/fluidtype.md)

- script_api.@minecraft/server-gametest.test.type.setfluidcontainer.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.setfluidcontainer.return


////

///


/// define
`setTntFuse`


///

script_api.@minecraft/server-gametest.test.settntfuse.description

```js
setTntFuse(entity: Entity, fuseLength: int32): void
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.entity.settntfuse.description


////

//// define
`fuseLength`：`int32`

- script_api.@minecraft/server-gametest.test.fuselength.settntfuse.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.settntfuse.return


////

///


/// define
`spawn`


///

script_api.@minecraft/server-gametest.test.spawn.description

```js
spawn(entityTypeIdentifier: string, blockLocation: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.spawn.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.spawn.description


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.spawn.return


////

///


/// define
`spawnAtLocation`


///

script_api.@minecraft/server-gametest.test.spawnatlocation.description

```js
spawnAtLocation(entityTypeIdentifier: string, location: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.spawnatlocation.description


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.spawnatlocation.description


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.spawnatlocation.return


////

///


/// define
`spawnItem`


///

script_api.@minecraft/server-gametest.test.spawnitem.description

```js
spawnItem(itemStack: ItemStack, location: Vector3): Entity
```

/// html | div.result
//// define
`itemStack`：[`ItemStack`](../../server/1.8.0/itemstack.md)

- script_api.@minecraft/server-gametest.test.itemstack.spawnitem.description


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.spawnitem.description


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.spawnitem.return


////

///


/// define
`spawnSimulatedPlayer`


///

script_api.@minecraft/server-gametest.test.spawnsimulatedplayer.description

```js
spawnSimulatedPlayer(blockLocation: Vector3, name: string, gameMode: GameMode): SimulatedPlayer
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.spawnsimulatedplayer.description


////

//// define
`name`：`string`

- script_api.@minecraft/server-gametest.test.name.spawnsimulatedplayer.description


////

//// define
`gameMode`：[`GameMode`](../../server/1.8.0/gamemode.md)

- script_api.@minecraft/server-gametest.test.gamemode.spawnsimulatedplayer.description


////

//// define
返回值：[`SimulatedPlayer`](./simulatedplayer.md)

- script_api.@minecraft/server-gametest.test.spawnsimulatedplayer.return


////

///


/// define
`spawnWithoutBehaviors`


///

script_api.@minecraft/server-gametest.test.spawnwithoutbehaviors.description

```js
spawnWithoutBehaviors(entityTypeIdentifier: string, blockLocation: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.spawnwithoutbehaviors.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.spawnwithoutbehaviors.description


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviors.return


////

///


/// define
`spawnWithoutBehaviorsAtLocation`


///

script_api.@minecraft/server-gametest.test.spawnwithoutbehaviorsatlocation.description

```js
spawnWithoutBehaviorsAtLocation(entityTypeIdentifier: string, location: Vector3): Entity
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.spawnwithoutbehaviorsatlocation.description


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.spawnwithoutbehaviorsatlocation.description


////

//// define
返回值：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviorsatlocation.return


////

///


/// define
`spreadFromFaceTowardDirection`


///

script_api.@minecraft/server-gametest.test.spreadfromfacetowarddirection.description

```js
spreadFromFaceTowardDirection(blockLocation: Vector3, fromFace: Direction, direction: Direction): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.spreadfromfacetowarddirection.description


////

//// define
`fromFace`：[`Direction`](../../server/1.8.0/direction.md)

- script_api.@minecraft/server-gametest.test.fromface.spreadfromfacetowarddirection.description


////

//// define
`direction`：[`Direction`](../../server/1.8.0/direction.md)

- script_api.@minecraft/server-gametest.test.direction.spreadfromfacetowarddirection.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.spreadfromfacetowarddirection.return


////

///


/// define
`startSequence`


///

script_api.@minecraft/server-gametest.test.startsequence.description

```js
startSequence(): GameTestSequence
```

/// html | div.result
//// define
返回值：[`GameTestSequence`](./gametestsequence.md)

- script_api.@minecraft/server-gametest.test.startsequence.return


////

///


/// define
`succeed`


///

script_api.@minecraft/server-gametest.test.succeed.description

```js
succeed(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeed.return


////

///


/// define
`succeedIf`


///

script_api.@minecraft/server-gametest.test.succeedif.description

```js
succeedIf(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.succeedif.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedif.return


////

///


/// define
`succeedOnTick`


///

script_api.@minecraft/server-gametest.test.succeedontick.description

```js
succeedOnTick(tick: int32): void
```

/// html | div.result
//// define
`tick`：`int32`

- script_api.@minecraft/server-gametest.test.tick.succeedontick.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedontick.return


////

///


/// define
`succeedOnTickWhen`


///

script_api.@minecraft/server-gametest.test.succeedontickwhen.description

```js
succeedOnTickWhen(tick: int32, callback: () => void): void
```

/// html | div.result
//// define
`tick`：`int32`

- script_api.@minecraft/server-gametest.test.tick.succeedontickwhen.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.succeedontickwhen.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedontickwhen.return


////

///


/// define
`succeedWhen`


///

script_api.@minecraft/server-gametest.test.succeedwhen.description

```js
succeedWhen(callback: () => void): void
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.succeedwhen.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedwhen.return


////

///


/// define
`succeedWhenBlockPresent`


///

script_api.@minecraft/server-gametest.test.succeedwhenblockpresent.description

```js
succeedWhenBlockPresent(blockType: BlockType | string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](../../server/1.8.0/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.blocktype.succeedwhenblockpresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.succeedwhenblockpresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.succeedwhenblockpresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedwhenblockpresent.return


////

///


/// define
`succeedWhenEntityHasComponent`


///

script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.description

```js
succeedWhenEntityHasComponent(entityTypeIdentifier: string, componentIdentifier: string, blockLocation: Vector3, hasComponent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.succeedwhenentityhascomponent.description


////

//// define
`componentIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.componentidentifier.succeedwhenentityhascomponent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.succeedwhenentityhascomponent.description


////

//// define
`hasComponent`：`boolean`

- script_api.@minecraft/server-gametest.test.hascomponent.succeedwhenentityhascomponent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.return


////

///


/// define
`succeedWhenEntityPresent`


///

script_api.@minecraft/server-gametest.test.succeedwhenentitypresent.description

```js
succeedWhenEntityPresent(entityTypeIdentifier: string, blockLocation: Vector3, isPresent: boolean): void
```

/// html | div.result
//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.entitytypeidentifier.succeedwhenentitypresent.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.succeedwhenentitypresent.description


////

//// define
`isPresent`：`boolean`

- script_api.@minecraft/server-gametest.test.ispresent.succeedwhenentitypresent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.succeedwhenentitypresent.return


////

///


/// define
`triggerInternalBlockEvent`


///

script_api.@minecraft/server-gametest.test.triggerinternalblockevent.description

```js
triggerInternalBlockEvent(blockLocation: Vector3, event: string, eventParameters: float[]): void
```

/// html | div.result
//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.triggerinternalblockevent.description


////

//// define
`event`：`string`

- script_api.@minecraft/server-gametest.test.event.triggerinternalblockevent.description


////

//// define
`eventParameters`：`float[]`

- script_api.@minecraft/server-gametest.test.eventparameters.triggerinternalblockevent.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.triggerinternalblockevent.return


////

///


/// define
`until`


///

script_api.@minecraft/server-gametest.test.until.description

```js
until(callback: () => void): Promise<void>
```

/// html | div.result
//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.callback.until.description


////

//// define
返回值：`Promise<void>`

- script_api.@minecraft/server-gametest.test.until.return


////

///


/// define
`walkTo`


///

script_api.@minecraft/server-gametest.test.walkto.description

```js
walkTo(mob: Entity, blockLocation: Vector3, speedModifier: float): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.mob.walkto.description


////

//// define
`blockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.blocklocation.walkto.description


////

//// define
`speedModifier`：`float`

- script_api.@minecraft/server-gametest.test.speedmodifier.walkto.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.walkto.return


////

///


/// define
`walkToLocation`


///

script_api.@minecraft/server-gametest.test.walktolocation.description

```js
walkToLocation(mob: Entity, location: Vector3, speedModifier: float): void
```

/// html | div.result
//// define
`mob`：[`Entity`](../../server/1.8.0/entity.md)

- script_api.@minecraft/server-gametest.test.mob.walktolocation.description


////

//// define
`location`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.location.walktolocation.description


////

//// define
`speedModifier`：`float`

- script_api.@minecraft/server-gametest.test.speedmodifier.walktolocation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-gametest.test.walktolocation.return


////

///


/// define
`worldBlockLocation`


///

script_api.@minecraft/server-gametest.test.worldblocklocation.description

```js
worldBlockLocation(relativeBlockLocation: Vector3): Vector3
```

/// html | div.result
//// define
`relativeBlockLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.relativeblocklocation.worldblocklocation.description


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.worldblocklocation.return


////

///


/// define
`worldLocation`


///

script_api.@minecraft/server-gametest.test.worldlocation.description

```js
worldLocation(relativeLocation: Vector3): Vector3
```

/// html | div.result
//// define
`relativeLocation`：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.relativelocation.worldlocation.description


////

//// define
返回值：[`Vector3`](../../server/1.8.0/vector3.md)

- script_api.@minecraft/server-gametest.test.worldlocation.return


////

///

