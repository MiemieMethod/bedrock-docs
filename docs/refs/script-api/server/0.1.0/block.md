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

/// html | div.result
//// define
`dimension`：[`Dimension`](./dimension.md)

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
`isEmpty`


///

```js
read-only isEmpty: boolean;
```

/// html | div.result
//// define
`isEmpty`：`boolean`

- 属性。


////

///


/// define
`isWaterlogged`


///

```js
isWaterlogged: boolean;
```

/// html | div.result
//// define
`isWaterlogged`：`boolean`

- 属性。


////

///


/// define
`location`


///

```js
read-only location: BlockLocation;
```

/// html | div.result
//// define
`location`：[`BlockLocation`](./blocklocation.md)

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


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

- 属性。


////

///


## 方法

/// define
`getComponent`


///

```js
getComponent(componentName: string): BlockComponent | undefined
```

/// html | div.result
//// define
`componentName`：`string`

- 参数1。


////

//// define
返回值：[`BlockComponent`](./blockcomponent.md)|`undefined`

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
setType(blockType: BlockType): void
```

/// html | div.result
//// define
`blockType`：[`BlockType`](./blocktype.md)

- 参数1。


////

//// define
返回值：`void`

- 返回值。


////

///

