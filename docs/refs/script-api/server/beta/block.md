# `Block`

> 文档版本：1.21.60.21

`Block`类。代表维度中的一个方块。一个方块对应了一维度中唯一的X、Y和Z轴坐标值，可读取或修改该坐标下的方块状态等数据。

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

- 返回该方块所在的维度的对象。


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

- 如果该方块为空气，值为`true`。


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

- 如果该方块属于液体方块（含水方块不属于液体方块），值为`true`。


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

- 如果该方块属于固体方块，值为`true`。


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

- 表示并接受设置该方块是否含水。如果该方块含水，值为`true`。


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

- 该方块的坐标。


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

- 该方块的置换。


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

- 该方块的类型。


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

- 该方块的类型对应的标识符。


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

- 该方块的X轴坐标值。


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

- 该方块的Y轴坐标值。


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

- 该方块的Z轴坐标值。


////

///


## 方法

/// define
`above`


///

获取位于该方块上方一定距离处的方块（即Y轴正方向延长线上的方块）。

```js
above(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向Y轴正方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`below`


///

获取位于该方块下方一定距离处的方块（即Y轴负方向延长线上的方块）。

```js
below(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向Y轴负方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`bottomCenter`


///

获取该方块底面中心处的坐标（即该方块在X和Z轴上的中心坐标）。

```js
bottomCenter(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 包含该方块底面中心处坐标值的`Vector3`对象。


////

///


/// define
`canPlace`


///

根据类型或置换检查是否可在该方块的某个面上放置给定的方块。

```js
canPlace(blockToPlace: BlockPermutation | BlockType | string, faceToPlaceOn?: Direction): boolean
```

/// html | div.result
//// define
`blockToPlace`：[`BlockPermutation`](./blockpermutation.md)|[`BlockType`](./blocktype.md)|`string`

- 要检查放置可行性的方块类型(`BlockType`对象)或方块置换(`BlockPermutation`对象)。


////

//// define
`faceToPlaceOn`?：[`Direction`](./direction.md)＝`null`

- 要检查的面。


////

//// define
返回值：`boolean`

- 如果给定的方块可以放置在该方块的这个面上，返回`true`。


////

///


/// define
`center`


///

获取该方块中心处的坐标（即该方块在X、Y和Z轴上的中心坐标）。

```js
center(): Vector3
```

/// html | div.result
//// define
返回值：[`Vector3`](./vector3.md)

- 包含该方块中心处坐标值的`Vector3`对象。


////

///


/// define
`east`


///

获取位于该方块东面一定距离处的方块（即X轴正方向延长线上的方块）。

```js
east(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向X轴正方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`getComponent`


///

获取一个该方块的组件。

```js
getComponent(componentId: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- 要获取的组件的标识符。


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- 如果该方块具有这个组件，返回该组件的对象，否则返回`undefined`。


////

///


/// define
`getItemStack`


///

创建一个基于该方块的物品堆叠。

```js
getItemStack(amount: int32, withData: boolean): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`＝`1`∈[`1`, `255`]

- 该物品堆叠所含物品的数量。


////

//// define
`withData`：`boolean`＝`False`

- 该物品堆叠是否附加用户数据。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 创建出的物品堆叠对象。如果方块类型不兼容则返回`undefined`。


////

///


/// define
`getMapColor`


///

script_api.@minecraft/server.block.getmapcolor.description

```js
getMapColor(): RGBA
```

/// html | div.result
//// define
返回值：[`RGBA`](./rgba.md)

- script_api.@minecraft/server.block.getmapcolor.return


////

///


/// define
`getRedstonePower`


///

获取该方块的净红石能量强度。

```js
getRedstonePower(): int32 | undefined
```

/// html | div.result
//// define
返回值：`int32`|`undefined`

- 如果该方块可被充能，返回其红石能量强度，否则返回`undefined`。


////

///


/// define
`getTags`


///

获取该方块的所有标签。

```js
getTags(): string[]
```

/// html | div.result
//// define
返回值：`string[]`

- 一个包含该方块所有标签的数组。


////

///


/// define
`hasTag`


///

检查该方块的置换中是否具有指定的标签。

```js
hasTag(tag: string): boolean
```

/// html | div.result
//// define
`tag`：`string`

- 要检查的标签。


////

//// define
返回值：`boolean`

- 如果该方块的置换中具有此标签，返回`true`。


////

///


/// define
`isValid`


///

检查该方块是否有效（被加载且在可放置方块范围内）。

```js
isValid(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 如果该方块有效，返回`true`。


////

///


/// define
`matches`


///

测试该方块是否符合给定条件（方块类型和方块状态）。

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- 要测试的方块类型的标识符。


////

//// define
`states`?：`Record<string, boolean | int32 | string>`＝`null`

- 要测试的方块状态集合。


////

//// define
返回值：`boolean`

- 如果该方块符合给定的条件，返回`true`。


////

///


/// define
`north`


///

获取位于该方块北面一定距离处的方块（即Z轴负方向延长线上的方块）。

```js
north(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向Z轴负方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`offset`


///

获取相对于该方块位置给定偏移量处的方块。

```js
offset(offset: Vector3): Block | undefined
```

/// html | div.result
//// define
`offset`：[`Vector3`](./vector3.md)

- 要偏移的量（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`setPermutation`


///

设置该方块的置换。

```js
setPermutation(permutation: BlockPermutation): void
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- 要设置的置换的对象。


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setpermutation.return


////

///


/// define
`setType`


///

设置该方块的类型。

```js
setType(blockType: BlockType | string): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](./blocktype.md)|`string`

- 要设置的类型的标识符或`BlockType`对象。


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.settype.return


////

///


/// define
`setWaterlogged`


///

设置该方块的含水情况（仅对可含水方块有效）。

```js
setWaterlogged(isWaterlogged: boolean): void
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- 如果为`true`，则使该方块含水，否则取消含水。


////

//// define
返回值：`void`

- script_api.@minecraft/server.block.setwaterlogged.return


////

///


/// define
`south`


///

获取位于该方块南面一定距离处的方块（即Z轴正方向延长线上的方块）。

```js
south(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向Z轴正方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///


/// define
`trySetPermutation`


///

先检查放置可行性，然后再尝试设置该方块的置换。

```js
trySetPermutation(permutation: BlockPermutation): boolean
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- 要设置的置换的`BlockPermutation`对象。


////

//// define
返回值：`boolean`

- 如果成功设置了该方块的置换，返回`true`。


////

///


/// define
`west`


///

获取位于该方块西面一定距离处的方块（即X轴负方向延长线上的方块）。

```js
west(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`＝`1`

- 向X轴负方向延伸的距离（以米为单位）。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 获取到的方块对象。


////

///

