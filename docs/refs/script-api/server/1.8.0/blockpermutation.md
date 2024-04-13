# `BlockPermutation`

> 文档版本：1.21.0.21

`BlockPermutation`类。script_api.@minecraft/server.blockpermutation.description

## 方法

/// define
`getState`


///

script_api.@minecraft/server.blockpermutation.getstate.description

```js
getState(stateName: string): boolean | int32 | string | undefined
```

/// html | div.result
//// define
`stateName`：`string`

- script_api.@minecraft/server.blockpermutation.getstate.statename.description


////

//// define
返回值：`boolean`|`int32`|`string`|`undefined`

- script_api.@minecraft/server.blockpermutation.getstate.return


////

///


/// define
`matches`


///

script_api.@minecraft/server.blockpermutation.matches.description

```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```

/// html | div.result
//// define
`blockName`：`string`

- script_api.@minecraft/server.blockpermutation.matches.blockname.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.matches.states.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server.blockpermutation.matches.return


////

///


/// define
`resolve`


///

script_api.@minecraft/server.blockpermutation.resolve.description

```js
static resolve(blockName: string, states?: Record<string, boolean | int32 | string>): BlockPermutation
```

/// html | div.result
//// define
`blockName`：`string`

- script_api.@minecraft/server.blockpermutation.resolve.blockname.description


////

//// define
`states`：`Record<string, boolean | int32 | string>`|`undefined`

- script_api.@minecraft/server.blockpermutation.resolve.states.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.blockpermutation.resolve.return


////

///


/// define
`withState`


///

script_api.@minecraft/server.blockpermutation.withstate.description

```js
withState(name: string, value: boolean | int32 | string): BlockPermutation
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server.blockpermutation.withstate.name.description


////

//// define
`value`：`boolean`|`int32`|`string`

- script_api.@minecraft/server.blockpermutation.withstate.value.description


////

//// define
返回值：[`BlockPermutation`](./blockpermutation.md)

- script_api.@minecraft/server.blockpermutation.withstate.return


////

///

