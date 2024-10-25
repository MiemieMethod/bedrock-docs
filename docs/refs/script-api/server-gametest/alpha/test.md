# `Test`

> 文档版本：1.21.50.25

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

- script_api.@minecraft/server-gametest.test.assert.condition.description


////

//// define
`message`：`string`

- script_api.@minecraft/server-gametest.test.assert.message.description


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
`blockType`：[`BlockType`](../../server/2.0.0-alpha/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.assertblockpresent.blocktype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertblockpresent.blocklocation.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertblockpresent.ispresent.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertblockstate.blocklocation.description


////

//// define
`callback`：<code>(<a href="../../../server/2.0.0-alpha/block/">Block</a>) =&gt; boolean</code>

- script_api.@minecraft/server-gametest.test.assertblockstate.callback.description


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
`mob`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.assertcanreachlocation.mob.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertcanreachlocation.blocklocation.description


////

//// define
`canReach`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertcanreachlocation.canreach.description


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
`itemStack`：[`ItemStack`](../../server/2.0.0-alpha/itemstack.md)

- script_api.@minecraft/server-gametest.test.assertcontainercontains.itemstack.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertcontainercontains.blocklocation.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertcontainerempty.blocklocation.description


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

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.entitytypeidentifier.description


////

//// define
`armorSlot`：`int32`

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.armorslot.description


////

//// define
`armorName`：`string`

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.armorname.description


////

//// define
`armorData`：`int32`

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.armordata.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.blocklocation.description


////

//// define
`hasArmor`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentityhasarmor.hasarmor.description


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

- script_api.@minecraft/server-gametest.test.assertentityhascomponent.entitytypeidentifier.description


////

//// define
`componentIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.assertentityhascomponent.componentidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentityhascomponent.blocklocation.description


////

//// define
`hasComponent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentityhascomponent.hascomponent.description


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
`entity`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.assertentityinstancepresent.entity.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentityinstancepresent.blocklocation.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentityinstancepresent.ispresent.description


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
`entity`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.assertentityinstancepresentinarea.entity.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentityinstancepresentinarea.ispresent.description


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

- script_api.@minecraft/server-gametest.test.assertentitypresent.entitytypeidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentitypresent.blocklocation.description


////

//// define
`searchDistance`：`float`＝`0.0`

- script_api.@minecraft/server-gametest.test.assertentitypresent.searchdistance.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentitypresent.ispresent.description


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

- script_api.@minecraft/server-gametest.test.assertentitypresentinarea.entitytypeidentifier.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentitypresentinarea.ispresent.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentitystate.blocklocation.description


////

//// define
`entityTypeIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.assertentitystate.entitytypeidentifier.description


////

//// define
`callback`：<code>(<a href="../../../server/2.0.0-alpha/entity/">Entity</a>) =&gt; boolean</code>

- script_api.@minecraft/server-gametest.test.assertentitystate.callback.description


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

- script_api.@minecraft/server-gametest.test.assertentitytouching.entitytypeidentifier.description


////

//// define
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertentitytouching.location.description


////

//// define
`isTouching`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertentitytouching.istouching.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertiswaterlogged.blocklocation.description


////

//// define
`isWaterlogged`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertiswaterlogged.iswaterlogged.description


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
`itemType`：[`ItemType`](../../server/2.0.0-alpha/itemtype.md)|`string`

- script_api.@minecraft/server-gametest.test.assertitementitycountis.itemtype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertitementitycountis.blocklocation.description


////

//// define
`searchDistance`：`float`

- script_api.@minecraft/server-gametest.test.assertitementitycountis.searchdistance.description


////

//// define
`count`：`int32`

- script_api.@minecraft/server-gametest.test.assertitementitycountis.count.description


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
`itemType`：[`ItemType`](../../server/2.0.0-alpha/itemtype.md)|`string`

- script_api.@minecraft/server-gametest.test.assertitementitypresent.itemtype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertitementitypresent.blocklocation.description


////

//// define
`searchDistance`：`float`＝`0.0`

- script_api.@minecraft/server-gametest.test.assertitementitypresent.searchdistance.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.assertitementitypresent.ispresent.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.assertredstonepower.blocklocation.description


////

//// define
`power`：`int32`

- script_api.@minecraft/server-gametest.test.assertredstonepower.power.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.destroyblock.blocklocation.description


////

//// define
`dropResources`：`boolean`＝`False`

- script_api.@minecraft/server-gametest.test.destroyblock.dropresources.description


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

- script_api.@minecraft/server-gametest.test.fail.errormessage.description


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

- script_api.@minecraft/server-gametest.test.failif.callback.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.getblock.blocklocation.description


////

//// define
返回值：[`Block`](../../server/2.0.0-alpha/block.md)

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
返回值：[`Dimension`](../../server/2.0.0-alpha/dimension.md)

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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.getfenceconnectivity.blocklocation.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.getsculkspreader.blocklocation.description


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
返回值：[`Direction`](../../server/2.0.0-alpha/direction.md)

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

- script_api.@minecraft/server-gametest.test.idle.tickdelay.description


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
`mob`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.onplayerjump.mob.description


////

//// define
`jumpAmount`：`int32`

- script_api.@minecraft/server-gametest.test.onplayerjump.jumpamount.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.pressbutton.blocklocation.description


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

- script_api.@minecraft/server-gametest.test.print.text.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.pulllever.blocklocation.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.pulseredstone.blocklocation.description


////

//// define
`duration`：`int32`

- script_api.@minecraft/server-gametest.test.pulseredstone.duration.description


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
`worldBlockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.relativeblocklocation.worldblocklocation.description


////

//// define
返回值：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

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
`worldLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.relativelocation.worldlocation.description


////

//// define
返回值：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

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

- script_api.@minecraft/server-gametest.test.removesimulatedplayer.simulatedplayer.description


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
`direction`：[`Direction`](../../server/2.0.0-alpha/direction.md)

- script_api.@minecraft/server-gametest.test.rotatedirection.direction.description


////

//// define
返回值：[`Direction`](../../server/2.0.0-alpha/direction.md)

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
`vector`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.rotatevector.vector.description


////

//// define
返回值：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

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

- script_api.@minecraft/server-gametest.test.runafterdelay.delayticks.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.runafterdelay.callback.description


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

- script_api.@minecraft/server-gametest.test.runatticktime.tick.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.runatticktime.callback.description


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
`blockData`：[`BlockPermutation`](../../server/2.0.0-alpha/blockpermutation.md)

- script_api.@minecraft/server-gametest.test.setblockpermutation.blockdata.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.setblockpermutation.blocklocation.description


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
`blockType`：[`BlockType`](../../server/2.0.0-alpha/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.setblocktype.blocktype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.setblocktype.blocklocation.description


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
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.setfluidcontainer.location.description


////

//// define
`type`：[`FluidType`](../../server/2.0.0-alpha/fluidtype.md)

- script_api.@minecraft/server-gametest.test.setfluidcontainer.type.description


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
`entity`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.settntfuse.entity.description


////

//// define
`fuseLength`：`int32`

- script_api.@minecraft/server-gametest.test.settntfuse.fuselength.description


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

- script_api.@minecraft/server-gametest.test.spawn.entitytypeidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawn.blocklocation.description


////

//// define
返回值：[`Entity`](../../server/2.0.0-alpha/entity.md)

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

- script_api.@minecraft/server-gametest.test.spawnatlocation.entitytypeidentifier.description


////

//// define
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawnatlocation.location.description


////

//// define
返回值：[`Entity`](../../server/2.0.0-alpha/entity.md)

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
`itemStack`：[`ItemStack`](../../server/2.0.0-alpha/itemstack.md)

- script_api.@minecraft/server-gametest.test.spawnitem.itemstack.description


////

//// define
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawnitem.location.description


////

//// define
返回值：[`Entity`](../../server/2.0.0-alpha/entity.md)

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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawnsimulatedplayer.blocklocation.description


////

//// define
`name`：`string`＝`Simulated Player`

- script_api.@minecraft/server-gametest.test.spawnsimulatedplayer.name.description


////

//// define
`gameMode`：[`GameMode`](../../server/2.0.0-alpha/gamemode.md)＝`0`

- script_api.@minecraft/server-gametest.test.spawnsimulatedplayer.gamemode.description


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

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviors.entitytypeidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviors.blocklocation.description


////

//// define
返回值：[`Entity`](../../server/2.0.0-alpha/entity.md)

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

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviorsatlocation.entitytypeidentifier.description


////

//// define
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spawnwithoutbehaviorsatlocation.location.description


////

//// define
返回值：[`Entity`](../../server/2.0.0-alpha/entity.md)

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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.spreadfromfacetowarddirection.blocklocation.description


////

//// define
`fromFace`：[`Direction`](../../server/2.0.0-alpha/direction.md)

- script_api.@minecraft/server-gametest.test.spreadfromfacetowarddirection.fromface.description


////

//// define
`direction`：[`Direction`](../../server/2.0.0-alpha/direction.md)

- script_api.@minecraft/server-gametest.test.spreadfromfacetowarddirection.direction.description


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

- script_api.@minecraft/server-gametest.test.succeedif.callback.description


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

- script_api.@minecraft/server-gametest.test.succeedontick.tick.description


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

- script_api.@minecraft/server-gametest.test.succeedontickwhen.tick.description


////

//// define
`callback`：<code>() =&gt; void</code>

- script_api.@minecraft/server-gametest.test.succeedontickwhen.callback.description


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

- script_api.@minecraft/server-gametest.test.succeedwhen.callback.description


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
`blockType`：[`BlockType`](../../server/2.0.0-alpha/blocktype.md)|`string`

- script_api.@minecraft/server-gametest.test.succeedwhenblockpresent.blocktype.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.succeedwhenblockpresent.blocklocation.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.succeedwhenblockpresent.ispresent.description


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

- script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.entitytypeidentifier.description


////

//// define
`componentIdentifier`：`string`

- script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.componentidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.blocklocation.description


////

//// define
`hasComponent`：`boolean`

- script_api.@minecraft/server-gametest.test.succeedwhenentityhascomponent.hascomponent.description


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

- script_api.@minecraft/server-gametest.test.succeedwhenentitypresent.entitytypeidentifier.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.succeedwhenentitypresent.blocklocation.description


////

//// define
`isPresent`：`boolean`＝`True`

- script_api.@minecraft/server-gametest.test.succeedwhenentitypresent.ispresent.description


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
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.triggerinternalblockevent.blocklocation.description


////

//// define
`event`：`string`

- script_api.@minecraft/server-gametest.test.triggerinternalblockevent.event.description


////

//// define
`eventParameters`：`float[]`＝`[]`

- script_api.@minecraft/server-gametest.test.triggerinternalblockevent.eventparameters.description


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

- script_api.@minecraft/server-gametest.test.until.callback.description


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
`mob`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.walkto.mob.description


////

//// define
`blockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.walkto.blocklocation.description


////

//// define
`speedModifier`：`float`＝`1.0`

- script_api.@minecraft/server-gametest.test.walkto.speedmodifier.description


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
`mob`：[`Entity`](../../server/2.0.0-alpha/entity.md)

- script_api.@minecraft/server-gametest.test.walktolocation.mob.description


////

//// define
`location`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.walktolocation.location.description


////

//// define
`speedModifier`：`float`＝`1.0`

- script_api.@minecraft/server-gametest.test.walktolocation.speedmodifier.description


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
`relativeBlockLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.worldblocklocation.relativeblocklocation.description


////

//// define
返回值：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

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
`relativeLocation`：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.worldlocation.relativelocation.description


////

//// define
返回值：[`Vector3`](../../server/2.0.0-alpha/vector3.md)

- script_api.@minecraft/server-gametest.test.worldlocation.return


////

///

