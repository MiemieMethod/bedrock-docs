# `Block`

> 文档版本：1.21.0.20

`Block`类。script_api.@minecraft/server.block.description

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

- script_api.@minecraft/server.block.dimension.description


////

///


/// define
`isAir`


///

```js
read-only isAir: boolean;
```

/// html | div.result
//// define
`isAir`：`boolean`

- script_api.@minecraft/server.block.isair.description


////

///


/// define
`isLiquid`


///

```js
read-only isLiquid: boolean;
```

/// html | div.result
//// define
`isLiquid`：`boolean`

- script_api.@minecraft/server.block.isliquid.description


////

///


/// define
`isSolid`


///

```js
read-only isSolid: boolean;
```

/// html | div.result
//// define
`isSolid`：`boolean`

- script_api.@minecraft/server.block.issolid.description


////

///


/// define
`isWaterlogged`


///

```js
read-only isWaterlogged: boolean;
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- script_api.@minecraft/server.block.iswaterlogged.description


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

- script_api.@minecraft/server.block.location.description


////

///


/// define
`permutation`


///

```js
read-only permutation: BlockPermutation;
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.block.permutation.description


////

///


/// define
`type`


///

```js
read-only type: BlockType;
```

/// html | div.result
//// define
`type`：[`BlockType`](./blocktype.md)

- script_api.@minecraft/server.block.type.description


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

- script_api.@minecraft/server.block.typeid.description


////

///


/// define
`x`


///

```js
read-only x: int32;
```

/// html | div.result
//// define
`x`：`int32`

- script_api.@minecraft/server.block.x.description


////

///


/// define
`y`


///

```js
read-only y: int32;
```

/// html | div.result
//// define
`y`：`int32`

- script_api.@minecraft/server.block.y.description


////

///


/// define
`z`


///

```js
read-only z: int32;
```

/// html | div.result
//// define
`z`：`int32`

- script_api.@minecraft/server.block.z.description


////

///


## 方法

/// define
`above`


///

script_api.@minecraft/server.block.above.description

```js
above(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.above.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.above.return


////

///


/// define
`below`


///

script_api.@minecraft/server.block.below.description

```js
below(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.below.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.below.return


////

///


/// define
`bottomCenter`


///

script_api.@minecraft/server.block.bottomcenter.description

```js
bottomCenter(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.bottomcenter.return


////

///


/// define
`canPlace`


///

script_api.@minecraft/server.block.canplace.description

```js
canPlace(blockToPlace: BlockPermutation | BlockType | string, faceToPlaceOn?: Direction): boolean
```

/// html | div.result
//// define
`blockToPlace`：[`BlockPermutation`](./blockpermutation.md)|[`BlockType`](./blocktype.md)|`string`

- script_api.@minecraft/server.block.canplace.blocktoplace.description


////

//// define
`faceToPlaceOn`：[`Direction`](./direction.md)|`undefined`

- script_api.@minecraft/server.block.canplace.facetoplaceon.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.block.canplace.return


////

///


/// define
`center`


///

script_api.@minecraft/server.block.center.description

```js
center(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.center.return


////

///


/// define
`east`


///

script_api.@minecraft/server.block.east.description

```js
east(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.east.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.east.return


////

///


/// define
`getComponent`


///

script_api.@minecraft/server.block.getcomponent.description

```js
getComponent(componentId: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- script_api.@minecraft/server.block.getcomponent.componentid.description


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- script_api.@minecraft/server.block.getcomponent.return


////

///


/// define
`getItemStack`


///

script_api.@minecraft/server.block.getitemstack.description

```js
getItemStack(amount: int32, withData: boolean): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`

- script_api.@minecraft/server.block.getitemstack.amount.description


////

//// define
`withData`：`boolean`

- script_api.@minecraft/server.block.getitemstack.withdata.description


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- script_api.@minecraft/server.block.getitemstack.return


////

///


/// define
`getRedstonePower`


///

script_api.@minecraft/server.block.getredstonepower.description

```js
getRedstonePower(): int32 | undefined
```

/// html | div.result
//// define
返回值：`int32`|`undefined`

- script_api.@minecraft/server.block.getredstonepower.return


////

///


/// define
`getTags`


///

script_api.@minecraft/server.block.gettags.description

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- script_api.@minecraft/server.block.gettags.return


////

///


/// define
`hasTag`


///

script_api.@minecraft/server.block.hastag.description

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- script_api.@minecraft/server.block.hastag.tag.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.block.hastag.return


////

///


/// define
`isValid`


///

script_api.@minecraft/server.block.isvalid.description

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server.block.isvalid.return


////

///


/// define
`matches`


///

script_api.@minecraft/server.block.matches.description

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- script_api.@minecraft/server.block.matches.blockname.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.block.matches.states.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.block.matches.return


////

///


/// define
`north`


///

script_api.@minecraft/server.block.north.description

```js
north(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.north.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.north.return


////

///


/// define
`offset`


///

script_api.@minecraft/server.block.offset.description

```js
offset(offset: Vector3): Block | undefined
```

/// html | div.result
//// define
`offset`：[`Vector3`](./vector3.md)

- script_api.@minecraft/server.block.offset.offset.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.offset.return


////

///


/// define
`setPermutation`


///

script_api.@minecraft/server.block.setpermutation.description

```js
setPermutation(permutation: BlockPermutation): void
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.block.setpermutation.permutation.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setpermutation.return


////

///


/// define
`setType`


///

script_api.@minecraft/server.block.settype.description

```js
setType(blockType: BlockType | string): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](./blocktype.md)|`string`

- script_api.@minecraft/server.block.settype.blocktype.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.settype.return


////

///


/// define
`setWaterlogged`


///

script_api.@minecraft/server.block.setwaterlogged.description

```js
setWaterlogged(isWaterlogged: boolean): void
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- script_api.@minecraft/server.block.setwaterlogged.iswaterlogged.description


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setwaterlogged.return


////

///


/// define
`south`


///

script_api.@minecraft/server.block.south.description

```js
south(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.south.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.south.return


////

///


/// define
`trySetPermutation`


///

script_api.@minecraft/server.block.trysetpermutation.description

```js
trySetPermutation(permutation: BlockPermutation): boolean
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.block.trysetpermutation.permutation.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.block.trysetpermutation.return


////

///


/// define
`west`


///

script_api.@minecraft/server.block.west.description

```js
west(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- script_api.@minecraft/server.block.west.steps.description


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- script_api.@minecraft/server.block.west.return


////

///

