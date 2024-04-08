# `Block`

> 文档版本：1.21.0.20

`Block`类。

## 属性

/// define
`dimension`


///

```js
read-only dimension: Dimension
```


/// define
`isAir`


///

```js
read-only isAir: boolean
```


/// define
`isLiquid`


///

```js
read-only isLiquid: boolean
```


/// define
`isSolid`


///

```js
read-only isSolid: boolean
```


/// define
`isWaterlogged`


///

```js
read-only isWaterlogged: boolean
```


/// define
`location`


///

```js
read-only location: Vector3
```


/// define
`permutation`


///

```js
read-only permutation: BlockPermutation
```


/// define
`type`


///

```js
read-only type: BlockType
```


/// define
`typeId`


///

```js
read-only typeId: string
```


/// define
`x`


///

```js
read-only x: int32
```


/// define
`y`


///

```js
read-only y: int32
```


/// define
`z`


///

```js
read-only z: int32
```


## 方法

/// define
`above`


///

```js
above(steps: int32): Block | undefined
```


/// define
`below`


///

```js
below(steps: int32): Block | undefined
```


/// define
`bottomCenter`


///

```js
bottomCenter(): Vector3
```


/// define
`canPlace`


///

```js
canPlace(blockToPlace: BlockPermutation | BlockType | string, faceToPlaceOn?: Direction): boolean
```


/// define
`center`


///

```js
center(): Vector3
```


/// define
`east`


///

```js
east(steps: int32): Block | undefined
```


/// define
`getComponent`


///

```js
getComponent(componentId: string): BlockComponent | undefined
```


/// define
`getItemStack`


///

```js
getItemStack(amount: int32, withData: boolean): ItemStack | undefined
```


/// define
`getRedstonePower`


///

```js
getRedstonePower(): int32 | undefined
```


/// define
`getTags`


///

```js
getTags(): string[]
```


/// define
`hasTag`


///

```js
hasTag(tag: string): boolean
```


/// define
`isValid`


///

```js
isValid(): boolean
```


/// define
`matches`


///

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```


/// define
`north`


///

```js
north(steps: int32): Block | undefined
```


/// define
`offset`


///

```js
offset(offset: Vector3): Block | undefined
```


/// define
`setPermutation`


///

```js
setPermutation(permutation: BlockPermutation): void
```


/// define
`setType`


///

```js
setType(blockType: BlockType | string): void
```


/// define
`setWaterlogged`


///

```js
setWaterlogged(isWaterlogged: boolean): void
```


/// define
`south`


///

```js
south(steps: int32): Block | undefined
```


/// define
`trySetPermutation`


///

```js
trySetPermutation(permutation: BlockPermutation): boolean
```


/// define
`west`


///

```js
west(steps: int32): Block | undefined
```

