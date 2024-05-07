# `BlockPermutation`

> 文档版本：1.21.0.24

`BlockPermutation`类。代表方块的置换。

## 方法

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

