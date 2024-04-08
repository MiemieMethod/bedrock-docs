# `Block`

> 文档版本：1.21.0.20

`Block`类。

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension;
```


/// define
`isAir`


///

```js
read-only isAir: boolean;
```


/// define
`isLiquid`


///

```js
read-only isLiquid: boolean;
```


/// define
`isSolid`


///

```js
read-only isSolid: boolean;
```


/// define
`isWaterlogged`


///

```js
read-only isWaterlogged: boolean;
```


/// define
`location`


///

```js
read-only location: Vector3;
```


/// define
`permutation`


///

```js
read-only permutation: BlockPermutation;
```


/// define
`type`


///

```js
read-only type: BlockType;
```


/// define
`typeId`


///

```js
read-only typeId: string;
```


/// define
`x`


///

```js
read-only x: int32;
```


/// define
`y`


///

```js
read-only y: int32;
```


/// define
`z`


///

```js
read-only z: int32;
```


## 方法

/// define
`above`


///

```js
above(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`below`


///

```js
below(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`bottomCenter`


///

```js
bottomCenter(): Vector3
```

/// html | div.result

///


/// define
`canPlace`


///

```js
canPlace(blockToPlace: BlockPermutation | BlockType | string, faceToPlaceOn?: Direction): boolean
```

/// html | div.result
//// define
`blockToPlace`：BlockPermutation|BlockType|string

- 参数1。


////

//// define
`faceToPlaceOn`：[`Direction`](./direction.md)|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`center`


///

```js
center(): Vector3
```

/// html | div.result

///


/// define
`east`


///

```js
east(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

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
getComponent(componentId: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentId`：`string`

- 参数1。


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

- 返回值。


////

///


/// define
`getItemStack`


///

```js
getItemStack(amount: int32, withData: boolean): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`

- 参数1。


////

//// define
`withData`：`boolean`

- 参数2。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 返回值。


////

///


/// define
`getRedstonePower`


///

```js
getRedstonePower(): int32 | undefined
```

/// html | div.result

///


/// define
`getTags`


///

```js
getTags(): string[]
```

/// html | div.result

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
`isValid`


///

```js
isValid(): boolean
```

/// html | div.result

///


/// define
`matches`


///

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- 参数1。


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`north`


///

```js
north(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`offset`


///

```js
offset(offset: Vector3): Block | undefined
```

/// html | div.result
//// define
`offset`：[`Vector3`](./vector3.md)

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`setPermutation`


///

```js
setPermutation(permutation: BlockPermutation): void
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setType`


///

```js
setType(blockType: BlockType | string): void
```

/// html | div.result
//// define
`blockType`：BlockType|string

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`setWaterlogged`


///

```js
setWaterlogged(isWaterlogged: boolean): void
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`south`


///

```js
south(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///


/// define
`trySetPermutation`


///

```js
trySetPermutation(permutation: BlockPermutation): boolean
```

/// html | div.result
//// define
`permutation`：[`BlockPermutation`](./blockpermutation.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`west`


///

```js
west(steps: int32): Block | undefined
```

/// html | div.result
//// define
`steps`：`int32`

- 参数1。


////

//// define
返回值：[`Block`](./block.md)|`undefined`

- 返回值。


////

///

