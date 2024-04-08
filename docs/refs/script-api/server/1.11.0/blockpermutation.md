# `BlockPermutation`

> 文档版本：1.21.0.20

`BlockPermutation`类。

## 方法

/// define
`getAllStates`


///

```js
getAllStates(): Record<string, boolean | int32 | string>
```

/// html | div.result
//// define
返回值：`Record<string, boolean | int32 | string>`

- 返回值。


////

///


/// define
`getItemStack`


///

```js
getItemStack(amount: int32): ItemStack | undefined
```

/// html | div.result
//// define
`amount`：`int32`

- 参数1。


////

//// define
返回值：[`ItemStack`](./itemstack.md)|`undefined`

- 返回值。


////

///


/// define
`getState`


///

```js
getState(stateName: string): boolean | int32 | string | undefined
```

/// html | div.result
//// define
`stateName`：`string`

- 参数1。


////

//// define
返回值：`boolean`|`int32`|`string`|`undefined`

- 返回值。


////

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
`resolve`


///

```js
static resolve(blockName: string, states?: Record<string, boolean | int32 | string>): BlockPermutation
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
返回值：[`BlockPermutation`](./blockpermutation.md)

- 返回值。


////

///


/// define
`withState`


///

```js
withState(name: string, value: boolean | int32 | string): BlockPermutation
```

/// html | div.result
//// define
`name`：`string`

- 参数1。


////

//// define
`value`：`boolean`|`int32`|`string`

- 参数2。


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- 返回值。


////

///

