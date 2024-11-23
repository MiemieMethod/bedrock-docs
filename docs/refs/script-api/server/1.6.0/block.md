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
