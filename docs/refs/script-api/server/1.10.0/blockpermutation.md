# `BlockPermutation`

> 文档版本：1.21.50.25

`BlockPermutation`类。代表方块的置换。

## 方法

/// define
`getAllStates`


///

获取该置换中包含的所有可用的方块状态。

```js
getAllStates(): Record<string, boolean | int32 | string>
```

/// html | div.result
//// define
返回值：`Record<string, boolean | int32 | string>`

- 一个记录了该置换所有可用方块状态的对象。


////

///


/// define
`getItemStack`


///

创建一个基于该方块置换的物品堆叠。

```js
getItemStack(amount: int32): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`＝`1`∈[`1`, `255`]

- 该物品堆叠所含物品的数量。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 创建出的物品堆叠对象。


////

///


/// define
`getState`


///

获取该置换中一个指定的方块状态。

```js
getState(stateName: string): boolean | int32 | string | undefined
```

/// html | div.result
//// define
`stateName`：`string`

- 要获取的状态的标识符。


////

//// define
返回值：`boolean`|`int32`|`string`|`undefined`

- 如果该置换含有这个状态，返回此状态的值，否则返回`undefined`。


////

///


/// define
`matches`


///

测试该置换的内容是否与给定内容相同。若不传入方块状态，则只对方块类型进行测试。

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- 要测试的方块类型的名称。


////

//// define
`states`?：`Record<string, boolean | int32 | string>`＝`null`

- 要测试的方块状态。


////

//// define
返回值：`boolean`

- 如果该置换的内容与给定内容相同，返回`true`。


////

///


/// define
`resolve`


///

根据方块名称和方块状态创建一个方块置换。

```js
static resolve(blockName: string, states?: Record<string, boolean | int32 | string>): BlockPermutation
```

/// html | div.result
//// define
`blockName`：`string`

- 置换中的方块类型的名称。


////

//// define
`states`?：`Record<string, boolean | int32 | string>`＝`null`

- 置换中的方块状态。


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- 创建出的方块置换。


////

///


/// define
`withState`


///

通过修改指定方块状态创建一个派生自该置换的方块置换。

```js
withState(name: string, value: boolean | int32 | string): BlockPermutation
```

/// html | div.result
//// define
`name`：`string`

- 派生置换中要修改的方块状态的标识符。


////

//// define
`value`：`boolean`|`int32`|`string`

- 派生置换中要修改的方块状态的值。


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- 创建出的派生置换。


////

///

