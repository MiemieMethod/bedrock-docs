# `Block`

> 文档版本：1.21.50.25

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

